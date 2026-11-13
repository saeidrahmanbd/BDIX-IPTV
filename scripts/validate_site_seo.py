#!/usr/bin/env python3
"""Validate public BDIX-IPTV website SEO essentials.

Standard-library-only checks for metadata, canonical and hreflang URLs,
structured data, internal links, sitemaps, and the IndexNow verification key.
"""

from __future__ import annotations

from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
BASE = "https://saeidrahmanbd.github.io/BDIX-IPTV/"
PAGES = {
    "index.html": {
        "canonical": BASE,
        "hreflang": {
            "en": BASE,
            "bn": BASE + "bangla-iptv.html",
            "x-default": BASE,
        },
    },
    "playlists.html": {
        "canonical": BASE + "playlists.html",
        "hreflang": {
            "en": BASE + "playlists.html",
            "x-default": BASE + "playlists.html",
        },
    },
    "playlist-studio.html": {
        "canonical": BASE + "playlist-studio.html",
        "hreflang": {
            "en": BASE + "playlist-studio.html",
            "x-default": BASE + "playlist-studio.html",
        },
    },
    "bangla-iptv.html": {
        "canonical": BASE + "bangla-iptv.html",
        "hreflang": {
            "bn": BASE + "bangla-iptv.html",
            "en": BASE,
            "x-default": BASE,
        },
    },
}
SITEMAP_NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
INDEXNOW_KEY_FILE = DOCS / "4e1c93ab76d25f0881a4b7c3e9d6205f.txt"


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title_parts: list[str] = []
        self.in_title = False
        self.meta: dict[str, str] = {}
        self.canonical = ""
        self.og_url = ""
        self.h1_parts: list[list[str]] = []
        self._h1_current: list[str] | None = None
        self.ids: set[str] = set()
        self.duplicate_ids: set[str] = set()
        self.image_missing_alt: list[str] = []
        self.links: list[str] = []
        self.hreflang: dict[str, str] = {}
        self.schema_blocks: list[str] = []
        self._schema_current: list[str] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        a = {k: (v or "") for k, v in attrs}

        if "id" in a:
            if a["id"] in self.ids:
                self.duplicate_ids.add(a["id"])
            self.ids.add(a["id"])

        if tag == "title":
            self.in_title = True
        elif tag == "meta":
            key = a.get("name") or a.get("property")
            if key:
                self.meta[key.lower()] = a.get("content", "").strip()
            if a.get("property", "").lower() == "og:url":
                self.og_url = a.get("content", "").strip()
        elif tag == "link":
            rel = set(a.get("rel", "").lower().split())
            if "canonical" in rel:
                self.canonical = a.get("href", "").strip()
            if "alternate" in rel and a.get("hreflang") and a.get("href"):
                self.hreflang[a["hreflang"].lower()] = a["href"].strip()
        elif tag == "h1":
            self._h1_current = []
        elif tag == "img":
            if not a.get("alt", "").strip():
                self.image_missing_alt.append(a.get("src", "(unknown image)"))
        elif tag == "script" and a.get("type", "").lower() == "application/ld+json":
            self._schema_current = []

        if tag in {"a", "area"} and a.get("href"):
            self.links.append(a["href"].strip())

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False
        elif tag == "h1" and self._h1_current is not None:
            self.h1_parts.append(self._h1_current)
            self._h1_current = None
        elif tag == "script" and self._schema_current is not None:
            self.schema_blocks.append("".join(self._schema_current))
            self._schema_current = None

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)
        if self._h1_current is not None:
            self._h1_current.append(data)
        if self._schema_current is not None:
            self._schema_current.append(data)

    @property
    def title(self) -> str:
        return " ".join("".join(self.title_parts).split())

    @property
    def h1_count(self) -> int:
        return len(self.h1_parts)


errors = 0
page_summaries: list[tuple[str, str, str]] = []


def fail(message: str) -> None:
    global errors
    errors += 1
    print(f"ERROR: {message}")


