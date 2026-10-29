#!/usr/bin/env python3
"""Build and continuously improve EPG mappings from public XMLTV sources."""
import csv, gzip, hashlib, io, json, os, re, unicodedata, urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse
import xml.etree.ElementTree as ET
from official_epg_sources import (
    HUM_TV_SOURCE, HUM_TV_CHANNEL_ID, fetch_hum_tv_programmes,
    RTV_SOURCE, RTV_CHANNEL_ID, fetch_rtv_programmes,
)
from collections import defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path
from generate_epg import ALWAYS_DROP_GENERIC_TITLES, is_slot_placeholder, normalized_title, sources_with_mapped_channels


def is_filler_title(text):
    """Titles the generator never publishes ("No Data", "Movie", "Program @ 5:00 AM").

    Coverage must not count these as schedule data, or the report overstates
    what the published guide can actually show.
    """
    return normalized_title(text) in ALWAYS_DROP_GENERIC_TITLES or is_slot_placeholder(text)

PLAYLIST = Path("IPTV-Playlist.m3u")
MAPPING = Path("reports/epg-channel-mapping.csv")
EPG_PUBLIC_URL = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/epg/epg.xml"
EPG_PUBLISHED_PATH = Path("epg/epg.xml")

# Bound source-fetch latency while allowing healthy feeds to finish concurrently.
SOURCE_FETCH_TIMEOUT_SECONDS = 60
SOURCE_FETCH_WORKERS = 8

