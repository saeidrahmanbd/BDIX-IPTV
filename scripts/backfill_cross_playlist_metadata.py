#!/usr/bin/env python3
"""Conservatively backfill missing country/language metadata across auxiliary playlists.

Only exact tvg-id/channel-id matches or globally unambiguous exact tvg-name matches are used.
Existing metadata, channel order, group placement, tvg-chno, stream URLs, and review
queues are never changed. Unknown or ambiguous values remain blank rather than guessed.
"""
import hashlib
import re
import unicodedata
import json
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

PLAYLISTS = (
    Path("IPTV-Playlist.m3u"),
    Path("International-Playlist.m3u"),
)
TARGETS = (Path("International-Playlist.m3u"),)
REPORT = Path("reports/playlist-metadata-backfill.md")
IPTV_ORG_CHANNELS_URL = "https://iptv-org.github.io/api/channels.json"
IPTV_ORG_FEEDS_URL = "https://iptv-org.github.io/api/feeds.json"
ID_SUFFIXES = {"SD", "HD", "FHD", "UHD", "4K", "INDIA", "UK", "HINDI", "TELUGU", "ALT1"}
ATTR_RE = re.compile(r'([\w-]+)="([^"]*)"')
COUNTRY_RE = re.compile(r"^[A-Z]{2}$")
LANGUAGE_LIST_RE = re.compile(r"^[a-z]{3}(?:;[a-z]{3})*$")
REVIEW_GROUPS = {"backup", "adult", "review", "new channels", "new backups", "not playing", "not playing...", "not playing…", "not playing... (review)"}


def attrs(line):
    return dict(ATTR_RE.findall(line))


def normalize_name(value):
    value = unicodedata.normalize("NFKC", str(value or "")).casefold().strip()
    return re.sub(r"\s+", " ", value)


def valid_country(value):
    value = (value or "").strip().upper()
    return value if COUNTRY_RE.fullmatch(value) else ""


def valid_languages(value):
    value = (value or "").strip().lower()
    return value if LANGUAGE_LIST_RE.fullmatch(value) else ""


def url_inventory(text):
    return [line.strip() for line in text.splitlines() if line.strip().startswith(("http://", "https://"))]


def playlist_rows(text):
    lines = text.splitlines(keepends=True)
    rows = []
    current_index = None
    for index, line in enumerate(lines):
        stripped = line.strip()
        if line.startswith("#EXTINF:"):
            current_index = index
        elif current_index is not None and stripped.startswith(("http://", "https://")):
            info = lines[current_index].rstrip("\r\n")
            metadata = attrs(info)
            rows.append({
                "index": current_index,
                "line": info,
                "attrs": metadata,
                "url": stripped,
                "group": metadata.get("group-title", "").strip(),
            })
            current_index = None
    return rows


def build_indexes(text_by_path):
    id_values = defaultdict(lambda: {"country": set(), "language": set()})
    name_values = defaultdict(lambda: {"ids": set(), "country": set(), "language": set()})
    for path in PLAYLISTS:
        text = text_by_path.get(path)
        if text is None:
            continue
        for row in playlist_rows(text):
            meta = row["attrs"]
            if row["group"].casefold() in REVIEW_GROUPS:
                continue
            channel_ids = {
                value.strip()
                for value in (meta.get("tvg-id", ""), meta.get("channel-id", ""))
                if value.strip()
            }
            name_key = normalize_name(meta.get("tvg-name") or row["line"].rsplit(",", 1)[-1])
            country = valid_country(meta.get("tvg-country", ""))
            language = valid_languages(meta.get("tvg-language", ""))
            for channel_id in channel_ids:
                item = id_values[channel_id]
                if country:
                    item["country"].add(country)
                if language:
                    item["language"].add(language)
            if name_key:
                item = name_values[name_key]
                for channel_id in channel_ids:
                    item["ids"].add(channel_id)
                if country:
                    item["country"].add(country)
                if language:
                    item["language"].add(language)
    by_id = {
        channel_id: {
            "country": next(iter(values["country"])) if len(values["country"]) == 1 else "",
            "language": next(iter(values["language"])) if len(values["language"]) == 1 else "",
        }
        for channel_id, values in id_values.items()
    }
    by_name = {}
    for name, values in name_values.items():
        # Name-only propagation is allowed only where all references point to one ID.
        # Repeated generic names or conflicting metadata remain unresolved.
        if len(values["ids"]) == 1:
            by_name[name] = {
                "country": next(iter(values["country"])) if len(values["country"]) == 1 else "",
                "language": next(iter(values["language"])) if len(values["language"]) == 1 else "",
            }
    return by_id, by_name


