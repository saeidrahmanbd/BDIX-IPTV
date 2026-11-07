#!/usr/bin/env python3
"""Enforce one primary stream per channel and keep Backup free of orphan rows.

Distinct alternate stream URLs are preserved. Duplicate primary copies are
reclassified as Backup; Backup records without an exact primary identity are
quarantined into Review. No stream URL is rewritten or silently discarded.
"""
from __future__ import annotations

import argparse
import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

PLAYLIST = Path("IPTV-Playlist.m3u")
REPORT = Path("reports/primary-backup-integrity.md")
RAW_LOGO_BASE = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/"
ATTR = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')

PRIMARY_GROUPS = [
    "Bangladesh", "Indian Bangla", "Indian Movies", "Indian Music",
    "Indian Entertainment", "Pakistani", "International",
    "Documentary & Wildlife", "Kids", "Religious", "Sports",
]
GROUP_ORDER = PRIMARY_GROUPS + ["Backup", "Review", "New Channels", "New Backups"]
REVIEW_GROUPS = {"Review", "New Channels", "New Backups", "Not Playing"}
LEGACY_GROUPS = {"Not Playing": "Review"}

# Orphan candidates verified against channel identity and programming format.
# Indian news, kids and religious services stay out of primary categories.
MIGRATION_GROUP_BY_ID = {
    "channelwin.in@sd": "Review",
    "darshanatv.in@sd": "Review",
    "greengoldtv.in@india": "Review",
    "gtcpunjabi.in@uk": "Indian Entertainment",
    "hungama.in@sd": "Review",
    "thejunglebook.in": "Review",
    "mbctv.in@sd": "Review",
    "mhone.in@sd": "Indian Music",
    # Both feeds have failed 34 consecutive checks; retain them outside Xtream.
    "mhonedilse.in@sd": "Review",
    "mhonemovies.in": "Review",
    "mh1music.in@sd": "Indian Music",
    "mh1prime.in": "Review",
    "ntv.in": "Indian Entertainment",
    "pogo.in@sd": "Review",
    "qtv.in": "Indian Entertainment",
    "totaltvharyana.in@sd": "Review",
    "tv9bangla.in": "Review",
    "wowkidz.in@hindi": "Review",
    "wowkidztamil.in": "Review",
    "wowkidz.in@telugu": "Review",
    "zbcartoon.in": "Review",
}


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
        "unknown_groups_quarantined": 0,
        "duplicate_primary_demoted": 0,
        "orphan_backups_quarantined": 0,
        "orphan_backups_promoted": 0,
        "restricted_backups_reviewed": 0,
        "name_matched_backups_linked": 0,
        "metadata_fields_filled": 0,
        "backup_metadata_reconciled": 0,
        "missing_logos_deferred": [],
        "undetermined_languages": [],
    }
    errors: list[str] = []
    seen_urls: set[str] = set()

    for index, record in enumerate(records):
        info = record[0]
        url = stream_url(record)
        if not url:
            errors.append(f"Entry {index + 1}: missing HTTP(S) stream URL")
            continue
        url_key = url.casefold()
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
        if attrs(info).get("group-title", "").strip() in REVIEW_GROUPS:
            record[0] = remove_attr(info, "tvg-chno")

    rank = {name: index for index, name in enumerate(GROUP_ORDER)}
    records.sort(key=lambda record: (
        rank.get(attrs(record[0]).get("group-title", "").strip(), len(rank)),
        natural_key(display_name(record[0])),
        stream_url(record).casefold(),
    ))
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
        f"- Verified orphan Backup streams promoted to a primary genre: **{stats.get('orphan_backups_promoted', 0)}**",
        f"- Backup rows linked to an existing primary by unique exact name: **{stats.get('name_matched_backups_linked', 0)}**",
        f"- Restricted Indian news/kids/religious rows retained in Review: **{stats.get('restricted_backups_reviewed', 0)}**",
        f"- Legacy Not Playing groups renamed to Review: **{stats.get('legacy_review_renamed', 0)}**",
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
        f"orphan_backups_quarantined={stats['orphan_backups_quarantined']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