EPG_ALIASES = {
    "DDHimachalPradesh.in@SD": ["ts1217", "1217", "LIVETV_LIVETVCHANNEL_DD_SHIMLA"],
    "MTVIndia.in@SD": ["jtv248", "248"], "MusicMastii.in": ["jtv584", "584", "IN4#MASTII.in"],
    "KappaTV.in@ALT1": ["jtv786", "786", "377"], "IqraBangla.uk": ["3914"], "DeenTV.uk": ["1235"],
    "ATNBanglaUK.uk": ["6753"],
    "TamilanTV.in": ["jtv2958", "2958"],
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
    "Enterr10 Bangla.in": ["ENTER10.BANGLA.in", "Enterr10Bangla.in"], "ColorsInfinity.in": ["ColorsInfinity.in@HD", "ColorsInfinity.in@SD"],
    "Enter10Bangla.in": ["Enterr10Bangla.in@SD"], "tntsports1.uk": ["TNTSport1.uk", "TNTSports1.uk", "tntsports1.uk"],
    "tntsports2.uk": ["TNTSport2.uk", "TNTSports2.uk", "tntsports2.uk"], "tntsports3.uk": ["TNTSport3.uk", "TNTSports3.uk", "tntsports3.uk"],
    "tntsports4.uk": ["TNTSport4.uk", "TNTSports4.uk", "tntsports4.uk"], "skysportsmainevent.uk": ["SkySportsMainEvent.uk", "SkySpMainEvHD.uk", "SkySpMainEv.uk"],
    "skysportspremiereleague.uk": ["SkySportsPremierLeague.uk", "SkySp.PL.HD.uk", "SkySp.PL.uk"],

    # Verified identities found in existing source feeds during the strict unmapped audit.
    "TravelxpEnglish.us": ["Travelxp.uk"],
    "WildFlixHindi.in": ["IN460000585"],
    "WorldWarTV.us": ["WorldWarTV.uk"],
    "XXTremeJobsHindi.in": ["IN46000011Q"],
    "custom.sony.max.2": ["143801", "LIVETV_LIVETVCHANNEL_SONY_MAX_2", "jtv483"],
    "MovieSphere.us@AU": ["Moviesphere.au"],
    # Same AU service: exact name match after region suffix, with 64 current
    # programme rows in epg_ripper_AU1 (2026-10-26 strict unmapped audit).
    "custom.moviesphere-au": ["Moviesphere.au"],

    # Exact display-name matches (after stripping quality tags) in fresh India
    # provider feeds that are already in SOURCES (airtel/jiotv/yupptv). Checked
    # 2026-10-26 against the feed repo's current files: each ID had >=20
    # programme rows in the next 7 days and sample titles matched the channel.
    # All are Indian-service (.in) playlist IDs; none is a Bangladesh identity.
    "NationalGeographic.in@SD": ["LIVETV_LIVETVCHANNEL_NATIONAL_GEOGRAPHIC_CHANNEL"],
    "NationalGeographic.in@HD": ["LIVETV_LIVETVCHANNEL_NATIONAL_GEOGRAPHIC_CHANNEL_HD"],
    "ColorsSuper.in@SD": ["LIVETV_LIVETVCHANNEL_COLORS_SUPER"],
    "DarshanaTV.in@SD": ["3354"],
    "ETVComedy.in@HD": ["jtv3561"],
    "EpicBharat.in@Digital": ["jtv3383"],
    "SuperHungama.in@SD": ["LIVETV_LIVETVCHANNEL_SUPER_HUNGAMA"],
    "ZeeCineClassic.in@SD": ["ZEEFAST_LIVECHANNEL_5"],
    "ZeeComedyNation.in@HD": ["ZEEFAST_LIVECHANNEL_4"],
    "ZeeSouthFlix.in@HD": ["ZEEFAST_LIVECHANNEL_3"],
    "JalshaMovies.in@HD": ["LIVETV_LIVETVCHANNEL_JALSHA_MOVIES_HD"],
    "NHBollyFlix.in@HD": ["jtv3336"],
    "PunjabiShorts.in@SD": ["jtv3471"],
    "SonyPix.in@HD": ["LIVETV_LIVETVCHANNEL_SONY_PIX_HD"],
    "StarMovies.in@HD": ["LIVETV_LIVETVCHANNEL_STAR_MOVIES_HD"],
    "ThalaaTV.in@HD": ["6601"],
    "TollyTV.in@HD": ["6613"],
    "DisneyChannel.in@HD": ["LIVETV_LIVETVCHANNEL_DISNEY_CHANNEL_HD"],
    # SunDirect GO / airtel exact-name matches (2026-10-26). Epic Music titles
    # agree across both feeds (Astro Tunes, Sunrise 90's); airtel has more rows.
    "KeralaVision.in@SD": ["149044"],
    "EpicMusic.in@Digital": ["LIVETV_LIVETVCHANNEL_SHOWBOX"],
    "custom.bdix.cnninternationla": ["157679"],
    "ToonamiAftermathEast.us": ["ToonamiAftermath.us"],
    "DocumentaryPlus": ["plex.tv.Documentary+.plex"],
    # Reuses the prior mapped EPG identity for the same channel after ID normalization.
    # Verified against fresh dishtv/jiotv feeds (exact display name, current English rows).
    "Hungama.in@SD": ["143150"],
    "ZBMusic.in@HD": ["jtv3319"],
    # Verified against current JioTV/Dish TV source IDs for the same channels.
    "AmarBanglaDigital.in": ["jtv1962"],
    "EpicBhojpuriDigital.in": ["157803", "jtv3384"],
    "Picture.in": ["And.Pictures.HD.in", "142638", "jtv185"],
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
SOURCE_AUDIT_REPORT = Path("reports/epg-source-audit.md")
SOURCES = [
    "https://epgshare01.online/epgshare01/epg_ripper_IN1.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_IN2.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz",
    "https://iptv-epg.org/files/epg-in.xml.gz",
    # Additional regional sources also used by the mapping-discovery pass.
    "https://epg.lat/files/in.xml.gz",
    "https://epg.lat/files/us.xml.gz",
    "https://www.free-epg.de/api/epg/in.xml.gz",
    "https://www.free-epg.de/api/epg/us.xml.gz",
    "https://www.open-epg.com/files/india.xml.gz",
    # Supplemental country guides for international playlist regions improve schedule coverage.
    "https://iptv-epg.org/files/epg-ar.xml.gz",
    "https://iptv-epg.org/files/epg-bg.xml.gz",
    "https://iptv-epg.org/files/epg-br.xml.gz",
    "https://iptv-epg.org/files/epg-ca.xml.gz",
    "https://iptv-epg.org/files/epg-cl.xml.gz",
    "https://iptv-epg.org/files/epg-co.xml.gz",
    "https://iptv-epg.org/files/epg-cz.xml.gz",
    "https://iptv-epg.org/files/epg-de.xml.gz",
    "https://iptv-epg.org/files/epg-es.xml.gz",
    "https://iptv-epg.org/files/epg-fr.xml.gz",
    "https://iptv-epg.org/files/epg-gr.xml.gz",
    "https://iptv-epg.org/files/epg-hk.xml.gz",
    "https://iptv-epg.org/files/epg-hu.xml.gz",
    "https://iptv-epg.org/files/epg-it.xml.gz",
    "https://iptv-epg.org/files/epg-mx.xml.gz",
    "https://iptv-epg.org/files/epg-nl.xml.gz",
    "https://iptv-epg.org/files/epg-pe.xml.gz",
    "https://iptv-epg.org/files/epg-pl.xml.gz",
    "https://iptv-epg.org/files/epg-pt.xml.gz",
    "https://iptv-epg.org/files/epg-ro.xml.gz",
    "https://iptv-epg.org/files/epg-ru.xml.gz",
    "https://iptv-epg.org/files/epg-rs.xml.gz",
    "https://iptv-epg.org/files/epg-se.xml.gz",
    "https://iptv-epg.org/files/epg-tr.xml.gz",
    "https://iptv-epg.org/files/epg-gb.xml.gz",
    # Samsung TV Plus schedules for India and the US; useful for matching FAST channels.
    "https://i.mjh.nz/SamsungTVPlus/in.xml",
    "https://i.mjh.nz/SamsungTVPlus/us.xml",
    "https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml",
    "https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz",
    "https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml",
    "https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml",
    "https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/yupptv.xml",
    "https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/zee5.xml",
    "https://avkb.short.gy/epg.xml.gz",
    "https://avkb.short.gy/jioepg.xml.gz",
    "https://avkb.short.gy/tsepg.xml.gz",
    # Targeted FAST-channel guides avoid the oversized all-sources mega-feed.
    "https://epgshare01.online/epgshare01/epg_ripper_DISTROTV1.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_RAKUTEN1.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz",
    "https://www.open-epg.com/files/unitedkingdom.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz",
    "https://iptv-epg.org/files/epg-us.xml.gz",
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
    "https://www.rtvbd.tv/schedule.php",
]


PRIVATE_SOURCE_ENV = "M3U4U_XMLTV_URL"
PRIVATE_SOURCE_LABEL = "M3U4U XMLTV (private Actions secret)"


def configured_sources():
    """Add the personalized M3U4U feed only from a GitHub Actions secret."""
    sources = list(SOURCES)
    private_url = os.environ.get(PRIVATE_SOURCE_ENV, "").strip()
    if not private_url:
        return sources
    parsed = urlparse(private_url)
    if (
        parsed.scheme.lower() != "https"
        or (parsed.hostname or "").lower() not in {"m3u4u.com", "www.m3u4u.com"}
        or not parsed.path.startswith(("/epg/", "/xml/"))
    ):
        print(
            f"Ignoring {PRIVATE_SOURCE_ENV}: use an HTTPS M3U4U XMLTV endpoint; "
            "the configured URL is not printed."
        )
        return sources
    if private_url not in sources:
        sources.append(private_url)
    return sources


def source_label(src):
    if src == os.environ.get(PRIVATE_SOURCE_ENV, "").strip():
        return PRIVATE_SOURCE_LABEL
    return src


def source_error(src, exc):
    if source_label(src) == PRIVATE_SOURCE_LABEL:
        return "details suppressed for private source"
    return str(exc)[:220]


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

PLAYLISTS = [Path("IPTV-Playlist.m3u"), Path("BDIX-Playlist.m3u"), Path("International-Playlist.m3u")]
INACTIVE_GROUPS = {"Backup", "Test", "Not Playing"}

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

# All valid non-empty programme languages remain eligible. If multiple titles
# represent the same programme, prefer English, then Bengali, then other languages.
LANG_PRIORITY = {"en": 3, "eng": 3, "bn": 2, "ben": 2}
LANG_PREFIXES = (("en-", 3), ("en_", 3), ("bn-", 2), ("bn_", 2))


def _script_rank(text):
    scripts = set()
    for char in text:
        if unicodedata.category(char).startswith("L"):
            name = unicodedata.name(char, "")
            if "LATIN" in name:
                scripts.add("latin")
            elif "BENGALI" in name:
                scripts.add("bengali")
            elif name:
                scripts.add("other")
    if scripts == {"latin"} or scripts == {"latin", "bengali"}:
        return 3
    if scripts == {"bengali"}:
        return 2
    return 1 if scripts else 0


def language_priority(elem):
    text = (elem.text or "").strip()
    lang = (elem.attrib.get("{http://www.w3.org/XML/1998/namespace}lang") or elem.attrib.get("lang") or "").strip().lower()
    if lang:
        if lang in LANG_PRIORITY:
            return LANG_PRIORITY[lang]
        for prefix, rank in LANG_PREFIXES:
            if lang.startswith(prefix):
                return rank
        return 1
    return _script_rank(text)


def is_english_text_element(elem):
    """Compatibility name: accept non-empty titles in any valid script/language."""
    text = (elem.text or "").strip()
    if not text:
        return True
    return any(unicodedata.category(char).startswith("L") for char in text)


def fetch_source(url):
    if url == RTV_SOURCE:
        programmes = fetch_rtv_programmes()
        ids = {RTV_CHANNEL_ID} if programmes else set()
        future = set()
        counts = defaultdict(int)
        names = defaultdict(set)
        now = datetime.now(timezone.utc)
        for program in programmes:
            cid = program["channel_id"]
            counts[cid] += 1
            names[norm_name("RTV")].add(cid)
            if program["stop_dt"] >= now:
                future.add(cid)
        return ids, future, counts, names

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
    with urllib.request.urlopen(req, timeout=SOURCE_FETCH_TIMEOUT_SECONDS) as r:
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
                and title is not None and bool((title.text or "").strip())
                and not is_filler_title(title.text)
                and is_english_text_element(title)
            ):
                counts[cid] += 1
                if stop >= now:
                    future.add(cid)
            elem.clear()
    return ids, future, counts, names


