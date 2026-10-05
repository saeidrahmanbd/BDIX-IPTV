#!/usr/bin/env python3
"""Generate a playlist-aligned, conflict-free XMLTV guide from approved public EPG sources."""
import bisect
import csv
import gzip
import io
import re
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta
from pathlib import Path

PLAYLIST = Path("IPTV-Playlist.m3u")
MAPPING = Path("reports/epg-india-channel-mapping.csv")
OUTPUT = Path("epg.xml")

SOURCES = [
    "https://epgshare01.online/epgshare01/epg_ripper_IN1.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz",
    "https://iptv-epg.org/files/epg-in.xml",
    "https://epg.pw/xmltv/epg_IN.xml",
    "https://m3u-edit.com/epg-source.php?file=india_dishtv.in.xml",
    "https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz",
    "https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml",
    "https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml",
    "https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/yupptv.xml",
    "https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/zee5.xml",
    "https://avkb.short.gy/epg.xml.gz",
    "https://avkb.short.gy/jioepg.xml.gz",
    "https://avkb.short.gy/tsepg.xml.gz",
]

GENERIC_TITLES = {
    "movie", "program", "programme", "entertainment", "live", "live tv",
    "tba", "to be announced", "unknown", "schedule", "telecast", "show",
    "music", "test", "testing", "coming soon",
}

def fetch(url):
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "BDIX-IPTV-EPG/1.0",
            "Accept": "application/gzip,application/xml,*/*",
        },
    )
    with urllib.request.urlopen(req, timeout=90) as r:
        data = r.read()
    if data[:2] == b"\x1f\x8b" or url.endswith(".gz"):
        data = gzip.decompress(data)
    return data

def playlist_channels():
    lines = PLAYLIST.read_text(encoding="utf-8-sig").splitlines()
    out = {}
    for line in lines:
        if line.startswith("#EXTINF:"):
            attrs = {}
            for m in re.finditer(r'([\w-]+)="([^"]*)"', line):
                attrs[m.group(1)] = m.group(2)
            group = attrs.get("group-title", "")
            tvg_id = attrs.get("tvg-id", "").strip()
            name = attrs.get("tvg-name", "").strip() or line.rsplit(",", 1)[-1].strip()
            if tvg_id and group not in ("Backup", "Not Playing"):
                out[tvg_id] = name
    return out

def load_mapping():
    reverse = {}
    if not MAPPING.exists():
        return reverse
    with MAPPING.open(encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh):
            target = row.get("tvg_id", "").strip()
            if not target:
                continue
            for source_id in row.get("epg_id", "").split("|"):
                source_id = source_id.strip()
                if source_id:
                    reverse[source_id] = target
    return reverse

def stamp(value):
    try:
        raw = str(value).strip()
        if len(raw) < 14:
            return None
        dt = datetime.strptime(raw[:14], "%Y%m%d%H%M%S")
        if len(raw) >= 20 and raw[15] in "+-":
            sign = 1 if raw[15] == "+" else -1
            hh = int(raw[16:18])
            mm = int(raw[18:20])
            dt = dt.replace(tzinfo=timezone(sign * timedelta(hours=hh, minutes=mm)))
        else:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except Exception:
        return None

def normalized_title(title):
    return re.sub(r"\s+", " ", (title or "").strip().lower())

def title_score(title):
    t = normalized_title(title)
    if not t or t in GENERIC_TITLES or len(t) <= 2:
        return 0
    return 1.0 + min(len(t), 80) / 400.0

def clone_children(elem):
    return [ET.fromstring(ET.tostring(child, encoding="utf-8")) for child in list(elem)]

def interval_weight(record):
    """Weight programmes primarily by count, then by title/source quality.

    The old generator selected one provider for an entire channel. That
    discarded large amounts of valid non-overlapping programming. Here all
    mapped providers contribute candidates; interval scheduling removes only
    conflicts. A high base weight makes programme count the dominant objective,
    while modest bonuses prefer named titles and higher-priority sources when
    two candidates compete for the same time.
    """
    start = record["start_dt"]
    stop = record["stop_dt"]
    duration = (stop - start).total_seconds() if stop else 0
    hours = duration / 3600.0 if duration > 0 else 0

    weight = 100.0

    # Prefer real programme names over placeholders such as "Movie".
    if title_score(record["title"]) > 0:
        weight += 8.0

    # Earlier approved sources win close quality ties, but source priority
    # must never outweigh retaining an additional non-overlapping programme.
    source_index = record["source_index"]
    weight += max(0.0, (len(SOURCES) - source_index) / len(SOURCES)) * 3.0

    # Small sanity bonus only; duration is deliberately not allowed to
    # dominate programme count.
    if 0.25 <= hours <= 8:
        weight += 1.0
    elif hours > 12:
        weight -= min(5.0, (hours - 12) * 0.25)

    return max(1.0, weight)


