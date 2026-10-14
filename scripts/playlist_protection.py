#!/usr/bin/env python3
"""Final playlist protection checks.

This guard is intentionally fail-closed: maintenance automation must not publish
an IPTV playlist unless the canonical category blocks and metadata invariants
remain intact. It also keeps Backup as a terminal block.
"""
from pathlib import Path
import re
import unicodedata

PLAYLIST = Path("IPTV-Playlist.m3u")
CATEGORIES = ["Bangladesh", "Indian Bangla", "Indian Movies", "Indian Music", "Indian Entertainment", "Pakistani", "International", "Documentary & Wildlife", "Kids", "Religious", "Sports", "Backup", "New Channels", "New Backup", "Not Playing"]
PRIMARY_EXCEPTIONS = {"Backup", "New Backup", "Not Playing"}
ATTR_RE = re.compile(r'([\w-]+)="([^"]*)"')

def attrs(line):
    return dict(ATTR_RE.findall(line))

def sort_key(value):
    value = unicodedata.normalize("NFKD", value).casefold().strip()
    return [int(x) if x.isdigit() else x for x in re.split(r"(\d+)", value)]

def parse():
    lines = PLAYLIST.read_text(encoding="utf-8").replace("\r", "").splitlines()
    entries=[]
    for i,line in enumerate(lines):
        if not line.startswith("#EXTINF:"): continue
        a=attrs(line); url=""
        for v in lines[i+1:]:
            v=v.strip()
            if v.startswith("#EXTINF:"): break
            if v.startswith(("http://","https://")): url=v; break
        entries.append((a,url))
    return entries

def main():
    entries=parse(); errors=[]
    transitions=[]; last=None
    for a,_ in entries:
        g=a.get("group-title","").strip()
        if g!=last: transitions.append(g); last=g
    last_index=-1
    for g in transitions:
        if g not in CATEGORIES: errors.append(f"unknown category: {g}"); continue
        idx=CATEGORIES.index(g)
        if idx<last_index: errors.append(f"category out of order: {g}")
        last_index=max(last_index,idx)
    # Every category is one contiguous block.
    seen={}
    for g in transitions: seen[g]=seen.get(g,0)+1
    for g,n in seen.items():
        if n>1: errors.append(f"category split into {n} blocks: {g}")
    # A-Z within every block.
    for g in CATEGORIES:
        names=[a.get("tvg-name","").strip() for a,_ in entries if a.get("group-title","").strip()==g]
        if names and names!=sorted(names,key=sort_key): errors.append(f"not A-Z: {g}")
    # Primary channel numbers are mandatory and unique; Backup is unnumbered.
    primary=[a for a,_ in entries if a.get("group-title","").strip() not in PRIMARY_EXCEPTIONS]
    missing=[a.get("tvg-name","") for a in primary if not a.get("tvg-chno","").strip()]
    nums=[a.get("tvg-chno","").strip() for a in primary]
    dup=sorted({n for n in nums if n and nums.count(n)>1},key=sort_key)
    if missing: errors.append(f"primary entries missing tvg-chno: {missing[:10]}")
    if dup: errors.append(f"duplicate primary tvg-chno: {dup}")
    if any(a.get("tvg-chno","").strip() for a,_ in entries if a.get("group-title","").strip() in {"Backup","New Backup","Not Playing"}): errors.append("non-primary category contains tvg-chno")
    # Ultimate TV must remain one canonical identity/category.
    ult=[a.get("group-title","").strip() for a,_ in entries if a.get("tvg-id","").strip().casefold()=="ultimatetv.in@sd"]
    if len(set(ult))>1: errors.append("ultimatetv.in@sd appears in multiple groups")
    if errors:
        for e in errors: print("BLOCK:",e)
        raise SystemExit(1)
    print(f"PASS: {len(entries)} entries; {len(primary)} numbered primary entries; category order, A-Z order, numbering, Backup isolation and identity guard passed.")

if __name__ == "__main__": main()
