#!/usr/bin/env python3
"""Fail early when EPG source lists or channel aliases drift or contain duplicates."""
import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COVERAGE = ROOT / "scripts" / "epg_coverage.py"
GENERATOR = ROOT / "scripts" / "generate_epg.py"


def assignments(path):
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    found = {}
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id in {"SOURCES", "EPG_ALIASES", "EPG_LOCKS"}:
                found[target.id] = node.value
    return found


def literal(node, label):
    try:
        return ast.literal_eval(node)
    except (ValueError, TypeError) as exc:
        raise SystemExit(f"ERROR: {label} must be a literal configuration: {exc}")


def duplicate_dict_keys(node, label):
    if not isinstance(node, ast.Dict):
        raise SystemExit(f"ERROR: {label} must be a dictionary literal")
    keys = [literal(k, label) for k in node.keys]
    duplicates = sorted({k for k in keys if keys.count(k) > 1})
    if duplicates:
        raise SystemExit(f"ERROR: duplicate {label} keys: {', '.join(map(str, duplicates))}")


def main():
    coverage = assignments(COVERAGE)
    generator = assignments(GENERATOR)
    for label, values in (("coverage", coverage), ("generator", generator)):
        if "SOURCES" not in values:
            raise SystemExit(f"ERROR: SOURCES is missing from {label} script")

    coverage_sources = literal(coverage["SOURCES"], "coverage SOURCES")
    generator_sources = literal(generator["SOURCES"], "generator SOURCES")
    if len(coverage_sources) != len(set(coverage_sources)):
        raise SystemExit("ERROR: duplicate URLs in epg_coverage.py SOURCES")
    if len(generator_sources) != len(set(generator_sources)):
        raise SystemExit("ERROR: duplicate URLs in generate_epg.py SOURCES")
    if coverage_sources != generator_sources:
        only_coverage = sorted(set(coverage_sources) - set(generator_sources))
        only_generator = sorted(set(generator_sources) - set(coverage_sources))
        raise SystemExit(
            "ERROR: EPG source lists differ. "
            f"Only coverage={only_coverage}; only generator={only_generator}"
        )

    for name in ("EPG_ALIASES", "EPG_LOCKS"):
        if name not in coverage:
            raise SystemExit(f"ERROR: {name} is missing from epg_coverage.py")
        duplicate_dict_keys(coverage[name], name)
        mapping = literal(coverage[name], name)
        for key, ids in mapping.items():
            if not isinstance(key, str) or not key.strip():
                raise SystemExit(f"ERROR: {name} contains an empty/non-string playlist ID")
            if not isinstance(ids, list) or not ids or any(not isinstance(x, str) or not x.strip() for x in ids):
                raise SystemExit(f"ERROR: {name}[{key!r}] must contain non-empty string IDs")

    print(
        "EPG configuration check passed: "
        f"{len(coverage_sources)} synchronized sources, "
        f"{len(literal(coverage['EPG_ALIASES'], 'EPG_ALIASES'))} unique aliases, "
        f"{len(literal(coverage['EPG_LOCKS'], 'EPG_LOCKS'))} unique locks."
    )


if __name__ == "__main__":
    main()
