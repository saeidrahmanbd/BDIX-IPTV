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
PRIMARY_EXCEPTIONS = {"Backup", "Not Playing"}

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

def logo_issue(info):
    logo = attrs(info).get("tvg-logo", "").strip()
    if not logo:
        return "missing"
    if logo.startswith(RAW_BASE):
        fn = logo[len(RAW_BASE):].split("?", 1)[0]
        if not fn.lower().endswith(".png"):
            return "non-png"
        path = LOGOS / fn
        if not path.is_file():
            return "broken-local"
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
    if "raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV" in logo or logo.startswith("logos/"):
        return "repository-reference"
    if logo.startswith(("http://", "https://")):
        return "external"
    return "other"

entries = parse(PLAYLIST.read_text(encoding="utf-8-sig"))
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
for info, url in entries:
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

name_collisions = {k:v for k,v in by_name.items() if len({identity(x[0]) for x in v}) > 1}

primary_by_root = defaultdict(list)
primary_by_name = defaultdict(list)
for cid, items in by_id.items():
    for info, url in items:
        if attrs(info).get("group-title", "").strip() != "Backup":
            primary_by_root[identity_root(cid)].append((cid, info, url))
            primary_by_name[normalized_name(display_name(info))].append((cid, info, url))

cross_country_backups = []
for cid, items in by_id.items():
    c = country_code(cid)
    if not c:
        continue
    for info, url in items:
        if attrs(info).get("group-title", "").strip() != "Backup":
            continue
        primary_countries_for_root = {
            country_code(primary_cid)
            for primary_cid, primary_info, primary_url
            in primary_by_root.get(identity_root(cid), [])
            if country_code(primary_cid)
        }
        if primary_countries_for_root and c not in primary_countries_for_root:
            primary_cid = next(
                primary_cid
                for primary_cid, primary_info, primary_url
                in primary_by_root.get(identity_root(cid), [])
                if country_code(primary_cid)
            )
            cross_country_backups.append((cid, display_name(info), primary_cid, url))
            continue
        if not primary_countries_for_root:
            same_name_primaries = primary_by_name.get(normalized_name(display_name(info)), [])
            name_countries = {country_code(primary_cid) for primary_cid, primary_info, primary_url in same_name_primaries if country_code(primary_cid)}
            if name_countries and c not in name_countries:
                primary_cid = same_name_primaries[0][0]
                cross_country_backups.append((cid, display_name(info), primary_cid, url))

logos_by_id = defaultdict(set)
logo_counts = Counter()
logo_exceptions = []

for info, url in entries:
    cid = identity(info)
    logo = attrs(info).get("tvg-logo", "").strip()
    if cid and logo:
        logos_by_id[cid].add(logo)
    issue = logo_issue(info)
    logo_counts["healthy" if not issue or issue == "repository-reference" else issue] += 1
    if issue in {"missing", "broken-local", "external", "non-png", "invalid-dimensions", "corrupt-image", "unvalidated-image", "other"}:
        logo_exceptions.append((display_name(info), identity(info), issue, attrs(info).get("tvg-logo","")))

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
            display_name(info).strip(),
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

    for key, count in old_primary.items():
        if new_primary[key] + new_not_playing[key] < count:
            cid, name, url = key
            protected_changes.append((cid, name, "primary entry removed or changed"))
except Exception:
    pass

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
    f"- Duplicate primary identities: **{len(primary_duplicate_ids)}**",
    f"- Primary channel-number collisions: **{len(primary_chno_collisions)}**",
    f"- Suspicious URL credentials/syntax: **{len(suspicious_urls)}**",
    "",
    "## Duplicate IDs",
    "",
]
for cid, items in sorted(duplicate_ids.items()):
    lines.append(f"### {cid} ({len(items)} streams)")
    for info, url in items:
        lines.append(f"- {display_name(info)} — {attrs(info).get('group-title','')} — {url}")
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

lines += ["", "## Suspicious URLs", ""]
if suspicious_urls:
    for name, reason, url in suspicious_urls:
        lines.append(f"- **{name}** — {reason} — {url}")
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

REPORT.parent.mkdir(parents=True, exist_ok=True)
REPORT.write_text("\n".join(lines).rstrip()+"\n", encoding="utf-8")
print(f"Playlist audit: entries={len(entries)} duplicate_ids={len(duplicate_ids)} duplicate_urls={len(duplicate_urls)} conflicts={len(metadata_conflicts)} name_collisions={len(name_collisions)} protected_changes={len(protected_changes)} logo_exceptions={len(logo_exceptions)}")

if protected_changes:
    raise SystemExit("Protected primary playlist entries changed; refusing automatic commit.")
if cross_country_backups:
    raise SystemExit("Cross-country Backup collisions detected; refusing automatic commit.")
if primary_duplicate_ids:
    raise SystemExit("Duplicate primary identities detected; refusing automatic commit.")
if primary_chno_collisions:
    raise SystemExit("Primary channel-number collisions detected; refusing automatic commit.")
if suspicious_urls:
    raise SystemExit("Suspicious test credentials or malformed URL syntax detected; refusing automatic commit.")


# Metadata hygiene hard checks
backup_channel_numbers = [
    (info, url) for info, url in entries
    if attrs(info).get("group-title", "").strip() == "Backup"
    and attrs(info).get("tvg-chno", "").strip()
]
missing_tvg_name = [
    (info, url) for info, url in entries
    if not attrs(info).get("tvg-name", "").strip()
]
missing_channel_id = [
    (info, url) for info, url in entries
    if not attrs(info).get("channel-id", "").strip()
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
if stray_name_markers:
    raise SystemExit("Stray Unicode channel-name markers detected.")


inconsistent_tvg_names = []
for cid, items in by_id.items():
    values = {attrs(info).get("tvg-name", "").strip() for info, _ in items}
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
    tvg_name = a.get("tvg-name", "").strip()
    display = info.rsplit(",", 1)[-1].strip()
    if tvg_name and metadata_base_name(tvg_name) != metadata_base_name(display):
        name_tvg_mismatches.append((display_name(info), tvg_name, display))

if inconsistent_tvg_names:
    raise SystemExit("Same tvg-id has inconsistent tvg-name values.")
if name_tvg_mismatches:
    raise SystemExit("Channel display name and tvg-name disagree after normalization.")
