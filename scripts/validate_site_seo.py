#!/usr/bin/env python3
"""Validate the public BDIX-IPTV GitHub Pages SEO essentials.

Standard-library-only checks for canonical URLs, metadata, headings, links,
sitemaps, and the IndexNow verification key.
"""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
BASE = "https://saeidrahmanbd.github.io/BDIX-IPTV/"
PAGES = {
    "index.html": BASE,
    "playlists.html": BASE + "playlists.html",
    "bangla-iptv.html": BASE + "bangla-iptv.html",
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
        elif tag == "link":
            rel = set(a.get("rel", "").lower().split())
            if "canonical" in rel:
                self.canonical = a.get("href", "").strip()
            if "alternate" in rel and a.get("hreflang") and a.get("href"):
                self.hreflang[a["hreflang"].lower()] = a["href"]
        elif tag == "h1":
            self._h1_current = []
        elif tag == "img":
            if not a.get("alt", "").strip():
                self.image_missing_alt.append(a.get("src", "(unknown image)"))
        if tag in {"a", "area"} and a.get("href"):
            self.links.append(a["href"].strip())
        if tag == "meta" and a.get("property", "").lower() == "og:url":
            self.og_url = a.get("content", "").strip()

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False
        elif tag == "h1" and self._h1_current is not None:
            self.h1_parts.append(self._h1_current)
            self._h1_current = None

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)
        if self._h1_current is not None:
            self._h1_current.append(data)

    @property
    def title(self) -> str:
        return " ".join("".join(self.title_parts).split())

    @property
    def h1_count(self) -> int:
        return len(self.h1_parts)


errors = 0


def fail(message: str) -> None:
    global errors
    errors += 1
    print(f"ERROR: {message}")


def check_page(filename: str, canonical_url: str) -> None:
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

    if not title:
        fail(f"docs/{filename} has no title.")
    elif len(title) > 75:
        fail(f"docs/{filename} title is too long ({len(title)} characters).")

    if not description:
        fail(f"docs/{filename} has no meta description.")
    elif len(description) > 200:
        fail(f"docs/{filename} meta description is too long ({len(description)} characters).")

    if parser.canonical != canonical_url:
        fail(f"docs/{filename} canonical mismatch: {parser.canonical!r}")
    if parser.og_url != canonical_url:
        fail(f"docs/{filename} og:url must match its canonical URL.")
    if "noindex" in robots:
        fail(f"docs/{filename} is marked noindex.")
    if parser.h1_count != 1:
        fail(f"docs/{filename} must have exactly one H1; found {parser.h1_count}.")
    if parser.duplicate_ids:
        fail(f"docs/{filename} has duplicate IDs: {sorted(parser.duplicate_ids)}")
    if parser.image_missing_alt:
        fail(f"docs/{filename} has images without alt text: {parser.image_missing_alt}")

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

    if title:
        print(f"OK: {filename} — {title}")


for filename, canonical_url in PAGES.items():
    check_page(filename, canonical_url)

try:
    tree = ET.parse(DOCS / "sitemap.xml")
    locs = {
        item.text.strip()
        for item in tree.findall(".//sm:loc", SITEMAP_NS)
        if item.text and item.text.strip()
    }
    expected = set(PAGES.values())
    if locs != expected:
        fail(f"sitemap.xml URLs differ from canonical pages. Missing={sorted(expected-locs)}, extra={sorted(locs-expected)}")
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
    if text_urls != set(PAGES.values()):
        fail(f"sitemap.txt URLs differ from canonical pages. Missing={sorted(set(PAGES.values())-text_urls)}, extra={sorted(text_urls-set(PAGES.values()))}")
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
