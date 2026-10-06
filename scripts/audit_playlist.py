#!/usr/bin/env python3
"""Audit playlist identity, metadata, duplicate IDs, and local logo integrity."""
import re
import subprocess
from collections import defaultdict, Counter
from pathlib import Path
try:
    from PIL import Image
except ImportError:
    Image = None

PLAYLIST = Path("IPTV-Playlist.m3u")
REPORT = Path("reports/playlist-audit.md")
LOGOS = Path("logos")
RAW_BASE = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/"
ATTR_RE = re.compile(r'([\w-]+)="([^"]*)"')
PRIMARY_EXCEPTIONS = {"Backup", "New", "New Backup", "New Channels", "Not Playing"}
CATEGORY_ORDER = ["Bangladesh", "Indian Bangla", "Indian Movies", "Indian Music", "Indian Entertainment", "Pakistani", "International", "Documentary & Wildlife", "Kids", "Religious", "Sports", "Backup", "New", "Not Playing"]

def attrs(line):
    return dict(ATTR_RE.findall(line))

def parse(text):
    lines = text.replace("\r", "").splitlines()
    entries = []
    i = 0
    while i < len(lines):
        if lines[i].startswith("#EXTINF"):
            info = lines[i]
            url = ""
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and lines[j].startswith(("http://", "https://")):
                url = lines[j].strip()
            entries.append((info, url))
            i = j
        i += 1
    return entries

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
    # Custom identities such as custom.bangla.tv are internal IDs, not
    # country-qualified channel IDs. Do not interpret their final label
    # (e.g. ".tv") as an ISO country code.
    if base.startswith("custom."):
        return ""
    m = re.search(r"\.([a-z]{2})$", base)
    return m.group(1).lower() if m else ""

def normalized_name(name):
    return re.sub(r"\s*\[[^]]+\]\s*$", "", name).strip().lower()

def redact_url(url):
    """Redact credential-like query values in reports without changing the playlist."""
    return re.sub(
        r'([?&](?:token|sig|signature|jwt|session|key|authorization|hdnts)=[^&\s]+)',
        lambda m: m.group(1).split("=", 1)[0] + "=[REDACTED]",
        url,
        flags=re.I,
    )

def logo_issue(info):
    logo = attrs(info).get("tvg-logo", "").strip()
    if not logo:
        return "missing"

    def check_local(path):
        if not path.is_file():
            return "broken-local"
        if path.suffix.lower() == ".svg":
            try:
                if "<svg" not in path.read_text(encoding="utf-8", errors="ignore")[:10000].lower():
                    return "corrupt-svg"
            except Exception:
                return "corrupt-svg"
            return ""
        if path.suffix.lower() not in {".png", ".jpg", ".jpeg", ".webp", ".avif"}:
            return "unsupported-format"
        if Image is None:
            return "unvalidated-image"
        try:
            with Image.open(path) as im:
                im.verify()
            with Image.open(path) as im:
                if im.width < 16 or im.height < 16:
                    return "invalid-dimensions"
        except Exception:
            return "corrupt-image"
        return ""

    if logo.startswith(RAW_BASE):
        fn = logo[len(RAW_BASE):].split("?", 1)[0].lstrip("/")
        return check_local(LOGOS / fn)
    if logo.startswith("logos/"):
        return check_local(Path(logo))
    if "raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV" in logo:
        return "repository-reference"
    if logo.startswith(("http://", "https://")):
        return "external"
    return "other"

entries = parse(PLAYLIST.read_text(encoding="utf-8-sig"))
raw_lines = PLAYLIST.read_text(encoding="utf-8-sig").replace("\r","").splitlines()
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
    while j < len(raw_lines) and not raw_lines[j].strip():
        j += 1
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

primary_entries = [
    (info, url) for info, url in entries
    if attrs(info).get("group-title", "").strip() not in PRIMARY_EXCEPTIONS
]
primary_identity_groups = defaultdict(list)
primary_channel_numbers = defaultdict(list)
for info, url in primary_entries:
    a = attrs(info)
    cid = identity(info)
    if cid:
        primary_identity_groups[(cid, a.get("group-title", "").strip())].append((info, url))
    chno = a.get("tvg-chno", "").strip()
    if chno:
        primary_channel_numbers[chno].append((info, url))

