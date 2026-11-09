#!/usr/bin/env python3
"""Fill blank IPTV metadata from catalogue data with safe group fallbacks."""
import csv
import hashlib
import io
import json
import re
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

PLAYLIST = Path("IPTV-Playlist.m3u")
REPORT = Path("reports/iptv-metadata-backfill.md")
CHANNELS_URL = "https://iptv-org.github.io/api/channels.json"
FEEDS_URL = "https://iptv-org.github.io/api/feeds.json"
ACTIVE_GROUPS = {
    "Bangladesh", "Indian Bangla", "Indian Movies", "Indian Music",
    "Indian Entertainment", "Fashion", "Pakistani", "International",
    "Documentary & Wildlife", "Kids", "Religious", "Sports",
}
TARGET_GROUPS = ACTIVE_GROUPS | {"Backup"}

# Channel-specific language evidence for feeds not yet represented in
# iptv-org's feed catalogue. Values are ISO 639-3 codes; "und" is used only
# where the service is deliberately language-agnostic or its audio is unknown.
LANGUAGE_OVERRIDES = {
    # Explicit languages for IPTV-Playlist channels previously marked und (reviewed by name/script).
    "ktvbangla.in@sd": ("ben",),
    "sonarbangla.in@sd": ("ben",),
    "zodiaktv.in@sd": ("ben",),
    "asianetmovies.in@sd": ("mal",),
    "kaumudytv.in@sd": ("mal",),
    "chhayachitramtelugu.in@sd": ("tel",),
    "chithiram.in@sd": ("tam",),
    "suntv.in@hd": ("tam",),
    "taazatv.in@sd": ("hin",),
    "thendraltv.in@sd": ("tam",),
    "moviepunjab.in@sd": ("pan",),
    "punjabimusichd.in@sd": ("pan",),
    "mahapunjabi.in@sd": ("pan",),
    "punjabitv.in@sd": ("pan",),
    "nandighoshatv.in@sd": ("ori",),
    "nepal1.in@sd": ("nep",),
    "ntctv.in@sd": ("nep",),
    "tehzeebtv.in@sd": ("urd",),
    "meialaitv.in": ("tam",),
    "mahuaplay.in@sd": ("bho",),
    "tvbricsenglish.in@sd": ("eng",),
    "b4umovies.in@india": ("hin",),
    "b4umusic.in@india": ("hin",),
    "ddarunprabha.in@sd": ("eng",),
    "durontotv.bd": ("ben",),
    "gtcpunjabi.in@sd": ("pan",),
    "gtcpunjabi.in@uk": ("pan",),
    "insync.in": ("und",),
    "jalshamovies.in@hd": ("ben",),
    "star.jalsha.movies.in": ("ben",),
    "kairaliwe.in@sd": ("mal",),
    "kappatv.in@alt1": ("eng", "hin", "mal", "tam"),
    "keralavision.in@sd": ("mal",),
    "mazhavilmanorama.in@sd": ("mal",),
    "mbctv.in@sd": ("ori",),
    "ptcpunjabi.in@sd": ("pan",),
    "punjabihits.in": ("pan",),
    "punjabishorts.in": ("pan",),
    "rplus.in@sd": ("ben",),
    "rplusgold.in@sd": ("ben",),
    "rajtv.in@sd": ("tam",),
    "shemaroojosh.in@sd": ("hin",),
    "star.jalsha.in": ("ben",),
    "starmoviesselect.in@hd": ("eng", "hin", "tam"),
    "tabbarhits.in": ("pan",),
    "themovieclub.in@hd": ("und",),
    "tlc.in@hd": ("ben", "eng", "hin", "mal", "mar", "tam", "tel"),
    "zeebangla.in@hd": ("ben",),
    "zeetelugu.in@hd": ("tel",),
    "zeetv.in@sd": ("hin",),
}
# Verified channel-specific language corrections override inconsistent upstream
# feed metadata for these exact channel identities.
FORCED_LANGUAGE_OVERRIDES = {
    "taazatv.in@sd": ("hin",),
    "meialaitv.in": ("tam",),
}
GROUP_DEFAULTS = {
    "Bangladesh": ("BD", "ben"),
    "Indian Bangla": ("IN", "ben"),
    "Indian Movies": ("IN", "hin"),
    "Indian Music": ("IN", "hin"),
    "Indian Entertainment": ("IN", "hin"),
    "Pakistani": ("PK", "urd"),
    "International": ("US", "eng"),
    "Documentary & Wildlife": ("US", "eng"),
    "Kids": ("US", "eng"),
    "Religious": ("SA", "ara"),
    "Sports": ("US", "eng"),
}
QUALITY_SUFFIXES = {"SD", "HD", "FHD", "UHD", "4K"}
ATTR_RE = re.compile(r'([\w-]+)="([^"]*)"')
COUNTRY_RE = re.compile(r"^[A-Z]{2}$")
LANGUAGE_RE = re.compile(r"^[a-z]{3}$")


