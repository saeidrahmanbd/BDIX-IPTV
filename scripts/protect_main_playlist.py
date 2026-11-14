#!/usr/bin/env python3
"""Protect the owner-curated IPTV playlist during metadata-only maintenance."""
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
        current["ids"] = {
            value.strip().casefold().split("@", 1)[0]
            for value in (meta.get("tvg-id", ""), meta.get("channel-id", ""))
            if value.strip()
        }
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
    lines = [
        line for line in playlist.read_text(encoding="utf-8-sig").splitlines()
        if line.startswith("#PLAYLIST-STUDIO-CATEGORIES:")
    ]
    if len(lines) != 1:
        return None
    try:
        return json.loads(lines[0].split(":", 1)[1])
    except ValueError:
        return None


def primary_identity_conflicts(rows):
    names_by_id = defaultdict(set)
    for row in rows:
        if row.get("group") not in PRIMARY_GROUPS:
            continue
        name_key = re.sub(r"[^a-z0-9]+", "", str(row.get("name", "")).casefold())
        for identity in row.get("ids", set()):
            names_by_id[identity].add(name_key)
    return {
        identity: sorted(names
                         for names in names_by_id[identity])
        for identity in sorted(names_by_id)
        if len(names_by_id[identity]) > 1
    }


def snapshot(playlist: Path, state: Path):
    rows = records(playlist)
    payload = {
        "rows": [
            {"url": row["url"], "group": row["group"], "number": row["number"]}
            for row in rows
        ],
        "category_registry": category_registry(playlist),
        # Existing identity/name collisions are baseline debt. Preserve them,
        # but never allow routine maintenance to introduce additional conflicts.
        "identity_conflicts": primary_identity_conflicts(rows),
    }
    state.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Protected {len(rows)} existing IPTV rows and exact stream URL occurrences.")


def verify(playlist: Path, state: Path):
    saved = json.loads(state.read_text(encoding="utf-8"))
    before, after = saved["rows"], records(playlist)
    failures = []

    current_registry = category_registry(playlist)
    if current_registry != saved.get("category_registry"):
        failures.append("The owner's Playlist Studio category registry changed.")

    expected = Counter(str(row["url"]) for row in before)
    actual = Counter(str(row["url"]) for row in after)
    missing = expected - actual
    if missing:
        failures.append(f"{sum(missing.values())} pre-existing URL occurrence(s) disappeared or were replaced.")
    if any(url in expected for url in (actual - expected)):
        failures.append("An additional occurrence of a pre-existing URL was added.")

    old_order = [str(row["url"]) for row in before]
    new_order = [str(row["url"]) for row in after if str(row["url"]) in expected]
    if new_order != old_order:
        failures.append("Pre-existing stream rows were reordered or removed.")

    old_by_url, new_by_url = defaultdict(list), defaultdict(list)
    for row in before:
        old_by_url.setdefault(str(row["url"]), []).append(row)
    for row in after:
        new_by_url.setdefault(str(row["url"]), []).append(row)

    for url, old_rows in old_by_url.items():
        new_rows = new_by_url.get(url, [])
        if len(old_rows) != len(new_rows):
            continue
        for old, new in zip(old_rows, new_rows):
            old_group = str(old.get("group", "")).strip()
            new_group = str(new.get("group", "")).strip()
            if old_group != new_group:
                failures.append(f"Unapproved existing group change for {new['name']}: {old_group} -> {new_group}.")
            old_number = str(old.get("number", "")).strip()
            new_number = str(new.get("number", "")).strip()
            if old_number != new_number:
                failures.append(f"Existing channel number changed for {new['name']}.")

    before_conflicts = saved.get("identity_conflicts", {})
    after_conflicts = primary_identity_conflicts(after)
    for identity, names in after_conflicts.items():
        new_names = set(names) - set(before_conflicts.get(identity, []))
        if new_names:
            failures.append(
                f"New primary identity/name conflict for {identity!r}: {', '.join(sorted(new_names))}."
            )

    for url in set(actual) - set(expected):
        if actual[url] != 1:
            failures.append("A new discovery URL is duplicated.")
        for row in new_by_url[url]:
            if row["group"] not in DISCOVERY_GROUPS:
                failures.append(f"New row outside manual queues: {row['name']} ({row['group']}).")

    if failures:
        for item in failures[:30]:
            print(f"::error::{item}", file=sys.stderr)
        raise SystemExit(f"IPTV owner-protection gate failed with {len(failures)} issue(s).")
    print(
        f"IPTV owner-protection passed: {len(before)} existing URL occurrences, row order, "
        "group assignments and channel numbers preserved; no new identity conflicts."
    )


def main():
    if len(sys.argv) != 4 or sys.argv[1] not in {"snapshot", "verify"}:
        raise SystemExit("Usage: protect_main_playlist.py snapshot|verify PLAYLIST STATE.json")
    action, playlist, state = sys.argv[1], Path(sys.argv[2]), Path(sys.argv[3])
    snapshot(playlist, state) if action == "snapshot" else verify(playlist, state)


if __name__ == "__main__":
    main()
