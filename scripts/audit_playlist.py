#!/usr/bin/env python3
"""Audit playlist identity, metadata, duplicate IDs, and local logo integrity."""
import hashlib
import json
import re
import subprocess
import unicodedata
from collections import defaultdict, Counter
from pathlib import Path
from urllib.parse import unquote
try:
    from PIL import Image
except ImportError:
    Image = None

PLAYLIST = Path("IPTV-Playlist.m3u")
REPORT = Path("reports/iptv-playlist-audit.md")
LOGOS = Path("logos")
RAW_BASE = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/"
ATTR_RE = re.compile(r'([\w-]+)="([^"]*)"')
PRIMARY_EXCEPTIONS = {"Backup", "Not Playing", "New Channels", "New Backup"}
from playlist_order_policy import should_check_alphabetical_order
from country_verification import queue_errors as review_queue_country_errors, reference_from_playlists
CATEGORY_ORDER = ["Bangladesh", "Indian Bangla", "Indian Movies", "Indian Music", "Indian Entertainment", "Pakistani", "International", "Documentary & Wildlife", "Kids", "Religious", "Sports", "New Channels", "New Backup", "Backup", "Not Playing"]
REGISTRY_ORDER = [x for x in CATEGORY_ORDER if x not in {"New Channels", "New Backup"}]  # review queues are never registered

def attrs(line):
    return dict(ATTR_RE.findall(line))

def parse(text):
    lines = text.replace("\r", "").splitlines()
    parsed = []
    current_info = None
    for line in lines:
        if line.startswith("#EXTINF"):
            if current_info is not None:
                parsed.append((current_info, ""))
            current_info = line
            continue
        if current_info is None:
            continue
        value = line.strip()
        if value.startswith(("http://", "https://")):
            parsed.append((current_info, value))
            current_info = None
        elif not value or value.startswith("#"):
            continue
        else:
            parsed.append((current_info, ""))
            current_info = None
    if current_info is not None:
        parsed.append((current_info, ""))
    return parsed

def identity(info):
    a = attrs(info)
    return (a.get("tvg-id") or a.get("channel-id") or "").strip().lower()

def display_name(info):
    a = attrs(info)
    return a.get("tvg-name") or info.rsplit(",", 1)[-1].strip()

def base_id(cid):
    return cid.split("@", 1)[0]

def identity_root(cid):
    return re.sub(r"\.[a-z]{2}$", "", base_id(cid))

def country_code(cid):
    base = base_id(cid)
    if base.startswith("custom."):
        return ""
    m = re.search(r"\.([a-z]{2})$", base)
    return m.group(1).lower() if m else ""

def normalized_name(name):
    return re.sub(r"\s*\[[^]]+\]\s*$", "", name).strip().lower()

def near_duplicate_name(name):
    """Normalize common HD/SD/TV qualifiers for review-only near-duplicate detection."""
    value = unicodedata.normalize("NFKD", str(name or "")).casefold()
    value = re.sub(r"\[[^]]*\]|\([^)]*\)", " ", value)
    value = re.sub(r"\b(hd|sd|uhd|fhd|4k|tv|channel)\b", " ", value)
    return re.sub(r"[^a-z0-9]+", "", value)

def redact_url(url):
    url = re.sub(r'(/live/)[^/?#]+/[^/?#]+/([^/?#]+\.ts)(?=$|[?#])', r'\1[REDACTED]/[REDACTED]/\2', url, flags=re.I)
    return re.sub(r'([?&](?:token|sig|signature|jwt|session|key|authorization|hdnts)=[^&\s]+)', lambda m: m.group(1).split("=", 1)[0] + "=[REDACTED]", url, flags=re.I)

