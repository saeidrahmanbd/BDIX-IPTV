#!/usr/bin/env python3
"""Reconcile orphan Backups and promote reachable New Channels/New Backups."""
from __future__ import annotations
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

from discover_bd_in_new_queues import prohibited_channel
from country_verification import reference_from_playlists, verify_country

PLAYLIST = Path("IPTV-Playlist.m3u")
PROBES = Path("/tmp/iptv-owner-requested-probes.json")
APPROVALS = Path("/tmp/iptv-owner-requested-migrations.json")
REPORT = Path("reports/owner-requested-main-migrations.md")
RAW_BASE = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/"
ATTR = re.compile(r'([\w-]+)="([^"]*)"')
PRIMARY = {
    "Bangladesh", "Indian Bangla", "Indian Movies", "Indian Music",
    "Indian Entertainment", "Pakistani", "International",
    "Documentary & Wildlife", "Kids", "Religious", "Sports",
}
QUEUE = {"New Channels", "New Backups", "New Backup"}
GROUP_ORDER = [
    "Bangladesh", "Indian Bangla", "Indian Movies", "Indian Music",
    "Indian Entertainment", "Pakistani", "International",
    "Documentary & Wildlife", "Kids", "Religious", "Sports",
    "Backup", "New Channels", "New Backups", "Review",
]
QUALITY = {"hd", "sd", "fhd", "uhd", "4k", "1080p", "720p", "576p", "480p", "360p"}
KIDS = re.compile(r"\b(kids?|cartoon|pogo|nick(?:elodeon)?|disney\s*(?:jr|junior)|hungama|baby\s*tv|toon|zbcartoon)\b", re.I)
SPORTS = re.compile(r"\b(sports?|cricket|football|soccer|wrestling|boxing|ufc|espn|ten\s*sports|sony\s*sports|star\s*sports|bein\s*sports|willow|eurosport)\b", re.I)
MOVIE = re.compile(r"\b(movie|movies|cinema|film|films|bollywood|hollywood|pictures|cineplex|plex)\b", re.I)
MUSIC = re.compile(r"\b(music|mtv|vh1|9xm|mastiii|sangeet|vevo|music\s*box)\b", re.I)
DOC = re.compile(r"\b(documentary|wildlife|nature|animal\s*planet|national\s*geographic|nat\s*geo|discovery\s*science)\b", re.I)
ISLAMIC = re.compile(r"\b(islam|islamic|muslim|qur.?an|madani|peace\s*tv|huda|noor|deen|ummah|makkah|madina|sunnah)\b", re.I)
ATTR_ORDER = ("tvg-id", "tvg-name", "tvg-logo", "tvg-chno", "channel-id", "tvg-country", "tvg-language", "group-title")

def attrs(info):
    return dict(ATTR.findall(info))

def split_info(info):
    quoted = False
    for i, ch in enumerate(info):
        if ch == '"':
            quoted = not quoted
        elif ch == "," and not quoted:
            return info[:i], info[i + 1:]
    return info, ""

def set_attr(info, key, value):
    pattern = re.compile(rf'\s+{re.escape(key)}="[^"]*"')
    if pattern.search(info):
        return pattern.sub(f' {key}="{value}"', info, count=1)
    head, display = split_info(info)
    marker = re.search(r'\s+group-title="', head)
    at = marker.start() if marker else len(head)
    return head[:at] + f' {key}="{value}"' + head[at:] + ("," + display if display else "")

def remove_attr(info, key):
    return re.sub(rf'\s+{re.escape(key)}="[^"]*"', "", info, count=1)

def set_group(info, group):
    return set_attr(info, "group-title", group)

def set_display(info, name):
    head, _ = split_info(info)
    return head + "," + name

def name_key(value):
    value = unicodedata.normalize("NFKD", str(value or "")).casefold()
    value = re.sub(r"\([^)]*\)|\[[^]]*\]", " ", value)
    value = re.sub(r"\b(?:backup|hd|fhd|uhd|sd|4k|1080p|720p|576p|480p|360p)\b", " ", value)
    value = re.sub(r"[^a-z0-9]+", "", value)
    return value