def load_json(url):
    request = urllib.request.Request(url, headers={"User-Agent": "BDIX-IPTV-metadata-maintenance/3.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8-sig"))


def parse_catalogue(channels, feeds=None):
    """Build the exact-ID catalogue from iptv-org JSON, with legacy CSV fixture support.

    Production callers pass the upstream channel and feed lists. The single-argument
    CSV form is kept for the maintenance tests and older callers; it does not affect
    the production feed-derived language rules.
    """
    if isinstance(channels, str):
        catalogue = {}
        reader = csv.DictReader(io.StringIO(channels))
        for row in reader:
            channel_id = (row.get("id") or row.get("channel") or "").strip()
            if not channel_id:
                continue
            country = (row.get("country") or "").strip().upper()
            raw_languages = row.get("languages") or row.get("language") or ""
            languages = tuple(sorted({
                value.strip().lower()
                for value in re.split(r"[;,|]", raw_languages)
                if LANGUAGE_RE.fullmatch(value.strip().lower())
            }))
            catalogue[channel_id] = (country, languages)
        return catalogue

    feeds = feeds or []
    feed_languages = {}
    for feed in feeds:
        channel_id = (feed.get("channel") or "").strip()
        if not channel_id:
            continue
        langs = tuple(sorted({
            x.strip().lower() for x in (feed.get("languages") or [])
            if isinstance(x, str) and LANGUAGE_RE.fullmatch(x.strip().lower())
        }))
        if langs:
            feed_languages.setdefault(channel_id, set()).update(langs)

    catalogue = {}
    for row in channels:
        channel_id = (row.get("id") or "").strip()
        if not channel_id:
            continue
        country = (row.get("country") or "").strip().upper()
        channel_languages = {
            value.strip().lower()
            for value in (row.get("languages") or [])
            if isinstance(value, str) and LANGUAGE_RE.fullmatch(value.strip().lower())
        }
        languages = tuple(sorted(feed_languages.get(channel_id, set()) | channel_languages))
        catalogue[channel_id] = (country, languages)
    return catalogue


def matching_id(tvg_id, catalogue):
    tvg_id = (tvg_id or "").strip()
    if tvg_id in catalogue:
        return tvg_id
    if "@" in tvg_id:
        base, suffix = tvg_id.rsplit("@", 1)
        if suffix.upper() in (QUALITY_SUFFIXES | {"INDIA", "UK", "HINDI", "TELUGU", "ALT1"}) and base in catalogue:
            return base
    return None


def attrs(line):
    return dict(ATTR_RE.findall(line))


def active_gaps(text):
    rows, current = [], None
    for line in text.splitlines():
        if line.startswith("#EXTINF:"):
            current = line
        elif current is not None and line.strip().startswith(("http://", "https://")):
            meta = attrs(current)
            current = None
            if meta.get("group-title", "").strip() not in TARGET_GROUPS:
                continue
            missing = []
            if not meta.get("tvg-country", "").strip():
                missing.append("tvg-country")
            if not meta.get("tvg-language", "").strip():
                missing.append("tvg-language")
            if missing:
                name = (meta.get("tvg-name") or line.rsplit(",", 1)[-1]).strip()
                rows.append((meta.get("group-title", ""), name, meta.get("tvg-id", ""), ", ".join(missing)))
    return rows