def check_page(filename: str, page_config: dict[str, object]) -> None:
    path = DOCS / filename
    if not path.is_file():
        fail(f"Missing public page: docs/{filename}")
        return

    parser = PageParser()
    try:
        parser.feed(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"Could not parse docs/{filename}: {exc}")
        return

    title = parser.title
    description = parser.meta.get("description", "")
    robots = parser.meta.get("robots", "index,follow").lower()
    canonical = str(page_config["canonical"])
    expected_hreflang = page_config["hreflang"]

    if not title:
        fail(f"docs/{filename} has no title.")
    elif len(title) > 75:
        fail(f"docs/{filename} title is too long ({len(title)} characters).")

    if not description:
        fail(f"docs/{filename} has no meta description.")
    elif len(description) > 200:
        fail(f"docs/{filename} meta description is too long ({len(description)} characters).")

    page_summaries.append((filename, title, description))

    if parser.canonical != canonical:
        fail(f"docs/{filename} canonical mismatch: {parser.canonical!r}")
    if parser.og_url != canonical:
        fail(f"docs/{filename} og:url must match its canonical URL.")
    if "noindex" in robots:
        fail(f"docs/{filename} is marked noindex.")
    if parser.h1_count != 1:
        fail(f"docs/{filename} must have exactly one H1; found {parser.h1_count}.")
    if parser.duplicate_ids:
        fail(f"docs/{filename} has duplicate IDs: {sorted(parser.duplicate_ids)}")
    if parser.image_missing_alt:
        fail(f"docs/{filename} has images without alt text: {parser.image_missing_alt}")

    for meta_name in (
        "og:title", "og:description", "og:image", "og:image:alt",
        "twitter:card", "twitter:title", "twitter:description",
        "twitter:image", "twitter:image:alt",
    ):
        if not parser.meta.get(meta_name):
            fail(f"docs/{filename} is missing {meta_name}.")

    if parser.hreflang != expected_hreflang:
        fail(
            f"docs/{filename} hreflang alternates differ from expected values. "
            f"Expected={expected_hreflang}, found={parser.hreflang}"
        )

    if not parser.schema_blocks:
        fail(f"docs/{filename} has no JSON-LD structured data.")
    for index, block in enumerate(parser.schema_blocks, start=1):
        try:
            schema = json.loads(block)
            if not isinstance(schema, dict) or schema.get("@context") != "https://schema.org" or not schema.get("@type"):
                fail(f"docs/{filename} JSON-LD block {index} lacks a Schema.org context or type.")
        except json.JSONDecodeError as exc:
            fail(f"docs/{filename} JSON-LD block {index} is invalid: {exc}")

    for href in parser.links:
        if href.startswith(("#", "mailto:", "tel:", "javascript:")):
            if href.startswith("#") and unquote(href[1:]) not in parser.ids:
                fail(f"docs/{filename} has a broken in-page link: {href}")
            continue

        parsed = urlparse(href)
        if parsed.scheme in {"http", "https"} or href.startswith("//") or parsed.scheme:
            continue

        clean_path = unquote(parsed.path)
        if not clean_path or clean_path in {".", "./"}:
            target = DOCS / "index.html"
        else:
            target = (path.parent / clean_path).resolve()

        try:
            target.relative_to(DOCS.resolve())
        except ValueError:
            fail(f"docs/{filename} has a relative link outside docs/: {href}")
            continue

        if not target.exists():
            fail(f"docs/{filename} has a broken local link: {href}")

    print(f"OK: {filename} — {title}")


for filename, config in PAGES.items():
    check_page(filename, config)

titles = [item[1].casefold() for item in page_summaries]
if len(titles) != len(set(titles)):
    fail("Public pages must have unique title elements.")

descriptions = [item[2].casefold() for item in page_summaries]
if len(descriptions) != len(set(descriptions)):
    fail("Public pages must have unique meta descriptions.")

try:
    tree = ET.parse(DOCS / "sitemap.xml")
    locs = {
        item.text.strip()
        for item in tree.findall(".//sm:loc", SITEMAP_NS)
        if item.text and item.text.strip()
    }
    expected_urls = {str(config["canonical"]) for config in PAGES.values()}
    if locs != expected_urls:
        fail(f"sitemap.xml URLs differ from canonical pages. Missing={sorted(expected_urls-locs)}, extra={sorted(locs-expected_urls)}")
    else:
        print(f"OK: sitemap.xml — {len(locs)} canonical pages")
except (ET.ParseError, OSError) as exc:
    fail(f"sitemap.xml is missing or invalid: {exc}")

try:
    text_urls = {
        line.strip()
        for line in (DOCS / "sitemap.txt").read_text(encoding="utf-8").splitlines()
        if line.strip()
    }
    expected_urls = {str(config["canonical"]) for config in PAGES.values()}
    if text_urls != expected_urls:
        fail(f"sitemap.txt URLs differ from canonical pages. Missing={sorted(expected_urls-text_urls)}, extra={sorted(text_urls-expected_urls)}")
    else:
        print(f"OK: sitemap.txt — {len(text_urls)} canonical pages")
except OSError as exc:
    fail(f"sitemap.txt is missing: {exc}")

try:
    key_value = INDEXNOW_KEY_FILE.read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"[a-fA-F0-9]{8,128}", key_value):
        fail("IndexNow key file must contain an 8–128 character hexadecimal key.")
    else:
        print("OK: IndexNow verification key file")
except OSError as exc:
    fail(f"IndexNow key file is missing: {exc}")

if errors:
    print(f"\nSEO validation failed with {errors} error(s).")
    sys.exit(1)

print("\nSEO validation passed.")
