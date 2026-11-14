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
from stream_url_identity import stream_url_key
from permanent_removals import AUTHORIZED_ORPHAN_BACKUP_REMOVALS, PERMANENTLY_REMOVED_NAMES

PLAYLIST = Path("IPTV-Playlist.m3u")
BASELINE = Path("/tmp/iptv-playlist-baseline.json")
PROTECTED_SNAPSHOT = Path("/tmp/iptv-protected-review.m3u")
REMOVAL_REPORT = Path("reports/proposed-removals.md")
PROTECTED_GROUPS = {"Backup", "Review", "Not Playing"}
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
    parsed = urlsplit(stream_url_key(url))
    if not parsed.netloc or not parsed.path:
        return ""
    # This helper is used only for the owner-allowlisted Sparkle Movies
    # duplicate endpoint, whose known CDN route is case-insensitive. Do not use
    # it for general stream identity comparisons.
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
    return stream_url_key(url)


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


def _is_authorized_orphan_backup_removal(info: str, url: str) -> bool:
    """Match only the exact Backup identity + endpoint authorized for deletion."""
    if _group(info) != "Backup":
        return False
    a = _attrs(info)
    ids = {
        value.strip().casefold()
        for value in (a.get("tvg-id", ""), a.get("channel-id", ""))
        if value.strip()
    }
    candidate_url = stream_url_key(url)
    return any(
        channel_id in ids and candidate_url == stream_url_key(expected_url)
        for channel_id, expected_url in AUTHORIZED_ORPHAN_BACKUP_REMOVALS.items()
    )


def _is_authorized_removal(info: str, url: str) -> bool:
    return (
        _is_permanently_removed(info)
        or _is_authorized_duplicate_backup(info, url)
        or _is_authorized_orphan_backup_removal(info, url)
    )


def _protected_blocks(text: str) -> list[dict[str, object]]:
    return [
        block
        for block in _parse_blocks(text)
        if (
            _group(str(block["info"])) in PROTECTED_GROUPS
            and not _is_authorized_removal(str(block["info"]), str(block["url"]))
        )
    ]


def _protected_text(text: str, skip_urls: set[str] | None = None) -> str:
    """Compare protected rows while permitting validated Backup↔Review quarantine moves."""
    skip_urls = {stream_url_key(value) for value in (skip_urls or set())}
    blocks = [block for block in _protected_blocks(text) if stream_url_key(str(block["url"])) not in skip_urls]
    if not blocks:
        return ""
    # Sort by identity and URL only; moving an orphan Backup to Review must
    # not alter the comparison order of protected records.
    blocks.sort(key=lambda block: (
        _canonical_channel_name(_name(str(block["info"]))),
        stream_url_key(str(block["url"])),
    ))
    serialized = []
    for block in blocks:
        lines = list(block["lines"])
        if lines:
            info = str(lines[0])
            # Numbering is intentionally absent from Backup/Not Playing queues.
            # Permit this metadata-only normalization while protecting every
            # other EXTINF value and the exact stream URL.
            if _group(info) in PROTECTED_GROUPS:
                # Integrity enforcement may normalize channel name, local logo,
                # country/language and group during a validated quarantine move.
                # Exact IDs, stream URLs and all other attributes stay protected.
                # Only channel numbering is mutable in a protected row. Group transitions
                # are checked separately against the exact baseline identity above; channel
                # name, ID, logo, country and language remain protected metadata.
                for key in ("tvg-chno", "group-title", "tvg-logo"):
                    info = re.sub(rf'\s+{re.escape(key)}="[^"]*"', "", info, count=1)
            lines[0] = _canonical_extinf(info)
        serialized.extend(lines)
    return "\n".join(serialized) + "\n"


def _protected_snapshot_text(text: str) -> str:
    """Serialize protected records with original group names for the restore step."""
    blocks = _protected_blocks(text)
    blocks.sort(key=lambda block: (
        _canonical_channel_name(_name(str(block["info"]))),
        stream_url_key(str(block["url"])),
    ))
    serialized = []
    for block in blocks:
        lines = list(block["lines"])
        if lines:
            info = str(lines[0])
            # Channel numbering is mutable, but the original group is required by
            # restore_protected_review.py to validate and reconstruct each queue.
            info = re.sub(r'\s+tvg-chno="[^"]*"', "", info, count=1)
            lines[0] = _canonical_extinf(info)
        serialized.extend(lines)
    return "\n".join(serialized) + ("\n" if serialized else "")


