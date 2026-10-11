#!/usr/bin/env python3
"""Replace generic NVisionBD CHANNEL MARK assets with source-verified channel logos.

Resolution order:
1. Reuse a matching, non-generic logo already in /logos.
2. Use a unique exact-name / exact-ID match from the IPTV-org public logo dataset.
3. Use a unique, explicitly titled and licensed logo file from Wikimedia Commons.
Anything ambiguous remains untouched and is reported for manual review.
"""
import json
import re
import time
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode, urlparse, unquote
from urllib.request import Request, urlopen

PLAYLIST = Path("NVisionBD-Playlist.m3u")
LOGOS = Path("logos")
REPORT = Path("reports/generic-logo-replacement-results.md")
AUDIT = Path("reports/generic-logo-audit.md")
RAW_BASE = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/"
UA = "BDIX-IPTV-logo-audit/2.0 (https://github.com/saeidrahmanbd/BDIX-IPTV)"
IPTV_CHANNELS_URL = "https://iptv-org.github.io/api/channels.json"
IPTV_LOGOS_URL = "https://iptv-org.github.io/api/logos.json"

# These three lookalike matches from the prior pass were not the right logo.
REJECTED_PREVIOUS_MATCHES = {
    "nvisionbd-action-24.jpg": ("nvisionbd-action-24.svg", "Prior match was an event photo, not the channel logo"),
    "nvisionbd-digital-fashion.png": ("nvisionbd-digital-fashion.svg", "Prior match was a different business logo"),
    "nvisionbd-sport-2.jpg": ("nvisionbd-sport-2.svg", "Prior match was a different regional sports channel"),
}

# Repository-first policy: scan every eligible file in /logos before any external lookup.
# Known exact local assets. Use only if the target file exists and is non-generic.
LOCAL_LOGO_FILES = {
    "Zee Cinema HD": "zee-cinema.png",
    "Zee TV HD": "zee-tv.png",
    "Zee Cafe HD": "zee-cafe.png",
    "Zing": "zing.png",
    "Zoom Music": "zoom-music.png",
    "Wild Earth": "wildearth.png",
    "Cowboy Movie Channel": "cowboy-movie-channel.png",
    "NBC Sports": "nbc-sports.png",
    "Talk Sport": "talksport.png",
    "Ducktv": "duck-tv.png",
    "Afrobeats": "afrobeats.png",
}
STOP_WORDS = {"hd", "uhd", "fhd", "sd", "4k", "8k", "1080p", "720p", "576p", "hevc", "h265", "h264"}
COMMONS_STOP_WORDS = {"the"}
SUPPORTED_FORMATS = {"SVG", "PNG", "JPEG", "JPG", "WEBP"}


def norm(value):
    value = unicodedata.normalize("NFKD", str(value or "")).encode("ascii", "ignore").decode().lower()
    value = value.replace("&", " and ").replace("+", " plus ")
    return re.sub(r"[^a-z0-9]+", " ", value).strip()


def clean_channel_name(value):
    words = norm(value).split()
    while words and (words[-1] in STOP_WORDS or re.fullmatch(r"\d{3,4}p", words[-1])):
        words.pop()
    return " ".join(words)


def slug(value):
    return re.sub(r"[^a-z0-9]+", "-", clean_channel_name(value)).strip("-") or "channel"


def basename(value):
    path = unquote(urlparse(value).path) if "://" in value else value
    return Path(path).name


def raw_logo_url(filename):
    return RAW_BASE + filename


def fetch_bytes(url, timeout=30, max_bytes=5_000_000):
    request = Request(url, headers={"User-Agent": UA})
    with urlopen(request, timeout=timeout) as response:
        raw = response.read(max_bytes + 1)
        content_type = response.headers.get("Content-Type", "").split(";", 1)[0].strip().lower()
    if len(raw) > max_bytes:
        raise ValueError("download exceeds 5 MB limit")
    return raw, content_type


def fetch_json(url):
    raw, _ = fetch_bytes(url, timeout=45, max_bytes=20_000_000)
    return json.loads(raw.decode("utf-8"))


def is_generic_file(path):
    path = Path(path)
    if not path.is_file():
        return False
    if path.suffix.lower() == ".svg":
        return "CHANNEL MARK" in path.read_text(encoding="utf-8", errors="ignore").upper()
    return False


def is_generic_logo_url(value):
    return is_generic_file(LOGOS / basename(value))


