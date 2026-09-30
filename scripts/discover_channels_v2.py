#!/usr/bin/env python3
from __future__ import annotations
import json, unicodedata, urllib.request
from pathlib import Path
from urllib.parse import urlparse

PLAYLIST=Path("IPTV-Playlist.m3u")
REPORT=Path("reports/channel-discovery.md")
SOURCES=[("Bangladesh","https://iptv-org.github.io/iptv/countries/bd.m3u"),("India","https://iptv-org.github.io/iptv/countries/in.m3u")]
BLOCKED={"sports","religious","kids"}
INDIA_OK={"music","movies","movie"}
BAD_WORDS=("vod","catchup","catch-up","test","demo","proxy","proxied","cors","webcam","radio","podcast","event","ppv","24/7","timeshift")
BAD_HOSTS=("proxy","proxied","cors","localhost","workers.dev","worker.dev","pages.dev")
BAD_QUERY=("token=","auth=","authorization=","hdnts=","sig=","signature=","expires=","session=","jwt=","key=")

def attrs(line):
    out={}
    for part in line.split(" "):
        if "=" in part:
            k,v=part.split("=",1)
            if v.startswith('"') and v.endswith('"'): out[k]=v[1:-1]
    return out

def norm(s):
    s=" ".join(s.lower().split())
    for l,r in (("(",")"),("[","]")):
        if s.endswith(r) and l in s: s=s[:s.rfind(l)].strip()
    return "".join(c for c in s if c.isalnum() or unicodedata.category(c).startswith("L"))

def parse(text):
    lines=text.replace("\r","").splitlines(); out=[]; i=0
    while i<len(lines):
        if lines[i].startswith("#EXTINF"):
            j=i+1
            while j<len(lines) and not lines[j].strip(): j+=1
            if j<len(lines) and lines[j].startswith(("http://","https://")):
                a=attrs(lines[i]); n=a.get("tvg-name") or lines[i].rsplit(",",1)[-1].strip()
                out.append((a,n.strip(),lines[j].strip())); i=j
        i+=1
    return out

def cats(a):
    s=set()
    for k in ("group-title","category","categories"):
        s.update(x.strip().lower() for x in a.get(k,"").replace("; ",",").replace("|",",").split(",") if x.strip())
    return s

def ok(country,a,n,u):
    c=cats(a); h=" ".join((n,a.get("tvg-id",""),a.get("group-title",""),a.get("category",""))).lower()
    if c&BLOCKED or any(x in h for x in BAD_WORDS): return False
    if country=="India" and ("news" in c or not c&INDIA_OK): return False
    p=urlparse(u)
    if p.scheme not in ("http","https") or not p.netloc or p.query or p.fragment: return False
    if any(x in u.lower() for x in BAD_QUERY) or any(x in p.netloc.lower() for x in BAD_HOSTS): return False
    return p.path.lower().endswith((".m3u8",".m3u",".ts")) and "vod" not in p.path.lower() and "catchup" not in p.path.lower()

def ext(a,n,g):
    cid=(a.get("tvg-id") or a.get("channel-id") or "").strip()
    if not cid: return None
    x=[f'#EXTINF:-1 tvg-id="{cid}" tvg-name="{n}"']
    if a.get("tvg-logo"): x[0]+=f' tvg-logo="{a["tvg-logo"].strip()}"'
    x[0]+=f' channel-id="{a.get("channel-id",cid).strip()}" group-title="{g}"'
    return x[0]+","+n

def main():
    original=PLAYLIST.read_text(encoding="utf-8-sig"); entries=parse(original)
    pairs={(norm(n),u) for a,n,u in entries}; names={norm(n) for a,n,u in entries}
    cand=[]; rejected=0
    for country,src in SOURCES:
        try:
            req=urllib.request.Request(src,headers={"User-Agent":"BDIX-IPTV-discovery/1.0"})
            text=urllib.request.urlopen(req,timeout=30).read().decode("utf-8","replace")
        except Exception as e:
            print("Source unavailable:",src,e); continue
        for a,n,u in parse(text):
            if ok(country,a,n,u) and (norm(n),u) not in pairs: cand.append((country,a,n,u))
            elif not ok(country,a,n,u): rejected+=1
    cand.sort(key=lambda x:(x[0]!="Bangladesh",norm(x[2]),x[3]))
    new=[]; backups=[]; planned=set(names); seen=set(pairs)
    for country,a,n,u in cand:
        pair=(norm(n),u)
        if pair in seen: continue
        if norm(n) in planned: backups.append((country,a,n,u))
        else: new.append((country,a,n,u)); planned.add(norm(n))
        seen.add(pair)
    new=new[:40]; backups=backups[:80]
    lines=original.replace("\r","").splitlines(); additions=[]
    for c,a,n,u in new:
        z=ext(a,n,"New Channels")
        if z: additions += [z,u]
    for c,a,n,u in backups:
        z=ext(a,n,"New Backup")
        if z: additions += [z,u]
    if additions:
        pos=next((i for i,l in enumerate(lines) if l.startswith("#EXTINF") and 'group-title="Backup"' in l),len(lines))
        lines[pos:pos]=additions
        for i,l in enumerate(lines):
            if l.startswith("#PLAYLIST-STUDIO-CATEGORIES:"):
                cs=json.loads(l.split(":",1)[1])
                for g in ("New Channels","New Backup"):
                    if g not in cs: cs.insert(cs.index("Backup") if "Backup" in cs else len(cs),g)
                lines[i]="#PLAYLIST-STUDIO-CATEGORIES:"+json.dumps(cs,ensure_ascii=False); break
        PLAYLIST.write_text("\n".join(lines)+"\n",encoding="utf-8")
    REPORT.parent.mkdir(parents=True,exist_ok=True)
    REPORT.write_text("# Channel Discovery\n\n"+f"- New channels: **{len(new)}**\n- New backups: **{len(backups)}**\n- Rejected: **{rejected}**\n\n## New Channels\n\n"+"\n".join(f"- {n} ({c}) — {u}" for c,a,n,u in new)+"\n\n## New Backups\n\n"+"\n".join(f"- {n} ({c}) — {u}" for c,a,n,u in backups)+"\n",encoding="utf-8")
    print(f"Discovery: {len(new)} new channels, {len(backups)} new backups, {rejected} rejected.")

if __name__=="__main__": main()
