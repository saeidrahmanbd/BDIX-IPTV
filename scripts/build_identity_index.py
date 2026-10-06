#!/usr/bin/env python3
"""Build a canonical channel identity index without modifying the playlist."""
import json,re
from collections import defaultdict
from datetime import datetime,timezone
from pathlib import Path
PLAYLIST=Path("IPTV-Playlist.m3u"); OUT=Path("reports/channel-identity-index.json")
ATTR=re.compile(r'([\w-]+)="([^"]*)"')
EXCLUDE={"New","New Channels","New Backup","Not Playing"}
def attrs(s): return dict(ATTR.findall(s))
def root(cid):
    cid=(cid or "").strip().lower().split("@",1)[0]
    return re.sub(r"\.[a-z]{2}$","",cid)
def main():
    lines=PLAYLIST.read_text(encoding="utf-8-sig").splitlines(); cur=None
    index=defaultdict(lambda:{"names":set(),"ids":set(),"groups":set(),"streams":0,"primary":0,"backup":0})
    for line in lines:
        if line.startswith("#EXTINF:"):
            cur=attrs(line); cur["_name"]=(cur.get("tvg-name") or line.rsplit(",",1)[-1]).strip()
        elif cur and line.strip().startswith(("http://","https://")):
            cid=(cur.get("tvg-id") or cur.get("channel-id") or "").strip().lower()
            if cid:
                r=index[root(cid)]; r["names"].add(cur["_name"]); r["ids"].add(cid); r["groups"].add(cur.get("group-title","").strip()); r["streams"]+=1
                if cur.get("group-title","").strip()=="Backup": r["backup"]+=1
                elif cur.get("group-title","").strip() not in EXCLUDE: r["primary"]+=1
            cur=None
    clean={k:{**v,"names":sorted(v["names"]),"ids":sorted(v["ids"]),"groups":sorted(v["groups"])} for k,v in sorted(index.items())}
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps({"generated":datetime.now(timezone.utc).isoformat(timespec="seconds"),"channels":clean},indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(f"Identity index: {len(clean)} canonical roots")
if __name__=="__main__": main()