def logo_issue(info):
    logo = attrs(info).get("tvg-logo", "").strip()
    if not logo:
        return "missing"
    def check_local(path):
        try:
            root = LOGOS.resolve()
            resolved = path.resolve()
            if resolved != root and root not in resolved.parents:
                return "other"
        except Exception:
            return "broken-local"
        if not resolved.is_file():
            return "broken-local"
        if resolved.suffix.lower() == ".svg":
            try:
                if "<svg" not in resolved.read_text(encoding="utf-8", errors="ignore")[:10000].lower():
                    return "corrupt-svg"
            except Exception:
                return "corrupt-svg"
            return ""
        if resolved.suffix.lower() not in {".png", ".jpg", ".jpeg", ".webp", ".avif"}:
            return "unsupported-format"
        if Image is None:
            return "unvalidated-image"
        try:
            with Image.open(resolved) as im:
                im.verify()
            with Image.open(resolved) as im:
                if im.width < 16 or im.height < 16:
                    return "invalid-dimensions"
        except Exception:
            return "corrupt-image"
        return ""
    if logo.startswith(RAW_BASE):
        fn = unquote(logo[len(RAW_BASE):].split("?", 1)[0].split("#", 1)[0]).lstrip("/")
        return check_local(LOGOS / fn)
    if logo.startswith("logos/"):
        return check_local(Path(unquote(logo)))
    if logo.startswith(("http://", "https://")):
        return "external"
    return "other"

entries = parse(PLAYLIST.read_text(encoding="utf-8-sig"))
raw_lines = PLAYLIST.read_text(encoding="utf-8-sig").replace("\r","").splitlines()
category_registry_issues = []
registry_lines = [line for line in raw_lines if line.startswith("#PLAYLIST-STUDIO-CATEGORIES:")]
if len(registry_lines) != 1:
    category_registry_issues.append(f"expected exactly one category registry, found {len(registry_lines)}")
else:
    try:
        actual_registry = json.loads(registry_lines[0].split(":", 1)[1])
        if actual_registry != REGISTRY_ORDER:
            category_registry_issues.append("registry does not match canonical category order")
        if any(value not in CATEGORY_ORDER for value in actual_registry):
            category_registry_issues.append("registry contains an unknown category")
        if any(value in actual_registry for value in ("New Channels", "New Backup")):
            category_registry_issues.append("review queue categories must not be registered")
    except Exception as exc:
        category_registry_issues.append("registry is not valid JSON: " + str(exc)[:100])
malformed_extinf = []

def validate_extinf(line_no, line):
    errors = []
    if not re.match(r"^#EXTINF:-?\d+(?:\.\d+)?(?:\s|,|$)", line):
        errors.append("invalid EXTINF duration/prefix")
    if line.count('"') % 2:
        errors.append("unbalanced quotes")
        return errors
    in_quote = False
    comma = None
    for idx, ch in enumerate(line):
        if ch == '"':
            in_quote = not in_quote
        elif ch == "," and not in_quote:
            comma = idx
            break
    if comma is None:
        errors.append("missing display-name comma")
        return errors
    if not line[comma+1:].strip():
        errors.append("missing display name")
        return errors
    prefix = line[len("#EXTINF:"):comma]
    duration_match = re.match(r"-?\d+(?:\.\d+)?", prefix)
    attrs_part = prefix[duration_match.end():] if duration_match else prefix
    seen_keys = set()
    pos = 0
    attr_re = re.compile(r"([A-Za-z0-9_-]+)=")
    while pos < len(attrs_part):
        while pos < len(attrs_part) and attrs_part[pos].isspace():
            pos += 1
        if pos >= len(attrs_part):
            break
        m = attr_re.match(attrs_part, pos)
        if not m:
            errors.append("malformed attribute syntax")
            break
        key = m.group(1)
        if key in seen_keys:
            errors.append(f"duplicate attribute: {key}")
        seen_keys.add(key)
        pos = m.end()
        if pos >= len(attrs_part) or attrs_part[pos] != '"':
            errors.append(f"unquoted attribute value: {key}")
            break
        pos += 1
        end = pos
        while end < len(attrs_part) and attrs_part[end] != '"':
            end += 1
        if end >= len(attrs_part):
            errors.append(f"unterminated attribute value: {key}")
            break
        pos = end + 1
        if pos < len(attrs_part) and not attrs_part[pos].isspace():
            errors.append(f"missing whitespace between attributes near {key}")
            break
    j = line_no
    while j < len(raw_lines):
        candidate = raw_lines[j].strip()
        if not candidate:
            j += 1
            continue
        if candidate.lower().startswith(("http://", "https://")):
            break
        if candidate.startswith("#") and not candidate.upper().startswith("#EXTINF:"):
            j += 1
            continue
        break
    if j >= len(raw_lines) or not raw_lines[j].strip().lower().startswith(("http://", "https://")):
        errors.append("missing stream URL")
    return errors

