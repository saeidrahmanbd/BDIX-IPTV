#!/usr/bin/env python3
import re,html,json
from collections import Counter
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PLAYLIST=ROOT/"IPTV-Playlist.m3u"; AUDIT=ROOT/"reports/playlist-audit.md"; EPG=ROOT/"reports/epg-coverage.md"; HEALTH=ROOT/"reports/stream-health.md"; GATE=ROOT/"reports/pre-publish-gate.md"
OUT_MD=ROOT/"reports/dashboard.md"; OUT_SVG=ROOT/"assets/dashboard.svg"; OUT_MAINT=ROOT/"reports/maintenance-report.md"; HISTORY=ROOT/"reports/maintenance-history.json"
ATTR=re.compile(r'([\w-]+)="([^"]*)"')
def metric(text,label):
    m=re.search(r'- '+re.escape(label)+r': \*\*(\d+)\*\*',text); return int(m.group(1)) if m else 0
def read(p): return p.read_text(encoding="utf-8") if p.exists() else ""
def timestamp(p):
    m=re.search(r'(?:Generated|Last generated):\s*\*\*([^*]+)\*\*',read(p),re.I); return m.group(1) if m else "not available"
def parse():
    lines=PLAYLIST.read_text(encoding="utf-8-sig").splitlines(); rows=[]; cur=None
    for line in lines:
        if line.startswith("#EXTINF:"): cur=dict(re.findall(r'([\w-]+)="([^"]*)"',line)); cur["_name"]=(cur.get("tvg-name") or line.rsplit(",",1)[-1]).strip()
        elif cur and line.strip().startswith(("http://","https://")): rows.append(cur|{"url":line.strip()}); cur=None
    return rows
