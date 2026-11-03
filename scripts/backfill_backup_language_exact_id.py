#!/usr/bin/env python3
"""Backfill missing Backup language tags from an exact primary tvg-id match only.

This never changes stream URLs, channel identity, country, channel number, group,
logo, or an already-present language value. Ambiguous/missing source languages
are left unchanged and reported.
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


def insert_before_group(line: str, key: str, value: str) -> str:
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


def backfill_text(text: str):
    lines, rows = parse_records(text)
    original_urls = url_inventory(rows)
    primary_languages = defaultdict(set)
    for _, _, metadata, _ in rows:
        group = metadata.get("group-title", "").strip()
        if group in REVIEW_GROUPS:
            continue
        channel_id = (metadata.get("tvg-id") or metadata.get("channel-id") or "").strip()
        language = metadata.get("tvg-language", "").strip()
        if channel_id and language:
            primary_languages[channel_id].add(language)

    filled = []
    ambiguous = []
    unmatched = []
    for index, info, metadata, _ in rows:
        if metadata.get("group-title", "").strip() != "Backup":
            continue
        if metadata.get("tvg-language", "").strip():
            continue
        channel_id = (metadata.get("tvg-id") or metadata.get("channel-id") or "").strip()
        candidates = primary_languages.get(channel_id, set())
        if len(candidates) == 1:
            language = next(iter(candidates))
            ending = "\r\n" if lines[index].endswith("\r\n") else "\n" if lines[index].endswith("\n") else ""
            lines[index] = insert_before_group(info, "tvg-language", language) + ending
            filled.append((metadata.get("tvg-name", ""), channel_id, language))
        elif len(candidates) > 1:
            ambiguous.append((metadata.get("tvg-name", ""), channel_id, sorted(candidates)))
        else:
            unmatched.append((metadata.get("tvg-name", ""), channel_id))

    updated = "".join(lines)
    _, updated_rows = parse_records(updated)
    if url_inventory(updated_rows) != original_urls:
        raise ValueError("Backup language backfill changed the stream URL inventory.")
    return updated, filled, ambiguous, unmatched


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if a safe language backfill remains")
    args = parser.parse_args()
    if not PLAYLIST.is_file():
        raise SystemExit(f"Playlist not found: {PLAYLIST}")
    before = PLAYLIST.read_text(encoding="utf-8-sig")
    after, filled, ambiguous, unmatched = backfill_text(before)
    if args.check:
        if filled:
            raise SystemExit(f"{len(filled)} exact-ID Backup language tags can still be filled.")
    elif after != before:
        PLAYLIST.write_text(after, encoding="utf-8", newline="")
    print(f"Backup languages filled: {len(filled)}; ambiguous: {len(ambiguous)}; no exact primary match: {len(unmatched)}.")
    if ambiguous:
        print("Ambiguous exact-ID mappings were left untouched.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
