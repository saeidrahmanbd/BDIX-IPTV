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

def _is_hex(value: str, length: int) -> bool:
    return len(value) == length and all(char in "0123456789abcdefABCDEF" for char in value)

def validate_manifest(manifest: CandidateManifest) -> list[str]:
    errors: list[str] = []
    if manifest.engine not in PLAYLIST_ALLOWLIST:
        errors.append("unknown engine")
        return errors
    if not (_is_hex(manifest.baseline_commit,40) or _is_hex(manifest.baseline_commit,64)):
        errors.append("baseline commit must be a full hexadecimal Git object identifier")
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
        if not _is_hex(fingerprint,64):
            errors.append(f"missing or invalid SHA-256 fingerprint: {path}")
    return errors