def build_external_indexes(channels, feeds):
    """Build conservative exact-ID and unique-name metadata from iptv-org."""
    language_by_channel = defaultdict(set)
    for feed in feeds if isinstance(feeds, list) else []:
        channel_id = str(feed.get("channel") or "").strip()
        if not channel_id:
            continue
        for language in feed.get("languages") or []:
            value = str(language).strip().lower()
            if re.fullmatch(r"[a-z]{3}", value):
                language_by_channel[channel_id].add(value)

    values_by_id = {}
    names = defaultdict(lambda: {"ids": set(), "country": set(), "language": set()})
    for channel in channels if isinstance(channels, list) else []:
        channel_id = str(channel.get("id") or "").strip()
        if not channel_id:
            continue
        country = valid_country(channel.get("country") or "")
        languages = set(language_by_channel.get(channel_id, set()))
        # The API channel record may also expose languages in some versions.
        for language in channel.get("languages") or []:
            value = str(language).strip().lower()
            if re.fullmatch(r"[a-z]{3}", value):
                languages.add(value)
        values_by_id[channel_id] = {
            "country": country,
            "language": ";".join(sorted(languages)) if languages else "",
        }
        for name in [channel.get("name"), *(channel.get("alt_names") or [])]:
            key = normalize_name(name)
            if not key:
                continue
            names[key]["ids"].add(channel_id)
            if country:
                names[key]["country"].add(country)
            names[key]["language"].update(languages)

    by_name = {}
    for name, values in names.items():
        if len(values["ids"]) == 1:
            by_name[name] = {
                "country": next(iter(values["country"])) if len(values["country"]) == 1 else "",
                "language": ";".join(sorted(values["language"])) if values["language"] else "",
            }
    return values_by_id, by_name


def merge_external_indexes(by_id, by_name, external_id, external_name):
    """Use upstream data only where local exact-ID/name evidence is missing."""
    for channel_id, source in external_id.items():
        target = by_id.setdefault(channel_id, {"country": "", "language": ""})
        if not target.get("country") and source.get("country"):
            target["country"] = source["country"]
        if not target.get("language") and source.get("language"):
            target["language"] = source["language"]
    for name, source in external_name.items():
        target = by_name.setdefault(name, {"country": "", "language": ""})
        if not target.get("country") and source.get("country"):
            target["country"] = source["country"]
        if not target.get("language") and source.get("language"):
            target["language"] = source["language"]


def load_external_indexes():
    """Fetch current public channel/feed metadata; fail soft to local evidence."""
    def load(url):
        request = urllib.request.Request(url, headers={"User-Agent": "BDIX-IPTV metadata audit"})
        with urllib.request.urlopen(request, timeout=25) as response:
            return json.loads(response.read().decode("utf-8"))
    channels = load(IPTV_ORG_CHANNELS_URL)
    feeds = load(IPTV_ORG_FEEDS_URL)
    if not isinstance(channels, list) or not isinstance(feeds, list):
        raise ValueError("iptv-org channel/feed response is not a JSON list")
    return build_external_indexes(channels, feeds)


