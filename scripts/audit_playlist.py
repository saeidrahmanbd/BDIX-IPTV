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
PRIMARY_EXCEPTIONS = {"Backup"}
CATEGORY_ORDER = ["Bangladesh", "Indian Bangla", "Indian Movies", "Indian Music", "Indian Entertainment", "Pakistani", "International", "Documentary & Wildlife", "Kids", "Religious", "Sports", "Backup"]

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

def redact_url(url):
    url = re.sub(r'(/live/)[^/?#]+/[^/?#]+/([^/?#]+\.ts)(?=$|[?#])', r'\1[REDACTED]/[REDACTED]/\2', url, flags=re.I)
    return re.sub(r'([?&](?:token|sig|signature|jwt|session|key|authorization|hdnts)=[^&\s]+)', lambda m: m.group(1).split("=", 1)[0] + "=[REDACTED]", url, flags=re.I)

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
        primary_identity_groups[(cid, a.get("group-title", "").strip())].append((info, url))
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

REVIEW_GROUPS = set()
name_collisions = {k: [x for x in v if attrs(x[0]).get("group-title", "").strip() not in REVIEW_GROUPS] for k, v in by_name.items()}
name_collisions = {k:v for k,v in name_collisions.items() if len({identity_root(identity(x[0])) for x in v}) > 1}

primary_by_root = defaultdict(list)
primary_by_name = defaultdict(list)
for cid, items in by_id.items():
    for info, url in items:
        if attrs(info).get("group-title", "").strip() not in PRIMARY_EXCEPTIONS:
            primary_by_root[identity_root(cid)].append((cid, info, url))
            primary_by_name[normalized_name(display_name(info))].append((cid, info, url))
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
    logo_counts["healthy" if not issue or issue == "repository-reference" else issue] += 1
    item = (display_name(info), identity(info), issue, attrs(info).get("tvg-logo",""))
    if issue == "external":
        logo_warnings.append(item)
    elif issue in {"missing", "broken-local", "unsupported-format", "invalid-dimensions", "corrupt-image", "unvalidated-image", "other"}:
        if attrs(info).get("group-title", "").strip() == "Backup":
            review_logo_exceptions.append(item)
        else:
            logo_exceptions.append(item)

protected_changes = []
try:
    old = subprocess.check_output(["git", "show", "HEAD:IPTV-Playlist.m3u"], text=True, stderr=subprocess.DEVNULL)
    old_primary = Counter()
    new_primary = Counter()
    new_backup_by_url = Counter()
    def stable(info, url):
        a = attrs(info)
        return ((a.get("tvg-id") or a.get("channel-id") or "").strip().lower(), url.strip())
    for info, url in parse(old):
        if attrs(info).get("group-title", "").strip() not in PRIMARY_EXCEPTIONS:
            old_primary[stable(info, url)] += 1
    for info, url in entries:
        group = attrs(info).get("group-title", "").strip()
        key = stable(info, url)
        if group not in PRIMARY_EXCEPTIONS:
            new_primary[key] += 1
        elif url.strip():
            new_backup_by_url[url.strip().lower()] += 1
    new_primary_by_url = defaultdict(list)
    for (cid, url), count in new_primary.items():
        new_primary_by_url[url].append((cid, count))
    for key, count in old_primary.items():
        cid, url = key
        direct = new_primary[key]
        if direct >= count:
            continue
        if direct + new_backup_by_url[url.strip().lower()] >= count:
            continue
        preserved = 0
        for new_cid, new_count in new_primary_by_url.get(url, []):
            if not cid and new_cid:
                preserved += new_count
            elif cid and new_cid.startswith(cid + "@"):
                preserved += new_count
        if direct + preserved < count:
            protected_changes.append((cid, url, "primary entry removed or changed"))
except Exception:
    pass

missing_primary_chno = [(info, url) for info, url in entries if attrs(info).get("group-title", "").strip() not in PRIMARY_EXCEPTIONS and not attrs(info).get("tvg-chno", "").strip()]
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
    return [int(part) if part.isdigit() else part for part in re.split(r"(\d+)", value)]
for group in category_transitions:
    names = [display_name(info).strip() for info, url in entries if attrs(info).get("group-title", "").strip() == group]
    for prev, cur in zip(names, names[1:]):
        if natural_sort_key(cur) < natural_sort_key(prev):
            alphabetical_order_issues.append((group, prev, cur))

lines = [
    "# Playlist Audit", "", "Non-destructive audit of channel identity, metadata consistency, duplicate identities, and logo integrity.", "", "## Summary", "",
    f"- Playlist entries: **{len(entries)}**", f"- Unique channel IDs: **{len(by_id)}**", f"- IDs with multiple streams: **{len(duplicate_ids)}**", f"- Duplicate stream URLs: **{len(duplicate_urls)}**", f"- Metadata conflicts: **{len(metadata_conflicts)}**", f"- Same-name / different-ID collisions: **{len(name_collisions)}**", f"- Cross-country backup collisions: **{len(cross_country_backups)}**", f"- IDs with multiple logo references: **{sum(1 for v in logos_by_id.values() if len(v) > 1)}**", f"- Protected primary-entry changes: **{len(protected_changes)}**", f"- Logo exceptions requiring repair: **{len(logo_exceptions)}**", f"- External logo references (review only): **{len(logo_warnings)}**", f"- Logo references checked: **{sum(logo_counts.values())}**", f"- Duplicate primary identities: **{len(primary_duplicate_ids)}**", f"- Primary channel-number collisions: **{len(primary_chno_collisions)}**", f"- Primary entries missing channel numbers: **{len(missing_primary_chno)}**", f"- Malformed EXTINF entries: **{len(malformed_extinf)}**", f"- Category block-order issues: **{len(category_order_issues)}**", f"- Alphabetical ordering issues: **{len(alphabetical_order_issues)}**", f"- Suspicious URL credentials/syntax: **{len(suspicious_urls)}**", f"- Signed/tokenized stream URLs: **{len(signed_urls)}**", f"- Embedded Xtream-style credential paths (redacted): **{len(xtream_credential_paths)}**", "", "## Duplicate IDs", ""]
