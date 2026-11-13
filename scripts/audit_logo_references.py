"""Conservative repository-wide logo reference scanner. Never deletes or modifies assets."""
from __future__ import annotations
import argparse, json, re
from pathlib import Path

IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg"}
TEXT_SUFFIXES = {".py", ".yml", ".yaml", ".json", ".md", ".txt", ".m3u", ".xml", ".html", ".js", ".css", ".toml", ".ini", ".sh"}
LOGO_REF = re.compile(r'(?:https?://[^\s"\']+?/)?(logos/[A-Za-z0-9_./@+-]+\.(?:png|jpe?g|webp|gif|svg))', re.I)

def scan(root: Path) -> dict:
    logo_root = root / "logos"
    assets = sorted(p.relative_to(root).as_posix() for p in logo_root.rglob("*") if p.is_file() and p.suffix.lower() in IMAGE_SUFFIXES)
    references: dict[str, set[str]] = {}
    for path in root.rglob("*"):
        if not path.is_file() or "logos" in path.relative_to(root).parts:
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
    return {
        "schema_version": 1,
        "scan_scope": "repository text files with explicit logos/<filename> references; binary data and dynamically constructed names may be missed",
        "logo_image_files": len(assets),
        "explicitly_referenced_logo_files": len(referenced),
        "apparently_unreferenced_logo_files": len(asset_set - set(referenced)),
        "missing_explicit_logo_targets": missing,
        "referenced": {key: sorted(references[key]) for key in sorted(references) if key in asset_set},
        "apparently_unreferenced": sorted(asset_set - set(referenced)),
        "deletion_performed": False,
    }

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = scan(args.root.resolve())
    rendered = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    print(f"Logo reference audit: {result['logo_image_files']} assets; {result['explicitly_referenced_logo_files']} explicit refs; {result['apparently_unreferenced_logo_files']} candidates; no deletion", flush=True)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
