#!/usr/bin/env python3
"""Preserve curated IPTV row order and assign contiguous channel numbers in place.

Backup, Review, New Channels and New Backups remain unnumbered. Legacy Not Playing
rows are normalized to Review; stream URLs are never rewritten.
"""
from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path

CATEGORY_ORDER = [
    "Bangladesh", "Indian Bangla", "Indian Movies", "Indian Music",
    "Indian Entertainment", "Pakistani", "International",
    "Documentary & Wildlife", "Kids", "Religious", "Sports",
    "Backup", "New Channels", "New Backups", "Review",
]
CATEGORY_RANK = {name: index for index, name in enumerate(CATEGORY_ORDER)}
REVIEW_GROUPS = {"Backup", "Review", "Not Playing", "New Channels", "New Backups"}
ATTR_RE = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')


def attrs(info: str) -> dict[str, str]:
    return dict(ATTR_RE.findall(info))


def natural_key(value: str):
    value = unicodedata.normalize("NFKD", str(value or "")).casefold().strip()
    return tuple(int(part) if part.isdigit() else part for part in re.split(r"(\d+)", value))


def display_name(record: list[str]) -> str:
    metadata = attrs(record[0])
    return metadata.get("tvg-name", "").strip() or record[0].rsplit(",", 1)[-1].strip()


def stream_url(record: list[str]) -> str:
    return next((line.strip() for line in record[1:] if line.strip().startswith(("http://", "https://"))), "")


def set_channel_number(info: str, number: int) -> str:
    replacement = f'tvg-chno="{number}"'
    if re.search(r'\s+tvg-chno="[^"]*"', info):
        return re.sub(r'\s+tvg-chno="[^"]*"', " " + replacement, info, count=1)
    match = re.search(r'\s+group-title="', info)
    if match:
        return info[:match.start()] + " " + replacement + info[match.start():]
    comma = info.find(",")
    if comma >= 0:
        return info[:comma] + " " + replacement + info[comma:]
    raise ValueError(f"Cannot insert tvg-chno into malformed EXTINF: {info[:120]}")


def remove_channel_number(info: str) -> str:
    return re.sub(r'\s+tvg-chno="[^"]*"', "", info, count=1)


def parse_records(text: str):
    lines = text.splitlines()
    preamble: list[str] = []
    records: list[list[str]] = []
    current: list[str] | None = None
    for line in lines:
        if line.startswith("#EXTINF:"):
            if current is not None:
                records.append(current)
            current = [line]
        elif current is None:
            preamble.append(line)
        else:
            current.append(line)
    if current is not None:
        records.append(current)
    return preamble, records


def url_inventory(records: list[list[str]]) -> list[str]:
    return [url for url in (stream_url(record) for record in records) if url]


def normalize_playlist_text(text: str) -> tuple[str, int]:
    newline = "\r\n" if "\r\n" in text else "\n"
    had_final_newline = text.endswith(("\n", "\r"))
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    preamble, records = parse_records(normalized)
    # Keep Playlist Studio's category registry aligned with the canonical
    # UI order. This does not authorize moving any playlist record.
    registry_prefix = "#PLAYLIST-STUDIO-CATEGORIES:"
    registry_positions = [i for i, line in enumerate(preamble) if line.startswith(registry_prefix)]
    if len(registry_positions) > 1:
        raise ValueError("Multiple category registries; refusing ambiguous rewrite.")
    registry_line = registry_prefix + json.dumps(CATEGORY_ORDER, ensure_ascii=False)
    if registry_positions:
        preamble[registry_positions[0]] = registry_line
    else:
        header_index = next((i + 1 for i, line in enumerate(preamble) if line.startswith("#EXTM3U")), len(preamble))
        preamble.insert(header_index, registry_line)
    original_urls = url_inventory(records)
    for record in records:
        if attrs(record[0]).get("group-title", "").strip() == "Not Playing":
            record[0] = re.sub(r'group-title="Not Playing"', 'group-title="Review"', record[0], count=1)
    primary = []
    review = []
    for record in records:
        group = attrs(record[0]).get("group-title", "").strip()
        if group in REVIEW_GROUPS:
            review.append(record)
        else:
            if group not in CATEGORY_RANK:
                raise ValueError(f"Unknown IPTV category; refusing to reorder: {group!r}")
            primary.append(record)

    # Preserve every existing primary channel number. Fill only missing/invalid
    # primary numbers with the lowest unused positive integers; this repairs gaps
    # without renumbering the owner's already-numbered channels.
    used_numbers = set()
    for record in primary:
        raw = attrs(record[0]).get("tvg-chno", "").strip()
        if raw.isdigit() and int(raw) > 0:
            used_numbers.add(int(raw))
    next_number = 1
    for record in primary:
        raw = attrs(record[0]).get("tvg-chno", "").strip()
        if raw.isdigit() and int(raw) > 0:
            continue
        while next_number in used_numbers:
            next_number += 1
        record[0] = set_channel_number(record[0], next_number)
        used_numbers.add(next_number)
        next_number += 1
    for record in review:
        record[0] = remove_channel_number(record[0])

    ordered = records
    if sorted(url_inventory(ordered)) != sorted(original_urls):
        raise ValueError("Stream URL inventory changed during primary ordering/numbering.")
    result = newline.join(preamble + [line for record in ordered for line in record])
    if had_final_newline:
        result += newline
    return result, len(primary)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("playlist", nargs="?", default="IPTV-Playlist.m3u")
    parser.add_argument("--check", action="store_true", help="fail if the playlist is not already canonical")
    args = parser.parse_args()
    path = Path(args.playlist)
    if not path.is_file():
        raise SystemExit(f"Playlist not found: {path}")
    before = path.read_text(encoding="utf-8-sig")
    after, count = normalize_playlist_text(before)
    if args.check:
        if after != before:
            raise SystemExit("Category registry or in-place channel numbering is not canonical.")
        print(f"OK: {count} active channels are numbered in existing row order.")
        return 0
    if after != before:
        path.write_text(after, encoding="utf-8", newline="")
        print(f"Normalized {count} active channels in place; all playlist row positions and stream URLs were preserved.")
    else:
        print(f"No changes needed: {count} active channels are already canonical.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
