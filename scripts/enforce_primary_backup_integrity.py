#!/usr/bin/env python3
"""Enforce one primary stream per channel and keep Backup free of orphan rows.

Distinct alternate stream URLs are preserved. Duplicate primary copies are
reclassified as Backup; Backup records without an exact primary identity are
quarantined into Review, except for exact owner-authorized orphan Backup removals. No other stream URL is silently discarded.
"""
from __future__ import annotations

import argparse
import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

from permanent_removals import AUTHORIZED_ORPHAN_BACKUP_REMOVALS
from stream_url_identity import stream_url_key
from logo_asset_naming import is_blocked_logo_basename

PLAYLIST = Path("IPTV-Playlist.m3u")
REPORT = Path("reports/primary-backup-integrity.md")
RAW_LOGO_BASE = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/"
ATTR = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')

PRIMARY_GROUPS = [
    "Bangladesh", "Indian Bangla", "Indian Movies", "Indian Music",
    "Indian Entertainment", "Pakistani", "International",
    "Documentary & Wildlife", "Kids", "Religious", "Sports",
]
GROUP_ORDER = PRIMARY_GROUPS + ["Backup", "New Channels", "New Backups", "Review"]
CANONICAL_ATTR_ORDER = ["tvg-id", "tvg-name", "tvg-logo", "tvg-chno", "channel-id", "tvg-country", "tvg-language", "group-title"]
REVIEW_GROUPS = {"Review", "New Channels", "New Backups", "Not Playing"}
LEGACY_GROUPS = {"Not Playing": "Review"}

# Orphan candidates verified against channel identity, genre and current stream-health evidence.
# Only BD/IN-eligible, non-restricted candidates are promoted to active groups.
# User-directed overrides: kids are assigned to Kids; specified non-kids are removed.
MIGRATION_GROUP_BY_ID = {
    "channelwin.in@sd": "REMOVE",
    "darshanatv.in@sd": "REMOVE",
    "eurosport.in@sd": "Sports",
    "humtv.pk": "Pakistani",
    "greengoldtv.in@india": "Kids",
    "gtcpunjabi.in@uk": "Indian Entertainment",
    "hungama.in@sd": "Kids",
    "thejunglebook.in": "Kids",
    "mbctv.in@sd": "REMOVE",
    "mhone.in@sd": "Indian Music",
    "mhonedilse.in@sd": "Indian Music",
    "mhonemovies.in": "Indian Movies",
    "mhonemovies.in@sd": "Indian Movies",
    "mh1music.in@sd": "Indian Music",
    "mh1prime.in": "REMOVE",
    "ntv.in": "Indian Entertainment",
    "pogo.in@sd": "Kids",
    "qtv.in": "Indian Entertainment",
    "totaltvharyana.in@sd": "REMOVE",
    "tv9bangla.in": "REMOVE",
    "wowkidz.in@hindi": "Kids",
    "wowkidztamil.in": "Kids",
    "wowkidz.in@telugu": "Kids",
    "zbcartoon.in": "Kids",
}
# These identities were explicitly removed at the user's direction.
# Do not let playlist maintenance or discovery reintroduce them.
REMOVE_CHANNEL_IDS = frozenset({
    "channelwin.in@sd", "darshanatv.in@sd", "mbctv.in@sd",
    "mh1prime.in",
    "totaltvharyana.in@sd", "tv9bangla.in",
})
KIDS_CHANNEL_IDS = frozenset({
    "greengoldtv.in@india", "hungama.in@sd", "thejunglebook.in",
    "pogo.in@sd", "wowkidz.in@hindi", "wowkidztamil.in",
    "wowkidz.in@telugu", "zbcartoon.in",
})



def attrs(info: str) -> dict[str, str]:
    return dict(ATTR.findall(info))


def split_extinf(info: str) -> tuple[str, str]:
    quoted = False
    for index, char in enumerate(info):
        if char == '"':
            quoted = not quoted
        elif char == "," and not quoted:
            return info[:index], info[index + 1:]
    return info, ""