def valid_image(raw, content_type, file_format=""):
    if len(raw) < 200:
        return False
    fmt = (file_format or "").upper()
    if content_type == "image/svg+xml" or fmt == "SVG" or raw.lstrip().startswith(b"<?xml") or b"<svg" in raw[:1000].lower():
        text = raw.decode("utf-8", errors="ignore")
        return "<svg" in text.lower() and "CHANNEL MARK" not in text.upper() and "<script" not in text.lower()
    if content_type == "image/png" or fmt == "PNG":
        return raw.startswith(b"\x89PNG\r\n\x1a\n")
    if content_type in ("image/jpeg", "image/jpg") or fmt in ("JPEG", "JPG"):
        return raw.startswith(b"\xff\xd8\xff")
    if content_type == "image/webp" or fmt == "WEBP":
        return raw[:4] == b"RIFF" and raw[8:12] == b"WEBP"
    return False


def extension_for(content_type, file_format="", source_url=""):
    fmt = (file_format or "").upper()
    by_fmt = {"SVG": ".svg", "PNG": ".png", "JPEG": ".jpg", "JPG": ".jpg", "WEBP": ".webp"}
    if fmt in by_fmt:
        return by_fmt[fmt]
    by_mime = {"image/svg+xml": ".svg", "image/png": ".png", "image/jpeg": ".jpg", "image/jpg": ".jpg", "image/webp": ".webp"}
    if content_type in by_mime:
        return by_mime[content_type]
    suffix = Path(urlparse(source_url).path).suffix.lower()
    return suffix if suffix in (".svg", ".png", ".jpg", ".jpeg", ".webp") else ".png"


def parse_extinf(line):
    attrs = dict(re.findall(r'([\w-]+)="([^"]*)"', line))
    label = line.split(",", 1)[-1].strip() if "," in line else ""
    return attrs, label


def set_tvg_logo(line, url):
    return re.sub(r'tvg-logo="[^"]*"', 'tvg-logo="' + url + '"', line, count=1)


def load_iptv_org_indexes():
    channels = fetch_json(IPTV_CHANNELS_URL)
    logos = fetch_json(IPTV_LOGOS_URL)
    by_id = {}
    name_to_ids = {}
    for channel in channels:
        cid = str(channel.get("id") or "")
        if not cid:
            continue
        by_id[cid.casefold()] = channel
        aliases = [channel.get("name", "")] + list(channel.get("alt_names") or [])
        for alias in aliases:
            key = clean_channel_name(alias)
            if key:
                name_to_ids.setdefault(key, set()).add(cid)
    logos_by_id = {}
    for logo in logos:
        cid = str(logo.get("channel") or "")
        fmt = str(logo.get("format") or "").upper()
        if cid and fmt in SUPPORTED_FORMATS and logo.get("url"):
            logos_by_id.setdefault(cid.casefold(), []).append(logo)
    return by_id, name_to_ids, logos_by_id


def choose_iptv_logo(channel_id, logos_by_id):
    found = logos_by_id.get(channel_id.casefold(), [])
    if not found:
        return None
    active = [logo for logo in found if logo.get("in_use") is True]
    if active:
        found = active
    def rank(logo):
        tags = {str(tag).lower() for tag in (logo.get("tags") or [])}
        white_penalty = 1 if "white" in tags else 0
        horizontal = 1 if "horizontal" in tags else 0
        default_feed = 1 if not logo.get("feed") else 0
        pixels = int(logo.get("width") or 0) * int(logo.get("height") or 0)
        vector = 1 if str(logo.get("format") or "").upper() == "SVG" else 0
        return (default_feed, horizontal, -white_penalty, vector, pixels)
    found.sort(key=rank, reverse=True)
    return found[0]


def get_iptv_org_candidate(channel_label, tvg_id, indexes):
    by_id, name_to_ids, logos_by_id = indexes
    raw_id = (tvg_id or "").strip()
    if raw_id and not raw_id.lower().startswith(("custom.", "new.", "local.")):
        candidate_id = raw_id.split("@", 1)[0].strip()
        channel = by_id.get(candidate_id.casefold())
        if channel and choose_iptv_logo(candidate_id, logos_by_id):
            return choose_iptv_logo(candidate_id, logos_by_id), "IPTV-org exact ID: " + candidate_id
    key = clean_channel_name(channel_label)
    ids = name_to_ids.get(key, set())
    if len(ids) != 1:
        return None
    candidate_id = next(iter(ids))
    logo = choose_iptv_logo(candidate_id, logos_by_id)
    if not logo:
        return None
    return logo, "IPTV-org exact unique channel name: " + candidate_id


