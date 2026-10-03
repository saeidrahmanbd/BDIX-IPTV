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
    # Targeted India-wide XMLTV feed; mapping remains exact-ID/name based to avoid false matches.
    "https://free-epg.de/api/epg/in.xml.gz",
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
    seen = set()
    programme_count = 0

    for src in SOURCES:
        try:
            data = fetch(src)
            for _, elem in ET.iterparse(io.BytesIO(data), events=("end",)):
                if elem.tag != "programme":
                    continue
                source_id = elem.attrib.get("channel", "").strip()
                target = reverse.get(source_id)
                if not target or target not in mapped_targets:
                    elem.clear()
                    continue
                start = stamp(elem.attrib.get("start", ""))
                stop = stamp(elem.attrib.get("stop", "")) if elem.attrib.get("stop") else None
                if not start or start > upper or (stop and stop < lower):
                    elem.clear()
                    continue

                title = elem.findtext("title") or ""
                key = (target, elem.attrib.get("start", ""), elem.attrib.get("stop", ""), title.strip())
                if key in seen:
                    elem.clear()
                    continue
                seen.add(key)

                attrs = dict(elem.attrib)
                attrs["channel"] = target
                p = ET.SubElement(root, "programme", attrs)
                for child in list(elem):
                    p.append(child)
                programme_count += 1
                elem.clear()
        except Exception as exc:
            print(f"EPG source failed: {src}: {exc}")

    if programme_count == 0:
        raise SystemExit("No current/future programmes were generated; refusing to publish empty guide")

    ET.indent(root, space="  ")
    tree = ET.ElementTree(root)
    OUTPUT.write_bytes(b'<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(root, encoding="utf-8"))
    print(f"EPG generated: {len(mapped_targets)} mapped channels, {programme_count} programmes")

if __name__ == "__main__":
    main()