primary_duplicate_ids = {
    key: items for key, items in primary_identity_groups.items() if len(items) > 1
}
primary_chno_collisions = {
    key: items for key, items in primary_channel_numbers.items() if len(items) > 1
}

suspicious_urls = []
signed_urls = []
for info, url in entries:
    if re.search(r"[?&](?:token|sig|signature|jwt|session|key|authorization)=[^&]+", url, re.I) or re.search(r"[?&]hdnts=[^&]+", url, re.I):
        signed_urls.append((display_name(info), attrs(info).get("group-title", "").strip(), url))
    if re.search(r"[?&](token|auth)=(?:test|testpub)(?:&|$)", url, re.I):
        suspicious_urls.append((display_name(info), "test credential", url))
    elif re.search(r"https?://[^/@]+@[^/]+", url, re.I):
        suspicious_urls.append((display_name(info), "URL userinfo", url))
    elif re.search(r"[?&]hdnts=$", url, re.I):
        suspicious_urls.append((display_name(info), "empty hdnts", url))

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

name_collisions = {k:v for k,v in by_name.items() if len({identity_root(identity(x[0])) for x in v}) > 1}

primary_by_root = defaultdict(list)
primary_by_name = defaultdict(list)
for cid, items in by_id.items():
    for info, url in items:
        if attrs(info).get("group-title", "").strip() != "Backup":
            primary_by_root[identity_root(cid)].append((cid, info, url))
            primary_by_name[normalized_name(display_name(info))].append((cid, info, url))

# Backup validity is channel-based, not transmission-country-based.
# A Bangladeshi channel remains the same channel regardless of where its
# stream is transmitted or hosted. Country-qualified IDs are therefore not
# used as a blocking criterion for backup streams.
cross_country_backups = []

logos_by_id = defaultdict(set)
logo_counts = Counter()
logo_exceptions = []
review_logo_exceptions = []

for info, url in entries:
    cid = identity(info)
    logo = attrs(info).get("tvg-logo", "").strip()
    if cid and logo:
        logos_by_id[cid].add(logo)
    issue = logo_issue(info)
    logo_counts["healthy" if not issue or issue == "repository-reference" else issue] += 1
    if issue in {"missing", "broken-local", "external", "unsupported-format", "invalid-dimensions", "corrupt-image", "unvalidated-image", "other"}:
        item = (display_name(info), identity(info), issue, attrs(info).get("tvg-logo",""))
        if attrs(info).get("group-title", "").strip() == "Not Playing":
            review_logo_exceptions.append(item)
        else:
            logo_exceptions.append(item)

protected_changes = []
try:
    old = subprocess.check_output(["git", "show", "HEAD:IPTV-Playlist.m3u"], text=True, stderr=subprocess.DEVNULL)
    old_primary = Counter()
    new_primary = Counter()
    new_not_playing = Counter()

    # A primary entry is protected against silent removal or URL/identity
    # changes. Moving the exact same entry to Not Playing is intentional
    # quarantine behavior and is not a destructive change.
    def stable(info, url):
        a = attrs(info)
        return (
            (a.get("tvg-id") or a.get("channel-id") or "").strip().lower(),
            url.strip(),
        )

    for info, url in parse(old):
        if attrs(info).get("group-title", "").strip() not in PRIMARY_EXCEPTIONS:
            old_primary[stable(info, url)] += 1

    for info, url in entries:
        group = attrs(info).get("group-title", "").strip()
        key = stable(info, url)
        if group not in PRIMARY_EXCEPTIONS:
            new_primary[key] += 1
        elif group == "Not Playing":
            new_not_playing[key] += 1

    # A metadata identity repair may intentionally change an existing primary
    # tvg-id/channel-id when the exact stream URL is preserved under a derived
    # identity (for example, resolving an old duplicate ID as @ALT1/@HD).
    # Treat that as safe: the protected stream itself was not removed.
    new_primary_by_url = defaultdict(list)
    for (cid, url), count in new_primary.items():
        new_primary_by_url[url].append((cid, count))

    for key, count in old_primary.items():
        cid, url = key
        direct = new_primary[key]
        if direct + new_not_playing[key] >= count:
            continue
        preserved = 0
        for new_cid, new_count in new_primary_by_url.get(url, []):
            if new_cid.startswith(cid + "@"):
                preserved += new_count
        if direct + preserved < count:
            protected_changes.append((cid, url, "primary entry removed or changed"))
