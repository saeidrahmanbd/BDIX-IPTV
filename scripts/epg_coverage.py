#!/usr/bin/env python3
"""Build and continuously improve EPG mappings from public XMLTV sources."""
import csv, gzip, io, re, urllib.request
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path

PLAYLIST = Path("IPTV-Playlist.m3u")
MAPPING = Path("reports/epg-india-channel-mapping.csv")
REPORT = Path("reports/epg-coverage.md")

SOURCES = [
    "https://epgshare01.online/epgshare01/epg_ripper_IN1.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz",
    "https://iptv-epg.org/files/epg-in.xml",
    "https://epg.pw/xmltv/epg_IN.xml",
    "https://m3u-edit.com/epg-source.php?file=india_dishtv.in.xml",
    "https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz",
    "https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml",
    "https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml",
    "https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/yupptv.xml",
    "https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/zee5.xml",
]
ATTR_RE = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')

def attrs(s): return dict(ATTR_RE.findall(s))
def norm_name(s):
    s = str(s or "").lower()
    s = re.sub(r"\b(hd|sd|uhd|fhd|tv|channel)\b", "", s)
    return re.sub(r"[^a-z0-9]+", "", s)
def norm_id(s):
    return re.sub(r"[^a-z0-9]+", "", re.sub(r"@(?:sd|hd|uhd|fhd)$", "", str(s or "").lower()))
def parse_stamp(value):
    m = re.match(r"^(\d{14})(?:\s*([+-]\d{4}))?", str(value or ""))
    if not m: return None
    try:
        dt = datetime.strptime(m.group(1), "%Y%m%d%H%M%S")
        off = m.group(2)
        if off:
            mins = int(off[1:3]) * 60 + int(off[3:5])
            dt = dt.replace(tzinfo=timezone(timedelta(minutes=(mins if off[0] == "+" else -mins))))
        else: dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except ValueError: return None

def parse_playlist():
    lines = PLAYLIST.read_text(encoding="utf-8-sig").splitlines()
    out=[]; cur=None
    for line in lines:
        if line.startswith("#EXTINF:"):
            a=attrs(line)
            cur={"tvg_id":a.get("tvg-id","").strip(),"name":a.get("tvg-name","").strip() or line.rsplit(",",1)[-1].strip(),
                 "group":a.get("group-title","").strip(),"country":a.get("tvg-country","").strip().upper()}
        elif cur and line.strip().startswith(("http://","https://")):
            if cur["group"] not in ("Backup","Not Playing"):
                out.append(cur)
            cur=None
    seen=set(); result=[]
    for x in out:
        key=(x["tvg_id"],x["name"],x["group"])
        if key not in seen: seen.add(key); result.append(x)
    return result

def fetch_source(url):
    req=urllib.request.Request(url,headers={"User-Agent":"BDIX-IPTV-EPG-Maintenance/4.0","Accept":"application/xml,text/xml,application/gzip,*/*"})
    with urllib.request.urlopen(req,timeout=90) as r: data=r.read()
    if url.endswith(".gz") or data[:2]==b"\x1f\x8b": data=gzip.decompress(data)
    ids=set(); future=set(); counts=defaultdict(int); names=defaultdict(set); now=datetime.now(timezone.utc)
    for _,elem in ET.iterparse(io.BytesIO(data),events=("end",)):
        if elem.tag=="channel":
            cid=elem.attrib.get("id","").strip()
            if cid:
                ids.add(cid)
                for dn in elem.findall("display-name"):
                    if dn.text: names[norm_name(dn.text)].add(cid)
        elif elem.tag=="programme":
            cid=elem.attrib.get("channel","").strip()
            if cid:
                counts[cid]+=1
                st=parse_stamp(elem.attrib.get("start","")); sp=parse_stamp(elem.attrib.get("stop",""))
                if (st and st>=now) or (st and sp and st<=now<=sp) or (sp and sp>=now): future.add(cid)
            elem.clear()
    return ids,future,counts,names

def load_previous():
    out={}
    if not MAPPING.exists(): return out
    with MAPPING.open(encoding="utf-8-sig",newline="") as fh:
        for r in csv.DictReader(fh):
            if r.get("tvg_id"):
                out[r["tvg_id"]] = r
    return out