def id_key(value):
    value = str(value or "").strip().casefold()
    if not value:
        return ""
    return value.split("@", 1)[0]


def normalized_label(value):
    """Remove technical feed prefixes/suffixes while preserving channel identity."""
    value = unicodedata.normalize("NFKC", str(value or "")).strip()
    value = re.sub(r"^(?:\[[A-Z]{2,3}\]\s*|[A-Z]{2,3}\s*[|:/-]\s*)", "", value, flags=re.I)
    quality = r"(?:HD|FHD|UHD|SD|4K|\d{3,4}p|\d{3,4}i)"
    value = re.sub(rf"\s*[\(\[]\s*{quality}\s*[\)\]]\s*$", "", value, flags=re.I)
    value = re.sub(rf"\s+{quality}\s*$", "", value, flags=re.I)
    value = re.sub(r"\s*[-_]\s*", " ", value)
    return re.sub(r"\s+", " ", value).strip(" -|:")

def country_for(a):
    country = (a.get("tvg-country") or "").strip().upper()
    if re.fullmatch(r"[A-Z]{2}", country):
        return country
    for value in (a.get("tvg-id"), a.get("channel-id")):
        match = re.search(r"\.([a-z]{2})(?:@|$)", str(value or ""), re.I)
        if match:
            return match.group(1).upper()
    return ""

def local_png_exists(logo):
    logo = str(logo or "").strip()
    if not logo.startswith(RAW_BASE) or not logo.lower().endswith(".png"):
        return False
    relative = logo[len(RAW_BASE):].split("?", 1)[0].split("#", 1)[0]
    target = (Path("logos") / relative).resolve()
    root = Path("logos").resolve()
    return target != root and root in target.parents and target.is_file()

def parse_playlist(text):
    preamble, records, current = [], [], None
    for line in text.replace("\r\n", "\n").replace("\r", "\n").splitlines():
        if line.startswith("#EXTINF:"):
            if current is not None:
                records.append(current)
            current = [line]
        elif current is None:
            preamble.append(line)
        else:
            current.append(line)
            if line.strip().lower().startswith(("http://", "https://")):
                records.append(current)
                current = None
    if current is not None:
        records.append(current)
    return preamble, records

def url_of(record):
    return next((line.strip() for line in record[1:] if line.strip().lower().startswith(("http://", "https://"))), "")

def display_name(info):
    a = attrs(info)
    _, display = split_info(info)
    return (a.get("tvg-name") or display).strip()

def country_matches(left, right):
    lc, rc = country_for(left), country_for(right)
    return not lc or not rc or lc == rc

def primary_match(info, rows):
    a = attrs(info)
    ids = {id_key(x) for x in (a.get("tvg-id"), a.get("channel-id")) if id_key(x)}
    name = name_key(display_name(info))
    id_matches, name_matches = [], []
    for row in rows:
        pa = attrs(row[0])
        pids = {id_key(x) for x in (pa.get("tvg-id"), pa.get("channel-id")) if id_key(x)}
        if ids & pids:
            id_matches.append(row)
        elif name and name_key(display_name(row[0])) == name and country_matches(a, pa):
            name_matches.append(row)
    if len(id_matches) == 1:
        return id_matches[0]
    if len(id_matches) > 1:
        return None
    return name_matches[0] if len(name_matches) == 1 else None