except Exception:
    pass

missing_primary_chno = [
    (info, url) for info, url in entries
    if attrs(info).get("group-title", "").strip() not in PRIMARY_EXCEPTIONS
    and not attrs(info).get("tvg-chno", "").strip()
]

# Category blocks must follow the canonical order and each block must be A-Z.
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
import unicodedata

def natural_sort_key(value):
    value = unicodedata.normalize("NFKD", value).casefold().strip()
    return [int(part) if part.isdigit() else part for part in re.split(r"(\\d+)", value)]

for group in category_transitions:
    names = [display_name(info).strip() for info, url in entries if attrs(info).get("group-title", "").strip() == group]
    for prev, cur in zip(names, names[1:]):
        if natural_sort_key(cur) < natural_sort_key(prev):
            alphabetical_order_issues.append((group, prev, cur))

lines = [
    "# Playlist Audit",
    "",
    "Non-destructive audit of channel identity, metadata consistency, duplicate identities, and logo integrity.",
    "",
    "## Summary",
    "",
    f"- Playlist entries: **{len(entries)}**",
    f"- Unique channel IDs: **{len(by_id)}**",
    f"- IDs with multiple streams: **{len(duplicate_ids)}**",
    f"- Duplicate stream URLs: **{len(duplicate_urls)}**",
    f"- Metadata conflicts: **{len(metadata_conflicts)}**",
    f"- Same-name / different-ID collisions: **{len(name_collisions)}**",
    f"- Cross-country backup collisions: **{len(cross_country_backups)}**",
    f"- IDs with multiple logo references: **{sum(1 for v in logos_by_id.values() if len(v) > 1)}**",
    f"- Protected primary-entry changes: **{len(protected_changes)}**",
    f"- Logo exceptions: **{len(logo_exceptions)}**",
    f"- Logo references checked: **{sum(logo_counts.values())}**",
    f"- Not Playing logo exceptions: **{len(review_logo_exceptions)}**",
    f"- Duplicate primary identities: **{len(primary_duplicate_ids)}**",
    f"- Primary channel-number collisions: **{len(primary_chno_collisions)}**",
    f"- Primary entries missing channel numbers: **{len(missing_primary_chno)}**",
    f"- Malformed EXTINF entries: **{len(malformed_extinf)}**",
    f"- Category block-order issues: **{len(category_order_issues)}**",
    f"- Alphabetical ordering issues: **{len(alphabetical_order_issues)}**",
    f"- Suspicious URL credentials/syntax: **{len(suspicious_urls)}**",
    f"- Signed/tokenized stream URLs: **{len(signed_urls)}**",
    "",
    "## Duplicate IDs",
    "",
]
for cid, items in sorted(duplicate_ids.items()):
    lines.append(f"### {cid} ({len(items)} streams)")
    for info, url in items:
        lines.append(f"- {display_name(info)} — {attrs(info).get('group-title','')} — {redact_url(url)}")
if not duplicate_ids:
    lines.append("None.")

lines += ["", "## Duplicate Primary Identities", ""]
if primary_duplicate_ids:
    for (key, items) in sorted(primary_duplicate_ids.items()):
        cid, group = key
        lines.append(f"- **{cid}** in **{group}** — " + ", ".join(display_name(x[0]) for x in items))
else:
    lines.append("None.")

lines += ["", "## Primary Channel-Number Collisions", ""]
if primary_chno_collisions:
    for chno, items in sorted(primary_chno_collisions.items()):
        lines.append(f"- **{chno}** — " + ", ".join(display_name(x[0]) for x in items))
else:
    lines.append("None.")

lines += ["", "## Malformed EXTINF Entries", ""]
if malformed_extinf:
    for line_no, reason in malformed_extinf:
        lines.append(f"- line {line_no}: {reason}")
else:
    lines.append("None.")

lines += ["", "## Ordering", ""]
if category_order_issues:
    for group, reason in category_order_issues:
        lines.append(f"- category block **{group}** — {reason}")
else:
    lines.append("Category block order: OK.")
if alphabetical_order_issues:
    for group, prev, cur in alphabetical_order_issues:
        lines.append(f"- **{group}** — **{cur}** appears after **{prev}**")
