#!/usr/bin/env python3
"""Sort one selected M3U playlist by canonical group order and A–Z name."""
from pathlib import Path
import re, sys, unicodedata

CATEGORY_ORDER=["Bangladesh","Indian Bangla","Indian Movies","Indian Music","Indian Entertainment","Pakistani","International","Documentary & Wildlife","Kids","Religious","Sports","Backup","Not Playing"]
RANK={name:i for i,name in enumerate(CATEGORY_ORDER)}
ATTR=re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')

def natural_key(value):
 value=unicodedata.normalize("NFKD",str(value or "")).casefold().strip()
 return tuple(int(p) if p.isdigit() else p for p in re.split(r"(\d+)",value))
def record_key(record):
 info=record[0]; a=dict(ATTR.findall(info)); name=(a.get("tvg-name") or info.rsplit(",",1)[-1]).strip(); group=a.get("group-title","").strip(); url=next((x.strip() for x in record[1:] if x.strip().startswith(("http://","https://"))),"")
 # Bangladesh is intentionally channel-number ordered, not alphabetical.
 if group == "Bangladesh":
  raw=a.get("tvg-chno","").strip()
  number=int(raw) if raw.isdigit() else 10**12
  return (RANK.get(group,len(RANK)),number,natural_key(name),url.casefold())
 return (RANK.get(group,len(RANK)),natural_key(name),url.casefold())
def sort_playlist(path):
 if not path.is_file(): raise SystemExit(f"Playlist not found: {path}")
 lines=path.read_text(encoding="utf-8-sig").replace("\r\n","\n").replace("\r","\n").splitlines(); preamble=[]; records=[]; current=None
 for line in lines:
  if line.startswith("#EXTINF:"):
   if current is not None: records.append(current)
   current=[line]
  elif current is not None: current.append(line)
  else: preamble.append(line)
 if current is not None: records.append(current)
 records.sort(key=record_key)
 path.write_text("\n".join(preamble+[line for rec in records for line in rec])+"\n",encoding="utf-8")
 print(f"SORTED {path}: {len(records)} records")

if __name__=="__main__":
 paths=sys.argv[1:] or ["IPTV-Playlist.m3u"]
 for name in paths: sort_playlist(Path(name))
