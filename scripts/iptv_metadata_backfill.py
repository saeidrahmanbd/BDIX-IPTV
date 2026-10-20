#!/usr/bin/env python3
"""Fill blank IPTV metadata from exact iptv-org channel IDs only."""
import csv
import hashlib
import io
import re
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

PLAYLIST = Path("IPTV-Playlist.m3u")
REPORT = Path("reports/iptv-metadata-backfill.md")
SOURCE_URL = "https://raw.githubusercontent.com/iptv-org/database/master/data/channels.csv"
ACTIVE_GROUPS = {
    "Bangladesh", "Indian Bangla", "Indian Movies", "Indian Music",
    "Indian Entertainment", "Pakistani", "International",
    "Documentary & Wildlife", "Kids", "Religious", "Sports",
}
QUALITY_SUFFIXES = {"SD", "HD", "FHD", "UHD", "4K"}
ATTR_RE = re.compile(r'([\w-]+)="([^"]*)"')
COUNTRY_RE = re.compile(r"^[A-Z]{2}$")
LANGUAGE_RE = re.compile(r"^[a-z]{3}$")


def parse_catalogue(text):
    reader = csv.DictReader(io.StringIO(text))
    required = {"id", "country", "languages"}
    if not reader.fieldnames or not required.issubset(set(reader.fieldnames)):
        raise ValueError("catalogue is missing id/country/languages columns")
    by_id, ambiguous = {}, set()
    for row in reader:
        channel_id = (row.get("id") or "").strip()
        if not channel_id:
            continue
        country = (row.get("country") or "").strip().upper()
        languages = tuple(x.strip().lower() for x in (row.get("languages") or "").split(";") if x.strip())
        value = (country, languages)
        if channel_id in by_id and by_id[channel_id] != value:
            ambiguous.add(channel_id)
        else:
            by_id[channel_id] = value
    for channel_id in ambiguous:
        by_id.pop(channel_id, None)
    return by_id


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
        original_info = result[current_index]
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
        # Only populate a single language; multi-language values remain for review.
        if (
            not meta.get("tvg-language", "").strip()
            and len(languages) == 1
            and LANGUAGE_RE.fullmatch(languages[0])
        ):
            additions.append(("tvg-language", languages[0]))
        group = re.search(r'\s+group-title="[^"]*"', original_info)
        if additions and group:
            insert = "".join(' {}="{}"'.format(k, v) for k, v in additions)
            result[current_index] = original_info[:group.start()] + insert + original_info[group.start():]
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
        "# IPTV Playlist Metadata Backfill",
        "",
        "Generated: **{}**".format(datetime.now(timezone.utc).isoformat(timespec="seconds")),
        "",
        "Status: **{}**".format(status),
        "Source catalogue: {}".format(SOURCE_URL),
        "Before playlist SHA-256: **{}**".format(before_hash),
        "After playlist SHA-256: **{}**".format(after_hash),
        "- Exact catalogue IDs matched: **{}**".format(metrics.get("source_ids_matched", 0)),
        "- Entries updated: **{}**".format(metrics.get("entries_changed", 0)),
        "- tvg-country fields filled: **{}**".format(metrics.get("country_fields_filled", 0)),
        "- tvg-language fields filled: **{}**".format(metrics.get("language_fields_filled", 0)),
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
    request = urllib.request.Request(SOURCE_URL, headers={"User-Agent": "BDIX-IPTV-metadata-maintenance/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            catalogue = parse_catalogue(response.read().decode("utf-8-sig"))
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
