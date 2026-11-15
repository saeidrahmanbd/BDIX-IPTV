#!/usr/bin/env python3
"""Non-destructive HTTP/HLS stream health probe with persistent failure history."""
import concurrent.futures, hashlib, json, re, time, os, subprocess
from collections import Counter
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
from pathlib import Path
from urllib.error import HTTPError, URLError
import socket, ssl
from urllib.request import Request, urlopen
from urllib.parse import urlsplit, urlunsplit, parse_qsl

PLAYLIST=Path("IPTV-Playlist.m3u")
REPORT=Path("reports/stream-health.md")
HISTORY=Path("reports/stream-health-history.json")
ATTR=re.compile(r'([\w-]+)="([^"]*)"')
REVIEW_GROUPS={"Review","New Channels","New Backups","New Backup","Not Playing"}
GROUP_EXCLUDE=set()
SENSITIVE_QUERY={"token","access_token","refresh_token","sig","signature","jwt","session","key","api_key","apikey","authorization","auth","client_secret","hdnts","expires","e","username","user","password","passwd","pass"}

def attrs(s): return dict(ATTR.findall(s))
def url_fingerprint(url):
    """One-way history key: never persist credentials, tokens, or raw stream URLs."""
    return hashlib.sha256(str(url).strip().encode("utf-8")).hexdigest()

def migrate_history_keys(previous):
    """Convert legacy raw-URL history keys to fingerprints without losing streaks."""
    if not isinstance(previous,dict):
        return {}
    migrated = {}
    for key, value in previous.items():
        if not isinstance(value,dict):
            continue
        key = str(key)
        safe_key = key if re.fullmatch(r"[0-9a-f]{64}", key) else url_fingerprint(key)
        migrated[safe_key] = value
    return migrated

def load_history(path=HISTORY):
    """Load required durable history and fail closed instead of resetting streaks."""
    path = Path(path)
    try:
        previous = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Required stream-health history is missing or unreadable: {path}") from exc
    if not isinstance(previous, dict) or not previous:
        raise RuntimeError(f"Required stream-health history is empty or invalid: {path}")
    return migrate_history_keys(previous)


BD_TZ=ZoneInfo("Asia/Dhaka")
DEFINITIVE_HTTP_FAILURES={404,410}
def update_failure_history(history, result, check_date):
    """Advance a stream failure streak once per Bangladesh date, only for 404/410."""
    yesterday=(datetime.fromisoformat(check_date).date()-timedelta(days=1)).isoformat()
    previous_date=history.get("last_checked_date","")
    if previous_date == check_date:
        return history, int(history.get("consecutive_failure_days",0)), "already-checked-today"
    status=int(result.get("status",0) or 0)
    if result.get("ok"):
        streak=0
        history["last_status"]="ok"
        history["last_ok_date"]=check_date
    elif status in DEFINITIVE_HTTP_FAILURES:
        prior=int(history.get("consecutive_failure_days",0))
        streak=prior+1 if previous_date==yesterday and history.get("last_status")=="definitive_failure" else 1
        history["last_status"]="definitive_failure"
        history["last_failure_date"]=check_date
    else:
        streak=0
        history["last_status"]="inconclusive"
    history["last_checked_date"]=check_date
    history["consecutive_failure_days"]=streak
    history["consecutive_failures"]=streak
    return history, streak, history["last_status"]

def canonical_url(url):
    """Return a private in-memory family key without URL userinfo or query values."""
    p=urlsplit(url)
    host=(p.hostname or "").casefold()
    try: port=p.port
    except ValueError: port=None
    netloc=host + (f":{port}" if port and not ((p.scheme.lower()=="http" and port==80) or (p.scheme.lower()=="https" and port==443)) else "")
    path_parts=p.path.split("/")
    lower_parts=[x.casefold() for x in path_parts]
    for i,segment in enumerate(lower_parts):
        if segment in {"live","movie","series","timeshift"} and i+3<len(path_parts):
            path_parts[i+1]="REDACTED"; path_parts[i+2]="REDACTED"
    safe_path="/".join(path_parts).rstrip("/") or "/"
    return urlunsplit((p.scheme.lower(),netloc,safe_path,"",""))
