#!/usr/bin/env python3
"""Verify a one-time owner-authorized IPTV cleanup without losing stream URLs."""
from __future__ import annotations
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from stream_url_identity import stream_url_key

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
OWNER_MIGRATION_AUTHORIZED = Path("/tmp/iptv-owner-migration-authorized")


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
    # URI scheme and host are case-insensitive; canonicalize only those
    # components so signed paths, query strings and exact stream identity remain
    # protected while approvals survive harmless host/scheme casing differences.
    return {
        (stream_url_key(str(row.get("url", ""))),
         str(row.get("source_group", "")).strip(),
         str(row.get("target_group", "")).strip()): row
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
    failures = []
    primary_ids = {}
    for row in after:
        if row.get("group") not in PRIMARY_GROUPS:
            continue
        identity_name = re.sub(r"[^a-z0-9]+", "", str(row.get("name", "")).casefold())
        for identity in row.get("ids", set()):
            previous = primary_ids.get(identity)
            if previous is not None and previous != identity_name:
                failures.append(
                    f"Duplicate primary channel identity {identity!r}: assigned to multiple channel names."
                )
            else:
                primary_ids[identity] = identity_name
    current_registry = category_registry(playlist)
    if current_registry != saved.get("category_registry"):
        if not (OWNER_MIGRATION_AUTHORIZED.is_file() and current_registry == CATEGORY_ORDER):
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
    approvals = load_approvals() if OWNER_MIGRATION_AUTHORIZED.is_file() else {}
    for url, old_rows in old_by_url.items():
        new_rows = new_by_url.get(url, [])
        if len(old_rows) != len(new_rows):
            continue
        for old, new in zip(old_rows, new_rows):
            old_group = str(old.get("group", "")).strip()
            new_group = str(new.get("group", "")).strip()
            approval_key = (stream_url_key(url), old_group, new_group)
            if old_group != new_group and approval_key not in approvals:
                failures.append(f"Unapproved existing group change for {new['name']}: {old_group} -> {new_group}.")
            old_number = str(old.get("number", "")).strip()
            new_number = str(new.get("number", "")).strip()
            if old_number != new_number:
                queue_number_cleanup = (
                    OWNER_MIGRATION_AUTHORIZED.is_file()
                    and old_group not in PRIMARY_GROUPS
                    and not new_number
                    and new_group in {"Backup", "Review", "New Channels", "New Backups"}
                )
                approved_primary_promotion = (
                    OWNER_MIGRATION_AUTHORIZED.is_file()
                    and old_group not in PRIMARY_GROUPS
                    and new_group in PRIMARY_GROUPS
                    and new_number.isdigit()
                    and int(new_number) > 0
                    and approval_key in approvals
                )
                authorized_primary_number_fill = (
                    OWNER_MIGRATION_AUTHORIZED.is_file()
                    and old_group in PRIMARY_GROUPS
                    and new_group == old_group
                    and not (old_number.isdigit() and int(old_number) > 0)
                    and new_number.isdigit()
                    and int(new_number) > 0
                )
                if queue_number_cleanup or approved_primary_promotion or authorized_primary_number_fill:
                    # The one-time owner authorization permits removing legacy
                    # queue numbers or assigning a fresh positive number to an
                    # exact-URL-approved queue-to-primary promotion. Existing
                    # primary numbers remain immutable.
                    pass
                else:
                    failures.append(f"Existing channel number changed for {new['name']}.")
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
    print(f"IPTV owner-protection passed: {len(before)} existing URL occurrences and order preserved; exact approved transitions only; primary numbers preserved.")


def main():
    if len(sys.argv) != 4 or sys.argv[1] not in {"snapshot", "verify"}:
        raise SystemExit("Usage: protect_main_playlist.py snapshot|verify PLAYLIST STATE.json")
    action, playlist, state = sys.argv[1], Path(sys.argv[2]), Path(sys.argv[3])
    snapshot(playlist, state) if action == "snapshot" else verify(playlist, state)


if __name__ == "__main__":
    main()
