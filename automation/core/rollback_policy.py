"""Fail-closed policy for preparing owner-reviewed Automation V2 rollback PRs."""
from __future__ import annotations

from dataclasses import dataclass

ALLOWED_PRODUCTION_PATHS = frozenset({
    "IPTV-Playlist.m3u",
    "International-Playlist.m3u",
    "epg/epg.xml",
})
PUBLICATION_PR_TITLE_PREFIX = "Review Automation V2 production candidates:"
PUBLICATION_BRANCH_PREFIX = "automation-v2/publish-"


@dataclass(frozen=True)
class RollbackTarget:
    pull_request_number: int
    merge_commit_sha: str
    changed_paths: tuple[str, ...]


def validate_publication_pr(payload: dict, pull_request_number: int) -> RollbackTarget:
    """Accept only a merged Automation V2 candidate PR with allowlisted output files."""
    if not isinstance(payload, dict):
        raise ValueError("publication PR metadata must be an object")
    if payload.get("state") != "CLOSED" or not payload.get("mergedAt"):
        raise ValueError("source publication PR must be merged and closed")
    if payload.get("baseRefName") != "main":
        raise ValueError("source publication PR must target main")
    title = payload.get("title")
    if not isinstance(title, str) or not title.startswith(PUBLICATION_PR_TITLE_PREFIX):
        raise ValueError("source PR is not an Automation V2 candidate publication")
    head = payload.get("headRefName")
    if not isinstance(head, str) or not head.startswith(PUBLICATION_BRANCH_PREFIX):
        raise ValueError("source PR does not come from an Automation V2 publication branch")
    merge_commit = payload.get("mergeCommit")
    sha = merge_commit.get("oid") if isinstance(merge_commit, dict) else None
    if not isinstance(sha, str) or len(sha) not in (40, 64) or any(
        char not in "0123456789abcdefABCDEF" for char in sha
    ):
        raise ValueError("source publication PR has no valid merge commit")
    raw_files = payload.get("files")
    if not isinstance(raw_files, list) or not raw_files:
        raise ValueError("source publication PR has no changed-file list")
    paths = []
    for item in raw_files:
        path = item.get("path") if isinstance(item, dict) else None
        if not isinstance(path, str) or not path:
            raise ValueError("source publication PR contains an invalid changed-file entry")
        paths.append(path)
    if len(set(paths)) != len(paths):
        raise ValueError("source publication PR contains duplicate changed paths")
    unexpected = set(paths) - ALLOWED_PRODUCTION_PATHS
    if unexpected:
        raise ValueError(f"source publication PR contains non-production or unapproved paths: {sorted(unexpected)}")
    return RollbackTarget(pull_request_number, sha.lower(), tuple(sorted(paths)))
