"""Strict candidate manifest checks. This module has no Git or publication side effects."""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import PurePosixPath

PLAYLIST_ALLOWLIST = {
    "iptv": {"IPTV-Playlist.m3u"},
    "international": {"International-Playlist.m3u"},
    "epg": {"epg/epg.xml"},
}
COMMON_REPORTS = {"reports/automation-v2/run-report.json"}

@dataclass(frozen=True)
class CandidateManifest:
    engine: str
    baseline_commit: str
    changed_paths: tuple[str, ...]
    candidate_fingerprints: dict[str, str]

def validate_manifest(manifest: CandidateManifest) -> list[str]:
    errors: list[str] = []
    if manifest.engine not in PLAYLIST_ALLOWLIST:
        errors.append("unknown engine")
        return errors
    if not manifest.baseline_commit or len(manifest.baseline_commit) not in (40, 64):
        errors.append("baseline commit must be a full Git object identifier")
    if not manifest.changed_paths:
        errors.append("candidate manifest has no declared changed paths")
    allowed = PLAYLIST_ALLOWLIST[manifest.engine] | COMMON_REPORTS
    for raw in manifest.changed_paths:
        path = PurePosixPath(raw)
        if path.is_absolute() or ".." in path.parts or raw not in allowed:
            errors.append(f"path outside engine allowlist: {raw}")
    if len(set(manifest.changed_paths)) != len(manifest.changed_paths):
        errors.append("duplicate changed path")
    for path in manifest.changed_paths:
        fingerprint = manifest.candidate_fingerprints.get(path, "")
        if len(fingerprint) != 64 or any(c not in "0123456789abcdef" for c in fingerprint.lower()):
            errors.append(f"missing or invalid SHA-256 fingerprint: {path}")
    return errors
