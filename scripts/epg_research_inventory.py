#!/usr/bin/env python3
"""Offline EPG research inventory for IPTV-Playlist.m3u only.

Every active IPTV identity without a usable schedule in epg/epg.xml is listed (no records are
dropped). Each record gets the first failing stage of this chain, so categories are exclusive:

  1. PUBLISHED_CHANNEL_NO_PROGRAMMES  XMLTV declares the channel but has zero programme nodes
  2. NO_MAPPING_ROW                   no row for this tvg-id in reports/epg-channel-mapping.csv
  3. NO_SOURCE_MAPPING_ID             row exists but no epg_id is recorded
  4. SOURCE_NOT_VERIFIED_LATEST_FETCH epg_id recorded, but the latest fetch did not verify it
  5. SOURCE_MAPPED_NO_PUBLISHED_CHANNEL epg_id recorded, but no XMLTV channel for the tvg-id
  6. PROGRAMMES_* subcategories       programme nodes exist but none is usable now

It never fetches feeds, edits mappings or the guide, or invents IDs. Candidate IDs are only
epg_id values already in the mapping snapshot. Missing provenance is written as UNKNOWN.
"""
import csv
import hashlib
import json
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from update_epg_published_coverage import INACTIVE_GROUPS, parse_playlist, parse_time, usable_title  # noqa: E402

PLAYLIST = ROOT / "IPTV-Playlist.m3u"
GUIDE = ROOT / "epg" / "epg.xml"
MAPPING = ROOT / "reports" / "epg-channel-mapping.csv"
COVERAGE_JSON = ROOT / "reports" / "epg-iptv-coverage.json"
OUT_CSV = ROOT / "reports" / "epg-research-inventory.csv"
OUT_MD = ROOT / "reports" / "epg-research-inventory.md"

CATEGORIES = {
    "PUBLISHED_CHANNEL_NO_PROGRAMMES": (
        "XMLTV declares the channel but has no programme nodes.",
        "Needs a source feed that supplies programme nodes for this tvg-id. A channel declaration is not a schedule.",
        "Find a verified source for this tvg-id with programme nodes; verify identity before recording an epg_id.",
    ),
    "NO_MAPPING_ROW": (
        "No mapping snapshot row for this tvg-id.",
        "Needs a candidate provider channel ID with a matching schedule and identity evidence.",
        "Search public sources for an exact or strongly verified ID; add only after identity review.",
    ),
    "NO_SOURCE_MAPPING_ID": (
        "Mapping row exists, but no epg_id is recorded.",
        "Needs a candidate provider ID that carries future programmes and passes identity review.",
        "Research candidate IDs in public sources; keep ambiguous name matches in manual review.",
    ),
    "SOURCE_NOT_VERIFIED_LATEST_FETCH": (
        "epg_id is recorded, but the latest fetch did not verify it.",
        "Needs re-verification of the recorded epg_id against a current feed before reuse.",
        "Re-fetch the recorded source and confirm the ID and schedule; do not reuse it unverified.",
    ),
    "SOURCE_MAPPED_NO_PUBLISHED_CHANNEL": (
        "epg_id is recorded, but no XMLTV channel exists for the tvg-id.",
        "Needs confirmation that the epg_id exists in a fetched feed and its publication as this tvg-id.",
        "Confirm the epg_id in a fetched feed; publish only after it carries future programmes.",
    ),
    "PROGRAMMES_EXPIRED": (
        "Programme nodes exist, and all are valid but ended before now.",
        "Needs a feed carrying schedules after the current time for this channel.",
        "Look for a current feed for the recorded epg_id; expired schedules are not a mapping error by themselves.",
    ),
    "PROGRAMMES_INVALID_TIMESTAMPS": (
        "Programme nodes exist, but none has parseable start and stop times.",
        "Needs a source whose programme timestamps parse, with a verified timezone offset.",
        "Inspect the source's timestamp format and offsets before using it.",
    ),
    "PROGRAMMES_PLACEHOLDER_TITLES": (
        "Programme nodes have valid times, but every title is a placeholder or generic text.",
        "Needs a source with real programme titles for this channel.",
        "Check the source's title quality; reject sources that only publish placeholder titles.",
    ),
    "PROGRAMMES_FUTURE_BEYOND_7_DAYS": (
        "Programme nodes exist, but future ones start more than 7 days ahead, so none is usable in the window.",
        "Needs schedules that start within the 7-day publication window.",
        "Check whether the source refreshes near-term schedules; do not extend the window to pass the check.",
    ),
}
COLUMNS = [
    "category", "group", "channel", "tvg_id", "tvg_country", "tvg_language", "csv_status",
    "epg_id_recorded", "source_name", "source_url", "last_verified", "guide_channel_declared",
    "programme_nodes", "valid_time_nodes", "usable_title_nodes", "future_nodes_beyond_window",
    "usable_now", "missing_requirement", "recommended_next_action",
]


