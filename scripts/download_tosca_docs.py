"""Download Tosca Structure documentation as markdown with images.

Uses the ?read= endpoint to discover all articles, then fetches each
individual .htm page (static HTML) and converts to markdown.
"""

import asyncio
import re
import urllib.parse
from pathlib import Path

import httpx
from bs4 import BeautifulSoup, Tag
from markdownify import markdownify as md

BASE_URL = "https://docs.software.vt.edu/abaqusv2025/English"
OUTPUT_DIR = Path("reference/tosca_docs")

GUIDES = {
    "user_guide": {
        "map": "TsoUserMap",
        "title": "Tosca Structure User Guide",
    },
    "commands_guide": {
        "map": "TsoCmdMap",
        "title": "Tosca Structure Commands Guide",
    },
    "examples_guide": {
        "map": "TsoExampleMap",
        "title": "Tosca Structure Examples Guide",
    },
}

# Rate limiting
CONCURRENT_REQUESTS = 5
DELAY_BETWEEN_BATCHES = 0.5


def parse_toc_html(html: str, map_name: str) -> list[dict[str, str]]:
    """Parse the TOC HTML from ?read= endpoint into a list of articles."""
    soup = BeautifulSoup(html, "html.parser")
    articles: list[dict[str, str]] = []
    seen_hrefs: set[str] = set()

    for li in soup.find_all("li"):
        href = li.get("data-href", "")
        title = li.get("title", "")
        if not href or not title:
            continue

        # Skip anchor-only references (subsections of the same page)
        if "#" in href:
            continue

        if href in seen_hrefs:
            continue
        seen_hrefs.add(href)

        articles.append(
            {
                "href": href,
                "title": title,
                "parent": li.get("data-parent", map_name),
                "url": f"{BASE_URL}/{map_name}/{href}",
            }
        )

    return articles


def html_to_markdown(html: str, page_url: str) -> tuple[str, list[dict[str, str]]]:
    """Convert HTML content to markdown and extract image URLs.

    Returns (markdown_text, list of {src, filename} dicts for images).
    """
    soup = BeautifulSoup(html, "html.parser")

    # Find the main content - it's in a <table class="table1"> typically
    content = soup.find("table", class_="table1")
    if not content:
        content = soup.find("body")
    if not content:
        return "", []

    # Extract images
    images: list[dict[str, str]] = []
    if isinstance(content, Tag):
        for img in content.find_all("img"):
            src = img.get("src", "")
            if not src:
                continue

            # Resolve relative URLs
            abs_url = urllib.parse.urljoin(page_url, src)
            filename = Path(urllib.parse.urlparse(abs_url).path).name

            images.append({"src": abs_url, "filename": filename})

            # Update img src to point to local images directory
            img["src"] = f"images/{filename}"

    # Remove script tags
    if isinstance(content, Tag):
        for script in content.find_all("script"):
            script.decompose()
        for style in content.find_all("style"):
            style.decompose()

    # Convert to markdown
    markdown = md(str(content), heading_style="ATX", strip=["a"])

    # Clean up excessive whitespace
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    markdown = markdown.strip()

    return markdown, images


async def fetch_toc(client: httpx.AsyncClient, map_name: str) -> str:
    """Fetch the TOC HTML for a given map."""
    url = f"{BASE_URL}/?read={map_name}"
    resp = await client.get(url)
    resp.raise_for_status()
    return resp.text


async def fetch_page(
    client: httpx.AsyncClient, url: str, semaphore: asyncio.Semaphore
) -> str:
    """Fetch a single page with rate limiting."""
    async with semaphore:
        resp = await client.get(url)
        resp.raise_for_status()
        return resp.text


async def download_image(
    client: httpx.AsyncClient,
    url: str,
    dest: Path,
    semaphore: asyncio.Semaphore,
) -> bool:
    """Download an image file."""
    if dest.exists():
        return True
    async with semaphore:
        try:
            resp = await client.get(url)
            resp.raise_for_status()
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(resp.content)
            return True
        except Exception as e:
            print(f"    Failed to download image {url}: {e}")
            return False


async def process_guide(
    client: httpx.AsyncClient,
    guide_key: str,
    guide_info: dict[str, str],
) -> None:
    """Process a complete guide: fetch TOC, download all articles and images."""
    map_name = guide_info["map"]
    guide_title = guide_info["title"]
    guide_dir = OUTPUT_DIR / guide_key

    print(f"\n{'='*60}")
    print(f"Processing: {guide_title}")
    print(f"{'='*60}")

    # Fetch TOC
    print(f"  Fetching TOC from ?read={map_name}...")
    toc_html = await fetch_toc(client, map_name)
    articles = parse_toc_html(toc_html, map_name)
    print(f"  Found {len(articles)} articles")

    # Create output directory
    guide_dir.mkdir(parents=True, exist_ok=True)
    images_dir = guide_dir / "images"
    images_dir.mkdir(exist_ok=True)

    # Fetch all pages
    semaphore = asyncio.Semaphore(CONCURRENT_REQUESTS)
    all_images: list[dict[str, str]] = []

    # Process in batches
    for i, article in enumerate(articles):
        url = article["url"]
        title = article["title"]
        href = article["href"]
        safe_name = re.sub(r"[^\w\-.]", "_", href.replace(".htm", ""))

        try:
            html = await fetch_page(client, url, semaphore)
            markdown_text, page_images = html_to_markdown(html, url)

            if markdown_text:
                md_path = guide_dir / f"{safe_name}.md"
                md_path.write_text(
                    f"# {title}\n\n{markdown_text}", encoding="utf-8"
                )
                all_images.extend(page_images)

            if (i + 1) % 20 == 0:
                print(f"  Processed {i + 1}/{len(articles)} articles...")

        except Exception as e:
            print(f"  Error processing {title} ({url}): {e}")

    print(f"  Processed all {len(articles)} articles")

    # Download all images
    unique_images = {img["src"]: img for img in all_images}
    print(f"  Downloading {len(unique_images)} unique images...")

    image_tasks = []
    for img_info in unique_images.values():
        dest = images_dir / img_info["filename"]
        image_tasks.append(download_image(client, img_info["src"], dest, semaphore))

    results = await asyncio.gather(*image_tasks)
    downloaded = sum(1 for r in results if r)
    print(f"  Downloaded {downloaded}/{len(unique_images)} images")

    # Create an index file
    index_lines = [f"# {guide_title}\n"]
    for article in articles:
        safe_name = re.sub(r"[^\w\-.]", "_", article["href"].replace(".htm", ""))
        index_lines.append(f"- [{article['title']}]({safe_name}.md)")

    index_path = guide_dir / "INDEX.md"
    index_path.write_text("\n".join(index_lines), encoding="utf-8")
    print(f"  Created INDEX.md")


async def main() -> None:
    print("Tosca Structure Documentation Downloader")
    print(f"Output directory: {OUTPUT_DIR.resolve()}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    async with httpx.AsyncClient(
        timeout=30.0,
        follow_redirects=True,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        },
    ) as client:
        for guide_key, guide_info in GUIDES.items():
            await process_guide(client, guide_key, guide_info)

    print(f"\nDone! Documentation saved to {OUTPUT_DIR.resolve()}")


if __name__ == "__main__":
    asyncio.run(main())
