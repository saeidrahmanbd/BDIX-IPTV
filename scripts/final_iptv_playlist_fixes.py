#!/usr/bin/env python3
"""Final safe fixes for IPTV-Playlist.m3u only.

This pass deliberately does NOT test, replace, or remove stream URLs.
It fixes deterministic metadata/identity/number/logo issues and leaves
BDIX-Playlist.m3u untouched.
"""
from pathlib import Path
import re

P = Path("IPTV-Playlist.m3u")
RAW = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/"
NO_NUMBER = {"Backup", "New Backup", "Not Playing"}
ATTR_RE = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')

LOGO_MAP = {
    "ATN News": "atn-news.png",
    "Bangla TV": "bangla-tv.png",
    "Duronto TV": "duronto-tv.png",
    "Ekushey TV": "ekushey-tv.png",
}

# Numbers above this range are treated as obvious legacy/import anomalies.
# We do not renumber normal existing primary numbers.
ANOMALOUS_NUMBERS = {1001, 1115, 1116, 1120}


def attrs(s):
    return dict(ATTR_RE.findall(s))


def set_attr(s, key, value):
    p = re.compile(rf'{re.escape(key)}="[^"]*"')
    replacement = f'{key}="{value}"'
    if p.search(s):
        return p.sub(replacement, s, count=1)
    return s.replace("#EXTINF:-1 ", f'#EXTINF:-1 {replacement} ', 1)


def remove_attr(s, key):
    return re.sub(rf'\s+{re.escape(key)}="[^"]*"', "", s, count=1)


def split_display(s):
    quoted = False
    for i, ch in enumerate(s):
        if ch == '"':
            quoted = not quoted
        elif ch == ',' and not quoted:
            return s[:i], s[i + 1:].strip()
    return s, ""


def set_display(s, name):
    return split_display(s)[0] + "," + name


def name_of(info):
    a = attrs(info)
    return (a.get("tvg-name") or split_display(info)[1]).strip()


def url_of(block):
    for line in block[1:]:
        x = line.strip()
        if x.startswith(("http://", "https://")):
            return x
    return ""


def parse(text):
    pre, blocks, cur = [], [], None
    for line in text.replace("\r", "").splitlines():
        if line.startswith("#EXTINF:"):
            if cur is not None:
                blocks.append(cur)
            cur = [line]
        elif cur is None:
            pre.append(line)
        else:
            cur.append(line)
    if cur is not None:
        blocks.append(cur)
    return pre, blocks


def main():
    if not P.exists():
        raise SystemExit("IPTV-Playlist.m3u not found")

    pre, blocks = parse(P.read_text(encoding="utf-8-sig"))
    changed = 0
    removed_duplicates = 0

    # First pass: deterministic metadata corrections only.
    for block in blocks:
        info = block[0]
        a = attrs(info)
        name = name_of(info)
        group = a.get("group-title", "").strip()

        # Canonicalize the BTV National identity used by the IPTV playlist.
        if name.casefold() == "btv national" and a.get("tvg-id") == "custom.btv.national":
            info = set_attr(info, "tvg-id", "BTVNational.bd")
            info = set_attr(info, "channel-id", "BTVNational.bd")
            changed += 1

        # Remove the known obsolete NVision-generated logo references when a
        # verified canonical local asset exists in the repository.
        if name in LOGO_MAP and ("nvisionbd-verified-" in a.get("tvg-logo", "").casefold()):
            info = set_attr(info, "tvg-logo", RAW + LOGO_MAP[name])
            changed += 1

        # Backup/review groups never receive primary channel numbers.
        if group in NO_NUMBER and a.get("tvg-chno"):
            info = remove_attr(info, "tvg-chno")
            changed += 1

        # Replace only clearly anomalous legacy/import numbers. The next pass
        # assigns the lowest unused positive primary number.
        n = a.get("tvg-chno", "").strip()
        if group not in NO_NUMBER and n.isdigit() and int(n) in ANOMALOUS_NUMBERS:
            info = remove_attr(info, "tvg-chno")
            changed += 1

        block[0] = info

    # Remove exact duplicate stream URLs while preserving the first occurrence.
    seen = set()
    kept = []
    for block in blocks:
        url = url_of(block).strip().casefold()
        if url and url in seen:
            removed_duplicates += 1
            continue
        if url:
            seen.add(url)
        kept.append(block)
    blocks = kept

    # Assign only the anomalous/missing primary numbers, without disturbing
    # existing valid numbering.
    used = set()
    for block in blocks:
        a = attrs(block[0])
        group = a.get("group-title", "").strip()
        n = a.get("tvg-chno", "").strip()
        if group not in NO_NUMBER and n.isdigit() and int(n) > 0:
            used.add(int(n))

    next_number = 1
    for block in blocks:
        info = block[0]
        a = attrs(info)
        group = a.get("group-title", "").strip()
        n = a.get("tvg-chno", "").strip()
        if group in NO_NUMBER:
            continue
        if n.isdigit() and int(n) > 0:
            continue
        while next_number in used:
            next_number += 1
        block[0] = set_attr(info, "tvg-chno", str(next_number))
        used.add(next_number)
        next_number += 1
        changed += 1

    output = []
    for line in pre:
        if line.strip():
            output.append(line)
    for block in blocks:
        output.extend(block)

    P.write_text("\n".join(output).rstrip() + "\n", encoding="utf-8")
    print(f"Final IPTV fixes: changed={changed}, duplicate_streams_removed={removed_duplicates}, entries={len(blocks)}")


if __name__ == "__main__":
    main()