def load_mapping():
    mapping = {}
    if MAPPING.is_file():
        with MAPPING.open(encoding="utf-8-sig", newline="") as handle:
            for row in csv.DictReader(handle):
                tid = (row.get("tvg_id") or "").strip()
                if tid and tid not in mapping:
                    mapping[tid] = row
    return mapping


def scan_guide(active_ids, now):
    lower, upper = now - timedelta(hours=6), now + timedelta(days=7)
    stats = {tid: Counter() for tid in active_ids}
    declared = set()
    for _, elem in ET.iterparse(str(GUIDE), events=("end",)):
        if elem.tag == "channel":
            cid = (elem.get("id") or "").strip()
            if cid:
                declared.add(cid)
            elem.clear()
        elif elem.tag == "programme":
            cid = (elem.get("channel") or "").strip()
            if cid in stats:
                s = stats[cid]
                s["nodes"] += 1
                start, stop = parse_time(elem.get("start")), parse_time(elem.get("stop"))
                title = elem.find("title")
                if start and stop and stop > start:
                    s["valid"] += 1
                    titled = title is not None and usable_title(title.text)
                    if titled:
                        s["titled"] += 1
                    if stop >= now and start <= upper and stop >= lower and titled:
                        s["usable"] += 1
                    elif stop >= now and start > upper:
                        s["future_beyond"] += 1
            elem.clear()
    return stats, declared


def source_name(url):
    if not url:
        return "UNKNOWN"
    hosts = sorted({urlparse(part.strip()).netloc for part in url.split("|") if part.strip()})
    return ", ".join(hosts) or "UNKNOWN"


def classify(tid, row, declared, s):
    """Return (category, programme_nodes_summary) for an unusable identity."""
    if tid in declared and s["nodes"] == 0:
        return "PUBLISHED_CHANNEL_NO_PROGRAMMES"
    if row is None:
        return "NO_MAPPING_ROW"
    epg_id = (row.get("epg_id") or "").strip()
    if not epg_id:
        return "NO_SOURCE_MAPPING_ID"
    if (row.get("status") or "").strip() == "MAPPED_NOT_CURRENTLY_FOUND":
        return "SOURCE_NOT_VERIFIED_LATEST_FETCH"
    if tid not in declared:
        return "SOURCE_MAPPED_NO_PUBLISHED_CHANNEL"
    if s["nodes"] == 0:
        return "PUBLISHED_CHANNEL_NO_PROGRAMMES"
    if s["valid"] == 0:
        return "PROGRAMMES_INVALID_TIMESTAMPS"
    if s["titled"] == 0:
        return "PROGRAMMES_PLACEHOLDER_TITLES"
    if s["future_beyond"] > 0:
        return "PROGRAMMES_FUTURE_BEYOND_7_DAYS"
    return "PROGRAMMES_EXPIRED"


