#!/usr/bin/env python3
"""Read-only qualification probe for the amazeyourself/epg XMLTV exports.

This deliberately does not add the feeds to the public EPG generator. It checks
reachability, XMLTV structure, valid current/future schedules, and strict channel
identity matches against both maintained playlists. Results are evidence for
manual source/rights review, not automatic mapping instructions.
"""
import gzip
import os
import re
import sys
import unicodedata
import urllib.request
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from io import BytesIO
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLAYLISTS = ("IPTV-Playlist.m3u", "International-Playlist.m3u")
TIMEOUT_SECONDS = 45
MAX_FEED_BYTES = 35 * 1024 * 1024
USER_AGENT = "BDIX-IPTV-EPG-Source-Probe/1.0"
INACTIVE_GROUPS = {
    "backup", "review", "test", "not playing", "new channels",
    "new backups", "new backup",
}
PLACEHOLDER_TITLES = {
    "", "tba", "tbc", "to be announced", "unknown", "no information",
    "no programme information", "schedule", "program", "programme",
    "movie", "movies", "live", "live tv", "test", "testing",
}
ATTR_RE = re.compile(r'([\w-]+)="([^"]*)"')
TIME_RE = re.compile(r"^(\d{8})T?(\d{6})\s*([+-]\d{2}:?\d{2})$")

FEEDS = (
    (
        "KableOne",
        "https://raw.githubusercontent.com/amazeyourself/epg/main/epg/kableone.xml",
    ),
    (
        "NeoTV+",
        "https://raw.githubusercontent.com/amazeyourself/epg/main/epg/neotv.xml",
    ),
    (
        "Oli TV",
        "https://raw.githubusercontent.com/amazeyourself/epg/main/epg/olitv.xml",
    ),
    (
        "RunnTV",
        "https://raw.githubusercontent.com/amazeyourself/epg/main/epg/runntv.xml",
    ),
)


def normalize_name(value):
    """Strict comparison key: case, accents, punctuation and HD/SD suffix only."""
    value = unicodedata.normalize("NFKD", str(value or ""))
    value = "".join(char for char in value if not unicodedata.combining(char))
    value = re.sub(r"[^a-z0-9]+", "", value.casefold())
    return re.sub(r"(?:hd|sd)$", "", value)


def parse_xmltv_datetime(value):
    """Parse common XMLTV timestamps, including the KableOne date-time separator."""
    text = re.sub(r"\s+", " ", str(value or "").strip())
    match = TIME_RE.fullmatch(text)
    if not match:
        return None
    offset = match.group(3)
    if len(offset) == 5:
        offset = offset[:3] + ":" + offset[3:]
    try:
        parsed = datetime.strptime(
            match.group(1) + match.group(2) + offset,
            "%Y%m%d%H%M%S%z",
        )
        return parsed.astimezone(timezone.utc)
    except ValueError:
        return None


def parse_playlist_text(text, playlist_name):
    """Return active playlist identities keyed by tvg-id."""
    channels = {}
    current = None
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if line.startswith("#EXTINF:"):
            attrs = dict(ATTR_RE.findall(line))
            display = line.split(",", 1)[1].strip() if "," in line else ""
            current = {
                "id": attrs.get("tvg-id", "").strip(),
                "tvg_name": attrs.get("tvg-name", "").strip(),
                "name": display,
                "group": attrs.get("group-title", "").strip(),
                "country": attrs.get("tvg-country", "").strip().upper(),
                "playlists": {playlist_name},
                "names": set(),
            }
            continue
        if current and line.startswith(("http://", "https://")):
            channel_id = current["id"]
            if channel_id and current["group"].casefold() not in INACTIVE_GROUPS:
                record = channels.setdefault(
                    channel_id,
                    {
                        "id": channel_id,
                        "names": set(),
                        "groups": set(),
                        "countries": set(),
                        "playlists": set(),
                    },
                )
                for candidate in (current["name"], current["tvg_name"]):
                    if candidate:
                        record["names"].add(candidate)
                record["groups"].add(current["group"])
                if current["country"]:
                    record["countries"].add(current["country"])
                record["playlists"].add(playlist_name)
            current = None
    return channels