def target_group(a, name, pakistani_count):
    country = country_for(a)
    language = (a.get("tvg-language") or "und").strip().casefold()
    evidence = " ".join((name, a.get("tvg-name", ""), a.get("tvg-id", ""),
                         a.get("channel-id", ""), a.get("tvg-content", "")))
    content = (a.get("tvg-content") or "").casefold()
    if not country:
        return None
    if country == "IN":
        # Keep the established Indian restrictions; Kids and Sports are allowed.
        if prohibited_channel(a, name, "IN", discovery=True):
            return None
    if KIDS.search(evidence) or content == "kids":
        return "Kids"
    if SPORTS.search(evidence) or content in {"sports", "sport"}:
        return "Sports"
    if DOC.search(evidence) or content in {"documentary", "wildlife"}:
        return "Documentary & Wildlife"
    if country == "IN":
        if MOVIE.search(evidence) or content in {"movie", "movies", "film"}:
            return "Indian Movies"
        if MUSIC.search(evidence) or content in {"music", "musics"}:
            return "Indian Music"
        if language in {"ben", "bn", "bengali", "ben-eng"} or re.search(r"\b(bangla|bengali)\b", evidence, re.I):
            return "Indian Bangla"
        if ISLAMIC.search(evidence):
            return None
        return "Indian Entertainment"
    if country == "BD" or (language in {"ben", "bn", "bengali"} and country != "IN"):
        if ISLAMIC.search(evidence):
            return "Religious"
        if re.search(r"\b(religious|quran|islamic|church|hindu|buddhist)\b", evidence, re.I):
            return None
        return "Bangladesh"
    if country == "PK":
        return "Pakistani" if pakistani_count >= 5 else "International"
    if ISLAMIC.search(evidence):
        return "Religious"
    if re.search(r"\b(religious|church|hindu|buddhist)\b", evidence, re.I):
        return None
    # The main playlist already uses these genre groups for eligible non-BD/IN services.
    return "International"