def canonicalize_extinf(info: str) -> str:
    """Serialize known EXTINF attributes in one stable order without changing values."""
    head, display = split_extinf(info)
    matches = ATTR.findall(head)
    if not matches:
        return info
    values = dict(matches)
    prefix = head.split(None, 1)[0]
    ordered = [key for key in CANONICAL_ATTR_ORDER if key in values]
    ordered.extend(key for key, _ in matches if key not in CANONICAL_ATTR_ORDER and key not in ordered)
    rendered = " ".join(f'{key}="{values[key]}"' for key in ordered)
    return prefix + (" " + rendered if rendered else "") + ("," + display if "," in info else "")


def set_attr(info: str, key: str, value: str) -> str:
    pattern = re.compile(rf'\s+{re.escape(key)}="[^"]*"')
    if pattern.search(info):
        return pattern.sub(f' {key}="{value}"', info, count=1)
    head, display = split_extinf(info)
    marker = re.search(r'\s+group-title="', head)
    insert_at = marker.start() if marker else len(head)
    return head[:insert_at] + f' {key}="{value}"' + head[insert_at:] + ("," + display if display or "," in info else "")


def remove_attr(info: str, key: str) -> str:
    return re.sub(rf'\s+{re.escape(key)}="[^"]*"', "", info, count=1)


def set_group(info: str, group: str) -> str:
    return set_attr(info, "group-title", group)


def set_display(info: str, name: str) -> str:
    head, _ = split_extinf(info)
    return head + "," + name


def parse_playlist(text: str) -> tuple[list[str], list[list[str]]]:
    preamble: list[str] = []
    records: list[list[str]] = []
    current: list[str] | None = None
    for line in text.replace("\r\n", "\n").replace("\r", "\n").splitlines():
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


def stream_url(record: list[str]) -> str:
    return next(
        (line.strip() for line in record[1:] if line.strip().lower().startswith(("http://", "https://"))),
        "",
    )


def display_name(info: str) -> str:
    a = attrs(info)
    _, display = split_extinf(info)
    return (a.get("tvg-name") or display).strip()


def identity_ids(info: str) -> set[str]:
    a = attrs(info)
    return {
        value.strip().casefold()
        for value in (a.get("tvg-id", ""), a.get("channel-id", ""))
        if value.strip()
    }


def is_authorized_orphan_backup_removal(info: str, url: str) -> bool:
    """Match only the exact channel identity + URL explicitly rejected by the owner."""
    a = attrs(info)
    if a.get("group-title", "").strip() != "Backup":
        return False
    ids = {
        value.strip().casefold()
        for value in (a.get("tvg-id", ""), a.get("channel-id", ""))
        if value.strip()
    }
    candidate_url = stream_url_key(url)
    return any(
        channel_id in ids and candidate_url == stream_url_key(expected_url)
        for channel_id, expected_url in AUTHORIZED_ORPHAN_BACKUP_REMOVALS.items()
    )


def normalized_channel_name(value: str) -> str:
    value = unicodedata.normalize("NFKD", str(value or "")).casefold()
    value = "".join(char for char in value if not unicodedata.combining(char))
    value = re.sub(r"\b(?:backup|hd|fhd|uhd|sd|4k|1080p|720p|576p|480p|360p)\b", " ", value)
    return re.sub(r"[^a-z0-9]+", "", value)

def natural_key(value: str):
    value = unicodedata.normalize("NFKD", str(value or "")).casefold().strip()
    return tuple(int(part) if part.isdigit() else part for part in re.split(r"(\d+)", value))


def country_from_id(value: str) -> str:
    match = re.search(r"\.([a-z]{2})(?:@|$)", str(value or "").strip(), re.I)
    return match.group(1).upper() if match else ""


def update_registry(preamble: list[str]) -> list[str]:
    out = [line for line in preamble if not line.startswith("#PLAYLIST-STUDIO-CATEGORIES:")]
    registry = "#PLAYLIST-STUDIO-CATEGORIES:" + json.dumps(GROUP_ORDER, ensure_ascii=False)
    insert_at = next((index + 1 for index, line in enumerate(out) if line.startswith("#EXTM3U")), 0)
    out.insert(insert_at, registry)
    return out


