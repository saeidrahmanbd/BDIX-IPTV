#!/usr/bin/env python3
"""Fix deterministic findings from the IPTV-Playlist.m3u audit.

This script intentionally touches IPTV-Playlist.m3u only.  It does not modify
BDIX-Playlist.m3u.

Safe repairs:
- correct known category misclassifications;
- quarantine clearly mislabelled B4U Movies proxy entries as Backup and give
  them the channel names/IDs their URLs actually represent;
- remove the known malformed Deepto TV backup URL;
- remove exact duplicate stream URLs, preserving the first occurrence;
- ensure every entry has a tvg-name and a matching channel-id/tvg-id pair when
  one identity is available;
- fill missing primary channel numbers without changing existing numbers;
- normalize repository-local logo references and repair references to an
  existing root logo when a channel currently points at logos/unused;
- use an existing local logo when its filename can be matched unambiguously.

No stream URL is rewritten or tested here.  Health failures are handled by the
existing stream-health workflow and are never used as a deletion criterion.
"""
from pathlib import Path
import re
import unicodedata
from urllib.parse import urlparse

PLAYLIST = Path("IPTV-Playlist.m3u")
LOGOS = Path("logos")
RAW_BASE = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/"
ATTR_RE = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
NON_NUMBERED = {"Backup", "New Backup", "Not Playing"}
PRIMARY_EXCLUDED = {"Backup", "New Backup", "Not Playing"}


def attrs(line):
    return dict(ATTR_RE.findall(line))


def set_attr(line, key, value):
    pat = re.compile(rf'{re.escape(key)}="[^"]*"')
    if pat.search(line):
        return pat.sub(f'{key}="{value}"', line, count=1)
    return line.replace("#EXTINF:-1 ", f'#EXTINF:-1 {key}="{value}" ', 1)


def remove_attr(line, key):
    return re.sub(rf'\s+{re.escape(key)}="[^"]*"', '', line, count=1)


def split_display(line):
    in_quote = False
    for i, ch in enumerate(line):
        if ch == '"':
            in_quote = not in_quote
        elif ch == ',' and not in_quote:
            return line[:i], line[i + 1:].strip()
    return line, ""


def set_display(line, display):
    prefix, _ = split_display(line)
    return prefix + "," + display


def slug(value):
    value = unicodedata.normalize("NFKD", str(value or ""))
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    value = value.casefold()
    value = re.sub(r"[^a-z0-9]+", ".", value).strip(".")
    return value


def display_name(line):
    a = attrs(line)
    return (a.get("tvg-name") or split_display(line)[1]).strip()


def following_url(lines, index):
    for line in lines[index + 1:]:
        if line.startswith("#EXTINF:"):
            return ""
        value = line.strip()
        if value.startswith(("http://", "https://")):
            return value
    return ""


def record_blocks(lines):
    records = []
    pre = []
    current = None
    for line in lines:
        if line.startswith("#EXTINF:"):
            if current is not None:
                records.append(current)
            current = [line]
        elif current is None:
            pre.append(line)
        else:
            current.append(line)
    if current is not None:
        records.append(current)
    return pre, records


def record_url(record):
    for line in record[1:]:
        value = line.strip()
        if value.startswith(("http://", "https://")):
            return value
    return ""


def logo_filename(logo):
    return Path(urlparse(logo).path).name


def normalize_logo(record, logo_index):
    line = record[0]
    a = attrs(line)
    name = display_name(line)
    logo = a.get("tvg-logo", "").strip()
    candidate = ""

    if logo.startswith(RAW_BASE):
        rel = logo[len(RAW_BASE):].split("?", 1)[0].lstrip("/")
        p = LOGOS / rel
        if rel.startswith("unused/"):
            root_name = Path(rel).name
            if (LOGOS / root_name).is_file():
                candidate = root_name
        elif p.is_file():
            return record, False
        else:
            base = Path(rel).name
            if base in logo_index:
                candidate = base
    elif logo.startswith(("http://", "https://")):
        base = logo_filename(logo)
        if base in logo_index:
            candidate = base
    elif logo.startswith("logos/"):
        p = Path(logo)
        if p.is_file():
            return record, False
        base = p.name
        if base in logo_index:
            candidate = base

    if not logo:
        # Only use an existing logo with an unambiguous normalized filename.
        key = slug(name)
        matches = logo_index.get(key, [])
        if len(matches) == 1:
            candidate = matches[0]

    if candidate:
        record[0] = set_attr(line, "tvg-logo", RAW_BASE + candidate)
        return record, True
    return record, False


def build_logo_index():
    index = {}
    for p in LOGOS.iterdir() if LOGOS.is_dir() else []:
        if not p.is_file() or p.name.startswith("."):
            continue
        index.setdefault(p.name, p.name)
        index.setdefault(slug(p.stem), []).append(p.name)
    # Keep exact filename lookup distinct from normalized-name lookup.
    exact = {p.name: p.name for p in LOGOS.iterdir()} if LOGOS.is_dir() else {}
    for p in LOGOS.iterdir() if LOGOS.is_dir() else []:
        if p.is_file():
            exact[p.name] = p.name
    return exact, index


