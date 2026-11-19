#!/usr/bin/env python3
"""Single source of truth for logo provenance records and classification.

Every component that records or judges logo provenance (the repair script, the
authenticity manifest generator and the final workflow validation) must go
through this module, so they cannot disagree about what a logo is.

Core rule: the *asset* decides its class. A generated fallback asset is always
``generated_fallback``; no registry record, source URL or third-party attribution
can promote it to a verified status.
"""
import json
import re
import urllib.parse
from pathlib import Path

FALLBACK_PREFIX = "generated-fallback-"
FALLBACK_STATUS = "generated_fallback"
VERIFIED_STATUSES = frozenset({"official_verified", "third_party_verified"})
RECORD_STATUSES = VERIFIED_STATUSES | {FALLBACK_STATUS}

# Both phrases must appear (case-insensitively) in every fallback record's notes.
DISCLOSURE_PHRASES = ("unofficial fallback", "not an official broadcaster logo")
FALLBACK_DISCLOSURE_NOTE = (
    "Unofficial fallback artwork generated after exact local and attributable "
    "online logo lookup failed; not an official broadcaster logo."
)

MATCH_EXACT = "exact-key"
MATCH_STEM = "same-asset-stem-format-conversion"
MATCH_AMBIGUOUS = "ambiguous"
MATCH_NONE = "none"

PROBLEM_UNMATCHED = "fallback_not_disclosed_or_provenance_unmatched"
PROBLEM_STATUS_CONFLICT = "fallback_registry_status_conflict"
PROBLEM_SOURCE_URL = "fallback_registry_carries_source_url"

# The converter adds this deterministic suffix only when a same-stem PNG already
# exists with different pixels; provenance still belongs to the same original
# source asset after format conversion.
_CONVERTED_SUFFIX = re.compile(r"-converted-[0-9a-f]{10}$")


def entry_identity(meta):
    """Registry identity of a playlist entry; matches the key the repair script writes."""
    return (meta.get("tvg-id") or meta.get("channel-id") or "").strip()


def logo_filename(logo):
    """Return the final, unquoted, case-folded filename of a logo reference."""
    path = str(logo or "").split("?", 1)[0].split("#", 1)[0]
    return urllib.parse.unquote(Path(path).name).casefold()


RAW_LOGO_BASE = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/"


def canonical_logo(logo):
    """Return the repository-relative form ``logos/<name>`` of a logo reference.

    Playlists carry absolute raw URLs, while older registry keys hold relative
    paths. Both name the same file, so provenance lookups must treat them alike.
    External references are returned unchanged.
    """
    value = str(logo or "").strip()
    if value.startswith(RAW_LOGO_BASE):
        rest = value[len(RAW_LOGO_BASE):]
    elif value.startswith("logos/"):
        rest = value[len("logos/"):]
    else:
        return value
    rest = urllib.parse.unquote(rest.split("?", 1)[0].split("#", 1)[0]).lstrip("/")
    return "logos/" + rest


def canonical_key(key):
    """Canonical registry key: the logo (the final ``|`` field) is canonicalised."""
    head, sep, logo = str(key).rpartition("|")
    if not sep:
        return key
    return head + sep + canonical_logo(logo)


def asset_stem(logo):
    """Return the case-folded filename stem without the converter's digest suffix."""
    return _CONVERTED_SUFFIX.sub("", Path(logo_filename(logo)).stem)


def is_generated_fallback_asset(logo):
    return logo_filename(logo).startswith(FALLBACK_PREFIX)


def notes_disclose_fallback(notes):
    folded = str(notes or "").casefold()
    return all(phrase in folded for phrase in DISCLOSURE_PHRASES)


def canonical_fallback_record():
    return {"status": FALLBACK_STATUS, "source_url": "", "notes": FALLBACK_DISCLOSURE_NOTE}


def normalize_fallback_record(record):
    """Return a record that satisfies the fallback invariants.

    Status is forced to ``generated_fallback`` and any source URL is dropped, since
    generated artwork has no source. Existing notes are preserved; missing
    disclosure wording is appended rather than replacing history.
    """
    notes = str((record or {}).get("notes", "")).strip()
    if not notes_disclose_fallback(notes):
        notes = (notes + " " + FALLBACK_DISCLOSURE_NOTE).strip()
    return {"status": FALLBACK_STATUS, "source_url": "", "notes": notes}