def repair_playlist_text(text: str) -> tuple[str, dict[str, object], list[str]]:
    preamble, records = parse_playlist(text)
    stats: dict[str, object] = {
        "entries": len(records),
        "legacy_review_renamed": 0,
        "kids_promoted_from_review": 0,
        "non_kids_review_removed": 0,
        "unknown_groups_quarantined": 0,
        "missing_logos_quarantined": 0,
        "missing_logos_unresolved": [],
        "duplicate_primary_demoted": 0,
        "orphan_backups_quarantined": 0,
        "user_authorized_orphan_backups_removed": 0,
        "orphan_backups_promoted": 0,
        "restricted_backups_reviewed": 0,
        "name_matched_backups_linked": 0,
        "metadata_fields_filled": 0,
        "backup_metadata_reconciled": 0,
        "missing_logos_deferred": [],
        "review_invalid_logos_cleared": 0,
        "undetermined_languages": [],
    }
    errors: list[str] = []
    seen_urls: set[str] = set()

    # Apply the user's explicit Review decision before duplicate and metadata
    # validation: eligible kids go to Kids; all listed non-kids are removed.
    retained_records: list[list[str]] = []
    for record in records:
        info = record[0]
        if is_authorized_orphan_backup_removal(info, stream_url(record)):
            stats["user_authorized_orphan_backups_removed"] += 1
            continue
        ids = identity_ids(info)
        if ids & REMOVE_CHANNEL_IDS:
            stats["non_kids_review_removed"] += 1
            continue
        group = attrs(info).get("group-title", "").strip()
        if ids & KIDS_CHANNEL_IDS and group in REVIEW_GROUPS:
            record[0] = set_group(info, "Kids")
            stats["kids_promoted_from_review"] += 1
        retained_records.append(record)
    records = retained_records

    for index, record in enumerate(records):
        info = record[0]
        url = stream_url(record)
        if not url:
            errors.append(f"Entry {index + 1}: missing HTTP(S) stream URL")
            continue
        url_key = stream_url_key(url)
        if url_key in seen_urls:
            errors.append(f"Duplicate stream URL: {url}")
        seen_urls.add(url_key)

        a = attrs(info)
        group = a.get("group-title", "").strip()
        if group in LEGACY_GROUPS:
            info = set_group(info, LEGACY_GROUPS[group])
            group = LEGACY_GROUPS[group]
            stats["legacy_review_renamed"] += 1
        if not group or group not in GROUP_ORDER:
            info = set_group(info, "Review")
            group = "Review"
            stats["unknown_groups_quarantined"] += 1

        name = display_name(info)
        a = attrs(info)
        if name and not a.get("tvg-name", "").strip():
            info = set_attr(info, "tvg-name", name)
            stats["metadata_fields_filled"] += 1
        elif name and a.get("tvg-name", "").strip() != name:
            info = set_display(info, a["tvg-name"].strip())

        a = attrs(info)
        tvg_id = a.get("tvg-id", "").strip()
        channel_id = a.get("channel-id", "").strip()
        if not tvg_id and channel_id:
            info = set_attr(info, "tvg-id", channel_id)
            stats["metadata_fields_filled"] += 1
        elif not channel_id and tvg_id:
            info = set_attr(info, "channel-id", tvg_id)
            stats["metadata_fields_filled"] += 1

        if not identity_ids(info) and group in PRIMARY_GROUPS + ["Backup"]:
            info = set_group(info, "Review")
            group = "Review"

        # A missing or unverified logo is a publish-gate issue, not permission
        # to reclassify an owner-curated primary. Keep its group, number, stream
        # URL, and channel identity unchanged; remove only an unsafe logo ref.
        logo = attrs(info).get("tvg-logo", "").strip()
        logo_name = logo.split("?", 1)[0].rsplit("/", 1)[-1]
        valid_local_logo = logo.startswith(RAW_LOGO_BASE) and not is_blocked_logo_basename(logo_name)
        if group in PRIMARY_GROUPS and not valid_local_logo:
            info = remove_attr(info, "tvg-logo")
            stats["missing_logos_unresolved"].append(display_name(info))

        if group in REVIEW_GROUPS and attrs(info).get("tvg-chno"):
            info = remove_attr(info, "tvg-chno")
        record[0] = info

    primary_by_id: dict[str, int] = {}
    for index, record in enumerate(records):
        info = record[0]
        group = attrs(info).get("group-title", "").strip()
        if group not in PRIMARY_GROUPS:
            continue
        ids = identity_ids(info)
        if not ids:
            record[0] = set_group(info, "Review")
            stats["unknown_groups_quarantined"] += 1
            continue
        duplicate_of = next((primary_by_id[value] for value in sorted(ids) if value in primary_by_id), None)
        if duplicate_of is not None:
            record[0] = set_group(info, "Backup")
            stats["duplicate_primary_demoted"] += 1
            continue
        for value in ids:
            primary_by_id[value] = index

    # Build a unique-name index only for a tightly controlled fallback. It is
    # used to link a known alternate spelling (Jalsha Movies) to its existing
    # primary ID; it never promotes a second primary copy.
    primary_by_name: dict[str, set[int]] = defaultdict(set)
    for index, record in enumerate(records):
        info = record[0]
        if attrs(info).get("group-title", "").strip() in PRIMARY_GROUPS:
            primary_by_name[normalized_channel_name(display_name(info))].add(index)

    # Reconcile each Backup by exact identity first. Known orphan candidates are
    # promoted once into an appropriate active genre; additional URLs for the
    # same identity remain Backup. Indian news/kids/religious candidates stay
    # Review. Unique exact-name matches only link an alternate stream to one
    # existing primary; they never create another primary.
    for record in records:
        info = record[0]
        if attrs(info).get("group-title", "").strip() != "Backup":
            continue
        ids = identity_ids(info)
        matches = {primary_by_id[value] for value in ids if value in primary_by_id}

        if not matches:
            migration_targets = {
                MIGRATION_GROUP_BY_ID[value]
                for value in ids if value in MIGRATION_GROUP_BY_ID
            }
            if len(migration_targets) == 1:
                target = next(iter(migration_targets))
                if target == "Review":
                    record[0] = set_group(info, "Review")
                    stats["orphan_backups_quarantined"] += 1
                    stats["restricted_backups_reviewed"] += 1
                    continue
                if target in PRIMARY_GROUPS:
                    if "ntv.in" in ids and not attrs(info).get("tvg-logo", "").strip():
                        info = set_attr(info, "tvg-logo", RAW_LOGO_BASE + "ntv-malayalam.svg")
                    info = set_group(info, target)
                    info = remove_attr(info, "tvg-chno")
                    record[0] = info
                    primary_index = records.index(record)
                    for value in identity_ids(info):
                        primary_by_id[value] = primary_index
                    primary_by_name[normalized_channel_name(display_name(info))].add(primary_index)
                    stats["orphan_backups_promoted"] += 1
                    continue

            name_key = normalized_channel_name(display_name(info))
            name_matches = primary_by_name.get(name_key, set()) if name_key else set()
            if len(name_matches) == 1:
                match_index = next(iter(name_matches))
                primary_info = records[match_index][0]
                primary_ids = identity_ids(primary_info)
                if len(primary_ids) == 1:
                    canonical_id = next(iter(primary_ids))
                    info = set_attr(info, "tvg-id", canonical_id)
                    info = set_attr(info, "channel-id", canonical_id)
                    record[0] = info
                    matches = {match_index}
                    stats["name_matched_backups_linked"] += 1

        if len(matches) != 1:
            record[0] = set_group(info, "Review")
            stats["orphan_backups_quarantined"] += 1
            continue

        primary_info = records[next(iter(matches))][0]
        pa = attrs(primary_info)
        before = info
        current_attrs = attrs(info)
        for key in ("tvg-name", "tvg-country", "tvg-language"):
            primary_value = pa.get(key, "").strip()
            current_value = current_attrs.get(key, "").strip()
            if primary_value and (
                not current_value
                or current_value.casefold() != primary_value.casefold()
                and (key != "tvg-language" or primary_value.casefold() != "und")
            ):
                info = set_attr(info, key, primary_value)
        current_logo = attrs(info).get("tvg-logo", "").strip()
        primary_logo = pa.get("tvg-logo", "").strip()
        if (not current_logo or not current_logo.startswith(RAW_LOGO_BASE)) and primary_logo.startswith(RAW_LOGO_BASE):
            info = set_attr(info, "tvg-logo", primary_logo)
        if info != before:
            stats["backup_metadata_reconciled"] += 1
        record[0] = info

    # Unknown language is explicitly marked undetermined, never guessed.
    for record in records:
        info = record[0]
        a = attrs(info)
        if not a.get("tvg-language", "").strip():
            info = set_attr(info, "tvg-language", "und")
            stats["metadata_fields_filled"] += 1
            stats["undetermined_languages"].append(display_name(info))
        a = attrs(info)
        if not a.get("tvg-country", "").strip():
            inferred = country_from_id(a.get("tvg-id") or a.get("channel-id", ""))
            if inferred:
                info = set_attr(info, "tvg-country", inferred)
                stats["metadata_fields_filled"] += 1
            elif a.get("group-title", "").strip() not in REVIEW_GROUPS:
                errors.append(f"{display_name(info)}: missing tvg-country and no country suffix in ID")
        a = attrs(info)
        group = a.get("group-title", "").strip()
        if group not in REVIEW_GROUPS:
            if not a.get("tvg-name", "").strip():
                errors.append(f"Active/Backup entry missing tvg-name: {display_name(info)}")
            if not (a.get("tvg-id", "").strip() and a.get("channel-id", "").strip()):
                errors.append(f"Active/Backup entry missing tvg-id or channel-id: {display_name(info)}")
            if not a.get("tvg-logo", "").strip():
                errors.append(f"Active/Backup entry missing local logo: {display_name(info)}")
            elif not a["tvg-logo"].startswith(RAW_LOGO_BASE):
                errors.append(f"Active/Backup entry has non-local logo: {display_name(info)}")
            if not a.get("tvg-country", "").strip():
                errors.append(f"Active/Backup entry missing tvg-country: {display_name(info)}")
        record[0] = info

    check_primary: dict[str, list[str]] = defaultdict(list)
    for record in records:
        info = record[0]
        if attrs(info).get("group-title", "").strip() in PRIMARY_GROUPS:
            for value in identity_ids(info):
                check_primary[value].append(display_name(info))
    duplicate_ids = {key: names for key, names in check_primary.items() if len(names) > 1}
    if duplicate_ids:
        errors.append("Duplicate primary identities remain: " + ", ".join(sorted(duplicate_ids)[:10]))

    primary_ids = set(primary_by_id)
    orphan_names = []
    for record in records:
        info = record[0]
        if attrs(info).get("group-title", "").strip() == "Backup" and not (identity_ids(info) & primary_ids):
            orphan_names.append(display_name(info))
    if orphan_names:
        errors.append("Orphan Backup entries remain: " + ", ".join(orphan_names[:20]))

    for record in records:
        info = record[0]
        group = attrs(info).get("group-title", "").strip()
        if group in REVIEW_GROUPS:
            info = remove_attr(info, "tvg-chno")
            review_logo = attrs(info).get("tvg-logo", "").strip()
            if review_logo:
                logo_name = review_logo.split("?", 1)[0].rsplit("/", 1)[-1]
                if not review_logo.startswith(RAW_LOGO_BASE) or is_blocked_logo_basename(logo_name):
                    info = remove_attr(info, "tvg-logo")
                    stats["review_invalid_logos_cleared"] += 1
            record[0] = info

    for record in records:
        record[0] = canonicalize_extinf(record[0])

    rank = {name: index for index, name in enumerate(GROUP_ORDER)}
    # Stable category-only sort: enforce the user's category order while
    # preserving the relative order of all rows inside each category.
    records.sort(key=lambda record: rank.get(attrs(record[0]).get("group-title", "").strip(), len(rank)))
    preamble = update_registry(preamble)
    updated = "\n".join(preamble + [line for record in records for line in record]).rstrip() + "\n"

    stats["missing_logos_deferred"] = [
        display_name(record[0]) for record in records
        if not attrs(record[0]).get("tvg-logo", "").strip()
        and attrs(record[0]).get("group-title", "").strip() in REVIEW_GROUPS
    ]
    stats["review_entries"] = sum(
        1 for record in records
        if attrs(record[0]).get("group-title", "").strip() in REVIEW_GROUPS
    )
    stats["backup_entries"] = sum(
        1 for record in records
        if attrs(record[0]).get("group-title", "").strip() == "Backup"
    )
    stats["primary_entries"] = sum(
        1 for record in records
        if attrs(record[0]).get("group-title", "").strip() in PRIMARY_GROUPS
    )
    return updated, stats, errors


