#!/usr/bin/env python3
import hashlib,re,html,json
from collections import Counter,defaultdict
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PLAYLIST=ROOT/"IPTV-Playlist.m3u"; AUDIT=ROOT/"reports/iptv-playlist-audit.md"; EPG=ROOT/"reports/epg-coverage.md"; EPG_DETAIL=ROOT/"reports/epg-three-playlist-audit.md"; HEALTH=ROOT/"reports/stream-health.md"; GATE=ROOT/"reports/pre-publish-gate.md"
OUT_MD=ROOT/"reports/Update Report.md"; OUT_SVG=ROOT/"assets/dashboard.svg"; OUT_MAINT=ROOT/"reports/maintenance-report.md"; HISTORY=ROOT/"reports/maintenance-history.json"
ATTR=re.compile(r'([\w-]+)="([^"]*)"')
def metric(text,label):
    m=re.search(r'- '+re.escape(label)+r': \*\*(\d+)\*\*',text); return int(m.group(1)) if m else 0
def read(p): return p.read_text(encoding="utf-8") if p.exists() else ""
def timestamp(p):
    m=re.search(r'(?:Generated|Last generated):\s*\*\*([^*]+)\*\*',read(p),re.I); return m.group(1) if m else "not available"
def normalized_identity_name(value):
    value = re.sub(r"\s*(?:\[[^]]*(?:geo[- ]?blocked)[^]]*\]|\((?:\d{3,4}[pi]|UHD|FHD|HD|SD)\)|\s+(?:\d{3,4}[pi]))\s*$", "", str(value or "").strip(), flags=re.I)
    value = re.sub(r"\s+", " ", value).strip()
    aliases = {"disney channel (india)": "Disney Channel India", "disney channel india": "Disney Channel India", "gazi tv": "G TV", "g tv": "G TV", "nick": "Nickelodeon (India)", "nickelodeon (india)": "Nickelodeon (India)"}
    return aliases.get(value.casefold(), value).casefold()
def parse():
    lines=PLAYLIST.read_text(encoding="utf-8-sig").splitlines(); rows=[]; cur=None
    for line in lines:
        if line.startswith("#EXTINF:"): cur=dict(re.findall(r'([\w-]+)="([^"]*)"',line)); cur["_name"]=(cur.get("tvg-name") or line.rsplit(",",1)[-1]).strip()
        elif cur and line.strip().startswith(("http://","https://")): rows.append(cur|{"url":line.strip()}); cur=None
    return rows