def build_registry_record(*, generated_fallback, candidate=None, source_name=""):
    """Build the registry record for a freshly written logo reference.

    ``candidate`` must only be supplied when its bytes were downloaded and
    validated for this reference. Fallback status takes precedence over any
    candidate metadata, so a failed download can never leak a third-party source
    onto generated artwork.
    """
    if generated_fallback:
        return canonical_fallback_record()
    if not candidate:
        return None
    page = str(candidate.get("page", "")).strip()
    asset = str(candidate.get("url", "")).strip() or page
    parts = [
        str(source_name or "").strip(),
        str(candidate.get("license", "")).strip(),
        ("Source page: " + page) if page else "",
    ]
    return {
        "status": "third_party_verified",
        "source_url": asset,
        "notes": " ".join(part for part in parts if part),
    }


def normalize_registry(registry):
    """Heal fallback records in a registry. Returns (registry, healed_keys)."""
    healed = []
    for key, record in list(registry.items()):
        parts = key.split("|", 3)
        logo = parts[3] if len(parts) == 4 else ""
        is_fallback = isinstance(record, dict) and (
            record.get("status") == FALLBACK_STATUS or is_generated_fallback_asset(logo)
        )
        if not is_fallback:
            continue
        fixed = normalize_fallback_record(record if isinstance(record, dict) else {})
        if fixed != record:
            registry[key] = fixed
            healed.append(key)
    return registry, healed


def resolve_provenance(registry, playlist, tvg_id, name, logo):
    """Return ``(record, match)`` deterministically.

    An exact registry key wins. Otherwise a record is accepted only if exactly one
    distinct record has the same playlist, tvg-id, channel name and asset stem
    (format conversion and digest suffixes aside). A name-only match is forbidden:
    a different image for the same channel must not inherit provenance. Several
    distinct candidates are ambiguous and resolve to nothing.
    """
    key = canonical_key(f"{playlist}|{tvg_id}|{name}|{logo}")
    for reg_key in sorted(registry):
        if canonical_key(reg_key) == key and isinstance(registry[reg_key], dict):
            return registry[reg_key], MATCH_EXACT

    wanted = asset_stem(logo)
    if not wanted:
        return {}, MATCH_NONE

    distinct = {}
    for reg_key in sorted(registry):
        record = registry[reg_key]
        parts = reg_key.split("|", 3)
        if len(parts) != 4 or not isinstance(record, dict):
            continue
        reg_playlist, reg_id, reg_name, reg_logo = parts
        if (
            reg_playlist == playlist
            and reg_id == tvg_id
            and reg_name == name
            and asset_stem(reg_logo) == wanted
            and record.get("status") in RECORD_STATUSES
        ):
            distinct[json.dumps(record, sort_keys=True)] = record
    if len(distinct) == 1:
        return next(iter(distinct.values())), MATCH_STEM
    return ({}, MATCH_AMBIGUOUS) if distinct else ({}, MATCH_NONE)


def classify_logo(record, match, logo):
    """Classify one logo reference. The asset, not the registry, decides the class.

    Returns a dict with ``status``, ``reason``, ``source_url``,
    ``is_generated_fallback``, ``fallback_is_disclosed`` and ``problems`` (reason
    codes the final validation must reject).
    """
    record = record if isinstance(record, dict) else {}
    record_status = record.get("status", "")
    notes = str(record.get("notes", ""))

    if is_generated_fallback_asset(logo) or record_status == FALLBACK_STATUS:
        problems = []
        if not record or match in (MATCH_NONE, MATCH_AMBIGUOUS):
            problems.append(PROBLEM_UNMATCHED)
        elif record_status != FALLBACK_STATUS:
            problems.append(PROBLEM_STATUS_CONFLICT)
        else:
            if record.get("source_url"):
                problems.append(PROBLEM_SOURCE_URL)
            if not notes_disclose_fallback(notes):
                problems.append(PROBLEM_UNMATCHED)
        return {
            "status": FALLBACK_STATUS,
            # A conflicting or incomplete record never supplies the public reason.
            "reason": notes if not problems else FALLBACK_DISCLOSURE_NOTE,
            "source_url": "",
            "is_generated_fallback": True,
            "fallback_is_disclosed": not problems,
            "problems": problems,
        }

    if record_status in VERIFIED_STATUSES and record.get("source_url"):
        note = notes or "Source recorded in provenance registry."
        if match == MATCH_STEM:
            note = ("Verified source attribution retained for the same local asset stem "
                    "after file-format conversion. " + note)
        return {
            "status": record_status, "reason": note, "source_url": record["source_url"],
            "is_generated_fallback": False, "fallback_is_disclosed": False, "problems": [],
        }

    return {
        "status": "needs_review",
        "reason": ("No unambiguous provenance record matches this exact logo asset; "
                   "a similar channel name alone is not proof."),
        "source_url": "", "is_generated_fallback": False,
        "fallback_is_disclosed": False, "problems": [],
    }
