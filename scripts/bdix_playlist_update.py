#!/usr/bin/env python3
"""Safe audit and limited metadata repair for BDIX-Playlist.m3u."""
import concurrent.futures
import json
import re
import time
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

PLAYLIST = Path("BDIX-Playlist.m3u")
REPORT = Path("reports/bdix-playlist-audit.md")
HEALTH = Path("reports/bdix-stream-health.md")
HISTORY = Path("reports/bdix-maintenance-history.json")
ATTR = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')

def get_attrs(line):
    return dict(ATTR.findall(line))

def set_attr(line, key, value):
    p = re.compile(rf'{re.escape(key)}="[^"]*"')
    if p.search(line):
        return p.sub(f'{key}="{value}"', line, count=1)
    return line.replace("#EXTINF:-1 ", f'#EXTINF:-1 {key}="{value}" ', 1)

def redact(url):
    return re.sub(r'([?&](?:token|sig|signature|jwt|session|key|authorization|hdnts)=[^\s&]+)',
                  lambda m: m.group(1).split("=",1)[0] + "=[REDACTED]", url, flags=re.I)

def entries(lines):
    out = []
    for i, line in enumerate(lines):
        if not line.startswith("#EXTINF:"):
            continue
        j = i + 1
        while j < len(lines) and not lines[j].strip():
            j += 1
        url = lines[j].strip() if j < len(lines) and lines[j].strip().lower().startswith(("http://","https://")) else ""
        out.append({"line_no": i+1, "index": i, "line": line, "attrs": get_attrs(line),
                    "name": line.rsplit(",",1)[-1].strip() if "," in line else "", "url": url})
    return out

def probe(url):
    t = time.monotonic()
    try:
        req = Request(url, headers={"User-Agent":"BDIX-IPTV-BDIX-Playlist-Updater/1.0",
                                    "Range":"bytes=0-4095", "Accept":"*/*"})
        with urlopen(req, timeout=8) as r:
            status = getattr(r, "status", 200)
            r.read(4096)
            return True, status, round((time.monotonic()-t)*1000), ""
    except HTTPError as e:
        return False, e.code, round((time.monotonic()-t)*1000), f"HTTP {e.code}"
    except (URLError, TimeoutError, OSError) as e:
        return False, 0, round((time.monotonic()-t)*1000), type(e).__name__
    except Exception as e:
        return False, 0, round((time.monotonic()-t)*1000), type(e).__name__

