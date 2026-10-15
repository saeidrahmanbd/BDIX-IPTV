#!/usr/bin/env python3
"""Report Backup routes with no exact primary identity/name match; never delete entries."""
import re
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

PLAYLIST = Path("IPTV-Playlist.m3u")
REPORT = Path("reports/backup-orphan-audit.md")
ATTR = re.compile(r'([\w-]+)="([^"]*)"')
NON_PRIMARY = {"Backup", "New Backup", "Not Playing"}

def parse():
    lines = PLAYLIST.read_text(encoding="utf-8-sig").replace("\r", "").splitlines()
    rows, current = [], None
    for line_no, line in enumerate(lines, 1):
        if line.startswith("#EXTINF:"):
            a = dict(ATTR.findall(line))
            current = {"line":line_no, "name":a.get("tvg-name") or line.rsplit(",",1)[-1].strip(),
                       "id":(a.get("tvg-id") or a.get("channel-id") or "").strip(),
                       "group":a.get("group-title","").strip(), "url":""}
        elif current and line.strip().startswith(("http://","https://")):
            current["url"] = line.strip()
            rows.append(current)
            current = None
    return rows

def norm_name(value):
    value = unicodedata.normalize("NFKD", str(value or "")).casefold()
    value = "".join(c for c in value if not unicodedata.combining(c))
    value = re.sub(r"\[[^]]*\]|\([^)]*\)", " ", value)
    value = re.sub(r"\b(?:uhd|fhd|hd|sd|4k|1080p|720p|576p|480p|360p)\b", " ", value)
    return re.sub(r"[^a-z0-9]", "", value)

def main():
    rows = parse()
    primary = [x for x in rows if x["group"] not in NON_PRIMARY]
    backups = [x for x in rows if x["group"] == "Backup"]
    ids = {x["id"].casefold() for x in primary if x["id"]}
    names = {norm_name(x["name"]) for x in primary if norm_name(x["name"])}
    orphan = [x for x in backups if (not x["id"] or x["id"].casefold() not in ids)
              and norm_name(x["name"]) not in names]
    distinct = {}
    for x in orphan:
        distinct.setdefault(norm_name(x["name"]), x)
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    lines = [
        "# Backup Orphan Audit", "",
        f"Generated: **{now}**", "",
        "An orphan is a Backup route whose exact channel ID and normalized name do not match any primary entry in IPTV-Playlist.m3u. This is a candidate list, not proof that the stream is unusable or that a similarly named service is equivalent. No Backup entries are deleted by this audit.", "",
        "## Summary", "",
        f"- Primary entries checked: **{len(primary)}**",
        f"- Backup routes checked: **{len(backups)}**",
        f"- Orphan Backup routes: **{len(orphan)}**",
        f"- Distinct orphan channel labels: **{len(distinct)}**", "",
        "| Channel label | Channel ID (if present) | Stream host | Source line |",
        "|---|---|---|---:|"
    ]
    for x in orphan:
        host = urlsplit(x["url"]).hostname or "unknown"
        lines.append(f"| {x['name']} | {x['id'] or 'missing'} | {host} | {x['line']} |")
    if not orphan:
        lines.append("| — | — | — | — |")
    lines += ["", "## Action", "",
              "Review orphan routes before deleting or promoting them. Entries with signed, proxy, or credential-based URLs should be tested in the target player before any replacement or deletion. Aliases may require a verified mapping before this exact-name/ID audit can consider them linked.", ""]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Backup orphan audit: backup_routes={len(backups)} orphan_routes={len(orphan)} orphan_names={len(distinct)}")

if __name__ == "__main__":
    main()