def backfill_text(text, by_id, by_name):
    lines = text.splitlines(keepends=True)
    updated = list(lines)
    counts = {
        "entries_changed": 0,
        "country_fields_filled": 0,
        "language_fields_filled": 0,
        "language_fields_marked_undetermined": 0,
        "ambiguous_or_unknown": 0,
    }
    current_index = None
    for index, line in enumerate(lines):
        if line.startswith("#EXTINF:"):
            current_index = index
            continue
        if current_index is None or not line.strip().startswith(("http://", "https://")):
            continue

        info_index = current_index
        info = updated[info_index]
        meta = attrs(info)
        group = meta.get("group-title", "").strip().casefold()
        current_index = None
        if group in REVIEW_GROUPS:
            continue

        channel_ids = {
            value.strip()
            for value in (meta.get("tvg-id", ""), meta.get("channel-id", ""))
            if value.strip()
        }
        name_key = normalize_name(meta.get("tvg-name") or info.rsplit(",", 1)[-1])
        id_sources = []
        for channel_id in channel_ids:
            source = by_id.get(channel_id)
            if source is None and "@" in channel_id:
                base, suffix = channel_id.rsplit("@", 1)
                if suffix.upper() in ID_SUFFIXES:
                    source = by_id.get(base)
            if source is not None:
                id_sources.append(source)
        country_values = {valid_country(source.get("country", "")) for source in id_sources}
        language_values = {valid_languages(source.get("language", "")) for source in id_sources}
        country_values.discard("")
        language_values.discard("")
        country = next(iter(country_values)) if len(country_values) == 1 else ""
        language = next(iter(language_values)) if len(language_values) == 1 else ""
        if not country or not language:
            name_source = by_name.get(name_key, {}) if name_key else {}
            country = country or valid_country(name_source.get("country", ""))
            language = language or valid_languages(name_source.get("language", ""))

        additions = []
        if not meta.get("tvg-country", "").strip() and country:
            additions.append(("tvg-country", country))
        if not meta.get("tvg-language", "").strip():
            if language:
                additions.append(("tvg-language", language))
            else:
                # ISO 639-2 "und" means undetermined. Never guess a broadcast language.
                additions.append(("tvg-language", "und"))
                counts["language_fields_marked_undetermined"] += 1
        if not additions:
            if not meta.get("tvg-country", "").strip() or not meta.get("tvg-language", "").strip():
                counts["ambiguous_or_unknown"] += 1
            continue

        match = re.search(r'\s+group-title="[^"]*"', info)
        if not match:
            counts["ambiguous_or_unknown"] += 1
            continue
        insert = "".join(f' {key}="{value}"' for key, value in additions)
        body = info.rstrip("\r\n")
        trailing = info[len(body):]
        updated[info_index] = body[:match.start()] + insert + body[match.start():] + trailing
        counts["entries_changed"] += 1
        counts["country_fields_filled"] += sum(key == "tvg-country" for key, _ in additions)
        counts["language_fields_filled"] += sum(key == "tvg-language" for key, _ in additions)
    return "".join(updated), counts