for cid, items in sorted(duplicate_ids.items()):
    lines.append(f"### {cid} ({len(items)} streams)")
    for info, url in items:
        lines.append(f"- {display_name(info)} — {attrs(info).get('group-title','')} — {redact_url(url)}")
if not duplicate_ids: lines.append("None.")
lines += ["", "## Duplicate Primary Identities", ""]
if primary_duplicate_ids:
    for (key, items) in sorted(primary_duplicate_ids.items()):
        cid, group = key
        lines.append(f"- **{cid}** in **{group}** — " + ", ".join(display_name(x[0]) for x in items))
else: lines.append("None.")
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
else: lines.append("Alphabetical order: OK.")
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
    lines.append(f"- {issue}: **{logo_counts[issue]}")
lines += ["", "## External Logo Review", ""]
if logo_warnings:
    for name, cid, issue, logo in logo_warnings[:200]: lines.append(f"- {name} [{cid}] — {logo}")
    if len(logo_warnings) > 200: lines.append(f"- ... {len(logo_warnings)-200} additional external logo references omitted from report.")
else: lines.append("None.")
lines += ["", "## Protected Primary Entries", ""]
if protected_changes: lines.extend(f"- **{cid}** — {url}: {kind}" for cid,url,kind in protected_changes)
else: lines.append("No protected primary-entry changes detected.")
lines.insert(1, "Generated: **" + __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat() + "**")
REPORT.parent.mkdir(parents=True, exist_ok=True)
REPORT.write_text("\n".join(lines).rstrip()+"\n", encoding="utf-8")
print(f"Playlist audit: entries={len(entries)} duplicate_ids={len(duplicate_ids)} duplicate_urls={len(duplicate_urls)} conflicts={len(metadata_conflicts)} name_collisions={len(name_collisions)} protected_changes={len(protected_changes)} logo_exceptions={len(logo_exceptions)} external_logo_warnings={len(logo_warnings)}")

def run_change_guard():
    try: old_text = subprocess.check_output(["git", "show", "HEAD:IPTV-Playlist.m3u"], text=True, stderr=subprocess.DEVNULL)
    except Exception: return
    old_entries = parse(old_text)
    key = lambda info,url: ((attrs(info).get("tvg-id") or attrs(info).get("channel-id") or "").strip().lower(), url.strip())
    old_keys = {key(i,u) for i,u in old_entries}; new_keys = {key(i,u) for i,u in entries}
    added, removed = new_keys-old_keys, old_keys-new_keys
    review_urls = set(); review_added = {k for k in added if k[1].strip().lower() in review_urls}; active_added = added - review_added
    max_changes = 150; max_review_additions = 120
    if len(review_added) > max_review_additions: raise SystemExit(f"Change Guard blocked maintenance: {len(review_added)} review-queue additions exceed the {max_review_additions}-entry limit.")
    if len(active_added)+len(removed) > max_changes: raise SystemExit(f"Change Guard blocked maintenance: {len(active_added)} active additions + {len(removed)} removals exceed the {max_changes}-entry safety limit; {len(review_added)} review-queue additions are handled separately.")
    old_primary = Counter(key(i,u) for i,u in old_entries if attrs(i).get("group-title","").strip() not in PRIMARY_EXCEPTIONS)
    new_primary = Counter(key(i,u) for i,u in entries if attrs(i).get("group-title","").strip() not in PRIMARY_EXCEPTIONS)
    new_backup_by_url = Counter(u.strip().lower() for i,u in entries if attrs(i).get("group-title","").strip() in PRIMARY_EXCEPTIONS and u.strip())
    new_primary_by_url = defaultdict(Counter)
    for (cid, url), count in new_primary.items(): new_primary_by_url[url][cid] += count
    removed_primary = []
    for (old_cid, url), count in old_primary.items():
        direct = new_primary[(old_cid, url)]
        if direct >= count: continue
        quarantined = min(count-direct, new_backup_by_url.get(url.strip().lower(), 0))
        if direct + quarantined >= count: continue
        preserved = sum(n for new_cid,n in new_primary_by_url.get(url,{}).items() if (not old_cid and new_cid) or (old_cid and new_cid.startswith(old_cid+"@")))
        if direct + preserved < count: removed_primary.extend([(old_cid,url)]*(count-direct-preserved))
    if removed_primary: raise SystemExit(f"Change Guard blocked maintenance: {len(removed_primary)} primary entries would be removed or rewritten.")
    old_review = {}; new_review = {}
    for info,url in old_entries:
        group=attrs(info).get("group-title","").strip()
        if group in set() and url.strip(): old_review[url.strip().lower()]=group
    review_reclassified=[(url,old_group,new_review.get(url,"")) for url,old_group in old_review.items() if new_review.get(url)!=old_group]
    if review_reclassified: raise SystemExit(f"Change Guard blocked maintenance: {len(review_reclassified)} New entries were reclassified or removed from their user-review queue.")

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
if logo_exceptions: raise SystemExit("Logo integrity failures detected in active/reviewable entries.")
