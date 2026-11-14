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
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg"}
CANDIDATE_ROOT = Path("reports/automation-v2")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _reject_symlink_components(path: Path, stop: Path) -> None:
    """Reject symlinks in path from stop (inclusive) through the leaf."""
    path = path.absolute()
    stop = stop.absolute()
    try:
        relative = path.relative_to(stop)
    except ValueError as exc:
        raise ValueError("path is outside its approved root") from exc
    current = stop
    if current.is_symlink():
        raise ValueError("approved root cannot be a symlink")
    for part in relative.parts:
        current = current / part
        if current.is_symlink():
            raise ValueError(f"symlink path component is not allowed: {current}")


def _safe_logo(root: Path, relative: str, expected_sha: str) -> Path:
    if not isinstance(relative, str) or not relative.startswith("logos/"):
        raise ValueError("approved logo must be a repository-local logos/ path")
    rel = Path(relative)
    if rel.is_absolute() or "\\" in relative or ".." in rel.parts or len(rel.parts) < 2:
        raise ValueError("approved logo path is unsafe")
    logo_root = root / "logos"
    if logo_root.is_symlink() or not logo_root.is_dir():
        raise ValueError("logos root must be a real repository directory")
    candidate = root / rel
    _reject_symlink_components(candidate, logo_root)
    try:
        resolved_root = logo_root.resolve(strict=True)
        resolved = candidate.resolve(strict=True)
    except OSError as exc:
        raise ValueError("approved logo must resolve to an existing file under logos/") from exc
    if not resolved.is_relative_to(resolved_root) or not resolved.is_file():
        raise ValueError("approved logo must resolve to an existing file under logos/")
    if resolved.suffix.lower() not in IMAGE_SUFFIXES:
        raise ValueError("approved logo must use a supported image extension")
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
        match = re.match(r"(#EXTINF:[^ ]+)(.*)", extinf)
        if not match:
            raise ValueError(f"{playlist}:{line_number}: cannot safely insert tvg-logo")
        lines[index] = match.group(1) + f' tvg-logo="{new_logo}"' + match.group(2)


def _safe_candidate_dir(root: Path, output_dir: Path) -> Path:
    root = root.resolve(strict=True)
    output = output_dir if output_dir.is_absolute() else root / output_dir
    output = output.absolute()
    allowed = (root / CANDIDATE_ROOT).absolute()
    try:
        relative = output.relative_to(allowed)
    except ValueError as exc:
        raise ValueError("candidate output must be inside reports/automation-v2/") from exc
    _reject_symlink_components(output, root)
    if output == allowed:
        raise ValueError("candidate output must use a dedicated subdirectory")
    # Reject an existing non-directory at any output component.
    current = allowed
    for part in relative.parts:
        current = current / part
        if current.exists() and not current.is_dir():
            raise ValueError("candidate output path contains a non-directory")
    return output


def build_candidates(root: Path, manifest_path: Path, output_dir: Path) -> dict:
    root = root.resolve(strict=True)
    if (root / "logos").is_symlink():
        raise ValueError("logos root must not be a symlink")
    manifest_path = manifest_path if manifest_path.is_absolute() else root / manifest_path
    if manifest_path.is_symlink() or not manifest_path.is_file():
        raise ValueError("approved logo manifest must be a regular file")
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
        if not isinstance(item.get("channel_name"), str) or not item["channel_name"].strip():
            raise ValueError("approval requires an exact non-empty channel_name")
        if not isinstance(item.get("expected_current_logo", ""), str):
            raise ValueError("approval expected_current_logo must be text")
        asset = _safe_logo(root, item.get("approved_local_logo"), item.get("asset_sha256"))
        validated.append((item, asset))
    output_dir = _safe_candidate_dir(root, output_dir)
    source_hashes = manifest.get("source_playlist_sha256")
    if not isinstance(source_hashes, dict):
        raise ValueError("approved logo manifest must pin source_playlist_sha256 for each playlist")
    results = []
    for playlist in PLAYLISTS:
        source = root / playlist
        selected = [item for item, _ in validated if item["playlist"] == playlist]
        if not source.is_file() or source.is_symlink():
            if selected:
                raise ValueError(f"approved source playlist is missing or unsafe: {playlist}")
            continue
        original_bytes = source.read_bytes()
        has_utf8_bom = original_bytes.startswith(b"\xef\\xbb\\xbf")
        original = original_bytes.decode("utf-8-sig")
        actual_source_sha = _sha256(source)
        if selected and source_hashes.get(playlist) != actual_source_sha:
            raise ValueError(f"{playlist}: source playlist SHA-256 changed since approval")
        lines = original.splitlines()
        for item in selected:
            _apply_one(lines, item, playlist)
        candidate = "\n".join(lines) + ("\n" if original.endswith("\n") else "")
        changed = candidate != original
        if changed:
            destination = output_dir / playlist
            destination.parent.mkdir(parents=True, exist_ok=True)
            candidate_bytes = (b"\xef\\xbb\\xbf" if has_utf8_bom else b"") + candidate.encode("utf-8")
            destination.write_bytes(candidate_bytes)
            results.append({
                "playlist": playlist, "approved_rows": len(selected),
                "baseline_sha256": actual_source_sha,
                "candidate_sha256": hashlib.sha256(candidate_bytes).hexdigest(),
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
            "output_scope": CANDIDATE_ROOT.as_posix() + "/",
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
    report_path = report_path.absolute()
    allowed_report_root = (root / CANDIDATE_ROOT).absolute()
    try:
        report_path.relative_to(allowed_report_root)
    except ValueError as exc:
        raise ValueError("candidate report must remain inside reports/automation-v2/") from exc
    _reject_symlink_components(report_path, root)
    if report_path in {(root / "IPTV-Playlist.m3u").absolute(),
                       (root / "International-Playlist.m3u").absolute()}:
        raise ValueError("candidate report cannot overwrite a production playlist")
    result = build_candidates(root, manifest, output)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
