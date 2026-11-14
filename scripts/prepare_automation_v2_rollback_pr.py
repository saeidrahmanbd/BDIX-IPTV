#!/usr/bin/env python3
"""Prepare a rollback commit on a disposable branch; never push or merge it."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from automation.core.rollback_policy import validate_publication_pr


def git(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=root, check=True, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    return result.stdout.strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pr-json", required=True)
    parser.add_argument("--repo-root", default=str(ROOT))
    parser.add_argument("--report", required=True)
    args = parser.parse_args()

    root = Path(args.repo_root).resolve()
    payload = json.loads(Path(args.pr_json).read_text(encoding="utf-8"))
    number = payload.get("number")
    if not isinstance(number, int) or number < 1:
        raise ValueError("source PR number is invalid")
    target = validate_publication_pr(payload, number)

    head = git(root, "rev-parse", "HEAD")
    ancestor = subprocess.run(
        ["git", "merge-base", "--is-ancestor", target.merge_commit_sha, head],
        cwd=root, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    if ancestor.returncode != 0:
        raise ValueError("source publication merge commit is not an ancestor of current main")

    parents = git(root, "show", "-s", "--format=%P", target.merge_commit_sha).split()
    if len(parents) not in (1, 2):
        raise ValueError("source publication commit has an unsupported parent count")
    if git(root, "status", "--porcelain"):
        raise ValueError("rollback worktree must be clean before reverting")

    if len(parents) == 2:
        git(root, "revert", "--no-edit", "-m", "1", target.merge_commit_sha)
        revert_mode = "merge-mainline-parent-1"
    else:
        git(root, "revert", "--no-edit", target.merge_commit_sha)
        revert_mode = "single-commit"

    reverted_paths = tuple(sorted(filter(None, git(
        root, "diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD^", "HEAD"
    ).splitlines())))
    if reverted_paths != target.changed_paths:
        raise ValueError(
            "rollback commit path set does not exactly match the approved publication PR: "
            f"expected {target.changed_paths}, got {reverted_paths}"
        )
    if git(root, "status", "--porcelain"):
        raise ValueError("rollback worktree is not clean after revert commit")

    report = {
        "schema_version": 1,
        "source_publication_pr": number,
        "source_merge_commit": target.merge_commit_sha,
        "rollback_commit": git(root, "rev-parse", "HEAD"),
        "revert_mode": revert_mode,
        "changed_paths": list(reverted_paths),
        "main_modified": False,
        "force_push": False,
        "auto_merge": False,
        "owner_review_required": True,
    }
    Path(args.report).write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
