#!/usr/bin/env python3
"""Final deterministic fixes for IPTV-Playlist.m3u only."""
from pathlib import Path
import re
P = Path("IPTV-Playlist.m3u")
NO_NUMBER = {"Backup", "New Backup", "Not Playing"}
ATTR_RE = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
ANOMALOUS_NUMBERS = {1001, 1115, 1116, 1120}
EXPLICIT_NUMBER_FIXES = {"btv national": 39, "channel 16": 40}

def attrs(s): return dict(ATTR_RE.findall(s))
def set_attr(s, key, value):
    p = re.compile(rf'{re.escape(key)}="[^"]*"')
    replacement = f'{key}="{value}"'
    if p.search(s): return p.sub(replacement, s, count=1)
    return s.replace("#EXTINF:-1 ", f'#EXTINF:-1 {replacement} ', 1)
def remove_attr(s, key): return re.sub(rf'\s+{re.escape(key)}="[^"]*"', "", s, count=1)
def split_display(s):
    quoted = False
    for i, ch in enumerate(s):
        if ch == '"': quoted = not quoted
        elif ch == ',' and not quoted: return s[:i], s[i + 1:].strip()
    return s, ""
def name_of(info):
    a = attrs(info); return (a.get("tvg-name") or split_display(info)[1]).strip()
def url_of(block):
    for line in block[1:]:
        x = line.strip()
        if x.startswith(("http://", "https://")): return x
    return ""
def parse(text):
    pre, blocks, cur = [], [], None
    for line in text.replace("\r", "").splitlines():
        if line.startswith("#EXTINF:"):
            if cur is not None: blocks.append(cur)
            cur = [line]
        elif cur is None: pre.append(line)
        else: cur.append(line)
    if cur is not None: blocks.append(cur)
    return pre, blocks

def main():
    if not P.exists(): raise SystemExit("IPTV-Playlist.m3u not found")
    pre, blocks = parse(P.read_text(encoding="utf-8-sig"))
    changed = 0; removed_duplicates = 0
    for block in blocks:
        info = block[0]; a = attrs(info); name = name_of(info); key = name.casefold(); group = a.get("group-title", "").strip()
        if key == "btv national":
            if a.get("tvg-id") != "BTVNational.bd": info = set_attr(info, "tvg-id", "BTVNational.bd"); changed += 1
            if a.get("channel-id") != "BTVNational.bd": info = set_attr(info, "channel-id", "BTVNational.bd"); changed += 1
        if group in NO_NUMBER and a.get("tvg-chno"):
            info = remove_attr(info, "tvg-chno"); changed += 1
        if group not in NO_NUMBER and key in EXPLICIT_NUMBER_FIXES:
            desired = str(EXPLICIT_NUMBER_FIXES[key])
            if a.get("tvg-chno") != desired: info = set_attr(info, "tvg-chno", desired); changed += 1
        elif group not in NO_NUMBER and a.get("tvg-chno", "").isdigit() and int(a["tvg-chno"]) in ANOMALOUS_NUMBERS:
            info = remove_attr(info, "tvg-chno"); changed += 1
        block[0] = info
    seen = set(); kept = []
    for block in blocks:
        url = url_of(block).strip().casefold()
        if url and url in seen: removed_duplicates += 1; continue
        if url: seen.add(url)
        kept.append(block)
    blocks = kept
    used = set()
    for block in blocks:
        a = attrs(block[0]); group = a.get("group-title", "").strip(); n = a.get("tvg-chno", "").strip()
        if group not in NO_NUMBER and n.isdigit() and int(n) > 0: used.add(int(n))
    next_number = 1
    for block in blocks:
        info = block[0]; a = attrs(info); group = a.get("group-title", "").strip(); n = a.get("tvg-chno", "").strip()
        if group in NO_NUMBER or (n.isdigit() and int(n) > 0): continue
        while next_number in used: next_number += 1
        block[0] = set_attr(info, "tvg-chno", str(next_number)); used.add(next_number); next_number += 1; changed += 1
    output = [line for line in pre if line.strip()]
    for block in blocks: output.extend(block)
    P.write_text("\n".join(output).rstrip() + "\n", encoding="utf-8")
    print(f"Final IPTV fixes: changed={changed}, duplicate_streams_removed={removed_duplicates}, entries={len(blocks)}")

if __name__ == "__main__": main()
