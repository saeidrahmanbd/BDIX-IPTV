#!/usr/bin/env python3
"""Build and continuously improve EPG mappings from public XMLTV sources."""
import csv, gzip, io, json, re, unicodedata, urllib.request
import xml.etree.ElementTree as ET
from official_epg_sources import HUM_TV_SOURCE, HUM_TV_CHANNEL_ID, fetch_hum_tv_programmes
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
    "https://i.mjh.nz/SamsungTVPlus/in.xml", "https://i.mjh.nz/SamsungTVPlus/us.xml", "https://epg.pw/xmltv/epg_IN.xml",
    "https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml", "https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz",
    "https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml", "https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml",
    "https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/yupptv.xml", "https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/zee5.xml",
    "https://avkb.short.gy/epg.xml.gz", "https://avkb.short.gy/jioepg.xml.gz", "https://avkb.short.gy/tsepg.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_DISTROTV1.xml.gz", "https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_RAKUTEN1.xml.gz",
    "https://raw.githubusercontent.com/nasimali/epg-auto/release/main-epg/epg_data/merged_epg.xml", "https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz",
    "https://www.open-epg.com/files/unitedkingdom.xml.gz", "https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz", "https://iptv-epg.org/files/epg-us.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_AE1.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_AU1.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_CH1.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_CZ1.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_DE1.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_DO1.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_ES1.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_FR1.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_GR1.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_HK1.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_HU1.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_IT1.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_MY1.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_MX1.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_NL1.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_PL1.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_RO1.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_SA2.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_TR1.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_BEIN1.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_BR1.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_BR2.xml.gz",
    "https://hum.tv/schedule/",
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

def playlist_records(path):
    """Return M3U entries with stream URLs and parsed identity fields."""
    if not path.exists():
        return []
    records = []
    current = None
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        if line.startswith("#EXTINF:"):
            a = attrs(line)
            current = {
                "tvg_id": a.get("tvg-id", "").strip(),
                "name": a.get("tvg-name", "").strip() or line.rsplit(",", 1)[-1].strip(),
                "group": a.get("group-title", "").strip(),
                "country": a.get("tvg-country", "").strip().upper(),
            }
        elif current and line.strip().startswith(("http://", "https://")):
            current["url"] = line.strip()
            records.append(current)
            current = None
    return records


def header_status(path):
    """Check a playlist's declared XMLTV reference against the published guide URL."""
    if not path.exists():
        return "MISSING PLAYLIST"
    header = next((line for line in path.read_text(encoding="utf-8-sig").splitlines() if line.startswith("#EXTM3U")), "")
    refs = re.findall(r'(?:url-tvg|x-tvg-url)="([^"]+)"', header)
    if not refs:
        return "MISSING EPG HEADER"
    return "OK" if all(url == EPG_PUBLIC_URL for url in refs) else "MISMATCH"


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

def is_english_text_element(elem):
    """Match the generator's English-title policy when measuring EPG coverage."""
    text = (elem.text or "").strip()
    if not text:
        return True
    lang = (elem.attrib.get("{http://www.w3.org/XML/1998/namespace}lang") or elem.attrib.get("lang") or "").strip().lower()
    if lang and not (lang == "en" or lang == "eng" or lang.startswith("en-") or lang.startswith("en_")):
        return False
    for char in text:
        if unicodedata.category(char).startswith("L") and "LATIN" not in unicodedata.name(char, ""):
            return False
    return True