def main():
    e=parse(); a=read(AUDIT); g=read(EPG); egd=read(EPG_DETAIL); h=read(HEALTH); gate=read(GATE)
    gm=re.search(r'Status:\s*\*\*(PASS|BLOCK)\*\*',gate); gate_status=gm.group(1) if gm else "UNKNOWN"
    groups=Counter(x.get("group-title","") for x in e)
    active_groups={"Bangladesh","Indian Bangla","Indian Movies","Indian Music","Indian Entertainment","Pakistani","International","Documentary & Wildlife","Kids","Religious","Sports"}
    active=len({x.get("tvg-id") or x.get("channel-id") for x in e if x.get("group-title") in active_groups and (x.get("tvg-id") or x.get("channel-id"))})
    primary_streams=sum(1 for x in e if x.get("group-title") in active_groups)
    local=metric(a,"Healthy/local references"); logos=round(local*100/len(e),1) if e else 0
    id_names=defaultdict(set); name_ids=defaultdict(set)
    for x in e:
        cid=(x.get("tvg-id") or x.get("channel-id") or "").strip().casefold()
        name=normalized_identity_name(x.get("_name",""))
        if cid and name:
            id_names[cid].add(name)
            name_ids[name].add(cid)
    cross_queue_id_variants=sum(1 for names in id_names.values() if len(names)>1)
    cross_queue_name_collisions=sum(1 for ids in name_ids.values() if len(ids)>1)
    issues=sum(metric(a,k) for k in ["Duplicate stream URLs","Metadata conflicts","Cross-country backup collisions","Protected primary-entry changes","Logo exceptions","Duplicate primary identities","Primary channel-number collisions","Primary entries missing channel numbers","Malformed EXTINF entries","Category block-order issues","Alphabetical ordering issues"])
    hfail=metric(h,"Failed this check"); hpersist=metric(h,"Persistent failures (3+ consecutive)"); htested=metric(h,"Streams tested"); hnear=metric(h,"Near-duplicate URL families")
    total_match=re.search(r'Active unique playlist channel IDs audited:\s*\*\*(\d+)\*\*',g,re.I)
    mapping_match=re.search(r'IDs with an EPG source mapping:\s*\*\*(\d+)/(\d+) \(([\d.]+)%\)\*\*',g,re.I)
    current_match=re.search(r'IDs with usable current/future (?:English programme data|source schedules \(nonblank (?:English|allowed-language) titles\)):\s*\*\*(\d+)/(\d+) \(([\d.]+)%\)\*',g,re.I)
    missing_match=re.search(r'IDs with no EPG source mapping:\s*\*\*(\d+)\*\*',g,re.I)
    iptv_row=re.search(r'^\|\s*IPTV-Playlist\.m3u\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|',egd,re.M)
    if iptv_row:
        india=int(iptv_row.group(2)); mapped=int(iptv_row.group(3)); source_live=int(iptv_row.group(4)); present=int(iptv_row.group(5)); live=int(iptv_row.group(6)); missing=int(iptv_row.group(7)); mapct=round(mapped*100/india,1) if india else 0.0; livepct=round(live*100/india,1) if india else 0.0; epg_scope="IPTV-Playlist.m3u published-guide row"
    else:
        india=int(total_match.group(1)) if total_match else metric(g,"Active Indian channels audited"); mapped=int(mapping_match.group(1)) if mapping_match else metric(g,"Channels with an EPG mapping"); missing=int(missing_match.group(1)) if missing_match else metric(g,"No guide mapping found"); live=int(current_match.group(1)) if current_match else 0; livepct=float(current_match.group(3)) if current_match else 0.0; mapct=float(mapping_match.group(3)) if mapping_match else (round(mapped*100/india,1) if india else 0); epg_scope="combined EPG report fallback (IPTV-only row unavailable)"
    now=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"); source_sha=hashlib.sha256(PLAYLIST.read_bytes()).hexdigest()
    try: hist=json.loads(HISTORY.read_text(encoding="utf-8")); hist=hist[-30:] if isinstance(hist,list) else []
    except Exception: hist=[]
    prev=hist[-2] if len(hist)>=2 else {}; cur=hist[-1] if hist else {}
    md=f"""# Update Report

_Last generated: **{now}**_

Source playlist SHA-256: **{source_sha}**

| Metric | Current |
|---|---:|
| Streams | **{len(e)}** |
| Active Channel Identities | **{active}** |
| Active Primary Streams | **{primary_streams}** |
| Bangladesh | **{groups.get("Bangladesh",0)}** |
| India | **{sum(v for k,v in groups.items() if k.startswith("Indian "))}** |
| Backup Stream Entries | **{groups.get("Backup",0)}** |
| IPTV Local Logos | **{logos}%** |
| IPTV EPG Programme Coverage | **{livepct}%** |
| IPTV EPG Mapping | **{mapct}%** |
| Stream Health Tested | **{htested}** |
| Stream Health Failures | **{hfail}** |
| Persistent Failures | **{hpersist}** |
| Near-Duplicate URL Families | **{hnear}** |
| Audit Blocking Issues | **{issues}** |
| Pre-Publish Gate | **{gate_status}** |
| Pre-Publish Gate Generated | **{timestamp(GATE)}** |

## Quality Controls
- Duplicate stream URLs: **{metric(a,"Duplicate stream URLs")}**
- Metadata conflicts (canonical primary scope): **{metric(a,"Metadata conflicts")}**
- Same-name / different-ID collisions (canonical primary scope): **{metric(a,"Same-name / different-ID collisions")}**
- Cross-queue metadata identity variants: **{cross_queue_id_variants}**
- Cross-queue same-name / different-ID collisions: **{cross_queue_name_collisions}**
- Duplicate primary identities: **{metric(a,"Duplicate primary identities")}**
- Primary channel-number collisions: **{metric(a,"Primary channel-number collisions")}**
- Primary entries missing channel numbers: **{metric(a,"Primary entries missing channel numbers")}**
- Logo exceptions: **{metric(a,"Logo exceptions")}**
- Malformed EXTINF entries: **{metric(a,"Malformed EXTINF entries")}**
- Category block-order issues: **{metric(a,"Category block-order issues")}**
- Alphabetical ordering issues: **{metric(a,"Alphabetical ordering issues")}**
- Signed/tokenized URLs: **{metric(a,"Signed/tokenized stream URLs")}**

## Safety & Automation
- Stream health is non-destructive and keeps per-URL failure history.
- Backup streams are never automatically deleted because of health failures.
- `New Channels` and `New Backup` are active review queues used by discovery and validation; they are not retired categories.
- Pre-publish gate status: **{gate_status}**
- Canonical channel identity index: reports/channel-identity-index.json

## Counting Scope
- **Active Channel Identities / Active Primary Streams** count only canonical playlist groups.
- `New Channels`, `New Backup`, and `Not Playing` are review queues and are excluded from the active-primary count.
- **EPG IDs audited** use the EPG report's published-guide scope and therefore do not have to equal the active-primary identity count.
- **Backup Stream Entries** count playlist rows, not independent CDN/origin infrastructures. Backup independence is reviewed separately.

## EPG
- EPG IDs audited: **{india}**
- Mapped: **{mapped} ({mapct}%)**
- Current/future programme coverage: **{live}/{india} ({livepct}%)**
- No mapping: **{missing}**
- EPG metric scope: **{epg_scope}**
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
    cards=[("Streams",len(e)),("Channel Identities",active),("Bangladesh",groups.get("Bangladesh",0)),("India",sum(v for k,v in groups.items() if k.startswith("Indian "))),("Backup Entries",groups.get("Backup",0)),("IPTV Local Logos",f"{logos}%"),("IPTV EPG Coverage",f"{round(livepct)}%"),("Health Failures",hfail)]
    parts=['<svg xmlns="http://www.w3.org/2000/svg" width="980" height="650" viewBox="0 0 980 650">','<rect width="980" height="650" rx="24" fill="#f8fafc"/>','<rect width="980" height="92" rx="24" fill="#111827"/>',t(42,45,"BDIX-IPTV • PROJECT DASHBOARD",25,True),t(42,70,"Playlist • EPG • Metadata • Logos • Stream Health • Safety Gate",13)]
    for (lab,val),(x,y) in zip(cards,[(34,120),(268,120),(502,120),(736,120),(34,260),(268,260),(502,260),(736,260)]): parts += [f'<rect x="{x}" y="{y}" width="210" height="112" rx="18" fill="white" stroke="#e5e7eb"/>',t(x+18,y+34,lab,14),t(x+18,y+78,val,28,True)]
    parts += ['<rect x="34" y="400" width="912" height="190" rx="18" fill="white" stroke="#e5e7eb"/>',t(58,435,"Current quality status",18,True),t(58,470,f"Audit blocking issues: {issues}",15),t(58,498,f"Pre-publish gate: {gate_status}",15),t(58,526,f"Persistent health failures: {hpersist} • Near-duplicate URL families: {hnear}",15),t(58,554,f"Generated: {now}",13),'</svg>']
    OUT_SVG.write_text("".join(parts),encoding="utf-8")
    OUT_MAINT.write_text(f"""# IPTV Maintenance Report

_Generated: **{now}**_

Source playlist SHA-256: **{source_sha}**

| Item | Result |
|---|---:|
| Current playlist streams | **{len(e)}** |
| Active channel identities | **{active}** |
| Backup stream entries | **{groups.get("Backup",0)}** |
| EPG IDs audited | **{india}** |
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
- New Channels and New Backup remain active discovery/review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Dashboard and reports are generated from the current playlist.
""",encoding="utf-8")
if __name__=="__main__": main()
