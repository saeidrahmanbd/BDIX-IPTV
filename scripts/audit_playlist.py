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

PLAYLIST = Path("IPTV Playlist.m3u")
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
    m = re.search(r"\.([a-z]{2})$", base_id(cid))
    return m.group(1).lower() if m else ""

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

metadata_conflicts = []
for cid, items in sorted(by_id.items()):
    if len(items) < 2:
        continue
    names = {display_name(x[0]) for x in items}
    groups = {attrs(x[0]).get("group-title", "") for x in items}
    countries = {attrs(x[0]).get("tvg-country", "") for x in items}
    if len(names) > 1 or len(groups) > 1 or len(countries) > 1:
        metadata_conflicts.append((cid, names, groups, countries))

name_collisions = {k:v for k,v in by_name.items() if len({identity(x[0]) for x in v}) > 1}

primary_by_root = defaultdict(list)
for cid, items in by_id.items():
    for info, url in items:
        if attrs(info).get("group-title", "").strip() != "Backup":
            primary_by_root[identity_root(cid)].append((cid, info, url))

cross_country_backups = []
for cid, items in by_id.items():
    c = country_code(cid)
    if not c:
        continue
    for info, url in items:
        if attrs(info).get("group-title", "").strip() != "Backup":
            continue
        for primary_cid, primary_info, primary_url in primary_by_root.get(identity_root(cid), []):
            pc = country_code(primary_cid)
            if pc and c != pc:
                cross_country_backups.append((cid, display_name(info), primary_cid, url))
                break

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
    old = subprocess.check_output(["git", "show", "HEAD:IPTV Playlist.m3u"], text=True, stderr=subprocess.DEVNULL)
    old_primary = Counter()
    new_primary = Counter()

    def stable(info, url):
        a = attrs(info)
        return (
            (a.get("tvg-id") or a.get("channel-id") or "").strip().lower(),
            a.get("group-title", "").strip(),
            display_name(info).strip(),
            url.strip(),
        )

    for info, url in parse(old):
        if attrs(info).get("group-title", "").strip() not in PRIMARY_EXCEPTIONS:
            old_primary[stable(info, url)] += 1
    for info, url in entries:
        if attrs(info).get("group-title", "").strip() not in PRIMARY_EXCEPTIONS:
            new_primary[stable(info, url)] += 1

    for key, count in old_primary.items():
        if new_primary[key] < count:
            cid, group, name, url = key
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