def fetch_all_sources(source_urls, max_workers=SOURCE_FETCH_WORKERS):
    """Fetch source feeds concurrently and return results in configured order."""
    urls = list(source_urls)
    if not urls:
        return [], []

    results = {}
    workers = max(1, min(int(max_workers), len(urls)))
    with ThreadPoolExecutor(max_workers=workers, thread_name_prefix="epg-source") as pool:
        futures = {pool.submit(fetch_source, src): src for src in urls}
        for future in as_completed(futures):
            src = futures[future]
            try:
                data = future.result()
                ids, future_ids, counts, names = data
                status = (
                    source_label(src), "OK", len(ids), len(future_ids),
                    sum(counts.values()), "",
                )
            except Exception as exc:
                data = (set(), set(), defaultdict(int), defaultdict(set))
                status = (source_label(src), "FAILED", 0, 0, 0, source_error(src, exc))
            results[src] = (data, status)

    return (
        [results[src][0] for src in urls],
        [results[src][1] for src in urls],
    )

def load_previous():
    out={}
    if not MAPPING.exists(): return out
    with MAPPING.open(encoding="utf-8-sig",newline="") as fh:
        for r in csv.DictReader(fh):
            if r.get("tvg_id"): out[r["tvg_id"]]=r
    return out

def retained_mapping(is_bangladesh, old_epg, candidates):
    """Retain safe mappings but discard legacy EPG.PW IDs and stale foreign Bangladesh mappings."""
    # EPG.PW terms prohibit copying/retransmission; prevent legacy IDs from
    # reactivating its schedules in the public guide without explicit permission.
    prior_ids = [
        value.strip()
        for value in (old_epg or "").split("|")
        if value.strip() and not value.strip().casefold().startswith("epgpw:")
    ]
    old_epg = " | ".join(prior_ids)
    if not old_epg:
        return ""
    if is_bangladesh:
        prior = set(prior_ids)
        if not prior <= set(candidates):
            return ""
    return old_epg


