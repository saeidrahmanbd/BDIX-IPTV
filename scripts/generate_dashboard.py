#!/usr/bin/env python3
import re, html
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PLAYLIST=ROOT/"IPTV-Playlist.m3u"
AUDIT=ROOT/"reports/playlist-audit.md"
EPG=ROOT/"reports/epg-coverage.md"
OUT_MD=ROOT/"reports/dashboard.md"
OUT_SVG=ROOT/"assets/dashboard.svg"
ATTR_RE=re.compile(r'([\\w-]+)="([^"]*)"')

def attrs(s): return dict(ATTR_RE.findall(s))
def num(text,label):
    m=re.search(r'- '+re.escape(label)+r': \\*\\*(\\d+)\\*\\*',text)
    return int(m.group(1)) if m else 0
def parse_playlist():
    lines=PLAYLIST.read_text(encoding="utf-8-sig").splitlines(); out=[]; i=0
    while i<len(lines):
        if lines[i].startswith("#EXTINF:"):
            a=attrs(lines[i]); name=(a.get("tvg-name") or lines[i].rsplit(",",1)[-1]).strip()
            url=lines[i+1].strip() if i+1<len(lines) else ""
            if url.startswith(("http://","https://")): out.append((a.get("tvg-id",""),name,a.get("group-title",""),a.get("tvg-logo",""),url,a.get("tvg-chno","")))
            i+=1
        i+=1
    return out
def audit_stats():
    s=AUDIT.read_text(encoding="utf-8") if AUDIT.exists() else ""
    labels=["Playlist entries","Unique channel IDs","Duplicate stream URLs","Metadata conflicts","Same-name / different-ID collisions","Cross-country backup collisions","IDs with multiple logo references","Protected primary-entry changes","Logo exceptions","Duplicate primary identities","Primary channel-number collisions"]
    return {k:num(s,k) for k in labels}
def epg_stats():
    s=EPG.read_text(encoding="utf-8") if EPG.exists() else ""
    out={"Indian channels":0,"Mapped":0,"Live":0,"No mapping":0}
    for key,label in [("Indian channels","Active Indian channels audited"),("Mapped","Channels with an EPG mapping"),("No mapping","No guide mapping found")]:
        out[key]=num(s,label)
    m=re.search(r'Current/future programme coverage:\s*\\*\\*(\\d+)/(\\d+) \\((\\d+(?:\\.\\d+)?)%\\)\\*\\*',s,re.I)
    if m: out["Live"]=int(m.group(1)); out["LivePct"]=float(m.group(3))
    return out
def report_timestamp(path):
    if not path.exists(): return "not available"
    s=path.read_text(encoding="utf-8")
    m=re.search(r'(?:Generated|Last generated):\\s*\\*\\*([^*]+)\\*\\*',s,re.I)
    return m.group(1).strip() if m else "not available"
def svg_text(x,y,text,size=15,bold=False):
    esc=html.escape(str(text)); weight="700" if bold else "400"
    return f'<text x="{x}" y="{y}" font-family="Arial,Helvetica,sans-serif" font-size="{size}px" font-weight="{weight}" fill="#1f2937">{esc}</text>'
def make_svg(total,channels,bangla,india,backup,logos,epg_pct,epg_missing,issues):
    w,h=980,610
    parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">','<rect width="980" height="610" rx="24" fill="#f8fafc"/>','<rect x="0" y="0" width="980" height="92" rx="24" fill="#111827"/>',svg_text(42,45,"BDIX-IPTV • PROJECT DASHBOARD",25,True),svg_text(42,70,"EPG • Metadata • Logos • Playlist Audit",13,False)]
    cards=[("Streams",total),("Channels",channels),("Bangladesh",bangla),("India",india),("Backup Streams",backup),("Local Logos",f"{logos}%"),("EPG Coverage",f"{epg_pct}%"),("Audit Issues",issues)]
    coords=[(34,120),(268,120),(502,120),(736,120),(34,260),(268,260),(502,260),(736,260)]
    for (label,val),(x,y) in zip(cards,coords):
        parts += [f'<rect x="{x}" y="{y}" width="210" height="112" rx="18" fill="white" stroke="#e5e7eb"/>',svg_text(x+18,y+34,label,14),svg_text(x+18,y+78,val,28,True)]
    parts += [f'<rect x="34" y="400" width="912" height="170" rx="18" fill="white" stroke="#e5e7eb"/>',svg_text(58,435,"Current quality status",18,True),svg_text(58,468,f"EPG unmapped: {epg_missing}",15),svg_text(58,496,f"Metadata conflicts: {issues}",15),svg_text(58,524,f"Generated: {datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")}",13),'</svg>']
    return "".join(parts)
def main():
    e=parse_playlist(); a=audit_stats(); g=epg_stats(); groups=Counter(x[2] for x in e)
    total=len(e); channels=len(set(x[0] for x in e if x[0])); bangla=groups.get("Bangladesh",0); india=sum(v for k,v in groups.items() if k.startswith("Indian ")); backup=groups.get("Backup",0)
    local_logos=sum(1 for x in e if x[3].startswith("https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/"))
    logos=round(100*local_logos/total,1) if total else 0
    epg_pct=round(g.get("LivePct",0)); epg_missing=g.get("No mapping",0)
    issues=sum(a.get(k,0) for k in ["Duplicate stream URLs","Metadata conflicts","Same-name / different-ID collisions","Cross-country backup collisions","Protected primary-entry changes","Logo exceptions","Duplicate primary identities","Primary channel-number collisions"])
    now=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    md=f"""# Project Dashboard

_Last generated: **{now}**_

| Metric | Current |
|---|---:|
| 📺 Streams | **{total}** |
| 📡 Channels | **{channels}** |
| 🇧🇩 Bangladesh | **{bangla}** |
| 🇮🇳 India | **{india}** |
| 🔁 Backup Streams | **{backup}** |
| 🖼️ Local Logos | **{logos}%** |
| 📅 EPG Coverage | **{epg_pct}%** |
| ⚠️ Audit Issues | **{issues}** |

## Quality Controls
- Duplicate stream URLs: **{a.get("Duplicate stream URLs",0)}**
- Metadata conflicts: **{a.get("Metadata conflicts",0)}**
- Same-name / different-ID collisions: **{a.get("Same-name / different-ID collisions",0)}**
- Duplicate primary identities: **{a.get("Duplicate primary identities",0)}**
- Primary channel-number collisions: **{a.get("Primary channel-number collisions",0)}**
- Logo exceptions: **{a.get("Logo exceptions",0)}**
- EPG channels without mapping: **{epg_missing}**

## Data Freshness
| Source | Last generated |
|---|---|
| Playlist audit | **{report_timestamp(AUDIT)}** |
| EPG coverage | **{report_timestamp(EPG)}** |

This dashboard intentionally does not perform or report stream-health probing.
"""
    OUT_MD.parent.mkdir(parents=True,exist_ok=True); OUT_SVG.parent.mkdir(parents=True,exist_ok=True)
    OUT_MD.write_text(md,encoding="utf-8"); OUT_SVG.write_text(make_svg(total,channels,bangla,india,backup,logos,epg_pct,epg_missing,issues),encoding="utf-8")
    print(md)
if __name__=="__main__": main()
