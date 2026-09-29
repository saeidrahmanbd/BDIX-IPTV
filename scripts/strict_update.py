#!/usr/bin/env python3
"""Backup-only playlist updater. Existing channels/categories are locked."""
import re
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

PLAYLIST = Path("IPTV-Playlist.m3u")
REPORT = Path("reports/auto-update.md")
BACKUP = "Backup"

SOURCES = [
    "https://iptv-org.github.io/iptv/countries/in.m3u",
    "https://iptv-org.github.io/iptv/countries/cn.m3u",
    "https://iptv-org.github.io/iptv/countries/kr.m3u",
    "https://iptv-org.github.io/iptv/countries/th.m3u",
    "https://iptv-org.github.io/iptv/countries/tr.m3u",
    "https://iptv-org.github.io/iptv/countries/id.m3u",
    "https://iptv-org.github.io/iptv/languages/eng.m3u",
    "https://iptv-org.github.io/iptv/languages/hin.m3u",
    "https://iptv-org.github.io/iptv/languages/tam.m3u",
    "https://iptv-org.github.io/iptv/languages/tel.m3u",
    "https://iptv-org.github.io/iptv/languages/mal.m3u",
    "https://iptv-org.github.io/iptv/languages/kan.m3u",
    "https://iptv-org.github.io/iptv/languages/zho.m3u",
    "https://iptv-org.github.io/iptv/languages/kor.m3u",
    "https://iptv-org.github.io/iptv/languages/tha.m3u",
    "https://iptv-org.github.io/iptv/languages/tur.m3u",
    "https://iptv-org.github.io/iptv/languages/ind.m3u",
    "https://dearbulut.github.io/iptv/playlists/online.m3u",
    "https://raw.githubusercontent.com/Free-TV/IPTV/master/playlist.m3u8",
]

BLOCKED = {"adult","erotic","xxx","18+","webcam","porn","religion","religious","church","gospel","christian","hindu","krishna","temple","buddhist","sikh","jewish","test","promo","trailer","vod","podcast","radio"}

def attrs(info):
    return dict(re.findall(r'([\w-]+)="([^"]*)"', info))

def channel_name(info):
    return info.rsplit(",", 1)[-1].strip()

def clean_name(value):
    value = re.sub(r"\[[^]]*\]|\([^)]*\)", " ", value)
    value = re.sub(r"\b(?:hd|fhd|uhd|sd|4k|1080p|720p|576p|480p|360p)\b", " ", value, flags=re.I)
    return re.sub(r"[^a-z0-9]+", "", value.lower())

def identity_root(cid):
    return re.sub(r"\.[a-z]{2}$", "", cid.split("@", 1)[0])

def country_code(cid):
    match = re.search(r"\.([a-z]{2})$", cid.split("@", 1)[0])
    return match.group(1).lower() if match else ""

def parse(text):
    lines = text.replace("\r", "").splitlines()
    result = []
    i = 0
    while i < len(lines):
        if lines[i].startswith("#EXTINF"):
            j = i + 1
            while j < len(lines) and (not lines[j].strip() or lines[j].startswith("#")):
                j += 1
            if j < len(lines) and lines[j].startswith(("http://", "https://")):
                result.append((lines[i].strip(), lines[j].strip()))
            i = j
        i += 1
    return result

def acceptable(info):
    text = " ".join([channel_name(info), *attrs(info).values()]).lower()
    return not any(term in text for term in BLOCKED)

def acceptable_url(url):
    if not url.lower().startswith(("http://", "https://")):
        return False
    if re.search(r"[?&](token|auth)=(?:test|testpub)(?:&|$)", url, re.I):
        return False
    if re.search(r"https?://[^/@]+@[^/]+", url, re.I):
        return False
    if re.search(r"[?&]hdnts=$", url, re.I):
        return False
    return True

def set_attr(info, key, value):
    pattern = rf'({re.escape(key)}=")[^"]*(")'
    if re.search(pattern, info):
        return re.sub(pattern, rf'\g<1>{value}\g<2>', info, count=1)
    comma = info.find(",")
    prefix = info if comma < 0 else info[:comma]
    suffix = "" if comma < 0 else info[comma:]
    return prefix + f' {key}="{value}"' + suffix

def force_backup(info):
    metadata = attrs(info)
    display = metadata.get("tvg-name", "").strip() or channel_name(info)
    cid = metadata.get("tvg-id", "").strip() or metadata.get("channel-id", "").strip()
    if not cid:
        raise ValueError("Candidate stream has no tvg-id/channel-id; refusing to add it.")
    info = set_attr(info, "tvg-name", display)
    info = set_attr(info, "channel-id", cid)
    info = re.sub(r'\s+group-title="[^"]*"', "", info)
    return info.replace(",", f' group-title="{BACKUP}",', 1)

def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    return urllib.request.urlopen(request, timeout=35).read().decode("utf-8", "replace")

