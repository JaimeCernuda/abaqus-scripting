#!/usr/bin/env python
"""Download abqpy documentation for offline reference.

This script fetches the abqpy API documentation and converts it to markdown
for use by Claude Code skills.

Usage:
    uv run .claude/skills/abaqus-docs/scripts/download_abqpy_docs.py
    uv run .claude/skills/abaqus-docs/scripts/download_abqpy_docs.py --force  # Overwrite existing

Dependencies:
    uv add crawl4ai httpx beautifulsoup4 markdownify
"""

from __future__ import annotations

import argparse
import asyncio
import json
import re
from pathlib import Path
from typing import Any

# Try crawl4ai first, fall back to httpx+bs4
HAS_CRAWL4AI = False
HAS_HTTPX = False
AsyncWebCrawler = None

try:
    from crawl4ai import AsyncWebCrawler
    HAS_CRAWL4AI = True
except Exception as e:
    print(f"crawl4ai not available: {e}")

try:
    import httpx
    from bs4 import BeautifulSoup
    from markdownify import markdownify
    HAS_HTTPX = True
except Exception as e:
    print(f"httpx fallback not available: {e}")


# Documentation URLs
BASE_URL = "https://hailin.wang/abqpy/en/2025/reference"

# Modules to download (correct URL structure as of 2025)
MODULES = {
    "mdb": f"{BASE_URL}/mdb/index.html",
    "mdb_model": f"{BASE_URL}/mdb/model/index.html",
    "odb": f"{BASE_URL}/odb.html",
    "part": f"{BASE_URL}/mdb/model/part_assembly/part.html",
    "sketcher": f"{BASE_URL}/mdb/model/sketcher.html",
    "assembly": f"{BASE_URL}/mdb/model/part_assembly/assembly.html",
    "material": f"{BASE_URL}/mdb/model/material.html",
    "property": f"{BASE_URL}/mdb/model/property.html",
    "mesh": f"{BASE_URL}/mdb/model/mesh.html",
    "step": f"{BASE_URL}/mdb/model/step/index.html",
    "load": f"{BASE_URL}/mdb/model/load.html",
    "bc": f"{BASE_URL}/mdb/model/bc.html",
    "interaction": f"{BASE_URL}/mdb/model/interaction.html",
    "amplitude": f"{BASE_URL}/mdb/model/amplitude.html",
    "field": f"{BASE_URL}/mdb/model/field.html",
    "output": f"{BASE_URL}/mdb/model/output.html",
    "optimization": f"{BASE_URL}/mdb/model/optimization.html",
    "job": f"{BASE_URL}/mdb/job.html",
}

# Output directory
OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "docs" / "abaqus-api"


async def fetch_with_crawl4ai(url: str) -> str | None:
    """Fetch a URL using crawl4ai."""
    if AsyncWebCrawler is None:
        return None
    try:
        async with AsyncWebCrawler() as crawler:
            result = await crawler.arun(url=url)
            return result.markdown if result else None
    except Exception as e:
        print(f"  crawl4ai error for {url}: {e}")
        return None


async def fetch_with_httpx(url: str) -> str | None:
    """Fetch a URL using httpx and convert to markdown."""
    try:
        async with httpx.AsyncClient(follow_redirects=True, timeout=30.0) as client:
            response = await client.get(url)
            response.raise_for_status()
            html = response.text

            # Parse with BeautifulSoup
            soup = BeautifulSoup(html, "html.parser")

            # Extract main content (abqpy uses Sphinx)
            content = soup.find("div", class_="document") or soup.find("main") or soup.body

            if content:
                # Remove navigation, sidebar, etc.
                for nav in content.find_all(["nav", "aside"]):
                    nav.decompose()
                for cls in ["sphinxsidebar", "sidebar", "related", "footer"]:
                    for el in content.find_all(class_=cls):
                        el.decompose()

                # Convert to markdown
                md = markdownify(str(content), heading_style="ATX", code_language="python")
                return md
            return None
    except Exception as e:
        print(f"  httpx error for {url}: {e}")
        return None


async def fetch_url(url: str) -> str | None:
    """Fetch a URL and return markdown content."""
    if HAS_CRAWL4AI:
        content = await fetch_with_crawl4ai(url)
        if content:
            return content

    if HAS_HTTPX:
        return await fetch_with_httpx(url)

    print("  ERROR: No fetcher available. Install crawl4ai or httpx+beautifulsoup4+markdownify")
    return None


def clean_markdown(md: str) -> str:
    """Clean up markdown content."""
    # Remove excessive blank lines
    md = re.sub(r"\n{3,}", "\n\n", md)

    # Remove navigation links
    md = re.sub(r"\[(?:Next|Previous|Index)\]\([^)]+\)", "", md)

    # Fix code blocks
    md = re.sub(r"```\s*\n```", "", md)

    return md.strip()


