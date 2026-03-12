"""Download full Abaqus documentation as markdown with images and links.

Uses the ?read= endpoint to discover all articles per guide, then fetches
each static .htm page, converts to markdown preserving internal/external links,
and downloads images.
"""

import asyncio
import re
import urllib.parse
from pathlib import Path

import httpx
from bs4 import BeautifulSoup, Tag
from markdownify import MarkdownConverter

BASE_URL = "https://docs.software.vt.edu/abaqusv2025/English"
OUTPUT_DIR = Path("reference/abaqus_docs")

# All 22 Abaqus guides from the documentation tree
GUIDES: dict[str, dict[str, str]] = {
    "release_notes": {
        "map": "SIMACAERNGRefMap",
        "title": "Abaqus Release Notes",
    },
    "introduction_spatial_modeling": {
        "map": "SIMACAEMODRefMap",
        "title": "Abaqus Introduction & Spatial Modeling",
    },
    "cae": {
        "map": "SIMACAECAERefMap",
        "title": "Abaqus/CAE",
    },
    "analysis": {
        "map": "SIMACAEANLRefMap",
        "title": "Analysis",
    },
    "benchmarks": {
        "map": "SIMACAEBMKRefMap",
        "title": "Benchmarks",
    },
    "constraints": {
        "map": "SIMACAECSTRefMap",
        "title": "Constraints",
    },
    "elements": {
        "map": "SIMACAEELMRefMap",
        "title": "Elements",
    },
    "example_problems": {
        "map": "SIMACAEEXARefMap",
        "title": "Example Problems",
    },
    "execution": {
        "map": "SIMACAEEXCRefMap",
        "title": "Execution",
    },
    "getting_started": {
        "map": "SIMACAEGSARefMap",
        "title": "Getting Started with Abaqus/CAE",
    },
    "gui_toolkit": {
        "map": "SIMACAECUSRefMap",
        "title": "GUI Toolkit",
    },
    "gui_toolkit_reference": {
        "map": "SIMACAEGUIRefHtml",
        "title": "GUI Toolkit Reference",
    },
    "interactions": {
        "map": "SIMACAEITNRefMap",
        "title": "Interactions",
    },
    "keywords": {
        "map": "SIMACAEKEYRefMap",
        "title": "Keywords",
    },
    "materials": {
        "map": "SIMACAEMATRefMap",
        "title": "Materials",
    },
    "output": {
        "map": "SIMACAEOUTRefMap",
        "title": "Output",
    },
    "prescribed_conditions": {
        "map": "SIMACAEPRCRefMap",
        "title": "Prescribed Conditions",
    },
    "scripting": {
        "map": "SIMACAECMDRefMap",
        "title": "Scripting",
    },
    "scripting_reference": {
        "map": "SIMACAEKERRefMap",
        "title": "Scripting Reference",
    },
    "theory": {
        "map": "SIMACAETHERefMap",
        "title": "Theory",
    },
    "user_subroutines": {
        "map": "SIMACAESUBRefMap",
        "title": "User Subroutines",
    },
    "verification": {
        "map": "SIMACAEVERRefMap",
        "title": "Verification",
    },
}

CONCURRENT_REQUESTS = 10
CONCURRENT_IMAGES = 15

# Build reverse map: MapName -> guide_key for cross-guide link resolution
MAP_TO_GUIDE: dict[str, str] = {v["map"]: k for k, v in GUIDES.items()}


def parse_toc_html(html: str, map_name: str) -> list[dict[str, str]]:
    """Parse the TOC HTML from ?read= endpoint into a list of unique articles."""
    soup = BeautifulSoup(html, "html.parser")
    articles: list[dict[str, str]] = []
    seen_hrefs: set[str] = set()

    for li in soup.find_all("li"):
        href = li.get("data-href", "")
        title = li.get("title", "")
        if not href or not title:
            continue
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


