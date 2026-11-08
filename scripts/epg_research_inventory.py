#!/usr/bin/env python3
"""Offline EPG research inventory for IPTV-Playlist.m3u only.

Lists every active IPTV identity that has no usable (future, titled) schedule in epg/epg.xml,
with its mapping-snapshot status from reports/epg-channel-mapping.csv and the requirement that
a source must meet before the channel can be published. It never fetches feeds, never edits
mappings or the guide, and never invents candidate IDs: candidate IDs are only the epg_id values
already recorded in the mapping snapshot.
"""
import csv
import hashlib
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from update_epg_published_coverage import INACTIVE_GROUPS, parse_playlist, usable_title, parse_time  # noqa: E402

import xml.etree.ElementTree as ET  # noqa: E402
from datetime import timedelta  # noqa: E402

PLAYLIST = ROOT / "IPTV-Playlist.m3u"
GUIDE = ROOT / "epg" / "epg.xml"
MAPPING = ROOT / "reports" / "epg-channel-mapping.csv"
OUT_CSV = ROOT / "reports" / "epg-research-inventory.csv"
OUT_MD = ROOT / "reports" / "epg-research-inventory.md"

COLUMNS = [
    "category", "group", "channel", "tvg_id", "tvg_country", "tvg_language",
    "csv_status", "epg_id_recorded", "published_in_guide", "has_any_programme", "usable_now",
    "sources_recorded", "missing_requirement",
]

REQUIREMENT = {
    "UNMAPPED_NO_CSV_ROW": "No mapping snapshot row. Needs a provider channel ID whose schedule matches this channel, plus future programmes.",
    "UNMAPPED_NO_GUIDE_HIT": "Mapping snapshot records no guide hit. Needs a candidate provider ID that carries future programmes and passes identity review.",
    "MAPPED_ID_NOT_PUBLISHED": "epg_id is recorded but absent from epg/epg.xml. Needs the ID confirmed in a fetched feed and published with future programmes.",
    "MAPPED_NO_PROGRAMMES": "Published channel with no programme rows. Needs a feed that supplies future programmes for the recorded epg_id.",
    "MAPPED_SCHEDULE_ENDED": "Programmes exist but none are future or titled. Needs a feed carrying schedules after the current time.",
    "MAPPED_NOT_CURRENTLY_FOUND": "Recorded epg_id was not found in the last fetch. Needs re-verification against a current feed before reuse.",
}


def load_mapping():
    mapping = {}
    if MAPPING.is_file():
        with MAPPING.open(encoding="utf-8-sig", newline="") as handle:
            for row in csv.DictReader(handle):
                tid = (row.get("tvg_id") or "").strip()
                if tid and tid not in mapping:
                    mapping[tid] = row
    return mapping


def load_guide(active_ids):
    now = datetime.now(timezone.utc)
    lower, upper = now - timedelta(hours=6), now + timedelta(days=7)
    published, any_prog, usable = set(), set(), set()
    for _, elem in ET.iterparse(str(GUIDE), events=("end",)):
        if elem.tag == "channel":
            cid = (elem.get("id") or "").strip()
            if cid:
                published.add(cid)
            elem.clear()
        elif elem.tag == "programme":
            cid = (elem.get("channel") or "").strip()
            if cid:
                any_prog.add(cid)
            start, stop = parse_time(elem.get("start")), parse_time(elem.get("stop"))
            title = elem.find("title")
            if (cid in active_ids and start and stop and stop > start and start <= upper
                    and stop >= lower and stop >= now and title is not None and usable_title(title.text)):
                usable.add(cid)
            elem.clear()
    return published, any_prog, usable, now