for n, line in enumerate(raw_lines, 1):
    if line.startswith("#EXTINF:"):
        for reason in validate_extinf(n, line):
            malformed_extinf.append((n, reason))

by_id = defaultdict(list)
by_base = defaultdict(list)
by_name = defaultdict(list)
urls = defaultdict(list)
for info, url in entries:
    a = attrs(info)
    cid = identity(info)
    name = display_name(info).strip().lower()
    if cid:
        by_id[cid].append((info, url))
        by_base[base_id(cid)].append((info, url))
    if name:
        by_name[name].append((info, url))
    if url:
        urls[url.lower()].append((info, url))

duplicate_ids = {k:v for k,v in by_id.items() if len(v) > 1}
duplicate_urls = {k:v for k,v in urls.items() if len(v) > 1}
primary_entries = [(info, url) for info, url in entries if attrs(info).get("group-title", "").strip() not in PRIMARY_EXCEPTIONS]
primary_identity_groups = defaultdict(list)
primary_channel_numbers = defaultdict(list)
for info, url in primary_entries:
    a = attrs(info)
    cid = identity(info)
    if cid:
        # A channel identity may have only one primary record globally; an ID
        # repeated in a different category is still a primary-identity collision.
        primary_identity_groups[cid].append((info, url))
    chno = a.get("tvg-chno", "").strip()
    if chno:
        primary_channel_numbers[chno].append((info, url))
primary_duplicate_ids = {key: items for key, items in primary_identity_groups.items() if len(items) > 1}
primary_chno_collisions = {key: items for key, items in primary_channel_numbers.items() if len(items) > 1}

suspicious_urls = []
signed_urls = []
xtream_credential_paths = []
for info, url in entries:
    if re.search(r"[?&](?:token|sig|signature|jwt|session|key|authorization)=[^&]+", url, re.I) or re.search(r"[?&]hdnts=[^&]+", url, re.I):
        signed_urls.append((display_name(info), attrs(info).get("group-title", "").strip(), url))
    if re.search(r"/live/[^/?#]+/[^/?#]+/[^/?#]+\.ts(?:[?#]|$)", url, re.I):
        xtream_credential_paths.append((display_name(info), attrs(info).get("group-title", "").strip(), url))
    if re.search(r"[?&](token|auth)=(?:test|testpub)(?:&|$)", url, re.I):
        suspicious_urls.append((display_name(info), "test credential", url))
    elif re.search(r"https?://[^/@]+@[^/]+", url, re.I):
        suspicious_urls.append((display_name(info), "URL userinfo", url))
    elif re.search(r"[?&]hdnts=$", url, re.I):
        suspicious_urls.append((display_name(info), "empty hdnts", url))
    if re.search(r"^https?://(?:[^/]+\.)?dvltv\.cc(?::\d+)?/play(?:/|$)", url, re.I):
        suspicious_urls.append((display_name(info), "blocked dvltv.cc/play route", url))

metadata_conflicts = []
for cid, items in sorted(by_id.items()):
    non_backup = [x for x in items if attrs(x[0]).get("group-title", "").strip() not in PRIMARY_EXCEPTIONS]
    if len(non_backup) < 2:
        continue
    names = {normalized_name(display_name(x[0])) for x in non_backup}
    groups = {attrs(x[0]).get("group-title", "") for x in non_backup}
    countries = {attrs(x[0]).get("tvg-country", "") for x in non_backup}
    if len(names) > 1 or len(groups) > 1 or len(countries) > 1:
        metadata_conflicts.append((cid, names, groups, countries))

