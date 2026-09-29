#!/usr/bin/env python3
import csv
import gzip
import io
import re
import urllib.request
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path

PLAYLIST = Path("IPTV-Playlist.m3u")
MAPPING = Path("reports/epg-india-channel-mapping.csv")
REPORT = Path("reports/epg-coverage.md")

SOURCES = [
    "https://epgshare01.online/epgshare01/epg_ripper_IN1.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz",
    "https://iptv-org.github.io/epg/guides/in/dishtv.in.epg.xml",
    "https://iptv-org.github.io/epg/guides/in/tataplay.com.epg.xml",
    "https://iptv-epg.org/files/epg-in.xml",
    "https://epg.pw/xmltv/epg_IN.xml",
]

ATTR_RE = re.compile(r'(\w[\w-]*)="([^"]*)"')


def attrs(s):
    return dict(ATTR_RE.findall(s))


def playlist():
    lines = PLAYLIST.read_text(encoding="utf-8-sig").splitlines()
    out = []
    cur = None

    for line in lines:
        if line.startswith("#EXTINF:"):
            a = attrs(line)
            cur = {
                "tvg_id": a.get("tvg-id", "").strip(),
                "name": a.get("tvg-name", "").strip() or line.rsplit(",", 1)[-1].strip(),
                "group": a.get("group-title", "").strip(),
                "country": a.get("tvg-country", "").strip().upper(),
            }
        elif cur and line.strip() and not line.startswith("#"):
            if cur["group"] not in ("Backup", "Not Playing"):
                is_india = (
                    cur["group"].startswith("Indian")
                    or cur["country"] == "IN"
                    or re.search(r"\.in(?:@|$)", cur["tvg_id"], re.I)
                )
                if is_india:
                    out.append(cur)
            cur = None

    return list({(x["group"], x["tvg_id"], x["name"]): x for x in out}.values())


def norm_name(s):
    s = str(s or "").lower()
    s = re.sub(r"\b(hd|sd|uhd|fhd|tv|channel)\b", "", s)
    return re.sub(r"[^a-z0-9]+", "", s)


def norm_id(s):
    s = str(s or "").strip().lower()
    s = re.sub(r"@(?:sd|hd|uhd|fhd)$", "", s, flags=re.I)
    return re.sub(r"[^a-z0-9]+", "", s)


def parse_stamp(value):
    m = re.match(r"^(\d{14})(?:\s*([+-]\d{4}))?", str(value or ""))
    if not m:
        return None
    try:
        dt = datetime.strptime(m.group(1), "%Y%m%d%H%M%S")
        off = m.group(2)
        if off:
            sign = 1 if off[0] == "+" else -1
            mins = int(off[1:3]) * 60 + int(off[3:5])
            dt = dt.replace(tzinfo=timezone(sign * timedelta(minutes=mins)))
        else:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except ValueError:
        return None


def parse_source(url):
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "BDIX-IPTV-EPG-Coverage/3.0",
            "Accept": "application/xml,text/xml,application/gzip,*/*",
        },
    )
    with urllib.request.urlopen(req, timeout=90) as r:
        data = r.read()

    if url.endswith(".gz") or data[:2] == b"\x1f\x8b":
        data = gzip.decompress(data)

    ids = set()
    future = set()
    counts = defaultdict(int)
    names = defaultdict(set)
    now = datetime.now(timezone.utc)

    for _, elem in ET.iterparse(io.BytesIO(data), events=("end",)):
        if elem.tag == "channel":
            cid = elem.attrib.get("id", "").strip()
            if cid:
                ids.add(cid)
                for dn in elem.findall("display-name"):
                    if dn.text:
                        names[norm_name(dn.text)].add(cid)

        elif elem.tag == "programme":
            cid = elem.attrib.get("channel", "").strip()
            if cid:
                counts[cid] += 1
                stop = parse_stamp(elem.attrib.get("stop", ""))
                start = parse_stamp(elem.attrib.get("start", ""))
                if (start and start >= now) or (start and stop and start <= now <= stop) or (stop and stop >= now):
                    future.add(cid)
            elem.clear()

    return ids, future, counts, names


def load_mapping():
    mapping = defaultdict(list)
    if not MAPPING.exists():
        return mapping

    with MAPPING.open(encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh):
            if row.get("tvg_id") and row.get("status") == "MAPPED":
                for value in row.get("epg_id", "").split("|"):
                    value = value.strip()
                    if value and value not in mapping[row["tvg_id"]]:
                        mapping[row["tvg_id"]].append(value)
    return mapping


