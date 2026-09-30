#!/usr/bin/env python3
"""Locked-category playlist updater with Backup and New Channels discovery."""
import re
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

PLAYLIST = Path("IPTV-Playlist.m3u")
REPORT = Path("reports/auto-update.md")
BACKUP = "Backup"
NEW_CHANNELS = "New Channels"
LOCKED_CATEGORIES = {"Bangladesh", "Indian Bangla", "Indian Movies", "Indian Music", "Indian Entertainment", "International", "Documentary & Wildlife", "Kids", "Religious", "Sports", "Backup", "Not Playing"}

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

def force_group(info, group):
    # Strip source-only visual markers before the entry reaches the master
    # playlist. They are not part of the channel identity and fail metadata
    # hygiene checks in downstream players/audits.
    info = re.sub(r"[ⓎⓈᴴᴰ🇹🇷]", "", info)
    metadata = attrs(info)
    display = metadata.get("tvg-name", "").strip() or channel_name(info)
    cid = metadata.get("tvg-id", "").strip() or metadata.get("channel-id", "").strip()
    if not cid:
        raise ValueError("Candidate stream has no tvg-id/channel-id; refusing to add it.")
    info = set_attr(info, "tvg-name", display)
    info = set_attr(info, "channel-id", cid)
    # New Channels are discovery-only entries, so never inherit a primary
    # channel number from the source. They will receive a number only after
    # manual review/placement into a locked primary category.
    if group == NEW_CHANNELS:
        info = re.sub(r'\s+tvg-chno="[^"]*"', "", info)
    info = re.sub(r'\s+group-title="[^"]*"', "", info)
    return info.replace(",", f' group-title="{group}",', 1)

def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    return urllib.request.urlopen(request, timeout=35).read().decode("utf-8", "replace")

def fetch_source(source):
    try:
        return source, parse(fetch(source)), None
    except Exception as exc:
        return source, [], exc

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

added, new_channels, rejected, unreachable, new_channel_candidates, source_errors = [], [], 0, 0, 0, 0
seen_additions = set()

# Fetch all source playlists concurrently, but preserve the original source order
# when applying candidates. This removes the sequential 35-second source-fetch bottleneck
# without changing playlist ordering or identity rules.
with ThreadPoolExecutor(max_workers=min(8, len(SOURCES))) as pool:
    source_results = list(pool.map(fetch_source, SOURCES))

# Reachability checks are I/O-bound. Run them concurrently while applying their
# results in the original candidate order, preserving all existing deduplication
# and category semantics. URLs are cached so the same stream is never tested twice
# during a single update run.
reachability_cache = {}

for source, candidates, source_error in source_results:
    if source_error is not None:
        source_errors += 1
        continue

    pending = []
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

        known = bool(
            (cid and cid in existing_ids)
            or (
                cid_base
                and cid_base in existing_ids
                and (same_id_country or not candidate_country)
                and not country_conflict
            )
        )

        url_l = url.lower()
        if not known:
            new_channel_candidates += 1
            if url_l in existing_urls or not cid:
                continue
            key = (cid_base or cname, url_l)
            if key in seen_additions:
                continue
            pending.append(("new", info, url, key))
            continue

        if url_l in existing_urls or url_l in backup_urls:
            continue
        key = (cid_base or cname, url_l)
        if key in seen_additions:
            continue
        pending.append(("backup", info, url, key))

    # Deduplicate URL checks before launching network requests.
    pending_urls = []
    seen_pending_urls = set()
    for _, _, url, _ in pending:
        url_l = url.lower()
        if url_l not in reachability_cache and url_l not in seen_pending_urls:
            seen_pending_urls.add(url_l)
            pending_urls.append(url_l)

    if pending_urls:
        with ThreadPoolExecutor(max_workers=24) as pool:
            results = pool.map(reachable, pending_urls)
            for url_l, ok in zip(pending_urls, results):
                reachability_cache[url_l] = ok

    for kind, info, url, key in pending:
        url_l = url.lower()
        # Re-check mutable deduplication state here because multiple candidates
        # can be queued before the first successful candidate is applied.
        if url_l in existing_urls or url_l in backup_urls or key in seen_additions:
            continue
        if not reachability_cache.get(url_l, False):
            unreachable += 1
            continue
        if kind == "new":
            new_channels.append((force_group(info, NEW_CHANNELS), url))
            seen_additions.add(key)
            existing_urls.add(url_l)
        else:
            added.append((force_group(info, BACKUP), url))
            seen_additions.add(key)
            existing_urls.add(url_l)
            backup_urls.add(url_l)

if added or new_channels:
    lines = base.splitlines()
    if added:
        backup_positions = [i for i, line in enumerate(lines) if line.startswith("#EXTINF") and attrs(line).get("group-title", "").strip() == BACKUP]
        if backup_positions:
            j = backup_positions[-1] + 1
            while j < len(lines) and not lines[j].startswith("#EXTINF"):
                j += 1
            block = []
            for info, url in added:
                block.extend([info, url])
            lines[j:j] = block
        else:
            added = []
            print("No Backup category exists; skipping backup additions.")
    if new_channels:
        block = []
        for info, url in new_channels:
            block.extend([info, url])
        # Always append New Channels after every existing category.
        lines.extend(block)
    PLAYLIST.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")

REPORT.parent.mkdir(exist_ok=True)
REPORT.write_text("\n".join([
    "# IPTV Auto Update", "",
    f"Generated: {datetime.now(timezone.utc).isoformat(timespec='seconds')}", "",
    "## Policy",
    "- Existing categories are locked.",
    '- The locked categories are never used for automatic new-channel additions.',
    '- New channel candidates are automatically placed only in the "New Channels" category at the bottom.',
    "- Only alternate streams whose playlist identity matches an existing channel ID are allowed.",
    '- Accepted alternate streams are placed in the existing "Backup" category.',
    "- The locked categories are: Bangladesh, Indian Bangla, Indian Movies, Indian Music, Indian Entertainment, International, Documentary & Wildlife, Kids, Religious, Sports, Backup, Not Playing.", "",
    f"Added backup streams: {len(added)}",
    f"Added new channels: {len(new_channels)}",
    f"New-channel candidates processed: {new_channel_candidates}",
    f"Rejected candidates: {rejected}",
    f"Unreachable candidates: {unreachable}",
    f"Source errors: {source_errors}",
]), encoding="utf-8")

print(f"Playlist update: backups_added={len(added)}, new_channels_added={len(new_channels)}, new_channel_candidates={new_channel_candidates}, rejected={rejected}, unreachable={unreachable}, source_errors={source_errors}")
