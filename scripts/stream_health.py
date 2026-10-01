#!/usr/bin/env python3
"""Non-destructive HTTP/HLS stream health probe with persistent failure history."""
import concurrent.futures, json, re, time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

PLAYLIST=Path("IPTV-Playlist.m3u")
REPORT=Path("reports/stream-health.md")
HISTORY=Path("reports/stream-health-history.json")
ATTR=re.compile(r'([\w-]+)="([^"]*)"')
GROUP_EXCLUDE={"New Channels","New Backup","Not Playing"}

def attrs(s): return dict(ATTR.findall(s))
def parse():
    lines=PLAYLIST.read_text(encoding="utf-8-sig").splitlines()
    rows=[]; cur=None
    for line in lines:
        if line.startswith("#EXTINF:"):
            cur=attrs(line); cur["_display"]=(cur.get("tvg-name") or line.rsplit(",",1)[-1]).strip()
        elif cur and line.strip().startswith(("http://","https://")):
            rows.append((cur,line.strip())); cur=None
    return rows

def probe(item):
    a,url=item
    started=time.monotonic()
    try:
        req=Request(url,headers={"User-Agent":"BDIX-IPTV-HealthCheck/1.0","Accept":"*/*","Range":"bytes=0-4095"})
        with urlopen(req,timeout=8) as r:
            data=r.read(4096)
            status=getattr(r,"status",200)
            ctype=r.headers.get("Content-Type","")
        latency=round((time.monotonic()-started)*1000)
        ok=status < 400 and len(data)>0
        return {"ok":ok,"status":status,"latency_ms":latency,"bytes":len(data),"content_type":ctype,"error":""}
    except HTTPError as e:
        return {"ok":False,"status":e.code,latency_ms":round((time.monotonic()-started)*1000),"bytes":0,"content_type":"","error":f"HTTP {e.code}"}
    except Exception as e:
        return {"ok":False,"status":0,"latency_ms":round((time.monotonic()-started)*1000),"bytes":0,"content_type":"","error":type(e).__name__}

def main():
    rows=parse()
    targets=[(a,u) for a,u in rows if a.get("group-title","").strip() not in GROUP_EXCLUDE]
    results=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=32) as ex:
        futs=[ex.submit(probe,(a,u)) for a,u in targets]
        for (a,u),f in zip(targets,futs):
            r=f.result()
            results.append({"id":(a.get("tvg-id") or a.get("channel-id") or "").strip().lower(),"name":a.get("_display",""),"group":a.get("group-title","").strip(),"url":u,**r})
    now=datetime.now(timezone.utc).isoformat(timespec="seconds")
    previous={}
    if HISTORY.exists():
        try: previous=json.loads(HISTORY.read_text(encoding="utf-8"))
        except Exception: previous={}
    if not isinstance(previous,dict): previous={}
    for r in results:
        h=previous.get(r["url"],{"checks":0,"successes":0,"failures":0,"consecutive_failures":0})
        h["checks"]+=1
        if r["ok"]:
            h["successes"]+=1; h["consecutive_failures"]=0; h["last_ok"]=now
        else:
            h["failures"]+=1; h["consecutive_failures"]=h.get("consecutive_failures",0)+1; h["last_failure"]=now
        h["last_status"]=r["status"]; h["last_latency_ms"]=r["latency_ms"]
        previous[r["url"]]=h
        r["consecutive_failures"]=h["consecutive_failures"]
        r["success_rate"]=round(h["successes"]/h["checks"]*100,1)
    HISTORY.parent.mkdir(parents=True,exist_ok=True)
    HISTORY.write_text(json.dumps({r["url"]:previous[r["url"]] for r in results},indent=2)+"\n",encoding="utf-8")
    ok=sum(r["ok"] for r in results); fail=len(results)-ok
    persistent=[r for r in results if r["consecutive_failures"]>=3]
    intermittent=[r for r in results if not r["ok"] and r["consecutive_failures"]<3]
    groups=Counter(r["group"] for r in results)
    lines=["# Stream Health Report","",f"Generated: **{now}**","",
           "Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.","",
           "## Summary","",f"- Streams tested: **{len(results)}**",f"- Reachable: **{ok}**",f"- Failed this check: **{fail}**",
           f"- Persistent failures (3+ consecutive): **{len(persistent)}**",f"- Intermittent failures: **{len(intermittent)}**",
           f"- Primary tested: **{sum(1 for r in results if r['group'] != 'Backup')}**",f"- Backup tested: **{groups.get('Backup',0)}**","",
           "## Persistent Failures",""]
    if persistent:
        lines += [f"- **{r['name']}** — {r['group']} — consecutive failures: **{r['consecutive_failures']}** — {r['error'] or r['status']}" for r in sorted(persistent,key=lambda x:(x["group"],x["name"]))]
    else: lines.append("None.")
    lines += ["","## Failed This Check",""]
    if fail:
        lines += [f"- **{r['name']}** — {r['group']} — streak {r['consecutive_failures']} — {r['error'] or r['status']}" for r in sorted([x for x in results if not x["ok"]],key=lambda x:(x["group"],x["name"]))]
    else: lines.append("None.")
    lines += ["","## Policy","","- Health failures never delete or reclassify streams automatically.",
              "- Backup streams remain protected even after repeated failures.",
              "- New Channels and New Backup are excluded from automated health promotion decisions.",
              "- Persistent failures are a review queue for Not Playing; they are not automatic deletion candidates."]
    REPORT.parent.mkdir(parents=True,exist_ok=True); REPORT.write_text("\n".join(lines)+"\n",encoding="utf-8")
    print(f"Stream health: tested={len(results)} ok={ok} failed={fail} persistent={len(persistent)}")

if __name__=="__main__": main()