def main():
    if not PLAYLIST.exists():
        raise SystemExit("BDIX-Playlist.m3u not found")
    lines = PLAYLIST.read_text(encoding="utf-8-sig").replace("\r","").splitlines()
    changes = []

    # Safe repairs only: fill missing channel-id from an existing tvg-id,
    # and missing tvg-name from the existing display name. Nothing else changes.
    for row in entries(lines):
        a = row["attrs"]
        line = row["line"]
        if a.get("tvg-id","").strip() and not a.get("channel-id","").strip():
            line = set_attr(line, "channel-id", a["tvg-id"].strip())
            changes.append(f"line {row['line_no']}: added missing channel-id")
        if not a.get("tvg-name","").strip() and row["name"]:
            line = set_attr(line, "tvg-name", row["name"])
            changes.append(f"line {row['line_no']}: added missing tvg-name")
        lines[row["index"]] = line

    if changes:
        PLAYLIST.write_text("\n".join(lines) + "\n", encoding="utf-8")

    rows = entries(lines)
    ids = defaultdict(list)
    urls = defaultdict(list)
    missing_ids = []
    missing_chno = []
    missing_logo = []
    malformed = []
    for row in rows:
        a = row["attrs"] if row["line"] == lines[row["index"]] else get_attrs(lines[row["index"]])
        if not (a.get("tvg-id") or a.get("channel-id")):
            missing_ids.append(row["name"])
        if not a.get("tvg-chno"):
            missing_chno.append(row["name"])
        if not a.get("tvg-logo"):
            missing_logo.append(row["name"])
        if not row["url"]:
            malformed.append((row["line_no"], "missing stream URL"))
        if row["line"].count('"') % 2:
            malformed.append((row["line_no"], "unbalanced quotes"))
        cid = (a.get("tvg-id") or a.get("channel-id") or "").strip().lower()
        if cid: ids[cid].append(row)
        if row["url"]: urls[row["url"].lower()].append(row)

    duplicate_ids = {k:v for k,v in ids.items() if len(v) > 1}
    duplicate_urls = {k:v for k,v in urls.items() if len(v) > 1}

    registry = []
    reg = next((x for x in lines if x.startswith("#PLAYLIST-STUDIO-CATEGORIES:")), "")
    if reg:
        try: registry = json.loads(reg.split(":",1)[1])
        except Exception: registry = []
    groups = Counter(row["attrs"].get("group-title","").strip() for row in rows)
    unknown_groups = sorted(g for g in groups if g and g not in registry)

    unique_urls = list(urls)
    health = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=24) as pool:
        future_map = {pool.submit(probe,u):u for u in unique_urls}
        for f in concurrent.futures.as_completed(future_map):
            u = future_map[f]
            ok,status,latency,error = f.result()
            health.append((u,ok,status,latency,error))
    failed = [x for x in health if not x[1]]
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")

    report = [
        "# BDIX Playlist Audit","",f"Generated: **{now}**","",
        "## Summary","",
        f"- Playlist: **{PLAYLIST.name}**",
        f"- Total entries: **{len(rows)}**",
        f"- Unique stream URLs: **{len(unique_urls)}**",
        f"- Unique channel identities: **{len(ids)}**",
        f"- Duplicate stream URLs: **{len(duplicate_urls)}**",
        f"- Duplicate channel identities: **{len(duplicate_ids)}**",
        f"- Missing channel IDs: **{len(missing_ids)}**",
        f"- Missing channel numbers: **{len(missing_chno)}**",
        f"- Missing logos: **{len(missing_logo)}**",
        f"- Malformed entries: **{len(malformed)}**",
        f"- Unknown categories: **{len(unknown_groups)}**",
        f"- Streams tested: **{len(health)}**",
        f"- Reachable: **{len(health)-len(failed)}**",
        f"- Failed: **{len(failed)}**","",
        "## Protection Policy","",
        "This workflow does not discover/import channels, delete streams, change existing IDs or channel numbers, change categories, reorder entries, or rewrite stream URLs.",
        f"Safe metadata repairs made: **{len(changes)}**","",
        "## Categories",""
    ]
    for c in registry:
        report.append(f"- {c}: **{groups.get(c,0)}**")
    if unknown_groups:
        report += ["","Unknown categories:"] + [f"- {g}" for g in unknown_groups]

    report += ["","## Duplicate Stream URLs",""]
    if duplicate_urls:
        for u, rs in sorted(duplicate_urls.items()):
            names = sorted({r["name"] for r in rs if r["name"]})
            report.append(f"- {', '.join(names[:6])}: {redact(u)}")
    else:
        report.append("None.")

    report += ["","## Duplicate Channel Identities",""]
    if duplicate_ids:
        for cid, rs in sorted(duplicate_ids.items()):
            names = sorted({r["name"] for r in rs if r["name"]})
            report.append(f"- {cid}: {', '.join(names[:8])}")
    else:
        report.append("None.")

    report += ["","## Missing Metadata","",
               f"- Missing channel ID: {', '.join(missing_ids[:30]) or 'None'}",
               f"- Missing channel number: {', '.join(missing_chno[:30]) or 'None'}",
               f"- Missing logo: {', '.join(missing_logo[:30]) or 'None'}","",
               "## Malformed Entries",""]
    report += [f"- Line {n}: {reason}" for n,reason in malformed[:100]] or ["None."]

    health_report = [
        "# BDIX Stream Health","",f"Generated: **{now}**","",
        "Non-destructive connectivity test. Health failures never delete or reclassify BDIX streams.",
        "",f"- Unique streams tested: **{len(health)}**",
        f"- Reachable: **{len(health)-len(failed)}**",
        f"- Failed: **{len(failed)}**","",
        "## Failed Streams",""
    ]
    health_report += [f"- {redact(u)} — {error or status} — {latency} ms"
                      for u,ok,status,latency,error in sorted(failed,key=lambda x:redact(x[0]))] or ["None."]

    REPORT.parent.mkdir(parents=True,exist_ok=True)
    REPORT.write_text("\n".join(report)+"\n",encoding="utf-8")
    HEALTH.write_text("\n".join(health_report)+"\n",encoding="utf-8")

    history = []
    if HISTORY.exists():
        try: history = json.loads(HISTORY.read_text(encoding="utf-8"))
        except Exception: history = []
    if not isinstance(history,list): history=[]
    history.append({"timestamp_utc":now,"entries":len(rows),"unique_urls":len(unique_urls),
                    "duplicate_urls":len(duplicate_urls),"duplicate_ids":len(duplicate_ids),
                    "missing_ids":len(missing_ids),"missing_chno":len(missing_chno),
                    "missing_logos":len(missing_logo),"malformed":len(malformed),
                    "health_tested":len(health),"health_failures":len(failed),
                    "safe_repairs":len(changes)})
    HISTORY.write_text(json.dumps(history[-180:],indent=2)+"\n",encoding="utf-8")
    print(f"BDIX Playlist Update: entries={len(rows)} failed={len(failed)} repairs={len(changes)}")

if __name__ == "__main__":
    main()