def stream_url_inventory_sha256(path=PLAYLIST):
    urls=sorted(line.strip() for line in Path(path).read_text(encoding="utf-8-sig").splitlines() if line.strip().startswith(("http://","https://")))
    return hashlib.sha256("\n".join(urls).encode("utf-8")).hexdigest()
def parse():
    lines=PLAYLIST.read_text(encoding="utf-8-sig").splitlines(); rows=[]; cur=None
    for line in lines:
        if line.startswith("#EXTINF:"):
            cur=attrs(line); cur["_display"]=(cur.get("tvg-name") or line.rsplit(",",1)[-1]).strip()
        elif cur and line.strip().startswith(("http://","https://")):
            rows.append((cur,line.strip())); cur=None
    return rows
def probe(item):
    a,url=item; started=time.monotonic()
    try:
        req=Request(url,headers={"User-Agent":"BDIX-IPTV-HealthCheck/1.0","Accept":"*/*","Range":"bytes=0-4095"})
        with urlopen(req,timeout=15) as r:
            data=r.read(4096); status=getattr(r,"status",200); ctype=r.headers.get("Content-Type","")
        latency=round((time.monotonic()-started)*1000); ok=status < 400 and len(data)>0
        return {"ok":ok,"status":status,"latency_ms":latency,"bytes":len(data),"content_type":ctype,"error":""}
    except HTTPError as e:
        return {"ok":False,"status":e.code,"latency_ms":round((time.monotonic()-started)*1000),"bytes":0,"content_type":"","error":f"HTTP {e.code}"}
    except URLError as e:
        reason=e.reason
        if isinstance(reason, socket.gaierror): kind="DNS"
        elif isinstance(reason, ssl.SSLError): kind="TLS"
        elif isinstance(reason,(TimeoutError,socket.timeout)): kind="Timeout"
        elif isinstance(reason,(ConnectionError,ConnectionResetError,ConnectionRefusedError)): kind="Connection"
        else: kind="Network"
        return {"ok":False,"status":0,"latency_ms":round((time.monotonic()-started)*1000),"bytes":0,"content_type":"","error":kind}
    except (TimeoutError,socket.timeout):
        return {"ok":False,"status":0,"latency_ms":round((time.monotonic()-started)*1000),"bytes":0,"content_type":"","error":"Timeout"}
    except ssl.SSLError:
        return {"ok":False,"status":0,"latency_ms":round((time.monotonic()-started)*1000),"bytes":0,"content_type":"","error":"TLS"}
    except Exception:
        return {"ok":False,"status":0,"latency_ms":round((time.monotonic()-started)*1000),"bytes":0,"content_type":"","error":"Other"}

