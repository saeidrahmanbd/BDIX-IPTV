#!/usr/bin/env python3
"""Build and continuously improve EPG mappings from public XMLTV sources."""
import csv, gzip, io, json, re, urllib.request
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path

PLAYLIST = Path("IPTV-Playlist.m3u")
MAPPING = Path("reports/epg-india-channel-mapping.csv")
EPG_PUBLIC_URL = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/epg/epg.xml"
EPG_PUBLISHED_PATH = Path("epg/epg.xml")

EPG_ALIASES = {
    "DDHimachalPradesh.in@SD": ["ts1217", "1217", "LIVETV_LIVETVCHANNEL_DD_SHIMLA"],
    "MTVIndia.in@SD": ["jtv248", "248"], "MusicMastii.in": ["jtv584", "584", "IN4#MASTII.in"],
    "KappaTV.in@ALT1": ["jtv786", "786", "377"], "IqraBangla.uk": ["3914"], "DeenTV.uk": ["1235"],
    "ATNBanglaUK.uk": ["6753"], "TamilanTV.in": ["jtv2958", "2958"],
    "SonyKALHindi.us": ["US1#Sony.KAL.us"], "custom.bdix.aakashaath": ["AakaashAath.in@SD"],
    "custom.bdix.abpananda": ["ABPAnanda.in@SD"], "custom.abp.ananda": ["ABPAnanda.in@SD"],
    "custom.bdix.9bangla": ["TV9Bangla.in@SD"], "custom.ctvn.akd.plus": ["CTVNAKDPlus.in@SD"],
    "RepublicBangla.in": ["RepublicBangla.in@SD"], "custom.anmol.cinema": ["AnmolCinema.in@SD", "Zee.Anmol.Cinema.Today.Movies.in2"],
    "custom.anmol.cinema.2": ["AnmolCinema2.in@SD", "Zee.Anmol.Cinema.2.in2"], "custom.the.q.india": ["TheQIndia.us@SD"],
    "custom.news.18.bangla": ["News18Bangla.in@SD"], "custom.news.18.assam": ["News18AssamNorthEast.in@SD"],
    "custom.aaj.tak": ["AajTak.in@SD"], "custom.10.tv": ["10TV.in@SD"], "custom.good.news.today": ["GoodNewsToday.in@SD"],
    "custom.india.today": ["IndiaToday.in@SD"], "SETASHD": ["SonyEntertainmentTelevision.in@HD"],
    "new.and.pictures.hd": ["Andpictures.in@HD", "And.Pictures.Tv.Channel.Today.in2"], "SouthStation.in": ["SouthStation.in@HD"],
    "custom.epic": ["EpicTV.in@SD"], "custom.isai.aruvi.tv": ["IsaiAruvi.in@SD"], "custom.the.q": ["TheQIndia.us@SD"],
    "Star Gold Romance.in": ["StarGoldRomance.in@SD", "Star.Gold.Romance.Tv.Channel.Today.in2"],
    "Enterr10 Bangla.in": ["ENTER10.BANGLA.in", "Enterr10Bangla.in"], "custom.colors.infinity": ["ColorsInfinity.in@HD", "ColorsInfinity.in@SD"],
    "custom.enter10.bangla": ["Enterr10Bangla.in@SD"], "tntsports1.uk": ["TNTSport1.uk", "TNTSports1.uk", "tntsports1.uk"],
    "tntsports2.uk": ["TNTSport2.uk", "TNTSports2.uk", "tntsports2.uk"], "tntsports3.uk": ["TNTSport3.uk", "TNTSports3.uk", "tntsports3.uk"],
    "tntsports4.uk": ["TNTSport4.uk", "TNTSports4.uk", "tntsports4.uk"], "skysportsmainevent.uk": ["SkySportsMainEvent.uk", "SkySpMainEvHD.uk", "SkySpMainEv.uk"],
    "skysportspremiereleague.uk": ["SkySportsPremierLeague.uk", "SkySp.PL.HD.uk", "SkySp.PL.uk"],
}

EPG_LOCKS = {
    "ColorsCineplex.in@SD": ["543298"],
    "IqraBangla.uk": ["3914"],
    "Star.Jalsha.in": ["StarJalsha.in@SD"],
    # ATN Bangla UK is a distinct UK service. This narrow lock does not affect
    # ATNBangla.bd or any other domestic Bangladesh identity.
    "ATNBanglaUK.uk": ["6753"],
}

