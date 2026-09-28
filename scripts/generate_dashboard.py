#!/usr/bin/env python3
import re, html
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PLAYLIST=ROOT/"IPTV-Playlist.m3u"
AUDIT=ROOT/"reports/playlist-audit.md"
HEALTH=ROOT/"reports/stream-health.md"
EPG=ROOT/"reports/epg-coverage.md"
OUT_MD=ROOT/"reports/dashboard.md"
OUT_SVG=ROOT/"assets/dashboard.svg"

ATTR_RE=re.compile(r'([\w-]+)="([^"]*)"')

def attrs(s): return dict(ATTR_RE.findall(s))
def num(text,label):
    m=re.search(r'- '+re.escape(label)+r': \*\*(\d+)\*\*',text)
    return int(m.group(1)) if m else 0
def parse_playlist():
    lines=PLAYLIST.read_text(encoding="utf-8-sig").splitlines()
    entries=[]; i=0
    while i<len(lines):
        if lines[i].startswith("#EXTINF:"):
            a=attrs(lines[i]); name=(a.get("tvg-name") or lines[i].rsplit(",",1)[-1]).strip()
            url=lines[i+1].strip() if i+1<len(lines) else ""
            if url.startswith(("http://","https://")):
                entries.append((a.get("tvg-id",""),name,a.get("group-title",""),a.get("tvg-logo",""),url))
            i+=1
        i+=1
    return entries
def audit_stats():
    s=AUDIT.read_text(encoding="utf-8")
    return {k:num(s,k) for k in ["Playlist entries","Unique channel IDs","Duplicate stream URLs","Metadata conflicts","Same-name / different-ID collisions","Cross-country backup collisions","IDs with multiple logo references","Logo exceptions"]}
def report_stats(path):
    if not path.exists(): return {}
    s=path.read_text(encoding="utf-8")
    out={}
    for k in ["Healthy","Redirect/temporary","Timeout","HTTP error","Invalid HLS","Connection error","Not Playing","Repeated-failure candidates (>= 3 runs)","Unique stream URLs checked","EPG matched","EPG missing","Exact ID matches","Alias/name matches","Matched with future programme data"]:
        out[k]=num(s,k)
    return out
def svg_text(x,y,text,size=15,bold=False):
    esc=html.escape(str(text))
    weight="700" if bold else "400"
    return f'<text x="{x}" y="{y}" font-family="Arial,Helvetica,sans-serif" font-size="{size}px" font-weight="{weight}" fill="#1f2937">{esc}</text>'
def make_svg(total,channels,bangla,india,backup,logos,epg_match,epg_missing,health):
    healthy=health.get("Healthy",0)+health.get("Redirect/temporary",0)
    checked=health.get("Unique stream URLs checked",0)
    pct=round(100*healthy/checked) if checked else 0
    w,h=980,610
    parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
           '<rect width="980" height="610" rx="24" fill="#f8fafc"/>',
           '<rect x="0" y="0" width="980" height="92" rx="24" fill="#111827"/>',
           svg_text(42,45,"BDIX-IPTV • LIVE PROJECT DASHBOARD",25,True),
           '<text x="42" y="70" font-family="Arial,Helvetica,sans-serif" font-size="13px" fill="#cbd5e1">Automatically generated from the current repository state</text>']
    cards=[("Streams",total),("Channels",channels),("Bangladesh",bangla),("India",india),("Backup Streams",backup),("Logos",f"{logos}%"),("EPG Coverage",f"{epg_match}%"),("Stream Health",f"{pct}%")]
    coords=[(34,120),(268,120),(502,120),(736,120),(34,260),(268,260),(502,260),(736,260)]
    for (label,val),(x,y) in zip(cards,coords):
        parts += [f'<rect x="{x}" y="{y}" width="210" height="112" rx="18" fill="white" stroke="#e5e7eb"/>',
                  svg_text(x+18,y+34,label,14,False),svg_text(x+18,y+78,val,28,True)]
    parts += [f'<rect x="34" y="400" width="912" height="170" rx="18" fill="white" stroke="#e5e7eb"/>',
              svg_text(58,435,"Operational status",18,True),
              svg_text(58,468,f"EPG missing: {epg_missing}",15),
              svg_text(58,496,f"Stream health: {healthy}/{checked} reachable",15),
              svg_text(58,524,f"Generated: {datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")}",13),
              '</svg>']
    return "".join(parts)
def main():
    e=parse_playlist(); a=audit_stats(); h=report_stats(HEALTH); g=report_stats(EPG)
    groups=Counter(x[2] for x in e)
    total=len(e); channels=len(set(x[0] for x in e if x[0]))
    bangla=groups.get("Bangladesh",0)
    india=sum(v for k,v in groups.items() if k.startswith("Indian "))
    backup=groups.get("Backup",0)
    logos=100 if total and all(x[3].startswith("https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/") and x[3].lower().endswith(".png") for x in e) else 0
    epg_matched=g.get("EPG matched",0); epg_missing=g.get("EPG missing",0)
    epg_pct=round(100*epg_matched/channels) if channels else 0
    OUT_MD.parent.mkdir(parents=True,exist_ok=True); OUT_SVG.parent.mkdir(parents=True,exist_ok=True)
    now=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    md=f"""# Live Project Dashboard

_Last generated: **{now}**_

| Metric | Current |
|---|---:|
| 📺 Streams | **{total}** |
| 📡 Channels | **{channels}** |
| 🇧🇩 Bangladesh | **{bangla}** |
| 🇮🇳 India | **{india}** |
| 🔁 Backup Streams | **{backup}** |
| 🖼️ Logos | **{logos}%** |
| 📅 EPG Coverage | **{epg_pct}%** |
| 🟢 Stream Health | **{round(100*(h.get("Healthy",0)+h.get("Redirect/temporary",0))/h.get("Unique stream URLs checked",1))}%** |

## Quality Controls

- Duplicate stream URLs: **{a["Duplicate stream URLs"]}**
- Metadata conflicts: **{a["Metadata conflicts"]}**
- Same-name collisions: **{a["Same-name / different-ID collisions"]}**
- Cross-country Backup collisions: **{a["Cross-country backup collisions"]}**
- EPG missing: **{epg_missing}**
- Repeated-failure stream candidates: **{h.get("Repeated-failure candidates (>= 3 runs)",0)}**

This file is generated automatically. It is safe for the Wiki to display as a live dashboard source.
"""
    OUT_MD.write_text(md,encoding="utf-8")
    OUT_SVG.write_text(make_svg(total,channels,bangla,india,backup,logos,epg_pct,epg_missing,h),encoding="utf-8")
    print(md)
if __name__=="__main__": main()