def main():
    now = datetime.now(timezone.utc)
    identities = {}
    for record in parse_playlist(PLAYLIST):
        attrs = record["attrs"]
        tid = (attrs.get("tvg-id") or "").strip()
        group = (attrs.get("group-title") or "").strip()
        if tid and group not in INACTIVE_GROUPS and tid not in identities:
            identities[tid] = {
                "group": group, "channel": record["name"],
                "country": (attrs.get("tvg-country") or "").strip(),
                "language": (attrs.get("tvg-language") or "").strip(),
            }
    active = set(identities)
    mapping = load_mapping()
    stats, declared = scan_guide(active, now)
    usable = {tid for tid in active if stats[tid]["usable"] > 0}

    rows = []
    for tid in sorted(active, key=lambda t: (identities[t]["group"].casefold(), identities[t]["channel"].casefold(), t)):
        if tid in usable:
            continue
        info, row, s = identities[tid], mapping.get(tid), stats[tid]
        category = classify(tid, row, declared, s)
        epg_id = (row.get("epg_id") or "").strip() if row else ""
        status = (row.get("status") or "").strip() if row else ""
        url = (row.get("source") or "").strip() if row else ""
        rows.append({
            "category": category, "group": info["group"], "channel": info["channel"], "tvg_id": tid,
            "tvg_country": info["country"], "tvg_language": info["language"], "csv_status": status or "UNKNOWN",
            "epg_id_recorded": epg_id or "UNKNOWN", "source_name": source_name(url), "source_url": url or "UNKNOWN",
            "last_verified": "UNKNOWN",
            "guide_channel_declared": "yes" if tid in declared else "no",
            "programme_nodes": s["nodes"], "valid_time_nodes": s["valid"], "usable_title_nodes": s["titled"],
            "future_nodes_beyond_window": s["future_beyond"], "usable_now": "no",
            "missing_requirement": CATEGORIES[category][1], "recommended_next_action": CATEGORIES[category][2],
        })

    with OUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)

    by_cat = Counter(r["category"] for r in rows)
    by_group = {}
    for r in rows:
        by_group.setdefault(r["group"], Counter())[r["category"]] += 1
    no_url_mapped = sum(1 for r in rows if r["epg_id_recorded"] != "UNKNOWN" and r["source_url"] == "UNKNOWN")
    mapped_epg = Counter((mapping[t].get("epg_id") or "").strip() for t in active if t in mapping and (mapping[t].get("epg_id") or "").strip())
    duplicate_epg_ids = sum(1 for count in mapped_epg.values() if count > 1)
    mapped_active = sum(mapped_epg.values())
    bd_rows = []
    for record in parse_playlist(PLAYLIST):
        a = record["attrs"]
        if (a.get("group-title") or "").strip() == "Bangladesh" and (a.get("tvg-country") or "").strip().upper() != "BD":
            tid = (a.get("tvg-id") or "").strip()
            bd_rows.append((tid, (a.get("tvg-country") or "").strip(), record["name"], "usable" if tid in usable else "unusable"))

    counts_json = {}
    if COVERAGE_JSON.is_file():
        counts_json = json.loads(COVERAGE_JSON.read_text(encoding="utf-8"))
    counts_json.update({
        "research_inventory_records": len(rows),
        "research_inventory_usable_now": len(usable),
        "research_inventory_csv_sha256": hashlib.sha256(OUT_CSV.read_bytes()).hexdigest(),
        "research_inventory_generated_at": now.isoformat(timespec="seconds"),
    })
    COVERAGE_JSON.write_text(json.dumps(counts_json, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# EPG Research Inventory — IPTV-Playlist.m3u only", "",
        f"Generated: **{now.isoformat(timespec='seconds')}**", "",
        "Scope: IPTV-Playlist.m3u only. International-Playlist.m3u is out of scope and is not read.",
        "Usable = a titled programme with stop at or after the generation time and start within 7 days.",
        "Categories are exclusive: each channel is assigned the first failing stage listed below.",
        "",
        f"- IPTV-Playlist.m3u SHA-256: **{hashlib.sha256(PLAYLIST.read_bytes()).hexdigest()}**",
        f"- epg/epg.xml SHA-256: **{hashlib.sha256(GUIDE.read_bytes()).hexdigest()}**",
        f"- Active identities (excluding queue groups): **{len(active)}**",
        f"- Usable now: **{len(usable)}**",
        f"- Channels needing research: **{len(rows)}** (check: {len(active)} − {len(usable)} = {len(active) - len(usable)})",
        f"- Mapped records in this inventory without a recorded source URL: **{no_url_mapped}**",
        f"- Mapped active IDs: **{mapped_active}**; duplicate epg_id values among them: **{duplicate_epg_ids}**",
        "- last_verified: UNKNOWN for every record; the mapping snapshot has no verification timestamps.",
        "", "## Counts by category", "",
        "| Category | Channels | Meaning | Recommended next action |", "|---|---:|---|---|",
    ]
    for key, (meaning, _req, action) in CATEGORIES.items():
        lines.append(f"| {key} | {by_cat.get(key, 0)} | {meaning} | {action} |")
    lines += ["", "## Counts by group", "", "| Group | " + " | ".join(CATEGORIES) + " | Total |",
              "|---|" + "---:|" * (len(CATEGORIES) + 1)]
    for group in sorted(by_group, key=str.casefold):
        cells = [str(by_group[group].get(k, 0)) for k in CATEGORIES]
        lines.append(f"| {group} | " + " | ".join(cells) + f" | {sum(by_group[group].values())} |")
    lines += [
        "", "## Manual review: non-BD tvg-country in the Bangladesh group", "",
        "Country codes are not changed automatically. Each entry needs a review of whether it is a Bangladeshi diaspora service or incorrect metadata.",
        "Bangladesh's unrestricted genre policy is unchanged.", "",
        f"Rows found: **{len(bd_rows)}**", "",
        "| tvg-id | tvg-country | Channel | Usable now |", "|---|---|---|---|",
    ]
    for tid, country, name, state in bd_rows:
        lines.append(f"| {tid} | {country} | {name} | {state} |")
    lines += [
        "", "## Full list", "",
        "Candidate IDs are limited to the epg_id values already recorded in reports/epg-channel-mapping.csv.",
        "Provenance fields are UNKNOWN where the mapping snapshot has no value. Full detail is in epg-research-inventory.csv.", "",
        "| Category | Group | Channel | tvg-id | Recorded epg_id | Status | Source name | Declared in guide | Programme nodes |",
        "|---|---|---|---|---|---|---|---|---:|",
    ]
    for r in rows:
        lines.append(
            f"| {r['category']} | {r['group']} | {r['channel']} | {r['tvg_id']} | {r['epg_id_recorded']} | "
            f"{r['csv_status']} | {r['source_name']} | {r['guide_channel_declared']} | {r['programme_nodes']} |"
        )
    lines += [
        "", "## Scripts and data needed for online source research", "",
        "Nothing in this inventory has been fetched or verified online. Source discovery is a separate, online step.", "",
        "- Data: IPTV-Playlist.m3u, epg/epg.xml, reports/epg-channel-mapping.csv, reports/epg-research-inventory.csv",
        "- Discovery and probing: scripts/fetch_iptv_org_epg.py, scripts/probe_epg_sources_for_bangladesh.py, scripts/official_epg_sources.py",
        "- Mapping augmentation: scripts/augment_epg_mapping_from_iptv_org.py, scripts/augment_epg_mapping_from_additional_sources.py, scripts/epg_mapping_policy.py",
        "- Coverage and caching: scripts/epg_coverage.py, scripts/epg_source_cache.py",
        "- Rights gate (must pass before any source is used): scripts/check_epg_source_rights.py",
        "- Generation and publication: scripts/generate_epg.py, scripts/run_generate_epg.py, scripts/epg_publish_gate_v2.py, scripts/validate_epg_freshness.py",
        "- Reports: reports/bangladesh-epg-source-audit.md, reports/epg-unmapped-audit.md, reports/epg-source-audit.md",
        "",
    ]
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(f"Inventory: {len(rows)} channels needing research; usable now {len(usable)}; wrote {OUT_CSV.name} and {OUT_MD.name}.")


if __name__ == "__main__":
    main()
