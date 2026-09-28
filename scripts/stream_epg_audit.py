#!/usr/bin/env python3
import csv, gzip, re, urllib.parse, urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

PLAYLIST_URL="https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u"
EPG_URLS=[
 "https://iptv-org.github.io/epg/guides/in/dishtv.in.epg.xml",
 "https://epg.pw/xmltv/epg_IN.xml",
 "https://iptv-epg.org/files/epg-in.xml",
]
UA="BDIX-IPTV-Audit/1.1"
TIMEOUT=8
WORKERS=32

def fetch(url, timeout=TIMEOUT):
    req=urllib.request.Request(url,headers={"User-Agent":UA,"Accept":"*/*"})
    with urllib.request.urlopen(req,timeout=timeout) as r:
        return r.status,dict(r.headers),r.read()

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

def base_id(x): return x.split("@",1)[0] if x else ""

def audit_stream(item):
    url,row=item
    try:
        status,headers,body=fetch(url)
        if ".m3u8" in url.lower() or body.lstrip().startswith(b"#EXTM3U"):
            lines=body.decode("utf-8","replace").splitlines()
            children=[x.strip() for x in lines if x.strip() and not x.startswith("#")]
            if children:
                child=urllib.parse.urljoin(url,children[0])
                try:
                    s2,_,b2=fetch(child)
                    state="OK" if 200<=s2<400 else "PARTIAL"
                    detail=f"HTTP {status}; child HTTP {s2}; {len(body)}B/{len(b2)}B"
                    return row,state,detail
                except Exception as e:
                    return row,"PARTIAL",f"HTTP {status}; child failed: {type(e).__name__}"
        return row,("OK" if 200<=status<400 else "FAIL"),f"HTTP {status}; {len(body)}B; {headers.get('Content-Type','')}"
    except Exception as e:
        return row,"FAIL",f"{type(e).__name__}: {e}"

def parse_epg_ids(data):
    if data[:2]==b"\x1f\x8b": data=gzip.decompress(data)
    root=ET.fromstring(data)
    return {c.attrib["id"] for c in root.findall(".//channel") if c.attrib.get("id")}

def main():
    out=Path("audit"); out.mkdir(exist_ok=True)
    _,_,data=fetch(PLAYLIST_URL,30)
    rows=parse_playlist(data.decode("utf-8","replace"))
    unique={}
    for r in rows:
        if r["url"]: unique.setdefault(r["url"],r)
    items=list(unique.items())
    results=[]
    print(f"Playlist entries: {len(rows)}; unique URLs: {len(items)}; workers: {WORKERS}")
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futures=[pool.submit(audit_stream,item) for item in items]
        for n,f in enumerate(as_completed(futures),1):
            row,state,detail=f.result()
            print(f"[{n}/{len(items)}] {state} {attr(row['extinf'],'tvg-name')}")
            results.append([attr(row["extinf"],"tvg-id"),attr(row["extinf"],"tvg-name"),
                            attr(row["extinf"],"group-title"),row["url"],state,detail])
    results.sort(key=lambda x:x[1].lower())
    with (out/"stream-audit.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.writer(f); w.writerow(["tvg-id","tvg-name","group","url","status","detail"]); w.writerows(results)

    playlist_ids={attr(r["extinf"],"tvg-id") for r in rows if attr(r["extinf"],"tvg-id")}
    epg_lines=[]
    with ThreadPoolExecutor(max_workers=3) as pool:
        fs={pool.submit(fetch,u,30):u for u in EPG_URLS}
        for f in as_completed(fs):
            u=fs[f]
            try:
                _,_,b=f.result(); ids=parse_epg_ids(b)
                matched={x for x in playlist_ids if x in ids or base_id(x) in ids}
                epg_lines.append(f"- {u}: {len(matched)}/{len(playlist_ids)} playlist IDs matched")
                print(f"EPG OK: {u} ({len(ids)} IDs; {len(matched)} matched)")
            except Exception as e:
                epg_lines.append(f"- {u}: FAILED — {type(e).__name__}: {e}")
                print(f"EPG FAIL: {u}: {type(e).__name__}: {e}")

    ok=sum(x[4]=="OK" for x in results); partial=sum(x[4]=="PARTIAL" for x in results); fail=sum(x[4]=="FAIL" for x in results)
    summary=["# Stream + EPG audit","",f"- Playlist entries: {len(rows)}",f"- Unique stream URLs tested: {len(items)}",
             f"- Stream OK: {ok}",f"- Stream PARTIAL: {partial}",f"- Stream FAIL: {fail}","",
             "## EPG coverage","",*sorted(epg_lines),"",
             "## Interpretation","",
             "OK: URL and, for HLS, first referenced child returned HTTP 2xx/3xx.",
             "PARTIAL: parent HLS playlist was reachable but first child failed.",
             "FAIL: request failed or returned non-success HTTP status.",
             "This checks HTTP/HLS reachability; it does not guarantee continuous playback in every IPTV player."]
    (out/"SUMMARY.md").write_text("\n".join(summary)+"\n",encoding="utf-8")

if __name__=="__main__": main()