def fetch_source(url):
    if url == HUM_TV_SOURCE:
        programmes = fetch_hum_tv_programmes()
        ids = {HUM_TV_CHANNEL_ID} if programmes else set()
        future = set()
        counts = defaultdict(int)
        names = defaultdict(set)
        now = datetime.now(timezone.utc)
        for program in programmes:
            cid = program["channel_id"]
            counts[cid] += 1
            names[norm_name("Hum TV")].add(cid)
            if program["stop_dt"] >= now:
                future.add(cid)
        return ids, future, counts, names

    req = urllib.request.Request(url, headers={"User-Agent": "BDIX-IPTV-EPG-Maintenance/4.0", "Accept": "application/xml,text/xml,application/gzip,*/*"})
    with urllib.request.urlopen(req, timeout=45) as r:
        data = r.read()
    if url.endswith(".gz") or data[:2] == b"\x1f\x8b":
        data = gzip.decompress(data)
    ids = set()
    future = set()
    counts = defaultdict(int)
    names = defaultdict(set)
    now = datetime.now(timezone.utc)
    lower = now - timedelta(hours=6)
    upper = now + timedelta(days=7)
    for _, elem in ET.iterparse(io.BytesIO(data), events=("end",)):
        if elem.tag == "channel":
            cid = elem.attrib.get("id", "").strip()
            if cid:
                ids.add(cid)
                for dn in elem.findall("display-name"):
                    if dn.text:
                        names[norm_name(dn.text)].add(cid)
            elem.clear()
        elif elem.tag == "programme":
            cid = elem.attrib.get("channel", "").strip()
            start = parse_stamp(elem.attrib.get("start", ""))
            stop = parse_stamp(elem.attrib.get("stop", "")) if elem.attrib.get("stop") else None
            title = elem.find("title")
            if (
                cid and start and stop and stop > start
                and start <= upper and stop >= lower
                and title is not None and is_english_text_element(title)
            ):
                counts[cid] += 1
                if stop >= now:
                    future.add(cid)
            elem.clear()
    return ids, future, counts, names

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
        candidates=[]; prev=previous.get(ch["tvg_id"],{}); locked_ids=EPG_LOCKS.get(ch["tvg_id"]); is_bangladesh=(ch["group"].strip()=="Bangladesh" or bool(re.search(r"\.bd(?:@|$)", ch["tvg_id"], re.I)))
        if locked_ids: candidates=list(dict.fromkeys(x.strip() for x in locked_ids if x.strip()))
        elif is_bangladesh: candidates=[ch["tvg_id"]] + EPG_ALIASES.get(ch["tvg_id"], [])
        else:
            candidates += [x.strip() for x in (prev.get("epg_id","").split("|") if prev.get("epg_id") else []) if x.strip()]
            candidates += [ch["tvg_id"], re.sub(r"@(?:sd|hd|uhd|fhd)$","",ch["tvg_id"],flags=re.I)] + EPG_ALIASES.get(ch["tvg_id"], [])
            candidates=list(dict.fromkeys(x for x in candidates if x))
        normalized={norm_id(x) for x in candidates}; name_keys={norm_name(x) for x in ch.get("aliases",[ch["name"]]) if norm_name(x)}
        hits=[]; hit_sources=[]; total=0; live=False; best_live=[]
        for src,data in zip(SOURCES,source_data):
            ids,future,counts,names=data
            if is_bangladesh:
                # Safety: exact playlist IDs/explicit aliases only; never use ID normalization or name fuzzy matching.
                src_hits=[x for x in candidates if x in ids]
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
        if ch["group"]=="Indian Bangla": epg_id=(best_live[0] if best_live else (hits[0] if hits else old_epg))
        else: epg_id=(best_live[0] if best_live else (hits[0] if hits else old_epg))
        if live: status="MAPPED"
        elif hits: status="MAPPED_ID_ONLY" if total==0 else "MAPPED_ENDED"
        elif old_epg: status="MAPPED_NOT_CURRENTLY_FOUND"
        else: status="NO_GUIDE_HIT"
        rows.append({"group":ch["group"],"channel":ch["name"],"tvg_id":ch["tvg_id"],"epg_id":epg_id,"source":" | ".join(hit_sources),"status":status,"note":"Auto-maintained; verify ambiguous/name matches manually."})

    MAPPING.parent.mkdir(parents=True,exist_ok=True)
    with MAPPING.open("w",encoding="utf-8",newline="") as fh:
        w=csv.DictWriter(fh,fieldnames=["group","channel","tvg_id","epg_id","source","status","note"]); w.writeheader(); w.writerows(sorted(rows,key=lambda r:(r["group"],r["channel"])))

    group_summary = defaultdict(lambda: {"active": 0, "mapped": 0, "live": 0, "unmapped": 0})
    for row in rows:
        stats = group_summary[row["group"]]
        stats["active"] += 1
        stats["mapped"] += bool(row["epg_id"])
        stats["live"] += row["status"] == "MAPPED"
        stats["unmapped"] += not bool(row["epg_id"])

    total_active = len(rows)
    total_mapped = sum(bool(r["epg_id"]) for r in rows)
    total_live = sum(r["status"] == "MAPPED" for r in rows)
    total_unmapped = sum(not bool(r["epg_id"]) for r in rows)
    lines = [
        "# EPG Coverage & Mapping Report",
        "",
        f"Generated: **{datetime.now(timezone.utc).isoformat(timespec='seconds')}**",
        "",
        "This report audits active unique channel identities across the playlist files in the repository. A source mapping is not counted as usable current/future coverage unless it has a valid programme interval and acceptable English-title data within the generator's -6-hour/+7-day window.",
        f"The XMLTV guide is published at **{EPG_PUBLISHED_PATH.as_posix()}**. The published guide uses the playlist's tvg-id as the XMLTV channel ID, not the upstream provider's source ID.",
        "",
        "## Overall Coverage",
        "",
        f"- Active unique playlist channel IDs audited: **{total_active}**",
        f"- IDs with an EPG source mapping: **{total_mapped}/{total_active} ({round(100*total_mapped/total_active,1) if total_active else 0}%)**",
        f"- IDs with usable current/future English programme data: **{total_live}/{total_active} ({round(100*total_live/total_active,1) if total_active else 0}%)**",
        f"- IDs with no EPG source mapping: **{total_unmapped}**",
        "",
        "## Coverage by Playlist Group",
        "",
        "| Group | Active IDs | Mapped IDs | Current/future | No mapping |",
        "|---|---:|---:|---:|---:|",
    ]
    for group in sorted(group_summary):
        s = group_summary[group]
        lines.append(f"| {group} | {s['active']} | {s['mapped']} | {s['live']} | {s['unmapped']} |")

    lines += ["", "## Source Status", ""]
    for src, status, ids, future, programmes, error in source_status:
        lines.append(
            f"- **{status}** — {src} — {ids} channel IDs; {future} IDs with usable current/future programmes; {programmes} eligible English-title programme rows in the guide window"
            + (f"; {error}" if error else "")
        )

    lines += [
        "",
        "## Channels Requiring Attention",
        "",
        "The table includes every active channel identity without usable current/future guide data, not only Indian channels. NO_GUIDE_HIT means no configured source could be matched; MAPPED_ID_ONLY means an identity was found but no usable schedule was available; MAPPED_NOT_CURRENTLY_FOUND means a retained mapping was not found in the currently configured feeds.",
        "",
        "| Group | Channel | Playlist ID | EPG source ID | Status |",
        "|---|---|---|---|---|",
    ]
    for r in sorted([x for x in rows if x["status"] != "MAPPED"], key=lambda z: (z["group"], z["status"], z["channel"].lower())):
        lines.append(f'| {r["group"]} | {r["channel"]} | {r["tvg_id"]} | {r["epg_id"] or "-"} | {r["status"]} |')

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    guide_channels = set()
    guide_live = set()
    guide_programmes = 0
    guide_error = ""
    now_guide = datetime.now(timezone.utc)
    lower_guide = now_guide - timedelta(hours=6)
    upper_guide = now_guide + timedelta(days=7)
    try:
        if not EPG_PUBLISHED_PATH.exists() or EPG_PUBLISHED_PATH.stat().st_size == 0:
            raise RuntimeError(f"{EPG_PUBLISHED_PATH} is missing or empty")
        for _, elem in ET.iterparse(str(EPG_PUBLISHED_PATH), events=("end",)):
            if elem.tag == "channel":
                cid = elem.attrib.get("id", "").strip()
                if cid:
                    guide_channels.add(cid)
                elem.clear()
            elif elem.tag == "programme":
                cid = elem.attrib.get("channel", "").strip()
                start = parse_stamp(elem.attrib.get("start", ""))
                stop = parse_stamp(elem.attrib.get("stop", "")) if elem.attrib.get("stop") else None
                title = elem.find("title")
                if (
                    cid and start and stop and stop > start
                    and start <= upper_guide and stop >= lower_guide
                    and title is not None and is_english_text_element(title)
                ):
                    guide_programmes += 1
                    if stop >= now_guide:
                        guide_live.add(cid)
                elem.clear()
    except Exception as exc:
        guide_error = str(exc)[:300]

    active_ids = {r["tvg_id"] for r in rows if r["tvg_id"]}
    mapped_targets = {r["tvg_id"] for r in rows if r["tvg_id"] and r["epg_id"]}
    present_ids = mapped_targets & guide_channels
    live_ids = mapped_targets & guide_live
    active_present = active_ids & guide_channels
    active_live = active_ids & guide_live
    missing = sorted(mapped_targets - guide_channels)
    without_live = sorted(present_ids - guide_live)
    header_results = [(path, header_status(path)) for path in PLAYLISTS]
    lines += [
        "",
        "## Published Guide Validation",
        "",
        f"- XMLTV channel IDs published: **{len(guide_channels)}**",
        f"- Active playlist IDs present in the published guide: **{len(active_present)}/{len(active_ids)} ({round(100*len(active_present)/len(active_ids),1) if active_ids else 0}%)**",
        f"- Active playlist IDs with usable current/future programmes: **{len(active_live)}/{len(active_ids)} ({round(100*len(active_live)/len(active_ids),1) if active_ids else 0}%)**",
        f"- Mapped playlist IDs present in the guide: **{len(present_ids)}/{len(mapped_targets)} ({round(100*len(present_ids)/len(mapped_targets),1) if mapped_targets else 0}%)**",
        f"- Mapped playlist IDs with usable current/future programmes: **{len(live_ids)}/{len(mapped_targets)} ({round(100*len(live_ids)/len(mapped_targets),1) if mapped_targets else 0}%)**",
        f"- Eligible programme rows published in the guide window: **{guide_programmes}**",
        f"- Mapped playlist IDs missing from the published XMLTV channel list: **{len(missing)}**",
        "- Missing mapped playlist IDs: " + (", ".join(missing[:60]) if missing else "none") + (f" (and {len(missing)-60} more)" if len(missing) > 60 else ""),
        f"- Published mapped IDs without usable current/future programmes: **{len(without_live)}**",
        "- IDs without usable current/future programmes: " + (", ".join(without_live[:60]) if without_live else "none") + (f" (and {len(without_live)-60} more)" if len(without_live) > 60 else ""),
    ]
    if guide_error:
        lines.append(f"- XMLTV validation error: **{guide_error}**")
    lines += ["", "## Playlist EPG Headers", "", "| Playlist | Header status |", "|---|---|"]
    for path, status in header_results:
        lines.append(f"| {path.as_posix()} | {status} |")
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    mapping_by_id = {r["tvg_id"]: r for r in rows if r["tvg_id"]}
    report_lines = [
        "# EPG Audit — Published Playlists",
        "",
        f"Generated: **{datetime.now(timezone.utc).isoformat(timespec='seconds')}**",
        "",
        "This report measures the two M3U files currently published at the repository root. The historic filename epg-three-playlist-audit.md is retained for link compatibility; it does not mean a third playlist file exists.",
        "",
        "| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for path in PLAYLISTS:
        records = playlist_records(path)
        active_for_file = [x for x in records if x["tvg_id"] and x["group"] not in INACTIVE_GROUPS]
        active_for_file_ids = {x["tvg_id"] for x in active_for_file}
        mapped_for_file = {cid for cid in active_for_file_ids if mapping_by_id.get(cid, {}).get("epg_id")}
        current_for_file = {cid for cid in active_for_file_ids if mapping_by_id.get(cid, {}).get("status") == "MAPPED"}
        present_for_file = active_for_file_ids & guide_channels
        live_for_file = active_for_file_ids & guide_live
        no_map = len(active_for_file_ids - mapped_for_file)
        status = header_status(path)
        report_lines.append(
            f"| {path.name} | {len(records)} | {len(active_for_file_ids)} | {len(mapped_for_file)} | {len(current_for_file)} | {len(present_for_file)} | {len(live_for_file)} | {no_map} | {status} |"
        )

    report_lines += ["", "## Group coverage", "", "| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |", "|---|---:|---:|---:|---:|"]
    for group in sorted(group_summary):
        s = group_summary[group]
        report_lines.append(f"| {group} | {s['active']} | {s['mapped']} | {s['live']} | {s['unmapped']} |")
    report_lines += [
        "",
        "## Interpretation",
        "",
        "- Mapped IDs means a playlist identity was connected to a source XMLTV ID.",
        "- Current/future source schedules means source data contains eligible English-title programmes inside the generator's -6-hour/+7-day window.",
        "- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.",
        "- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.",
        "",
    ]
    if guide_error:
        report_lines += ["## Published XMLTV validation", "", "ERROR: " + guide_error, ""]
    THREE_PLAYLIST_REPORT.parent.mkdir(parents=True, exist_ok=True)
    THREE_PLAYLIST_REPORT.write_text("\n".join(report_lines), encoding="utf-8")

if __name__=="__main__": main()