def reachable(url):
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Range": "bytes=0-8191"})
        with urllib.request.urlopen(request, timeout=10) as response:
            status = getattr(response, "status", 200)
            if not 200 <= status < 400:
                return False
            data = response.read(8192)
            if not data:
                return False
            text = data.decode("utf-8", "ignore").lstrip()
            if ".m3u8" in url.lower() or "mpegurl" in str(response.headers.get("Content-Type", "")).lower():
                return "#EXTM3U" in text or "#EXT-X-" in text
            return True
    except Exception:
        return False

base = PLAYLIST.read_text(encoding="utf-8-sig").replace("\r", "")
entries = parse(base)

existing_ids, existing_names, existing_urls, backup_urls = set(), set(), set(), set()
existing_id_countries = {}
existing_root_countries = {}
for info, url in entries:
    metadata = attrs(info)
    cid = metadata.get("tvg-id", "").strip().lower()
    cid_base = cid.split("@", 1)[0]
    country = metadata.get("tvg-country", "").strip().lower()
    if not country:
        match = re.search(r"\.([a-z]{2})(?:@|$)", cid_base)
        country = match.group(1) if match else ""
    if cid:
        existing_ids.add(cid)
        existing_ids.add(cid_base)
        if country:
            existing_id_countries.setdefault(cid_base, set()).add(country)
            existing_root_countries.setdefault(identity_root(cid), set()).add(country)
    # Display names are retained only for reporting/debugging; they are not identity keys.
    existing_urls.add(url.lower())
    if metadata.get("group-title", "").strip() == BACKUP:
        backup_urls.add(url.lower())

added, rejected, unreachable, new_channel_candidates, source_errors = [], 0, 0, 0, 0
seen_additions = set()

for source in SOURCES:
    try:
        candidates = parse(fetch(source))
    except Exception:
        source_errors += 1
        continue
    for info, url in candidates:
        if not acceptable(info) or not acceptable_url(url):
            rejected += 1
            continue
        metadata = attrs(info)
        cid = metadata.get("tvg-id", "").strip().lower()
        cid_base = cid.split("@", 1)[0]
        cname = clean_name(channel_name(info))
        candidate_country = metadata.get("tvg-country", "").strip().lower()
        if not candidate_country:
            match = re.search(r"\.([a-z]{2})(?:@|$)", cid_base)
            candidate_country = match.group(1) if match else ""
        same_id_country = (
            bool(cid_base and cid_base in existing_id_countries and candidate_country)
            and candidate_country in existing_id_countries.get(cid_base, set())
        )
        root_country_conflict = (
            bool(candidate_country and identity_root(cid) in existing_root_countries)
            and candidate_country not in existing_root_countries.get(identity_root(cid), set())
        )
        country_conflict = (
            bool(cid_base and cid_base in existing_id_countries and candidate_country)
            and candidate_country not in existing_id_countries.get(cid_base, set())
        ) or root_country_conflict
        # Channel identity is metadata-driven only. Never use a display-name match
        # to decide that an unrelated source is an alternate stream. Exact IDs are
        # preferred; base IDs may match only when their country identity is compatible.
        known = bool(
            (cid and cid in existing_ids)
            or (
                cid_base
                and cid_base in existing_ids
                and (same_id_country or not candidate_country)
                and not country_conflict
            )
        )
        if not known:
            new_channel_candidates += 1
            continue
        if url.lower() in existing_urls or url.lower() in backup_urls:
            continue
        key = (cid_base or cname, url.lower())
        if key in seen_additions:
            continue
        if not reachable(url):
            unreachable += 1
            continue
        added.append((force_backup(info), url))
        seen_additions.add(key)
        existing_urls.add(url.lower())
        backup_urls.add(url.lower())

if added:
    lines = base.splitlines()
    backup_positions = [i for i, line in enumerate(lines) if line.startswith("#EXTINF") and attrs(line).get("group-title", "").strip() == BACKUP]
    if backup_positions:
        j = backup_positions[-1] + 1
        while j < len(lines) and not lines[j].startswith("#EXTINF"):
            j += 1
        block = []
        for info, url in added:
            block.extend([info, url])
        lines[j:j] = block
        PLAYLIST.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    else:
        added = []
        print("No Backup category exists; refusing to create a new category.")

REPORT.parent.mkdir(exist_ok=True)
REPORT.write_text("\n".join([
    "# IPTV Auto Update", "",
    f"Generated: {datetime.now(timezone.utc).isoformat(timespec='seconds')}", "",
    "## Policy",
    "- Existing categories are locked.",
    "- New channel additions are disabled.",
    "- Only alternate streams whose playlist identity matches an existing channel ID are allowed.",
    '- Accepted alternate streams are placed in the existing "Backup" category.', "",
    f"Added backup streams: {len(added)}",
    f"New-channel candidates skipped: {new_channel_candidates}",
    f"Rejected candidates: {rejected}",
    f"Unreachable candidates: {unreachable}",
    f"Source errors: {source_errors}",
]), encoding="utf-8")

print(f"Backup-only update: added={len(added)}, new_channel_candidates_skipped={new_channel_candidates}, rejected={rejected}, unreachable={unreachable}, source_errors={source_errors}")
