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
RUNNER = ROOT / "scripts" / "run_generate_epg.py"
MAPPING_AUGMENT = ROOT / "scripts" / "augment_epg_mapping_from_additional_sources.py"
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
    runner_urls = assignment(RUNNER, "ADDITIONAL_SOURCES")
    discovery_urls = assignment(MAPPING_AUGMENT, "SOURCES")
    if len(urls) != len(set(urls)):
        raise ValueError("Duplicate URLs in scripts/generate_epg.py SOURCES")
    required = set(urls)
    required.update(runner_urls)
    required.update(discovery_urls)
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
    normalized_scope = scope.casefold()
    positive_permission = any(
        word in normalized_scope
        for word in ("permitted", "allowed", "authorized", "authorised", "granted", "licensed", "licenced")
    )
    affirmative_scope = "public" in normalized_scope and "redistribut" in normalized_scope and positive_permission
    negative_scope = any(
        word in normalized_scope
        for word in ("not confirmed", "not established", "unconfirmed", "not permitted", "prohibited", "personal use only", "no redistribution")
    )
    if not affirmative_scope or negative_scope:
        errors.append(
            f"{key}: APPROVED requires evidence of explicit permission for public redistribution"
        )
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


def require_approved_sources(context="EPG source access"):
    """Check source policy; permit an explicit owner override for review-required feeds."""
    errors = policy_errors()
    if not errors:
        print(f"{context}: PASS — every active source has documented redistribution permission.")
        return True

    if os.environ.get("EPG_ALLOW_UNVERIFIED_SOURCES", "").strip().lower() == "true":
        try:
            required = required_source_keys()
            records = read_register()
        except (OSError, ValueError, SyntaxError) as exc:
            print(f"{context}: BLOCKED — source register/configuration error: {exc}")
            raise SystemExit(1)
        prohibited = [
            key for key in sorted(required)
            if records.get(key, {}).get("status", "").upper() == "PROHIBITED"
        ]
        if prohibited:
            print(f"{context}: BLOCKED — explicitly prohibited source(s) are active.")
            for key in prohibited:
                print("- " + key)
            raise SystemExit(1)
        print(
            f"{context}: WARNING — continuing under EPG_ALLOW_UNVERIFIED_SOURCES=true; "
            f"{len(errors)} source-rights review item(s) remain open."
        )
        print(
            "EPG.PW sources remain excluded. Review epg/source-rights-register.csv; "
            "the override is not a claim that upstream permissions have been verified."
        )
        return True

    print(f"{context}: BLOCKED by source-rights policy ({len(errors)} issue(s))")
    for error in errors:
        print("- " + error)
    print("Set EPG_ALLOW_UNVERIFIED_SOURCES=true only when the repository owner explicitly chooses to publish review-required, non-prohibited sources.")
    raise SystemExit(1)


def main():
    try:
        require_approved_sources("EPG source-rights audit")
    except SystemExit as exc:
        return int(exc.code or 1)
    return 0


if __name__ == "__main__":
    sys.exit(main())
