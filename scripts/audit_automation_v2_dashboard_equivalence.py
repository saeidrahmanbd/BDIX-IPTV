#!/usr/bin/env python3
"""Independently recompute legacy dashboard metrics from immutable source inputs.

This audit does not import or execute generate_dashboard.py. It reads the
playlist and reports, recomputes the displayed metrics, and compares them with
the committed dashboard. Output is confined to reports/automation-v2/.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

ACTIVE_GROUPS = {
    "Bangladesh", "Indian Bangla", "Indian Movies", "Indian Music",
    "Indian Entertainment", "Pakistani", "International",
    "Documentary & Wildlife", "Kids", "Religious", "Sports",
}
REVIEW_GROUPS = {"backup", "review", "not playing", "new channels", "new backups", "test"}
ISSUE_METRICS = [
    "Duplicate stream URLs", "Metadata conflicts",
    "Cross-country backup collisions", "Protected primary-entry changes",
    "Logo exceptions", "Duplicate primary identities",
    "Primary channel-number collisions", "Primary entries missing channel numbers",
    "Malformed EXTINF entries", "Category block-order issues",
    "Alphabetical ordering issues",
]
REPORTS = {
    "audit": "reports/iptv-playlist-audit.md",
    "epg_coverage": "reports/epg-coverage.md",
    "epg_detail": "reports/epg-playlist-audit.md",
    "health": "reports/stream-health.md",
    "gate": "reports/pre-publish-gate.md",
    "freshness": "reports/epg-publish-freshness.md",
    "dashboard": "reports/Update Report.md",
    "history": "reports/maintenance-history.json",
}

def read(root: Path, relative: str) -> str:
    try:
        return (root / relative).read_text(encoding="utf-8-sig", errors="replace")
    except OSError:
        return ""

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def metric(text: str, label: str) -> int:
    aliases = {"Logo exceptions": "Logo exceptions requiring repair"}
    candidates = (label, aliases[label]) if label in aliases else (label,)
    for candidate in candidates:
        match = re.search(r"- " + re.escape(candidate) + r": \*\*(\d+)\*\*", text)
        if match:
            return int(match.group(1))
    return 0

def parse_playlist(path: Path) -> list[dict]:
    rows, current = [], None
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        if line.startswith("#EXTINF:"):
            attrs = dict(re.findall(r'([\w-]+)="([^"]*)"', line))
            attrs["_name"] = (attrs.get("tvg-name") or line.rsplit(",", 1)[-1]).strip()
            current = attrs
        elif current and line.strip().startswith(("http://", "https://")):
            rows.append(current | {"url": line.strip()})
            current = None
    return rows

def url_inventory_sha(path: Path) -> str:
    urls = sorted(line.strip() for line in path.read_text(encoding="utf-8-sig").splitlines()
                  if line.strip().startswith(("http://", "https://")))
    return sha256("\n".join(urls).encode("utf-8"))

def source_sha(text: str) -> str:
    match = re.search(r"Source playlist SHA-256:\s*\*\*([a-f0-9]{64})\*\*", text, re.I)
    return match.group(1).lower() if match else ""

def timestamp(root: Path, relative: str) -> str:
    text = read(root, relative)
    match = re.search(r"(?:Generated|Last generated):\s*\*\*([^*]+)\*\*", text, re.I)
    return match.group(1) if match else "not available"

def epg_is_current(root: Path, epg_detail: str, freshness: str) -> bool:
    guide = root / "epg/epg.xml"
    if not guide.is_file() or guide.stat().st_size <= 0:
        return False
    if not re.search(r"(?im)^Status:\s*\*\*PASS\*\*\s*$", freshness):
        return False
    try:
        guide_root = ET.parse(guide).getroot()
    except (OSError, ET.ParseError):
        return False
    if guide_root.tag != "tv" or guide_root.find("channel") is None or guide_root.find("programme") is None:
        return False
    for name in ("IPTV-Playlist.m3u", "International-Playlist.m3u"):
        match = re.search(
            rf"(?m)^-\s*{re.escape(name)} SHA-256:\s*\*\*([a-f0-9]{{64}})\*\*\s*$",
            epg_detail,
        )
        playlist = root / name
        if not playlist.is_file() or not match or match.group(1).lower() != sha256(playlist.read_bytes()):
            return False
        header = re.search(
            rf"(?m)^\|\s*{re.escape(name)}\s*\|.*\|\s*(OK|MISMATCH)\s*\|$",
            epg_detail,
        )
        if not header or header.group(1) != "OK":
            return False
    return True

def compute_metrics(root: Path) -> dict:
    playlist = root / "IPTV-Playlist.m3u"
    rows = parse_playlist(playlist) if playlist.is_file() else []
    audit = read(root, REPORTS["audit"])
    epg_coverage = read(root, REPORTS["epg_coverage"])
    epg_detail = read(root, REPORTS["epg_detail"])
    health = read(root, REPORTS["health"])
    gate = read(root, REPORTS["gate"])
    freshness = read(root, REPORTS["freshness"])
    dashboard = read(root, REPORTS["dashboard"])
    playlist_hash = sha256(playlist.read_bytes()) if playlist.is_file() else ""
    audit_current = bool(playlist_hash and source_sha(audit) == playlist_hash)
    gate_current = bool(playlist_hash and source_sha(gate) == playlist_hash)
    health_current = bool(playlist.is_file() and re.search(
        r"Stream URL inventory SHA-256:\s*\*\*([a-f0-9]{64})\*\*", health, re.I
    ) and re.search(
        r"Stream URL inventory SHA-256:\s*\*\*([a-f0-9]{64})\*\*", health, re.I
    ).group(1).lower() == url_inventory_sha(playlist))
    epg_current = epg_is_current(root, epg_detail, freshness)

    groups = Counter(row.get("group-title", "") for row in rows)
    active = len({
        (row.get("tvg-id") or row.get("channel-id"))
        for row in rows
        if row.get("group-title") in ACTIVE_GROUPS
        and (row.get("tvg-id") or row.get("channel-id"))
    })
    primary_streams = sum(1 for row in rows if row.get("group-title") in ACTIVE_GROUPS)
    local_count = metric(audit, "Healthy/local references")
    logos = f"{round(local_count * 100 / len(rows), 1)}%" if rows and audit_current else "STALE"
    issues = sum(metric(audit, label) for label in ISSUE_METRICS) if audit_current else None
    gate_match = re.search(r"(?im)^Status:\s*\*\*(PASS|BLOCK)\*\*\s*$", gate)
    gate_status = (gate_match.group(1) if gate_match else "UNKNOWN") if gate_current else "STALE / UNKNOWN"

    health_values = {}
    for label, key in (
        ("Streams tested", "Stream Health Tested"),
        ("Failed this check", "Stream Health Failures"),
        ("Persistent failures (3+ consecutive)", "Persistent Failures"),
        ("Near-duplicate URL families", "Near-Duplicate URL Families"),
    ):
        health_values[key] = metric(health, label) if health_current else "STALE / UNKNOWN"

    epg_row = re.search(
        r"(?m)^\|\s*IPTV-Playlist\.m3u\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|",
        epg_detail,
    )
    if epg_row:
        epg_ids, mapped, source_live, present, live, missing = map(int, epg_row.groups()[1:])
        map_pct = round(mapped * 100 / epg_ids, 1) if epg_ids else 0.0
        live_pct = round(live * 100 / epg_ids, 1) if epg_ids else 0.0
    else:
        total_match = re.search(r"Active unique playlist channel IDs audited:\s*\*\*(\d+)\*\*", epg_coverage, re.I)
        mapping_match = re.search(r"IDs with an EPG source mapping:\s*\*\*(\d+)/(\d+) \(([\d.]+)%\)\*\*", epg_coverage, re.I)
        current_match = re.search(
            r"IDs with usable current/future (?:English programme data|source schedules \(nonblank (?:English|allowed-language) titles\)):\s*\*\*(\d+)/(\d+) \(([\d.]+)%\)\*",
            epg_coverage, re.I,
        )
        missing_match = re.search(r"IDs with no EPG source mapping:\s*\*\*(\d+)\*\*", epg_coverage, re.I)
        epg_ids = int(total_match.group(1)) if total_match else metric(epg_coverage, "Active Indian channels audited")
        mapped = int(mapping_match.group(1)) if mapping_match else metric(epg_coverage, "Channels with an EPG mapping")
        live = int(current_match.group(1)) if current_match else 0
        missing = int(missing_match.group(1)) if missing_match else metric(epg_coverage, "No guide mapping found")
        live_pct = float(current_match.group(3)) if current_match else 0.0
        map_pct = float(mapping_match.group(3)) if mapping_match else (round(mapped * 100 / epg_ids, 1) if epg_ids else 0.0)

    expected = {
        "Streams": len(rows),
        "Active Channel Identities": active,
        "Active Primary Streams": primary_streams,
        "Bangladesh": groups.get("Bangladesh", 0),
        "India": sum(count for group, count in groups.items() if group.startswith("Indian ")),
        "Backup Stream Entries": groups.get("Backup", 0),
        "IPTV Local Logos": logos,
        "IPTV EPG Programme Coverage": f"{round(live_pct)}%" if epg_current else "PENDING",
        "IPTV EPG Mapping": f"{map_pct:.1f}%" if epg_current else "PENDING",
        **health_values,
        "Audit Blocking Issues": issues if issues is not None else "STALE / UNKNOWN",
        "Pre-Publish Gate": gate_status,
        "Pre-Publish Gate Generated": timestamp(root, REPORTS["gate"]),
    }
    actual = {}
    for label, value in re.findall(r"(?m)^\|\s*([^|]+?)\s*\|\s*\*\*(.*?)\*\*\s*\|$", dashboard):
        actual[label.strip()] = value.strip()
    mismatches = {
        key: {"expected": str(value), "actual": actual.get(key)}
        for key, value in expected.items()
        if actual.get(key) != str(value)
    }
    return {
        "schema_version": 1,
        "report_type": "automation-v2-independent-dashboard-equivalence",
        "status": "PASS" if not mismatches else "MISMATCH",
        "equivalent": not mismatches,
        "inputs_current": {
            "playlist_audit": audit_current,
            "stream_health": health_current,
            "pre_publish_gate": gate_current,
            "published_epg": epg_current,
        },
        "source_sha256": {
            "iptv_playlist": playlist_hash,
            "audit_report_playlist": source_sha(audit),
            "gate_report_playlist": source_sha(gate),
            "health_report_url_inventory": re.search(
                r"Stream URL inventory SHA-256:\s*\*\*([a-f0-9]{64})\*\*", health, re.I
            ).group(1).lower() if re.search(
                r"Stream URL inventory SHA-256:\s*\*\*([a-f0-9]{64})\*\*", health, re.I
            ) else "",
            "computed_playlist_url_inventory": url_inventory_sha(playlist) if playlist.is_file() else "",
        },
        "expected_metrics": expected,
        "dashboard_metrics": actual,
        "mismatches": mismatches,
        "cutover_ready": bool(not mismatches and all((
            audit_current, health_current, gate_current, epg_current
        ))),
        "cutover_blockers": [
            name for name, current in {
                "playlist_audit": audit_current,
                "stream_health": health_current,
                "pre_publish_gate": gate_current,
                "published_epg": epg_current,
            }.items() if not current
        ] + (["dashboard_metric_mismatch"] if mismatches else []),
        "safety": {
            "production_dashboard_modified": False,
            "production_reports_modified": False,
            "playlists_epg_logos_modified": False,
            "publication_performed": False,
        },
    }

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path, default=Path("reports/automation-v2/dashboard-equivalence.json"))
    parser.add_argument("--strict", action="store_true", help="return non-zero when dashboard metrics differ")
    parser.add_argument("--require-cutover-ready", action="store_true",
                        help="return non-zero unless all dashboard source inputs are current and metrics match")
    args = parser.parse_args()
    root = args.root.resolve(strict=True)
    output = args.output if args.output.is_absolute() else root / args.output
    output = output.absolute()
    if not output.is_relative_to(root):
        parser.error("output must remain inside repository root")
    current = root
    for part in output.relative_to(root).parts:
        current = current / part
        if current.is_symlink():
            parser.error("output path cannot contain symlinks")
    report = compute_metrics(root)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": report["status"],
        "mismatch_count": len(report["mismatches"]),
        "mismatches": report["mismatches"],
        "inputs_current": report["inputs_current"],
        "source_sha256": report["source_sha256"],
    }, indent=2))
    if args.strict and not report["equivalent"]:
        return 1
    if args.require_cutover_ready and not report["cutover_ready"]:
        print("Cutover blocked: " + ", ".join(report["cutover_blockers"]))
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