def main():
    channels = playlist()
    mapping = load_mapping()

    source_data = []
    source_status = []

    for src in SOURCES:
        try:
            parsed = parse_source(src)
            source_data.append(parsed)
            ids, future, counts, _ = parsed
            source_status.append({
                "url": src,
                "status": "OK",
                "channel_ids": len(ids),
                "active_ids": len(future),
                "programme_rows": sum(counts.values()),
                "error": "",
            })
        except Exception as exc:
            source_data.append((set(), set(), defaultdict(int), defaultdict(set)))
            source_status.append({
                "url": src,
                "status": "FAILED",
                "channel_ids": 0,
                "active_ids": 0,
                "programme_rows": 0,
                "error": str(exc)[:220],
            })

    rows = []

    for ch in channels:
        candidates = []
        candidates.extend(mapping.get(ch["tvg_id"], []))
        candidates.extend([ch["tvg_id"], re.sub(r"@(?:sd|hd|uhd|fhd)$", "", ch["tvg_id"], flags=re.I)])
        candidates = list(dict.fromkeys(x for x in candidates if x))
        normalized_candidates = {norm_id(x) for x in candidates}
        name_key = norm_name(ch["name"])

        hits = []
        hit_sources = []
        total_rows = 0
        has_live_or_future = False

        for src, parsed in zip(SOURCES, source_data):
            ids, future, counts, names = parsed

            src_hits = [x for x in candidates if x in ids]
            if not src_hits:
                src_hits = [x for x in ids if norm_id(x) in normalized_candidates]
            if not src_hits:
                src_hits = list(names.get(name_key, set()))

            if src_hits:
                hit_sources.append(src)
                for cid in src_hits:
                    if cid not in hits:
                        hits.append(cid)
                    total_rows += counts.get(cid, 0)
                    if cid in future:
                        has_live_or_future = True

        if has_live_or_future:
            status = "LIVE/FUTURE EPG"
        elif total_rows:
            status = "EPG ROWS, ENDED"
        elif hits:
            status = "CHANNEL ID ONLY"
        else:
            status = "NO GUIDE HIT"

        rows.append({
            **ch,
            "epg_id": " | ".join(hits[:8]),
            "sources": hit_sources,
            "status": status,
            "programme_rows": total_rows,
        })

    live = [r for r in rows if r["status"] == "LIVE/FUTURE EPG"]
    ended = [r for r in rows if r["status"] == "EPG ROWS, ENDED"]
    id_only = [r for r in rows if r["status"] == "CHANNEL ID ONLY"]
    no_hit = [r for r in rows if r["status"] == "NO GUIDE HIT"]

    lines = [
        "# EPG Coverage Report",
        "",
        "Generated: **" + datetime.now(timezone.utc).isoformat(timespec="seconds") + "**",
        "",
        "This report audits every active Indian channel against four India XMLTV guides.",
        "A channel is counted as **LIVE/FUTURE EPG** only when a matched guide ID has at least one programme whose start/stop window is current or future.",
        "",
        "## Coverage Summary",
        "",
        f"- Active Indian channels audited: **{len(rows)}**",
        f"- LIVE/FUTURE EPG: **{len(live)}**",
        f"- EPG ROWS, ENDED: **{len(ended)}**",
        f"- CHANNEL ID ONLY: **{len(id_only)}**",
        f"- NO GUIDE HIT: **{len(no_hit)}**",
        f"- Current/future programme coverage: **{len(live)}/{len(rows)} ({round(len(live) / len(rows) * 100, 1) if rows else 0}%)**",
        "",
        "## Source Status",
        "",
    ]

    for src in source_status:
        if src["status"] == "OK":
            lines.append(
                f'- **OK** — {src["url"]} — {src["channel_ids"]} channel IDs; '
                f'{src["active_ids"]} IDs with current/future rows; '
                f'{src["programme_rows"]} programme rows'
            )
        else:
            lines.append(f'- **FAILED** — {src["url"]} — {src["error"]}')

    lines += [
        "",
        "## Missing / Incomplete Channels",
        "",
        "| Group | Channel | Playlist ID | EPG ID matched | Status | Programme rows |",
        "|---|---|---|---|---|---:|",
    ]

    for r in sorted(ended + id_only + no_hit, key=lambda z: (z["status"], z["group"], z["name"])):
        lines.append(
            f'| {r["group"]} | {r["name"]} | {r["tvg_id"]} | '
            f'{r["epg_id"] or "-"} | {r["status"]} | {r["programme_rows"]} |'
        )

    lines += [
        "",
        "## Channel-by-Channel Result",
        "",
        "| Group | Channel | Playlist ID | EPG ID matched | Source(s) | Status | Programme rows |",
        "|---|---|---|---|---|---|---:|",
    ]

    for r in sorted(rows, key=lambda z: (z["group"], z["name"])):
        source_names = ", ".join(r["sources"]) if r["sources"] else "-"
        lines.append(
            f'| {r["group"]} | {r["name"]} | {r["tvg_id"]} | '
            f'{r["epg_id"] or "-"} | {source_names} | {r["status"]} | {r["programme_rows"]} |'
        )

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(
        "Indian EPG audit:",
        len(rows),
        "channels;",
        len(live),
        "live/future;",
        len(ended),
        "ended rows;",
        len(id_only),
        "id-only;",
        len(no_hit),
        "no-guide-hit",
    )


if __name__ == "__main__":
    main()
