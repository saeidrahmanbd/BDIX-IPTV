#!/usr/bin/env python3
"""Conservatively repair playlist metadata and review-queue duplication.

Stream URLs are never changed. The pass only normalizes channel metadata,
canonicalizes IDs when an established primary identity exists, and removes
review entries that duplicate an already-established active or higher-priority
review identity.
"""
from pathlib import Path
import re
P=Path("IPTV-Playlist.m3u")
REVIEW={"New Channels","New Backup","Not Playing"}
ACTIVE={"Bangladesh","Indian Bangla","Indian Movies","Indian Music","Indian Entertainment","Pakistani","International","Documentary & Wildlife","Kids","Religious","Sports"}
REVIEW_PRIORITY={"New Channels":3,"New Backup":2,"Not Playing":1}
ATTR=re.compile(r'([\w-]+)="([^"]*)"')
RAW_TAG=re.compile(r"\s*(?:\[[^]]*(?:geo-blocked|geo blocked)[^]]*\]|\((?:\d{3,4}p|\d{3,4}i|UHD|FHD|HD|SD)\)|\s+(?:\d{3,4}p|\d{3,4}i))\s*$",re.I)
ALIASES={"disney channel india":"Disney Channel India","disney channel (india)":"Disney Channel India","gazi tv":"G TV","g tv":"G TV","nick":"Nickelodeon (India)","nickelodeon (india)":"Nickelodeon (India)"}
def attrs(line): return dict(ATTR.findall(line))
def replace_attr(line,key,value): return re.compile(rf'{re.escape(key)}="[^"]*"').sub(f'{key}="{value}"',line,1)
def clean_name(name):
    value=RAW_TAG.sub("",name.strip()); value=re.sub(r"\s+"," ",value).strip(); return ALIASES.get(value.casefold(),value)
def canonical_id_for_name(name,active_ids): return active_ids.get(ALIASES.get(name.casefold(),name).casefold())
def main():
    text=P.read_text(encoding="utf-8-sig"); lines=text.replace("\r","").splitlines(); records=[]; current=None
    for idx,line in enumerate(lines):
        if line.startswith("#EXTINF:"): current={"idx":idx,"info":line,"attrs":attrs(line)}
        elif current and line.strip().startswith(("http://","https://")):
            current["url_idx"]=idx; current["url"]=line.strip(); records.append(current); current=None
    active_ids={}
    for r in records:
        a=r["attrs"]
        if a.get("group-title","").strip() in ACTIVE:
            name=clean_name(a.get("tvg-name","").strip()).casefold(); cid=(a.get("tvg-id") or a.get("channel-id") or "").strip()
            if name and cid: active_ids.setdefault(name,cid)
    active_id_keys={v.casefold() for v in active_ids.values()}; changed=0; removed=set(); review_seen={}
    for r in records:
        a=r["attrs"]; group=a.get("group-title","").strip(); old_name=a.get("tvg-name","").strip(); name=clean_name(old_name)
        if name!=old_name: r["info"]=replace_attr(r["info"],"tvg-name",name); changed+=1
        cid=(a.get("tvg-id") or a.get("channel-id") or "").strip(); canonical=canonical_id_for_name(name,active_ids)
        if canonical and cid and group not in ACTIVE and cid.casefold()!=canonical.casefold():
            r["info"]=replace_attr(r["info"],"tvg-id",canonical)
            if 'channel-id="' in r["info"]: r["info"]=replace_attr(r["info"],"channel-id",canonical)
            changed+=1
        key=(canonical or cid or name).casefold()
        if group in REVIEW:
            if key in active_id_keys:
                removed.update({r["idx"],r["url_idx"]}); continue
            previous=review_seen.get(key)
            if previous:
                # Keep the higher-priority queue entry. This removes legacy
                # Not Playing duplicates when the same identity is already in
                # New Backup/New Channels without touching distinct URLs for
                # the same legitimate backup identity.
                if REVIEW_PRIORITY.get(group,0)<=REVIEW_PRIORITY.get(previous,0):
                    removed.update({r["idx"],r["url_idx"]}); continue
            review_seen[key]=group
        lines[r["idx"]]=r["info"]
    if removed: lines=[line for i,line in enumerate(lines) if i not in removed]
    new="\n".join(lines)+"\n"
    if new!=text: P.write_text(new,encoding="utf-8")
    print(f"Consistency repair: metadata changes={changed}, review lines removed={len(removed)}")
if __name__=="__main__": main()