def load_playlist_channels():
    combined = {}
    for filename in PLAYLISTS:
        path = ROOT / filename
        if not path.is_file():
            raise FileNotFoundError(f"Required playlist is missing: {filename}")
        parsed = parse_playlist_text(path.read_text(encoding="utf-8-sig"), filename)
        for channel_id, record in parsed.items():
            target = combined.setdefault(
                channel_id,
                {
                    "id": channel_id,
                    "names": set(),
                    "groups": set(),
                    "countries": set(),
                    "playlists": set(),
                },
            )
            target["names"].update(record["names"])
            target["groups"].update(record["groups"])
            target["countries"].update(record["countries"])
            target["playlists"].update(record["playlists"])
    return combined


def is_bangladesh_channel(channel):
    channel_id = channel["id"].casefold().split("@", 1)[0]
    return (
        "BD" in channel["countries"]
        or channel_id.endswith(".bd")
        or any(group.casefold() == "bangladesh" for group in channel["groups"])
    )


def fetch_feed(url):
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/xml,text/xml,*/*",
        },
    )
    with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
        data = response.read(MAX_FEED_BYTES + 1)
    if len(data) > MAX_FEED_BYTES:
        raise ValueError("feed exceeds the 35 MiB safety limit")
    if not data:
        raise ValueError("empty response")
    if data[:2] == b"\x1f\x8b":
        data = gzip.decompress(data)
    if b"<!DOCTYPE" in data.upper() or b"<!ENTITY" in data.upper():
        raise ValueError("DTD/entity declarations are not accepted")
    return data


def element_text(element, local_name):
    for child in element:
        if child.tag.rsplit("}", 1)[-1] == local_name:
            return (child.text or "").strip()
    return ""


def scan_xmltv(data, window_start, window_end):
    """Return channel names and programme counts without retaining programme rows."""
    channels = {}
    counts = defaultdict(lambda: {"valid": 0, "window": 0})
    invalid_times = 0
    invalid_titles = 0
    root_seen = False
    for _event, element in ET.iterparse(BytesIO(data), events=("start", "end")):
        tag = element.tag.rsplit("}", 1)[-1]
        if _event == "start" and tag == "tv":
            root_seen = True
            continue
        if _event != "end":
            continue
        if tag == "channel":
            channel_id = (element.get("id") or "").strip()
            if channel_id:
                display_names = []
                for child in element:
                    if child.tag.rsplit("}", 1)[-1] == "display-name":
                        name = (child.text or "").strip()
                        if name and name not in display_names:
                            display_names.append(name)
                channels[channel_id] = display_names
            element.clear()
        elif tag == "programme":
            channel_id = (element.get("channel") or "").strip()
            start = parse_xmltv_datetime(element.get("start"))
            stop = parse_xmltv_datetime(element.get("stop"))
            title = element_text(element, "title")
            if not channel_id or not start or not stop or stop <= start:
                invalid_times += 1
            elif title.casefold() in PLACEHOLDER_TITLES:
                invalid_titles += 1
            else:
                counts[channel_id]["valid"] += 1
                if stop >= window_start and start <= window_end:
                    counts[channel_id]["window"] += 1
            element.clear()
    if not root_seen:
        raise ValueError("document root is not an XMLTV <tv> element")
    return {
        "channels": channels,
        "counts": counts,
        "invalid_times": invalid_times,
        "invalid_titles": invalid_titles,
    }


def build_name_index(playlist_channels):
    index = defaultdict(set)
    for channel_id, channel in playlist_channels.items():
        for name in channel["names"]:
            key = normalize_name(name)
            if key:
                index[key].add(channel_id)
    return index


def find_exact_matches(feed_channels, programme_counts, playlist_channels):
    """Match only exact IDs or unique strict-normalized display names."""
    name_index = build_name_index(playlist_channels)
    matches = []
    ambiguous = []
    matched_ids = set()
    for feed_id, display_names in feed_channels.items():
        schedule_count = programme_counts.get(feed_id, {}).get("window", 0)
        if schedule_count <= 0:
            continue
        if feed_id in playlist_channels:
            candidate_ids = {feed_id}
            match_type = "EXACT_ID"
        else:
            candidate_ids = set()
            for display_name in display_names:
                candidate_ids.update(name_index.get(normalize_name(display_name), set()))
            if len(candidate_ids) > 1:
                ambiguous.append((feed_id, display_names, sorted(candidate_ids), schedule_count))
                continue
            if not candidate_ids:
                continue
            match_type = "EXACT_NAME"
        for playlist_id in sorted(candidate_ids):
            if playlist_id in matched_ids:
                continue
            matched_ids.add(playlist_id)
            channel = playlist_channels[playlist_id]
            matches.append(
                {
                    "playlist_id": playlist_id,
                    "playlist_names": sorted(channel["names"]),
                    "groups": sorted(channel["groups"]),
                    "country": ",".join(sorted(channel["countries"])),
                    "bangladesh": is_bangladesh_channel(channel),
                    "feed_id": feed_id,
                    "feed_names": display_names,
                    "match": match_type,
                    "programmes": schedule_count,
                }
            )
    return matches, ambiguous


def markdown_cell(value):
    return str(value or "").replace("|", "/").replace("\n", " ").strip()


def probe_feed(label, url, playlist_channels, window_start, window_end):
    data = fetch_feed(url)
    scan = scan_xmltv(data, window_start, window_end)
    matches, ambiguous = find_exact_matches(
        scan["channels"], scan["counts"], playlist_channels
    )
    channels_with_schedules = sum(
        1 for item in scan["counts"].values() if item["window"] > 0
    )
    return {
        "label": label,
        "url": url,
        "status": "OK",
        "bytes": len(data),
        "channel_count": len(scan["channels"]),
        "programme_rows": sum(item["valid"] for item in scan["counts"].values()),
        "window_rows": sum(item["window"] for item in scan["counts"].values()),
        "channels_with_schedules": channels_with_schedules,
        "invalid_times": scan["invalid_times"],
        "invalid_titles": scan["invalid_titles"],
        "matches": matches,
        "ambiguous": ambiguous,
        "bangladesh_matches": sum(1 for item in matches if item["bangladesh"]),
        "error": "",
    }


def main():
    output = Path(
        sys.argv[1] if len(sys.argv) > 1
        else "reports/epg-amazeyourself-source-probe.md"
    )
    playlist_channels = load_playlist_channels()
    now = datetime.now(timezone.utc)
    window_start = now - timedelta(hours=6)
    window_end = now + timedelta(days=7)
    results = []

    for label, url in FEEDS:
        try:
            result = probe_feed(
                label, url, playlist_channels, window_start, window_end
            )
        except Exception as exc:  # noqa: BLE001 - each failed feed remains auditable
            result = {
                "label": label,
                "url": url,
                "status": "FAILED",
                "bytes": 0,
                "channel_count": 0,
                "programme_rows": 0,
                "window_rows": 0,
                "channels_with_schedules": 0,
                "invalid_times": 0,
                "invalid_titles": 0,
                "matches": [],
                "ambiguous": [],
                "bangladesh_matches": 0,
                "error": f"{type(exc).__name__}: {str(exc)[:180]}",
            }
        results.append(result)
        print(
            f"{label}: {result['status']}; channels={result['channel_count']}; "
            f"valid_window_rows={result['window_rows']}; "
            f"exact_matches={len(result['matches'])}; "
            f"Bangladesh_matches={result['bangladesh_matches']}",
            flush=True,
        )

    all_matches = []
    for result in results:
        for match in result["matches"]:
            item = dict(match)
            item["feed"] = result["label"]
            all_matches.append(item)

    lines = [
        "# amazeyourself/epg external source qualification",
        "",
        f"Generated: **{now.isoformat(timespec='seconds')}**",
        "",
        "## Scope and safety",
        "",
        "- Read-only qualification probe for the four XMLTV exports published by "
        "amazeyourself/epg.",
        "- No schedule data is copied into the public guide, no playlist or mapping "
        "is changed, and no source is added to the production generator.",
        "- Matches are exact XMLTV ID or a unique display-name match after "
        "case/accent/punctuation normalization and removal of a trailing HD/SD "
        "quality suffix. No fuzzy matching is used.",
        "- The upstream repository's code licence does not, by itself, confirm "
        "rights to redistribute programme schedules. Each source remains subject "
        "to separate rights review before public ingestion.",
        "- No provider API key, user identifier, session token or account credential "
        "is used by this probe.",
        "",
        f"- Active unique playlist identities checked: **{len(playlist_channels)}**",
        f"- Bangladesh identities (Bangladesh group, BD country or .bd ID): "
        f"**{sum(1 for item in playlist_channels.values() if is_bangladesh_channel(item))}**",
        f"- XMLTV window: **{window_start.isoformat(timespec='minutes')}** to "
        f"**{window_end.isoformat(timespec='minutes')}**",
        "",
        "## Feed results",
        "",
        "| Feed | Status | XMLTV channels | Valid programme rows | Rows in window | Channels with schedules | Exact playlist matches | Bangladesh matches |",
        "|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for result in results:
        lines.append(
            "| " + " | ".join(
                markdown_cell(value) for value in (
                    result["label"], result["status"], result["channel_count"],
                    result["programme_rows"], result["window_rows"],
                    result["channels_with_schedules"], len(result["matches"]),
                    result["bangladesh_matches"],
                )
            ) + " |"
        )
    lines += [
        "",
        "## Exact matches with usable schedules",
        "",
        "| Feed | Playlist channel | Playlist tvg-id | Playlist group(s) | Feed channel | Feed display name(s) | Match type | Valid programme rows in window |",
        "|---|---|---|---|---|---|---|---:|",
    ]
    if all_matches:
        for item in sorted(
            all_matches,
            key=lambda row: (
                not row["bangladesh"], row["feed"], row["playlist_id"]
            ),
        ):
            lines.append(
                "| " + " | ".join(
                    markdown_cell(value) for value in (
                        item["feed"],
                        ", ".join(item["playlist_names"]),
                        item["playlist_id"],
                        ", ".join(item["groups"]),
                        item["feed_id"],
                        ", ".join(item["feed_names"]),
                        item["match"],
                        item["programmes"],
                    )
                ) + " |"
            )
    else:
        lines.append("| _No exact matches with valid current/future schedules_ | | | | | | | |")
    lines += [
        "",
        "## Ambiguous exact-name candidates",
        "",
        "These are deliberately not counted as matches because one feed name maps "
        "to multiple active playlist identities.",
        "",
        "| Feed | Feed channel ID | Feed display name(s) | Possible playlist tvg-ids | Programme rows in window |",
        "|---|---|---|---|---:|",
    ]
    ambiguous_rows = [
        (result["label"], *candidate)
        for result in results for candidate in result["ambiguous"]
    ]
    if ambiguous_rows:
        for label, feed_id, feed_names, candidate_ids, programme_count in ambiguous_rows:
            lines.append(
                "| " + " | ".join(
                    markdown_cell(value) for value in (
                        label, feed_id, ", ".join(feed_names),
                        ", ".join(candidate_ids), programme_count,
                    )
                ) + " |"
            )
    else:
        lines.append("| _None_ | | | | |")
    lines += [
        "",
        "## Feed diagnostics",
        "",
        "| Feed | Bytes downloaded | Invalid time/interval rows | Placeholder/empty-title rows | Error |",
        "|---|---:|---:|---:|---|",
    ]
    for result in results:
        lines.append(
            "| " + " | ".join(
                markdown_cell(value) for value in (
                    result["label"], result["bytes"], result["invalid_times"],
                    result["invalid_titles"], result["error"] or "-",
                )
            ) + " |"
        )
    lines += [
        "",
        "## Decision",
        "",
        "A source is eligible for a separate rights and implementation review only "
        "when it is reachable, has correctly timed non-placeholder schedules, and "
        "adds exact, unique channel matches. Bangladesh matches receive priority. "
        "No automatic production mapping or guide publication is performed.",
        "",
    ]

    output.parent.mkdir(parents=True, exist_ok=True)
    report = "\n".join(lines)
    output.write_text(report, encoding="utf-8")
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as summary:
            summary.write("\n".join(lines[:42]) + "\n")
    print(
        f"Wrote {output}; exact matches={len(all_matches)}; "
        f"Bangladesh matches={sum(1 for item in all_matches if item['bangladesh'])}",
        flush=True,
    )


if __name__ == "__main__":
    main()
