#!/usr/bin/env python3
"""Inventory every file under logos/ and classify its repository references.

Read-only. It never deletes or rewrites logos. Outputs:
  reports/logo-inventory.md    orphan and duplicate report for maintainers
  reports/logo-inventory.json  machine-readable classification and content hashes

Classification of each file (a file can match several categories):
  playlist_active     referenced by an active entry in IPTV-Playlist.m3u or International-Playlist.m3u
  playlist_queue      referenced only by Backup, Review, Not Playing or New* entries
  docs_or_site        referenced by README, docs/, assets/ or a website page
  code_or_workflow    referenced by scripts/, tests/ or .github/
  generated_fallback  filename starts with generated-fallback-
  duplicate           content hash matches another file
  unreferenced        no reference from any tracked location

Exit status is 0 unless a playlist references a logo file that does not exist,
which is a blocking error.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(".")
LOGOS = ROOT / "logos"
RAW_PREFIX = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/"
QUEUE_GROUPS = {"Backup", "Review", "Not Playing", "New Channels", "New Backups"}
PLAYLISTS = {"IPTV-Playlist.m3u": "primary", "International-Playlist.m3u": "international"}
TEXT_SUFFIXES = {".md", ".html", ".htm", ".css", ".js", ".json", ".yml", ".yaml", ".py", ".toml", ".txt", ".svg", ".csv", ".xml"}
ATTR_RE = re.compile(r'([\w-]+)="([^"]*)"')
REPORT_MD = ROOT / "reports" / "logo-inventory.md"
REPORT_JSON = ROOT / "reports" / "logo-inventory.json"
LARGE_BYTES = 500_000


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def logo_name_from_url(url: str) -> str | None:
    if not url.startswith(RAW_PREFIX):
        return None
    relative = urlsplit(url).path.split("/logos/", 1)
    return relative[1] if len(relative) == 2 else None


def playlist_references() -> tuple[dict[str, set[str]], dict[str, set[str]], list[str]]:
    active: dict[str, set[str]] = defaultdict(set)
    queue: dict[str, set[str]] = defaultdict(set)
    missing_in_playlist: list[str] = []
    for name in PLAYLISTS:
        path = ROOT / name
        if not path.is_file():
            continue
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        for line in lines:
            if not line.startswith("#EXTINF"):
                continue
            attrs = dict(ATTR_RE.findall(line))
            logo = attrs.get("tvg-logo", "").strip()
            relative = logo_name_from_url(logo)
            if relative is None:
                continue
            group = attrs.get("group-title", "").strip()
            target = queue if group in QUEUE_GROUPS else active
            target[relative].add(name)
    return active, queue, missing_in_playlist


def text_references(files: list[Path], names: set[str]) -> dict[str, set[str]]:
    found: dict[str, set[str]] = defaultdict(set)
    for path in files:
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for name in names:
            if name in text:
                found[name].add(path.as_posix())
    return found


def build() -> dict:
    logo_files = sorted(p for p in LOGOS.rglob("*") if p.is_file())
    relatives = {p.relative_to(LOGOS).as_posix(): p for p in logo_files}
    names = set(relatives)

    active, queue, _ = playlist_references()
    docs_files = [p for p in ROOT.glob("*.md")] + list((ROOT / "docs").rglob("*")) + list((ROOT / "assets").rglob("*"))
    code_files = list((ROOT / "scripts").rglob("*.py")) + list((ROOT / "tests").rglob("*.py")) + list((ROOT / ".github").rglob("*.yml"))
    docs_hits = text_references(docs_files, names)
    code_hits = text_references(code_files, names)

    by_hash: dict[str, list[str]] = defaultdict(list)
    hashes = {}
    for rel, path in relatives.items():
        digest = sha256(path)
        hashes[rel] = digest
        by_hash[digest].append(rel)

    missing_refs = sorted((set(active) | set(queue)) - names)

    entries = []
    counts: dict[str, int] = defaultdict(int)
    for rel, path in relatives.items():
        categories = []
        if rel in active:
            categories.append("playlist_active")
        if rel in queue and rel not in active:
            categories.append("playlist_queue")
        if rel in docs_hits:
            categories.append("docs_or_site")
        if rel in code_hits:
            categories.append("code_or_workflow")
        if Path(rel).name.casefold().startswith("generated-fallback-"):
            categories.append("generated_fallback")
        if len(by_hash[hashes[rel]]) > 1:
            categories.append("duplicate")
        if not any(c in categories for c in ("playlist_active", "playlist_queue", "docs_or_site", "code_or_workflow")):
            categories.append("unreferenced")
        size = path.stat().st_size
        for category in categories:
            counts[category] += 1
        entries.append({
            "file": f"logos/{rel}",
            "bytes": size,
            "sha256": hashes[rel],
            "categories": categories,
            "playlists": sorted(active.get(rel, set()) | queue.get(rel, set())),
            "docs": sorted(docs_hits.get(rel, set())),
            "code": sorted(code_hits.get(rel, set())),
            "large": size >= LARGE_BYTES,
        })

    duplicate_groups = [sorted(f"logos/{x}" for x in members) for members in by_hash.values() if len(members) > 1]
    return {
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "inputs": {name: sha256(ROOT / name) for name in PLAYLISTS if (ROOT / name).is_file()},
        "total_files": len(logo_files),
        "total_bytes": sum(e["bytes"] for e in entries),
        "counts": dict(sorted(counts.items())),
        "referenced_but_missing": missing_refs,
        "duplicate_groups": duplicate_groups,
        "entries": entries,
    }


def render(data: dict) -> str:
    lines = [
        "# Logo Inventory",
        "",
        f"Generated: **{data['generated_at']}** (read-only; no logo was changed or deleted)",
        "",
        f"Files under `logos/`: **{data['total_files']}** ({data['total_bytes'] / 1_000_000:.1f} MB)",
        "",
        "## Classification",
        "",
        "A file can belong to several categories.",
        "",
        "| Category | Files |",
        "|---|---:|",
    ]
    for category, count in data["counts"].items():
        lines.append(f"| {category} | {count} |")
    lines += [
        "",
        "## Blocking: referenced but missing",
        "",
    ]
    if data["referenced_but_missing"]:
        lines += [f"- `logos/{name}`" for name in data["referenced_but_missing"]]
    else:
        lines.append("None. Every logo referenced by a playlist exists locally.")
    lines += ["", "## Duplicate content (identical SHA-256)", ""]
    if data["duplicate_groups"]:
        for group in data["duplicate_groups"]:
            lines.append("- " + ", ".join(f"`{x}`" for x in group))
    else:
        lines.append("None.")
    lines += [
        "",
        "## Unreferenced files",
        "",
        "These have no reference from a playlist, documentation, script, test or workflow.",
        "They are not deleted automatically. Review each one before removing it.",
        "",
    ]
    unreferenced = [e for e in data["entries"] if "unreferenced" in e["categories"]]
    if unreferenced:
        lines += ["| File | Bytes | Duplicate |", "|---|---:|---|"]
        for e in unreferenced:
            dup = "yes" if "duplicate" in e["categories"] else ""
            lines.append(f"| `{e['file']}` | {e['bytes']} | {dup} |")
    else:
        lines.append("None.")
    large = [e for e in data["entries"] if e["large"]]
    lines += ["", "## Large files (at least 500 KB)", ""]
    if large:
        lines += ["| File | Bytes |", "|---|---:|"]
        lines += [f"| `{e['file']}` | {e['bytes']} |" for e in sorted(large, key=lambda e: -e["bytes"])]
    else:
        lines.append("None.")
    lines += [
        "",
        "Per-file classifications, hashes and reference locations are in `reports/logo-inventory.json`.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="only fail on referenced-but-missing logos")
    args = parser.parse_args()
    data = build()
    if args.check:
        if data["referenced_but_missing"]:
            print("Referenced logo files missing:", ", ".join(data["referenced_but_missing"]), file=sys.stderr)
            return 1
        print(f"OK: all playlist-referenced logos exist ({data['total_files']} files scanned).")
        return 0
    REPORT_MD.write_text(render(data), encoding="utf-8")
    REPORT_JSON.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"total_files": data["total_files"], "counts": data["counts"], "missing": len(data["referenced_but_missing"])}, indent=2))
    return 1 if data["referenced_but_missing"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
