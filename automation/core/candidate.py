"""Read-only candidate comparison; this module never publishes or mutates playlists."""
from __future__ import annotations
import hashlib
from pathlib import Path
from automation.core.playlist_contract import parse_rows, assert_iptv_existing_rows_preserved

SUPPORTED = {"IPTV-Playlist.m3u", "International-Playlist.m3u"}

def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

def validate_candidate(playlist: str, baseline_path: str | Path, candidate_path: str | Path) -> dict:
    """Validate a temporary candidate against an immutable baseline.

    Validation is not publication authorization. This function has no write,
    git, network, or production credentials and always reports publish=false.
    """
    if playlist not in SUPPORTED:
        raise ValueError(f"Unsupported playlist target: {playlist}")
    baseline = Path(baseline_path).resolve()
    candidate = Path(candidate_path).resolve()
    if baseline == candidate:
        raise ValueError("Candidate must be a separate file; baseline cannot be overwritten")
    if not baseline.is_file() or not candidate.is_file():
        raise FileNotFoundError("Both baseline and candidate files must exist")
    before_text = baseline.read_text(encoding="utf-8-sig")
    after_text = candidate.read_text(encoding="utf-8-sig")
    before_rows, after_rows = parse_rows(before_text), parse_rows(after_text)
    if playlist == "IPTV-Playlist.m3u":
        assert_iptv_existing_rows_preserved(before_text, after_text)
    before_urls = [row.url for row in before_rows]
    after_urls = [row.url for row in after_rows]
    return {
        "schema_version": 1,
        "playlist": playlist,
        "baseline_sha256": sha256(baseline),
        "candidate_sha256": sha256(candidate),
        "baseline_rows": len(before_rows),
        "candidate_rows": len(after_rows),
        "added_url_occurrences": max(0, len(after_urls) - len(before_urls)),
        "removed_url_occurrences": max(0, len(before_urls) - len(after_urls)),
        "invariants": "PASS",
        "publish": False
    }
