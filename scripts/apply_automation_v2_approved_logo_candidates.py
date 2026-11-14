#!/usr/bin/env python3
"""Apply only explicit, hash-pinned logo approvals to isolated playlist candidates.

This tool never writes production playlists or changes logo assets. Each approval
must bind a specific playlist EXTINF line and channel name to an existing local
asset whose SHA-256 is pinned in the approval manifest.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

PLAYLISTS = ("IPTV-Playlist.m3u", "International-Playlist.m3u")
ATTR_RE = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
LOGO_RE = re.compile(r'(?<![A-Za-z0-9_-])tvg-logo="[^"]*"')


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _safe_logo(root: Path, relative: str, expected_sha: str) -> Path:
    if not isinstance(relative, str) or not relative.startswith("logos/"):
        raise ValueError("approved logo must be a repository-local logos/ path")
    candidate = root / relative
    if candidate.is_symlink():
        raise ValueError("approved logo cannot be a symlink")
    resolved_root = (root / "logos").resolve()
    resolved = candidate.resolve()
    if not resolved.is_relative_to(resolved_root) or not resolved.is_file():
        raise ValueError("approved logo must resolve to an existing file under logos/")
    if not re.fullmatch(r"[0-9a-f]{64}", str(expected_sha)):
        raise ValueError("approved logo requires a lowercase SHA-256 pin")
    if _sha256(resolved) != expected_sha:
        raise ValueError("approved logo SHA-256 does not match the manifest")
    return resolved


def _apply_one(lines: list[str], approval: dict, playlist: str) -> None:
    if approval.get("playlist") != playlist:
        return
    line_number = approval.get("line")
    if not isinstance(line_number, int) or isinstance(line_number, bool) or not 1 <= line_number <= len(lines):
        raise ValueError(f"{playlist}: approval line number is invalid")
    index = line_number - 1
    extinf = lines[index]
    if not extinf.startswith("#EXTINF:"):
        raise ValueError(f"{playlist}:{line_number}: target is not an EXTINF row")
    attrs = dict(ATTR_RE.findall(extinf))
    channel_name = (attrs.get("tvg-name") or extinf.rsplit(",", 1)[-1]).strip()
    if channel_name != approval.get("channel_name"):
        raise ValueError(f"{playlist}:{line_number}: channel identity changed since approval")
    current_logo = attrs.get("tvg-logo", "")
    if current_logo != approval.get("expected_current_logo", ""):
        raise ValueError(f"{playlist}:{line_number}: current logo changed since approval")
    new_logo = approval["approved_local_logo"]
    if LOGO_RE.search(extinf):
        lines[index] = LOGO_RE.sub(lambda _: f'tvg-logo="{new_logo}"', extinf, count=1)
    else:
        # Add the new attribute immediately after the EXTINF duration token.
        match = re.match(r"(#EXTINF:[^ ]+)(.*)", extinf)
        if not match:
            raise ValueError(f"{playlist}:{line_number}: cannot safely insert tvg-logo")
        lines[index] = match.group(1) + f' tvg-logo="{new_logo}"' + match.group(2)


def build_candidates(root: Path, manifest_path: Path, output_dir: Path) -> dict:
    root = root.resolve()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if not isinstance(manifest, dict) or manifest.get("schema_version") != 1:
        raise ValueError("approved logo manifest schema is unsupported")
    approvals = manifest.get("approvals")
    if not isinstance(approvals, list):
        raise ValueError("approved logo manifest must contain an approvals array")
    seen = set()
    validated = []
    for item in approvals:
        if not isinstance(item, dict):
            raise ValueError("each logo approval must be an object")
        playlist = item.get("playlist")
        if playlist not in PLAYLISTS:
            raise ValueError("approval references a playlist outside the V2 allowlist")
        key = (playlist, item.get("line"))
        if key in seen:
            raise ValueError("duplicate logo approval for the same playlist line")
        seen.add(key)
        asset = _safe_logo(root, item.get("approved_local_logo"), item.get("asset_sha256"))
        validated.append((item, asset))
    output_dir = output_dir.resolve()
    if output_dir == root or not output_dir.is_relative_to(root):
        raise ValueError("candidate output directory must be inside the repository and not its root")
    output_dir.mkdir(parents=True, exist_ok=True)
    results = []
    for playlist in PLAYLISTS:
        source = root / playlist
        if not source.is_file() or source.is_symlink():
            continue
        original = source.read_text(encoding="utf-8-sig")
        lines = original.splitlines()
        before = hashlib.sha256(original.encode("utf-8")).hexdigest()
        selected = [item for item, _ in validated if item["playlist"] == playlist]
        for item in selected:
            _apply_one(lines, item, playlist)
        candidate = "\n".join(lines) + ("\n" if original.endswith("\n") else "")
        changed = candidate != original
        if changed:
            destination = output_dir / playlist
            destination.write_text(candidate, encoding="utf-8")
            results.append({
                "playlist": playlist, "approved_rows": len(selected),
                "baseline_sha256": before,
                "candidate_sha256": hashlib.sha256(candidate.encode("utf-8")).hexdigest(),
                "candidate_path": destination.relative_to(root).as_posix(),
            })
    return {
        "schema_version": 1,
        "report_type": "automation-v2-approved-logo-candidate-playlists",
        "approved_mappings": len(validated),
        "changed_playlists": results,
        "safety": {
            "production_playlists_modified": False,
            "logo_assets_modified": False,
            "publication_performed": False,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--manifest", type=Path, default=Path("config/automation-v2/approved-logo-repairs.json"))
    parser.add_argument("--output-dir", type=Path, default=Path("reports/automation-v2/logo-repair-candidate-playlists"))
    parser.add_argument("--report", type=Path, default=Path("reports/automation-v2/approved-logo-candidate-playlists.json"))
    args = parser.parse_args()
    root = args.root.resolve()
    manifest = args.manifest if args.manifest.is_absolute() else root / args.manifest
    output = args.output_dir if args.output_dir.is_absolute() else root / args.output_dir
    report_path = args.report if args.report.is_absolute() else root / args.report
    result = build_candidates(root, manifest, output)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
