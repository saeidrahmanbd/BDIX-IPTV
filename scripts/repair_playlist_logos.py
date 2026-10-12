#!/usr/bin/env python3
"""Repair missing, generic and known-contaminated logos across the three playlists.

Policy: search this repository's /logos tree first (including /logos/unused),
then use exact channel/ID matches from curated sources, IPTV-org, or Wikimedia
Commons. Never invent a broadcaster logo or use an unrelated lookalike.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import shutil
import time
import unicodedata
import urllib.parse

import replace_generic_logos as source

ROOT = Path(".")
LOGOS = Path("logos")
RAW_BASE = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/"
PLAYLISTS = [
    "BDIX-Playlist.m3u",
    "IPTV-Playlist.m3u",
    "NVisionBD-Playlist.m3u",
]
REPORT = Path("reports/playlist-logo-repair-results.md")

# The following files were visually inspected and found contaminated, generic,
# or mismatched. A bad file is never reused, even if its filename is an exact
# channel-name match.
BAD_ASSETS = {
    "atn-news.png",
    "a-sports-5485adff.png",
    "a-sports-hd.png",
    "bein-sports-3.png",
    "bangla-tv.png",
    "btv-news.png",  # M3U World 4K branding is embedded in the image.
    "colors.png",
    "duronto-tv.png",
    "duronto-tv-1ad55c95.png",  # alternate contains an embedded phone number.
    "ekushey-tv.png",
    "global-tv.png",
    "green-tv.png",
    "mohona-tv.png",
    "nagorik-tv.png",
    "nagorik.png",
    "nick-bangla.png",
    "sananda-tv.png",
    "sananda.png",  # SUN Bangla image, not Sananda.
    "star-gold-select.png",
    "star-gold.png",
    "star-plus.png",
    "zee-tv.png",
    "tom-and-jerry.png",
    "arirang-tv.png",  # KBS WORLD wordmark under an Arirang filename.
}
GENERIC_ASSETS = {
    "generated-fallback-btv-news.png",
    "generated-fallback-channel-1.png",
    "generated-fallback-channel-16.png",
    "generated-fallback-channel-52.png",
    "placeholder-btv-news.png",
    "placeholder-channel-1.png",
    "placeholder-channel-16.png",
    "placeholder-channel-52.png",
}
BAD_ASSETS = {name.casefold() for name in BAD_ASSETS}
GENERIC_ASSETS = {name.casefold() for name in GENERIC_ASSETS}

# This alternate was visually inspected in /logos/unused and is clean.
# Use it instead of the contaminated root copy for Global TV.
LOCAL_OVERRIDES = {
    "global tv": "unused/global-tv-1080p-5ffc043912.png",
    "channel 1": "channel-1.png",
}

# Exact, source-attributed fallback URLs for unresolved channels. These are
# only consulted after the repository-wide local logo search. Keep them here
# so all playlist variants reuse the same locally stored image.
EXTRA_DIRECT_HINTS = {
    "Nick Bangla": {
        "url": "https://otapp.store/uploads/tv_image/sm/nick-bangla.png",
        "format": "PNG",
        "page": "https://github.com/channeliptv0/IPTV/blob/f26247efa6b641fda8d6bb16f01f99f4948d8a3b/Master/Bangla.m3u",
        "license": "Channel-specific logo URL found in a public IPTV logo listing; original logo rights belong to broadcaster",
        "license_url": "",
    },
    "Alistiqamah": {
        "url": "https://i.imgur.com/2FPtYZr.png",
        "format": "PNG",
        "page": "https://iptv-org.github.io/channels/om/AlistiqamaTV",
        "license": "Station logo from IPTV-org channel listing",
        "license_url": "https://iptv-org.github.io/channels/om/AlistiqamaTV",
    },
    "Cafe Film": {
        "url": "https://raw.githubusercontent.com/shayanline/iptv-iran/main/assets/logos/CafeFilm.ir.png",
        "format": "PNG",
        "page": "https://github.com/shayanline/iptv-iran/blob/main/assets/logos/CafeFilm.ir.png",
        "license": "Public IPTV logo repository; original logo rights belong to broadcaster",
        "license_url": "https://github.com/shayanline/iptv-iran",
    },
    "Persiana Travel": {
        "url": "https://raw.githubusercontent.com/shayanline/iptv-iran/main/assets/logos/PersianaTravel.fr.png",
        "format": "PNG",
        "page": "https://github.com/shayanline/iptv-iran/blob/main/assets/logos/PersianaTravel.fr.png",
        "license": "Public IPTV logo repository; original logo rights belong to broadcaster",
        "license_url": "https://github.com/shayanline/iptv-iran",
    },
    "Aurora Media Flims": {
        "url": "https://i.imgur.com/DVC5w6H.png",
        "format": "PNG",
        "page": "https://github.com/nsdevaraj/48239b1a55a1df69be38126ed1092e13",
        "license": "Public playlist logo reference; original logo rights belong to broadcaster",
        "license_url": "",
    },
    "Radio Bangla Rock": {
        "url": "https://cdn-radiotime-logos.tunein.com/s253847d.png",
        "format": "PNG",
        "page": "https://tunein.com/radio/Radio-Bangla-Rock-s253847/",
        "license": "Station logo served by TuneIn",
        "license_url": "",
    },
    "Tapmad": {
        "url": "https://www.tapmad.com/tapmad-icon.svg",
        "format": "SVG",
        "page": "https://www.tapmad.com/",
        "license": "Tapmad brand asset from its official website",
        "license_url": "",
    },
    "88 Stereo [not 24/7]": {
        "url": "https://cdn-profiles.tunein.com/s10749/images/logod.jpg?t=637503840760000000",
        "format": "JPEG",
        "page": "https://tunein.com/radio/Radio-88-Stereo-887-s10749/",
        "license": "Station logo served by TuneIn",
        "license_url": "",
    },
    "Power Turk": {
        "url": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/powerturk-tr.png",
        "format": "PNG",
        "page": "https://github.com/tv-logo/tv-logos/blob/main/countries/turkey/powerturk-tr.png",
        "license": "Public TV logo repository; original logo rights belong to broadcaster",
        "license_url": "https://github.com/tv-logo/tv-logos",
    },
    "Dream Music Prime": {
        "url": "https://images.zeno.fm/qCoeGkoZ7uMDvdOso_NCx_7ZVgkxpHVWtvkP9RcAy1k/rs%3Afill%3A152%3A152/q%3A75/g%3Ace%3A0%3A0/aHR0cHM6Ly9wcm94eS56ZW5vLmZtL2NvbnRlbnQvc3RhdGlvbnMvYjg4OGM3NGItNzAzMS00NmM3LTg5MGEtNDg3MzczYjYzMDQ5L2ltYWdlLz91PTE2NzI4MjgxNzMwMDA",
        "format": "",
        "page": "https://zeno.fm/radio/dream-music-prime/",
        "license": "Station logo served by Zeno",
        "license_url": "",
    },
    "Radio Barakah": {
        "url": "https://images.zeno.fm/wSOx1NwNUG6eJNFe2MbZTKU6BvXBDMX5vjbef7G2k_s/rs%3Afill%3A152%3A152/q%3A75/g%3Ace%3A0%3A0/aHR0cHM6Ly9wcm94eS56ZW5vLmZtL2NvbnRlbnQvc3RhdGlvbnMvYWd4emZucGxibTh0YzNSaGRITnlNZ3NTQ2tGMWRHaERiR2xsYm5RWWdJQ3dnNWVUbXdzTUN4SU9VM1JoZEdsdmJsQnliMlpwYkdVWWdJQ3dvX3o0aFFrTW9nRUVlbVZ1YncvaW1hZ2UvP3U9MTY2MTYxNDM0MzAwMA",
        "format": "",
        "page": "https://zeno.fm/radio/radiobarakah/",
        "license": "Station logo served by Zeno",
        "license_url": "",
    },
    "In Sony Sports Ten 3 HD": {
        "url": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/india/sony-ten-3-hd-in.png",
        "format": "PNG",
        "page": "https://github.com/tv-logo/tv-logos/blob/main/countries/india/sony-ten-3-hd-in.png",
        "license": "Channel-specific Sony Sports Ten 3 logo from the TV-logo catalog; broadcaster retains rights",
        "license_url": "https://github.com/tv-logo/tv-logos",
    },
    "Sony Sports Ten 3 HD": {
        "url": "https://www.sonypicturesnetworks.com/images/logos/Sony_Sports_Ten_3_Hindi_HD.png",
        "format": "PNG",
        "page": "https://www.sonypicturesnetworks.com/channels",
        "license": "Sony Pictures Networks India official channel logo; broadcaster retains rights",
        "license_url": "https://www.sonypicturesnetworks.com/",
    },
    "beIN Sports Arabic HD": {
        "url": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/world-middle-east/bein-sports/bein-sports-arabic-mea.png",
        "format": "PNG",
        "page": "https://github.com/tv-logo/tv-logos/blob/main/countries/world-middle-east/bein-sports/bein-sports-arabic-mea.png",
        "license": "Public TV logo repository; original logo rights belong to broadcaster",
        "license_url": "https://github.com/tv-logo/tv-logos",
    },
    "beIN Sports Extra HD": {
        "url": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/international/beinsports/old/horizontal/bein-sports-xtra-hz-int.png",
        "format": "PNG",
        "page": "https://github.com/tv-logo/tv-logos/blob/main/countries/international/beinsports/old/horizontal/bein-sports-xtra-hz-int.png",
        "license": "Public TV logo repository; original logo rights belong to broadcaster",
        "license_url": "https://github.com/tv-logo/tv-logos",
    },
    "TNT Sport 1": {
        "url": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/united-kingdom/hd/tnt-sports-1-hd-uk.png",
        "format": "PNG",
        "page": "https://github.com/tv-logo/tv-logos/blob/main/countries/united-kingdom/hd/tnt-sports-1-hd-uk.png",
        "license": "Public TV logo repository; original logo rights belong to broadcaster",
        "license_url": "https://github.com/tv-logo/tv-logos",
    },
    "Disney Channel Big City Greens": {
        "url": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/international/disney-channel-int.png",
        "format": "PNG",
        "page": "https://github.com/tv-logo/tv-logos/blob/main/countries/international/disney-channel-int.png",
        "license": "Public TV logo repository; original logo rights belong to broadcaster",
        "license_url": "https://github.com/tv-logo/tv-logos",
    },
}

IMAGE_EXTS = {".svg", ".png", ".jpg", ".jpeg", ".webp", ".avif"}
QUALITY_SUFFIX = re.compile(
    r"-(?:1080p|720p|576p|480p|360p|4k|8k|uhd|fhd|hd|sd|hevc|h265|h264)$",
    re.I,
)
ATTR_RE = re.compile(r'([\w-]+)="([^"]*)"')


def parse_extinf(line):
    attrs = dict(ATTR_RE.findall(line))
    label = line.split(",", 1)[-1].strip() if "," in line else ""
    return attrs, label


def set_logo(line, url):
    if re.search(r'tvg-logo="[^"]*"', line):
        return re.sub(r'tvg-logo="[^"]*"', 'tvg-logo="' + url + '"', line, count=1)
    comma = line.find(",")
    if comma < 0:
        return line
    return line[:comma] + ' tvg-logo="' + url + '"' + line[comma:]


def clean_channel(value):
    value = str(value or "").strip()
    value = re.sub(r"\s*\[[^\]]*\]", " ", value)
    value = re.sub(r"\s*\((?:alt|backup|mirror)\s*#?\s*\d+\)\s*$", "", value, flags=re.I)
    value = re.sub(r"\s+(?:alt|backup|mirror)\s*#?\s*\d+\s*$", "", value, flags=re.I)
    return source.clean_channel_name(value)


def norm_key(value):
    return source.norm(clean_channel(value))


def file_is_valid(path):
    try:
        raw = path.read_bytes()
        if len(raw) < 100:
            return False
        suffix = path.suffix.lower()
        if suffix == ".png":
            return raw.startswith(b"\x89PNG\r\n\x1a\n")
        if suffix in (".jpg", ".jpeg"):
            return raw.startswith(b"\xff\xd8\xff")
        if suffix == ".webp":
            return raw[:4] == b"RIFF" and raw[8:12] == b"WEBP"
        if suffix == ".svg":
            text = raw.decode("utf-8", errors="ignore")
            return "<svg" in text.lower() and "CHANNEL MARK" not in text.upper() and "<script" not in text.lower()
        if suffix == ".avif":
            return b"ftypavif" in raw[:40] or b"ftypavis" in raw[:40]
    except Exception:
        return False
    return False


def asset_key(path):
    stem = path.stem.casefold()
    if stem.startswith("nvisionbd-official-"):
        stem = stem[len("nvisionbd-official-"):]
    elif stem.startswith("nvisionbd-verified-"):
        stem = stem[len("nvisionbd-verified-"):]
    elif stem.startswith("nvisionbd-"):
        # Other project-made marks are not trusted as broadcaster art.
        return ""
    elif stem.startswith("verified-"):
        stem = stem[len("verified-"):]
    stem = re.sub(r"-[a-f0-9]{8,}$", "", stem)
    previous = None
    while stem != previous:
        previous = stem
        stem = QUALITY_SUFFIX.sub("", stem)
    return clean_channel(stem)


def prepare_local_asset(path):
    """Return a stable root-relative filename, copying from /unused if needed."""
    path = Path(path)
    if not path.is_file() or not file_is_valid(path):
        return None
    if path.name.casefold() in BAD_ASSETS or path.name.casefold() in GENERIC_ASSETS:
        return None
    if path.parent == LOGOS:
        return path.name
    destination = LOGOS / path.name
    if destination.exists():
        # Do not overwrite a different file or revive a quarantined root asset.
        digest = hashlib.sha256(path.read_bytes()).hexdigest()[:10]
        destination = LOGOS / f"verified-{path.stem}-{digest}{path.suffix.lower()}"
    if not destination.exists():
        shutil.copyfile(path, destination)
    return destination.name if file_is_valid(destination) else None


def find_local_logo(channel):
    target = norm_key(channel)
    if not target:
        return None

    override = LOCAL_OVERRIDES.get(target)
    if override:
        path = LOGOS / override
        result = prepare_local_asset(path)
        if result:
            return result

    candidates = []
    for path in LOGOS.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in IMAGE_EXTS:
            continue
        lower = path.name.casefold()
        if lower in BAD_ASSETS or lower in GENERIC_ASSETS:
            continue
        if lower.startswith(("placeholder-", "generated-fallback-", "generic-", "unknown-", "unidentified-")):
            continue
        if "channel mark" in (path.read_text(encoding="utf-8", errors="ignore").casefold()
                              if path.suffix.lower() == ".svg" else ""):
            continue
        if re.search(r"(?:-backup-?\d*|-alt-\d+)(?:\.|$)", lower):
            continue
        key = asset_key(path)
        if key != target:
            continue
        # Exact file first, then clean vector/raster formats and root-level
        # assets before items archived under /unused.
        exact_stem = 0 if source.norm(path.stem) == source.norm(channel) else 1
        quality_penalty = 1 if QUALITY_SUFFIX.search(path.stem) else 0
        unused_penalty = 1 if "unused" in path.parts else 0
        ext_rank = {".svg": 0, ".png": 1, ".webp": 2, ".jpg": 3, ".jpeg": 4, ".avif": 5}.get(path.suffix.lower(), 9)
        candidates.append((exact_stem, quality_penalty, unused_penalty, ext_rank, str(path).casefold(), path))

    if not candidates:
        return None
    candidates.sort(key=lambda item: item[:-1])
    # Avoid arbitrary choice between two different assets with the same exact
    # channel stem. Duplicate bytes are fine; different bytes require review.
    best_rank = candidates[0][:-2]
    tied = [item[-1] for item in candidates if item[:-2] == best_rank]
    distinct = {}
    for path in tied:
        distinct.setdefault(hashlib.sha256(path.read_bytes()).hexdigest(), path)
    if len(distinct) > 1:
        # A channel-name match may be ambiguous (for example, regional feeds).
        return None
    return prepare_local_asset(next(iter(distinct.values())))


def find_mapping(mapping, channel):
    target = norm_key(channel)
    for name, value in mapping.items():
        if norm_key(name) == target:
            return value
    return None


def candidate_for(channel, attrs, iptv_indexes, history_index):
    # Hand-checked exact fallback URLs, after the repository-wide local search.
    item = find_mapping(EXTRA_DIRECT_HINTS, channel)
    if item:
        return dict(item), "Exact external logo asset"

    # Curated exact source hints are the first external step, after a local scan.
    item = find_mapping(source.DIRECT_LOGO_HINTS, channel)
    if item:
        item = dict(item)
        source_name = item.pop("source", "Curated broadcaster/station source")
        return item, source_name

    item = find_mapping(source.TV_LOGO_HINTS, channel)
    if item:
        hint_path = item
        return {
            "url": source.TV_LOGO_BASE + hint_path,
            "format": Path(hint_path).suffix.lstrip(".").upper(),
            "page": source.TV_LOGO_REPO + "/blob/main/" + hint_path,
            "license": "Source repository; license must be checked at source",
            "license_url": "",
        }, "Curated exact channel/region asset"

    page_hint = find_mapping(source.DIRECT_PAGE_HINTS, channel)
    if page_hint:
        page_url, allow_og = page_hint
        try:
            image_url = source.find_page_logo(page_url, allow_og_image=allow_og)
        except Exception:
            image_url = None
        if image_url:
            return {
                "url": image_url,
                "format": "",
                "page": page_url,
                "license": "Logo image served on the broadcaster/station page",
                "license_url": "",
            }, "Broadcaster/station page"

    if iptv_indexes:
        result = source.get_iptv_org_candidate(channel, attrs.get("tvg-id", ""), iptv_indexes)
        if result and result[0].get("url"):
            logo, source_name = result
            return {
                "url": logo.get("url", ""),
                "format": str(logo.get("format") or "").upper(),
                "page": logo.get("url", ""),
                "license": "IPTV-org public logo dataset",
                "license_url": "https://github.com/iptv-org/database",
            }, source_name

    historical = history_index.get(norm_key(channel))
    if historical and Path(urllib.parse.urlparse(historical.get("url", "")).path).name.casefold() not in BAD_ASSETS | GENERIC_ASSETS:
        item = dict(historical)
        source_name = item.pop("source", "Exact-name historical playlist logo mapping")
        return item, source_name

    try:
        item = source.commons_candidate(channel)
        if item:
            item = dict(item)
            source_name = "Wikimedia Commons exact-logo search"
            return item, source_name
    except Exception:
        pass
    return None, ""


def download_exact_asset(channel, candidate):
    """Fetch and validate exact source bytes, then store them locally."""
    url = candidate.get("url", "")
    if not url.startswith(("https://", "http://")):
        raise ValueError("source URL is missing or not HTTP(S)")
    raw, mime = source.fetch_bytes(url, timeout=35, max_bytes=5_000_000)
    fmt = str(candidate.get("format") or "").upper()
    if not source.valid_image(raw, mime, fmt):
        raise ValueError("source response is not a valid supported image")
    ext = source.extension_for(mime, fmt, url)
    slug = source.slug(channel)
    digest = hashlib.sha256(raw).hexdigest()[:10]
    filename = f"nvisionbd-verified-{slug}-{digest}{ext}"
    dest = LOGOS / filename
    if not dest.exists():
        dest.write_bytes(raw)
    if not file_is_valid(dest):
        raise ValueError("downloaded image failed local validation")
    return filename


def raw_url(filename):
    return RAW_BASE + urllib.parse.quote(filename)


def main():
    LOGOS.mkdir(parents=True, exist_ok=True)
    try:
        iptv_indexes = source.load_iptv_org_indexes()
        iptv_status = "loaded"
    except Exception as exc:
        iptv_indexes = None
        iptv_status = "unavailable: " + str(exc)[:140]
    try:
        history_index = source.load_historical_logo_index()
        # Keep only history entries with non-quarantined basenames.
        history_index = {
            key: value for key, value in history_index.items()
            if Path(urllib.parse.urlparse(value.get("url", "")).path).name.casefold()
            not in BAD_ASSETS | GENERIC_ASSETS
        }
        history_status = f"loaded {len(history_index)} historical name mappings"
    except Exception as exc:
        history_index = {}
        history_status = "unavailable: " + str(exc)[:140]

    fixes_cache = {}
    report_rows = []
    summary = {}
    for playlist in PLAYLISTS:
        path = Path(playlist)
        if not path.is_file():
            summary[playlist] = {"entries": 0, "changed": 0, "missing_after": 0, "flagged_after": 0, "unresolved": 0}
            continue
        original = path.read_text(encoding="utf-8-sig").replace("\r\n", "\n").replace("\r", "\n")
        lines = original.splitlines()
        changed = unresolved = entries = 0
        output = []
        for line_number, line in enumerate(lines, start=1):
            if not line.startswith("#EXTINF:"):
                output.append(line)
                continue
            entries += 1
            attrs, label = parse_extinf(line)
            current = (attrs.get("tvg-logo") or "").strip()
            basename = Path(urllib.parse.urlparse(current).path).name.casefold() if current else ""
            missing = not current
            flagged = basename in BAD_ASSETS or basename in GENERIC_ASSETS or bool(re.search(r"(?:placeholder|generated-fallback|generic-logo)", basename))
            if not (missing or flagged):
                output.append(line)
                continue

            channel = label or attrs.get("tvg-name", "")
            key = norm_key(channel)
            new_file = fixes_cache.get(key)
            source_name = "Reused repaired exact-name logo"
            source_page = ""
            license_name = ""
            license_url = ""

            if not new_file:
                try:
                    new_file = find_local_logo(channel)
                    if new_file:
                        source_name = "Exact clean asset found in repository /logos (including /unused)"
                        source_page = "https://github.com/saeidrahmanbd/BDIX-IPTV/tree/main/logos"
                except Exception as exc:
                    report_rows.append((playlist, line_number, channel, basename, "", "local lookup", "", "", "Local asset lookup failed: " + str(exc)[:120]))

            if not new_file:
                try:
                    candidate, source_name = candidate_for(channel, attrs, iptv_indexes, history_index)
                    if candidate:
                        source_page = candidate.get("page", "")
                        license_name = candidate.get("license", "")
                        license_url = candidate.get("license_url", "")
                        new_file = download_exact_asset(channel, candidate)
                except Exception as exc:
                    report_rows.append((playlist, line_number, channel, basename, "", source_name or "external lookup", "", "", "Download/validation failed: " + str(exc)[:150]))
                    new_file = None

            if new_file:
                fixes_cache[key] = new_file
                line = set_logo(line, raw_url(new_file))
                changed += 1
                report_rows.append((playlist, line_number, channel, basename, new_file, source_name, source_page, license_name + ((" — " + license_url) if license_url else ""), "replaced"))
            else:
                unresolved += 1
                if flagged:
                    # Do not leave a known-generic, contaminated, or mismatched
                    # image attached to a channel when no reliable replacement exists.
                    line = set_logo(line, "")
                report_rows.append((playlist, line_number, channel, basename, "", "none", "", "", "No exact clean logo found; left blank" if missing else "Quarantined flagged logo; no exact replacement found"))
            output.append(line)

        new_text = "\n".join(output).rstrip() + "\n"
        if new_text != original:
            path.write_text(new_text, encoding="utf-8")
        # Confirm reference counts against the resulting file.
        missing_after = flagged_after = 0
        for item in output:
            if not item.startswith("#EXTINF:"):
                continue
            meta, _ = parse_extinf(item)
            logo = (meta.get("tvg-logo") or "").strip()
            name = Path(urllib.parse.urlparse(logo).path).name.casefold() if logo else ""
            if not logo:
                missing_after += 1
            if name in BAD_ASSETS or name in GENERIC_ASSETS or bool(re.search(r"(?:placeholder|generated-fallback|generic-logo)", name)):
                flagged_after += 1
        summary[playlist] = {
            "entries": entries, "changed": changed, "missing_after": missing_after,
            "flagged_after": flagged_after, "unresolved": unresolved,
        }

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    report = [
        "# Three-Playlist Logo Repair Results", "",
        f"Run time: **{now}**  ",
        f"Repository-first local logo search completed before external lookup.  ",
        f"IPTV-org data: {iptv_status}  ",
        f"Historical mapping index: {history_status}", "",
        "## Results by playlist", "",
        "| Playlist | Entries | References changed | Missing after | Known generic/contaminated refs after | Unresolved repair targets |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for name, data in summary.items():
        report.append(f"| {name} | {data['entries']} | {data['changed']} | {data['missing_after']} | {data['flagged_after']} | {data['unresolved']} |")
    report += ["", "## Repair log", "",
               "| Playlist | Line | Channel | Previous logo | Replacement | Source | Attribution | Result |",
               "|---|---:|---|---|---|---|---|---|"]
    for playlist, line_number, channel, previous, new_file, source_name, source_page, attribution, result in report_rows:
        src = f"[{source_name}]({source_page})" if source_page else source_name
        report.append(
            f"| {playlist} | {line_number} | {channel.replace('|', '/')} | {previous or '(missing)'} | "
            f"{new_file or '(none)'} | {src.replace('|', '/')} | {attribution.replace('|', '/')} | {result} |"
        )
    report += ["", "## Quality rule", "",
               "- Only exact, clean local assets or externally downloaded and validated image assets were applied.",
               "- Generic/fallback and previously contaminated/mismatched assets were not reused.",
               "- When no exact clean asset was found, a bad reference was removed rather than replaced with unrelated artwork.",
               "- Original playlist entries, channel metadata, and stream URLs were otherwise preserved.", ""]
    REPORT.write_text("\n".join(report), encoding="utf-8")
    print(json.dumps({"summary": summary, "iptv_org": iptv_status, "history": history_status}, ensure_ascii=False))


if __name__ == "__main__":
    main()