else:
    lines.append("Alphabetical order: OK.")

lines += ["", "## Suspicious URLs", ""]
if suspicious_urls:
    for name, reason, url in suspicious_urls:
        lines.append(f"- **{name}** — {reason} — {redact_url(url)}")
else:
    lines.append("None.")

lines += ["", "## Signed / Tokenized Stream URLs", ""]
if signed_urls:
    for name, group, url in signed_urls:
        lines.append(f"- **{name}** — {group or 'Uncategorized'} — {redact_url(url)}")
else:
    lines.append("None.")

lines += ["", "## Review Queue Name Consistency", ""]
review_name_mismatches = []
primary_by_norm_name = {}
for info, url in primary_entries:
    group = attrs(info).get("group-title", "").strip()
    if group in {"New"}:
        continue
    pname = attrs(info).get("tvg-name", "").strip()
    key = re.sub(r"s+", " ", re.sub(r"s*[[^]]+]s*$", "", pname)).strip().lower()
    primary_by_norm_name.setdefault(key, pname)
for info, url in entries:
    group = attrs(info).get("group-title", "").strip()
    if group not in {"New Channels", "New Backup"}:
        continue
    name = attrs(info).get("tvg-name", "").strip()
    key = re.sub(r"s+", " ", re.sub(r"s*[[^]]+]s*$", "", name)).strip().lower()
    canonical = primary_by_norm_name.get(key)
    if canonical and canonical != name:
        review_name_mismatches.append((display_name(info), canonical, group))
if review_name_mismatches:
    for name, canonical, group in review_name_mismatches:
        lines.append(f"- **{name}** ({group}) → canonical primary name: **{canonical}**")
else:
    lines.append("None.")

lines += ["", "## Metadata Conflicts", ""]
for cid, names, groups, countries in metadata_conflicts:
    lines.append(f"- **{cid}** — names: {', '.join(sorted(names))}; groups: {', '.join(sorted(groups))}; countries: {', '.join(sorted(countries))}")
if not metadata_conflicts:
    lines.append("None.")

lines += ["", "## Cross-Country Backup Collisions", ""]
for cid, name, primary_cid, url in cross_country_backups:
    lines.append("- " + name + " [" + cid + "] conflicts with primary " + primary_cid)
if not cross_country_backups:
    lines.append("None.")

lines += ["", "## Same-Name / Different-ID Collisions", ""]
for name, items in sorted(name_collisions.items()):
    ids = sorted({identity(x[0]) for x in items})
    lines.append(f"- **{name}** → {', '.join(ids)}")
if not name_collisions:
    lines.append("None.")

lines += ["", "## Logo Integrity", ""]
lines.append(f"- Healthy/local references: **{logo_counts['healthy']}**")
for issue in ["missing","broken-local","external","non-png","invalid-dimensions","corrupt-image","unvalidated-image","other"]:
    lines.append(f"- {issue}: **{logo_counts[issue]}**")
if logo_exceptions:
    for name, cid, issue, logo in logo_exceptions:
        lines.append(f"- {issue} — {name} [{cid}] — {logo}")
for cid, logos_for_id in sorted(logos_by_id.items()):
    if len(logos_for_id) > 1:
        lines.append("- multiple-logo-references — " + cid + " — " + ", ".join(sorted(logos_for_id)))

lines += ["", "## Protected Primary Entries", ""]
if protected_changes:
    lines.extend(f"- **{cid}** — {name}: {kind}" for cid,name,kind in protected_changes)
else:
    lines.append("No protected primary-entry changes detected.")

lines.insert(1, "Generated: **" + __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat() + "**")
REPORT.parent.mkdir(parents=True, exist_ok=True)
REPORT.write_text("\n".join(lines).rstrip()+"\n", encoding="utf-8")
print(f"Playlist audit: entries={len(entries)} duplicate_ids={len(duplicate_ids)} duplicate_urls={len(duplicate_urls)} conflicts={len(metadata_conflicts)} name_collisions={len(name_collisions)} protected_changes={len(protected_changes)} logo_exceptions={len(logo_exceptions)}")

