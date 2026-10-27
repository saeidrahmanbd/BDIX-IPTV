#!/usr/bin/env python3
import hashlib,re,html,json,os
import xml.etree.ElementTree as ET
from collections import Counter,defaultdict
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PLAYLIST=ROOT/"IPTV-Playlist.m3u"; AUDIT=ROOT/"reports/iptv-playlist-audit.md"; EPG=ROOT/"reports/epg-coverage.md"; EPG_DETAIL=ROOT/"reports/epg-three-playlist-audit.md"; HEALTH=ROOT/"reports/stream-health.md"; GATE=ROOT/"reports/pre-publish-gate.md"
OUT_MD=ROOT/"reports/Update Report.md"; OUT_SVG=ROOT/"assets/dashboard.svg"; OUT_MAINT=ROOT/"reports/maintenance-report.md"; HISTORY=ROOT/"reports/maintenance-history.json"
EPG_GUIDE=ROOT/"epg/epg.xml"; EPG_FRESHNESS=ROOT/"reports/epg-publish-freshness.md"
ATTR=re.compile(r'([\w-]+)="([^"]*)"')
def metric(text,label):
    m=re.search(r'- '+re.escape(label)+r': \*\*(\d+)\*\*',text); return int(m.group(1)) if m else 0
def read(p): return p.read_text(encoding="utf-8") if p.exists() else ""
def timestamp(p):
    m=re.search(r'(?:Generated|Last generated):\s*\*\*([^*]+)\*\*',read(p),re.I); return m.group(1) if m else "not available"
def report_source_sha(text):
    m=re.search(r'Source playlist SHA-256:\s*\*\*([a-f0-9]{64})\*\*',text,re.I)
    return m.group(1).lower() if m else ""
def report_url_inventory_sha(text):
    m=re.search(r'Stream URL inventory SHA-256:\s*\*\*([a-f0-9]{64})\*\*',text,re.I)
    return m.group(1).lower() if m else ""
def url_inventory_sha(text):
    urls=sorted(line.strip() for line in text.splitlines() if line.strip().startswith(("http://","https://")))
    return hashlib.sha256("\n".join(urls).encode("utf-8")).hexdigest()
REVIEW_GROUPS={"backup","not playing","test"}
def normalized_identity_name(value):
    value = re.sub(r"\s*(?:\[[^]]*(?:geo[- ]?blocked)[^]]*\]|\((?:\d{3,4}[pi]|UHD|FHD|HD|SD)\)|\s+(?:\d{3,4}[pi]))\s*$", "", str(value or "").strip(), flags=re.I)
    value = re.sub(r"\s+", " ", value).strip()
    aliases = {"disney channel (india)": "Disney Channel India", "disney channel india": "Disney Channel India", "gazi tv": "G TV", "g tv": "G TV", "nick": "Nickelodeon (India)", "nickelodeon (india)": "Nickelodeon (India)"}
    return aliases.get(value.casefold(), value).casefold()
def parse(path=PLAYLIST):
    lines=Path(path).read_text(encoding="utf-8-sig").splitlines(); rows=[]; cur=None
    for line in lines:
        if line.startswith("#EXTINF:"): cur=dict(re.findall(r'([\w-]+)="([^"]*)"',line)); cur["_name"]=(cur.get("tvg-name") or line.rsplit(",",1)[-1]).strip()
        elif cur and line.strip().startswith(("http://","https://")): rows.append(cur|{"url":line.strip()}); cur=None
    return rows
def playlist_counts(path):
    rows=parse(path)
    ids={((x.get("tvg-id") or x.get("channel-id") or "").strip().casefold())
         for x in rows if (x.get("tvg-id") or x.get("channel-id") or "").strip()
         and x.get("group-title","").strip().casefold() not in REVIEW_GROUPS}
    return len(rows),len(ids)