def cross_queue_name_key(value):
    value = unicodedata.normalize("NFKC", str(value or "")).casefold().strip()
    value = re.sub(r"\s*(?:\[[^]]*(?:geo[- ]?blocked|geo blocked)[^]]*\]|\((?:\d{3,4}[pi]|UHD|FHD|HD\+?|SD)\)|\s+(?:\d{3,4}[pi]))\s*$", "", value, flags=re.I)
    value = re.sub(r"\s+", " ", value).strip()
    aliases = {
        "disney channel (india)": "disney channel india",
        "gazi tv": "g tv",
        "nick": "nickelodeon (india)",
    }
    value = aliases.get(value, value)
    return re.sub(r"[^a-z0-9]+", "", value)


# Report label/ID variants across primary and review groups separately from
# primary-only blocking metrics. This is diagnostic only: no IDs or URLs change.
cross_id_names = defaultdict(list)
cross_name_ids = defaultdict(list)
for info, url in entries:
    a = attrs(info)
    cid = identity(info).casefold()
    name = display_name(info).strip()
    key = cross_queue_name_key(name)
    group = a.get("group-title", "").strip() or "Uncategorized"
    if cid and key:
        cross_id_names[cid].append((name, group, key))
        cross_name_ids[key].append((cid, name, group))
cross_queue_metadata_variants = {
    cid: rows for cid, rows in cross_id_names.items()
    if len({key for _, _, key in rows}) > 1
}
cross_queue_name_id_collisions = {
    key: rows for key, rows in cross_name_ids.items()
    if len({cid for cid, _, _ in rows if cid}) > 1
}

REVIEW_GROUPS = {"New Channels", "New Backup"}
name_collisions = {k: [x for x in v if attrs(x[0]).get("group-title", "").strip() not in REVIEW_GROUPS] for k, v in by_name.items()}
name_collisions = {k:v for k,v in name_collisions.items() if len({identity_root(identity(x[0])) for x in v}) > 1}

primary_by_root = defaultdict(list)
primary_by_name = defaultdict(list)
for cid, items in by_id.items():
    for info, url in items:
        if attrs(info).get("group-title", "").strip() not in PRIMARY_EXCEPTIONS:
            primary_by_root[identity_root(cid)].append((cid, info, url))
            primary_by_name[normalized_name(display_name(info))].append((cid, info, url))

# Near-duplicate names are warnings only: different IDs can represent
# distinct legitimate feeds or HD/SD variants and must not be merged automatically.
near_name_index = defaultdict(list)
for info, url in primary_entries:
    cid = identity(info)
    key = near_duplicate_name(display_name(info))
    if key:
        near_name_index[key].append((cid, info, url))
near_duplicate_name_groups = {
    key: items
    for key, items in near_name_index.items()
    if len({cid for cid, _, _ in items if cid}) > 1
    and len({display_name(info).strip().casefold() for _, info, _ in items}) > 1
}
cross_country_backups = []

logos_by_id = defaultdict(set)
logo_counts = Counter()
logo_exceptions = []
logo_warnings = []
review_logo_exceptions = []
for info, url in entries:
    cid = identity(info)
    logo = attrs(info).get("tvg-logo", "").strip()
    if cid and logo:
        logos_by_id[cid].add(logo)
    issue = logo_issue(info)
    logo_counts["healthy" if not issue else issue] += 1
    item = (display_name(info), identity(info), issue, attrs(info).get("tvg-logo",""))
    if issue == "external":
        logo_warnings.append(item)
    elif issue in {"missing", "broken-local", "unsupported-format", "invalid-dimensions", "corrupt-image", "unvalidated-image", "other"}:
        # Every entry, including Backup and Not Playing, must use a valid local logo.
        logo_exceptions.append(item)

