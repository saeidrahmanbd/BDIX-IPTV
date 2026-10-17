#!/usr/bin/env python3
"""Deterministic quality repair for IPTV-Playlist.m3u only.

This script intentionally NEVER reads or writes BDIX-Playlist.m3u.
"""
from pathlib import Path
import re
import unicodedata

PLAYLIST = Path("IPTV-Playlist.m3u")
ATTR = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
PRIMARY_EXCLUDED = {"Backup", "New Backup", "Not Playing"}

COLLISION_IDS = {
    "action hollywood movies": "plex.tv.action.hollywood.movies.plex",
    "amc": "amc.us",
    "b4u movies": "b4umovies.in@india",
    "btv chattogram": "btvchattogram.bd",
    "btv news": "custom.btv.news",
    "colors cineplex": "colorscineplex.in@sd",
    "dangal 2": "dangal2.in@sd",
    "desh tv": "deshtv.bd",
    "discovery kids": "discoverykids.au",
    "discovery science": "custom.discovery.science",
    "discovery turbo": "custom.discovery.turbo",
    "disney channel india": "disneychannel.in@hd",
    "food food": "foodfood.in@sd",
    "hbo": "custom.hbo",
    "history tv18": "historytv18.in@sd",
    "investigation discovery": "investigationdiscovery.in@sd",
    "kolkata tv": "custom.kolkatatv",
    "movie bangla": "moviebangla.bd",
    "movies now": "moviesnow.in@sd",
    "nexus tv": "nexustv.bd",
    "ntv": "ntv.bd",
    "powertürk tv": "powerturktv.tr",
    "quran tv": "qurantv.iq",
    "rtv": "rtv.bd",
    "sa tv": "satv.bd",
    "shemaroo tv": "shemarootv.in@sd",
    "sony entertainment tv": "sonyentertainmenttelevision.in@sd",
    "sony max": "sonymax.in@sd",
    "sony sab": "sonysab.in@hd",
    "star movies select": "starmoviesselect.in@hd",
    "travelxp english": "custom.travelxp.english",
    "zee action": "zeeaction.in",
    "zee bangla cinema": "zeebanglacinema.in@sd",
    "zee bollywood": "zeebollywood.in@sd",
    "zee tv": "zeetv.in@sd",
}


def attrs(line):
    return dict(ATTR.findall(line))


def set_attr(line, key, value):
    p = re.compile(rf'{re.escape(key)}="[^"]*"')
    if p.search(line):
        return p.sub(f'{key}="{value}"', line, count=1)
    return line.replace("#EXTINF:-1 ", f'#EXTINF:-1 {key}="{value}" ', 1)


def canonical_name(value):
    value = unicodedata.normalize("NFKD", str(value or ""))
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]+", " ", value.casefold()).strip()


def display_name(line):
    a = attrs(line)
    return (a.get("tvg-name") or line.rsplit(",", 1)[-1]).strip()


def entries(lines):
    return [(i, line) for i, line in enumerate(lines) if line.startswith("#EXTINF:")]


def following_url(lines, index):
    for candidate in lines[index + 1:]:
        if candidate.startswith("#EXTINF:"):
            break
        value = candidate.strip()
        if value.startswith(("http://", "https://")):
            return value
    return ""


def repair():
    if not PLAYLIST.is_file():
        return
    lines = PLAYLIST.read_text(encoding="utf-8-sig").replace("\r", "").splitlines()
    changes = 0

    # Quarantine the known alternate Filamchi endpoint rather than pretending it
    # is canonical B4U Movies. Preserve its URL and identity as a Backup.
    for idx, line in entries(lines):
        a = attrs(line)
        if (a.get("group-title", "").strip() == "Indian Movies" and
            canonical_name(display_name(line)) == "b4u movies" and
            not a.get("tvg-id", "").strip() and
            not a.get("channel-id", "").strip() and
            "/api/play/Filamchi.m3u8" in following_url(lines, idx)):
            lines[idx] = set_attr(line, "group-title", "Backup")
            changes += 1

    # Resolve only blank identities from the audited collision list. Never
    # overwrite an existing non-empty identity.
    for idx, line in entries(lines):
        a = attrs(line)
        if a.get("tvg-id", "").strip() or a.get("channel-id", "").strip():
            continue
        cid = COLLISION_IDS.get(canonical_name(display_name(line)))
        if cid:
            line = set_attr(line, "tvg-id", cid)
            line = set_attr(line, "channel-id", cid)
            lines[idx] = line
            changes += 1

    # Keep Channel S and Channel S UK as different identities.
    # Only primary Channel S UK records belong in Bangladesh. Alternate
    # streams already in Backup/Not Playing stay there and never receive a
    # primary channel number simply because their display name matches.
    for idx, line in entries(lines):
        if canonical_name(display_name(line)) != "channel s uk":
            continue
        group = attrs(line).get("group-title", "").strip()
        line = set_attr(line, "tvg-id", "custom.channel.s.uk")
        line = set_attr(line, "channel-id", "custom.channel.s.uk")
        line = set_attr(line, "tvg-language", "ben")
        line = set_attr(line, "tvg-country", "GB")
        if group in PRIMARY_EXCLUDED:
            line = re.sub(r'\\s+tvg-chno="[^"]*"', "", line, count=1)
        else:
            line = set_attr(line, "group-title", "Bangladesh")
        lines[idx] = line

    # Keep Ultimate TV consistently in Indian Music.
    for idx, line in entries(lines):
        a = attrs(line)
        cid = (a.get("tvg-id") or a.get("channel-id") or "").strip().casefold()
        if cid == "ultimatetv.in@sd" and a.get("group-title", "").strip() == "Indian Movies":
            lines[idx] = set_attr(line, "group-title", "Indian Music")
            changes += 1

    # Never assign primary numbers to Backup/Not Playing entries. Existing
    # primary numbers remain untouched; only genuinely missing primary numbers
    # receive the lowest unused positive integer.
    used = set()
    for _, line in entries(lines):
        a = attrs(line)
        if a.get("group-title", "").strip() in PRIMARY_EXCLUDED:
            continue
        n = a.get("tvg-chno", "").strip()
        if n.isdigit() and int(n) > 0:
            used.add(int(n))

    next_number = 1
    for idx, line in entries(lines):
        a = attrs(line)
        if a.get("group-title", "").strip() in PRIMARY_EXCLUDED:
            continue
        if a.get("tvg-chno", "").strip():
            continue
        while next_number in used:
            next_number += 1
        lines[idx] = set_attr(line, "tvg-chno", str(next_number))
        used.add(next_number)
        next_number += 1
        changes += 1

    PLAYLIST.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"IPTV-Playlist.m3u quality repair: changes={changes}")


if __name__ == "__main__":
    repair()
