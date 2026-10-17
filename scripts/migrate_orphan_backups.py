#!/usr/bin/env python3
"""Migrate confirmed orphan Backup streams into their canonical primary groups."""
from pathlib import Path
import re

P = Path("IPTV-Playlist.m3u")
ATTR_RE = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
MIGRATIONS = {
    "7X Punjabi": ("Indian Music", "1214"),
    "Bangla Cinema": ("Indian Bangla", "1215"),
    "Oscar Movies Bhojpuri": ("Indian Movies", "1216"),
    "PTV Sports": ("Sports", "1217"),
    "Sony Aath": ("Indian Bangla", "1218"),
    "Star Gold": ("Indian Movies", "1219"),
}


def attrs(line):
    return dict(ATTR_RE.findall(line))


def set_attr(line, key, value):
    pat = re.compile(rf'{re.escape(key)}="[^"]*"')
    if pat.search(line):
        return pat.sub(f'{key}="{value}"', line, count=1)
    comma = line.find(",")
    if comma >= 0:
        return line[:comma] + f' {key}="{value}"' + line[comma:]
    return line + f' {key}="{value}"'


def main():
    lines = P.read_text(encoding="utf-8-sig").replace("\r", "").splitlines()
    changed = []
    used_numbers = set()
    for line in lines:
        if line.startswith("#EXTINF:"):
            a = attrs(line)
            n = a.get("tvg-chno", "").strip()
            if n.isdigit():
                used_numbers.add(int(n))

    for i, line in enumerate(lines):
        if not line.startswith("#EXTINF:"):
            continue
        a = attrs(line)
        name = a.get("tvg-name", "").strip()
        if a.get("group-title", "").strip() != "Backup" or name not in MIGRATIONS:
            continue
        target_group, preferred = MIGRATIONS[name]
        number = int(preferred)
        while number in used_numbers:
            number += 1
        lines[i] = set_attr(line, "group-title", target_group)
        lines[i] = set_attr(lines[i], "tvg-chno", str(number))
        used_numbers.add(number)
        changed.append((name, target_group, number))

    # Keep canonical category order and alphabetical order inside each category.
    order = [
        "Bangladesh", "Indian Bangla", "Indian Movies", "Indian Music",
        "Indian Entertainment", "Pakistani", "International",
        "Documentary & Wildlife", "Kids", "Religious", "Sports", "Backup",
        "Not Playing",
    ]
    rank = {name: i for i, name in enumerate(order)}
    blocks, pre, cur = [], [], None
    for line in lines:
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

    def name_of(block):
        a = attrs(block[0])
        return a.get("tvg-name", block[0].rsplit(",", 1)[-1]).strip().casefold()

    blocks.sort(key=lambda b: (rank.get(attrs(b[0]).get("group-title", ""), 999), name_of(b)))
    out = pre[:]
    for block in blocks:
        out.extend(block)
    P.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")
    print("Orphan backup migration:", ", ".join(f"{n} -> {g} #{num}" for n, g, num in changed))
    if len(changed) != 6:
        raise SystemExit(f"Expected 6 orphan migrations, performed {len(changed)}")


if __name__ == "__main__":
    main()
# one-time trigger marker