def write_report(stats: dict[str, object], errors: list[str]) -> None:
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Primary / Backup Integrity",
        "",
        f"- Primary entries: **{stats.get('primary_entries', 0)}**",
        f"- Backup entries: **{stats.get('backup_entries', 0)}**",
        f"- Review-only entries (Review / New Channels / New Backups): **{stats.get('review_entries', 0)}**",
        f"- Duplicate primary copies moved to Backup: **{stats.get('duplicate_primary_demoted', 0)}**",
        f"- Orphan Backup entries moved to Review: **{stats.get('orphan_backups_quarantined', 0)}**",
        f"- Owner-authorized orphan Backup entries removed: **{stats.get('user_authorized_orphan_backups_removed', 0)}**",
        f"- Verified orphan Backup streams promoted to a primary genre: **{stats.get('orphan_backups_promoted', 0)}**",
        f"- Backup rows linked to an existing primary by unique exact name: **{stats.get('name_matched_backups_linked', 0)}**",
        f"- Restricted Indian news/kids/religious rows retained in Review: **{stats.get('restricted_backups_reviewed', 0)}**",
        f"- Legacy Not Playing groups renamed to Review: **{stats.get('legacy_review_renamed', 0)}**",
        f"- Active channels retained with unresolved logos (not reclassified): **{len(stats.get('missing_logos_unresolved', []))}**",
        f"- Kids entries moved from Review to Kids: **{stats.get('kids_promoted_from_review', 0)}**",
        f"- Explicitly removed non-kids Review entries: **{stats.get('non_kids_review_removed', 0)}**",
        f"- Backup metadata records reconciled from exact primary IDs: **{stats.get('backup_metadata_reconciled', 0)}**",
        f"- Missing language values set to und (undetermined): **{len(stats.get('undetermined_languages', []))}**",
        "",
        "Unknown languages are marked und; no language is guessed. Incomplete logos are retained only in Review queues.",
        "",
        "## Missing logos deferred to Review",
        "",
    ]
    missing = stats.get("missing_logos_deferred", [])
    lines.extend(f"- {name}" for name in missing) if missing else lines.append("None.")
    lines += ["", "## Blocking validation errors", ""]
    lines.extend(f"- {error}" for error in errors) if errors else lines.append("None.")
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if repair changes are still required")
    args = parser.parse_args()
    if not PLAYLIST.is_file():
        raise SystemExit(f"Playlist not found: {PLAYLIST}")
    before = PLAYLIST.read_text(encoding="utf-8-sig")
    updated, stats, errors = repair_playlist_text(before)
    write_report(stats, errors)
    if errors:
        for error in errors:
            print(f"::error::{error}")
        return 1
    if args.check and updated != before:
        raise SystemExit("Primary/Backup integrity changes are still required.")
    if not args.check and updated != before:
        PLAYLIST.write_text(updated, encoding="utf-8", newline="")
    print(
        "Primary/Backup integrity: "
        f"primary={stats['primary_entries']} backup={stats['backup_entries']} "
        f"review={stats['review_entries']} demoted={stats['duplicate_primary_demoted']} "
        f"orphan_backups_quarantined={stats['orphan_backups_quarantined']} "
        f"owner_authorized_orphan_backups_removed={stats['user_authorized_orphan_backups_removed']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
