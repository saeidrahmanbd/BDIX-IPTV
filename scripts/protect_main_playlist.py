#!/usr/bin/env python3
"""Verify a one-time owner-authorized IPTV cleanup without losing stream URLs."""
from __future__ import annotations
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ATTR = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
CATEGORY_ORDER = [
    "Bangladesh", "Indian Bangla", "Indian Movies", "Indian Music",
    "Indian Entertainment", "Pakistani", "International",
    "Documentary & Wildlife", "Kids", "Religious", "Sports",
    "Backup", "New Channels", "New Backups", "Review",
]
PRIMARY_GROUPS = set(CATEGORY_ORDER[:11])
DISCOVERY_GROUPS = {"New Channels", "New Backups"}
OWNER_APPROVALS = Path("/tmp/iptv-owner-requested-migrations.json")


def attrs(info: str) -> dict[str, str]:
    return dict(ATTR.findall(info))


def records(path: Path):
    result = []
    current = None
    def finish():
        if current is None or not current["url"]:
            return
        meta = attrs(current["info"])
        current["group"] = meta.get("group-title", "").strip()
        current["number"] = meta.get("tvg-chno", "").strip()
        current["name"] = meta.get("tvg-name") or current["info"].rsplit(",", 1)[-1].strip()
        current["ids"] = {v.strip().casefold().split("@", 1)[0] for v in (meta.get("tvg-id", ""), meta.get("channel-id", "")) if v.strip()}
        result.append(dict(current))
    for line in path.read_text(encoding="utf-8-sig").replace("\r\n", "\n").replace("\r", "\n").splitlines():
        if line.startswith("#EXTINF:"):
            finish()
            current = {"info": line, "url": ""}
        elif current is not None and line.strip().lower().startswith(("http://", "https://")) and not current["url"]:
            current["url"] = line.strip()
    finish()
    return result


def category_registry(playlist: Path):
    lines = [line for line in playlist.read_text(encoding="utf-8-sig").splitlines()
             if line.startswith("#PLAYLIST-STUDIO-CATEGORIES:")]
    if len(lines) != 1:
        return None
    try:
        return json.loads(lines[0].split(":", 1)[1])
    except ValueError:
        return None


def load_approvals():
    if not OWNER_APPROVALS.is_file():
        return {}
    try:
        rows = json.loads(OWNER_APPROVALS.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise SystemExit(f"Could not read exact-URL migration approvals: {exc}")
    if not isinstance(rows, list):
        raise SystemExit("Migration approvals must be a JSON list.")
    return {
        (str(row.get("url", "")), str(row.get("source_group", "")), str(row.get("target_group", ""))): row
        for row in rows if isinstance(row, dict) and row.get("url")
    }


def snapshot(playlist: Path, state: Path):
    rows = [{"url": row["url"], "group": row["group"], "number": row["number"]} for row in records(playlist)]
    state.write_text(json.dumps({"rows": rows, "category_registry": category_registry(playlist)},
                                ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Protected {len(rows)} existing IPTV rows and exact stream URL occurrences.")


def verify(playlist: Path, state: Path):
    saved = json.loads(state.read_text(encoding="utf-8"))
    before, after = saved["rows"], records(playlist)
    if category_registry(playlist) != CATEGORY_ORDER:
        raise SystemExit("IPTV-Playlist.m3u category registry is not the canonical category order.")
    expected_counts = Counter(str(row["url"]) for row in before)
    actual_counts = Counter(str(row["url"]) for row in after)
    missing = expected_counts - actual_counts
    if missing:
        raise SystemExit(f"IPTV URL preservation failed: {sum(missing.values())} existing URL occurrence(s) missing.")
    added = actual_counts - expected_counts

    before_by_url, after_by_url = defaultdict(list), defaultdict(list)
    for row in before:
        before_by_url[str(row["url"])].append(row)
    for row in after:
        after_by_url[str(row["url"])].append(row)
    approvals = load_approvals()
    failures = []
    for url, original_rows in before_by_url.items():
        updated_rows = after_by_url[url]
        if len(original_rows) != len(updated_rows):
            failures.append(f"URL occurrence count changed: {url}")
            continue
        for original, current in zip(original_rows, updated_rows):
            old_group = str(original.get("group", "")).strip()
            new_group = str(current.get("group", "")).strip()
            if old_group != new_group:
                approval = approvals.get((url, old_group, new_group))
                if old_group == "Review" or not approval or approval.get("allow_metadata") is not True:
                    failures.append(f"Unapproved group migration for {current['name']}: {old_group} -> {new_group}")
            if new_group not in CATEGORY_ORDER:
                failures.append(f"Unknown category {new_group!r}: {current['name']}")
            if new_group in PRIMARY_GROUPS and not current["number"].isdigit():
                failures.append(f"Primary channel has no numeric tvg-chno: {current['name']}")
            if new_group not in PRIMARY_GROUPS and current["number"]:
                failures.append(f"Non-primary channel carries tvg-chno: {current['name']} ({new_group})")

    remaining_additions = added.copy()
    for row in after:
        url = str(row["url"])
        if remaining_additions[url] > 0:
            if url in expected_counts:
                failures.append(f"Duplicate stream URL occurrence added: {row['name']}")
            if row["group"] not in DISCOVERY_GROUPS:
                failures.append(f"New row outside discovery queues: {row['name']} ({row['group']})")
            remaining_additions[url] -= 1

    seen_groups = []
    for row in after:
        group = row["group"]
        if not seen_groups or seen_groups[-1] != group:
            if group in seen_groups:
                failures.append(f"Category block is split: {group}")
            seen_groups.append(group)
    ranks = [CATEGORY_ORDER.index(group) for group in seen_groups if group in CATEGORY_ORDER]
    if ranks != sorted(ranks):
        failures.append("Category blocks do not follow the canonical category order.")

    primary_numbers = []
    seen_ids = {}
    duplicate_urls = [url for url, count in Counter(row["url"] for row in after).items() if count > 1]
    if duplicate_urls:
        failures.append(f"Duplicate stream URL occurrences remain: {len(duplicate_urls)}")
    for row in after:
        if row["group"] not in PRIMARY_GROUPS:
            continue
        primary_numbers.append(int(row["number"]) if row["number"].isdigit() else -1)
        for channel_id in row["ids"]:
            previous = seen_ids.get(channel_id)
            if previous and previous != row["url"]:
                failures.append(f"Duplicate primary channel identity: {channel_id} ({row['name']})")
            seen_ids[channel_id] = row["url"]
    if primary_numbers != list(range(1, len(primary_numbers) + 1)):
        failures.append("Primary tvg-chno values are not sequential in playlist order.")

    if failures:
        for item in failures[:30]:
            print(f"::error::{item}", file=sys.stderr)
        raise SystemExit(f"IPTV cleanup safety gate failed with {len(failures)} issue(s).")
    print(f"IPTV cleanup guard passed: {sum(actual_counts.values())} stream URLs preserved; "
          "all group changes exact-URL approved; category blocks, identities and numbering valid.")


def main():
    if len(sys.argv) != 4 or sys.argv[1] not in {"snapshot", "verify"}:
        raise SystemExit("Usage: protect_main_playlist.py snapshot|verify PLAYLIST STATE.json")
    action, playlist, state = sys.argv[1], Path(sys.argv[2]), Path(sys.argv[3])
    snapshot(playlist, state) if action == "snapshot" else verify(playlist, state)


if __name__ == "__main__":
    main()