def main():
    e=parse(); a=read(AUDIT); g=read(EPG); egd=read(EPG_DETAIL); h=read(HEALTH); gate=read(GATE)
    source_sha=hashlib.sha256(PLAYLIST.read_bytes()).hexdigest()
    audit_current=report_source_sha(a)==source_sha
    gate_current=report_source_sha(gate)==source_sha
    health_current=report_url_inventory_sha(h)==url_inventory_sha(PLAYLIST.read_text(encoding="utf-8-sig"))
    # Base the dashboard on the published artefact, not the legacy rights flag.
    # The owner override is EPG_ALLOW_UNVERIFIED_SOURCES; it does not prove
    # upstream redistribution rights, but an actual guide can still be audited.
    epg_current=False
    freshness_text=read(EPG_FRESHNESS)
    freshness_pass=bool(re.search(r"(?im)^Status:\s*\*\*PASS\*\*\s*$", freshness_text))
    if EPG_GUIDE.is_file() and EPG_GUIDE.stat().st_size>0 and freshness_pass:
        try:
            guide_root=ET.parse(EPG_GUIDE).getroot()
            epg_current=(guide_root.tag=="tv" and guide_root.find("channel") is not None
                         and guide_root.find("programme") is not None)
        except (OSError, ET.ParseError):
            epg_current=False
    for playlist_name, playlist_path in (
        ("IPTV-Playlist.m3u", ROOT/"IPTV-Playlist.m3u"),
        ("BDIX-Playlist.m3u", ROOT/"BDIX-Playlist.m3u"),
        ("International-Playlist.m3u", ROOT/"International-Playlist.m3u"),
    ):
        row=re.search(r'^\|\s*'+re.escape(playlist_name)+r'\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|',egd,re.M)
        current_rows,current_ids=playlist_counts(playlist_path)
        if not row or (int(row.group(1)),int(row.group(2)))!=(current_rows,current_ids):
            epg_current=False
    gm=re.search(r'Status:\\s*\\*\\*(PASS|BLOCK)\\*\\*',gate)
    gate_status=(gm.group(1) if gm else "UNKNOWN") if gate_current else "STALE / UNKNOWN"
    groups=Counter(x.get("group-title","") for x in e)
    active_groups={"Bangladesh","Indian Bangla","Indian Movies","Indian Music","Indian Entertainment","Pakistani","International","Documentary & Wildlife","Kids","Religious","Sports"}
    active=len({x.get("tvg-id") or x.get("channel-id") for x in e if x.get("group-title") in active_groups and (x.get("tvg-id") or x.get("channel-id"))})
    primary_streams=sum(1 for x in e if x.get("group-title") in active_groups)
    local=metric(a,"Healthy/local references") if audit_current else 0
    logos=round(local*100/len(e),1) if e and audit_current else 0
    logos_value=f"{logos}%" if audit_current else "STALE"
    id_names=defaultdict(set); name_ids=defaultdict(set)
    for x in e:
        cid=(x.get("tvg-id") or x.get("channel-id") or "").strip().casefold()
        name=normalized_identity_name(x.get("_name",""))
        if cid and name:
            id_names[cid].add(name)
            name_ids[name].add(cid)
    cross_queue_id_variants=sum(1 for names in id_names.values() if len(names)>1)
    cross_queue_name_collisions=sum(1 for ids in name_ids.values() if len(ids)>1)
    issues=sum(metric(a,k) for k in ["Duplicate stream URLs","Metadata conflicts","Cross-country backup collisions","Protected primary-entry changes","Logo exceptions","Duplicate primary identities","Primary channel-number collisions","Primary entries missing channel numbers","Malformed EXTINF entries","Category block-order issues","Alphabetical ordering issues"]) if audit_current else None
    issues_value=issues if issues is not None else "STALE / UNKNOWN"
    def audit_metric(label):
        value=metric(a,label)
        return value if audit_current else f"STALE / UNKNOWN (last saved: {value})"
    hfail=metric(h,"Failed this check") if health_current else None
    hpersist=metric(h,"Persistent failures (3+ consecutive)") if health_current else None
    htested=metric(h,"Streams tested") if health_current else None
    hnear=metric(h,"Near-duplicate URL families") if health_current else None
    health_fail_value=hfail if hfail is not None else "STALE"
    health_persist_value=hpersist if hpersist is not None else "STALE"
    health_tested_value=htested if htested is not None else "STALE"
    total_match=re.search(r'Active unique playlist channel IDs audited:\s*\*\*(\d+)\*\*',g,re.I)
    mapping_match=re.search(r'IDs with an EPG source mapping:\s*\*\*(\d+)/(\d+) \(([\d.]+)%\)\*\*',g,re.I)
    current_match=re.search(r'IDs with usable current/future (?:English programme data|source schedules \(nonblank (?:English|allowed-language) titles\)):\s*\*\*(\d+)/(\d+) \(([\d.]+)%\)\*',g,re.I)
    missing_match=re.search(r'IDs with no EPG source mapping:\s*\*\*(\d+)\*\*',g,re.I)
    iptv_row=re.search(r'^\|\s*IPTV-Playlist\.m3u\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|',egd,re.M)
    if iptv_row:
        india=int(iptv_row.group(2)); mapped=int(iptv_row.group(3)); source_live=int(iptv_row.group(4)); present=int(iptv_row.group(5)); live=int(iptv_row.group(6)); missing=int(iptv_row.group(7)); mapct=round(mapped*100/india,1) if india else 0.0; livepct=round(live*100/india,1) if india else 0.0; epg_scope="IPTV-Playlist.m3u published-guide row"
    else:
        india=int(total_match.group(1)) if total_match else metric(g,"Active Indian channels audited"); mapped=int(mapping_match.group(1)) if mapping_match else metric(g,"Channels with an EPG mapping"); missing=int(missing_match.group(1)) if missing_match else metric(g,"No guide mapping found"); live=int(current_match.group(1)) if current_match else 0; livepct=float(current_match.group(3)) if current_match else 0.0; mapct=float(mapping_match.group(3)) if mapping_match else (round(mapped*100/india,1) if india else 0); epg_scope="combined EPG report fallback (IPTV-only row unavailable)"
    now=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    epg_map_value=f"{mapped} ({mapct}%)" if epg_current else "PENDING — no current validated guide"
    epg_live_value=f"{live}/{india} ({livepct}%)" if epg_current else "PENDING — no current validated guide"
    epg_coverage_card=f"{round(livepct)}%" if epg_current else "PENDING"
    audit_freshness="CURRENT" if audit_current else "STALE"
    gate_freshness="CURRENT" if gate_current else "STALE"
    health_freshness="CURRENT" if health_current else "STALE"
    epg_freshness="CURRENT" if epg_current else "PENDING — guide missing or freshness not PASS"
    try: hist=json.loads(HISTORY.read_text(encoding="utf-8")); hist=hist[-30:] if isinstance(hist,list) else []
    except (OSError, UnicodeError, json.JSONDecodeError): hist=[]
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
| IPTV Local Logos | **{logos_value}** |
| IPTV EPG Programme Coverage | **{epg_coverage_card}** |
| IPTV EPG Mapping | **{"%.1f%%" % mapct if epg_current else "PENDING"}** |
| Stream Health Tested | **{health_tested_value}** |
| Stream Health Failures | **{health_fail_value}** |
| Persistent Failures | **{health_persist_value}** |
| Near-Duplicate URL Families | **{hnear if health_current else "STALE / UNKNOWN"}** |
| Audit Blocking Issues | **{issues_value}** |
| Pre-Publish Gate | **{gate_status}** |
| Pre-Publish Gate Generated | **{timestamp(GATE)}** |

