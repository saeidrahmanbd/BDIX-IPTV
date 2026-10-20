#!/usr/bin/env python3
"""Generate a current, non-historical logo repair/status summary."""
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

PLAYLIST = Path("IPTV-Playlist.m3u")
MANIFEST = Path("reports/logo-authenticity-manifest.json")
OUT = Path("reports/playlist-logo-repair-results.md")
ATTR = re.compile(r'([\w-]+)="([^"]*)"')


def main():
    raw = PLAYLIST.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    playlist_status = manifest.get("status_counts_by_playlist", {}).get(PLAYLIST.name, {})
    total = manifest.get("counts_by_playlist", {}).get(PLAYLIST.name, 0)

    missing = external = 0
    for line in PLAYLIST.read_text(encoding="utf-8-sig").splitlines():
        if not line.startswith("#EXTINF:"):
            continue
        meta = dict(ATTR.findall(line))
        logo = meta.get("tvg-logo", "").strip()
        if not logo:
            missing += 1
        elif logo.startswith(("http://", "https://")) and "/raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/" not in logo:
            external += 1

    generated = datetime.now(timezone.utc).isoformat(timespec="seconds")
    lines = [
        "# IPTV Playlist Logo Repair Results — Current Status", "",
        f"Generated: **{generated}**",
        f"Source playlist SHA-256: **{digest}**", "",
        "This is the current logo status. The 2026-10-17 repair history is preserved separately in `reports/playlist-logo-repair-history-2026-10-17.md`.", "",
        "## Current results", "",
        "| Metric | Current |", "|---|---:|",
        f"| Playlist entries | **{total}** |",
        f"| Officially verified | **{playlist_status.get('official_verified', 0)}** |",
        f"| Third-party verified | **{playlist_status.get('third_party_verified', 0)}** |",
        f"| Generated fallback | **{playlist_status.get('generated_fallback', 0)}** |",
        f"| Needs review | **{playlist_status.get('needs_review', 0)}** |",
        f"| Missing logo references | **{missing}** |",
        f"| External/non-repository logo references | **{external}** |",
        "",
        "## Policy", "",
        "- Exact clean local assets are preferred over external references.",
        "- Generated fallback artwork is explicitly non-official and remains distinguishable from broadcaster branding.",
        "- Logo integrity and logo authenticity are separate checks: a readable image is not automatically an authentic broadcaster logo.",
        "- Playlist stream URLs are never deleted or reclassified by logo repair.",
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Current logo status generated: {total} entries; needs_review={playlist_status.get('needs_review', 0)}")


if __name__ == "__main__":
    main()