def migrate(text, probe_data):
    preamble, records = parse_playlist(text)
    probe_by_url = {row["url"]: row for row in probe_data.get("results", [])}
    # Only promote candidates whose BD/IN identity is independently verified.
    # Provisional or incorrect queue country metadata remains a manual-review warning.
    country_reference = reference_from_playlists([PLAYLIST, Path("International-Playlist.m3u")])
    # One-time owner-requested metadata cleanup. Channel IDs and stream URLs
    # remain unchanged; only feed-quality labels and supported metadata are fixed.
    normalized_names = 0
    metadata_fields_filled = 0
    for record in records:
        info = record[0]
        a = attrs(info)
        old_name = display_name(info)
        new_name = normalized_label(old_name)
        if (a.get("tvg-id", "").casefold() == "mov.bollywood.old.in"
                or a.get("channel-id", "").casefold() == "mov.bollywood.old.in"):
            new_name = "Hindi Movie Classic 24"
        if new_name and new_name != old_name:
            info = set_attr(info, "tvg-name", new_name)
            info = set_display(info, new_name)
            normalized_names += 1
        elif new_name and not a.get("tvg-name", "").strip():
            info = set_attr(info, "tvg-name", new_name)
            metadata_fields_filled += 1
        a = attrs(info)
        if not a.get("tvg-id", "").strip() and a.get("channel-id", "").strip():
            info = set_attr(info, "tvg-id", a["channel-id"].strip())
            metadata_fields_filled += 1
        elif not a.get("channel-id", "").strip() and a.get("tvg-id", "").strip():
            info = set_attr(info, "channel-id", a["tvg-id"].strip())
            metadata_fields_filled += 1
        a = attrs(info)
        country = country_for(a)
        if not a.get("tvg-country", "").strip() and country:
            info = set_attr(info, "tvg-country", country)
            metadata_fields_filled += 1
        if not a.get("tvg-language", "").strip():
            info = set_attr(info, "tvg-language", "und")
            metadata_fields_filled += 1
        elif a.get("tvg-language", "").strip() != a["tvg-language"].strip().lower():
            info = set_attr(info, "tvg-language", a["tvg-language"].strip().lower())
        record[0] = info
    initial_primary = [r for r in records if attrs(r[0]).get("group-title", "").strip() in PRIMARY]
    pakistani_count = len({id_key(attrs(r[0]).get("tvg-id") or attrs(r[0]).get("channel-id")) for r in initial_primary
                           if attrs(r[0]).get("group-title", "").strip() == "Pakistani"})
    changes, approvals, stats = [], [], Counter()
    if normalized_names:
        stats["channel_names_normalized"] += normalized_names
    if metadata_fields_filled:
        stats["metadata_fields_completed"] += metadata_fields_filled
    primary_rows = list(initial_primary)

    # First reconcile alternate IDs/names to a unique existing primary identity.
    for record in records:
        info = record[0]
        if attrs(info).get("group-title", "").strip() != "Backup":
            continue
        match = primary_match(info, primary_rows)
        if not match:
            continue
        primary = attrs(match[0])
        before = info
        for key in ("tvg-id", "channel-id", "tvg-name", "tvg-country", "tvg-language"):
            value = primary.get(key, "").strip()
            if value:
                info = set_attr(info, key, value)
        logo = primary.get("tvg-logo", "").strip()
        if local_png_exists(logo):
            info = set_attr(info, "tvg-logo", logo)
        if info != before:
            record[0] = info
            approvals.append({"url": url_of(record), "source_group": "Backup",
                              "target_group": "Backup", "allow_metadata": True})
            stats["backup_metadata_reconciled"] += 1
            changes.append((display_name(before), "Backup", "Backup", "matched unique primary identity; metadata reconciled"))

    # Promote reachable queue entries and eligible orphan Backup streams. Failed
    # candidates go to Review without deleting their URLs; pre-existing Review
    # entries are deliberately untouched.
    candidates = []
    for record in records:
        group = attrs(record[0]).get("group-title", "").strip()
        if group in QUEUE:
            candidates.append(record)
        elif group == "Backup" and not primary_match(record[0], primary_rows):
            candidates.append(record)

    for record in candidates:
        info, url = record[0], url_of(record)
        a = attrs(info)
        old_group = a.get("group-title", "").strip()
        probe = probe_by_url.get(url)
        if not probe:
            continue
        name = display_name(info)
        if not probe.get("ok"):
            if old_group != "Review":
                record[0] = remove_attr(set_group(info, "Review"), "tvg-chno")
                approvals.append({"url": url, "source_group": old_group,
                                  "target_group": "Review", "allow_metadata": True})
                stats["not_streaming_to_review"] += 1
                changes.append((name, old_group, "Review", probe.get("error") or f"HTTP {probe.get('status')}"))
            continue

        match = primary_match(info, primary_rows)
        if match:
            pa = attrs(match[0])
            before = info
            for key in ("tvg-id", "channel-id", "tvg-name", "tvg-country", "tvg-language"):
                value = pa.get(key, "").strip()
                if value:
                    info = set_attr(info, key, value)
            logo = pa.get("tvg-logo", "").strip()
            if local_png_exists(logo):
                info = set_attr(info, "tvg-logo", logo)
            if old_group in QUEUE:
                logo = attrs(info).get("tvg-logo", "").strip()
                if not local_png_exists(logo):
                    info = remove_attr(info, "tvg-logo")
                    record[0] = info
                    stats["queue_alternates_without_local_logo_deferred"] += 1
                    changes.append((name, old_group, old_group, "reachable alternate; authentic local PNG logo still needs repair"))
                    continue
                info = set_group(info, "Backup")
                info = remove_attr(info, "tvg-chno")
                approvals.append({"url": url, "source_group": old_group,
                                  "target_group": "Backup", "allow_metadata": True})
                stats["queue_alternates_to_backup"] += 1
                changes.append((name, old_group, "Backup", "reachable alternate for an existing primary"))
            elif old_group == "Backup":
                stats["orphan_aliases_linked"] += 1
                if info != before:
                    approvals.append({"url": url, "source_group": "Backup",
                                      "target_group": "Backup", "allow_metadata": True})
                    changes.append((name, "Backup", "Backup", "unique name/ID alias linked to primary"))
            record[0] = info
            continue

        verdict = verify_country(a, name, country_reference)
        if not verdict.ok:
            if old_group == "Backup":
                record[0] = remove_attr(set_group(info, "New Channels"), "tvg-chno")
                approvals.append({"url": url, "source_group": old_group,
                                  "target_group": "New Channels", "allow_metadata": True})
                stats["unverified_orphans_staged_for_manual_review"] += 1
                changes.append((name, "Backup", "New Channels",
                                "reachable, but BD/IN country identity is not independently verified"))
            else:
                stats["unverified_queue_candidates_deferred"] += 1
                changes.append((name, old_group, old_group,
                                "reachable, but BD/IN country identity is not independently verified"))
            continue
        # Fill country/ID only from the independent verification result.
        if not a.get("tvg-country", "").strip():
            info = set_attr(info, "tvg-country", verdict.country)
        if verdict.tvg_id and not a.get("tvg-id", "").strip():
            info = set_attr(info, "tvg-id", verdict.tvg_id)
        if not attrs(info).get("channel-id", "").strip() and attrs(info).get("tvg-id", "").strip():
            info = set_attr(info, "channel-id", attrs(info)["tvg-id"])
        record[0] = info
        a = attrs(info)
        target = target_group(a, name, pakistani_count)
        if not target:
            if old_group == "Backup":
                record[0] = remove_attr(set_group(info, "New Channels"), "tvg-chno")
                approvals.append({"url": url, "source_group": "Backup",
                                  "target_group": "New Channels", "allow_metadata": True})
                stats["unclassified_orphans_staged_for_manual_review"] += 1
                changes.append((name, "Backup", "New Channels", "reachable, but country/genre eligibility needs owner review"))
            elif old_group in QUEUE:
                record[0] = remove_attr(info, "tvg-logo")
                stats["queue_policy_review_deferred"] += 1
                changes.append((name, old_group, old_group, "country/genre eligibility not established; left in discovery queue"))
            continue
        logo = a.get("tvg-logo", "").strip()
        if not local_png_exists(logo):
            # A reachable orphan is not a non-streaming Review entry. Keep it
            # staged until an authentic local PNG can be attached.
            if old_group == "Backup":
                record[0] = remove_attr(set_group(info, "New Channels"), "tvg-chno")
                approvals.append({"url": url, "source_group": "Backup",
                                  "target_group": "New Channels", "allow_metadata": True})
                stats["orphan_without_local_logo_staged"] += 1
                changes.append((name, "Backup", "New Channels", "reachable; authentic local PNG logo still needs repair"))
            elif old_group in QUEUE:
                record[0] = remove_attr(info, "tvg-logo")
                stats["queue_without_local_logo_deferred"] += 1
                changes.append((name, old_group, old_group, "authentic local PNG not available; left in discovery queue"))
            continue
        cid = (a.get("tvg-id") or a.get("channel-id") or "").strip()
        if not cid:
            if old_group == "Backup":
                record[0] = remove_attr(set_group(info, "New Channels"), "tvg-chno")
                approvals.append({"url": url, "source_group": "Backup",
                                  "target_group": "New Channels", "allow_metadata": True})
                stats["orphan_without_identity_staged"] += 1
            elif old_group in QUEUE:
                record[0] = remove_attr(info, "tvg-logo")
                stats["queue_without_identity_deferred"] += 1
            continue
        info = set_group(info, target)
        info = set_attr(info, "tvg-id", cid)
        info = set_attr(info, "channel-id", cid)
        country = country_for(a)
        if country and not a.get("tvg-country", "").strip():
            info = set_attr(info, "tvg-country", country)
        if not a.get("tvg-language", "").strip():
            info = set_attr(info, "tvg-language", "und")
        info = remove_attr(info, "tvg-chno")
        record[0] = info
        if old_group == "Backup" or old_group in QUEUE:
            approvals.append({"url": url, "source_group": old_group,
                              "target_group": target, "allow_metadata": True})
        new_row = [info] + record[1:]
        primary_rows.append(new_row)
        stats["promoted_to_primary"] += 1
        changes.append((name, old_group, target, "reachable, identity and local PNG logo verified"))

    # Enforce a single primary identity; retain a duplicate stream as Backup.
    seen_id, seen_name = {}, {}
    for record in records:
        info = record[0]
        a = attrs(info)
        group = a.get("group-title", "").strip()
        if group not in PRIMARY:
            continue
        name = display_name(info)
        cid = id_key(a.get("tvg-id") or a.get("channel-id"))
        country = country_for(a)
        nkey = (name_key(name), country)
        duplicate = seen_id.get(cid) if cid else None
        if duplicate is None and nkey[0]:
            duplicate = seen_name.get(nkey)
        if duplicate is not None:
            canonical = attrs(duplicate[0])
            for key in ("tvg-id", "channel-id", "tvg-name", "tvg-country", "tvg-language", "tvg-logo"):
                value = canonical.get(key, "").strip()
                if value:
                    info = set_attr(info, key, value)
            info = remove_attr(set_group(info, "Backup"), "tvg-chno")
            record[0] = info
            approvals.append({"url": url_of(record), "source_group": group,
                              "target_group": "Backup", "allow_metadata": True})
            stats["duplicate_primary_demoted_to_backup"] += 1
            changes.append((name, group, "Backup", "duplicate primary identity retained as alternate stream"))
            continue
        if cid:
            seen_id[cid] = record
        if nkey[0]:
            seen_name[nkey] = record

    # Keep the canonical group registry synchronized. The normal maintenance
    # sort/renumber steps reassemble blocks and assign primary channel numbers.
    registry = "#PLAYLIST-STUDIO-CATEGORIES:" + json.dumps(GROUP_ORDER, ensure_ascii=False)
    replaced = False
    for i, line in enumerate(preamble):
        if line.startswith("#PLAYLIST-STUDIO-CATEGORIES:"):
            if not replaced:
                preamble[i] = registry
                replaced = True
            else:
                preamble[i] = ""
    if not replaced:
        at = next((i + 1 for i, line in enumerate(preamble) if line.startswith("#EXTM3U")), 0)
        preamble.insert(at, registry)

    updated = "\n".join([x for x in preamble if x != ""] +
                       [line for record in records for line in record]).rstrip() + "\n"

    # The approval list is exact-URL scoped. Preserve entries from a first pass
    # when the workflow runs its automatic correction pass a second time.
    prior = []
    if APPROVALS.is_file():
        try:
            prior = json.loads(APPROVALS.read_text(encoding="utf-8"))
        except Exception:
            prior = []
    by_key = {}
    for item in prior + approvals:
        if item.get("url"):
            by_key[(item["url"], item.get("source_group"), item.get("target_group"))] = item
    APPROVALS.write_text(json.dumps(list(by_key.values()), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    report = [
        "# Owner-Requested Main Playlist Migrations", "",
        "- Every existing stream URL was retained; this pass changes metadata/group placement only.",
        "- Existing Review entries were not changed. Candidates that failed the current probe were moved to Review for later rechecking.",
        "",
        "## Summary", "",
    ]
    report.extend(f"- {key.replace('_', ' ').title()}: **{value}**" for key, value in sorted(stats.items()))
    report += ["", "## Channel-level changes", "", "| Channel | Previous group | New group | Reason |", "|---|---|---|---|"]
    report.extend(f"| {n.replace('|','/')} | {old} | {new} | {reason.replace('|','/')} |" for n,old,new,reason in changes)
    if not changes:
        report.append("| — | — | — | No eligible queue/orphan migrations were needed |")
    return updated, stats, changes, approvals

def main():
    if not PROBES.is_file():
        raise SystemExit("Missing fresh owner-requested stream probes; refusing queue migration.")
    probe_data = json.loads(PROBES.read_text(encoding="utf-8"))
    original = PLAYLIST.read_text(encoding="utf-8-sig")
    updated, stats, changes, approvals = migrate(original, probe_data)
    if updated != original:
        PLAYLIST.write_text(updated, encoding="utf-8", newline="\n")
    # Regenerate the readable report using the final report data returned by migrate.
    lines = [
        "# Owner-Requested Main Playlist Migrations", "",
        "- Every existing stream URL was retained; this pass changes metadata/group placement only.",
        "- Existing Review entries were not changed. Candidates that failed the current probe were moved to Review for later rechecking.",
        "",
        "## Summary", "",
    ]
    lines.extend(f"- {key.replace('_', ' ').title()}: **{value}**" for key, value in sorted(stats.items()))
    lines += ["", "## Channel-level changes", "", "| Channel | Previous group | New group | Reason |", "|---|---|---|---|"]
    lines.extend(f"| {n.replace('|','/')} | {old} | {new} | {reason.replace('|','/')} |" for n,old,new,reason in changes)
    if not changes:
        lines.append("| — | — | — | No eligible queue/orphan migrations were needed |")
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Owner-requested migrations: {len(changes)} channel-level changes; {len(approvals)} exact transition approvals.")

if __name__ == "__main__":
    main()