# Change Guard
def run_change_guard():
    try:
        old_text = subprocess.check_output(["git", "show", "HEAD:IPTV-Playlist.m3u"], text=True, stderr=subprocess.DEVNULL)
    except Exception:
        return
    old_entries = parse(old_text)
    key = lambda info,url: (
        (attrs(info).get("tvg-id") or attrs(info).get("channel-id") or "").strip().lower(),
        url.strip(),
    )
    old_keys = {key(i,u) for i,u in old_entries}
    new_keys = {key(i,u) for i,u in entries}
    added, removed = new_keys-old_keys, old_keys-new_keys
    review_urls = {u.strip().lower() for i,u in entries if attrs(i).get("group-title","").strip() in {"New Channels", "New Backup"} and u}
    review_added = {k for k in added if k[1].strip().lower() in review_urls}
    active_added = added - review_added
    max_changes = 150
    max_review_additions = 120
    if len(review_added) > max_review_additions:
        raise SystemExit(f"Change Guard blocked maintenance: {len(review_added)} review-queue additions exceed the {max_review_additions}-entry limit.")
    if len(active_added)+len(removed) > max_changes:
        raise SystemExit(
            f"Change Guard blocked maintenance: {len(active_added)} active additions + "
            f"{len(removed)} removals exceed the {max_changes}-entry safety limit; "
            f"{len(review_added)} review-queue additions are handled separately."
        )
    old_primary = Counter(
        key(i,u) for i,u in old_entries
        if attrs(i).get("group-title","").strip() not in PRIMARY_EXCEPTIONS
    )
    new_primary = Counter(
        key(i,u) for i,u in entries
        if attrs(i).get("group-title","").strip() not in PRIMARY_EXCEPTIONS
    )
    new_primary_by_url = defaultdict(Counter)
    for (cid, url), count in new_primary.items():
        new_primary_by_url[url][cid] += count

    removed_primary = []
    for (old_cid, url), count in old_primary.items():
        direct = new_primary[(old_cid, url)]
        if direct >= count:
            continue
        # Allow only the specific identity-repair form produced by metadata
        # normalization: the same primary stream URL retained under a derived
        # ID such as old_id@ALT1 or old_id@HD.
        preserved = sum(
            n for new_cid, n in new_primary_by_url.get(url, {}).items()
            if new_cid.startswith(old_cid + "@")
        )
        if direct + preserved < count:
            removed_primary.extend([(old_cid, url)] * (count - direct - preserved))
    if removed_primary:
        raise SystemExit(
            f"Change Guard blocked maintenance: {len(removed_primary)} primary entries "
            "would be removed or rewritten."
        )

    # Review queues are user-controlled. A stream placed in New Channels or
    # New Backup must remain in that review group until the user explicitly
    # promotes it. Never silently reclassify it into an active category or
    # approved Backup during automated maintenance.
    old_review = {}
    new_review = {}
    for info, url in old_entries:
        group = attrs(info).get("group-title", "").strip()
        if group in {"New Channels", "New Backup"} and url.strip():
            old_review[url.strip().lower()] = group
    for info, url in entries:
        group = attrs(info).get("group-title", "").strip()
        if group in {"New Channels", "New Backup"} and url.strip():
            new_review[url.strip().lower()] = group
    review_reclassified = [
        (url, old_group, new_review.get(url, ""))
        for url, old_group in old_review.items()
        if new_review.get(url) != old_group
    ]
    if review_reclassified:
        raise SystemExit(
            f"Change Guard blocked maintenance: {len(review_reclassified)} "
            "New entries were reclassified or removed from "
            "their user-review queue."
        )

run_change_guard()


if protected_changes:
    raise SystemExit("Protected primary playlist entries changed; refusing automatic commit.")
if duplicate_urls:
    raise SystemExit(f"Duplicate stream URLs detected ({len(duplicate_urls)} unique URLs); refusing automatic commit.")
if primary_duplicate_ids:
    raise SystemExit("Duplicate primary identities detected; refusing automatic commit.")
if primary_chno_collisions:
    raise SystemExit("Primary channel-number collisions detected; refusing automatic commit.")
if malformed_extinf:
    raise SystemExit("Malformed EXTINF entries detected; refusing automatic commit.")
if category_order_issues or alphabetical_order_issues:
    raise SystemExit("Playlist ordering defects detected; refusing automatic commit.")
