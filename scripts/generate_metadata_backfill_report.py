#!/usr/bin/env python3
"""Generate a read-only metadata-gap report from the current playlist."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import re

PLAYLIST = Path("IPTV-Playlist.m3u")
REPORT = Path("reports/iptv-metadata-backfill.md")
ACTIVE_GROUPS = {
    "Bangladesh", "Indian Bangla", "Indian Movies", "Indian Music",
    "Indian Entertainment", "Pakistani", "International",
    "Documentary & Wildlife", "Kids", "Religious", "Sports",
}
ATTR_RE = re.compile(r'([\w-]+)="([^"]*)"')

def main():
    raw = PLAYLIST.read_bytes()
    text = raw.decode("utf-8")
    digest = hashlib.sha256(raw).hexdigest()
    gaps = []
    current = None
    for line in text.splitlines():
        if line.startswith("#EXTINF:"):
            current = line
            continue
        if current is None or not line.strip().startswith(("http://", "https://")):
            continue
        meta = dict(ATTR_RE.findall(current))
        current = None
        if meta.get("group-title", "").strip() not in ACTIVE_GROUPS:
            continue
        missing = []
        if not meta.get("tvg-country", "").strip():
            missing.append("tvg-country")
        if not meta.get("tvg-language", "").strip():
            missing.append("tvg-language")
        if missing:
            gaps.append((meta.get("group-title", ""), meta.get("tvg-name", ""), meta.get("tvg-id", ""), ", ".join(missing)))

    lines = [
        "# IPTV Playlist Metadata Backfill", "",
        f"Generated: **{datetime.now(timezone.utc).isoformat(timespec='seconds')}**", "",
        f"Status: **{'PASS' if not gaps else 'REVIEW'}**",
        "Source: **current IPTV-Playlist.m3u**",
        f"Playlist SHA-256: **{digest}**",
        f"- Active entries with remaining metadata gaps: **{len(gaps)}**",
        "- This report is read-only and does not modify IPTV-Playlist.m3u.", "",
        "## Remaining active metadata gaps", "",
        "| Group | Channel | tvg-id | Missing fields |",
        "|---|---|---|---|",
    ]
    for group, name, tvg_id, missing in gaps:
        clean = lambda value: str(value).replace("|", "\\|").replace("\n", " ")
        lines.append(f"| {clean(group)} | {clean(name)} | {clean(tvg_id)} | {clean(missing)} |")
    if not gaps:
        lines.append("| — | — | — | none |")

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Metadata report generated: {len(gaps)} active gaps; playlist SHA {digest}")

if __name__ == "__main__":
    main()