def main():
    channels=parse_playlist(); previous=load_previous()
    source_data=[]; source_status=[]
    for src in SOURCES:
        try:
            data=fetch_source(src); source_data.append(data)
            ids,future,counts,names=data
            source_status.append((src,"OK",len(ids),len(future),sum(counts.values()),""))
        except Exception as exc:
            source_data.append((set(),set(),defaultdict(int),defaultdict(set)))
            source_status.append((src,"FAILED",0,0,0,str(exc)[:220]))

    rows=[]
    for ch in channels:
        candidates=[]
        prev=previous.get(ch["tvg_id"],{})
        candidates += [x.strip() for x in (prev.get("epg_id","").split("|") if prev.get("epg_id") else []) if x.strip()]
        candidates += [ch["tvg_id"], re.sub(r"@(?:sd|hd|uhd|fhd)$","",ch["tvg_id"],flags=re.I)]
        candidates=list(dict.fromkeys(x for x in candidates if x))
        normalized={norm_id(x) for x in candidates}; name_key=norm_name(ch["name"])
        hits=[]; hit_sources=[]; total=0; live=False
        for src,data in zip(SOURCES,source_data):
            ids,future,counts,names=data
            src_hits=[x for x in candidates if x in ids]
            if not src_hits: src_hits=[x for x in ids if norm_id(x) in normalized]
            if not src_hits: src_hits=list(names.get(name_key,set()))
            if src_hits:
                hit_sources.append(src)
                for cid in src_hits:
                    if cid not in hits: hits.append(cid)
                    total += counts.get(cid,0)
                    live = live or cid in future

        old_epg=prev.get("epg_id","").strip()
        epg_id=" | ".join(hits[:8]) or old_epg
        if live: status="MAPPED"
        elif hits: status="MAPPED_ID_ONLY" if total==0 else "MAPPED_ENDED"
        elif old_epg: status="MAPPED_NOT_CURRENTLY_FOUND"
        else: status="NO_GUIDE_HIT"
        rows.append({
            "group":ch["group"],"channel":ch["name"],"tvg_id":ch["tvg_id"],"epg_id":epg_id,
            "source":" | ".join(hit_sources),"status":status,"note":"Auto-maintained; verify ambiguous/name matches manually."
        })

    MAPPING.parent.mkdir(parents=True,exist_ok=True)
    with MAPPING.open("w",encoding="utf-8",newline="") as fh:
        w=csv.DictWriter(fh,fieldnames=["group","channel","tvg_id","epg_id","source","status","note"])
        w.writeheader(); w.writerows(sorted(rows,key=lambda r:(r["group"],r["channel"])))

    india=[r for r in rows if r["group"].startswith("Indian")]
    mapped=[r for r in india if r["epg_id"]]
    live=[r for r in india if r["status"]=="MAPPED"]
    no_hit=[r for r in india if r["status"]=="NO_GUIDE_HIT"]
    lines=[
        "# EPG Coverage & Mapping Report","",
        "Generated: **"+datetime.now(timezone.utc).isoformat(timespec="seconds")+"**","",
        "The automation maps playlist identities to available public XMLTV IDs, preserves previously verified mappings, and reports current/future programme coverage.","",
        "## Coverage Summary","",
        f"- Active Indian channels audited: **{len(india)}**",
        f"- Channels with an EPG mapping: **{len(mapped)}**",
        f"- Current/future programme coverage: **{len(live)}/{len(india)} ({round(len(live)/len(india)*100,1) if india else 0}%)**",
        f"- No guide mapping found: **{len(no_hit)}**","",
        "## Source Status",""
    ]
    for src,status,ids,future,programmes,error in source_status:
        lines.append(f"- **{status}** — {src} — {ids} channel IDs; {future} current/future IDs; {programmes} programme rows"+(f"; {error}" if error else ""))
    lines += ["","## Channels Requiring Attention","",
              "| Group | Channel | Playlist ID | EPG ID | Status |","|---|---|---|---|---|"]
    for r in sorted([x for x in india if x["status"]!="MAPPED"],key=lambda z:(z["status"],z["channel"])):
        lines.append(f'| {r["group"]} | {r["channel"]} | {r["tvg_id"]} | {r["epg_id"] or "-"} | {r["status"]} |')
    REPORT.parent.mkdir(parents=True,exist_ok=True)
    REPORT.write_text("\n".join(lines)+"\n",encoding="utf-8")
    print(f"EPG maintenance: India={len(india)} mapped={len(mapped)} live/future={len(live)} no-hit={len(no_hit)}")

if __name__=="__main__": main()
