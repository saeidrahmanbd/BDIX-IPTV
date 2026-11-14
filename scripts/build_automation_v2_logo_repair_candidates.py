#!/usr/bin/env python3
"""Generate conservative, review-only logo repair proposals from existing local assets.

No playlist or image is changed. A proposal is emitted only when the normalized
channel name exactly matches one unique local asset stem. Similarity guesses,
remote URLs, provenance claims and ambiguous matches are never auto-selected.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urlsplit

IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg"}
ATTR_RE = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
PLAYLISTS = ("IPTV-Playlist.m3u", "International-Playlist.m3u")
REVIEW_GROUPS = {"backup", "review", "new channels", "new backups", "test", "not playing"}


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", str(value or "").casefold())


def _asset_inventory(root: Path) -> dict[str, list[str]]:
    inventory: dict[str, list[str]] = {}
    logos = root / "logos"
    if not logos.is_dir():
        return inventory
    for path in sorted(logos.rglob("*")):
        if path.is_file() and path.suffix.lower() in IMAGE_SUFFIXES:
            key = normalize(path.stem)
            if key:
                inventory.setdefault(key, []).append(path.relative_to(root).as_posix())
    return inventory


def build_proposals(root: Path) -> dict:
    inventory = _asset_inventory(root)
    proposals = []
    counts = {"rows_scanned": 0, "active_rows": 0, "already_local": 0,
              "missing_logo": 0, "missing_local_target": 0, "unique_exact_match": 0,
              "ambiguous_exact_match": 0, "no_exact_match": 0}
    playlist_hashes = {}

    for playlist_name in PLAYLISTS:
        playlist = root / playlist_name
        if not playlist.is_file():
            continue
        playlist_hashes[playlist_name] = hashlib.sha256(playlist.read_bytes()).hexdigest()
        current = None
        for line_number, line in enumerate(playlist.read_text(encoding="utf-8-sig").splitlines(), 1):
            if line.startswith("#EXTINF:"):
                current = (line_number, line)
                continue
            if current is None or not line.strip().startswith(("http://", "https://")):
                continue
            extinf_line, extinf = current
            current = None
            counts["rows_scanned"] += 1
            meta = dict(ATTR_RE.findall(extinf))
            group = meta.get("group-title", "").strip().casefold()
            if group in REVIEW_GROUPS:
                continue
            counts["active_rows"] += 1
            name = (meta.get("tvg-name") or extinf.rsplit(",", 1)[-1]).strip()
            logo = meta.get("tvg-logo", "").strip()
            filename = Path(urlsplit(logo).path).name if logo else ""
            target = (root / "logos" / filename) if filename else None
            if target and target.is_file():
                counts["already_local"] += 1
                continue
            if not logo:
                counts["missing_logo"] += 1
            else:
                counts["missing_local_target"] += 1
            matches = inventory.get(normalize(name), [])
            if len(matches) == 1:
                counts["unique_exact_match"] += 1
                proposals.append({"playlist": playlist_name, "line": extinf_line,
                                  "channel_name": name, "current_logo": logo,
                                  "proposed_local_logo": matches[0],
                                  "match_rule": "unique exact normalized channel-name/asset-stem match",
                                  "decision": "owner_review_required"})
            elif len(matches) > 1:
                counts["ambiguous_exact_match"] += 1
                proposals.append({"playlist": playlist_name, "line": extinf_line,
                                  "channel_name": name, "current_logo": logo,
                                  "candidate_local_logos": matches,
                                  "match_rule": "exact normalized match has multiple assets",
                                  "decision": "ambiguous_no_change"})
            else:
                counts["no_exact_match"] += 1

    return {
        "schema_version": 1,
        "report_type": "automation-v2-logo-repair-candidates",
        "source_playlist_sha256": playlist_hashes,
        "counts": counts,
        "proposals": proposals,
        "safety": {
            "playlist_modified": False, "logo_assets_modified": False,
            "assets_downloaded": False, "provenance_asserted": False,
            "automatic_assignment_performed": False, "deletion_performed": False,
        },
        "limitations": [
            "Only unique exact normalized channel-name/asset-stem matches are proposed.",
            "A filename match does not establish broadcaster authenticity or provenance.",
            "Dynamic logo references and remote assets are not resolved.",
            "All proposals require owner review; no playlist or asset is changed.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path, default=Path("reports/automation-v2/logo-repair-candidates.json"))
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.output if args.output.is_absolute() else root / args.output
    report = build_proposals(root)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