def clean_schedule(records):
    """Deduplicate exact records and remove only true time conflicts."""
    unique = {}
    for r in records:
        if not r["stop_dt"] or r["stop_dt"] <= r["start_dt"]:
            continue

        # Same channel/start/stop/title from several providers is one
        # programme. Keep the best titled/highest-priority representation.
        key = (r["start_dt"], r["stop_dt"], normalized_title(r["title"]))
        old = unique.get(key)
        if old is None:
            unique[key] = r
        else:
            old_quality = (title_score(old["title"]), -old["source_index"])
            new_quality = (title_score(r["title"]), -r["source_index"])
            if new_quality > old_quality:
                unique[key] = r

    items = sorted(
        unique.values(),
        key=lambda r: (r["stop_dt"], r["start_dt"], normalized_title(r["title"])),
    )
    if not items:
        return []

    # Weighted interval scheduling across ALL source candidates. This keeps
    # non-overlapping programmes from different providers instead of throwing
    # them away merely because another provider was selected for the channel.
    stops = [r["stop_dt"] for r in items]
    prev = [bisect.bisect_right(stops, r["start_dt"]) - 1 for r in items]

    dp_score = [0.0] * (len(items) + 1)
    dp_count = [0] * (len(items) + 1)
    take = [False] * len(items)

    for i, r in enumerate(items, start=1):
        skip_score = dp_score[i - 1]
        skip_count = dp_count[i - 1]

        j = prev[i - 1] + 1
        take_score = dp_score[j] + interval_weight(r)
        take_count = dp_count[j] + 1

        if (take_score > skip_score + 1e-9) or (
            abs(take_score - skip_score) <= 1e-9 and take_count > skip_count
        ):
            dp_score[i] = take_score
            dp_count[i] = take_count
            take[i - 1] = True
        else:
            dp_score[i] = skip_score
            dp_count[i] = skip_count

    chosen = []
    i = len(items)
    while i > 0:
        if take[i - 1]:
            chosen.append(items[i - 1])
            i = prev[i - 1] + 1
        else:
            i -= 1

    chosen.reverse()
    return chosen

def main():
    channels = playlist_channels()
    reverse = load_mapping()
    if not channels or not reverse:
        raise SystemExit("No usable playlist/EPG mappings found")

    mapped_targets = {}
    for source_id, target in reverse.items():
        if target in channels:
            mapped_targets.setdefault(target, set()).add(source_id)
    if not mapped_targets:
        raise SystemExit("No mapped playlist channels found in EPG mapping")

    now = datetime.now(timezone.utc)
    lower = now - timedelta(hours=6)
    upper = now + timedelta(days=7)

    # Collect all candidates first. The previous implementation stopped at
    # the first usable source, which could select a poor generic/overlapping
    # schedule simply because it appeared earlier in SOURCES.
    candidates = {}
    source_stats = {}
    for source_index, src in enumerate(SOURCES):
        try:
            data = fetch(src)
            source_stats[src] = "OK"
            for _, elem in ET.iterparse(io.BytesIO(data), events=("end",)):
                if elem.tag != "programme":
                    continue
                source_id = elem.attrib.get("channel", "").strip()
                target = reverse.get(source_id)
                if not target or target not in mapped_targets:
                    elem.clear()
                    continue

                start_dt = stamp(elem.attrib.get("start", ""))
                stop_dt = stamp(elem.attrib.get("stop", "")) if elem.attrib.get("stop") else None
                if not start_dt or start_dt > upper or (stop_dt and stop_dt < lower):
                    elem.clear()
                    continue

                title = (elem.findtext("title") or "").strip()
                attrs = dict(elem.attrib)
                attrs["channel"] = target
                rec = {
                    "attrs": attrs,
                    "title": title,
                    "children": clone_children(elem),
                    "start_dt": start_dt,
                    "stop_dt": stop_dt,
                    "source_index": source_index,
                    "source": src,
                    "source_id": source_id,
                }
                candidates.setdefault((target, source_index, source_id), []).append(rec)
                elem.clear()
        except Exception as exc:
            source_stats[src] = f"FAILED: {exc}"

    # Keep every mapped provider as a candidate. Do NOT choose one provider
    # for an entire channel: that was the reason the previous candidate guide
    # collapsed from ~77k programmes to ~21k and failed the publish gate.
    by_target = {}
    for (target, source_index, source_id), records in candidates.items():
        by_target.setdefault(target, []).extend(records)

    root = ET.Element("tv", {
        "generator-info-name": "BDIX-IPTV EPG",
        "generator-info-url": "https://github.com/saeidrahmanbd/BDIX-IPTV",
    })
    for target in sorted(mapped_targets):
        ch = ET.SubElement(root, "channel", {"id": target})
        ET.SubElement(ch, "display-name").text = channels[target]

    final_count = 0
    raw_count = 0
    removed_count = 0
    generic_counts = 0
    for target in sorted(mapped_targets):
        records = by_target.get(target, [])
        cleaned = clean_schedule(records)
        raw_count += len(records)
        removed_count += len(records) - len(cleaned)
        generic_counts += sum(1 for r in cleaned if title_score(r["title"]) == 0)

        for r in cleaned:
            p = ET.Element("programme", r["attrs"])
            for child in r["children"]:
                p.append(ET.fromstring(ET.tostring(child, encoding="utf-8")))
            root.append(p)
            final_count += 1

        print(
            f"  {target}: candidates {len(records)}, clean {len(cleaned)}, "
            f"removed {len(records) - len(cleaned)}"
        )

    if final_count == 0:
        raise SystemExit("No current/future programmes were generated; refusing to publish empty guide")

    print(f"EPG candidate pool: {raw_count} mapped programmes before cleanup")
    print(f"EPG cleanup: removed {removed_count} exact-duplicate/overlapping programmes")
    print(f"EPG cleanup: retained {generic_counts} generic-title programmes where no named alternative won")
    print(f"EPG generated: {len(mapped_targets)} mapped channels, {final_count} programmes")

    ET.indent(root, space="  ")
    OUTPUT.write_bytes(
        b'<?xml version="1.0" encoding="UTF-8"?>\n'
        + ET.tostring(root, encoding="utf-8")
    )

if __name__ == "__main__":
    main()