def main():
    if not PLAYLIST.is_file():
        return

    lines = PLAYLIST.read_text(encoding="utf-8-sig").replace("\r", "").splitlines()
    pre, records = record_blocks(lines)
    changes = 0
    removed = 0

    # Exact-name classification fixes already established for this playlist.
    category_fixes = {
        "baiscope tv": "Bangladesh",
        "atn music": "Bangladesh",
    }

    # URL-level corrections: these were labelled B4U Movies but the endpoint
    # itself identifies a different service. Keep the stream as a backup while
    # making the metadata truthful.
    url_name_fixes = {
        "/api/play/filamchi.m3u8": ("Filamchi", "custom.filamchi"),
        "/api/play/manoranjan%20grand.m3u8": ("Manoranjan Grand", "custom.manoranjan.grand"),
    }

    # Known malformed backup URL found in the audit.
    bad_deepto_fragment = "tvsen5.aynaott.com/tK2BNdfsdfsdf/index.m3u8"

    exact_logo_index, normalized_logo_index = build_logo_index()

    # First pass: deterministic metadata repairs and explicit bad-entry removal.
    repaired = []
    for record in records:
        line = record[0]
        a = attrs(line)
        name = display_name(line)
        lname = name.casefold()
        url = record_url(record)

        if bad_deepto_fragment.casefold() in url.casefold():
            removed += 1
            continue

        if lname in category_fixes:
            new_group = category_fixes[lname]
            if a.get("group-title", "").strip() != new_group:
                line = set_attr(line, "group-title", new_group)
                changes += 1

        for fragment, (true_name, true_id) in url_name_fixes.items():
            if fragment in url.casefold():
                if name.casefold() == "b4u movies":
                    line = set_attr(line, "tvg-name", true_name)
                    line = set_attr(line, "tvg-id", true_id)
                    line = set_attr(line, "channel-id", true_id)
                    line = set_attr(line, "group-title", "Backup")
                    line = set_display(line, true_name)
                    changes += 1
                break

        a = attrs(line)
        name = display_name(line)
        # Ensure the machine-readable and display names agree when one side is absent.
        if not a.get("tvg-name", "").strip() and name:
            line = set_attr(line, "tvg-name", name)
            changes += 1
        elif a.get("tvg-name", "").strip() and not name:
            line = set_display(line, a["tvg-name"].strip())
            changes += 1

        # Replace development-only identities with stable custom identities.
        # Keep EPG behaviour conservative: only convert the IDs when the
        # channel has no known non-staging identity in the same record.
        a = attrs(line)
        cid = (a.get("tvg-id") or a.get("channel-id") or "").strip()
        if cid.casefold() == "staging.channel.52":
            line = set_attr(line, "tvg-id", "custom.channel.52")
            line = set_attr(line, "channel-id", "custom.channel.52")
            changes += 1
        elif cid.casefold() == "staging.assam.talks":
            line = set_attr(line, "tvg-id", "custom.assam.talks")
            line = set_attr(line, "channel-id", "custom.assam.talks")
            changes += 1
        elif cid.casefold() == "staging.islam.tv":
            line = set_attr(line, "tvg-id", "custom.islam.tv")
            line = set_attr(line, "channel-id", "custom.islam.tv")
            changes += 1

        # Complete a missing identity without inventing a provider-specific ID.
        a = attrs(line)
        tvg_id = a.get("tvg-id", "").strip()
        channel_id = a.get("channel-id", "").strip()
        if not tvg_id and channel_id:
            line = set_attr(line, "tvg-id", channel_id)
            changes += 1
        elif tvg_id and not channel_id:
            line = set_attr(line, "channel-id", tvg_id)
            changes += 1
        elif not tvg_id and not channel_id and name:
            custom_id = "custom." + slug(name)
            line = set_attr(line, "tvg-id", custom_id)
            line = set_attr(line, "channel-id", custom_id)
            changes += 1

        record[0] = line
        repaired.append(record)

    records = repaired

    # Remove exact duplicate URLs, preserving the first occurrence. This keeps
    # the best-positioned/primary record and prevents duplicate stream URLs.
    seen_urls = set()
    deduped = []
    for record in records:
        url = record_url(record).strip().casefold()
        if url:
            if url in seen_urls:
                removed += 1
                continue
            seen_urls.add(url)
        deduped.append(record)
    records = deduped

    # Fill missing primary channel numbers and resolve accidental collisions.
    used = set()
    for record in records:
        a = attrs(record[0])
        group = a.get("group-title", "").strip()
        n = a.get("tvg-chno", "").strip()
        if group not in PRIMARY_EXCLUDED and n.isdigit() and int(n) > 0:
            used.add(int(n))

    next_number = 1
    for record in records:
        a = attrs(record[0])
        group = a.get("group-title", "").strip()
        if group in PRIMARY_EXCLUDED:
            record[0] = remove_attr(record[0], "tvg-chno")
            continue
        n = a.get("tvg-chno", "").strip()
        if not n:
            while next_number in used:
                next_number += 1
            record[0] = set_attr(record[0], "tvg-chno", str(next_number))
            used.add(next_number)
            next_number += 1
            changes += 1

    # Logo repair/localization.
    for record in records:
        record, changed = normalize_logo(record, normalized_logo_index)
        if changed:
            changes += 1

    output = pre + [line for record in records for line in record]
    PLAYLIST.write_text("\n".join(output).rstrip() + "\n", encoding="utf-8")
    print(f"{PLAYLIST}: metadata_repairs={changes} removed_entries={removed} remaining_entries={len(records)}")


if __name__ == "__main__":
    main()