protected_changes = []
try:
    old = subprocess.check_output(["git", "show", "HEAD:IPTV-Playlist.m3u"], text=True, stderr=subprocess.DEVNULL)
    old_primary_urls = Counter(
        url.strip().casefold()
        for info, url in parse(old)
        if url.strip() and attrs(info).get("group-title", "").strip() not in PRIMARY_EXCEPTIONS
    )
    current_urls = Counter(url.strip().casefold() for info, url in entries if url.strip())
    # Metadata/ID/logo corrections may legitimately rewrite EXTINF. A primary
    # stream is protected by its URL; the separate review-queue guard protects
    # Backup/Not Playing records and their original category.
    for url, count in old_primary_urls.items():
        if current_urls[url] < count:
            protected_changes.append(("", url, "primary stream URL removed"))
except Exception:
    pass

missing_primary_chno = [(info, url) for info, url in entries if attrs(info).get("group-title", "").strip() not in PRIMARY_EXCEPTIONS and not attrs(info).get("tvg-chno", "").strip()]
missing_primary_country = [(info, url) for info, url in primary_entries if not attrs(info).get("tvg-country", "").strip()]
missing_primary_language = [(info, url) for info, url in primary_entries if not attrs(info).get("tvg-language", "").strip()]
metadata_gaps_by_group = defaultdict(Counter)
for info, url in primary_entries:
    a = attrs(info)
    group = a.get("group-title", "").strip() or "Uncategorized"
    if not a.get("tvg-country", "").strip():
        metadata_gaps_by_group[group]["tvg-country"] += 1
    if not a.get("tvg-language", "").strip():
        metadata_gaps_by_group[group]["tvg-language"] += 1
category_transitions = []
last_group = None
for info, url in entries:
    group = attrs(info).get("group-title", "").strip()
    if group != last_group:
        category_transitions.append(group)
        last_group = group
category_order_issues = []
last_index = -1
for group in category_transitions:
    if group not in CATEGORY_ORDER:
        category_order_issues.append((group, "unknown category"))
        continue
    index = CATEGORY_ORDER.index(group)
    if index < last_index:
        category_order_issues.append((group, "out of canonical block order"))
    last_index = max(last_index, index)

alphabetical_order_issues = []
def natural_sort_key(value):
    value = unicodedata.normalize("NFKD", value).casefold().strip()
    return [int(part) if part.isdigit() else part for part in re.split(r"(\d+)", value)]
for group in category_transitions:
    # Backup and Not Playing are manually maintained, byte-for-byte protected
    # review queues. Their internal order must not block automated maintenance.
    if not should_check_alphabetical_order(group):
        continue
    group_entries = [(info, url) for info, url in entries if attrs(info).get("group-title", "").strip() == group]
    if group == "Bangladesh":
        # The Bangladesh group is intentionally ordered by tvg-chno, not A–Z.
        numbered = []
        for info, url in group_entries:
            chno = attrs(info).get("tvg-chno", "").strip()
            if not chno.isdigit():
                continue
            numbered.append((int(chno), display_name(info).strip()))
        for (prev_no, prev_name), (cur_no, cur_name) in zip(numbered, numbered[1:]):
            if cur_no < prev_no:
                alphabetical_order_issues.append((group, f"{prev_no} — {prev_name}", f"{cur_no} — {cur_name}"))
        continue
    names = [display_name(info).strip() for info, url in group_entries]
    for prev, cur in zip(names, names[1:]):
        if natural_sort_key(cur) < natural_sort_key(prev):
            alphabetical_order_issues.append((group, prev, cur))

_reference = reference_from_playlists([PLAYLIST, Path("BDIX-Playlist.m3u"), Path("International-Playlist.m3u")])
review_queue_country_issues = review_queue_country_errors(
    [(attrs(info), display_name(info), url) for info, url in entries], _reference)

