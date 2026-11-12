#!/usr/bin/env python3
"""Protect owner-curated IPTV rows while allowing metadata fixes and queued discoveries.

Existing rows must retain their stream URL, group, channel number and relative
order. New rows are accepted only in the manual New Channels/New Backups queues.
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

ATTR = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
DISCOVERY_GROUPS = {"New Channels", "New Backups"}


def attrs(info: str) -> dict[str, str]:
    return dict(ATTR.findall(info))


def records(path: Path):
    result = []
    current = None
    for line in path.read_text(encoding="utf-8-sig").replace("\r\n", "\n").replace("\r", "\n").splitlines():
        if line.startswith("#EXTINF:"):
            if current is not None and current["url"]:
                meta = attrs(current["info"])
                current["group"] = meta.get("group-title", "").strip()
                current["number"] = meta.get("tvg-chno", "").strip()
                result.append(current)
            current = {"info": line, "url": ""}
        elif current is not None and line.strip().lower().startswith(("http://", "https://")) and not current["url"]:
            current["url"] = line.strip()
    if current is not None and current["url"]:
        meta = attrs(current["info"])
        current["group"] = meta.get("group-title", "").strip()
        current["number"] = meta.get("tvg-chno", "").strip()
        result.append(current)
    return result


def category_registry(playlist: Path):
    for line in playlist.read_text(encoding="utf-8-sig").splitlines():
        if line.startswith("#PLAYLIST-STUDIO-CATEGORIES:"):
            return json.loads(line.split(":", 1)[1])
    return None


def snapshot(playlist: Path, state: Path):
    rows = [
        {"url": row["url"], "group": row["group"], "number": row["number"]}
        for row in records(playlist)
    ]
    state.write_text(
        json.dumps(
            {"rows": rows, "category_registry": category_registry(playlist)},
            ensure_ascii=False,
            indent=2,
        ) + "\n",
        encoding="utf-8",
    )
    print(
        f"Protected {len(rows)} existing IPTV rows: exact stream URLs, "
        "group assignments, channel numbers and relative order."
    )


def verify(playlist: Path, state: Path):
    saved = json.loads(state.read_text(encoding="utf-8"))
    before = saved["rows"]
    after = records(playlist)
    if category_registry(playlist) != saved.get("category_registry"):
        raise SystemExit("IPTV-Playlist.m3u category registry/order changed; refusing to publish.")
    expected_counts = Counter(str(row["url"]) for row in before)
     actual_counts = Counter(str(row["url"]) for row in after)

    errors = []
    missing = expected_counts - actual_counts
    if missing:
        errors.append(f"{sum(missing.values())} existing stream URL occurrence(s) were deleted or replaced")

    duplicated = {
        url: count - expected_counts.get(url, 0)
        for url, count in actual_counts.items()
        if count > expected_counts.get(url, 0)
    }
    if duplicated:
        errors.append(f"{sum(duplicated.values())} unexpected duplicate stream URL occurrence(s) were added")

    # Match every baseline row as an ordered subsequence of the updated file.
    # Metadata may be repaired, but existing group placement and numbering stay fixed.
    cursor = 0
    matched_indices = set()
    for original in before:
        url = str(original.get("url", ""))
        found = next((i for i in range(cursor, len(after)) if after[i]["url"] == url), None)
        if found is None:
            errors.append("Existing row order changed or an existing row is missing")
            break
        matched_indices.add(found)
        current = after[found]
        if current["group"] != str(original.get("group", "")):
            errors.append(
                f"Existing group assignment changed for {url}: "
                f"{original.get('group', '')!r} -> {current['group']!r}"
            )
        if current["number"] != str(original.get("number", "")):
            errors.append(
                f"Existing channel number changed for {url}: "
                f"{original.get('number', '')!r} -> {current['number']!r}"
            )
        cursor = found + 1

    # New channel discovery is staging-only. Existing primary/Backup/Review
    # rows cannot be inserted, promoted or structurally changed by automation.
    for index, row in enumerate(after):
        if index in matched_indices:
            continue
        if row["group"] not in DISCOVERY_GROUPS:
            errors.append(
                f"New row outside manual discovery queues: {row['info'].rsplit(',', 1)[-1].strip()!r} "
                f"(group={row['group']!r})"
            )

    if errors:
        for error in errors:
            print(f"::error::{error}")
        raise SystemExit("IPTV-Playlist.m3u owner-protection guard failed; refusing to publish.")

    print(
        f"IPTV owner-protection passed: all {len(before)} existing rows retained "
        "with their exact URLs, groups, numbers and relative order; "
        "new rows are confined to New Channels/New Backups. "
        "Metadata/logo repairs remain permitted."
    )


def main():
    if len(sys.argv) != 4 or sys.argv[1] not in {"snapshot", "verify"}:
        raise SystemExit("Usage: protect_main_playlist.py snapshot|verify PLAYLIST STATE.json")
    action, playlist, state = sys.argv[1], Path(sys.argv[2]), Path(sys.argv[3])
    snapshot(playlist, state) if action == "snapshot" else verify(playlist, state)


if __name__ == "__main__":
    main()
