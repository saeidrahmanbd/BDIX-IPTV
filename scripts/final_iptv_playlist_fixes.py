#!/usr/bin/env python3
"""Final deterministic fixes for IPTV-Playlist.m3u only.

This pass deliberately does NOT test, replace, or remove stream URLs.
It fixes deterministic metadata/identity/number issues and leaves
BDIX-Playlist.m3u untouched.
"""
from pathlib import Path
import re

P = Path("IPTV-Playlist.m3u")
NO_NUMBER = {"Backup", "New Backup", "Not Playing"}
ATTR_RE = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')

# These are the four specific legacy/import numbers identified by the deep
# audit. They are replaced with the first four unused numbers after the normal
# Bangladesh primary block. We do not renumber otherwise-valid entries.
ANOMALOUS_NUMBERS = {1001, 1115, 1116, 1120}
EXPLICIT_NUMBER_FIXES = {
    "btv national": 39,
    "channel 16": 40,
    "duronto tv": 41,
    "channel s uk": 42,
}


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

    # First pass: deterministic metadata and identity corrections only.
    for block in blocks:
        info = block[0]
        a = attrs(info)
        name = name_of(info)
        key = name.casefold()
        group = a.get("group-title", "").strip()

        # Canonicalize BTV National identity while preserving its exact stream.
        if key == "btv national":
            if a.get("tvg-id") != "BTVNational.bd":
                info = set_attr(info, "tvg-id", "BTVNational.bd")
                changed += 1
            if a.get("channel-id") != "BTVNational.bd":
                info = set_attr(info, "channel-id", "BTVNational.bd")
                changed += 1

        # Backup/review groups never receive primary channel numbers.
        if group in NO_NUMBER and a.get("tvg-chno"):
            info = remove_attr(info, "tvg-chno")
            changed += 1

        # Apply the four explicit numbering corrections. These names are
        # intentionally mapped rather than assigning numbers based on file
        # position, so future playlist sorting cannot change their identity.
        if group not in NO_NUMBER and key in EXPLICIT_NUMBER_FIXES:
            desired = str(EXPLICIT_NUMBER_FIXES[key])
            if a.get("tvg-chno") != desired:
                info = set_attr(info, "tvg-chno", desired)
                changed += 1
        else:
            # Remove only the previously identified anomalous/import numbers;
            # valid existing numbering remains untouched.
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

    output = [line for line in pre if line.strip()]
    for block in blocks:
        output.extend(block)
    P.write_text("\n".join(output).rstrip() + "\n", encoding="utf-8")
    print(f"Final IPTV fixes: changed={changed}, duplicate_streams_removed={removed_duplicates}, entries={len(blocks)}")


if __name__ == "__main__":
    main()