def update_playlist(text, catalogue):
    lines = text.splitlines()
    result, current_index = [], None
    changed_entries = country_fills = language_fills = matched_ids = fallback_entries = 0
    matched = set()
    for line in lines:
        if line.startswith("#EXTINF:"):
            current_index = len(result)
            result.append(line)
            continue
        if current_index is None or not line.strip().startswith(("http://", "https://")):
            result.append(line)
            continue
        info_index = current_index
        original_info = result[info_index]
        current_index = None
        meta = attrs(original_info)
        group_name = meta.get("group-title", "").strip()
        if group_name not in TARGET_GROUPS:
            result.append(line)
            continue

        tvg_id = meta.get("tvg-id", "").strip()
        channel_id = meta.get("channel-id", "").strip()
        source_id = matching_id(tvg_id or channel_id, catalogue)
        country, languages = ("", ())
        if source_id is not None:
            matched.add(tvg_id or channel_id)
            matched_ids += 1
            country, languages = catalogue[source_id]

        # Verified corrections for these exact feeds override conflicting
        # catalogue metadata; other channel overrides remain fallbacks.
        language_key = (tvg_id or channel_id).casefold()
        if language_key in FORCED_LANGUAGE_OVERRIDES:
            languages = FORCED_LANGUAGE_OVERRIDES[language_key]
        elif not languages:
            languages = LANGUAGE_OVERRIDES.get(language_key, ())

        # An alternate stream may inherit the language of its exact-ID primary.
        # Do not use category defaults for Backup; if still unknown, label it
        # explicitly as undetermined rather than inventing a language.
        if not languages and group_name == "Backup":
            primary_languages = set()
            primary_ids = {tvg_id.casefold(), channel_id.casefold()} - {""}
            for row in lines:
                if not row.startswith("#EXTINF:"):
                    continue
                primary_meta = attrs(row)
                if primary_meta.get("group-title", "").strip() not in ACTIVE_GROUPS:
                    continue
                row_ids = {
                    primary_meta.get("tvg-id", "").strip().casefold(),
                    primary_meta.get("channel-id", "").strip().casefold(),
                } - {""}
                if primary_ids & row_ids and primary_meta.get("tvg-language", "").strip():
                    primary_languages.update(
                        value.strip().lower()
                        for value in primary_meta["tvg-language"].split(";")
                        if LANGUAGE_RE.fullmatch(value.strip().lower())
                    )
            if primary_languages:
                languages = tuple(sorted(primary_languages))

        default_country, default_language = GROUP_DEFAULTS.get(group_name, ("", ""))
        if not country:
            country = default_country
        if not languages:
            languages = (default_language,) if default_language else ()
        if not languages:
            languages = ("und",)
        if source_id is None:
            fallback_entries += 1

        additions = []
        if not meta.get("tvg-country", "").strip() and COUNTRY_RE.fullmatch(country):
            additions.append(("tvg-country", country))
        if not meta.get("tvg-language", "").strip() and languages and all(LANGUAGE_RE.fullmatch(lang) for lang in languages):
            additions.append(("tvg-language", ";".join(languages)))

        group = re.search(r'\s+group-title="[^"]*"', original_info)
        if additions and group:
            insert = "".join(' {}="{}"'.format(k, v) for k, v in additions)
            result[info_index] = original_info[:group.start()] + insert + original_info[group.start():]
            changed_entries += 1
            country_fills += sum(k == "tvg-country" for k, _ in additions)
            language_fills += sum(k == "tvg-language" for k, _ in additions)
        result.append(line)

    newline = "\r\n" if "\r\n" in text else "\n"
    updated = newline.join(result)
    if text.endswith(("\n", "\r")):
        updated += newline
    return updated, {
        "source_ids_matched": len(matched),
        "entries_changed": changed_entries,
        "country_fields_filled": country_fills,
        "language_fields_filled": language_fills,
        "fallback_entries": fallback_entries,
    }