REPORT = Path("reports/epg-coverage.md")
THREE_PLAYLIST_REPORT = Path("reports/epg-three-playlist-audit.md")
SOURCES = [
    "https://epgshare01.online/epgshare01/epg_ripper_IN1.xml.gz", "https://epgshare01.online/epgshare01/epg_ripper_IN2.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz", "https://iptv-epg.org/files/epg-in.xml.gz",
    "https://i.mjh.nz/SamsungTVPlus/in.xml", "https://epg.pw/xmltv/epg_IN.xml",
    "https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml", "https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz",
    "https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml", "https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml",
    "https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/yupptv.xml", "https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/zee5.xml",
    "https://avkb.short.gy/epg.xml.gz", "https://avkb.short.gy/jioepg.xml.gz", "https://avkb.short.gy/tsepg.xml.gz",
    "https://raw.githubusercontent.com/nasimali/epg-auto/release/main-epg/epg_data/merged_epg.xml", "https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz",
    "https://www.open-epg.com/files/unitedkingdom.xml.gz", "https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz", "https://iptv-epg.org/files/epg-us.xml.gz",
]
ATTR_RE = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
def attrs(s): return dict(ATTR_RE.findall(s))
def norm_name(s):
    s = str(s or "").lower(); s = re.sub(r"\b(hd|sd|uhd|fhd|tv|channel)\b", "", s); return re.sub(r"[^a-z0-9]+", "", s)
def norm_id(s): return re.sub(r"[^a-z0-9]+", "", re.sub(r"@(?:sd|hd|uhd|fhd)$", "", str(s or "").lower()))
def parse_stamp(value):
    m = re.match(r"^(\d{14})(?:\s*([+-]\d{4}))?", str(value or ""));
    if not m: return None
    try:
        dt = datetime.strptime(m.group(1), "%Y%m%d%H%M%S"); off = m.group(2)
        if off:
            mins = int(off[1:3]) * 60 + int(off[3:5]); dt = dt.replace(tzinfo=timezone(timedelta(minutes=(mins if off[0] == "+" else -mins))))
        else: dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except ValueError: return None

PLAYLISTS = [Path("IPTV-Playlist.m3u"), Path("BDIX-Playlist.m3u")]
INACTIVE_GROUPS = {"Backup", "Test", "Not Playing", "New Backup", "New Channels"}

def parse_playlist():
    combined = {}
    for playlist_path in PLAYLISTS:
        if not playlist_path.exists(): continue
        lines = playlist_path.read_text(encoding="utf-8-sig").splitlines(); cur = None
        for line in lines:
            if line.startswith("#EXTINF:"):
                a = attrs(line); cur = {"tvg_id": a.get("tvg-id", "").strip(), "name": a.get("tvg-name", "").strip() or line.rsplit(",", 1)[-1].strip(), "group": a.get("group-title", "").strip(), "country": a.get("tvg-country", "").strip().upper()}
            elif cur and line.strip().startswith(("http://", "https://")):
                if cur["tvg_id"] and cur["group"] not in INACTIVE_GROUPS:
                    cid, name = cur["tvg_id"], cur["name"]
                    if cid not in combined: combined[cid] = {**cur, "aliases": [name]}
                    elif name and name not in combined[cid]["aliases"]: combined[cid]["aliases"].append(name)
                cur = None
    return sorted(combined.values(), key=lambda x: (x["group"], x["name"].lower(), x["tvg_id"]))

def fetch_source(url):
    req = urllib.request.Request(url, headers={"User-Agent": "BDIX-IPTV-EPG-Maintenance/4.0", "Accept": "application/xml,text/xml,application/gzip,*/*"})
    with urllib.request.urlopen(req, timeout=45) as r: data = r.read()
    if url.endswith(".gz") or data[:2] == b"\x1f\x8b": data = gzip.decompress(data)
    ids=set(); future=set(); counts=defaultdict(int); names=defaultdict(set); now=datetime.now(timezone.utc)
    for _, elem in ET.iterparse(io.BytesIO(data), events=("end",)):
        if elem.tag == "channel":
            cid=elem.attrib.get("id","").strip()
            if cid:
                ids.add(cid)
                for dn in elem.findall("display-name"):
                    if dn.text: names[norm_name(dn.text)].add(cid)
        elif elem.tag == "programme":
            cid=elem.attrib.get("channel","").strip()
            if cid:
                counts[cid]+=1; st=parse_stamp(elem.attrib.get("start","")); sp=parse_stamp(elem.attrib.get("stop",""))
                if (st and st>=now) or (st and sp and st<=now<=sp) or (sp and sp>=now): future.add(cid)
            elem.clear()
    return ids,future,counts,names