def download_to_repo(source_url, channel, source_format=""):
    raw, mime = fetch_bytes(source_url)
    if not valid_image(raw, mime, source_format):
        raise ValueError("source bytes are not a supported channel image")
    ext = extension_for(mime, source_format, source_url)
    filename = "nvisionbd-official-" + slug(channel) + ext
    destination = LOGOS / filename
    if destination.exists() and not is_generic_file(destination):
        return filename
    LOGOS.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(raw)
    return filename


def commons_candidate(channel):
    query = '"' + str(channel).replace('"', "") + '" logo'
    params = {
        "action": "query", "format": "json", "generator": "search",
        "gsrsearch": query, "gsrnamespace": 6, "gsrlimit": 12,
        "prop": "imageinfo", "iiprop": "url|size|mime|extmetadata"
    }
    data = fetch_json("https://commons.wikimedia.org/w/api.php?" + urlencode(params))
    target_words = [word for word in clean_channel_name(channel).split() if word not in COMMONS_STOP_WORDS]
    found = []
    for page in ((data.get("query") or {}).get("pages") or {}).values():
        title = page.get("title", "").replace("File:", "")
        stem_words = norm(Path(title).stem).split()
        if not target_words or not all(word in stem_words for word in target_words):
            continue
        # Require an explicit logo/wordmark title; never accept an event photo
        # just because its filename contains a similar channel name.
        if not any(word in stem_words for word in ("logo", "logotype", "wordmark")):
            continue
        infos = page.get("imageinfo") or []
        if not infos:
            continue
        info = infos[0]
        mime = str(info.get("mime") or "").lower()
        fmt = {"image/svg+xml": "SVG", "image/png": "PNG", "image/jpeg": "JPEG", "image/webp": "WEBP"}.get(mime, "")
        if fmt not in SUPPORTED_FORMATS:
            continue
        if int(info.get("width") or 0) < 40 or int(info.get("height") or 0) < 25:
            continue
        metadata = info.get("extmetadata") or {}
        license_name = str((metadata.get("LicenseShortName") or {}).get("value") or "").strip()
        license_url = str((metadata.get("LicenseUrl") or {}).get("value") or "").strip()
        if not license_name or not license_url or not info.get("url"):
            continue
        pixels = int(info.get("width") or 0) * int(info.get("height") or 0)
        found.append((pixels, page, info, fmt, license_name, license_url))
    found.sort(key=lambda item: item[0], reverse=True)
    if not found:
        return None
    if len(found) > 1 and found[0][0] <= found[1][0] * 1.15:
        return None
    _, page, info, fmt, license_name, license_url = found[0]
    return {
        "url": info["url"], "format": fmt, "title": page.get("title", ""),
        "page": info.get("descriptionurl", ""), "license": license_name,
        "license_url": license_url,
    }


def get_local_logo(channel):
    """Search the repository's entire /logos folder before any external lookup.

    Match by normalized channel name only. Generic template assets, nvisionbd-
    placeholders, placeholder-* files, backups and unrelated fuzzy name matches
    are never accepted automatically.
    """
    target = clean_channel_name(channel)
    if not target:
        return None

    # Exact, curated overrides remain first in line, but only if the asset exists
    # and it is not itself a generic template.
    explicit = LOCAL_LOGO_FILES.get(channel)
    if explicit:
        path = LOGOS / explicit
        if path.is_file() and not is_generic_file(path):
            return explicit

    supported = {".svg", ".png", ".jpg", ".jpeg", ".webp"}
    matches = []
    for path in LOGOS.iterdir():
        if not path.is_file() or path.suffix.lower() not in supported:
            continue
        lower_name = path.name.lower()
        if lower_name.startswith(("nvisionbd-", "placeholder-")):
            continue
        if re.search(r"-backup-?\d*(?:\.|$)", lower_name):
            continue
        if is_generic_file(path):
            continue

        stem = path.stem.lower()
        # Remove generated hash and quality/resolution suffixes from filenames.
        stem = re.sub(r"-[a-f0-9]{8,}$", "", stem)
        previous = None
        while stem != previous:
            previous = stem
            stem = re.sub(
                r"-(?:1080p|720p|576p|480p|360p|4k|8k|uhd|fhd|hd|sd|hevc|h265|h264)$",
                "", stem, flags=re.I
            )
        candidate = clean_channel_name(stem)
        if candidate != target:
            continue

        # Prefer a canonical filename over a hashed / resolution-specific copy.
        original_norm = clean_channel_name(path.stem)
        has_hash = bool(re.search(r"-[a-f0-9]{8,}$", path.stem.lower()))
        has_quality = bool(re.search(
            r"-(?:1080p|720p|576p|480p|360p|4k|8k|uhd|fhd|hd|sd|hevc|h265|h264)$",
            path.stem.lower()
        ))
        ext_rank = {".svg": 0, ".png": 1, ".webp": 2, ".jpg": 3, ".jpeg": 4}.get(path.suffix.lower(), 9)
        matches.append((has_hash, has_quality, ext_rank, path.name.casefold(), path.name))

    if not matches:
        return None
    matches.sort()
    # Multiple files with the exact same normalized identity are safe only as
    # alternate copies of that exact filename identity; canonical copy wins.
    return matches[0][-1]