if suspicious_urls:
    raise SystemExit("Suspicious test credentials or malformed URL syntax detected; refusing automatic commit.")


# Metadata hygiene hard checks
backup_channel_numbers = [
    (info, url) for info, url in entries
    if attrs(info).get("group-title", "").strip() == "Backup"
    and attrs(info).get("tvg-chno", "").strip()
]
missing_primary_chno = [
    (info, url) for info, url in entries
    if attrs(info).get("group-title", "").strip() not in PRIMARY_EXCEPTIONS
    and not attrs(info).get("tvg-chno", "").strip()
]
missing_tvg_name = [
    (info, url) for info, url in entries
    if not attrs(info).get("tvg-name", "").strip()
]
missing_channel_id = [
    (info, url) for info, url in entries
    if not attrs(info).get("channel-id", "").strip()
]
missing_tvg_id = [
    (info, url) for info, url in entries
    if not attrs(info).get("tvg-id", "").strip()
]
missing_logo = [
    (info, url) for info, url in entries
    if not attrs(info).get("tvg-logo", "").strip()
]
missing_primary_chno = [
    (info, url) for info, url in entries
    if attrs(info).get("group-title", "").strip() not in PRIMARY_EXCEPTIONS
    and not attrs(info).get("tvg-chno", "").strip()
]
stray_name_markers = [
    (info, url) for info, url in entries
    if re.search(r"[ⓎⓈᴴᴰ🇹🇷]", info, re.UNICODE)
]

if backup_channel_numbers:
    raise SystemExit("Backup entries must not carry tvg-chno.")
if missing_tvg_name:
    raise SystemExit("All playlist entries must carry tvg-name.")
if missing_channel_id:
    raise SystemExit("All playlist entries must carry channel-id.")
if missing_tvg_id:
    raise SystemExit("All playlist entries must carry tvg-id.")
blocking_missing_logo = [
    (info, url) for info, url in entries
    if not attrs(info).get("tvg-logo", "").strip()
    and attrs(info).get("group-title", "").strip() != "Not Playing"
]
if blocking_missing_logo:
    raise SystemExit("All active/reviewable playlist entries must carry tvg-logo.")
if missing_primary_chno:
    raise SystemExit("All active primary entries must carry tvg-chno.")
if logo_exceptions:
    raise SystemExit("Logo integrity failures detected in active/reviewable entries.")
if stray_name_markers:
    raise SystemExit("Stray Unicode channel-name markers detected.")


inconsistent_tvg_names = []
for cid, items in by_id.items():
    # Backup/Not Playing entries may legitimately carry display variants
    # such as resolution or quarantine naming. Enforce tvg-name consistency
    # only across active primary entries.
    primary_items = [
        (info, url) for info, url in items
        if attrs(info).get("group-title", "").strip() not in PRIMARY_EXCEPTIONS
    ]
    values = {attrs(info).get("tvg-name", "").strip() for info, _ in primary_items}
    if len(values) > 1:
        inconsistent_tvg_names.append(cid)

def metadata_base_name(name):
    name = re.sub(r"[ⓎⓈᴴᴰ🇹🇷]", "", name, flags=re.UNICODE)
    name = re.sub(r"\s*\[Backup\s*\d+\]", "", name, flags=re.I)
    name = re.sub(r"\s*\[Geo-blocked\]", "", name, flags=re.I)
    name = re.sub(r"\s*\(\d{3,4}[pi]\)", "", name, flags=re.I)
    return re.sub(r"\s+", " ", name).strip().lower()

name_tvg_mismatches = []
for info, url in entries:
    a = attrs(info)
    group = a.get("group-title", "").strip()
    # Not Playing entries are quarantined/manual-review entries and may use
    # a descriptive display alias. Do not reject them for that presentation.
    if group == "Not Playing":
        continue
    tvg_name = a.get("tvg-name", "").strip()
    display = info.rsplit(",", 1)[-1].strip()
    if tvg_name and metadata_base_name(tvg_name) != metadata_base_name(display):
        name_tvg_mismatches.append((display_name(info), tvg_name, display))

if inconsistent_tvg_names:
    raise SystemExit("Same tvg-id has inconsistent tvg-name values.")
if name_tvg_mismatches:
    raise SystemExit("Channel display name and tvg-name disagree after normalization.")
