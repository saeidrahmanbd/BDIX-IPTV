#!/usr/bin/env python3
"""Final logo-reference validation for both playlists.

This is the exact logic the logo localization workflow runs after repair,
conversion and manifest generation. It lives in a module (not workflow YAML) so
the regression tests exercise the same code that gates publication.

Both playlists are always validated and reported before the run fails, so one
playlist's failure cannot hide problems in the other.
"""
import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

import logo_provenance
import repair_playlist_logos as logo_repair

PLAYLISTS = ["IPTV-Playlist.m3u", "International-Playlist.m3u"]
BASE = "logos/"
REGISTRY_PATH = "reports/logo-source-registry.json"
REVIEW_GROUPS = {"review", "new channels", "new backups", "not playing"}
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
BLOCKED_PREFIXES = ("placeholder-", "generic-", "unknown-", "unidentified-")

EXPLICIT_BLOCKLIST = frozenset({
    "atn-news.png", "a-sports-5485adff.png", "a-sports-hd.png", "bein-sports-3.png",
    "bangla-tv.png", "btv-news.png", "colors.png", "duronto-tv.png",
    "duronto-tv-1ad55c95.png", "ekushey-tv.png", "global-tv.png", "green-tv.png",
    "mohona-tv.png", "nagorik-tv.png", "nagorik.png", "nick-bangla.png",
    "sananda-tv.png", "sananda.png", "star-gold-select.png", "star-gold.png",
    "star-plus.png", "zee-tv.png", "tom-and-jerry.png", "arirang-tv.png",
})


def normalize_newlines(text):
    return text.replace("\r\n", "\n").replace("\r", "\n")


def strip_logo_attributes(text):
    """Playlist text with every tvg-logo attribute removed (protected-content view)."""
    return re.sub(r'\s+tvg-logo="[^"]*"', "", normalize_newlines(text))


def blocked_filenames():
    return set(EXPLICIT_BLOCKLIST) | set(logo_repair.BAD_ASSETS) | set(logo_repair.GENERIC_ASSETS)


def has_png_signature(path):
    try:
        with open(path, "rb") as stream:
            return stream.read(len(PNG_SIGNATURE)) == PNG_SIGNATURE
    except OSError:
        return False


def validate_playlist(name, text, registry, root=Path("."), blocked=None):
    """Validate one playlist's logo references.

    Returns ``{"summary": {...}, "invalid": [diagnostic, ...]}``.
    """
    root = Path(root)
    blocked = blocked_filenames() if blocked is None else blocked
    current = normalize_newlines(text)
    entries = [line for line in current.splitlines() if line.startswith("#EXTINF:")]
    missing = review_missing = external = nvision = broken = adult_ignored = non_png = 0
    invalid = []

    for line in entries:
        meta = dict(re.findall(r'([\w-]+)="([^"]*)"', line))
        group = (meta.get("group-title") or "").strip().casefold()
        channel_id = (meta.get("tvg-id") or meta.get("channel-id") or "").strip().casefold()
        label = line.rsplit(",", 1)[-1].strip() if "," in line else (meta.get("tvg-name") or "").strip()
        if logo_repair.is_adult_playlist_entry(name, group, channel_id, logo_repair.norm_key(label)):
            adult_ignored += 1
            continue

        found = re.search(r'tvg-logo="([^"]*)"', line)
        logo = found.group(1).strip() if found else ""
        if not logo:
            if group in REVIEW_GROUPS:
                review_missing += 1
            else:
                missing += 1
            continue
        if not logo.startswith(BASE):
            external += 1
            continue

        rel = unquote(logo[len(BASE):].split("?", 1)[0].split("#", 1)[0]).lstrip("/")
        asset = root / "logos" / rel
        if asset.suffix.casefold() != ".png":
            non_png += 1
        filename = asset.name.casefold()
        if filename.startswith("nvisionbd-"):
            nvision += 1

        channel_name = line.rsplit(",", 1)[-1].strip()
        record, match = logo_provenance.resolve_provenance(
            registry, name, logo_provenance.entry_identity(meta), channel_name, logo
        )
        verdict = logo_provenance.classify_logo(record, match, logo)

        reasons = []
        if not asset.is_file():
            reasons.append("missing_asset_file")
        elif asset.suffix.casefold() == ".png" and not has_png_signature(asset):
            reasons.append("invalid_png_signature")
        if filename in blocked:
            reasons.append("explicit_blocklist")
        if filename.startswith(BLOCKED_PREFIXES):
            reasons.append("blocked_filename_prefix")
        if verdict["is_generated_fallback"]:
            reasons.extend(verdict["problems"])
        if re.search(r"(?:placeholder|generic-logo)", filename, re.I):
            reasons.append("placeholder_or_generic_filename")
        if reasons:
            broken += 1
            invalid.append({
                "playlist": name, "channel": channel_name,
                "tvg_id": (meta.get("tvg-id") or meta.get("channel-id") or "").strip(),
                "logo": logo, "filename": filename, "reasons": reasons,
                "asset_exists": asset.is_file(),
                "provenance_match": match,
                "provenance_status": record.get("status", ""),
                "provenance_notes": record.get("notes", ""),
                "is_generated_fallback": verdict["is_generated_fallback"],
                "fallback_is_disclosed": verdict["fallback_is_disclosed"],
            })

    summary = {
        "entries": len(entries), "missing_logo_metadata": missing,
        "review_missing_logo_metadata": review_missing,
        "adult_entries_ignored": adult_ignored,
        "nonrepository_logo_refs": external, "nvision_refs": nvision,
        "invalid_or_blocked_refs": broken, "non_png_refs": non_png,
    }
    return {"summary": summary, "invalid": invalid}


def summary_failed(summary):
    return bool(
        summary["nonrepository_logo_refs"] or summary["nvision_refs"]
        or summary["invalid_or_blocked_refs"] or summary["non_png_refs"]
    )


def load_registry(path):
    path = Path(path)
    return json.loads(path.read_text(encoding="utf-8")) if path.is_file() else {}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="repository root (default: current directory)")
    parser.add_argument("--registry", default=None, help="provenance registry (default: reports/logo-source-registry.json)")
    parser.add_argument(
        "--baseline-dir", default=None,
        help="directory holding <playlist>.nonlogo baselines; non-logo content must match them exactly",
    )
    args = parser.parse_args(argv)
    root = Path(args.root)
    registry = load_registry(args.registry or root / REGISTRY_PATH)
    blocked = blocked_filenames()

    summaries, failures = {}, []
    for name in PLAYLISTS:
        text = normalize_newlines((root / name).read_text(encoding="utf-8-sig"))
        if args.baseline_dir:
            baseline = (Path(args.baseline_dir) / (name + ".nonlogo")).read_text(encoding="utf-8")
            if strip_logo_attributes(text) != baseline:
                raise SystemExit("Non-logo playlist content changed: " + name)
        result = validate_playlist(name, text, registry, root=root, blocked=blocked)
        for item in result["invalid"]:
            print("INVALID_LOGO_REFERENCE " + json.dumps(item, ensure_ascii=False))
        summaries[name] = result["summary"]
        if name == PLAYLISTS[0] and result["summary"]["missing_logo_metadata"]:
            print("::warning::Authentic local logo unavailable for some main-playlist rows; "
                  "leaving those logo fields empty for manual review: " + json.dumps(result["summary"]))
        if summary_failed(result["summary"]):
            failures.append(name + " " + json.dumps(result["summary"]))

    print(json.dumps(summaries, indent=2))
    if failures:
        raise SystemExit("Logo validation failed: " + "; ".join(failures))
    return summaries


if __name__ == "__main__":
    main()
