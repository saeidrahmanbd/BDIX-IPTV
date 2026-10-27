#!/usr/bin/env python3
"""Fail closed unless every EPG data source has documented public redistribution rights.

This checks XMLTV feeds, HTML schedule sites, the supplemental source repository,
and the optional private feed configured in GitHub Actions. It never prints secrets.
"""
import ast
import csv
import os
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GENERATOR = ROOT / "scripts" / "generate_epg.py"
SUPPLEMENT = ROOT / "scripts" / "fetch_iptv_org_epg.py"
REGISTER = ROOT / "epg" / "source-rights-register.csv"
REPOSITORY_KEY = "repository:https://github.com/iptv-org/epg"
PRIVATE_KEY = "secret:M3U4U_XMLTV_URL"


def assignment(path, name):
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name for target in node.targets
        ):
            return ast.literal_eval(node.value)
    raise ValueError(f"Cannot read literal {name} from {path.relative_to(ROOT)}")


def required_source_keys(env=None):
    env = os.environ if env is None else env
    urls = assignment(GENERATOR, "SOURCES")
    site_names = assignment(SUPPLEMENT, "SITES")
    if len(urls) != len(set(urls)):
        raise ValueError("Duplicate URLs in scripts/generate_epg.py SOURCES")
    required = set(urls)
    required.update("site:" + domain for domain in site_names)
    required.add(REPOSITORY_KEY)
    # The URL itself must never be emitted in diagnostics; only the secret key is recorded.
    if str(env.get("M3U4U_XMLTV_URL", "")).strip():
        required.add(PRIVATE_KEY)
    return required


def read_register(path=REGISTER):
    if not path.exists():
        raise ValueError(f"Rights register is missing: {path.relative_to(ROOT)}")
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        needed = {"source_key", "source_type", "status", "evidence_url", "reviewed_on", "rights_scope", "notes"}
        if not needed.issubset(reader.fieldnames or []):
            raise ValueError("Rights register is missing required columns")
        records = {}
        duplicates = set()
        for row in reader:
            key = (row.get("source_key") or "").strip()
            if not key:
                continue
            if key in records:
                duplicates.add(key)
            records[key] = {k: (v or "").strip() for k, v in row.items()}
    if duplicates:
        raise ValueError("Duplicate rights-register keys: " + ", ".join(sorted(duplicates)))
    return records


def approved_row_errors(key, row):
    errors = []
    evidence = row.get("evidence_url", "")
    reviewed = row.get("reviewed_on", "")
    scope = row.get("rights_scope", "")
    if not evidence.startswith("https://"):
        errors.append(f"{key}: APPROVED requires an HTTPS evidence URL")
    try:
        date.fromisoformat(reviewed)
    except ValueError:
        errors.append(f"{key}: APPROVED requires reviewed_on in YYYY-MM-DD format")
    if not scope or any(word in scope.casefold() for word in ("not confirmed", "not established", "unconfirmed")):
        errors.append(f"{key}: APPROVED requires an explicit, affirmative redistribution scope")
    return errors


def policy_errors(env=None, registry_path=REGISTER):
    try:
        required = required_source_keys(env)
        records = read_register(registry_path)
    except (OSError, ValueError, SyntaxError) as exc:
        return ["Configuration error: " + str(exc)]
    errors = []
    for key in sorted(required):
        row = records.get(key)
        if row is None:
            errors.append(f"Missing rights-register entry: {key}")
            continue
        status = row.get("status", "").upper()
        if status != "APPROVED":
            errors.append(f"Not approved for public redistribution ({status or 'NO STATUS'}): {key}")
        else:
            errors.extend(approved_row_errors(key, row))
    return errors


def main():
    errors = policy_errors()
    if errors:
        print("EPG source-rights gate: BLOCKED")
        for error in errors:
            print("- " + error)
        print("Resolve the source rights, then set EPG_REDISTRIBUTION_APPROVED=true deliberately.")
        return 1
    print("EPG source-rights gate: PASS — every active source has documented permission.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