lines = [
    "# IPTV Playlist Audit", "", "Non-destructive audit of channel identity, metadata consistency, duplicate identities, and logo integrity.", "Scope note: Metadata conflicts and same-name/different-ID counts below cover canonical primary entries; cross-queue variants are shown separately as review diagnostics.", "", "## Summary", "",
    f"- Playlist entries: **{len(entries)}**", f"- Unique channel IDs: **{len(by_id)}**", f"- IDs with multiple streams: **{len(duplicate_ids)}**", f"- Duplicate stream URLs: **{len(duplicate_urls)}**", f"- Metadata conflicts: **{len(metadata_conflicts)}**", f"- Same-name / different-ID collisions: **{len(name_collisions)}**", f"- Cross-queue same-ID name variants (review): **{len(cross_queue_metadata_variants)}**", f"- Cross-queue normalized-name/different-ID groups (review): **{len(cross_queue_name_id_collisions)}**", f"- Cross-country backup collisions: **{len(cross_country_backups)}**", f"- IDs with multiple logo references: **{sum(1 for v in logos_by_id.values() if len(v) > 1)}**", f"- Protected primary-entry changes: **{len(protected_changes)}**", f"- Logo exceptions requiring repair: **{len(logo_exceptions)}**", f"- External logo references (review only): **{len(logo_warnings)}**", f"- Logo references checked: **{sum(logo_counts.values())}**", f"- Duplicate primary identities: **{len(primary_duplicate_ids)}**", f"- Potential near-duplicate primary name groups (review only): **{len(near_duplicate_name_groups)}**", f"- Primary channel-number collisions: **{len(primary_chno_collisions)}**", f"- Primary entries missing channel numbers: **{len(missing_primary_chno)}**", f"- Primary entries missing tvg-country: **{len(missing_primary_country)}**", f"- Primary entries missing tvg-language: **{len(missing_primary_language)}**", f"- Malformed EXTINF entries: **{len(malformed_extinf)}**", f"- Category block-order issues: **{len(category_order_issues)}**", f"- Category registry issues: **{len(category_registry_issues)}**", f"- Alphabetical ordering issues: **{len(alphabetical_order_issues)}**", f"- Suspicious URL credentials/syntax: **{len(suspicious_urls)}**", f"- Signed/tokenized stream URLs: **{len(signed_urls)}**", f"- Embedded Xtream-style credential paths (redacted): **{len(xtream_credential_paths)}**", ""]
lines += ["", "## Primary Metadata Completeness", "",
    "Missing country/language values are informational, not a reason to delete, reclassify, or block otherwise valid channel entries. Only trusted exact-ID source metadata should be used to fill these fields.",
    f"- Active primary entries missing tvg-country: **{len(missing_primary_country)}**",
    f"- Active primary entries missing tvg-language: **{len(missing_primary_language)}**",
    "", "| Group | Missing tvg-country | Missing tvg-language |", "|---|---:|---:|"]
for group in sorted(metadata_gaps_by_group):
    gap = metadata_gaps_by_group[group]
    lines.append(f"| {group} | {gap['tvg-country']} | {gap['tvg-language']} |")
lines += ["", "## Review Queue Country Verification", ""]
if review_queue_country_issues:
    lines.extend("- " + issue for issue in review_queue_country_issues)
else:
    lines.append("New Channels/New Backup contain only entries verified as BD/IN.")
lines += ["", "## Category Registry", ""]
if category_registry_issues:
    lines.extend("- " + issue for issue in category_registry_issues)
else:
    lines.append("Canonical registry matches the permanent IPTV category order.")
lines += ["", "## Cross-Queue Identity Variants", "",
    "These diagnostics include canonical and review groups. Name/ID differences can be legitimate; this section does not merge identities, remove entries, or print stream URLs.", ""]
if cross_queue_metadata_variants:
    for cid, rows in sorted(cross_queue_metadata_variants.items()):
        variants = sorted({(name, group) for name, group, _ in rows})
        lines.append(f"- Same ID {cid}: " + "; ".join(f"{name} [{group}]" for name, group in variants))
else:
    lines.append("No same-ID label variants found across groups.")
