#!/usr/bin/env python3
"""Regenerate a read-only, current-state metadata report from the published playlist."""
import hashlib
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

PLAYLIST = Path("IPTV-Playlist.m3u")
REPORT = Path("reports/metadata-normalization.md")
ACTIVE_GROUPS = {"Bangladesh", "Indian Bangla", "Indian Movies", "Indian Music", "Indian Entertainment", "Pakistani", "International", "Documentary & Wildlife", "Kids", "Religious", "Sports"}
REVIEW_GROUPS = {"Backup", "Not Playing"}
ATTR = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
RAW_BASE = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/"


def parse_rows(text):
    rows, current = [], None
    for line in text.splitlines():
        if line.startswith("#EXTINF:"):
            current = {"info": line, "url": ""}
        elif current is not None and line.strip().startswith(("http://", "https://")):
            current["url"] = line.strip()
            current["meta"] = dict(ATTR.findall(current["info"]))
            rows.append(current)
            current = None
    return rows


def main():
    raw = PLAYLIST.read_bytes()
    rows = parse_rows(raw.decode("utf-8-sig"))
    active = [r for r in rows if r["meta"].get("group-title", "").strip() in ACTIVE_GROUPS]
    review = [r for r in rows if r["meta"].get("group-title", "").strip() in REVIEW_GROUPS]
    missing_chno = sum(not r["meta"].get("tvg-chno", "").strip() for r in active)
    missing_logo = sum(not r["meta"].get("tvg-logo", "").strip() for r in rows)
    missing_country = sum(not r["meta"].get("tvg-country", "").strip() for r in active)
    missing_language = sum(not r["meta"].get("tvg-language", "").strip() for r in active)
    local_refs = broken_local = 0
    for row in rows:
        logo = row["meta"].get("tvg-logo", "").strip()
        if not logo.startswith(RAW_BASE):
            continue
        local_refs += 1
        rel = urlsplit(logo).path.split("/logos/", 1)[-1]
        if not (Path("logos") / rel).is_file():
            broken_local += 1

    digest = hashlib.sha256(raw).hexdigest()
    lines = [
        "# Playlist Metadata Normalization", "",
        f"Generated: **{datetime.now(timezone.utc).isoformat(timespec='seconds')}**",
        f"Source playlist SHA-256: **{digest}**", "",
        "Read-only snapshot of the current playlist. It does not apply or imply any metadata changes.", "",
        f"- Complete EXTINF entries: **{len(rows)}**",
        f"- Active primary entries: **{len(active)}**",
        f"- Backup / Not Playing review entries: **{len(review)}**",
        f"- Active entries missing tvg-chno: **{missing_chno}**",
        f"- Active entries missing tvg-country: **{missing_country}**",
        f"- Active entries missing tvg-language: **{missing_language}**",
        f"- Entries missing tvg-logo: **{missing_logo}**",
        f"- Local repository logo references: **{local_refs}**",
        f"- Broken local logo references: **{broken_local}**", "",
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Current metadata report: {len(rows)} entries; playlist SHA-256 {digest}")


if __name__ == "__main__":
    main()