def load_previous():
    out={}
    if not MAPPING.exists(): return out
    with MAPPING.open(encoding="utf-8-sig",newline="") as fh:
        for r in csv.DictReader(fh):
            if r.get("tvg_id"): out[r["tvg_id"]]=r
    return out

def main():
    channels=parse_playlist(); previous=load_previous(); source_data=[]; source_status=[]
    for src in SOURCES:
        try:
            data=fetch_source(src); source_data.append(data); ids,future,counts,names=data; source_status.append((src,"OK",len(ids),len(future),sum(counts.values()),""))
        except Exception as exc:
            source_data.append((set(),set(),defaultdict(int),defaultdict(set))); source_status.append((src,"FAILED",0,0,0,str(exc)[:220]))
    rows=[]
    for ch in channels:
        candidates=[]; prev=previous.get(ch["tvg_id"],{}); locked_ids=EPG_LOCKS.get(ch["tvg_id"]); is_bangladesh=ch["group"].strip()=="Bangladesh"
        if locked_ids: candidates=list(dict.fromkeys(x.strip() for x in locked_ids if x.strip()))
        elif is_bangladesh: candidates=[]
        else:
            candidates += [x.strip() for x in (prev.get("epg_id","").split("|") if prev.get("epg_id") else []) if x.strip()]
            candidates += [ch["tvg_id"], re.sub(r"@(?:sd|hd|uhd|fhd)$","",ch["tvg_id"],flags=re.I)] + EPG_ALIASES.get(ch["tvg_id"], [])
            candidates=list(dict.fromkeys(x for x in candidates if x))
        normalized={norm_id(x) for x in candidates}; name_keys={norm_name(x) for x in ch.get("aliases",[ch["name"]]) if norm_name(x)}
        hits=[]; hit_sources=[]; total=0; live=False; best_live=[]
        for src,data in zip(SOURCES,source_data):
            ids,future,counts,names=data
            if is_bangladesh and not locked_ids: src_hits=[]
            else:
                src_hits=[x for x in candidates if x in ids]
                if not src_hits: src_hits=[x for x in ids if norm_id(x) in normalized]
                if not src_hits:
                    name_hits=set()
                    for name_key in name_keys: name_hits.update(names.get(name_key,set()))
                    src_hits=sorted(name_hits)
            if src_hits:
                hit_sources.append(src)
                for cid in src_hits:
                    if cid not in hits: hits.append(cid)
                    total += counts.get(cid,0)
                    if cid in future: best_live.append(cid); live=True
        old_epg=prev.get("epg_id","").strip()
        if is_bangladesh and not locked_ids: epg_id=""; old_epg=""
        elif ch["group"]=="Indian Bangla": epg_id=(best_live[0] if best_live else (hits[0] if hits else old_epg))
        else: epg_id=(best_live[0] if best_live else (hits[0] if hits else old_epg))
        if live: status="MAPPED"
        elif hits: status="MAPPED_ID_ONLY" if total==0 else "MAPPED_ENDED"
        elif old_epg: status="MAPPED_NOT_CURRENTLY_FOUND"
        else: status="NO_GUIDE_HIT"
        rows.append({"group":ch["group"],"channel":ch["name"],"tvg_id":ch["tvg_id"],"epg_id":epg_id,"source":" | ".join(hit_sources),"status":status,"note":"Auto-maintained; verify ambiguous/name matches manually."})

    MAPPING.parent.mkdir(parents=True,exist_ok=True)
    with MAPPING.open("w",encoding="utf-8",newline="") as fh:
        w=csv.DictWriter(fh,fieldnames=["group","channel","tvg_id","epg_id","source","status","note"]); w.writeheader(); w.writerows(sorted(rows,key=lambda r:(r["group"],r["channel"])))

    india=[r for r in rows if r["group"].startswith("Indian")]; mapped=[r for r in india if r["epg_id"]]; live=[r for r in india if r["status"]=="MAPPED"]; no_hit=[r for r in india if r["status"]=="NO_GUIDE_HIT"]
    lines=["# EPG Coverage & Mapping Report","",f"Generated: **{datetime.now(timezone.utc).isoformat(timespec='seconds')}**","","The automation maps playlist identities to available public XMLTV IDs, preserves previously verified mappings, and reports current/future programme coverage.",f"The published XMLTV guide is **{EPG_PUBLISHED_PATH.as_posix()}**, generated from this same mapping and referenced by the playlist header via **url-tvg** and **x-tvg-url**.","","## Coverage Summary","",f"- Active Indian channels audited: **{len(india)}**",f"- Channels with an EPG mapping: **{len(mapped)}**",f"- Current/future programme coverage: **{len(live)}/{len(india)} ({round(len(live)/len(india)*100,1) if india else 0}%)**",f"- No guide mapping found: **{len(no_hit)}**","","## Source Status",""]
    for src,status,ids,future,programmes,error in source_status: lines.append(f"- **{status}** — {src} — {ids} channel IDs; {future} current/future IDs; {programmes} programme rows"+(f"; {error}" if error else ""))
    lines += ["","## Channels Requiring Attention","","| Group | Channel | Playlist ID | EPG ID | Status |","|---|---|---|---|---|"]
    for r in sorted([x for x in india if x["status"]!="MAPPED"],key=lambda z:(z["status"],z["channel"])): lines.append(f'| {r["group"]} | {r["channel"]} | {r["tvg_id"]} | {r["epg_id"] or "-"} | {r["status"]} |')

    REPORT.parent.mkdir(parents=True,exist_ok=True)
    if EPG_PUBLISHED_PATH.exists() and EPG_PUBLISHED_PATH.stat().st_size>0:
        try:
            guide_root=ET.parse(EPG_PUBLISHED_PATH).getroot(); guide_channels={c.attrib.get("id","").strip() for c in guide_root.findall("channel") if c.attrib.get("id","").strip()}; mapped_targets={r["epg_id"] for r in rows if r["epg_id"]}; guide_live=set(); now_guide=datetime.now(timezone.utc)
            for prog in guide_root.findall("programme"):
                cid=prog.attrib.get("channel","").strip(); start=parse_stamp(prog.attrib.get("start","")); stop=parse_stamp(prog.attrib.get("stop","")) if prog.attrib.get("stop") else None
                if cid and start and (start>=now_guide or (stop and start<=now_guide<=stop) or (stop and stop>=now_guide)): guide_live.add(cid)
            header=next((line for line in PLAYLIST.read_text(encoding="utf-8-sig").splitlines() if line.startswith("#EXTM3U")),""); refs=re.findall(r'(?:url-tvg|x-tvg-url)="([^"]+)"',header); expected=EPG_PUBLIC_URL
            present_ids=mapped_targets & guide_channels; live_ids=mapped_targets & guide_live; missing=sorted(mapped_targets-guide_channels); without_live=sorted((mapped_targets&guide_channels)-guide_live)
            lines += ["","## Published Guide Validation","",f"- Published guide path: **{EPG_PUBLISHED_PATH}**",f"- Playlist EPG references: **{'OK' if refs and all(u==expected for u in refs) else 'MISMATCH'}**",f"- Guide channel IDs published: **{len(guide_channels)}**",f"- Mapped playlist IDs present in guide: **{len(present_ids)}/{len(mapped_targets)} ({round(len(present_ids)*100/len(mapped_targets),1) if mapped_targets else 0}%)**",f"- Mapped playlist IDs with current/future programmes: **{len(live_ids)}/{len(mapped_targets)} ({round(len(live_ids)*100/len(mapped_targets),1) if mapped_targets else 0}%)**",f"- Mapped IDs missing from the published XMLTV channel list: **{len(missing)}**","- IDs missing from guide: "+(", ".join(missing) if missing else "none"),f"- Mapped IDs with no current/future programmes: **{len(without_live)}**","- IDs without current/future programmes (first 30): "+(", ".join(without_live[:30]) if without_live else "none")]
        except Exception as exc: lines += ["","## Published Guide Validation","",f"- Validation: **ERROR** — {str(exc)[:220]}"]
    else: lines += ["","## Published Guide Validation","",f"- Validation: **ERROR** — {EPG_PUBLISHED_PATH} is missing or empty"]
    REPORT.write_text("\n".join(lines)+"\n",encoding="utf-8")

if __name__=="__main__": main()