def main():
    e=parse(); a=read(AUDIT); g=read(EPG); h=read(HEALTH); gate=read(GATE)
    gm=re.search(r'Status:\s*\*\*(PASS|BLOCK)\*\*',gate); gate_status=gm.group(1) if gm else "UNKNOWN"
    groups=Counter(x.get("group-title","") for x in e)
    active_groups={"Bangladesh","Indian Bangla","Indian Movies","Indian Music","Indian Entertainment","International","Documentary & Wildlife","Kids","Religious","Sports"}
    active=len({x.get("tvg-id") or x.get("channel-id") for x in e if x.get("group-title") in active_groups and (x.get("tvg-id") or x.get("channel-id"))})
    local=sum(1 for x in e if x.get("tvg-logo","").startswith("https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/")); logos=round(local*100/len(e),1) if e else 0
    issues=sum(metric(a,k) for k in ["Duplicate stream URLs","Metadata conflicts","Cross-country backup collisions","Protected primary-entry changes","Logo exceptions","Duplicate primary identities","Primary channel-number collisions","Primary entries missing channel numbers"])
    hfail=metric(h,"Failed this check"); hpersist=metric(h,"Persistent failures (3+ consecutive)"); htested=metric(h,"Streams tested")
    india=metric(g,"Active Indian channels audited"); mapped=metric(g,"Channels with an EPG mapping"); missing=metric(g,"No guide mapping found")
    m=re.search(r'Current/future programme coverage:\s*\*\*(\d+)/(\d+) \(([\d.]+)%\)',g,re.I); live=int(m.group(1)) if m else 0; livepct=float(m.group(3)) if m else 0; mapct=round(mapped*100/india,1) if india else 0
    now=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    try: hist=json.loads(HISTORY.read_text(encoding="utf-8")); hist=hist[-30:] if isinstance(hist,list) else []
    except Exception: hist=[]
    prev=hist[-2] if len(hist)>=2 else {}; cur=hist[-1] if hist else {}
    md=f"""# Project Dashboard

_Last generated: **{now}**_

| Metric | Current |
|---|---:|
| Streams | **{len(e)}** |
| Active Channels | **{active}** |
| Bangladesh | **{groups.get("Bangladesh",0)}** |
| India | **{sum(v for k,v in groups.items() if k.startswith("Indian "))}** |
| Backup Streams | **{groups.get("Backup",0)}** |
| New Channels | **{groups.get("New Channels",0)}** |
| New Backup Streams | **{groups.get("New Backup",0)}** |
| Local Logos | **{logos}%** |
| EPG Programme Coverage | **{livepct}%** |
| EPG Mapping | **{mapct}%** |
| Stream Health Tested | **{htested}** |
| Stream Health Failures | **{hfail}** |
| Persistent Failures | **{hpersist}** |
| Audit Blocking Issues | **{issues}** |
| Pre-Publish Gate | **{gate_status}** |

## Quality Controls
- Duplicate stream URLs: **{metric(a,"Duplicate stream URLs")}**
- Metadata conflicts: **{metric(a,"Metadata conflicts")}**
- Same-name / different-ID collisions: **{metric(a,"Same-name / different-ID collisions")}**
- Duplicate primary identities: **{metric(a,"Duplicate primary identities")}**
- Primary channel-number collisions: **{metric(a,"Primary channel-number collisions")}**
- Primary entries missing channel numbers: **{metric(a,"Primary entries missing channel numbers")}**
- Logo exceptions: **{metric(a,"Logo exceptions")}**
- Signed/tokenized URLs: **{metric(a,"Signed/tokenized stream URLs")}**

## Safety & Automation
- Stream health is non-destructive and keeps per-URL failure history.
- Backup streams are never automatically deleted because of health failures.
- Review queues remain user-controlled.
- Pre-publish gate status: **{gate_status}**
- Canonical channel identity index: reports/channel-identity-index.json

## EPG
- Indian channels audited: **{india}**
- Mapped: **{mapped} ({mapct}%)**
- Current/future programme coverage: **{live}/{india} ({livepct}%)**
- No mapping: **{missing}**
- Publication remains subject to source-policy approval.

## Freshness
| Report | Last generated |
|---|---|
| Playlist audit | **{timestamp(AUDIT)}** |
| EPG coverage | **{timestamp(EPG)}** |
| Stream health | **{timestamp(HEALTH)}** |
| Pre-publish gate | **{timestamp(GATE)}** |

## Maintenance History
- Records retained: **{len(hist)}**
- Latest entries change: **{prev.get("entries","—")} → {cur.get("entries","—")}**
- Latest health failures: **{prev.get("health_failures","—")} → {cur.get("health_failures","—")}**

Historical records are retained in reports/maintenance-history.json.
"""
    OUT_MD.write_text(md,encoding="utf-8")
    def t(x,y,s,size=15,b=False): return f'<text x="{x}" y="{y}" font-family="Arial,Helvetica,sans-serif" font-size="{size}px" font-weight="{"700" if b else "400"}" fill="#1f2937">{html.escape(str(s))}</text>'
    parts=['<svg xmlns="http://www.w3.org/2000/svg" width="980" height="650" viewBox="0 0 980 650">','<rect width="980" height="650" rx="24" fill="#f8fafc"/>','<rect width="980" height="92" rx="24" fill="#111827"/>',t(42,45,"BDIX-IPTV • PROJECT DASHBOARD",25,True),t(42,70,"Playlist • EPG • Metadata • Logos • Stream Health • Safety Gate",13)]
    cards=[("Streams",len(e)),("Active Channels",active),("Bangladesh",groups.get("Bangladesh",0)),("India",sum(v for k,v in groups.items() if k.startswith("Indian "))),("Backup Streams",groups.get("Backup",0)),("Local Logos",f"{logos}%"),("EPG Coverage",f"{round(livepct)}%"),("Health Failures",hfail)]
    for (lab,val),(x,y) in zip(cards,[(34,120),(268,120),(502,120),(736,120),(34,260),(268,260),(502,260),(736,260)]):
        parts += [f'<rect x="{x}" y="{y}" width="210" height="112" rx="18" fill="white" stroke="#e5e7eb"/>',t(x+18,y+34,lab,14),t(x+18,y+78,val,28,True)]
    parts += ['<rect x="34" y="400" width="912" height="190" rx="18" fill="white" stroke="#e5e7eb"/>',t(58,435,"Current quality status",18,True),t(58,470,f"Audit blocking issues: {issues}",15),t(58,498,f"Pre-publish gate: {gate_status}",15),t(58,526,f"Persistent health failures: {hpersist}",15),t(58,554,f"Generated: {now}",13),'</svg>']
    OUT_SVG.write_text("".join(parts),encoding="utf-8")
    OUT_MAINT.write_text(f"""# IPTV Maintenance Report

_Generated: **{now}**_

| Item | Result |
|---|---:|
| Current playlist streams | **{len(e)}** |
| Current channel IDs | **{metric(a,"Unique channel IDs")}** |
| Backup streams | **{groups.get("Backup",0)}** |
| New Channels | **{groups.get("New Channels",0)}** |
| New Backup | **{groups.get("New Backup",0)}** |
| Logo exceptions | **{metric(a,"Logo exceptions")}** |
| EPG mapping | **{mapct}%** |
| EPG programme coverage | **{livepct}%** |
| Health failures | **{hfail}** |
| Persistent health failures | **{hpersist}** |
| Audit blockers | **{issues}** |
| Pre-publish gate | **{gate_status}** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- New Channels and New Backup remain review queues.
- Dashboard and reports are generated from the current playlist.
""",encoding="utf-8")
if __name__=="__main__": main()
