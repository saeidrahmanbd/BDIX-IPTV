#!/usr/bin/env python3
"""Safety helpers for the IPTV maintenance workflow.

The maintenance workflow is intentionally conservative:
- existing stream URLs are protected;
- Backup/Not Playing entries are protected byte-for-byte;
- stream-health failures are advisory only;
- removals are reported and blocked unless they are provable exact-URL duplicates;
- metadata repair is allowed when the underlying stream URL survives.
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

PLAYLIST = Path("IPTV-Playlist.m3u")
BASELINE = Path("/tmp/iptv-playlist-baseline.json")
PROTECTED_SNAPSHOT = Path("/tmp/iptv-protected-review.m3u")
REMOVAL_REPORT = Path("reports/proposed-removals.md")
PROTECTED_GROUPS = {"Backup", "Not Playing"}

BAD_LOGOS = {
    'atn-news.png','a-sports-5485adff.png','a-sports-hd.png','bein-sports-3.png',
    'bangla-tv.png','btv-news.png','colors.png','duronto-tv.png',
    'duronto-tv-1ad55c95.png','ekushey-tv.png','global-tv.png','green-tv.png',
    'mohona-tv.png','nagorik-tv.png','nagorik.png','nick-bangla.png',
    'sananda-tv.png','sananda.png','star-gold-select.png','star-gold.png',
    'star-plus.png','zee-tv.png','tom-and-jerry.png','arirang-tv.png',
}


def _attrs(ext: str) -> dict[str, str]:
    return dict(re.findall(r'([A-Za-z0-9_-]+)="([^"]*)"', ext))


def _parse(text: str) -> list[tuple[str, str]]:
    lines = text.replace("\r", "").splitlines()
    result: list[tuple[str, str]] = []
    current = None
    for line in lines:
        if line.startswith("#EXTINF:"):
            if current is not None:
                result.append((current, ""))
            current = line
            continue
        if current is None:
            continue
        s = line.strip()
        if s.startswith(("http://", "https://")):
            result.append((current, s))
            current = None
        elif not s or s.startswith("#"):
            continue
        else:
            result.append((current, ""))
            current = None
    if current is not None:
        result.append((current, ""))
    return result


def _stable(info: str, url: str) -> str:
    """Preservation identity is the exact stream URL, not metadata.

    This deliberately permits tvg-id, channel name, logo, country and group
    metadata to be repaired while requiring the existing stream URL to survive.
    """
    return url.strip().casefold()


def _group(info: str) -> str:
    return _attrs(info).get("group-title", "").strip()


def _protected_text(entries: list[tuple[str, str]]) -> str:
    return "\n".join(
        info + "\n" + url
        for info, url in entries
        if _group(info) in PROTECTED_GROUPS
    ) + "\n"


def snapshot_protected() -> None:
    entries = _parse(PLAYLIST.read_text(encoding="utf-8-sig"))
    PROTECTED_SNAPSHOT.write_text(_protected_text(entries), encoding="utf-8")
    count = sum(_group(i) in PROTECTED_GROUPS for i, _ in entries)
    print(f"Protected review snapshot: {count} entries")


def snapshot_playlist() -> None:
    """Save the complete pre-maintenance stream-URL inventory."""
    entries = _parse(PLAYLIST.read_text(encoding="utf-8-sig"))
    baseline = []
    for info, url in entries:
        a = _attrs(info)
        baseline.append({
            "info": info,
            "url": url,
            "group": _group(info),
            "stable": _stable(info, url),
            "name": a.get("tvg-name", "") or info.rsplit(",", 1)[-1].strip(),
        })
    BASELINE.write_text(json.dumps(baseline, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Playlist safety baseline: {len(baseline)} entries")


def _write_removal_report(removals: list[dict], duplicate_allowed: list[dict]) -> None:
    REMOVAL_REPORT.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Proposed Playlist Removals",
        "",
        "This report is generated before publication. Existing entries are never silently deleted.",
        "",
        f"- Proposed removals: **{len(removals)}**",
        f"- Exact-URL duplicate removals potentially allowed: **{len(duplicate_allowed)}**",
        f"- Non-duplicate removals blocked: **{len(removals) - len(duplicate_allowed)}**",
        "",
    ]
    if removals:
        lines += ["## Entries proposed for removal", ""]
        for item in removals:
            lines.append(
                f"- `{item['name']}` — group=`{item['group']}` — reason=`{item['reason']}` — URL=`{item['url']}`"
            )
    else:
        lines += ["No existing entries were removed.", ""]
    REMOVAL_REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def verify_no_unauthorized_removals() -> int:
    """Block publication if maintenance removed existing stream URLs."""
    if not BASELINE.exists():
        print("ERROR: playlist safety baseline is missing", file=sys.stderr)
        return 2

    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    current = _parse(PLAYLIST.read_text(encoding="utf-8-sig"))
    baseline_counts = Counter(item["stable"] for item in baseline)
    current_counts = Counter(_stable(info, url) for info, url in current)
    baseline_url_counts = baseline_counts
    current_url_counts = current_counts

    removals: list[dict] = []
    duplicate_allowed: list[dict] = []
    for item in baseline:
        url = item["stable"]
        if not url or baseline_counts[url] <= current_counts[url]:
            continue
        missing = baseline_counts[url] - current_counts[url]
        for _ in range(missing):
            removals.append({
                "name": item["name"],
                "group": item["group"],
                "url": item["url"],
                "reason": "existing stream URL disappeared or changed",
            })

    remaining_blocked = []
    for item in removals:
        url = item["url"].strip().casefold()
        if (
            item["group"] not in PROTECTED_GROUPS
            and url
            and baseline_url_counts[url] > current_url_counts[url]
            and baseline_url_counts[url] > 1
            and current_url_counts[url] >= 1
        ):
            item["reason"] = "exact duplicate stream URL; one duplicate may be removed"
            duplicate_allowed.append(item)
        else:
            remaining_blocked.append(item)

    _write_removal_report(removals, duplicate_allowed)

    protected_removed = [x for x in removals if x["group"] in PROTECTED_GROUPS]
    allowed_duplicate_limit = 10
    if protected_removed:
        print(f"Change Guard BLOCKED: {len(protected_removed)} Backup/Not Playing entries would be removed.", file=sys.stderr)
        return 1
    if remaining_blocked:
        print(f"Change Guard BLOCKED: {len(remaining_blocked)} non-duplicate existing stream URLs would be removed.", file=sys.stderr)
        return 1
    if len(duplicate_allowed) > allowed_duplicate_limit:
        print(
            f"Change Guard BLOCKED: {len(duplicate_allowed)} exact-URL duplicates exceed the {allowed_duplicate_limit}-entry safety limit.",
            file=sys.stderr,
        )
        return 1

    current_protected = _protected_text(current)
    expected_protected = PROTECTED_SNAPSHOT.read_text(encoding="utf-8") if PROTECTED_SNAPSHOT.exists() else ""
    if current_protected != expected_protected:
        REMOVAL_REPORT.write_text(
            REMOVAL_REPORT.read_text(encoding="utf-8")
            + "\n**BLOCKED:** Backup/Not Playing content changed byte-for-byte.\n",
            encoding="utf-8",
        )
        print("Change Guard BLOCKED: Backup/Not Playing is not byte-for-byte identical.", file=sys.stderr)
        return 1

    print(
        f"Change Guard passed: {len(removals)} existing stream URLs proposed; "
        f"{len(duplicate_allowed)} are exact-URL duplicates and {len(remaining_blocked)} are unauthorized removals."
    )
    return 0


def invalidate_bad_logos(message: str) -> None:
    p = PLAYLIST
    lines = p.read_text(encoding="utf-8-sig").replace("\r", "").splitlines()
    out = []
    changed = 0
    for line in lines:
        if line.startswith("#EXTINF:"):
            m = re.search(r'tvg-logo="([^"]*)"', line)
            if m:
                logo = Path(m.group(1).split("?", 1)[0].split("#", 1)[0]).name.casefold()
                if logo in BAD_LOGOS:
                    line = line[:m.start(1)] + line[m.end(1):]
                    changed += 1
        out.append(line)
    p.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")
    print(f"{message}: {changed}")


def main() -> int:
    if len(sys.argv) != 2:
        print(
            "Usage: maintenance_helpers.py snapshot|snapshot-playlist|verify-no-unauthorized-removals|invalidate-bad-logos|invalidate-bad-logos-correction",
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
