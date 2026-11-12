#!/usr/bin/env python3
"""Protect existing IPTV rows while allowing stable category regrouping.

Metadata and logo edits are allowed. Existing stream URLs must remain present
in their original group and preserve their relative order within that group.
Category blocks may be reassembled; new rows may be added without disturbing
the existing order inside any category.
"""
from __future__ import annotations
import json
import sys
from collections import Counter
from pathlib import Path

def records(path: Path):
    result = []
    current = None
    for line in path.read_text(encoding="utf-8-sig").replace("\r\n", "\n").replace("\r", "\n").splitlines():
        if line.startswith("#EXTINF:"):
            if current is not None:
                result.append(current)
            current = {"info": line, "url": ""}
        elif current is not None and line.strip().lower().startswith(("http://", "https://")) and not current["url"]:
            current["url"] = line.strip()
    if current is not None:
        result.append(current)
    return [r for r in result if r["url"]]

def group(info: str) -> str:
    import re
    match = re.search(r'\bgroup-title="([^"]*)"', info)
    value = match.group(1) if match else ""
    return "Review" if value == "Not Playing" else value

def snapshot(playlist: Path, state: Path):
    rows = [{"url": r["url"], "group": group(r["info"])} for r in records(playlist)]
    state.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Protected {len(rows)} existing IPTV stream rows.")

def _is_subsequence(expected: list[str], actual: list[str]) -> bool:
    """Return true when expected rows retain their relative order in actual."""
    position = 0
    for url in actual:
        if position < len(expected) and url == expected[position]:
            position += 1
    return position == len(expected)


def verify(playlist: Path, state: Path):
    before = json.loads(state.read_text(encoding="utf-8"))
    after = records(playlist)
    before_by_group: dict[str, list[str]] = {}
    after_by_group: dict[str, list[str]] = {}
    for row in before:
        before_by_group.setdefault(row["group"], []).append(row["url"])
    for row in after:
        after_by_group.setdefault(group(row["info"]), []).append(row["url"])

    all_after = Counter(row["url"] for row in after)
    errors = []
    for old_group, old_urls in before_by_group.items():
        current_urls = after_by_group.get(old_group, [])
        old_counts = Counter(old_urls)
        current_counts = Counter(current_urls)
        missing = old_counts - current_counts
        if missing:
            for url, count in missing.items():
                available_elsewhere = max(0, all_after[url] - current_counts[url])
                moved = min(count, available_elsewhere)
                deleted = count - moved
                if moved:
                    errors.append(
                        f"{moved} existing stream(s) moved out of original group "
                        f"{old_group!r}: {url}"
                    )
                if deleted:
                    errors.append(
                        f"{deleted} existing stream(s) deleted or URL-changed from "
                        f"original group {old_group!r}: {url}"
                    )
        elif not _is_subsequence(old_urls, current_urls):
            errors.append(
                f"Existing stream order changed within group {old_group!r}; "
                "only cross-group category regrouping is permitted."
            )

    if errors:
        for error in errors:
            print(f"::error::{error}")
        raise SystemExit(f"IPTV-Playlist.m3u protection failed: {len(errors)} violation(s); refusing to publish.")
    print(
        f"IPTV protection passed: all {len(before)} existing stream rows retained "
        "in their original groups and relative order within each group."
    )

def main():
    if len(sys.argv) != 4 or sys.argv[1] not in {"snapshot", "verify"}:
        raise SystemExit("Usage: protect_main_playlist.py snapshot|verify PLAYLIST STATE.json")
    action, playlist, state = sys.argv[1], Path(sys.argv[2]), Path(sys.argv[3])
    snapshot(playlist, state) if action == "snapshot" else verify(playlist, state)

if __name__ == "__main__":
    main()
