#!/usr/bin/env python3
"""Offline, deterministic EPG coverage for the published guide.

Reads only committed inputs (both playlists and epg/epg.xml), so it runs without
network access and can be re-run by any workflow or maintainer. It reports what
the public guide actually contains today, separately from source-mapping data.

Outputs:
  reports/epg-published-coverage.md    human-readable report
  reports/epg-published-coverage.json  machine-readable figures and input fingerprints

Definitions:
  identity            casefold(tvg-id or channel-id) of an active entry
  active entry        any entry outside Backup, Review, Not Playing, New Channels, New Backups
  published channel   identity present as <channel id> in epg/epg.xml
  usable programme    published channel with at least one programme whose stop is after
                      generation time and whose title is non-empty
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

QUEUE_GROUPS = {"Backup", "Review", "Not Playing", "New Channels", "New Backups"}
ATTR_RE = re.compile(r'([\w-]+)="([^"]*)"')
DEFAULT_INPUTS = {
    "primary": Path("IPTV-Playlist.m3u"),
    "international": Path("International-Playlist.m3u"),
    "epg": Path("epg/epg.xml"),
}
REPORT_MD = Path("reports/epg-published-coverage.md")
REPORT_JSON = Path("reports/epg-published-coverage.json")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_xmltv_time(value: str) -> datetime | None:
    value = (value or "").strip()
    match = re.match(r"^(\d{14})(?:\s*([+-])(\d{2})(\d{2}))?$", value)
    if not match:
        return None
    stamp = datetime.strptime(match.group(1), "%Y%m%d%H%M%S").replace(tzinfo=timezone.utc)
    if match.group(2):
        offset = timedelta(hours=int(match.group(3)), minutes=int(match.group(4)))
        stamp -= offset if match.group(2) == "+" else -offset
    return stamp


def playlist_entries(path: Path):
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    for index, line in enumerate(lines):
        if not line.startswith("#EXTINF"):
            continue
        attrs = dict(ATTR_RE.findall(line))
        url = next((item.strip() for item in lines[index + 1:index + 4] if item.startswith(("http://", "https://"))), "")
        yield attrs, url


def identity_of(attrs: dict) -> str:
    return (attrs.get("tvg-id") or attrs.get("channel-id") or "").strip().casefold()


def group_label(attrs: dict, source: str) -> str:
    """Group by the playlist's own group-title, which is the owner's category."""
    return (attrs.get("group-title") or "").strip() or "Unknown"


def build(inputs: dict[str, Path], now: datetime) -> dict:
    channels: dict[str, dict] = {}
    programmes: Counter = Counter()
    future_channels: set[str] = set()
    last_stop: dict[str, datetime] = {}
    root = ET.parse(inputs["epg"]).getroot()
    for channel in root.findall("channel"):
        channels[channel.get("id", "").strip().casefold()] = channel.get("id", "")
    for programme in root.iter("programme"):
        channel_id = (programme.get("channel") or "").strip().casefold()
        programmes[channel_id] += 1
        start, stop = parse_xmltv_time(programme.get("start")), parse_xmltv_time(programme.get("stop"))
        if stop and (channel_id not in last_stop or stop > last_stop[channel_id]):
            last_stop[channel_id] = stop
        title = (programme.findtext("title") or "").strip()
        if stop and stop > now and title and start is not None:
            future_channels.add(channel_id)

    identities: dict[str, dict] = {}
    backup_only: set[str] = set()
    per_group: dict[str, Counter] = defaultdict(Counter)
    for source in ("primary", "international"):
        active_ids: set[str] = set()
        backup_ids: set[str] = set()
        for attrs, _url in playlist_entries(inputs[source]):
            ident = identity_of(attrs)
            if not ident:
                continue
            group = (attrs.get("group-title") or "").strip()
            label = group_label(attrs, source)
            if group in QUEUE_GROUPS:
                if group == "Backup":
                    backup_ids.add(ident)
                continue
            active_ids.add(ident)
            identities.setdefault(ident, {"source": source, "group": label, "name": attrs.get("tvg-name", "")})
        backup_only |= backup_ids - set(identities)

    summary = Counter()
    for ident, info in identities.items():
        label = info["group"]
        published = ident in channels
        usable = ident in future_channels
        per_group[label]["published"] += int(published)
        per_group[label]["usable"] += int(usable)
        per_group[label]["missing"] += int(not published)
        per_group[label]["mapped_without_usable"] += int(published and not usable)
        summary["identities"] += 1
        summary["published"] += int(published)
        summary["usable"] += int(usable)
        summary["missing"] += int(not published)
        summary["mapped_without_usable"] += int(published and not usable)
    primary_ids = {i for i, v in identities.items() if v["source"] == "primary"}
    summary["primary_identities"] = len(primary_ids)
    summary["primary_published"] = sum(1 for i in primary_ids if i in channels)
    summary["primary_usable"] = sum(1 for i in primary_ids if i in future_channels)
    summary["published_channels_total"] = len(channels)
    summary["published_channels_with_future_programmes"] = len(future_channels & set(channels))
    summary["programmes_total"] = sum(programmes.values())
    summary["backup_only_identities"] = len(backup_only)
    no_future = [i for i in identities if i in channels and i not in future_channels]
    summary["published_no_programmes"] = sum(1 for i in no_future if i not in last_stop)
    summary["published_schedule_ended"] = sum(1 for i in no_future if i in last_stop and last_stop[i] <= now)

    groups = []
    for label in sorted(per_group):
        counts = per_group[label]
        total = sum(1 for v in identities.values() if v["group"] == label)
        if total == 0:
            continue
        groups.append({
            "group": label,
            "identities": total,
            "published": counts["published"],
            "usable": counts["usable"],
            "missing": counts["missing"],
            "mapped_without_usable": counts["mapped_without_usable"],
        })

    missing = sorted(
        ({"group": v["group"], "name": v["name"], "id": k} for k, v in identities.items() if k not in channels),
        key=lambda r: (r["group"], r["name"].casefold()),
    )
    mapped_no_usable = sorted(
        ({"group": v["group"], "name": v["name"], "id": k} for k, v in identities.items() if k in channels and k not in future_channels),
        key=lambda r: (r["group"], r["name"].casefold()),
    )
    return {
        "generated_at": now.isoformat(timespec="seconds"),
        "inputs": {name: {"path": str(path), "sha256": sha256(path)} for name, path in inputs.items()},
        "summary": dict(summary),
        "groups": groups,
        "missing": missing,
        "mapped_without_usable": mapped_no_usable,
    }


def pct(part: int, whole: int) -> str:
    return f"{(100.0 * part / whole):.1f}%" if whole else "n/a"


def render_markdown(data: dict) -> str:
    s = data["summary"]
    lines = [
        "# EPG Published Coverage",
        "",
        f"Generated: **{data['generated_at']}** (offline, from committed inputs)",
        "",
        "## Inputs",
        "",
        "| Input | SHA-256 |",
        "|---|---|",
    ]
    for name, meta in data["inputs"].items():
        lines.append(f"| `{meta['path']}` | `{meta['sha256']}` |")
    lines += [
        "",
        "## Figures",
        "",
        "| Measure | Count | Share |",
        "|---|---:|---:|",
        f"| Primary playlist identities (IPTV-Playlist, active groups) | {s['primary_identities']} | — |",
        f"| Unique active identities across both playlists | {s['identities']} | — |",
        f"| Identities published in XMLTV | {s['published']} | {pct(s['published'], s['identities'])} |",
        f"| Identities with a usable future programme | {s['usable']} | {pct(s['usable'], s['identities'])} |",
        f"| Published identities without usable future programmes | {s['mapped_without_usable']} | {pct(s['mapped_without_usable'], s['identities'])} |",
        f"| Identities missing from the guide | {s['missing']} | {pct(s['missing'], s['identities'])} |",
        f"| Primary identities published | {s['primary_published']} | {pct(s['primary_published'], s['primary_identities'])} |",
        f"| Primary identities with usable future programmes | {s['primary_usable']} | {pct(s['primary_usable'], s['primary_identities'])} |",
        f"| Channels in epg.xml | {s['published_channels_total']} | — |",
        f"| epg.xml channels with future programmes | {s['published_channels_with_future_programmes']} | — |",
        f"| Programmes in epg.xml | {s['programmes_total']} | — |",
        f"| Published identities with no programmes at all | {s['published_no_programmes']} | — |",
        f"| Published identities whose schedule has ended | {s['published_schedule_ended']} | — |",
        f"| Backup-only identities (not in active groups) | {s['backup_only_identities']} | — |",
        "",
        "## By group",
        "",
        "| Group | Identities | Published | Usable future | Missing | Published, no usable |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for row in data["groups"]:
        lines.append(
            f"| {row['group']} | {row['identities']} | {row['published']} | {row['usable']} | {row['missing']} | {row['mapped_without_usable']} |"
        )
    lines += [
        "",
        "## Notes",
        "",
        "- Figures are computed from the committed guide and playlists. They are not source-mapping counts.",
        "- A channel is usable only if it has at least one future programme with a non-empty title.",
        "- Source-level mapping and upstream availability are reported by `scripts/epg_coverage.py` when run",
        "  with network access. This report does not claim coverage that the published guide does not contain.",
        "",
        f"Missing identities: {len(data['missing'])} (listed in the JSON report).",
        f"Published without usable future programmes: {len(data['mapped_without_usable'])} (listed in the JSON report).",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="fail if the committed report is not current")
    args = parser.parse_args()
    now = datetime.now(timezone.utc).replace(microsecond=0)
    data = build(DEFAULT_INPUTS, now)
    markdown = render_markdown(data)
    payload = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    if args.check:
        ok = REPORT_JSON.exists() and all(
            json.loads(REPORT_JSON.read_text(encoding="utf-8"))["inputs"][name]["sha256"] == meta["sha256"]
            for name, meta in data["inputs"].items()
        )
        if not ok:
            raise SystemExit("reports/epg-published-coverage.json does not match the current playlists or epg.xml.")
        print("OK: EPG coverage report fingerprints match current inputs.")
        return 0
    REPORT_MD.write_text(markdown, encoding="utf-8")
    REPORT_JSON.write_text(payload, encoding="utf-8")
    print(json.dumps(data["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