def build_audit():
    playlist_names = ["IPTV-Playlist.m3u", "BDIX-Playlist.m3u", "NVisionBD-Playlist.m3u"]
    rows = []
    for playlist_name in playlist_names:
        path = Path(playlist_name)
        if not path.is_file():
            rows.append((playlist_name, 0, 0, []))
            continue
        content = path.read_text(encoding="utf-8", errors="replace")
        labels, generic_files = set(), set()
        entry_count = 0
        for line in content.splitlines():
            if not line.startswith("#EXTINF:"):
                continue
            entry_count += 1
            attrs, label = parse_extinf(line)
            logo = attrs.get("tvg-logo", "")
            if logo and is_generic_logo_url(logo):
                generic_files.add(basename(logo))
                labels.add(label)
        rows.append((playlist_name, entry_count, len(generic_files), sorted(labels)))
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# Generic Channel Logo Audit — Three Playlists", "",
        f"Audit date: {timestamp}  ",
        "Repository: https://github.com/saeidrahmanbd/BDIX-IPTV  ",
        "Method: scans current playlist metadata and checks referenced local SVG files for the generic CHANNEL MARK template.", "",
        "## Summary", "",
        "| Playlist | Entries | Unique generic placeholder assets |",
        "|---|---:|---:|",
    ]
    for playlist_name, entries_count, generic_count, _ in rows:
        lines.append(f"| {playlist_name} | {entries_count} | {generic_count} |")
    target = next((row for row in rows if row[0] == "NVisionBD-Playlist.m3u"), ("", 0, 0, []))
    lines += ["", f"Current NVisionBD placeholder assets: **{target[2]} unique files**.", "",
              "## Remaining affected NVisionBD channel labels", ""]
    for label in target[3]:
        lines.append("- " + label.replace("\n", " "))
    lines += ["", "## Scope and quality rules", "",
              "- Only NVisionBD-Playlist.m3u is modified by the replacement workflow.",
              "- A replacement must be a validated image, must not contain the CHANNEL MARK template, and must have a source recorded in the replacement-results report.",
              "- If multiple channels share a name, or no trustworthy source is found, the placeholder is retained and listed for manual review.",
              "- Old generic files are not deleted automatically, to avoid breaking any other reference.", ""]
    AUDIT.parent.mkdir(parents=True, exist_ok=True)
    AUDIT.write_text("\n".join(lines), encoding="utf-8")