lines.append("")
if cross_queue_name_id_collisions:
    for key, rows in sorted(cross_queue_name_id_collisions.items()):
        variants = sorted({(cid, name, group) for cid, name, group in rows})
        lines.append("- Same normalized name: " + "; ".join(f"{name} [{cid}] ({group})" for cid, name, group in variants))
else:
    lines.append("No normalized same-name/different-ID groups found across groups.")
lines += ["", "## Duplicate IDs", ""]
for cid, items in sorted(duplicate_ids.items()):
    lines.append(f"### {cid} ({len(items)} streams)")
    for info, url in items:
        lines.append(f"- {display_name(info)} — {attrs(info).get('group-title','')} — {redact_url(url)}")
if not duplicate_ids: lines.append("None.")
lines += ["", "## Duplicate Primary Identities", ""]
if primary_duplicate_ids:
    for cid, items in sorted(primary_duplicate_ids.items()):
        details = []
        for info, url in items:
            group = attrs(info).get("group-title", "").strip()
            details.append(f"{display_name(info)} [{group}] — {redact_url(url)}")
        lines.append(f"- **{cid}** — " + "; ".join(details))
else: lines.append("None.")
lines += ["", "## Potential Near-Duplicate Primary Names (Review Only)", ""]
if near_duplicate_name_groups:
    for key, items in sorted(near_duplicate_name_groups.items()):
        details = []
        for cid, info, url in sorted(items, key=lambda item: (display_name(item[1]).casefold(), item[0])):
            details.append(f"{display_name(info)} [{cid}] ({attrs(info).get('group-title', '').strip()})")
        lines.append("- " + "; ".join(details))
    lines.append("")
    lines.append("These are review suggestions only. The audit does not merge identities, change channel order, or remove streams.")
else:
    lines.append("None.")
lines += ["", "## Primary Channel-Number Collisions", ""]
if primary_chno_collisions:
    for chno, items in sorted(primary_chno_collisions.items()): lines.append(f"- **{chno}** — " + ", ".join(display_name(x[0]) for x in items))
else: lines.append("None.")
lines += ["", "## Malformed EXTINF Entries", ""]
if malformed_extinf:
    for line_no, reason in malformed_extinf: lines.append(f"- line {line_no}: {reason}")
else: lines.append("None.")
lines += ["", "## Ordering", ""]
if category_order_issues:
    for group, reason in category_order_issues: lines.append(f"- category block **{group}** — {reason}")
else: lines.append("Category block order: OK.")
if alphabetical_order_issues:
    for group, prev, cur in alphabetical_order_issues: lines.append(f"- **{group}** — **{cur}** appears after **{prev}**")
else: lines.append("Primary-category alphabetical/channel-number order: OK.")
lines.append("Backup/Not Playing/New Channels/New Backup internal order is preserved for manual review and is intentionally not auto-enforced.")
lines += ["", "## Suspicious URLs", ""]
if suspicious_urls:
    for name, reason, url in suspicious_urls: lines.append(f"- **{name}** — {reason} — {redact_url(url)}")
else: lines.append("None.")
lines += ["", "## Signed / Tokenized Stream URLs", ""]
if signed_urls:
    for name, group, url in signed_urls: lines.append(f"- **{name}** — {group or 'Uncategorized'} — {redact_url(url)}")
else: lines.append("None.")
lines += ["", "## Embedded Xtream-Style Credential Paths (redacted)", ""]
if xtream_credential_paths:
    for name, group, url in xtream_credential_paths: lines.append(f"- **{name}** — {group or 'Uncategorized'} — {redact_url(url)}")
else: lines.append("None.")
lines += ["", "## Logo Integrity", "", f"- Healthy/local references: **{logo_counts['healthy']}**", f"- External references (review only): **{logo_counts['external']}**"]
for issue in ["missing","broken-local","unsupported-format","invalid-dimensions","corrupt-image","unvalidated-image","other"]:
    lines.append(f"- {issue}: **{logo_counts[issue]}**")
