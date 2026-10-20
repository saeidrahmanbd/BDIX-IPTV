#!/usr/bin/env python3
"""Conservative safety helpers for IPTV playlist maintenance.

Policy:
- Existing stream URLs are never automatically deleted.
- Backup and Not Playing entries are immutable during maintenance.
- Stream-health failures are advisory only.
- Metadata repair may change names/IDs/groups/logos, but an existing stream URL
  must survive.
- Exact duplicate URLs are detected and reported, never automatically deleted.
- Every proposed removal is written to reports/proposed-removals.md.
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

from logo_asset_naming import is_blocked_logo_basename

PLAYLIST = Path("IPTV-Playlist.m3u")
BASELINE = Path("/tmp/iptv-playlist-baseline.json")
PROTECTED_SNAPSHOT = Path("/tmp/iptv-protected-review.m3u")
REMOVAL_REPORT = Path("reports/proposed-removals.md")
PROTECTED_GROUPS = {"Backup", "Not Playing"}

def _attrs(ext: str) -> dict[str, str]:
    return dict(re.findall(r'([A-Za-z0-9_-]+)="([^"]*)"', ext))


def _parse_blocks(text: str) -> list[dict[str, object]]:
    """Parse complete EXTINF blocks without discarding intervening directives."""
    lines = text.replace("\r", "").splitlines()
    blocks: list[dict[str, object]] = []
    current: list[str] | None = None
    current_url: str | None = None

    def finish() -> None:
        nonlocal current, current_url
        if current is None:
            return
        blocks.append({
            "lines": list(current),
            "info": current[0],
            "url": current_url or "",
        })
        current = None
        current_url = None

    for line in lines:
        if line.startswith("#EXTINF:"):
            finish()
            current = [line]
            continue

        if current is None:
            continue

        current.append(line)
        stripped = line.strip()
        if stripped.startswith(("http://", "https://")):
            current_url = stripped
            finish()

    finish()
    return blocks


def _parse(text: str) -> list[tuple[str, str]]:
    """Compatibility representation used by existing callers."""
    return [
        (str(block["info"]), str(block["url"]))
        for block in _parse_blocks(text)
    ]


def _stable(info: str, url: str) -> str:
    """Use the stream URL as preservation identity, not mutable metadata."""
    return url.strip().casefold()


def _group(info: str) -> str:
    return _attrs(info).get("group-title", "").strip()


def _name(info: str) -> str:
    a = _attrs(info)
    return (a.get("tvg-name", "") or info.rsplit(",", 1)[-1]).strip()


def _protected_blocks(text: str) -> list[dict[str, object]]:
    return [
        block
        for block in _parse_blocks(text)
        if _group(str(block["info"])) in PROTECTED_GROUPS
    ]


def _protected_text(text: str) -> str:
    """Return protected blocks exactly as they appeared, preserving directives."""
    blocks = _protected_blocks(text)
    if not blocks:
        return ""
    return "\n".join(
        "\n".join(str(line) for line in block["lines"])
        for block in blocks
    ) + "\n"


def snapshot_protected() -> None:
    text = PLAYLIST.read_text(encoding="utf-8-sig")
    PROTECTED_SNAPSHOT.write_text(_protected_text(text), encoding="utf-8")
    print(f"Protected review snapshot: {len(_protected_blocks(text))} complete entries")


def snapshot_playlist() -> None:
    """Save the complete pre-maintenance stream URL inventory."""
    text = PLAYLIST.read_text(encoding="utf-8-sig")
    baseline: list[dict[str, str]] = []

    for block in _parse_blocks(text):
        info = str(block["info"])
        url = str(block["url"])
        baseline.append({
            "info": info,
            "url": url,
            "group": _group(info),
            "stable": _stable(info, url),
            "name": _name(info),
        })

    BASELINE.write_text(
        json.dumps(baseline, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Playlist safety baseline: {len(baseline)} complete entries")


def _write_removal_report(removals: list[dict[str, str]]) -> None:
    REMOVAL_REPORT.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        "# Proposed Playlist Removals",
        "",
        "This report is generated before publication.",
        "Existing entries are never automatically deleted by this guard.",
        "",
        f"- Proposed removals: **{len(removals)}**",
        f"- Automatic deletions authorized: **0**",
        "",
    ]

    if removals:
        lines += ["## Entries proposed for removal", ""]
        for item in removals:
            lines.append(
                f"- `{item['name']}` — group=`{item['group']}` — "
                f"reason=`{item['reason']}` — URL=`{item['url']}`"
            )
    else:
        lines += ["No existing stream URLs disappeared.", ""]

    REMOVAL_REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def verify_no_unauthorized_removals() -> int:
    """Block publication whenever an existing stream URL disappears."""
    if not BASELINE.exists():
        print("ERROR: playlist safety baseline is missing", file=sys.stderr)
        return 2

    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    current_text = PLAYLIST.read_text(encoding="utf-8-sig")
    current = _parse_blocks(current_text)

    baseline_counts = Counter(str(item["stable"]) for item in baseline if item["stable"])
    current_counts = Counter(
        _stable(str(block["info"]), str(block["url"]))
        for block in current
        if str(block["url"]).strip()
    )

    removals: list[dict[str, str]] = []

    for item in baseline:
        stable = str(item["stable"])
        if not stable:
            continue

        missing = baseline_counts[stable] - current_counts[stable]
        for _ in range(max(0, missing)):
            removals.append({
                "name": str(item["name"]),
                "group": str(item["group"]),
                "url": str(item["url"]),
                "reason": "existing stream URL disappeared or changed",
            })

    _write_removal_report(removals)

    if removals:
        protected_removed = [
            item for item in removals
            if item["group"] in PROTECTED_GROUPS
        ]
        duplicate_urls = Counter(
            str(item["url"]).strip().casefold()
            for item in baseline
            if str(item["url"]).strip()
        )
        current_urls = Counter(
            _stable(str(block["info"]), str(block["url"]))
            for block in current
            if str(block["url"]).strip()
        )
        duplicate_candidates = [
            item for item in removals
            if duplicate_urls[item["url"].strip().casefold()] > 1
            and current_urls[item["url"].strip().casefold()] >= 1
            and item["group"] not in PROTECTED_GROUPS
        ]

        if protected_removed:
            print(
                f"Change Guard BLOCKED: {len(protected_removed)} "
                "Backup/Not Playing entries would be removed.",
                file=sys.stderr,
            )
        else:
            print(
                f"Change Guard BLOCKED: {len(removals)} existing stream URLs "
                "would be removed. No automatic deletion is authorized.",
                file=sys.stderr,
            )

        print(
            f"Diagnostic: {len(duplicate_candidates)} proposed removals are "
            "exact-URL duplicate candidates; they are report-only.",
            file=sys.stderr,
        )
        return 1

    current_protected = _protected_text(current_text)
    expected_protected = (
        PROTECTED_SNAPSHOT.read_text(encoding="utf-8")
        if PROTECTED_SNAPSHOT.exists()
        else ""
    )

    if current_protected != expected_protected:
        with REMOVAL_REPORT.open("a", encoding="utf-8") as handle:
            handle.write(
                "\n**BLOCKED:** Backup/Not Playing content changed "
                "byte-for-byte.\n"
            )
        print(
            "Change Guard BLOCKED: Backup/Not Playing content is not "
            "byte-for-byte identical to the maintenance snapshot.",
            file=sys.stderr,
        )
        return 1

    print(
        "Change Guard passed: no existing stream URL disappeared; "
        "Backup/Not Playing content is unchanged."
    )
    return 0


def invalidate_bad_logos(message: str) -> None:
    """Remove only known-bad logo references; never touch stream URLs."""
    p = PLAYLIST
    lines = p.read_text(encoding="utf-8-sig").replace("\r", "").splitlines()
    out: list[str] = []
    changed = 0

    for line in lines:
        if line.startswith("#EXTINF:"):
            match = re.search(r'tvg-logo="([^"]*)"', line)
            if match:
                logo = Path(
                    match.group(1).split("?", 1)[0].split("#", 1)[0]
                ).name.casefold()
                if is_blocked_logo_basename(logo):
                    line = line[:match.start(1)] + line[match.end(1):]
                    changed += 1
        out.append(line)

    p.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")
    print(f"{message}: {changed}")


def main() -> int:
    if len(sys.argv) != 2:
        print(
            "Usage: maintenance_helpers.py "
            "snapshot|snapshot-playlist|verify-no-unauthorized-removals|"
            "invalidate-bad-logos|invalidate-bad-logos-correction",
            file=sys.stderr,
        )
        return 2

    command = sys.argv[1]

    if command == "snapshot":
        snapshot_protected()
        return 0
    if command == "snapshot-playlist":
        snapshot_playlist()
        return 0
    if command == "verify-no-unauthorized-removals":
        return verify_no_unauthorized_removals()
    if command == "invalidate-bad-logos":
        invalidate_bad_logos("Known-bad local logo references invalidated")
        return 0
    if command == "invalidate-bad-logos-correction":
        invalidate_bad_logos("Known-bad references invalidated on correction pass")
        return 0

    print(f"Unknown command: {command}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
