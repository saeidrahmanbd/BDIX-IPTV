"""Build a conservative, non-destructive plan for exact duplicate logo cleanup.

Only same-named copies in logos/unused/ with a byte-identical root-level
logos/<name> counterpart are eligible for review as low-risk candidates.
Exact path mentions in playlists and runtime registries block candidacy; basename mentions in executable runtime code remain conservative blockers.
This tool never deletes, moves, renames, or rewrites logo assets.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from audit_logo_references import scan

RUNTIME_DIRS = ("scripts", "automation", ".github")
PLAYLISTS = ("IPTV-Playlist.m3u", "International-Playlist.m3u")
RUNTIME_REGISTRIES = (
    "reports/logo-source-registry.json",
    "reports/logo-authenticity-manifest.json",
)
TEXT_SUFFIXES = {
    ".py", ".yml", ".yaml", ".json", ".md", ".txt", ".m3u",
    ".xml", ".html", ".js", ".css", ".toml", ".ini", ".sh",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def runtime_text_files(root: Path):
    paths = set()
    for directory in RUNTIME_DIRS:
        base = root / directory
        if base.is_dir():
            paths.update(
                p for p in base.rglob("*")
                if p.is_file() and not p.is_symlink()
                and p.suffix.lower() in TEXT_SUFFIXES
            )
    paths.update(root / name for name in PLAYLISTS if (root / name).is_file())
    paths.update(root / name for name in RUNTIME_REGISTRIES if (root / name).is_file())
    return sorted(paths)


def build_plan(root: Path) -> dict:
    root = root.resolve()
    audit = scan(root)
    runtime_contents = []
    for path in runtime_text_files(root):
        try:
            runtime_contents.append(
                (path.relative_to(root).as_posix(), path.read_text(encoding="utf-8"))
            )
        except (UnicodeDecodeError, OSError):
            # An unreadable runtime input makes automated candidacy unsafe.
            runtime_contents.append((path.relative_to(root).as_posix(), None))

    candidates = []
    held = []
    for group in audit["exact_duplicates"]:
        files = group["files"]
        unused = [p for p in files if p.startswith("logos/unused/")]
        for candidate in unused:
            name = Path(candidate).name
            canonical = "logos/" + name
            reasons = []
            if canonical not in files:
                reasons.append("no same-named root-level byte-identical counterpart")
            if any(content is None for _, content in runtime_contents):
                reasons.append("one or more runtime text files could not be read")
            else:
                for source, content in runtime_contents:
                    if source in PLAYLISTS or source in RUNTIME_REGISTRIES:
                        # These files record concrete logo paths. A reference to
                        # logos/<name> uses the retained canonical file and must
                        # not falsely block removal of logos/unused/<name>.
                        referenced = candidate in content
                    else:
                        # Executable code may construct paths dynamically, so
                        # keep basename matches as a conservative safety block.
                        referenced = name in content or candidate in content
                    if referenced:
                        reasons.append(f"runtime basename/path mention in {source}")
            if reasons:
                held.append({
                    "candidate": candidate,
                    "sha256": group["sha256"],
                    "duplicate_group": files,
                    "reasons": sorted(set(reasons)),
                })
            else:
                candidates.append({
                    "candidate": candidate,
                    "retain": canonical,
                    "sha256": group["sha256"],
                    "reason": "same-named root-level exact-byte copy; no runtime basename/path mention found",
                    "requires_review": True,
                })

    return {
        "schema_version": 1,
        "policy": (
            "Planning only. No assets are deleted or moved. A candidate requires "
            "a same-named root-level exact-byte copy and no basename/path mention "
            "in scanned runtime text. Dynamic references may still exist."
        ),
        "exact_duplicate_groups": audit["exact_duplicate_groups"],
        "exact_duplicate_files": audit["exact_duplicate_files"],
        "low_risk_review_candidates": candidates,
        "held_for_review": held,
        "deletion_performed": False,
        "quarantine_performed": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = build_plan(args.root)
    rendered = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    print(
        "Duplicate-logo cleanup plan: "
        f"{result['exact_duplicate_groups']} clusters; "
        f"{len(result['low_risk_review_candidates'])} low-risk review candidates; "
        f"{len(result['held_for_review'])} held; no deletion",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
