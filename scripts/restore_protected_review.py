#!/usr/bin/env python3
"""Restore protected review queues without changing unrelated queue entries.

Backup and Not Playing records are restored byte-for-byte from the snapshot,
except for channel names explicitly approved for permanent removal below.
Backup-only records are never silently promoted into published categories;
unrelated stream URLs and review entries remain protected.
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

SNAPSHOT = Path("/tmp/iptv-protected-review.m3u")
BASELINE = Path("/tmp/iptv-playlist-baseline.json")
PLAYLIST = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("IPTV-Playlist.m3u")
PROTECTED = {"Backup", "Not Playing"}
PERMANENTLY_REMOVED_NAMES = {
    "accuweather",
    "america's got talent",
    "american idol",
    "baraza music tv",
    "oscar movies bhojpuri",
    "the walking dead universe",
    "popflix",
    "60 days in",
    "deadly women",
    "highway thru hell",
    "mini",
    "mundial",
    "tvc arabic kids",
}
ORDER = [
    "Bangladesh", "Indian Bangla", "Indian Movies", "Indian Music",
    "Indian Entertainment", "Pakistani", "International",
    "Documentary & Wildlife", "Kids", "Religious", "Sports", "Backup",
    "Not Playing",
]
ATTR = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')


def attrs(info: str) -> dict[str, str]:
    return dict(ATTR.findall(info))


def set_attr(info: str, key: str, value: str) -> str:
    pattern = re.compile(rf'{re.escape(key)}="[^"]*"')
    if pattern.search(info):
        return pattern.sub(f'{key}="{value}"', info, count=1)
    return info.replace("#EXTINF:-1 ", f'#EXTINF:-1 {key}="{value}" ', 1)


def remove_attr(info: str, key: str) -> str:
    return re.sub(rf'\s+{re.escape(key)}="[^"]*"', "", info, count=1)


def group_of(info: str) -> str:
    return attrs(info).get("group-title", "").strip()


def display_name(info: str) -> str:
    a = attrs(info)
    return (a.get("tvg-name") or info.rsplit(",", 1)[-1]).strip()


def normalize_name(value: str) -> str:
    value = unicodedata.normalize("NFKD", str(value or "")).casefold()
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    value = re.sub(r"\b(?:backup|hd|fhd|uhd|sd|4k|1080p|720p|576p|480p|360p)\b", " ", value)
    return re.sub(r"[^a-z0-9]+", "", value)


def is_permanently_removed(info: str) -> bool:
    # Normalize punctuation and quality suffixes so harmless name variants cannot
    # reintroduce a channel that is explicitly authorized for permanent removal.
    name = normalize_name(display_name(info))
    return name in {normalize_name(candidate) for candidate in PERMANENTLY_REMOVED_NAMES}


def identity_keys(info: str) -> set[str]:
    a = attrs(info)
    keys = set()
    for key in ("tvg-id", "channel-id"):
        value = a.get(key, "").strip().casefold()
        if value:
            keys.add("id:" + value)
    name = normalize_name(display_name(info))
    if name:
        keys.add("name:" + name)
    return keys


def parse(text: str) -> tuple[list[str], list[list[str]]]:
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


def classify_backup(info: str) -> str:
    """Choose a published category for a Backup-only channel."""
    a = attrs(info)
    name = normalize_name(display_name(info))
    country = a.get("tvg-country", "").strip().upper()
    language = a.get("tvg-language", "").strip().casefold()

    sports = (
        "sport", "sports", "espn", "star sports", "ten sports", "tsports",
        "sony sports", "sony ten", "willow", "bein sports", "supersport",
        "cricket", "football"
    )
    kids = (
        "kids", "cartoon", "nickelodeon", "nick", "pogo", "sonic",
        "hungama", "disney junior", "baby tv", "discovery kids"
    )
    religious = (
        "madani", "quran", "quran", "islam", "islamic", "deen", "peace tv",
        "noor", "huda", "ummah", "christian", "church", "gospel"
    )
    documentary = (
        "discovery", "nat geo", "national geographic", "animal planet",
        "wildlife", "history tv", "history channel", "science", "travelxp",
        "documentary"
    )
    movies = (
        "movie", "movies", "cinema", "film", "filmy", "plex", "bollywood",
        "hollywood", "cineplex"
    )
    music = (
        "music", "mtv", "9xm", "mastiii", "b4u music", "songs", "beats"
    )

    def has_any(words: tuple[str, ...]) -> bool:
        return any(normalize_name(word) in name for word in words)

    if has_any(sports):
        return "Sports"
    if has_any(kids):
        return "Kids"
    if has_any(religious):
        return "Religious"
    if has_any(documentary):
        return "Documentary & Wildlife"

    if country == "BD":
        return "Bangladesh"
    if country == "PK":
        return "Pakistani"
    if country == "IN":
        if language in {"ben", "bn", "bengali"} or any(x in name for x in ("bangla", "bengali", "kolkata")):
            return "Indian Bangla"
        if has_any(movies):
            return "Indian Movies"
        if has_any(music):
            return "Indian Music"
        return "Indian Entertainment"

    if country in {"GB", "CA", "US", "AU", "AE", "SA", "SG", "MY"} and language in {"ben", "bn", "bengali"}:
        return "Bangladesh"
    if has_any(movies):
        return "International"
    return "International"


def assign_primary_number(info: str, used: set[int], next_number: int) -> tuple[str, int]:
    a = attrs(info)
    existing = a.get("tvg-chno", "").strip()
    if existing.isdigit() and int(existing) > 0 and int(existing) not in used:
        used.add(int(existing))
        return info, max(next_number, int(existing) + 1)
    while next_number in used:
        next_number += 1
    info = set_attr(info, "tvg-chno", str(next_number))
    used.add(next_number)
    return info, next_number + 1


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

    snapshot_urls = [url_of(record).casefold() for record in snapshot_records]
    if any(not url for url in snapshot_urls) or len(snapshot_urls) != len(set(snapshot_urls)):
        raise SystemExit("ERROR: protected snapshot contains a missing or duplicate URL; refusing restore.")
    protected_occurrences_to_restore = Counter(snapshot_urls)

    baseline_by_url: dict[str, dict[str, str]] = {}
    primary_identity_keys: set[str] = set()
    for item in baseline:
        url = str(item.get("url", "")).strip()
        info = str(item.get("info", ""))
        group = str(item.get("group", "")).strip()
        if url:
            key = url.casefold()
            if key in baseline_by_url:
                raise SystemExit(
                    f"ERROR: baseline contains repeated stream URL for {url}; refusing ambiguous restore."
                )
            baseline_by_url[key] = {"url": url, "group": group, "info": info}
        if group not in PROTECTED and info and not is_permanently_removed(info):
            primary_identity_keys.update(identity_keys(info))

    used_numbers: set[int] = set()
    for record in current_records:
        a = attrs(record[0])
        if group_of(record[0]) in PROTECTED or is_permanently_removed(record[0]):
            continue
        n = a.get("tvg-chno", "").strip()
        if n.isdigit() and int(n) > 0:
            used_numbers.add(int(n))
    for record in snapshot_records:
        a = attrs(record[0])
        if group_of(record[0]) in PROTECTED or is_permanently_removed(record[0]):
            continue
        n = a.get("tvg-chno", "").strip()
        if n.isdigit() and int(n) > 0:
            used_numbers.add(int(n))
    next_number = max(used_numbers, default=0) + 1

    active_records: list[list[str]] = []
    unexpected_backup: list[list[str]] = []
    unexpected_not_playing: list[list[str]] = []
    migrated_backup: list[list[str]] = []
    restored_from_queue = 0
    reclassification_reverted = 0
    migrated_count = 0
    migration_counts: Counter[str] = Counter()
    permanently_removed_count = 0

    def process_record(record: list[str], from_snapshot: bool = False) -> None:
        nonlocal next_number, restored_from_queue, reclassification_reverted, migrated_count, permanently_removed_count
        if is_permanently_removed(record[0]):
            permanently_removed_count += 1
            return

        url = url_of(record)
        key = url.casefold()
        current_group = group_of(record[0])
        original = baseline_by_url.get(key)

        if original and original["group"] in PROTECTED and protected_occurrences_to_restore[key] > 0:
            protected_occurrences_to_restore[key] -= 1
            restored_from_queue += 1
            return

        if original and current_group in PROTECTED and original["group"] not in PROTECTED:
            record[0] = original["info"]
            current_group = group_of(record[0])
            reclassification_reverted += 1

        if current_group == "Backup":
            # A current Backup record not represented in the snapshot stays in
            # the review queue; routine maintenance must not promote it.
            unexpected_backup.append(record)
        elif current_group == "Not Playing":
            unexpected_not_playing.append(record)
        else:
            active_records.append(record)

    for record in current_records:
        process_record(record)

    snapshot_backup: list[list[str]] = []
    snapshot_not_playing: list[list[str]] = []
    for record in snapshot_records:
        if is_permanently_removed(record[0]):
            permanently_removed_count += 1
            continue
        group = group_of(record[0])
        if group == "Backup":
            # Restore every unrelated Backup entry byte-for-byte; moving any
            # entry out of this protected queue would violate the safety guard.
            snapshot_backup.append(record)
        elif group == "Not Playing":
            snapshot_not_playing.append(record)

    final_records = (
        active_records
        + migrated_backup
        + snapshot_backup
        + unexpected_backup
        + snapshot_not_playing
        + unexpected_not_playing
    )
    new_text = serialize(preamble, final_records)
    if new_text != current_text:
        PLAYLIST.write_text(new_text, encoding="utf-8", newline="\n")

    # These allowlisted removals are explicit user-authorized exceptions. Update
    # temporary safety artifacts by channel identity, while protecting every other
    # stream URL even if it happens to be shared by another record.
    has_authorized_removals = any(
        is_permanently_removed(str(item.get("info", ""))) for item in baseline
    ) or any(is_permanently_removed(record[0]) for record in snapshot_records)
    if has_authorized_removals:
        # Filter only allowlisted channel identities, never their URLs. An unrelated
        # entry sharing a stream URL must not inherit the deletion authorization.
        filtered_baseline = [
            item for item in baseline
            if not is_permanently_removed(str(item.get("info", "")))
        ]
        BASELINE.write_text(
            json.dumps(filtered_baseline, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

        filtered_snapshot = [
            record for record in snapshot_records
            if not is_permanently_removed(record[0])
        ]
        SNAPSHOT.write_text(
            serialize([], filtered_snapshot) if filtered_snapshot else "",
            encoding="utf-8",
        )

    print(
        "Protected review restore: "
        f"snapshot_backup={len(snapshot_backup)} "
        f"snapshot_not_playing={len(snapshot_not_playing)} "
        f"restored_exact={restored_from_queue} "
        f"primary_reclassifications_reverted={reclassification_reverted} "
        f"backup_migrated={migrated_count} "
        f"migration_groups={dict(sorted(migration_counts.items()))} "
        f"unexpected_backup_retained={len(unexpected_backup)} "
        f"unexpected_not_playing_retained={len(unexpected_not_playing)} "
        f"permanently_removed={permanently_removed_count}"
    )


if __name__ == "__main__":
    restore()