async def download_module(name: str, url: str, output_dir: Path, force: bool = False) -> dict[str, Any] | None:
    """Download a single module's documentation."""
    output_file = output_dir / "modules" / f"{name}.md"

    if output_file.exists() and not force:
        print(f"  Skipping {name} (exists, use --force to overwrite)")
        return {
            "name": name,
            "file": str(output_file.relative_to(output_dir)),
            "url": url,
            "status": "skipped"
        }

    print(f"  Fetching {name}...")
    content = await fetch_url(url)

    if content:
        content = clean_markdown(content)

        # Add header
        header = f"""# Abaqus {name.upper()} Module API Reference

> Source: [{url}]({url})
> Downloaded for offline use by Claude Code skills.

---

"""
        content = header + content

        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(content, encoding="utf-8")

        print(f"    Saved: {output_file.name} ({len(content)} chars)")
        return {
            "name": name,
            "file": str(output_file.relative_to(output_dir)),
            "url": url,
            "status": "downloaded",
            "size": len(content)
        }
    else:
        print(f"    FAILED: Could not fetch {name}")
        return {
            "name": name,
            "url": url,
            "status": "failed"
        }


async def download_all(force: bool = False) -> None:
    """Download all module documentation."""
    print("\n" + "=" * 60)
    print("Downloading abqpy Documentation")
    print("=" * 60)

    output_dir = OUTPUT_DIR
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "modules").mkdir(exist_ok=True)

    print(f"\nOutput directory: {output_dir}")
    print(f"Force overwrite: {force}")
    print(f"Modules to download: {len(MODULES)}")

    if not HAS_CRAWL4AI and not HAS_HTTPX:
        print("\nERROR: No HTTP library available!")
        print("Install dependencies with:")
        print("  uv add crawl4ai httpx beautifulsoup4 markdownify")
        return

    print(f"\nUsing: {'crawl4ai' if HAS_CRAWL4AI else 'httpx+beautifulsoup4'}")
    print()

    # Download all modules
    index: dict[str, Any] = {
        "version": "2025",
        "source": BASE_URL,
        "modules": {}
    }

    for name, url in MODULES.items():
        result = await download_module(name, url, output_dir, force)
        if result:
            index["modules"][name] = result

    # Write index file
    index_file = output_dir / "index.json"
    index_file.write_text(json.dumps(index, indent=2), encoding="utf-8")
    print(f"\nIndex saved: {index_file}")

    # Write README
    readme = output_dir / "README.md"
    readme_content = """# Abaqus API Documentation

Local copy of the abqpy API documentation for Claude Code skills.

## Source

Downloaded from: https://hailin.wang/abqpy/en/2025/reference/

## Modules

| Module | Description | File |
|--------|-------------|------|
"""

    module_descriptions = {
        "mdb": "Model Database - core model operations",
        "mdb_model": "Model object and methods",
        "odb": "Output Database - results access",
        "part": "Part creation and features",
        "sketcher": "2D sketch operations",
        "assembly": "Instance and assembly operations",
        "material": "Material definitions",
        "property": "Section properties",
        "mesh": "Meshing operations",
        "step": "Analysis step types",
        "load": "Load definitions",
        "bc": "Boundary conditions",
        "interaction": "Contact and connectors",
        "amplitude": "Time-varying definitions",
        "field": "Initial/predefined fields",
        "output": "Output requests",
        "optimization": "Tosca optimization",
        "job": "Job management",
    }

    for name, info in index["modules"].items():
        desc = module_descriptions.get(name, "")
        file_link = info.get("file", "N/A")
        readme_content += f"| {name} | {desc} | [{file_link}]({file_link}) |\n"

    readme_content += """
## Usage

Reference these docs from skill files:
```markdown
For detailed API, see:
- [Material API](modules/material.md)
- [Step API](modules/step.md)
```

Search with grep:
```bash
grep -r "Elastic" .claude/docs/abaqus-api/
```

## Updating

Re-run the download script:
```bash
uv run .claude/skills/abaqus-docs/scripts/download_abqpy_docs.py --force
```
"""
    readme.write_text(readme_content, encoding="utf-8")
    print(f"README saved: {readme}")

    # Summary
    downloaded = sum(1 for m in index["modules"].values() if m.get("status") == "downloaded")
    skipped = sum(1 for m in index["modules"].values() if m.get("status") == "skipped")
    failed = sum(1 for m in index["modules"].values() if m.get("status") == "failed")

    print("\n" + "=" * 60)
    print("Download Complete")
    print("=" * 60)
    print(f"  Downloaded: {downloaded}")
    print(f"  Skipped: {skipped}")
    print(f"  Failed: {failed}")
    print()


def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Download abqpy documentation")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    args = parser.parse_args()

    asyncio.run(download_all(force=args.force))


if __name__ == "__main__":
    main()