## Quality Controls{" " if audit_current else " (STALE / UNKNOWN — saved audit values shown for reference)"}
- Duplicate stream URLs: **{audit_metric("Duplicate stream URLs")}**
- Metadata conflicts (canonical primary scope): **{audit_metric("Metadata conflicts")}**
- Same-name / different-ID collisions (canonical primary scope): **{audit_metric("Same-name / different-ID collisions")}**
- Cross-queue metadata identity variants: **{cross_queue_id_variants}**
- Cross-queue same-name / different-ID collisions: **{cross_queue_name_collisions}**
- Duplicate primary identities: **{audit_metric("Duplicate primary identities")}**
- Primary channel-number collisions: **{audit_metric("Primary channel-number collisions")}**
- Primary entries missing channel numbers: **{audit_metric("Primary entries missing channel numbers")}**
- Logo exceptions: **{audit_metric("Logo exceptions")}**
- Malformed EXTINF entries: **{audit_metric("Malformed EXTINF entries")}**
- Category block-order issues: **{audit_metric("Category block-order issues")}**
- Alphabetical ordering issues: **{audit_metric("Alphabetical ordering issues")}**
- Signed/tokenized URLs: **{audit_metric("Signed/tokenized stream URLs")}**

## Safety & Automation
- Stream health is non-destructive and keeps per-URL failure history.
- Backup streams are never automatically deleted because of health failures.
- `New Channels` and `New Backup` are active review queues used by discovery and validation; they are not retired categories.
- Pre-publish gate status: **{gate_status}**
- Canonical channel identity index: reports/channel-identity-index.json

## Counting Scope
- **Active Channel Identities / Active Primary Streams** count only canonical playlist groups.
- `New Channels`, `New Backup`, and `Not Playing` are review queues and are excluded from the active-primary count.
- EPG identity/programme coverage is reported only when the published XMLTV is valid, current, and its freshness report is PASS.
- **Backup Stream Entries** count playlist rows, not independent CDN/origin infrastructures. Backup independence is reviewed separately.