lines += ["", "## External Logo Review", ""]
if logo_warnings:
    for name, cid, issue, logo in logo_warnings[:200]: lines.append(f"- {name} [{cid}] — {logo}")
    if len(logo_warnings) > 200: lines.append(f"- ... {len(logo_warnings)-200} additional external logo references omitted from report.")
else: lines.append("None.")
lines += ["", "## Protected Primary Entries", ""]
if protected_changes: lines.extend(f"- **{cid}** — {url}: {kind}" for cid,url,kind in protected_changes)
else: lines.append("No protected primary-entry changes detected.")
lines.insert(1, "Generated: **" + __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat() + "**")
lines.insert(2, "Source playlist SHA-256: **" + hashlib.sha256(PLAYLIST.read_bytes()).hexdigest() + "**")
REPORT.parent.mkdir(parents=True, exist_ok=True)
REPORT.write_text("\n".join(lines).rstrip()+"\n", encoding="utf-8")
print(f"Playlist audit: entries={len(entries)} duplicate_ids={len(duplicate_ids)} duplicate_urls={len(duplicate_urls)} conflicts={len(metadata_conflicts)} name_collisions={len(name_collisions)} protected_changes={len(protected_changes)} logo_exceptions={len(logo_exceptions)} external_logo_warnings={len(logo_warnings)}")

def run_change_guard():
    try:
        old_text = subprocess.check_output(
            ["git", "show", "HEAD:IPTV-Playlist.m3u"],
            text=True,
            stderr=subprocess.DEVNULL,
        )
    except Exception:
        return

    old_entries = parse(old_text)
    old_urls = Counter(url.strip().casefold() for _, url in old_entries if url.strip())
    new_urls = Counter(url.strip().casefold() for _, url in entries if url.strip())
    removed = sum(max(0, count - new_urls[url]) for url, count in old_urls.items())
    if removed:
        raise SystemExit(
            f"Change Guard blocked maintenance: {removed} existing stream URL occurrence(s) "
            "would disappear. Existing streams are never automatically deleted."
        )

    # Keep a bounded-change guard on newly introduced URLs without treating
    # metadata-only EXTINF repairs as removals/additions.
    added = sum(max(0, count - old_urls[url]) for url, count in new_urls.items())
    if added > 150:
        raise SystemExit(
            f"Change Guard blocked maintenance: {added} new stream URL occurrence(s) "
            "exceed the 150-entry review limit."
        )

run_change_guard()

if protected_changes: raise SystemExit("Protected primary playlist entries changed; refusing automatic commit.")
if duplicate_urls: raise SystemExit(f"Duplicate stream URLs detected ({len(duplicate_urls)} unique URLs); refusing automatic commit.")
if primary_duplicate_ids: raise SystemExit("Duplicate primary identities detected; refusing automatic commit.")
if primary_chno_collisions: raise SystemExit("Primary channel-number collisions detected; refusing automatic commit.")
if malformed_extinf: raise SystemExit("Malformed EXTINF entries detected; refusing automatic commit.")
if category_order_issues or alphabetical_order_issues: raise SystemExit("Playlist ordering defects detected; refusing automatic commit.")
if suspicious_urls: raise SystemExit("Suspicious test credentials or malformed URL syntax detected; refusing automatic commit.")
backup_channel_numbers = [(info,url) for info,url in entries if attrs(info).get("group-title","").strip()=="Backup" and attrs(info).get("tvg-chno","").strip()]
missing_primary_chno = [(info,url) for info,url in entries if attrs(info).get("group-title","").strip() not in PRIMARY_EXCEPTIONS and not attrs(info).get("tvg-chno","").strip()]
if backup_channel_numbers: raise SystemExit("Backup entries must not carry tvg-chno.")
if missing_primary_chno: raise SystemExit("All active primary entries must carry tvg-chno.")
if review_queue_country_issues: raise SystemExit("New Channels/New Backup contain entries not verified as BD/IN; refusing automatic commit.")
if logo_exceptions: raise SystemExit("Logo integrity failures detected in active/reviewable entries.")