def main():
    channels=parse_playlist(); previous=load_previous(); source_data=[]; source_status=[]
    # Use the existing mapping snapshot to avoid parsing feeds that cannot
    # currently contribute a matched source ID. New channel/source discovery is
    # still handled by the targeted supplemental and iptv-org augmentation steps.
    source_urls = sources_with_mapped_channels(configured_sources())
    source_data, source_status = fetch_all_sources(source_urls)
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
        for src,data in zip(source_urls,source_data):
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
                hit_sources.append(source_label(src))
                for cid in src_hits:
                    if cid not in hits: hits.append(cid)
                    total += counts.get(cid,0)
                    if cid in future: best_live.append(cid); live=True
        old_epg=retained_mapping(is_bangladesh, prev.get("epg_id",""), candidates)
        if ch["group"]=="Indian Bangla": epg_id=(best_live[0] if best_live else (hits[0] if hits else old_epg))
        else: epg_id=(best_live[0] if best_live else (hits[0] if hits else old_epg))
        if live: status="MAPPED"
        elif hits: status="MAPPED_ID_ONLY" if total==0 else "MAPPED_ENDED"
        elif old_epg: status="MAPPED_NOT_CURRENTLY_FOUND"
        else: status="NO_GUIDE_HIT"
        rows.append({"group":ch["group"],"channel":ch["name"],"tvg_id":ch["tvg_id"],"epg_id":epg_id,"source":" | ".join(hit_sources),"status":status,"note":"Auto-maintained; verify ambiguous/name matches manually."})

    # Strict candidates are exact channel-name matches after removing known
    # territory/language suffixes. They are review-only and never auto-applied.
    # Bangladesh-group channels are excluded from fuzzy name matching entirely.
    def without_region_suffix(value):
        value = norm_name(value)
        suffixes = (
            "czechrepublic", "unitedkingdom", "international", "malayalam",
            "telugu", "bengali", "hindi", "tamil", "canada", "australia",
            "ukraine", "poland", "france", "germany", "mexico", "arabia",
            "india", "europe", "english", "favoris", "east", "west",
            "mena", "usa", "uae", "uk", "us", "au", "br", "ca", "fr", "de", "in",
        )
        for suffix in suffixes:
            if value.endswith(suffix) and len(value) - len(suffix) >= 5:
                return value[:-len(suffix)]
        return value

    audit_rows = []
    unmapped_rows = [row for row in rows if not row["epg_id"]]
    channels_with_candidates = set()
    for row in unmapped_rows:
        if row["group"].strip() == "Bangladesh":
            continue
        target_name = norm_name(row["channel"])
        target_regionless = without_region_suffix(row["channel"])
        candidates_by_id = {}
        for src, source_tuple in zip(source_urls, source_data):
            source_ids, source_future, source_counts, source_names = source_tuple
            for source_name_key, source_ids_for_name in source_names.items():
                if not source_name_key or len(source_name_key) < 5:
                    continue
                source_regionless = without_region_suffix(source_name_key)
                # Strict equality only: no fuzzy or substring-based candidates.
                is_exact = target_name == source_name_key
                is_region_variant = bool(target_regionless and target_regionless == source_regionless)
                if not (is_exact or is_region_variant):
                    continue
                for source_id in source_ids_for_name:
                    if source_id not in source_future:
                        continue
                    item = candidates_by_id.setdefault(source_id, {
                        "source_id": source_id,
                        "source_name": source_name_key,
                        "programme_rows": source_counts.get(source_id, 0),
                        "sources": [],
                        "match_type": "EXACT_NAME" if is_exact else "EXACT_AFTER_REGION_SUFFIX",
                    })
                    item["programme_rows"] = max(item["programme_rows"], source_counts.get(source_id, 0))
                    if source_label(src) not in item["sources"]:
                        item["sources"].append(source_label(src))
                    if is_exact:
                        item["match_type"] = "EXACT_NAME"
        ranked = sorted(
            candidates_by_id.values(),
            key=lambda item: (item["match_type"] != "EXACT_NAME", -item["programme_rows"], item["source_id"]),
        )[:5]
        if ranked:
            channels_with_candidates.add(row["tvg_id"])
        for item in ranked:
            audit_rows.append({
                "group": row["group"],
                "channel": row["channel"],
                "tvg_id": row["tvg_id"],
                "candidate_name": item["source_name"],
                "candidate_epg_id": item["source_id"],
                "similarity": 1.0,
                "usable_programmes": item["programme_rows"],
                "source_urls": item["sources"],
                "review_status": "MANUAL_REVIEW_ONLY",
                "match_type": item["match_type"],
            })

    audit_path = Path("reports/epg-unmapped-audit.md")
    audit_path.parent.mkdir(parents=True, exist_ok=True)
    audit_lines = [
        "# Strict Unmapped EPG Audit",
        "",
        f"Generated: **{datetime.now(timezone.utc).isoformat(timespec='seconds')}**",
        "",
        "Only exact normalized display-name matches or exact matches after removing a recognized territory/language suffix are listed below. Every candidate has current/future schedule rows in a configured feed, but candidates remain review-only and are never automatically applied.",
        "Bangladesh-group channels are not name-matched here. Their domestic schedules require exact ID/explicit alias evidence; a similar Indian or foreign channel is not acceptable.",
        "",
        f"- Unmapped active channel identities reviewed: **{len(unmapped_rows)}**",
        f"- Unmapped identities with exact/region-normalized schedule candidates: **{len(channels_with_candidates)}**",
        f"- Candidate rows: **{len(audit_rows)}**",
        f"- Unmapped identities without an exact schedule-backed candidate: **{len(set(row['tvg_id'] for row in unmapped_rows) - channels_with_candidates)}**",
        "",
        "## Exact candidates for manual review",
        "",
        "| Group | Playlist channel | Playlist tvg-id | Candidate source name | Candidate EPG ID | Match type | Usable programme rows | Source feed(s) | Decision |",
        "|---|---|---|---|---|---|---:|---|---|",
    ]
    for item in sorted(audit_rows, key=lambda x: (x["group"], x["channel"].lower(), x["match_type"], x["candidate_epg_id"])):
        urls = "<br>".join(item["source_urls"])
        audit_lines.append(
            f"| {item['group']} | {item['channel']} | {item['tvg_id']} | {item['candidate_name']} | {item['candidate_epg_id']} | {item['match_type']} | {item['usable_programmes']} | {urls} | MANUAL_REVIEW_ONLY |"
        )
    audit_lines += [
        "",
        "## Bangladesh-specific review",
        "",
        f"- Bangladesh-group IDs without a mapping: **{sum(1 for row in unmapped_rows if row['group'].strip() == 'Bangladesh')}**",
        "The nasimali/epg-auto diaspora guide uses numeric Sky channel IDs with generic display names such as Channel 3914; channel identity is never inferred from list ordering. Explicit sources are used for Iqra Bangla, ATN Bangla UK, NTV Europe, Channel S UK, and Deen TV. These mappings do not imply a general domestic Bangladesh EPG source.",
        "No dependable public, current XMLTV feed for the domestic Bangladesh channel set was verified. NTV Europe and Channel S UK use dedicated UK diaspora channel feeds; the remaining domestic channels stay unmapped until a trustworthy exact-ID schedule source is verified. No schedule is fabricated from stale static schedules or unrelated foreign channels.",
        "",
    ]
    audit_fingerprints = [
        f"- {path.name} SHA-256: **{hashlib.sha256(path.read_bytes()).hexdigest()}**"
        for path in PLAYLISTS if path.exists()
    ]
    audit_lines += ["", "## Source Playlist Fingerprints", "", *audit_fingerprints, ""]
    audit_path.write_text("\n".join(audit_lines) + "\n", encoding="utf-8")

    MAPPING.parent.mkdir(parents=True,exist_ok=True)
    with MAPPING.open("w",encoding="utf-8",newline="") as fh:
        w=csv.DictWriter(fh,fieldnames=["group","channel","tvg_id","epg_id","source","status","note"]); w.writeheader(); w.writerows(sorted((r for r in rows if r["group"].strip() != "Adult"),key=lambda r:(r["group"],r["channel"])))

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
        "This report audits active unique channel identities across the three maintained playlists configured in the automated EPG pipeline. A source mapping is not counted as usable current/future coverage unless it has a valid programme interval and valid non-empty multilingual title data within the generator's -6-hour/+7-day window; English titles rank first, then Bengali, then other valid languages.",
        f"The XMLTV guide is published at **{EPG_PUBLISHED_PATH.as_posix()}**. The published guide uses the playlist's tvg-id as the XMLTV channel ID, not the upstream provider's source ID.",
        "",
        "## Overall Coverage",
        "",
        f"- Active unique playlist channel IDs audited: **{total_active}**",
        f"- IDs with an EPG source mapping: **{total_mapped}/{total_active} ({round(100*total_mapped/total_active,1) if total_active else 0}%)**",
        f"- IDs with usable current/future source schedules (nonblank multilingual titles (English preferred, then Bengali, then other valid languages)): **{total_live}/{total_active} ({round(100*total_live/total_active,1) if total_active else 0}%)**",
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
            f"- **{status}** — {src} — {ids} channel IDs; {future} IDs with usable current/future programmes; {programmes} eligible programme rows with valid non-empty titles in any language in the guide window"
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
    guide_window = set()
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
                    and title is not None and bool((title.text or "").strip())
                    and not is_filler_title(title.text)
                    and is_english_text_element(title)
                ):
                    guide_programmes += 1
                    guide_window.add(cid)
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
    active_window = active_ids & guide_window
    missing = sorted(mapped_targets - guide_channels)
    without_live = sorted(present_ids - guide_live)
    source_live_ids = {r["tvg_id"] for r in rows if r["tvg_id"] and r["status"] == "MAPPED"}
    source_live_without_publication = sorted(source_live_ids - active_window)
    published_window_without_source = sorted(active_window - source_live_ids)
    source_live_without_current = sorted(source_live_ids - active_live)
    published_live_without_source = sorted(active_live - source_live_ids)
    channel_names = {r["tvg_id"]: r["channel"] for r in rows if r["tvg_id"]}
    header_results = [(path, header_status(path)) for path in PLAYLISTS]
    lines += [
        "",
        "## Published Guide Validation",
        "",
        f"- XMLTV channel IDs published: **{len(guide_channels)}**",
        f"- Active playlist IDs present in the published guide: **{len(active_present)}/{len(active_ids)} ({round(100*len(active_present)/len(active_ids),1) if active_ids else 0}%)**",
        f"- Active playlist IDs with usable current/future programmes: **{len(active_live)}/{len(active_ids)} ({round(100*len(active_live)/len(active_ids),1) if active_ids else 0}%)**",
        f"- Active playlist IDs with usable programmes anywhere in the guide window (-6h/+7d): **{len(active_window)}/{len(active_ids)} ({round(100*len(active_window)/len(active_ids),1) if active_ids else 0}%)**",
        f"- Mapped playlist IDs present in the guide: **{len(present_ids)}/{len(mapped_targets)} ({round(100*len(present_ids)/len(mapped_targets),1) if mapped_targets else 0}%)**",
        f"- Mapped playlist IDs with usable current/future programmes: **{len(live_ids)}/{len(mapped_targets)} ({round(100*len(live_ids)/len(mapped_targets),1) if mapped_targets else 0}%)**",
        f"- Mapped playlist IDs with usable programmes anywhere in the guide window: **{len(mapped_targets & guide_window)}/{len(mapped_targets)} ({round(100*len(mapped_targets & guide_window)/len(mapped_targets),1) if mapped_targets else 0}%)**",
        f"- Eligible programme rows published in the guide window: **{guide_programmes}**",
        f"- Mapped playlist IDs missing from the published XMLTV channel list: **{len(missing)}**",
        "- Missing mapped playlist IDs: " + (", ".join(missing[:60]) if missing else "none") + (f" (and {len(missing)-60} more)" if len(missing) > 60 else ""),
        f"- Published mapped IDs without usable current/future programmes: **{len(without_live)}**",
        "- IDs without usable current/future programmes: " + (", ".join(without_live[:60]) if without_live else "none") + (f" (and {len(without_live)-60} more)" if len(without_live) > 60 else ""),
    ]
    def format_identity_list(ids):
        return ", ".join(
            f"{channel_names.get(cid, 'Unknown channel')} (`{cid}`)" for cid in ids
        ) if ids else "none"
    lines += [
        "",
        "## Source / Published Schedule Reconciliation",
        "",
        f"- IDs with usable current/future source schedule data: **{total_live}/{total_active} ({round(100*total_live/total_active,1) if total_active else 0}%)**",
        f"- IDs with usable current/future schedules in published XMLTV at report time: **{len(active_live)}/{len(active_ids)} ({round(100*len(active_live)/len(active_ids),1) if active_ids else 0}%)**",
        f"- IDs with usable programmes in the published guide's common -6h/+7d window: **{len(active_window)}/{len(active_ids)} ({round(100*len(active_window)/len(active_ids),1) if active_ids else 0}%)**",
        f"- Current/future source IDs without any usable published programme in that common window: **{len(source_live_without_publication)}**",
        "- Source-scheduled IDs without a usable published programme in the common window: " + format_identity_list(source_live_without_publication),
        f"- IDs with an in-window published programme but no current/future source match at the later scan: **{len(published_window_without_source)}**",
        "- In-window published IDs not counted source-current/future: " + format_identity_list(published_window_without_source),
        f"- Source-current/future IDs whose published programme is no longer current by report time: **{len(source_live_without_current)}**",
        "- Source-current/future IDs no longer current in the published guide: " + format_identity_list(source_live_without_current),
        f"- Published current/future IDs not counted source-current/future: **{len(published_live_without_source)}**",
        "- Published current/future IDs not counted source-current/future: " + format_identity_list(published_live_without_source),
        "",
    ]
    if guide_error:
        lines.append(f"- XMLTV validation error: **{guide_error}**")
    lines += ["", "## Playlist EPG Headers", "", "| Playlist | Header status |", "|---|---|"]
    for path, status in header_results:
        lines.append(f"| {path.as_posix()} | {status} |")
    source_fingerprints = [
        f"- {path.name} SHA-256: **{hashlib.sha256(path.read_bytes()).hexdigest()}**"
        for path in PLAYLISTS if path.exists()
    ]
    lines += ["", "## Source Playlist Fingerprints", "", *source_fingerprints, ""]
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    source_audit_lines = [
        "# EPG Source Health Audit",
        "",
        f"Generated: **{datetime.now(timezone.utc).isoformat(timespec='seconds')}**",
        "",
        "This is a runtime availability and schedule-coverage report, not a permission gate. The source-review register is advisory and does not block discovery, mapping, generation, or publication.",
        "",
        "| Status | Source | Channel IDs | Current/future IDs | Eligible programme rows | Error / note |",
        "|---|---|---:|---:|---:|---|",
    ]
    for src, status, ids, future, programmes, error in source_status:
        safe_src = str(src).replace("|", "\\|")
        safe_error = (str(error).replace("|", "\\|").replace("\\n", " ") if error else "-")
        source_audit_lines.append(
            f"| {status} | {safe_src} | {ids} | {future} | {programmes} | {safe_error} |"
        )
    source_audit_lines += [
        "",
        "## Source handling notes",
        "",
        "- M3U4U is optional and is read only from the GitHub Actions secret named M3U4U_XMLTV_URL. Reports use a generic source label; the personalized URL and fetch errors are never logged.",
        "- EPG.PW is not ingested into the public guide because its published terms prohibit copying/retransmission and limit use to personal use. This is a source-specific constraint, not a blanket exclusion of third-party sources.",
        "- Bangladesh schedule mappings remain exact-ID/explicit-alias only. An official schedule source that fails TLS or parsing is recorded as failed and contributes no programme coverage.",
        "",
    ]
    SOURCE_AUDIT_REPORT.parent.mkdir(parents=True, exist_ok=True)
    SOURCE_AUDIT_REPORT.write_text("\\n".join(source_audit_lines) + "\\n", encoding="utf-8")

    mapping_by_id = {r["tvg_id"]: r for r in rows if r["tvg_id"]}
    report_lines = [
        "# EPG Audit — Published Playlists",
        "",
        f"Generated: **{datetime.now(timezone.utc).isoformat(timespec='seconds')}**",
        "",
        "This report measures the three maintained M3U playlists included in the automated EPG pipeline. The historic filename epg-three-playlist-audit.md is retained for link compatibility.",
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
        "- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.",
        "- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.",
        "- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.",
        "",
    ]
    if guide_error:
        report_lines += ["## Published XMLTV validation", "", "ERROR: " + guide_error, ""]
    THREE_PLAYLIST_REPORT.parent.mkdir(parents=True, exist_ok=True)
    report_lines += ["", "## Source Playlist Fingerprints", "", *source_fingerprints, ""]
    THREE_PLAYLIST_REPORT.write_text("\n".join(report_lines), encoding="utf-8")

if __name__=="__main__": main()
