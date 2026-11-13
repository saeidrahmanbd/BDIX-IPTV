"""Conservative repository-wide logo reference and exact-duplicate scanner; never modifies assets."""
from __future__ import annotations
import argparse, hashlib, json, re
from collections import defaultdict
from pathlib import Path

IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg"}
TEXT_SUFFIXES = {".py", ".yml", ".yaml", ".json", ".md", ".txt", ".m3u", ".xml", ".html", ".js", ".css", ".toml", ".ini", ".sh"}
EXCLUDED_REFERENCE_FILES = {"docs/automation-v2/baseline-tree-manifest.json", "docs/automation-v2/logo-reference-baseline.json"}
LOGO_REF = re.compile(r'(?:https?://[^\s"\']+?/)?(logos/[A-Za-z0-9_./@+-]+\.(?:png|jpe?g|webp|gif|svg))', re.I)

def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

def scan(root: Path) -> dict:
    logo_root = root / "logos"
    asset_paths = sorted(p for p in logo_root.rglob("*") if p.is_file() and p.suffix.lower() in IMAGE_SUFFIXES)
    assets = [p.relative_to(root).as_posix() for p in asset_paths]
    references: dict[str, set[str]] = {}
    for path in root.rglob("*"):
        relative = path.relative_to(root).as_posix()
        if not path.is_file() or "logos" in path.relative_to(root).parts or relative in EXCLUDED_REFERENCE_FILES:
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for match in LOGO_REF.finditer(content):
            target = match.group(1)
            references.setdefault(target, set()).add(path.relative_to(root).as_posix())
    asset_set = set(assets)
    referenced = sorted(asset_set.intersection(references))
    missing = sorted(target for target in references if target.startswith("logos/") and target not in asset_set)
    hashes: dict[str, list[str]] = defaultdict(list)
    for path in asset_paths:
        hashes[_sha256(path)].append(path.relative_to(root).as_posix())
    duplicate_groups = [
        {"sha256": digest, "files": sorted(paths)}
        for digest, paths in sorted(hashes.items()) if len(paths) > 1
    ]
    return {
        "schema_version": 2,
        "scan_scope": "explicit text-file logo references and exact byte-identical image hashes; binary data and dynamically constructed names may be missed",
        "logo_image_files": len(assets),
        "explicitly_referenced_logo_files": len(referenced),
        "apparently_unreferenced_logo_files": len(asset_set - set(referenced)),
        "missing_explicit_logo_targets": missing,
        "exact_duplicate_groups": len(duplicate_groups),
        "exact_duplicate_files": sum(len(group["files"]) - 1 for group in duplicate_groups),
        "exact_duplicates": duplicate_groups,
        "referenced": {key: sorted(references[key]) for key in sorted(references) if key in asset_set},
        "apparently_unreferenced": sorted(asset_set - set(referenced)),
        "deletion_performed": False,
        "quarantine_performed": False,
    }

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = scan(args.root.resolve())
    rendered = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    print(f"Logo audit: {result['logo_image_files']} assets; {result['explicitly_referenced_logo_files']} explicit refs; {result['apparently_unreferenced_logo_files']} apparent non-refs; {result['exact_duplicate_groups']} exact duplicate groups; no deletion or quarantine", flush=True)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
