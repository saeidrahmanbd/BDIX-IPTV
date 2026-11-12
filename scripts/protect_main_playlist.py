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
    approvals = load_approvals()
    # The approvals artifact is written only by the explicitly owner-requested
    # one-time cleanup branch. Routine daily maintenance has no such authority.
    # The migration script writes this exact-URL approvals file even when no
    # group transitions are needed. Its existence authorizes category-block
    # reassembly and missing-number repair; individual group moves still need
    # their own exact URL approval below.
    migration_mode = OWNER_APPROVALS.is_file()

    current_registry = category_registry(playlist)
    previous_registry = saved.get("category_registry")
    if migration_mode:
        if current_registry != CATEGORY_ORDER:
            raise SystemExit("Owner-approved migration did not produce the canonical category registry.")
    elif current_registry != previous_registry:
        raise SystemExit("Routine IPTV maintenance changed the owner's category registry.")

    expected_counts = Counter(str(row["url"]) for row in before)
    actual_counts = Counter(str(row["url"]) for row in after)
    missing = expected_counts - actual_counts
    if missing:
        raise SystemExit(f"IPTV URL preservation failed: {sum(missing.values())} existing URL occurrence(s) missing.")
    added = actual_counts - expected_counts
    if any(count > 1 for url, count in added.items() if url not in expected_counts):
        raise SystemExit("IPTV URL preservation failed: a newly discovered stream URL appears more than once.")
    if any(count for count in added.values()):
        # Existing URLs can never be duplicated by a discovery candidate.
        duplicated = sum(count for url, count in added.items() if url in expected_counts)
        if duplicated:
            raise SystemExit(f"IPTV URL preservation failed: {duplicated} duplicate existing URL occurrence(s) added.")

    before_by_url, after_by_url = defaultdict(list), defaultdict(list)
    for row in before:
        before_by_url[str(row["url"])].append(row)
    for row in after:
        after_by_url[str(row["url"])].append(row)

    failures = []
    baseline_order = [str(row["url"]) for row in before]
    after_existing_order = [str(row["url"]) for row in after if str(row["url"]) in expected_counts]
    # Daily repair/discovery jobs cannot reorder any existing row. The one-time
    # owner-approved cleanup may sort/reassemble categories after exact approvals.
    if not migration_mode and after_existing_order != baseline_order:
        failures.append("Existing row order changed or an existing row is missing")

    for url, original_rows in before_by_url.items():
        updated_rows = after_by_url[url]
        if len(original_rows) != len(updated_rows):
            failures.append(f"URL occurrence count changed: {url}")
            continue
        for original, current in zip(original_rows, updated_rows):
            old_group = str(original.get("group", "")).strip()
            new_group = str(current.get("group", "")).strip()
            approved = approvals.get((url, old_group, new_group))
            exact_approval = bool(approved and approved.get("allow_metadata") is True)
            if old_group != new_group and (old_group == "Review" or not exact_approval):
                failures.append(f"Unapproved group migration for {current['name']}: {old_group} -> {new_group}")
            if old_group == new_group and current["number"] != str(original.get("number", "")):
                old_number = str(original.get("number", "")).strip()
                new_number = str(current["number"]).strip()
                may_fill_missing_primary = (
                    migration_mode and old_group in PRIMARY_GROUPS
                    and (not old_number.isdigit() or int(old_number) <= 0)
                    and new_number.isdigit()
                )
                may_clear_nonprimary_queue = (
                    migration_mode and old_group not in PRIMARY_GROUPS
                    and bool(old_number) and not new_number
                )
                if not (may_fill_missing_primary or may_clear_nonprimary_queue):
                    failures.append(f"Existing channel number changed for {current['name']}")
            if new_group not in CATEGORY_ORDER:
                failures.append(f"Unknown category {new_group!r}: {current['name']}")

    # Metadata/country/logo defects in these queues are intentionally deferred
    # to the owner's manual review; they must never stop discovery from staging.
    for url, count in added.items():
        rows = after_by_url[url]
        if url in expected_counts:
            failures.append(f"Duplicate existing stream URL occurrence added: {url}")
            continue
        for row in rows:
            if row["group"] not in DISCOVERY_GROUPS:
                failures.append(f"New row outside discovery queues: {row['name']} ({row['group']})")

    # Routine maintenance preserves existing row placement, so category block
    # order and manual numbering anomalies remain diagnostics rather than a
    # reason to reshuffle the owner's playlist. The owner-approved one-time
    # migration is allowed to reassemble canonical category blocks.
    if migration_mode:
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
        for row in after:
            if row["group"] not in PRIMARY_GROUPS:
                continue
            if not row["number"].isdigit():
                failures.append(f"Owner-approved migration left a primary row unnumbered: {row['name']}")
            else:
                primary_numbers.append(int(row["number"]))
            for channel_id in row["ids"]:
                previous = seen_ids.get(channel_id)
                if previous and previous != row["url"]:
                    failures.append(f"Duplicate primary channel identity: {channel_id} ({row['name']})")
                seen_ids[channel_id] = row["url"]
        if any(number <= 0 for number in primary_numbers):
            failures.append("Owner-approved migration left a non-positive primary channel number.")
        if len(primary_numbers) != len(set(primary_numbers)):
            failures.append("Owner-approved migration produced duplicate primary channel numbers.")
        # Existing positive channel numbers are owner-curated and must be
        # preserved; only missing/invalid values are filled by the migration.

    if failures:
        for item in failures[:30]:
            print(f"::error::{item}", file=sys.stderr)
        raise SystemExit(f"IPTV owner-protection gate failed with {len(failures)} issue(s).")
    print(
        f"IPTV owner-protection passed: {sum(actual_counts.values())} stream URLs preserved; "
        f"{'owner-approved migration' if migration_mode else 'routine metadata/logo/discovery'} "
        "permissions respected."
    )


def main():
    if len(sys.argv) != 4 or sys.argv[1] not in {"snapshot", "verify"}:
        raise SystemExit("Usage: protect_main_playlist.py snapshot|verify PLAYLIST STATE.json")
    action, playlist, state = sys.argv[1], Path(sys.argv[2]), Path(sys.argv[3])
    snapshot(playlist, state) if action == "snapshot" else verify(playlist, state)


if __name__ == "__main__":
    main()