def main():
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
    published, any_prog, usable, now = load_guide(active)

    rows = []
    for tid in sorted(active, key=lambda t: (identities[t]["group"].casefold(), identities[t]["channel"].casefold(), t)):
        if tid in usable:
            continue
        info, row = identities[tid], mapping.get(tid)
        epg_id = (row.get("epg_id") or "").strip() if row else ""
        status = (row.get("status") or "").strip() if row else ""
        sources = (row.get("source") or "").strip() if row else ""
        # The guide is keyed by the playlist tvg-id; epg_id is only the source-side identifier.
        if row is None:
            category = "UNMAPPED_NO_CSV_ROW"
        elif not epg_id:
            category = "UNMAPPED_NO_GUIDE_HIT"
        elif tid not in published:
            category = "MAPPED_ID_NOT_PUBLISHED"
        elif tid not in any_prog:
            category = "MAPPED_NO_PROGRAMMES"
        elif status == "MAPPED_NOT_CURRENTLY_FOUND":
            category = "MAPPED_NOT_CURRENTLY_FOUND"
        else:
            category = "MAPPED_SCHEDULE_ENDED"
        rows.append({
            "category": category, "group": info["group"], "channel": info["channel"], "tvg_id": tid,
            "tvg_country": info["country"], "tvg_language": info["language"], "csv_status": status,
            "epg_id_recorded": epg_id, "published_in_guide": "yes" if tid in published else "no",
            "has_any_programme": "yes" if tid in any_prog else "no",
            "usable_now": "no", "sources_recorded": sources, "missing_requirement": REQUIREMENT[category],
        })

    with OUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)

    counts = {}
    by_group = {}
    for r in rows:
        counts[r["category"]] = counts.get(r["category"], 0) + 1
        by_group.setdefault(r["group"], {}).setdefault(r["category"], 0)
        by_group[r["group"]][r["category"]] += 1

    lines = [
        "# EPG Research Inventory — IPTV-Playlist.m3u only", "",
        f"Generated: **{now.isoformat(timespec='seconds')}**",
        "",
        "Scope: IPTV-Playlist.m3u only. International-Playlist.m3u is out of scope and is not read.",
        "Usable = a titled programme with stop at or after the generation time and start within 7 days.",
        "The usable set changes as time passes; re-run this script to refresh it.",
        "",
        f"- IPTV-Playlist.m3u SHA-256: **{hashlib.sha256(PLAYLIST.read_bytes()).hexdigest()}**",
        f"- epg/epg.xml SHA-256: **{hashlib.sha256(GUIDE.read_bytes()).hexdigest()}**",
        f"- Active identities (excluding queue groups): **{len(active)}**",
        f"- Usable now: **{len(usable)}**",
        f"- Channels needing research: **{len(rows)}**",
        "",
        "## Counts by category", "",
        "| Category | Channels | Missing requirement |", "|---|---:|---|",
    ]
    for key in REQUIREMENT:
        lines.append(f"| {key} | {counts.get(key, 0)} | {REQUIREMENT[key]} |")
    lines += ["", "## Counts by group", "", "| Group | " + " | ".join(REQUIREMENT) + " | Total |",
              "|---|" + "---:|" * (len(REQUIREMENT) + 1)]
    for group in sorted(by_group, key=str.casefold):
        cells = [str(by_group[group].get(k, 0)) for k in REQUIREMENT]
        lines.append(f"| {group} | " + " | ".join(cells) + f" | {sum(by_group[group].values())} |")
    lines += [
        "", "## Full list", "",
        "Candidate IDs are limited to the epg_id values already recorded in reports/epg-channel-mapping.csv.",
        "No candidate is proposed for channels whose snapshot row is empty.", "",
        "| Category | Group | Channel | tvg-id | Recorded epg_id | Status | Sources recorded |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in rows:
        src = r["sources_recorded"].replace("|", "/")[:120]
        lines.append(f"| {r['category']} | {r['group']} | {r['channel']} | {r['tvg_id']} | {r['epg_id_recorded'] or '-'} | {r['csv_status'] or '-'} | {src or '-'} |")
    lines += [
        "", "## Scripts and data needed for online source research", "",
        "Run these in an environment with outbound access. Nothing in this inventory has been fetched or verified online.", "",
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