## EPG
- EPG IDs audited: **{india if epg_current else "PENDING — guide not current"}**
- Mapped: **{epg_map_value}**
- Current/future programme coverage: **{epg_live_value}**
- No mapping: **{missing if epg_current else "PENDING — guide not current"}**
- EPG metric scope: **{epg_scope + (" (verified against all three current playlist inventories)" if epg_current else " (awaiting a valid, fresh published guide)") }**
- Upstream source-rights reviews remain unresolved; technical guide validation does not itself establish redistribution permission. See `epg/source-rights-register.csv`.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **{timestamp(AUDIT)}** | **{audit_freshness}** |
| EPG coverage / three-playlist inventory | **{timestamp(EPG_DETAIL)}** | **{epg_freshness}** |
| Stream health | **{timestamp(HEALTH)}** | **{health_freshness}** |
| Pre-publish gate | **{timestamp(GATE)}** | **{gate_freshness}** |

## Maintenance History
- Records retained: **{len(hist)}**
- Latest entries change: **{prev.get("entries","—")} → {cur.get("entries","—")}**
- Latest health failures: **{prev.get("health_failures","—")} → {cur.get("health_failures","—")}**

Historical records are retained in reports/maintenance-history.json.
"""
    OUT_MD.write_text(md,encoding="utf-8")
    def t(x,y,s,size=15,b=False): return f'<text x="{x}" y="{y}" font-family="Arial,Helvetica,sans-serif" font-size="{size}px" font-weight="{"700" if b else "400"}" fill="#1f2937">{html.escape(str(s))}</text>'
    cards=[("Streams",len(e)),("Channel Identities",active),("Bangladesh",groups.get("Bangladesh",0)),("India",sum(v for k,v in groups.items() if k.startswith("Indian "))),("Backup Entries",groups.get("Backup",0)),("IPTV Local Logos",logos_value),("IPTV EPG Coverage",epg_coverage_card),("Health Failures",health_fail_value)]
    parts=['<svg xmlns="http://www.w3.org/2000/svg" width="980" height="650" viewBox="0 0 980 650">','<rect width="980" height="650" rx="24" fill="#f8fafc"/>','<rect width="980" height="92" rx="24" fill="#111827"/>',t(42,45,"BDIX-IPTV • PROJECT DASHBOARD",25,True),t(42,70,"Freshness checked • stale metrics labelled",13)]
    for (lab,val),(x,y) in zip(cards,[(34,120),(268,120),(502,120),(736,120),(34,260),(268,260),(502,260),(736,260)]): parts += [f'<rect x="{x}" y="{y}" width="210" height="112" rx="18" fill="white" stroke="#e5e7eb"/>',t(x+18,y+34,lab,14),t(x+18,y+78,val,28,True)]
    parts += ['<rect x="34" y="400" width="912" height="190" rx="18" fill="white" stroke="#e5e7eb"/>',t(58,435,"Current quality status",18,True),t(58,470,f"Audit blocking issues: {issues_value}",15),t(58,498,f"Pre-publish gate: {gate_status}",15),t(58,526,f"Health failures: {health_fail_value} • persistent: {health_persist_value}",15),t(58,554,f"Generated: {now}",13),'</svg>']
    OUT_SVG.write_text("".join(parts),encoding="utf-8")
    OUT_MAINT.write_text(f"""# IPTV Maintenance Report

_Generated: **{now}**_

Source playlist SHA-256: **{source_sha}**

| Item | Result |
|---|---:|
| Current playlist streams | **{len(e)}** |
| Active channel identities | **{active}** |
| Backup stream entries | **{groups.get("Backup",0)}** |
| EPG IDs audited | **{india if epg_current else "PENDING — guide not current"}** |
| Logo exceptions | **{metric(a,"Logo exceptions") if audit_current else "STALE / UNKNOWN"}** |
| EPG mapping | **{"%.1f%%" % mapct if epg_current else "PENDING — guide not current"}** |
| EPG programme coverage | **{epg_coverage_card}** |
| Health failures | **{health_fail_value}** |
| Persistent health failures | **{health_persist_value}** |
| Audit blockers | **{issues_value}** |
| Pre-publish gate | **{gate_status}** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- New Channels and New Backup remain active discovery/review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current three-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
""",encoding="utf-8")
if __name__=="__main__": main()