def _resolve_link(href: str, page_url: str, current_map: str) -> str:
    """Convert an HTML href to a markdown-friendly relative or absolute link."""
    if not href:
        return ""

    # External links — keep as-is
    if href.startswith(("http://", "https://", "mailto:")):
        # Internal VT docs link via ?show= — convert to relative
        if "?show=" in href:
            show_match = re.search(r"\?show=([^#&]+)", href)
            if show_match:
                show_path = show_match.group(1)
                return _show_path_to_md(show_path, current_map)
        return href

    # ?show= relative link
    if href.startswith("?show="):
        show_path = href.split("?show=")[1].split("#")[0]
        return _show_path_to_md(show_path, current_map)

    # Relative .htm link within the same map
    if href.endswith(".htm") or ".htm#" in href:
        base_href = href.split("#")[0]
        anchor = ""
        if "#" in href:
            anchor = "#" + href.split("#", 1)[1]
        safe_name = re.sub(r"[^\w\-.]", "_", base_href.replace(".htm", ""))
        return f"{safe_name}.md{anchor}"

    return href


def _show_path_to_md(show_path: str, current_map: str) -> str:
    """Convert a MapName/page.htm path to a relative markdown link."""
    parts = show_path.split("/", 1)
    if len(parts) == 2:
        target_map, target_page = parts
        base_page = target_page.split("#")[0]
        anchor = ""
        if "#" in target_page:
            anchor = "#" + target_page.split("#", 1)[1]
        safe_name = re.sub(r"[^\w\-.]", "_", base_page.replace(".htm", ""))

        if target_map == current_map:
            return f"{safe_name}.md{anchor}"

        # Cross-guide link
        target_guide = MAP_TO_GUIDE.get(target_map, target_map)
        return f"../{target_guide}/{safe_name}.md{anchor}"

    return show_path


class LinkPreservingConverter(MarkdownConverter):
    """Markdownify converter that preserves links with resolved paths."""

    def __init__(self, page_url: str, current_map: str, **kwargs):
        self.page_url = page_url
        self.current_map = current_map
        super().__init__(**kwargs)

    def convert_a(self, el, text, parent_tags):
        href = el.get("href", "")
        if not href or not text.strip():
            return text
        resolved = _resolve_link(href, self.page_url, self.current_map)
        if resolved:
            return f"[{text.strip()}]({resolved})"
        return text


def html_to_markdown(
    html: str, page_url: str, map_name: str
) -> tuple[str, list[dict[str, str]]]:
    """Convert HTML content to markdown, preserving links and extracting images."""
    soup = BeautifulSoup(html, "html.parser")

    content = soup.find("table", class_="table1")
    if not content:
        content = soup.find("body")
    if not content:
        return "", []

    images: list[dict[str, str]] = []
    if isinstance(content, Tag):
        for img in content.find_all("img"):
            src = img.get("src", "")
            if not src:
                continue
            abs_url = urllib.parse.urljoin(page_url, src)
            filename = Path(urllib.parse.urlparse(abs_url).path).name
            images.append({"src": abs_url, "filename": filename})
            img["src"] = f"images/{filename}"

        for script in content.find_all("script"):
            script.decompose()
        for style in content.find_all("style"):
            style.decompose()

    converter = LinkPreservingConverter(
        page_url=page_url,
        current_map=map_name,
        heading_style="ATX",
    )
    markdown = converter.convert(str(content))

    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    markdown = markdown.strip()

    return markdown, images


async def fetch_toc(client: httpx.AsyncClient, map_name: str) -> str:
    url = f"{BASE_URL}/?read={map_name}"
    resp = await client.get(url)
    resp.raise_for_status()
    return resp.text


async def fetch_page(
    client: httpx.AsyncClient, url: str, semaphore: asyncio.Semaphore
) -> str:
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
            print(f"    Failed: {dest.name} ({e})")
            return False