def main():
    text_by_path = {}
    original_urls = {}
    for path in PLAYLISTS:
        if not path.is_file():
            raise SystemExit(f"Required playlist is missing: {path}")
        text = path.read_bytes().decode("utf-8-sig")
        text_by_path[path] = text
        original_urls[path] = url_inventory(text)

    by_id, by_name = build_indexes(text_by_path)
    external_status = "unavailable"
    try:
        external_id, external_name = load_external_indexes()
        merge_external_indexes(by_id, by_name, external_id, external_name)
        external_status = "loaded"
        print("Loaded iptv-org exact channel/feed metadata indexes.")
    except Exception as exc:
        print("iptv-org metadata unavailable; using exact cross-playlist evidence only: {}".format(str(exc)[:240]))
    summary = {}
    for path in TARGETS:
        raw = path.read_bytes()
        has_bom = raw.startswith(b"\xef\xbb\xbf")
        before = raw.decode("utf-8-sig")
        updated, counts = backfill_text(before, by_id, by_name)
        if url_inventory(before) != url_inventory(updated):
            raise SystemExit(f"Safety check failed: stream URL inventory changed in {path}")
        if updated != before:
            output = (b"\xef\xbb\xbf" if has_bom else b"") + updated.encode("utf-8")
            path.write_bytes(output)

        after_raw = path.read_bytes()
        after_text = after_raw.decode("utf-8-sig")
        if url_inventory(after_text) != original_urls[path]:
            raise SystemExit(f"Safety check failed: stream URL inventory changed after writing {path}")
        summary[path.name] = {
            **counts,
            "sha256": hashlib.sha256(after_raw).hexdigest(),
            "stream_urls_unchanged": True,
            "entries_missing_country_or_language_after": sum(
                1 for row in playlist_rows(after_text)
                if row["group"].casefold() not in REVIEW_GROUPS
                and (not row["attrs"].get("tvg-country", "").strip() or not row["attrs"].get("tvg-language", "").strip())
            ),
        }

    main_path = Path("IPTV-Playlist.m3u")
    summary[main_path.name] = {
        "entries_changed": 0,
        "country_fields_filled": 0,
        "language_fields_filled": 0,
        "ambiguous_or_unknown": 0,
        "sha256": hashlib.sha256(main_path.read_bytes()).hexdigest(),
        "stream_urls_unchanged": True,
        "entries_missing_country_or_language_after": sum(
            1 for row in playlist_rows(main_path.read_text(encoding="utf-8-sig"))
            if row["group"].casefold() not in REVIEW_GROUPS
            and (not row["attrs"].get("tvg-country", "").strip() or not row["attrs"].get("tvg-language", "").strip())
        ),
    }

    inventory_hash = {}
    for path in PLAYLISTS:
        actual = url_inventory(path.read_bytes().decode("utf-8-sig"))
        if actual != original_urls[path]:
            raise SystemExit(f"Safety check failed: stream URL inventory changed in {path}")
        inventory_hash[path.name] = hashlib.sha256("\n".join(actual).encode("utf-8")).hexdigest()

    lines = [
        "# Cross-Playlist Metadata Backfill", "",
        f"Generated: **{datetime.now(timezone.utc).isoformat(timespec='seconds')}**", "",
        "## Source playlist fingerprints", "",
        *[f"- {path.name} SHA-256: **{summary[path.name]['sha256']}**" for path in PLAYLISTS],
        "",
        "Only missing tvg-country and tvg-language values were filled. Sources: exact playlist tvg-id/channel-id, unique exact channel names, and iptv-org channel/feed metadata. Unresolved broadcast languages are marked und (ISO 639-2 undetermined), never guessed. iptv-org catalogue status: {}.".format(external_status),
        "The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Review/Adult/Not Playing entries.", "",
        "## Playlist results", "",
        "| Playlist | Entries changed | Country fields filled | Language fields filled | Language marked undetermined | Active entries still missing either field | Stream URL inventory | SHA-256 |",
        "|---|---:|---:|---:|---:|---:|---|---|",
    ]
    for path in PLAYLISTS:
        item = summary[path.name]
        inv = inventory_hash[path.name]
        lines.append(
            f"| {path.name} | {item.get('entries_changed', 0)} | {item.get('country_fields_filled', 0)} | "
            f"{item.get('language_fields_filled', 0)} | {item.get('language_fields_marked_undetermined', 0)} | "
            f"{item.get('entries_missing_country_or_language_after', 0)} | unchanged ({inv[:12]}...) | {item['sha256']} |"
        )
    lines += [
        "", "## Policy", "",
        "- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.",
        "- Country/language values are not inferred from group names alone.",
        "- Complete metadata does not guarantee EPG schedule coverage.", "",
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("Cross-playlist metadata backfill complete:")
    for playlist, item in summary.items():
        print(
            f"  {playlist}: entries changed={item.get('entries_changed', 0)}, "
            f"country={item.get('country_fields_filled', 0)}, "
            f"language={item.get('language_fields_filled', 0)}, "
            f"undetermined={item.get('language_fields_marked_undetermined', 0)}, "
            f"remaining gaps={item.get('entries_missing_country_or_language_after', 'n/a')}"
        )


if __name__ == "__main__":
    main()
