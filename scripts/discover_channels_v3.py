#!/usr/bin/env python3
from __future__ import annotations
import json, shlex, unicodedata, urllib.request
from pathlib import Path
from urllib.parse import urlparse

P=Path("IPTV-Playlist.m3u"); R=Path("reports/channel-discovery.md")
S=[("Bangladesh","https://iptv-org.github.io/iptv/countries/bd.m3u"),("India","https://iptv-org.github.io/iptv/countries/in.m3u")]
BLOCK={"sports","religious","kids"}; INDIA={"music","movies","movie"}
BAD=("vod","catchup","catch-up","test","demo","proxy","proxied","cors","webcam","radio","podcast","event","ppv","24/7","timeshift")
HOSTBAD=("proxy","proxied","cors","localhost","workers.dev","worker.dev","pages.dev")
QBAD=("token=","auth=","authorization=","hdnts=","sig=","signature=","expires=","session=","jwt=","key=")

def attrs(line):
    try: t=shlex.split(line,posix=True)
    except ValueError: return {}
    return dict(x.split("=",1) for x in t[1:] if "=" in x)

def norm(s):
    # Normalize channel names independently of quality/country/formatting labels.
    # Remove all parenthesized/bracketed metadata, not just the last suffix.
    s=unicodedata.normalize("NFKC",s).lower()
    s=s.replace("_"," ")
    while True:
        z=s
        s=s.replace("("," ").replace(")"," ").replace("["," ").replace("]"," ")
        # Remove common quality markers that may remain outside brackets.
        s=" ".join(x for x in s.split() if x not in {
            "uhd","fhd","hd","sd","4k","1080p","720p","576p","480p","360p","240p"
        })
        if s==z: break
    return "".join(c for c in s if c.isalnum() or unicodedata.category(c).startswith("L"))

def base_id(s):
    # IPTV-org often adds @SD/@HD/etc. to an identity already present locally.
    return (s or "").strip().lower().split("@",1)[0]

def parse(text):
    ls=text.replace("\r","").splitlines(); out=[]; i=0
    while i<len(ls):
        if ls[i].startswith("#EXTINF"):
            j=i+1
            while j<len(ls) and not ls[j].strip(): j+=1
            if j<len(ls) and ls[j].startswith(("http://","https://")):
                a=attrs(ls[i]); n=a.get("tvg-name") or ls[i].rsplit(",",1)[-1].strip()
                out.append((a,n.strip(),ls[j].strip())); i=j
        i+=1
    return out

def cats(a):
    z=set()
    for k in ("group-title","category","categories"):
        z.update(x.strip().lower() for x in a.get(k,"").replace("; ",",").replace("|",",").split(",") if x.strip())
    return z

def ok(country,a,n,u):
    c=cats(a); h=" ".join((n,a.get("tvg-id",""),a.get("group-title",""),a.get("category",""))).lower()
    if c&BLOCK or any(x in h for x in BAD): return False
    if country=="India" and ("news" in c or not c&INDIA): return False
    p=urlparse(u)
    if p.scheme not in ("http","https") or not p.netloc or p.query or p.fragment: return False
    if any(x in u.lower() for x in QBAD) or any(x in p.netloc.lower() for x in HOSTBAD): return False
    return p.path.lower().endswith((".m3u8",".m3u",".ts")) and "vod" not in p.path.lower() and "catchup" not in p.path.lower()

def ext(a,n,g):
    cid=(a.get("tvg-id") or a.get("channel-id") or "").strip()
    if not cid: return None
    x=f'#EXTINF:-1 tvg-id="{cid}" tvg-name="{n}"'
    if a.get("tvg-logo"): x+=f' tvg-logo="{a["tvg-logo"].strip()}"'
    x+=f' channel-id="{a.get("channel-id",cid).strip()}" group-title="{g}"'
    return x+","+n

def main():
    original=P.read_text(encoding="utf-8-sig"); entries=parse(original)
    pairs={(norm(n),u) for a,n,u in entries}
    names={norm(n) for a,n,u in entries}
    ids={base_id(a.get("tvg-id") or a.get("channel-id")) for a,n,u in entries
         if base_id(a.get("tvg-id") or a.get("channel-id"))}
    cand=[]; rejected=0
    for country,src in S:
        try:
            q=urllib.request.Request(src,headers={"User-Agent":"BDIX-IPTV-discovery/1.0"})
            text=urllib.request.urlopen(q,timeout=30).read().decode("utf-8","replace")
        except Exception as e:
            print("Source unavailable:",src,e); continue
        for a,n,u in parse(text):
            if ok(country,a,n,u) and (norm(n),u) not in pairs: cand.append((country,a,n,u))
            elif not ok(country,a,n,u): rejected+=1
    cand.sort(key=lambda x:(x[0]!="Bangladesh",norm(x[2]),x[3]))
    new=[]; backups=[]; planned_names=set(names); planned_ids=set(ids); seen=set(pairs)
    for c,a,n,u in cand:
        pair=(norm(n),u)
        if pair in seen:
            continue

        cid=base_id(a.get("tvg-id") or a.get("channel-id"))
        name_key=norm(n)

        # If the channel identity already exists locally, a different stream
        # is a backup candidate, never a "New Channel".
        if name_key in planned_names or (cid and cid in planned_ids):
            backups.append((c,a,n,u))
        else:
            new.append((c,a,n,u))
            planned_names.add(name_key)
            if cid: planned_ids.add(cid)
        seen.add(pair)
    new=new[:40]; backups=backups[:80]
    lines=original.replace("\r","").splitlines(); add=[]
    for c,a,n,u in new:
        z=ext(a,n,"New Channels")
        if z: add += [z,u]
    for c,a,n,u in backups:
        z=ext(a,n,"New Backup")
        if z: add += [z,u]
    if add:
        # New Channels and New Backup are intentionally appended to the
        # physical end of the playlist, after all existing Backup entries.
        while lines and not lines[-1].strip():
            lines.pop()
        if lines and add:
            lines.append("")
        lines.extend(add)
        for i,l in enumerate(lines):
            if l.startswith("#PLAYLIST-STUDIO-CATEGORIES:"):
                cs=json.loads(l.split(":",1)[1])
                for g in ("New Channels","New Backup"):
                    if g not in cs:
                        cs.append(g)
                lines[i]="#PLAYLIST-STUDIO-CATEGORIES:"+json.dumps(cs,ensure_ascii=False); break
        P.write_text("\n".join(lines)+"\n",encoding="utf-8")
    R.parent.mkdir(parents=True,exist_ok=True)
    R.write_text("# Channel Discovery\n\n"+f"- New channels: **{len(new)}**\n- New backups: **{len(backups)}**\n- Rejected: **{rejected}**\n\n## New Channels\n\n"+"\n".join(f"- {n} ({c}) — {u}" for c,a,n,u in new)+"\n\n## New Backups\n\n"+"\n".join(f"- {n} ({c}) — {u}" for c,a,n,u in backups)+"\n",encoding="utf-8")
    print(f"Discovery: {len(new)} new channels, {len(backups)} new backups, {rejected} rejected.")

if __name__=="__main__": main()
