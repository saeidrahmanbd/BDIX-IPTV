#!/usr/bin/env python3
"""Report Backup/Not Playing identity collisions without mutating the playlist."""
from __future__ import annotations

import csv
import re
from pathlib import Path

PLAYLIST = Path("IPTV-Playlist.m3u")
SNAPSHOT = Path("/tmp/iptv-protected-review.m3u")
REPORT = Path("reports/protected-review-identity-conflicts.csv")
SUMMARY = Path("reports/protected-review-identity-conflicts-summary.md")
REVIEW_GROUPS = {"Backup", "Not Playing"}
ATTR_RE = re.compile(r'([\w-]+)="([^"]*)"')


def attrs(info: str) -> dict[str, str]:
    return dict(ATTR_RE.findall(info))


def blocks(text: str) -> list[tuple[str, str]]:
    lines = text.replace("\r", "").splitlines()
    result: list[tuple[str, str]] = []
    i = 0
    while i < len(lines):
        if lines[i].startswith("#EXTINF:"):
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and lines[j].strip().lower().startswith(("http://", "https://")):
                result.append((lines[i], lines[j].strip()))
                i = j + 1
                continue
        i += 1
    return result


def identity(info: str) -> tuple[str, str]:
    a = attrs(info)
    return ((a.get("tvg-id") or a.get("channel-id") or "").strip().casefold(),
            a.get("tvg-name", "").strip().casefold())


def redact_url(raw: str) -> str:
    # Avoid exposing common URL credential patterns in report artifacts.
    raw = re.sub(r"(?i)([?&](?:token|auth|key|sig|signature|password|passwd|username|user|session)=)[^&#]*", r"\1[REDACTED]", raw)
    return re.sub(r"(?i)(/(?:live|hls|stream|play)/)[^/]+/[^/]+(?=/|$)", r"\1[REDACTED]/[REDACTED]", raw)


def main() -> int:
    if not PLAYLIST.is_file() or not SNAPSHOT.is_file():
        print("Protected identity conflict audit skipped: playlist or snapshot missing.")
        return 0
    protected = blocks(SNAPSHOT.read_text(encoding="utf-8", errors="replace"))
    current = blocks(PLAYLIST.read_text(encoding="utf-8-sig", errors="replace"))
    protected_ids = {identity(info) for info, _ in protected}
    protected_urls = {url.casefold() for _, url in protected}
    rows = []
    for info, url in current:
        key = identity(info)
        if not key[0] and not key[1]:
            continue
        if key not in protected_ids or url.casefold() in protected_urls:
            continue
        a = attrs(info)
        group = a.get("group-title", "").strip()
        rows.append({
            "impact_if_legacy_restore_used": "active primary stream at risk" if group not in REVIEW_GROUPS
              else "distinct review-queue URL at risk",
            "channel_name": a.get("tvg-name", info.rsplit(",", 1)[-1].strip()),
            "group": group,
            "identity": key[0],
            "url_redacted": redact_url(url),
            "would_legacy_code_remove": "yes",
            "reason": "same channel ID/name as a protected review entry, but a different URL",
        })
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    with REPORT.open("w", newline="", encoding="utf-8-sig") as handle:
        fields = ["impact_if_legacy_restore_used", "channel_name", "group", "identity", "url_redacted", "would_legacy_code_remove", "reason"]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    active = sum(r["impact_if_legacy_restore_used"] == "active primary stream at risk" for r in rows)
    review = len(rows) - active
    SUMMARY.write_text(
        "# Protected Review Identity Collision Audit\n\n"
        f"- Snapshot review entries: **{len(protected)}**\n"
        f"- Different-URL records sharing a protected identity: **{len(rows)}**\n"
        f"- Active primary streams the legacy restore logic would remove: **{active}**\n"
        f"- Distinct Backup/Not Playing URLs the legacy restore logic would remove: **{review}**\n\n"
        "The corrected restore script removes only exact URL duplicates from other categories. "
        "This report is diagnostic; it does not mutate the playlist.\n",
        encoding="utf-8",
    )
    print(f"Protected identity collision audit: records={len(rows)} active_at_risk={active} review_urls_at_risk={review}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
