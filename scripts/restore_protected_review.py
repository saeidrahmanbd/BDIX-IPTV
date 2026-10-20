#!/usr/bin/env python3
"""Restore review queues exactly and undo automatic reclassification of existing streams.

The removal guard remains strict: this helper does not delete stream URLs. It
restores the pre-maintenance Backup/Not Playing blocks from the snapshot and
restores the original EXTINF line if an existing primary stream was moved into
a protected queue by a metadata repair.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
import re

SNAPSHOT = Path("/tmp/iptv-protected-review.m3u")
BASELINE = Path("/tmp/iptv-playlist-baseline.json")
PLAYLIST = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("IPTV-Playlist.m3u")
PROTECTED = {"Backup", "Not Playing"}
ATTR = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')


def attrs(info: str) -> dict[str, str]:
    return dict(ATTR.findall(info))


def group_of(info: str) -> str:
    return attrs(info).get("group-title", "").strip()


def parse(text: str) -> tuple[list[str], list[list[str]]]:
    """Return preamble and complete EXTINF blocks without changing block text."""
    preamble: list[str] = []
    records: list[list[str]] = []
    current: list[str] | None = None
    for line in text.replace("\r", "").splitlines():
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


def url_of(record: list[str]) -> str:
    return next(
        (line.strip() for line in record[1:]
         if line.strip().lower().startswith(("http://", "https://"))),
        "",
    )


def serialize(preamble: list[str], records: list[list[str]]) -> str:
    return "\n".join(preamble + [line for record in records for line in record]).rstrip() + "\n"


def restore() -> None:
    if not SNAPSHOT.is_file() or not BASELINE.is_file():
        raise SystemExit(
            "ERROR: protected-review snapshot or playlist baseline is missing; "
            "refusing to alter the playlist."
        )

    current_text = PLAYLIST.read_text(encoding="utf-8-sig")
    snapshot_text = SNAPSHOT.read_text(encoding="utf-8")
    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    preamble, current_records = parse(current_text)
    _, snapshot_records = parse(snapshot_text)

    if any(group_of(record[0]) not in PROTECTED for record in snapshot_records):
        raise SystemExit("ERROR: protected snapshot contains a non-protected group; refusing restore.")

    # The snapshot provides the exact protected records and their original order.
    snapshot_urls = [url_of(record).casefold() for record in snapshot_records]
    if any(not url for url in snapshot_urls) or len(snapshot_urls) != len(set(snapshot_urls)):
        raise SystemExit("ERROR: protected snapshot contains a missing or duplicate URL; refusing restore.")

    # A stream URL must identify one baseline entry unambiguously. If it did not,
    # do not guess which identity or category should be restored.
    baseline_by_url: dict[str, dict[str, str]] = {}
    for item in baseline:
        url = str(item.get("url", "")).strip()
        if not url:
            continue
        key = url.casefold()
        if key in baseline_by_url:
            raise SystemExit(
                f"ERROR: baseline contains repeated stream URL for {url}; refusing ambiguous restore."
            )
        baseline_by_url[key] = {
            "url": url,
            "group": str(item.get("group", "")),
            "info": str(item.get("info", "")),
        }

    active_records: list[list[str]] = []
    unexpected_backup: list[list[str]] = []
    unexpected_not_playing: list[list[str]] = []
    restored_from_queue = 0
    reclassification_reverted = 0

    for record in current_records:
        url = url_of(record)
        key = url.casefold()
        current_group = group_of(record[0])
        original = baseline_by_url.get(key)

        if original and original["group"] in PROTECTED:
            # Do not trust an edited/reclassified copy of a protected stream.
            # The exact original copy is restored below from the protected snapshot.
            restored_from_queue += 1
            continue

        if original and current_group in PROTECTED and original["group"] not in PROTECTED:
            # An existing primary stream must not be silently demoted to Backup or
            # Not Playing. Restore its original metadata line, retaining its URL.
            record[0] = original["info"]
            current_group = group_of(record[0])
            reclassification_reverted += 1

        if current_group == "Backup":
            unexpected_backup.append(record)
        elif current_group == "Not Playing":
            unexpected_not_playing.append(record)
        else:
            active_records.append(record)

    # Preserve all existing non-protected streams as-is, then reinsert the entire
    # protected snapshot. Any unexpected new protected record is retained (never
    # deleted); the byte-for-byte safety guard will block publication for review.
    _, snapshot_parsed = parse(snapshot_text)
    snapshot_backup = [r for r in snapshot_parsed if group_of(r[0]) == "Backup"]
    snapshot_not_playing = [r for r in snapshot_parsed if group_of(r[0]) == "Not Playing"]

    final_records = (
        active_records
        + snapshot_backup
        + unexpected_backup
        + snapshot_not_playing
        + unexpected_not_playing
    )
    new_text = serialize(preamble, final_records)
    if new_text != current_text:
        PLAYLIST.write_text(new_text, encoding="utf-8", newline="\n")

    print(
        "Protected review restore: "
        f"snapshot_backup={len(snapshot_backup)} "
        f"snapshot_not_playing={len(snapshot_not_playing)} "
        f"restored_exact={restored_from_queue} "
        f"primary_reclassifications_reverted={reclassification_reverted} "
        f"unexpected_backup_retained={len(unexpected_backup)} "
        f"unexpected_not_playing_retained={len(unexpected_not_playing)}"
    )


if __name__ == "__main__":
    restore()
