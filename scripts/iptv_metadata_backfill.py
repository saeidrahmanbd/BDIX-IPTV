#!/usr/bin/env python3
"""Fill blank IPTV metadata from current iptv-org channel/feed metadata only."""
import hashlib
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
    "Indian Entertainment", "Pakistani", "International",
    "Documentary & Wildlife", "Kids", "Religious", "Sports",
}
QUALITY_SUFFIXES = {"SD", "HD", "FHD", "UHD", "4K"}
ATTR_RE = re.compile(r'([\w-]+)="([^"]*)"')
COUNTRY_RE = re.compile(r"^[A-Z]{2}$")
LANGUAGE_RE = re.compile(r"^[a-z]{3}$")


def load_json(url):
    request = urllib.request.Request(url, headers={"User-Agent": "BDIX-IPTV-metadata-maintenance/2.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8-sig"))


def parse_catalogue(channels, feeds):
    """Return channel_id -> (country, unique feed languages).

    iptv-org removed channel-level languages in 2025. Feed-level languages are
    now the authoritative source, so combine languages from the channel's feeds.
    """
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
        languages = tuple(sorted(feed_languages.get(channel_id, set())))
        catalogue[channel_id] = (country, languages)
    return catalogue


def matching_id(tvg_id, catalogue):
    tvg_id = (tvg_id or "").strip()
    if tvg_id in catalogue:
        return tvg_id
    if "@" in tvg_id:
        base, suffix = tvg_id.rsplit("@", 1)
        if suffix.upper() in QUALITY_SUFFIXES and base in catalogue:
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
            if meta.get("group-title", "").strip() not in ACTIVE_GROUPS:
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
    changed_entries = country_fills = language_fills = matched_ids = 0
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
        if meta.get("group-title", "").strip() not in ACTIVE_GROUPS:
            result.append(line)
            continue
        source_id = matching_id(meta.get("tvg-id", ""), catalogue)
        if source_id is None:
            result.append(line)
            continue
        matched.add(meta.get("tvg-id", ""))
        country, languages = catalogue[source_id]
        additions = []
        if not meta.get("tvg-country", "").strip() and COUNTRY_RE.fullmatch(country):
            additions.append(("tvg-country", country))
        # Fill feed-level languages when the feed metadata gives a stable set.
        # Multiple explicit languages are retained as semicolon-separated values.
        if (
            not meta.get("tvg-language", "").strip()
            and languages
            and all(LANGUAGE_RE.fullmatch(lang) for lang in languages)
        ):
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
    }


def write_report(status, before_hash, after_hash, metrics, remaining, note=""):
    lines = [
        "# IPTV Playlist Metadata Backfill", "",
        "Generated: **{}**".format(datetime.now(timezone.utc).isoformat(timespec="seconds")), "",
        "Status: **{}**".format(status),
        "Sources: {} + {}".format(CHANNELS_URL, FEEDS_URL),
        "Before playlist SHA-256: **{}**".format(before_hash),
        "After playlist SHA-256: **{}**".format(after_hash),
        "- Exact catalogue IDs matched: **{}**".format(metrics.get("source_ids_matched", 0)),
        "- Entries updated: **{}**".format(metrics.get("entries_changed", 0)),
        "- tvg-country fields filled: **{}**".format(metrics.get("country_fields_filled", 0)),
        "- tvg-language fields filled: **{}**".format(metrics.get("language_fields_filled", 0)),
        "- Language source: **iptv-org feed-level languages**",
        "- Active entries with remaining metadata gaps: **{}**".format(len(remaining)),
    ]
    if note:
        lines += ["", note]
    lines += ["", "## Remaining active metadata gaps", "", "| Group | Channel | tvg-id | Missing fields |", "|---|---|---|---|"]
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
        remaining = active_gaps(original)
        write_report("SKIPPED", before_hash, before_hash, {}, remaining,
                     "Source unavailable/invalid; playlist was not changed. Reason: {}".format(str(exc)[:240]))
        print("Metadata backfill skipped safely: {}".format(exc))
        return 0

    updated, metrics = update_playlist(original, catalogue)
    if updated != original:
        PLAYLIST.write_bytes(updated.encode("utf-8"))
    after_hash = hashlib.sha256(PLAYLIST.read_bytes()).hexdigest()
    remaining = active_gaps(updated)
    write_report("PASS", before_hash, after_hash, metrics, remaining)
    print("IPTV metadata backfill: matched={source_ids_matched}, entries_changed={entries_changed}, "
          "country_filled={country_fields_filled}, language_filled={language_fields_filled}, "
          "gaps_remaining={gaps}".format(**metrics, gaps=len(remaining)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
