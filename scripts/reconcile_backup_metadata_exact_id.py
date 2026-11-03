#!/usr/bin/env python3
"""Reconcile Backup country/language tags from exact primary tvg-id matches only.

A Backup country is corrected only when every canonical primary record with the
same exact tvg-id agrees on one country. Missing Backup language is filled only
when those exact primary records agree on one language. Ambiguous metadata stays
untouched. Stream URLs, identities, display names, groups, logos and channel
numbers are never changed.
"""
from __future__ import annotations

import argparse
import re
from collections import defaultdict
from pathlib import Path

PLAYLIST = Path("IPTV-Playlist.m3u")
ATTR_RE = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
REVIEW_GROUPS = {"Backup", "Not Playing", "New Channels", "New Backup"}


def attrs(line: str) -> dict[str, str]:
    return dict(ATTR_RE.findall(line))


def set_attr(line: str, key: str, value: str) -> str:
    pattern = re.compile(rf'(\s+{re.escape(key)}=")[^"]*(")')
    if pattern.search(line):
        return pattern.sub(lambda match: match.group(1) + value + match.group(2), line, count=1)
    marker = re.search(r'\s+group-title="', line)
    if not marker:
        raise ValueError(f"Missing group-title on EXTINF: {line[:120]}")
    return line[:marker.start()] + f' {key}="{value}"' + line[marker.start():]


def parse_records(text: str):
    lines = text.splitlines(keepends=True)
    rows = []
    current = None
    for index, line in enumerate(lines):
        if line.startswith("#EXTINF:"):
            current = index
        elif current is not None and line.strip().startswith(("http://", "https://")):
            info = lines[current].rstrip("\r\n")
            rows.append((current, info, attrs(info), line.strip()))
            current = None
    return lines, rows


def url_inventory(rows):
    return [row[3] for row in rows]


def reconcile_text(text: str):
    lines, rows = parse_records(text)
    original_urls = url_inventory(rows)
    primary_countries = defaultdict(set)
    primary_languages = defaultdict(set)

    for _, _, metadata, _ in rows:
        if metadata.get("group-title", "").strip() in REVIEW_GROUPS:
            continue
        channel_id = (metadata.get("tvg-id") or metadata.get("channel-id") or "").strip()
        country = metadata.get("tvg-country", "").strip().upper()
        language = metadata.get("tvg-language", "").strip().lower()
        if channel_id and country:
            primary_countries[channel_id].add(country)
        if channel_id and language:
            primary_languages[channel_id].add(language)

    language_filled = []
    country_repaired = []
    ambiguous = []
    unmatched = []

    for index, info, metadata, _ in rows:
        if metadata.get("group-title", "").strip() != "Backup":
            continue
        channel_id = (metadata.get("tvg-id") or metadata.get("channel-id") or "").strip()
        if not channel_id:
            unmatched.append((metadata.get("tvg-name", ""), channel_id))
            continue

        source_countries = primary_countries.get(channel_id, set())
        current_country = metadata.get("tvg-country", "").strip().upper()
        if len(source_countries) == 1:
            source_country = next(iter(source_countries))
            if current_country != source_country:
                info = set_attr(info, "tvg-country", source_country)
                country_repaired.append((metadata.get("tvg-name", ""), channel_id, current_country or "(missing)", source_country))

        if not metadata.get("tvg-language", "").strip():
            source_languages = primary_languages.get(channel_id, set())
            if len(source_languages) == 1:
                language = next(iter(source_languages))
                info = set_attr(info, "tvg-language", language)
                language_filled.append((metadata.get("tvg-name", ""), channel_id, language))
            elif len(source_languages) > 1:
                ambiguous.append((metadata.get("tvg-name", ""), channel_id, sorted(source_languages)))
            else:
                unmatched.append((metadata.get("tvg-name", ""), channel_id))

        ending = "\r\n" if lines[index].endswith("\r\n") else "\n" if lines[index].endswith("\n") else ""
        lines[index] = info + ending

    updated = "".join(lines)
    _, updated_rows = parse_records(updated)
    if url_inventory(updated_rows) != original_urls:
        raise ValueError("Backup metadata reconciliation changed the stream URL inventory.")
    return updated, language_filled, country_repaired, ambiguous, unmatched


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if an exact-ID Backup metadata repair remains")
    args = parser.parse_args()
    if not PLAYLIST.is_file():
        raise SystemExit(f"Playlist not found: {PLAYLIST}")
    before = PLAYLIST.read_text(encoding="utf-8-sig")
    after, language_filled, country_repaired, ambiguous, unmatched = reconcile_text(before)
    if args.check:
        if language_filled or country_repaired:
            raise SystemExit(
                f"Backup metadata repairs remain: {len(language_filled)} language and {len(country_repaired)} country."
            )
    elif after != before:
        PLAYLIST.write_text(after, encoding="utf-8", newline="")
    print(
        f"Backup metadata reconciled: {len(language_filled)} language tags filled; "
        f"{len(country_repaired)} country tags corrected; "
        f"{len(ambiguous)} ambiguous; {len(unmatched)} without an exact primary match."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
