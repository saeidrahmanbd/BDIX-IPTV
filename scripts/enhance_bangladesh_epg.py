#!/usr/bin/env python3
"""Merge verified Bangladesh EPG coverage from FreeEPG into the published guide.

Safety rules:
- Bangladesh channels are matched only against the Bangladesh-specific feed.
- Exact tvg-id matches and exact normalized display-name matches are allowed.
- No stream URLs are touched.
- Existing non-Bangladesh guide data is preserved.
"""
from collections import defaultdict
from pathlib import Path
import gzip
import io
import re
import urllib.request
import xml.etree.ElementTree as ET

PLAYLIST = Path("IPTV-Playlist.m3u")
GUIDE = Path("epg/epg.xml")
REPORT = Path("reports/bangladesh-epg-enhancement.md")
SOURCE = "https://free-epg.de/api/epg/bd.xml.gz"
ATTR_RE = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')


def attrs(line):
    return dict(ATTR_RE.findall(line))


def norm_name(value):
    value = (value or "").casefold()
    value = re.sub(r"\b(hd|sd|fhd|uhd|tv|channel)\b", "", value)
    return re.sub(r"[^a-z0-9]+", "", value)


def playlist_channels():
    out = {}
    current = None
    for line in PLAYLIST.read_text(encoding="utf-8-sig").splitlines():
        if line.startswith("#EXTINF:"):
            a = attrs(line)
            if a.get("group-title", "").strip() == "Bangladesh" and a.get("tvg-id"):
                current = (a.get("tvg-id", "").strip(), a.get("tvg-name", "").strip() or line.rsplit(",", 1)[-1].strip())
            else:
                current = None
    
            if current:
                out[current[0]] = current[1]
    return out


def fetch_source():
    req = urllib.request.Request(SOURCE, headers={"User-Agent": "BDIX-IPTV-Bangladesh-EPG/1.0", "Accept": "application/gzip,application/xml,*/*"})
    with urllib.request.urlopen(req, timeout=45) as r:
        data = r.read()
    if data[:2] == b"\x1f\x8b":
        data = gzip.decompress(data)
    return ET.parse(io.BytesIO(data)).getroot()


def channel_names(elem):
    return [((x.text or "").strip()) for x in elem.findall("display-name") if (x.text or "").strip()]


def main():
    if not PLAYLIST.exists() or not GUIDE.exists():
        raise SystemExit("Playlist or generated EPG guide is missing")

    wanted = playlist_channels()
    if not wanted:
        print("Bangladesh EPG enhancement: no Bangladesh channels found")
        return

    source_root = fetch_source()
    source_channels = {}
    source_name_index = defaultdict(list)
    for ch in source_root.findall("channel"):
        cid = (ch.get("id") or "").strip()
        if not cid:
            continue
        source_channels[cid] = ch
        for name in channel_names(ch):
            key = norm_name(name)
            if key:
                source_name_index[key].append(cid)

    matches = {}
    for tvg_id, name in wanted.items():
        if tvg_id in source_channels:
            matches[tvg_id] = tvg_id
            continue
        candidates = list(dict.fromkeys(source_name_index.get(norm_name(name), [])))
        if len(candidates) == 1:
            matches[tvg_id] = candidates[0]

    guide_root = ET.parse(GUIDE).getroot()
    existing_channels = {x.get("id") for x in guide_root.findall("channel") if x.get("id")}
    existing_programmes = {
        (x.get("channel"), x.get("start"), x.get("stop"), (x.findtext("title") or "").strip())
        for x in guide_root.findall("programme")
    }

    # Preserve all existing guide data. Add/merge only verified Bangladesh mappings.
    added_channels = 0
    added_programmes = 0
    source_programmes_by_channel = defaultdict(list)
    for programme in source_root.findall("programme"):
        cid = (programme.get("channel") or "").strip()
        if cid:
            source_programmes_by_channel[cid].append(programme)

    for playlist_id, source_id in matches.items():
        source_channel = source_channels[source_id]
        if playlist_id not in existing_channels:
            new_channel = ET.Element("channel", {"id": playlist_id})
            names = channel_names(source_channel)
            if names:
                ET.SubElement(new_channel, "display-name").text = wanted[playlist_id]
            icon = source_channel.find("icon")
            if icon is not None and icon.get("src"):
                ET.SubElement(new_channel, "icon", {"src": icon.get("src")})
            guide_root.append(new_channel)
            existing_channels.add(playlist_id)
            added_channels += 1

        for source_programme in source_programmes_by_channel.get(source_id, []):
            start = source_programme.get("start")
            stop = source_programme.get("stop")
            title = (source_programme.findtext("title") or "").strip()
            if not start or not stop or not title:
                continue
            key = (playlist_id, start, stop, title)
            if key in existing_programmes:
                continue
            new_programme = ET.fromstring(ET.tostring(source_programme, encoding="unicode"))
            new_programme.set("channel", playlist_id)
            guide_root.append(new_programme)
            existing_programmes.add(key)
            added_programmes += 1

    # Stable ordering: channels first as produced by the existing generator,
    # then programmes by channel/start/stop.
    channels = guide_root.findall("channel")
    programmes = guide_root.findall("programme")
    for node in list(guide_root):
        guide_root.remove(node)
    for node in channels:
        guide_root.append(node)
    programmes.sort(key=lambda x: (x.get("channel", ""), x.get("start", ""), x.get("stop", "")))
    for node in programmes:
        guide_root.append(node)

    tree = ET.ElementTree(guide_root)
    try:
        ET.indent(tree, space="  ")
    except AttributeError:
        pass
    tree.write(GUIDE, encoding="utf-8", xml_declaration=True)

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Bangladesh EPG Enhancement",
        "",
        f"Source: `{SOURCE}`",
        "",
        f"- Bangladesh playlist identities reviewed: **{len(wanted)}**",
        f"- Verified source matches: **{len(matches)}**",
        f"- New guide channel identities added: **{added_channels}**",
        f"- Programme rows added: **{added_programmes}**",
        "",
        "Only exact Bangladesh-feed tvg-id matches or unique exact normalized channel-name matches were accepted.",
    ]
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Bangladesh EPG enhancement: matched={len(matches)}/{len(wanted)}, added_channels={added_channels}, added_programmes={added_programmes}")


if __name__ == "__main__":
    main()
