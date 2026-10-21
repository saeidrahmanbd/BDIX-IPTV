#!/usr/bin/env python3
"""Conservative safety helpers for IPTV playlist maintenance.

Policy:
- A stream may disappear only when its exact normalized channel name is in the
  permanent-removal allowlist or it is the exact, independently verified duplicate
  Backup record listed below.
- Backup and Not Playing entries are protected except for those exact identities;
  URL-based authorization never applies to a different channel.
- EXTINF attribute reordering is normalized for comparison; values, URLs and the
  existence of unrelated records remain protected.
- Stream-health failures are advisory only.
- Every unauthorized removal is written to reports/proposed-removals.md.
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit

from logo_asset_naming import is_blocked_logo_basename

PLAYLIST = Path("IPTV-Playlist.m3u")
BASELINE = Path("/tmp/iptv-playlist-baseline.json")
PROTECTED_SNAPSHOT = Path("/tmp/iptv-protected-review.m3u")
REMOVAL_REPORT = Path("reports/proposed-removals.md")
PROTECTED_GROUPS = {"Backup", "Not Playing"}
PERMANENTLY_REMOVED_NAMES = {
    "AccuWeather",
    "America's Got Talent",
    "American Idol",
    "Baraza Music TV",
    "Oscar Movies Bhojpuri",
    "The Walking Dead Universe",
    "Popflix",
    "60 Days In",
    "Deadly Women",
    "Highway Thru Hell",
    "MINI",
    "Mundial",
    "TVC Arabic Kids",
    "Grace Network",
    "Joshua TV",
    "King TV",
    "Jeremiah TV",
    "CBN TV USA",
    "Dios Te Ve Kids",
    "ZB Bhakti",
}


def _canonical_channel_name(value: str) -> str:
    """Normalize display names for exact allowlist matching only."""
    value = unicodedata.normalize("NFKD", str(value or "")).casefold()
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    value = re.sub(
        r"\b(?:backup|hd|fhd|uhd|sd|4k|1080p|720p|576p|480p|360p)\b",
        " ",
        value,
    )
    return re.sub(r"[^a-z0-9]+", "", value)


_PERMANENTLY_REMOVED_KEYS = {
    _canonical_channel_name(name) for name in PERMANENTLY_REMOVED_NAMES
}
AUTHORIZED_DUPLICATE_BACKUPS = {
    (
        _canonical_channel_name("Sparkle Movies"),
        "61fc4f1a40a342daa23f92141853b7b4.mediatailor.us-east-1.amazonaws.com"
        "/v1/master/04fd913bb278d8775298c26fdca9d9841f37601f/"
        "samsung-gb_sparklemovies/playlist",
    ),
}


ATTRIBUTE_ORDER = (
    "tvg-id", "tvg-name", "tvg-logo", "tvg-chno",
    "channel-id", "tvg-country", "tvg-language", "group-title",
)


def _canonical_extinf(info: str) -> str:
    """Canonicalize attribute order while retaining every attribute value."""
    comma = -1
    quoted = False
    for index, char in enumerate(info):
        if char == '"':
            quoted = not quoted
        elif char == ',' and not quoted:
            comma = index
            break
    if comma < 0:
        return info
    head, display = info[:comma], info[comma:]
    duration = re.match(r"^#EXTINF:\S+", head)
    if not duration:
        return info
    pairs = list(re.finditer(r'([A-Za-z0-9_-]+)="([^"]*)"', head))
    if not pairs:
        return info
    rank = {key: index for index, key in enumerate(ATTRIBUTE_ORDER)}
    found = [(match.group(1), match.group(2), index) for index, match in enumerate(pairs)]
    found.sort(key=lambda item: (rank.get(item[0], len(rank)), item[2]))
    return duration.group(0) + " " + " ".join(
        f'{key}="{value}"' for key, value, _ in found
    ) + display


def _canonical_channel_url_base(url: str) -> str:
    """Normalize transport/query/manifest suffixes for exact feed comparison."""
    parsed = urlsplit(str(url or "").strip())
    if not parsed.netloc or not parsed.path:
        return ""
    path = parsed.path.casefold().rstrip("/")
    path = re.sub(r"\.(?:m3u8?|mpd)$", "", path, flags=re.IGNORECASE)
    return parsed.netloc.casefold() + path


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


def _is_permanently_removed(info: str) -> bool:
    return _canonical_channel_name(_name(info)) in _PERMANENTLY_REMOVED_KEYS


def _is_authorized_duplicate_backup(info: str, url: str) -> bool:
    if _group(info) != "Backup":
        return False
    key = (_canonical_channel_name(_name(info)), _canonical_channel_url_base(url))
    return bool(key[1]) and key in AUTHORIZED_DUPLICATE_BACKUPS


def _is_authorized_removal(info: str, url: str) -> bool:
    return _is_permanently_removed(info) or _is_authorized_duplicate_backup(info, url)


def _protected_blocks(text: str) -> list[dict[str, object]]:
    return [
        block
        for block in _parse_blocks(text)
        if (
            _group(str(block["info"])) in PROTECTED_GROUPS
            and not _is_authorized_removal(str(block["info"]), str(block["url"]))
        )
    ]


def _protected_text(text: str) -> str:
    """Compare protected records independent of harmless ordering/attribute normalization."""
    blocks = _protected_blocks(text)
    if not blocks:
        return ""
    category_rank = {"Backup": 0, "Not Playing": 1}
    blocks.sort(key=lambda block: (
        category_rank.get(_group(str(block["info"])), 99),
        _canonical_channel_name(_name(str(block["info"]))),
        str(block["url"]).casefold(),
    ))
    serialized = []
    for block in blocks:
        lines = list(block["lines"])
        if lines:
            lines[0] = _canonical_extinf(str(lines[0]))
        serialized.extend(lines)
    return "\n".join(serialized) + "\n"


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
        "Only exact normalized channel names in the permanent-removal allowlist and one exact query-only Sparkle Movies Backup duplicate are authorized removals.",
        "Every other existing stream is protected by this guard.",
        "",
        f"- Proposed unauthorized removals: **{len(removals)}**",
        f"- Exact-name permanent-removal allowlist entries: **{len(PERMANENTLY_REMOVED_NAMES)}**",
        "- Independently verified duplicate Backup records authorized: **1**",
        "- Other automatic deletions authorized: **0**",
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

    # Exclude only exact channel identities from the explicit allowlist. This is
    # deliberately name-based, not URL-based: an unrelated record sharing a URL
    # never inherits another channel's deletion authorization.
    baseline_guarded = [
        item for item in baseline
        if not _is_authorized_removal(str(item.get("info", "")), str(item.get("url", "")))
    ]
    current_guarded = [
        block for block in current
        if not _is_authorized_removal(str(block["info"]), str(block["url"]))
    ]
    baseline_counts = Counter(
        str(item["stable"]) for item in baseline_guarded if item.get("stable")
    )
    current_counts = Counter(
        _stable(str(block["info"]), str(block["url"]))
        for block in current_guarded
        if str(block["url"]).strip()
    )

    removals: list[dict[str, str]] = []
    remaining_current = current_counts.copy()

    # Consume URL occurrences one at a time; repeated baseline URLs must not
    # multiply the count of proposed removals.
    for item in baseline_guarded:
        stable = str(item.get("stable", ""))
        if not stable:
            continue
        if remaining_current[stable] > 0:
            remaining_current[stable] -= 1
            continue
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

    authorized_still_present = [
        str(block["info"]) for block in current
        if _is_authorized_removal(str(block["info"]), str(block["url"]))
    ]
    if authorized_still_present:
        names = sorted({_name(info) for info in authorized_still_present})
        print(
            "Change Guard BLOCKED: permanent-removal entries still present: "
            + ", ".join(names),
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
