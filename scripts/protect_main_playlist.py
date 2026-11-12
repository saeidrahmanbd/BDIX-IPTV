#!/usr/bin/env python3
"""Protect every existing IPTV stream URL while allowing verified group repairs.

Metadata/group classification may be corrected and category blocks may be
reassembled. Existing stream URL occurrences may never be deleted, replaced or
duplicated. Separate maintenance guards continue to protect manual queues.
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
    return [row for row in result if row["url"]]


def snapshot(playlist: Path, state: Path):
    rows = [{"url": row["url"]} for row in records(playlist)]
    state.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Protected {len(rows)} existing IPTV stream URL occurrences.")


def verify(playlist: Path, state: Path):
    before = json.loads(state.read_text(encoding="utf-8"))
    after = records(playlist)
    expected = Counter(str(row["url"]) for row in before)
    actual = Counter(str(row["url"]) for row in after)
    missing = expected - actual
    duplicated = actual - expected
    errors = []
    if missing:
        errors.append(f"{sum(missing.values())} existing stream URL occurrence(s) were deleted or replaced")
    if duplicated:
        errors.append(f"{sum(duplicated.values())} unexpected duplicate stream URL occurrence(s) were added")
    if errors:
        for error in errors:
            print(f"::error::{error}")
        raise SystemExit("IPTV-Playlist.m3u URL-preservation guard failed; refusing to publish.")
    print(
        f"IPTV URL-preservation passed: all {sum(expected.values())} existing stream URL "
        "occurrences retained exactly. Evidence-backed group corrections and new discoveries are allowed."
    )


def main():
    if len(sys.argv) != 4 or sys.argv[1] not in {"snapshot", "verify"}:
        raise SystemExit("Usage: protect_main_playlist.py snapshot|verify PLAYLIST STATE.json")
    action, playlist, state = sys.argv[1], Path(sys.argv[2]), Path(sys.argv[3])
    snapshot(playlist, state) if action == "snapshot" else verify(playlist, state)


if __name__ == "__main__":
    main()