async def process_guide(
    client: httpx.AsyncClient,
    guide_key: str,
    guide_info: dict[str, str],
    page_semaphore: asyncio.Semaphore,
    image_semaphore: asyncio.Semaphore,
) -> dict[str, int]:
    """Process a complete guide. Returns stats dict."""
    map_name = guide_info["map"]
    guide_title = guide_info["title"]
    guide_dir = OUTPUT_DIR / guide_key

    print(f"\n{'='*60}")
    print(f"Processing: {guide_title} ({map_name})")
    print(f"{'='*60}")

    toc_html = await fetch_toc(client, map_name)
    articles = parse_toc_html(toc_html, map_name)
    print(f"  {len(articles)} unique articles")

    guide_dir.mkdir(parents=True, exist_ok=True)
    images_dir = guide_dir / "images"
    images_dir.mkdir(exist_ok=True)

    all_images: list[dict[str, str]] = []
    errors = 0

    # Process articles with concurrency
    async def process_article(i: int, article: dict[str, str]) -> None:
        nonlocal errors
        url = article["url"]
        href = article["href"]
        safe_name = re.sub(r"[^\w\-.]", "_", href.replace(".htm", ""))
        md_path = guide_dir / f"{safe_name}.md"

        # Skip if already downloaded
        if md_path.exists():
            return

        try:
            html = await fetch_page(client, url, page_semaphore)
            markdown_text, page_images = html_to_markdown(html, url, map_name)
            if markdown_text:
                md_path.write_text(
                    f"# {article['title']}\n\n{markdown_text}", encoding="utf-8"
                )
                all_images.extend(page_images)
        except Exception as e:
            errors += 1
            if errors <= 5:
                print(f"  Error: {article['title'][:50]} ({e})")

    # Process in batches of 50
    batch_size = 50
    for batch_start in range(0, len(articles), batch_size):
        batch = articles[batch_start : batch_start + batch_size]
        tasks = [
            process_article(batch_start + i, article)
            for i, article in enumerate(batch)
        ]
        await asyncio.gather(*tasks)
        done = min(batch_start + batch_size, len(articles))
        print(f"  [{done}/{len(articles)}] articles processed")

    # Download images
    unique_images = {img["src"]: img for img in all_images}
    print(f"  Downloading {len(unique_images)} images...")

    image_tasks = [
        download_image(client, info["src"], images_dir / info["filename"], image_semaphore)
        for info in unique_images.values()
    ]
    results = await asyncio.gather(*image_tasks)
    downloaded = sum(1 for r in results if r)
    print(f"  {downloaded}/{len(unique_images)} images downloaded")

    # Create index
    index_lines = [f"# {guide_title}\n"]
    for article in articles:
        safe_name = re.sub(r"[^\w\-.]", "_", article["href"].replace(".htm", ""))
        index_lines.append(f"- [{article['title']}]({safe_name}.md)")
    (guide_dir / "INDEX.md").write_text("\n".join(index_lines), encoding="utf-8")

    stats = {
        "articles": len(articles),
        "images": downloaded,
        "errors": errors,
    }
    print(f"  Done: {stats}")
    return stats


async def main() -> None:
    print("Abaqus Documentation Downloader")
    print(f"Output: {OUTPUT_DIR.resolve()}")
    print(f"Guides: {len(GUIDES)}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    page_semaphore = asyncio.Semaphore(CONCURRENT_REQUESTS)
    image_semaphore = asyncio.Semaphore(CONCURRENT_IMAGES)

    all_stats: dict[str, dict[str, int]] = {}

    async with httpx.AsyncClient(
        timeout=30.0,
        follow_redirects=True,
        limits=httpx.Limits(max_connections=20, max_keepalive_connections=10),
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        },
    ) as client:
        for guide_key, guide_info in GUIDES.items():
            stats = await process_guide(
                client, guide_key, guide_info, page_semaphore, image_semaphore
            )
            all_stats[guide_key] = stats

    # Print summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    total_articles = 0
    total_images = 0
    total_errors = 0
    for guide_key, stats in all_stats.items():
        title = GUIDES[guide_key]["title"]
        print(f"  {title}: {stats['articles']} articles, {stats['images']} images"
              + (f", {stats['errors']} errors" if stats["errors"] else ""))
        total_articles += stats["articles"]
        total_images += stats["images"]
        total_errors += stats["errors"]
    print(f"\n  TOTAL: {total_articles} articles, {total_images} images, {total_errors} errors")
    print(f"\n  Saved to {OUTPUT_DIR.resolve()}")


if __name__ == "__main__":
    asyncio.run(main())