def main():
    if not PLAYLIST.is_file():
        raise SystemExit("NVisionBD-Playlist.m3u not found")
    text = PLAYLIST.read_text(encoding="utf-8", errors="replace")
    # Repair malformed URLs left by the previous script.
    text = re.sub(r"https:/raw\.githubusercontent\.com/", "https://raw.githubusercontent.com/", text)
    # Restore the correct generic file for the three prior lookalike matches.
    for bad_name, (good_name, _reason) in REJECTED_PREVIOUS_MATCHES.items():
        text = re.sub(r'tvg-logo="[^"]*' + re.escape(bad_name) + r'"',
                      'tvg-logo="' + raw_logo_url(good_name) + '"', text)

    try:
        iptv_indexes = load_iptv_org_indexes()
        iptv_status = "loaded"
    except Exception as error:
        iptv_indexes = None
        iptv_status = "unavailable: " + str(error)[:160]

    targets = {}
    for line in text.splitlines():
        if not line.startswith("#EXTINF:"):
            continue
        attrs, label = parse_extinf(line)
        logo = attrs.get("tvg-logo", "")
        if logo and is_generic_logo_url(logo):
            targets.setdefault(basename(logo), {"label": label, "tvg_id": attrs.get("tvg-id", "")})

    replacements, unresolved = [], []
    replacements_by_file = {}
    download_cache = {}
    for old_file, item in sorted(targets.items()):
        channel = item["label"]
        try:
            local = get_local_logo(channel)
            if local:
                new_file = local
                source = "Existing verified repository asset"
                source_page = "https://github.com/saeidrahmanbd/BDIX-IPTV/tree/main/logos"
                license_name, license_url = "Existing repository asset", ""
            else:
                candidate = None
                source, source_page = "", ""
                license_name, license_url = "", ""
                if iptv_indexes:
                    result = get_iptv_org_candidate(channel, item["tvg_id"], iptv_indexes)
                    if result and result[0]:
                        logo_obj, source = result
                        candidate = {
                            "url": logo_obj.get("url", ""),
                            "format": str(logo_obj.get("format") or "").upper(),
                            "page": logo_obj.get("url", ""),
                            "license": "IPTV-org public logo dataset",
                            "license_url": "https://github.com/iptv-org/database",
                        }
                if not candidate:
                    candidate = commons_candidate(channel)
                    if candidate:
                        source = "Wikimedia Commons"
                if not candidate:
                    unresolved.append((channel, old_file, "No unique source-verified channel logo found"))
                    time.sleep(0.1)
                    continue
                src = candidate["url"]
                cache_key = (src, channel)
                if cache_key in download_cache:
                    new_file = download_cache[cache_key]
                else:
                    new_file = download_to_repo(src, channel, candidate.get("format", ""))
                    download_cache[cache_key] = new_file
                source_page = candidate.get("page", "")
                license_name = candidate.get("license", "")
                license_url = candidate.get("license_url", "")

            replacements_by_file[old_file] = raw_logo_url(new_file)
            replacements.append((channel, old_file, new_file, source, source_page, license_name, license_url))
        except Exception as error:
            unresolved.append((channel, old_file, "Lookup/download/validation error: " + str(error)[:160]))
        time.sleep(0.15)

    output_lines = []
    for line in text.splitlines():
        if line.startswith("#EXTINF:"):
            attrs, _ = parse_extinf(line)
            logo = attrs.get("tvg-logo", "")
            old_file = basename(logo) if logo else ""
            if old_file in replacements_by_file:
                line = set_tvg_logo(line, replacements_by_file[old_file])
        output_lines.append(line)
    new_text = "\n".join(output_lines).rstrip() + "\n"
    PLAYLIST.write_text(new_text, encoding="utf-8")

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Generic Logo Replacement Results", "",
        "This report covers the current NVisionBD-Playlist.m3u. Only confidently matched, validated artwork is applied; ambiguous sources remain unresolved.", "",
        f"- Run time: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        f"- IPTV-org dataset: {iptv_status}",
        f"- Unique generic assets examined: {len(targets)}",
        f"- Successful replacements: {len(replacements)}",
        f"- Unresolved/manual review: {len(unresolved)}", "",
        "## Replacements", "",
        "| Channel | Former generic file | New local file | Source | License / attribution |",
        "|---|---|---|---|---|",
    ]
    for channel, old_file, new_file, source, source_page, license_name, license_url in replacements:
        source_link = f"[{source}]({source_page})" if source_page else source
        license_info = license_name + (f" ([license]({license_url}))" if license_url else "")
        lines.append(f"| {channel.replace('|', '/')} | {old_file} | [{new_file}]({RAW_BASE + new_file}) | {source_link} | {license_info} |")
    lines += ["", "## Unresolved — retained for manual source verification", "",
              "| Channel | Current placeholder asset | Reason |",
              "|---|---|---|"]
    for channel, old_file, reason in unresolved:
        lines.append(f"| {channel.replace('|', '/')} | {old_file} | {reason.replace('|', '/')} |")
    if not unresolved:
        lines += ["", "All identified generic assets were replaced with source-verified local logos."]
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    build_audit()
    print(f"examined={len(targets)} replaced={len(replacements)} unresolved={len(unresolved)} iptv_org={iptv_status}")


if __name__ == "__main__":
    main()
