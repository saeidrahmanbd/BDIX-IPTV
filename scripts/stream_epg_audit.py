#!/usr/bin/env python3
import csv, gzip, re, urllib.parse, urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

PLAYLIST_URL="https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u"
EPG_URLS=[
 "https://epg.pw/xmltv/epg_IN.xml",
 "https://epgshare01.online/epgshare01/epg_ripper_IN1.xml.gz",
 "https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz",
 "https://iptv-epg.org/files/epg-in.xml",
]
UA="BDIX-IPTV-Audit/1.3"
TIMEOUT=6
WORKERS=48
MAX_STREAM_BYTES=65536

def fetch(url, timeout=TIMEOUT, max_bytes=MAX_STREAM_BYTES, ranged=False):
    headers={"User-Agent":UA,"Accept":"*/*","Accept-Encoding":"identity"}
    if ranged: headers["Range"]=f"bytes=0-{max_bytes-1}"
    req=urllib.request.Request(url,headers=headers)
    with urllib.request.urlopen(req,timeout=timeout) as r:
        return r.status,dict(r.headers),r.read(max_bytes)

def parse_playlist(text):
    rows=[]; cur=None
    for raw in text.splitlines():
        line=raw.strip()
        if line.startswith("#EXTINF:"): cur={"extinf":line,"url":""}
        elif cur and line and not line.startswith("#"):
            cur["url"]=line; rows.append(cur); cur=None
    return rows

def attr(extinf,key):
    m=re.search(rf'{re.escape(key)}="([^"]*)"',extinf)
    return m.group(1) if m else ""

def audit_stream(item):
    url,row=item
    try:
        status,headers,body=fetch(url,ranged=True)
        if ".m3u8" in url.lower() or body.lstrip().startswith(b"#EXTM3U"):
            lines=body.decode("utf-8","replace").splitlines()
            children=[x.strip() for x in lines if x.strip() and not x.startswith("#")]
            if children:
                child=urllib.parse.urljoin(url,children[0])
                try:
                    s2,_,b2=fetch(child,ranged=False)
                    return row,("OK" if 200<=s2<400 else "PARTIAL"),f"HTTP {status}; child HTTP {s2}; {len(body)}B/{len(b2)}B"
                except Exception as e:
                    return row,"PARTIAL",f"HTTP {status}; child failed: {type(e).__name__}"
        return row,("OK" if 200<=status<400 else "FAIL"),f"HTTP {status}; {len(body)}B; {headers.get('Content-Type','')}"
    except Exception as e:
        return row,"FAIL",f"{type(e).__name__}: {e}"

def parse_epg_ids(data):
    if data[:2]==b"\x1f\x8b": data=gzip.decompress(data)
    root=ET.fromstring(data)
    return {c.attrib["id"] for c in root.findall(".//channel") if c.attrib.get("id")}

def audit_epg(url):
    try:
        # EPG XML must be downloaded completely before parsing.
        status,headers,data=fetch(url,timeout=45,max_bytes=100_000_000,ranged=False)
        ids=parse_epg_ids(data)
        return url,len(ids),ids,None
    except Exception as e:
        return url,0,set(),f"{type(e).__name__}: {e}"

def main():
    out=Path("audit"); out.mkdir(exist_ok=True)
    _,_,data=fetch(PLAYLIST_URL,30,2_000_000,False)
    rows=parse_playlist(data.decode("utf-8","replace"))
    unique={}
    for r in rows:
        if r["url"]: unique.setdefault(r["url"],r)
    items=list(unique.items())
    results=[]
    print(f"Playlist entries: {len(rows)}; unique URLs: {len(items)}; workers: {WORKERS}")
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        fs=[pool.submit(audit_stream,item) for item in items]
        for n,f in enumerate(as_completed(fs),1):
            row,state,detail=f.result()
            print(f"[{n}/{len(items)}] {state} {attr(row['extinf'],'tvg-name')}")
            results.append([attr(row["extinf"],"tvg-id"),attr(row["extinf"],"tvg-name"),
                            attr(row["extinf"],"group-title"),row["url"],state,detail])
    results.sort(key=lambda x:x[1].lower())
    with (out/"stream-audit.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.writer(f); w.writerow(["tvg-id","tvg-name","group","url","status","detail"]); w.writerows(results)

    playlist_ids={attr(r["extinf"],"tvg-id") for r in rows if attr(r["extinf"],"tvg-id")}
    epg_lines=[]
    with ThreadPoolExecutor(max_workers=2) as pool:
        fs=[pool.submit(audit_epg,u) for u in EPG_URLS]
        for f in as_completed(fs):
            u,count,ids,error=f.result()
            if error:
                epg_lines.append(f"- {u}: FAILED — {error}")
                print(f"EPG FAIL: {u}: {error}")
            else:
                matched={x for x in playlist_ids if x in ids or x.split("@",1)[0] in ids}
                epg_lines.append(f"- {u}: {len(matched)}/{len(playlist_ids)} playlist IDs matched ({count} EPG IDs)")
                print(f"EPG OK: {u} ({count} IDs; {len(matched)} matched)")

    ok=sum(x[4]=="OK" for x in results); partial=sum(x[4]=="PARTIAL" for x in results); fail=sum(x[4]=="FAIL" for x in results)
    summary=["# Stream + EPG audit","",f"- Playlist entries: {len(rows)}",f"- Unique stream URLs tested: {len(items)}",
             f"- Stream OK: {ok}",f"- Stream PARTIAL: {partial}",f"- Stream FAIL: {fail}","",
             "## EPG coverage","",*sorted(epg_lines),"",
             "## Interpretation","",
             "Stream checks use a small ranged read and a bounded child read; this tests HTTP/HLS reachability, not continuous playback.",
             "EPG files are downloaded completely before XML parsing, so coverage numbers are not based on truncated XML."]
    (out/"SUMMARY.md").write_text("\n".join(summary)+"\n",encoding="utf-8")

if __name__=="__main__": main()
