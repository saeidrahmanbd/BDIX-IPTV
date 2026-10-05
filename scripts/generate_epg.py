#!/usr/bin/env python3
"""Generate a playlist-aligned XMLTV guide from approved public EPG sources."""
import csv, gzip, io, urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta
from pathlib import Path

PLAYLIST = Path("IPTV-Playlist.m3u")
MAPPING = Path("reports/epg-india-channel-mapping.csv")
OUTPUT = Path("epg.xml")

# Approved public XMLTV feeds. EPGShare supplies the strongest India coverage;
# IPTV-EPG and EPG.PW add additional IDs/programmes that are not present there.
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

def fetch(url):
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "BDIX-IPTV-EPG/1.0", "Accept": "application/gzip,application/xml,*/*"},
    )
    with urllib.request.urlopen(req, timeout=90) as r:
        data = r.read()
    if data[:2] == b"\x1f\x8b" or url.endswith(".gz"):
        data = gzip.decompress(data)
    return data

def playlist_channels():
    lines = PLAYLIST.read_text(encoding="utf-8-sig").splitlines()
    out = []
    for line in lines:
        if line.startswith("#EXTINF:"):
            attrs = {}
            import re
            for m in re.finditer(r'([\w-]+)="([^"]*)"', line):
                attrs[m.group(1)] = m.group(2)
            group = attrs.get("group-title", "")
            tvg_id = attrs.get("tvg-id", "").strip()
            name = attrs.get("tvg-name", "").strip() or line.rsplit(",", 1)[-1].strip()
            if tvg_id and group not in ("Backup", "Not Playing"):
                out.append((tvg_id, name))
    return dict(out)

def load_mapping():
    reverse = {}
    if not MAPPING.exists():
        return reverse
    with MAPPING.open(encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh):
            target = row.get("tvg_id", "").strip()
            if not target:
                continue
            # Accept mappings from every approved source listed in SOURCES.
            # The playlist tvg-id remains canonical; provider IDs are translated
            # into that ID in the generated XMLTV guide.
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
            hh = int(raw[16:18]); mm = int(raw[18:20])
            dt = dt.replace(tzinfo=timezone(sign * timedelta(hours=hh, minutes=mm)))
        else:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except Exception:
        return None

def main():
    channels = playlist_channels()
    reverse = load_mapping()
    if not channels or not reverse:
        raise SystemExit("No usable playlist/EPG mappings found")

    root = ET.Element("tv", {
        "generator-info-name": "BDIX-IPTV EPG",
        "generator-info-url": "https://github.com/saeidrahmanbd/BDIX-IPTV",
    })

    mapped_targets = {}
    for source_id, target in reverse.items():
        if target in channels:
            mapped_targets.setdefault(target, set()).add(source_id)

    if not mapped_targets:
        raise SystemExit("No mapped playlist channels found in EPG mapping")

    for target in sorted(mapped_targets):
        ch = ET.SubElement(root, "channel", {"id": target})
        ET.SubElement(ch, "display-name").text = channels[target]

    now = datetime.now(timezone.utc)
    lower = now - timedelta(hours=6)
    upper = now + timedelta(days=7)

    # IMPORTANT: never merge competing schedules from multiple providers for
    # the same playlist channel.  A channel can have several provider IDs,
    # but only one provider schedule should be authoritative at a time.
    #
    # SOURCES is ordered from strongest/preferred to weakest fallback.  For
    # each playlist tvg-id we select the first source that supplies at least
    # one usable current/future programme.  Only that source's programmes
    # are copied for the channel.  This prevents cases such as &pictures
    # receiving Shoorveer from one provider and Mr. & Mrs. Khiladi from
    # another provider under the same XMLTV channel ID.

    selected_source = {}
    programmes_by_target = {}
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

                # Once a stronger source has been selected for this channel,
                # lower-priority sources must never contribute programmes.
                if target in selected_source:
                    elem.clear()
                    continue

                start_dt = stamp(elem.attrib.get("start", ""))
                stop_dt = stamp(elem.attrib.get("stop", "")) if elem.attrib.get("stop") else None
                if not start_dt or start_dt > upper or (stop_dt and stop_dt < lower):
                    elem.clear()
                    continue

                # Keep a private copy of the programme because iterparse
                # reuses/clears the source element.
                attrs = dict(elem.attrib)
                attrs["channel"] = target
                children = [ET.fromstring(ET.tostring(child, encoding="utf-8")) for child in list(elem)]
                title = (elem.findtext("title") or "").strip()

                # The first usable programme from a source makes that source
                # authoritative for this target channel.
                selected_source[target] = (source_index, src, source_id)
                programmes_by_target.setdefault(target, [])
                key = (attrs.get("start", ""), attrs.get("stop", ""), title)
                if key not in {(x[0].get("start", ""), x[0].get("stop", ""), x[1]) for x in programmes_by_target[target]}:
                    programmes_by_target[target].append((attrs, title, children))

                elem.clear()

            # A source may be authoritative for some channels and not others.
            # Continue through all sources only to find channels still without
            # a usable schedule.
        except Exception as exc:
            source_stats[src] = f"FAILED: {exc}"

    # The streaming logic above selects a source at the first usable programme.
    # Re-read each selected source once so that we can copy its complete
    # current/future schedule for the channel, rather than only that first
    # programme.
    final_programmes = {target: [] for target in selected_source}
    seen = set()

    selected_by_source = {}
    for target, (idx, src, source_id) in selected_source.items():
        selected_by_source.setdefault(src, []).append((target, source_id))

    for src, targets in selected_by_source.items():
        try:
            data = fetch(src)
            wanted_ids = {source_id: target for target, source_id in targets}
            for _, elem in ET.iterparse(io.BytesIO(data), events=("end",)):
                if elem.tag != "programme":
                    continue
                source_id = elem.attrib.get("channel", "").strip()
                target = wanted_ids.get(source_id)
                if not target:
                    elem.clear()
                    continue

                start_dt = stamp(elem.attrib.get("start", ""))
                stop_dt = stamp(elem.attrib.get("stop", "")) if elem.attrib.get("stop") else None
                if not start_dt or start_dt > upper or (stop_dt and stop_dt < lower):
                    elem.clear()
                    continue

                attrs = dict(elem.attrib)
                attrs["channel"] = target
                title = (elem.findtext("title") or "").strip()
                key = (target, attrs.get("start", ""), attrs.get("stop", ""), title)
                if key in seen:
                    elem.clear()
                    continue

                seen.add(key)
                p = ET.Element("programme", attrs)
                for child in list(elem):
                    p.append(ET.fromstring(ET.tostring(child, encoding="utf-8")))
                final_programmes[target].append(p)
                elem.clear()
        except Exception as exc:
            print(f"EPG source failed during selected-source read: {src}: {exc}")

    programme_count = 0
    for target in sorted(mapped_targets):
        if target not in final_programmes:
            continue
        for p in final_programmes[target]:
            root.append(p)
            programme_count += 1

    print(f"EPG source selection: {len(selected_source)} channels assigned a single authoritative source")
    for target in sorted(selected_source):
        idx, src, source_id = selected_source[target]
        print(f"  {target} <- {source_id} via priority {idx}: {src}")

    if programme_count == 0:
        raise SystemExit("No current/future programmes were generated; refusing to publish empty guide")

    ET.indent(root, space="  ")
    tree = ET.ElementTree(root)
    OUTPUT.write_bytes(b'<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(root, encoding="utf-8"))
    print(f"EPG generated: {len(mapped_targets)} mapped channels, {programme_count} programmes")

if __name__ == "__main__":
    main()