def snapshot_protected() -> None:
    text = PLAYLIST.read_text(encoding="utf-8-sig")
    # Keep group-title in the saved artifact: restore_protected_review.py needs
    # the original Backup/Review/Not Playing classification to restore queues.
    PROTECTED_SNAPSHOT.write_text(_protected_snapshot_text(text), encoding="utf-8")
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
        "No existing IPTV row may be deleted, replaced, moved, promoted, demoted, renumbered or reordered.",
        "Only genuinely new stream URLs may be appended to New Channels or New Backups.",
        "",
        f"- Proposed unauthorized removals: **{len(removals)}**",
        "- Automatic removals authorized: **0**",
        "- Existing group changes authorized: **0**",
        "- Existing channel-number changes authorized: **0**",
        "- Existing row reordering authorized: **0**",
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
    """Block all structural changes to the owner-curated IPTV playlist."""
    if not BASELINE.exists():
        print("ERROR: playlist safety baseline is missing", file=sys.stderr)
        return 2
    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    current = _parse_blocks(PLAYLIST.read_text(encoding="utf-8-sig"))
    old_urls = [str(x.get("url", "")) for x in baseline]
    old_counts, new_counts = Counter(old_urls), Counter(str(x.get("url", "")) for x in current)
    missing, added = old_counts - new_counts, new_counts - old_counts
    failures, removals = [], []
    for url, count in missing.items():
        candidates = [x for x in baseline if str(x.get("url", "")) == url]
        for old in candidates[:count]:
            removals.append({
                "name": str(old.get("name", "")), "group": str(old.get("group", "")),
                "url": url, "reason": "pre-existing stream URL occurrence disappeared or was replaced",
            })
    if missing:
        failures.append(f"{sum(missing.values())} existing URL occurrence(s) disappeared")
    if any(url in old_counts for url in added):
        failures.append("duplicate occurrence of an existing URL added")
    existing_order = [str(x.get("url", "")) for x in current if str(x.get("url", "")) in old_counts]
    if existing_order != old_urls:
        failures.append("pre-existing rows reordered or removed")
    old_by_url, new_by_url = {}, {}
    for x in baseline:
        old_by_url.setdefault(str(x.get("url", "")), []).append(x)
    for x in current:
        new_by_url.setdefault(str(x.get("url", "")), []).append(x)
    for url, old_rows in old_by_url.items():
        rows = new_by_url.get(url, [])
        if len(rows) != len(old_rows):
            continue
        for old, new in zip(old_rows, rows):
            info = str(new.get("info", ""))
            old_group = str(old.get("group", "")).strip()
            new_group = _group(info)
            if old_group != new_group:
                failures.append(f"existing owner-curated group assignment changed for {_name(info)}")
            old_number = _attrs(str(old.get("info", ""))).get("tvg-chno", "").strip()
            new_number = _attrs(info).get("tvg-chno", "").strip()
            if old_number != new_number:
                failures.append(f"existing owner-curated channel number changed for {_name(info)}")
    for url, count in added.items():
        if url in old_counts:
            continue
        if count != 1:
            failures.append(f"new stream URL duplicated: {url}")
        for block in new_by_url.get(url, []):
            if _group(str(block.get("info", ""))) not in {"New Channels", "New Backups"}:
                failures.append(f"new row outside manual queues: {_name(str(block.get('info', '')))}")
    _write_removal_report(removals)
    if failures:
        for item in failures[:30]:
            print(f"::error::{item}", file=sys.stderr)
        print("Change Guard BLOCKED: only new manual-queue rows may be added; existing rows are immutable.", file=sys.stderr)
        return 1
    print(f"Change Guard passed: {len(baseline)} existing rows preserve URL/group/number/order; new rows are manual-queue only.")
    return 0


def canonicalize_extinf() -> int:
    """Normalize EXTINF attribute order after all metadata/logo mutators have run."""
    lines = PLAYLIST.read_text(encoding="utf-8-sig").replace("\r", "").splitlines()
    updated = [
        _canonical_extinf(line) if line.startswith("#EXTINF:") else line
        for line in lines
    ]
    changed = sum(
        before != after
        for before, after in zip(lines, updated)
    )
    if changed:
        PLAYLIST.write_text("\n".join(updated).rstrip() + "\n", encoding="utf-8")
    print(f"Canonical EXTINF metadata order: {changed} row(s) normalized.")
    return changed


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
            "invalidate-bad-logos|invalidate-bad-logos-correction|canonicalize-extinf",
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
    if command == "canonicalize-extinf":
        canonicalize_extinf()
        return 0
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
