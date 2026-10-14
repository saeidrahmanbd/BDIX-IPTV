#!/usr/bin/env python3
"""Repair deterministic playlist-quality blockers before the maintenance audit.

Scope:
- fill the 35 audited same-name/different-ID collisions when the missing side
  has no channel identity, using the already-audited canonical ID;
- normalize the Ultimate TV metadata conflict to the IPTV-org canonical
  music identity/category;
- fill missing primary tvg-chno values with unused positive numbers;
- never change stream URLs, delete entries, or touch Backup channel numbers.
"""
from pathlib import Path
import re
import unicodedata

PLAYLISTS = (Path("IPTV-Playlist.m3u"), Path("BDIX-Playlist.m3u"))
ATTR = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
PRIMARY_EXCLUDED = {"Backup"}

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
    value = value.casefold()
    value = re.sub(r"[^a-z0-9]+", " ", value).strip()
    return value


def display_name(line):
    a = attrs(line)
    return (a.get("tvg-name") or line.rsplit(",", 1)[-1]).strip()


def entries(lines):
    out = []
    for i, line in enumerate(lines):
        if not line.startswith("#EXTINF:"):
            continue
        out.append((i, line))
    return out


def following_url(lines, index):
    for candidate in lines[index + 1:]:
        if candidate.startswith("#EXTINF:"):
            break
        value = candidate.strip()
        if value.startswith(("http://", "https://")):
            return value
    return ""


def repair(path):
    if not path.is_file():
        return 0, 0, 0

    lines = path.read_text(encoding="utf-8-sig").replace("\r", "").splitlines()
    changes = 0
    collision_repairs = 0
    number_repairs = 0

    # This blank-identity Filamchi proxy is an alternate stream, not canonical
    # B4U Movies. Preserve the URL but quarantine the entry as Backup so it
    # cannot create a duplicate active primary identity after ID completion.
    for idx, line in entries(lines):
        a = attrs(line)
        if (
            a.get("group-title", "").strip() == "Indian Movies"
            and canonical_name(display_name(line)) == "b4u movies"
            and not a.get("tvg-id", "").strip()
            and not a.get("channel-id", "").strip()
            and "/api/play/Filamchi.m3u8" in following_url(lines, idx)
        ):
            lines[idx] = set_attr(line, "group-title", "Backup")
            changes += 1

    # First resolve the audited same-name/different-ID cases. Every audited
    # collision currently has one blank identity and one known canonical ID.
    # Fill only the blank side; never overwrite a non-empty ID.
    for idx, line in entries(lines):
        a = attrs(line)
        if a.get("tvg-id", "").strip() or a.get("channel-id", "").strip():
            continue
        key = canonical_name(display_name(line))
        cid = COLLISION_IDS.get(key)
        if not cid:
            continue
        line = set_attr(line, "tvg-id", cid)
        line = set_attr(line, "channel-id", cid)
        lines[idx] = line
        changes += 1
        collision_repairs += 1

    # Ultimate TV is one canonical Indian music channel. Both current stream
    # URLs belong to the same IPTV-org identity, so do not let one stream's
    # stale Indian Movies grouping create a metadata conflict.
    for idx, line in entries(lines):
        a = attrs(line)
        cid = (a.get("tvg-id") or a.get("channel-id") or "").strip().casefold()
        if cid == "ultimatetv.in@sd" and a.get("group-title", "").strip() == "Indian Movies":
            lines[idx] = set_attr(line, "group-title", "Indian Music")
            changes += 1

    # Fill missing primary channel numbers with the lowest unused positive
    # integers. Existing numbers are preserved exactly; Backup is excluded.
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
        number_repairs += 1

    if changes:
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"{path}: changes={changes} collision_ids={collision_repairs} channel_numbers={number_repairs}")
    return changes, collision_repairs, number_repairs


if __name__ == "__main__":
    for playlist in PLAYLISTS:
        repair(playlist)