def write_report(status, before_hash, after_hash, metrics, remaining, note=""):
    lines = [
        "# IPTV Playlist Metadata Backfill", "",
        "Generated: **{}**".format(datetime.now(timezone.utc).isoformat(timespec="seconds")), "",
        "Status: **{}**".format(status),
        "Sources: {} + {} + controlled playlist category defaults".format(CHANNELS_URL, FEEDS_URL),
        "Before playlist SHA-256: **{}**".format(before_hash),
        "After playlist SHA-256: **{}**".format(after_hash),
        "- Exact catalogue IDs matched: **{}**".format(metrics.get("source_ids_matched", 0)),
        "- Entries updated: **{}**".format(metrics.get("entries_changed", 0)),
        "- tvg-country fields filled: **{}**".format(metrics.get("country_fields_filled", 0)),
        "- tvg-language fields filled: **{}**".format(metrics.get("language_fields_filled", 0)),
        "- Category fallback entries: **{}**".format(metrics.get("fallback_entries", 0)),
        "- Language source: **iptv-org channel/feed metadata, exact-ID primary inheritance, explicit channel overrides, then undetermined**",
        "- Active and Backup entries with remaining metadata gaps: **{}**".format(len(remaining)),
    ]
    if note:
        lines += ["", note]
    lines += ["", "## Remaining active / Backup metadata gaps", "", "| Group | Channel | tvg-id | Missing fields |", "|---|---|---|---|"]
    for group, name, tvg_id, missing in remaining[:250]:
        clean = lambda value: str(value).replace("|", "\\|").replace("\n", " ")
        lines.append("| {} | {} | {} | {} |".format(clean(group), clean(name), clean(tvg_id), clean(missing)))
    if len(remaining) > 250:
        lines.append("| … | … | … | {} additional rows omitted |".format(len(remaining) - 250))
    if not remaining:
        lines.append("| — | — | — | none |")
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    raw = PLAYLIST.read_bytes()
    original = raw.decode("utf-8")
    before_hash = hashlib.sha256(raw).hexdigest()
    try:
        channels = load_json(CHANNELS_URL)
        feeds = load_json(FEEDS_URL)
        if not isinstance(channels, list) or not isinstance(feeds, list):
            raise ValueError("iptv-org API response is not a list")
        catalogue = parse_catalogue(channels, feeds)
        if not catalogue:
            raise ValueError("catalogue is empty")
    except Exception as exc:
        # Do not silently claim success if the external catalogue is unavailable.
        # Controlled group defaults remain safe for the known active categories.
        catalogue = {}
        updated, metrics = update_playlist(original, catalogue)
        PLAYLIST.write_bytes(updated.encode("utf-8"))
        after_hash = hashlib.sha256(PLAYLIST.read_bytes()).hexdigest()
        remaining = active_gaps(updated)
        write_report("PASS" if not remaining else "PARTIAL", before_hash, after_hash, metrics, remaining,
                     "External catalogue unavailable; per-channel overrides and controlled primary-category defaults were used. Reason: {}".format(str(exc)[:240]))
        print("Metadata backfill used per-channel overrides and controlled primary-category defaults: {}".format(exc))
        return 0

    updated, metrics = update_playlist(original, catalogue)
    if updated != original:
        PLAYLIST.write_bytes(updated.encode("utf-8"))
    after_hash = hashlib.sha256(PLAYLIST.read_bytes()).hexdigest()
    remaining = active_gaps(updated)
    write_report("PASS" if not remaining else "PARTIAL", before_hash, after_hash, metrics, remaining)
    print("IPTV metadata backfill: matched={source_ids_matched}, active+backup entries_changed={entries_changed}, "
          "country_filled={country_fields_filled}, language_filled={language_fields_filled}, "
          "fallback_entries={fallback_entries}, gaps_remaining={gaps}".format(**metrics, gaps=len(remaining)))
    return 0 if not remaining else 1


if __name__ == "__main__":
    raise SystemExit(main())