def main():
    rows=parse()
    targets=[(a,u) for a,u in rows if a.get("group-title","").strip() not in GROUP_EXCLUDE]
    results=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=32) as ex:
        futs=[ex.submit(probe,(a,u)) for a,u in targets]
        for (a,u),f in zip(targets,futs):
            r=f.result(); results.append({"id":(a.get("tvg-id") or a.get("channel-id") or "").strip().lower(),"name":a.get("_display",""),"group":a.get("group-title","").strip(),"url":u,**r})
    now=datetime.now(timezone.utc).isoformat(timespec="seconds")
    check_date=datetime.now(BD_TZ).date().isoformat()
    previous=load_history()
    for r in results:
        history_key=url_fingerprint(r["url"])
        h=previous.get(history_key,{"checks":0,"successes":0,"failures":0,"consecutive_failure_days":0})
        h["checks"]+=1
        if r["ok"]: h["successes"]+=1
        else: h["failures"]+=1
        h, streak, state=update_failure_history(h,r,check_date)
        h["last_status_code"]=r["status"]
        h["last_latency_ms"]=r["latency_ms"]
        previous[history_key]=h
        r["consecutive_failures"]=streak
        r["consecutive_failure_days"]=streak
        r["history_state"]=state
        r["success_rate"]=round(h["successes"]/h["checks"]*100,1)
    HISTORY.parent.mkdir(parents=True,exist_ok=True); HISTORY.write_text(json.dumps({url_fingerprint(r["url"]):previous[url_fingerprint(r["url"])] for r in results},indent=2)+"\n",encoding="utf-8")
    ok=sum(r["ok"] for r in results); fail=len(results)-ok
    failure_classes=Counter(("HTTP 404/410 (definitive)" if r["status"] in {404,410} else "Inconclusive HTTP/network failure") for r in results if not r["ok"])
    persistent=[r for r in results if r["consecutive_failure_days"]>=3]; intermittent=[r for r in results if not r["ok"] and r["consecutive_failure_days"]<3]
    groups=Counter(r["group"] for r in results)
    primary_targets=[r for r in results if r["group"] not in {"Backup","Review","New Channels","New Backups","New Backup","Not Playing"}]
    families={}
    for r in results: families.setdefault(canonical_url(r["url"]),set()).add(url_fingerprint(r["url"]))
    near_duplicates={k:v for k,v in families.items() if len(v)>1}
    runner_context="GitHub-hosted ubuntu-latest runner" if os.getenv("GITHUB_ACTIONS")=="true" else "local/non-GitHub runner"
    lines=["# Stream Health Report","",f"Generated: **{now}**",f"Stream URL inventory SHA-256: **{stream_url_inventory_sha256()}**","",f"Probe environment: **{runner_context}**.","A successful HTTP response confirms endpoint reachability, not guaranteed video/audio playback. HTTP 401/403 can reflect authentication, entitlement, or geographic restrictions; results from a GitHub-hosted runner should not be treated as proof of Bangladesh/India-local playback availability.","","## Summary","",f"- Streams tested: **{len(results)}**",f"- Reachable: **{ok}**",f"- Failed this check: **{fail}**",f"- Persistent failures (3+ consecutive): **{len(persistent)}**",f"- Intermittent failures: **{len(intermittent)}**",f"- Primary tested: **{len(primary_targets)}**",f"- Backup tested: **{groups.get('Backup',0)}**",f"- Review-queue entries tested: **{sum(groups.get(g,0) for g in REVIEW_GROUPS)}**",f"- Near-duplicate URL families: **{len(near_duplicates)}**","","## Failure Classification","","- Only HTTP 404 and 410 count as definitive failures; all other HTTP statuses and network/authentication errors are inconclusive.","- Streaks count consecutive Bangladesh calendar days; repeated runs on one date count once, and a missed day resets the streak.",""]
    lines += [f"- {k}: **{v}**" for k,v in sorted(failure_classes.items())]
    lines += ["","## Persistent Failures",""]
    lines += ([f"- **{r['name']}** — {r['group']} — consecutive failed days: **{r['consecutive_failure_days']}** — {r['error'] or r['status']}" for r in sorted(persistent,key=lambda x:(x["group"],x["name"]))] if persistent else ["None."])
    lines += ["","## Failed This Check",""]
    lines += ([f"- **{r['name']}** — {r['group']} — streak {r['consecutive_failure_days']} days — {r['error'] or r['status']}" for r in sorted([x for x in results if not x["ok"]],key=lambda x:(x["group"],x["name"]))] if fail else ["None."])
    lines += ["","## Near-Duplicate URL Families",""]
    lines += ([f"- URL family fingerprint `{hashlib.sha256(canonical.encode()).hexdigest()[:12]}` — {len(urls)} URL variants; credentials and query values are not published." for canonical,urls in sorted(near_duplicates.items())] if near_duplicates else ["None."])
    lines += ["","## Policy","","- Health failures never delete or reclassify streams automatically.","- Backup streams remain protected even after repeated failures.","- Persistent failures are reported for review; they are never automatic deletion candidates.","- A URL family is not automatically counted as independent redundancy merely because its path, rendition, or query string differs."]
    REPORT.parent.mkdir(parents=True,exist_ok=True); REPORT.write_text("\n".join(lines)+"\n",encoding="utf-8")
    print(f"Stream health: tested={len(results)} ok={ok} failed={fail} persistent={len(persistent)}")
if __name__=="__main__": main()
