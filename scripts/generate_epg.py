#!/usr/bin/env python3
"""Generate a playlist-aligned, conflict-free XMLTV guide from approved public EPG sources."""
import bisect
from concurrent.futures import ThreadPoolExecutor, as_completed
import csv
import gzip
import io
import os
import re
import urllib.request
from urllib.parse import parse_qs, urlparse
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta
from difflib import SequenceMatcher
from pathlib import Path
from official_epg_sources import (
    HUM_TV_SOURCE, HUM_TV_CHANNEL_ID, fetch_hum_tv_programmes,
    RTV_SOURCE, RTV_CHANNEL_ID, fetch_rtv_programmes,
    BTV_SOURCE, BTV_CHANNEL_ID, fetch_btv_programmes,
    MAASRANGA_SOURCE, MAASRANGA_CHANNEL_ID, fetch_maasranga_programmes,
)

PLAYLISTS = [
    Path("IPTV-Playlist.m3u"),
    Path("International-Playlist.m3u"),
]
INACTIVE_GROUPS = {"Backup", "Test", "Not Playing"}
MAPPING = Path("reports/epg-channel-mapping.csv")
OUTPUT = Path("epg/epg.xml")

# Bound the worst-case wait for a batch of remote XMLTV feeds.
SOURCE_FETCH_TIMEOUT_SECONDS = 90
SOURCE_FETCH_WORKERS = 16

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
    # Additional country feeds from iptv-epg.org for active International groups.
    "https://iptv-epg.org/files/epg-at.xml.gz",
    "https://iptv-epg.org/files/epg-au.xml.gz",
    "https://iptv-epg.org/files/epg-cr.xml.gz",
    "https://iptv-epg.org/files/epg-pa.xml.gz",
    "https://iptv-epg.org/files/epg-py.xml.gz",
    "https://iptv-epg.org/files/epg-sg.xml.gz",
    # Targeted FreeEPG country guides for regions represented in International-Playlist.m3u.
    "https://free-epg.de/api/epg/at.xml.gz",
    "https://free-epg.de/api/epg/cn.xml.gz",
    "https://free-epg.de/api/epg/cr.xml.gz",
    "https://free-epg.de/api/epg/ec.xml.gz",
    "https://free-epg.de/api/epg/ee.xml.gz",
    "https://free-epg.de/api/epg/pa.xml.gz",
    "https://free-epg.de/api/epg/sa.xml.gz",
    "https://free-epg.de/api/epg/ua.xml.gz",
    # Samsung TV Plus schedules for India and the US; useful for matching FAST channels.
    "https://i.mjh.nz/SamsungTVPlus/in.xml",
    "https://i.mjh.nz/SamsungTVPlus/us.xml",
    "https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml",
    "https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz",
    "https://m3u-edit.com/epg-source.php?file=IN1.xml.gz",
    "https://m3u-edit.com/epg-source.php?file=IN4.xml.gz",
    "https://m3u-edit.com/epg-source.php?file=india_dishtv.in.xml",
    "https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml",
    "https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml",
    "https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/yupptv.xml",
    "https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/zee5.xml",
    "https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/slingtv.xml",
    "https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/sundirectgo.xml",
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
    "https://migrate.btvlive.gov.bd/channel/BTV",
    "https://maasranga.tv/full-width/program-time-schedule/",
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
        print(f"Ignoring {PRIVATE_SOURCE_ENV}: use an HTTPS M3U4U XMLTV endpoint; the configured URL is not printed.")
        return sources
    if private_url not in sources:
        sources.append(private_url)
    return sources


COUNTRY_GROUP_CODES = {
    "argentina": "AR", "aruba": "AW", "austria": "AT", "brazil": "BR",
    "bulgaria": "BG", "canada": "CA", "chile": "CL", "china": "CN",
    "colombia": "CO", "costa rica": "CR", "czech republic": "CZ",
    "dominican republic": "DO", "ecuador": "EC", "estonia": "EE",
    "france": "FR", "germany": "DE", "greece": "GR", "hungary": "HU",
    "iran": "IR", "italy": "IT", "lebanon": "LB", "mexico": "MX",
    "netherlands": "NL", "panama": "PA", "paraguay": "PY", "peru": "PE",
    "poland": "PL", "portugal": "PT", "romania": "RO", "russia": "RU",
    "saudi arabia": "SA", "serbia": "RS", "singapore": "SG", "spain": "ES",
    "turkey": "TR", "ukraine": "UA", "united kingdom": "GB",
    "united states": "US", "uzbekistan": "UZ", "vietnam": "VN",
    "indian bangla": "IN", "indian movies": "IN", "indian music": "IN",
    "indian entertainment": "IN", "pakistani": "PK",
}
COUNTRY_CODE_ALIASES = {"UK": "GB"}
# Recognized XMLTV country suffixes. Restrict suffix inference to real/used
# country codes so display variants such as ".HD" are never treated as regions.
PLAYLIST_ID_COUNTRY_CODES = {
    "ae", "ar", "at", "au", "bd", "be", "bg", "br", "by", "ca", "ch", "cl",
    "cn", "co", "cr", "cz", "de", "dk", "do", "ee", "es", "fi", "fr",
    "gb", "gr", "hu", "id", "ie", "il", "in", "iq", "ir", "is", "it",
    "jp", "kr", "kw", "lb", "lk", "lt", "lu", "lv", "ma", "mx", "my",
    "ng", "nl", "no", "np", "nz", "om", "pa", "pe", "ph", "pk", "pl",
    "pt", "qa", "ro", "rs", "ru", "sa", "se", "sg", "sk", "th", "tr", "tw",
    "ua", "uk", "us", "uy", "uz", "vn", "za",
}


def normalize_country_code(value):
    code = str(value or "").strip().upper()
    if len(code) != 2 or not code.isalpha():
        return ""
    return COUNTRY_CODE_ALIASES.get(code, code)


PLAYLIST_ID_QUALIFIER_COUNTRY_ALIASES = {
    "czechia": "CZ", "bulgary": "BG", "belarus": "BY", "slovakia": "SK",
    "nepal": "NP", "taiwan": "TW", "sweden": "SE", "denmark": "DK",
    "norway": "NO", "india": "IN", "australia": "AU", "usa": "US",
    "southafrica": "ZA", "newzealand": "NZ", "japan": "JP",
    "southkorea": "KR", "hongkong": "HK", "malaysia": "MY",
    "indonesia": "ID", "philippines": "PH", "ireland": "IE",
    "finland": "FI", "iceland": "IS", "switzerland": "CH",
    "belgium": "BE", "uae": "AE", "unitedarabemirates": "AE",
    "thailand": "TH", "vietnam": "VN", "bangladesh": "BD",
}


def playlist_id_qualifier_country_code(value):
    """Resolve a country/territory qualifier such as @UK or @Poland, not quality tags."""
    token = re.sub(r"[^a-z0-9]+", "", str(value or "").casefold())
    if not token:
        return ""
    if len(token) == 2 and token in PLAYLIST_ID_COUNTRY_CODES:
        return normalize_country_code(token)
    if token in PLAYLIST_ID_QUALIFIER_COUNTRY_ALIASES:
        return normalize_country_code(PLAYLIST_ID_QUALIFIER_COUNTRY_ALIASES[token])
    for name, code in COUNTRY_GROUP_CODES.items():
        if token == re.sub(r"[^a-z0-9]+", "", name.casefold()):
            return normalize_country_code(code)
    return ""


def playlist_id_country_code(tvg_id):
    """Infer the broadcast territory from @qualifiers before falling back to the base ID suffix."""
    value = re.sub(r"\s*\([^)]*\)\s*$", "", str(tvg_id or "").strip())
    if "@" in value:
        qualifier_code = playlist_id_qualifier_country_code(value.rsplit("@", 1)[1])
        if qualifier_code:
            return qualifier_code
    match = re.search(r"\.([a-z]{2})(?:@[^@]*)?$", value, flags=re.I)
    if not match or match.group(1).lower() not in PLAYLIST_ID_COUNTRY_CODES:
        return ""
    return normalize_country_code(match.group(1))


def playlist_entry_country_code(tvg_id, tvg_country="", group=""):
    """Resolve explicit country, territory qualifier, country group, then base tvg-id suffix."""
    explicit = normalize_country_code(tvg_country)
    if explicit:
        return explicit
    value = str(tvg_id or "").strip()
    if "@" in value:
        qualifier = playlist_id_qualifier_country_code(value.rsplit("@", 1)[1])
        if qualifier:
            return qualifier
    group_code = COUNTRY_GROUP_CODES.get(str(group or "").strip().casefold(), "")
    if group_code:
        return normalize_country_code(group_code)
    return playlist_id_country_code(value)


def active_playlist_country_codes():
    """Return country codes represented by active entries in the two maintained playlists."""
    countries = set()
    for playlist_path in PLAYLISTS:
        if not playlist_path.is_file():
            continue
        current = None
        for line in playlist_path.read_text(encoding="utf-8-sig").splitlines():
            if line.startswith("#EXTINF:"):
                current = dict(re.findall(r'([\w-]+)="([^"]*)"', line))
            elif current and line.strip().startswith(("http://", "https://")):
                group = current.get("group-title", "").strip()
                tvg_id = current.get("tvg-id", "").strip()
                if tvg_id and group not in INACTIVE_GROUPS:
                    # An explicit @territory qualifier overrides the base channel
                    # origin and a broad country group (for example XITEHits.nl@UK).
                    code = playlist_entry_country_code(
                        tvg_id, current.get("tvg-country", ""), group
                    )
                    if code:
                        countries.add(code)
                current = None
    return countries


def source_country_codes(source):
    """Infer a source region only from a country-specific feed path or known provider family."""
    parsed = urlparse(str(source or ""))
    host = (parsed.hostname or "").casefold()
    path = parsed.path.casefold()
    code = ""
    match = None
    if host.endswith("iptv-epg.org"):
        match = re.search(r"/epg-([a-z]{2})\.xml(?:\.gz)?$", path)
    elif host.endswith("free-epg.de"):
        match = re.search(r"/api/epg/([a-z]{2})\.xml\.gz$", path)
    elif host.endswith("epgshare01.online"):
        match = re.search(r"epg_ripper_([a-z]{2})\d+\.xml\.gz$", path)
    elif host.endswith("epg.lat"):
        match = re.search(r"/([a-z]{2})\.xml\.gz$", path)
    elif host.endswith("mjh.nz"):
        match = re.search(r"/([a-z]{2})\.xml$", path)
    elif host.endswith("m3u-edit.com"):
        filename = parse_qs(parsed.query).get("file", [""])[0].casefold()
        if filename.startswith("in") or "india" in filename:
            code = "IN"
    elif host.endswith("open-epg.com"):
        filename = Path(path).name
        if filename.startswith("india."):
            code = "IN"
        elif filename.startswith("unitedkingdom."):
            code = "GB"
    elif host == "raw.githubusercontent.com" and "/jasonramg/iptv-epg/main/epg/" in path:
        # Sling TV is a US service; the other provider exports in this repository are India-oriented.
        code = "US" if Path(path).name == "slingtv.xml" else "IN"
    elif host == "avkb.short.gy":
        code = "IN"
    if match:
        code = match.group(1).upper()
    normalized = normalize_country_code(code)
    return {normalized} if normalized else set()


def sources_with_mapped_channels(source_urls):
    """Keep mapped feeds plus country-specific discovery feeds for active playlist regions."""
    source_urls = list(source_urls)
    if not MAPPING.is_file():
        print("EPG source pruning skipped: mapping CSV is missing.")
        return source_urls
    try:
        mapped_sources = set()
        with MAPPING.open(encoding="utf-8-sig", newline="") as handle:
            for row in csv.DictReader(handle):
                for source in (part.strip() for part in (row.get("source") or "").split("|")):
                    if source:
                        mapped_sources.add(source)
    except (OSError, csv.Error, UnicodeError) as exc:
        print(f"EPG source pruning skipped: cannot read mapping CSV ({exc}).")
        return source_urls
    private_url = os.environ.get(PRIVATE_SOURCE_ENV, "").strip()
    active_countries = active_playlist_country_codes()
    discovery_sources = {
        source for source in source_urls
        if source_country_codes(source) & active_countries
    }
    selected = [
        source for source in source_urls
        if source in mapped_sources
        or source in (HUM_TV_SOURCE, RTV_SOURCE, BTV_SOURCE, MAASRANGA_SOURCE)
        or source.startswith("file://")
        or (private_url and source == private_url)
        or source in discovery_sources
    ]
    if not selected:
        print("EPG source pruning skipped: no mapped or region-relevant source URLs found.")
        return source_urls
    print(
        f"EPG source pruning: using {len(selected)} of {len(source_urls)} feeds; "
        f"{len(discovery_sources)} are country-discovery feeds for {len(active_countries)} active regions."
    )
    return selected


def source_label(src):
    if src == os.environ.get(PRIVATE_SOURCE_ENV, "").strip():
        return PRIVATE_SOURCE_LABEL
    if src == MAASRANGA_SOURCE:
        return "Maasranga official weekly grid (undated)"
    return src

CHANNEL_TIME_OFFSETS = {
    "ColorsCineplex.in@SD": timedelta(hours=2),
}

GENERIC_TITLES = {
    "movie", "movies", "program", "programme", "entertainment", "live", "live tv",
    "tba", "to be announced", "unknown", "schedule", "telecast", "show",
    "music", "test", "testing", "coming soon",
}
PLACEHOLDER_TITLES = {
    "no data", "no information", "no info", "n/a", "none", "no title",
    "no program", "no programs", "no programme", "no programmes",
    "no schedule", "no schedule available", "not available",
    "program not available", "programme not available",
    # Scheduling-system slot labels (no real programme information).
    "slot", "commercial slot", "ad slot", "advertisement slot", "filler",
    # "No schedule" markers emitted by non-English feeds.
    "brak zaplanowanych emisji", "sin programación", "sin programacion",
    "programación no disponible", "kein programm", "keine sendung",
}
GENERIC_TITLES |= PLACEHOLDER_TITLES
SINGLE_SHOW_CHANNEL_IDS = {"Mythbusters.us", "AxMen.us", "StrawberryShortcake.us", "Teletubbies.uk", "WildEarth.za"}


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "BDIX-IPTV-EPG/1.0", "Accept": "application/gzip,application/xml,*/*"})
    with urllib.request.urlopen(req, timeout=SOURCE_FETCH_TIMEOUT_SECONDS) as r:
        data = r.read()
    if data[:2] == b"\x1f\x8b" or url.endswith(".gz"):
        data = gzip.decompress(data)
    return data


def fetch_xmltv_sources_concurrently(source_urls, max_workers=SOURCE_FETCH_WORKERS):
    """Fetch ordinary XMLTV feeds concurrently, preserving per-URL results and errors."""
    urls = [url for url in source_urls if url not in (HUM_TV_SOURCE, RTV_SOURCE, BTV_SOURCE, MAASRANGA_SOURCE)]
    if not urls:
        return {}, {}
    workers = max(1, min(int(max_workers), len(urls)))
    payloads = {}
    errors = {}
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(fetch, url): url for url in urls}
        for future in as_completed(futures):
            url = futures[future]
            try:
                payloads[url] = future.result()
            except Exception as exc:
                errors[url] = exc
            completed = len(payloads) + len(errors)
            print(
                f"EPG feed progress: {completed}/{len(urls)} complete; "
                f"{len(payloads)} succeeded, {len(errors)} failed.",
                flush=True,
            )
    return payloads, errors


def playlist_channels():
    """Include primary channel IDs from the two maintained playlists, keeping main-list names first."""
    out = {}
    for playlist_path in PLAYLISTS:
        if not playlist_path.exists():
            continue
        for line in playlist_path.read_text(encoding="utf-8-sig").splitlines():
            if not line.startswith("#EXTINF:"):
                continue
            attrs = {}
            for m in re.finditer(r'([\w-]+)="([^"]*)"', line):
                attrs[m[1]] = m[2]
            group = attrs.get("group-title", "").strip()
            tvg_id = attrs.get("tvg-id", "").strip()
            name = attrs.get("tvg-name", "").strip() or line.rsplit(",", 1)[-1].strip()
            if tvg_id and group not in INACTIVE_GROUPS:
                out.setdefault(tvg_id, name)
    return out


def playlist_groups():
    """Return the first active group for each playlist identity."""
    groups = {}
    for playlist_path in PLAYLISTS:
        if not playlist_path.exists():
            continue
        for line in playlist_path.read_text(encoding="utf-8-sig").splitlines():
            if not line.startswith("#EXTINF:"):
                continue
            attrs = {}
            for m in re.finditer(r'([\w-]+)="([^"]*)"', line):
                attrs[m[1]] = m[2]
            group = attrs.get("group-title", "").strip()
            tvg_id = attrs.get("tvg-id", "").strip()
            if tvg_id and group not in INACTIVE_GROUPS:
                groups.setdefault(tvg_id, group)
    return groups

import unicodedata
TEXT_FIELDS = {"title", "sub-title", "desc"}
XML_LANG = "{http://www.w3.org/XML/1998/namespace}lang"
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
    lang = (elem.attrib.get(XML_LANG) or elem.attrib.get("lang") or "").strip().lower()
    if lang:
        if lang in LANG_PRIORITY:
            return LANG_PRIORITY[lang]
        for prefix, rank in LANG_PREFIXES:
            if lang.startswith(prefix):
                return rank
        return 1
    return _script_rank(text)


def is_english_text_element(elem):
    text = (elem.text or "").strip()
    if not text:
        return True
    lang = (elem.attrib.get(XML_LANG) or elem.attrib.get("lang") or "").strip().lower()
    if lang and any(lang.startswith(prefix) for prefix, _ in LANG_PREFIXES):
        return True
    if lang in LANG_PRIORITY:
        return True
    return any(unicodedata.category(char).startswith("L") for char in text)


def preferred_title_element(elem):
    titles = [x for x in elem.findall("title") if (x.text or "").strip()]
    if not titles:
        return None
    return max(titles, key=lambda x: (language_priority(x), len((x.text or "").strip()), -(titles.index(x))))


def load_mapping():
    reverse = {}
    if not MAPPING.exists():
        return reverse
    with MAPPING.open(encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh):
            target = row.get("tvg_id", "").strip()
            if not target:
                continue
            ids = [x.strip() for x in row.get("epg_id", "").split("|") if x.strip()]
            if row.get("group", "").strip() == "Indian Bangla":
                ids = ids[:1]
            for source_id in ids:
                reverse.setdefault(source_id, set()).add(target)
    return {source_id: sorted(targets) for source_id, targets in reverse.items()}


def stamp(value):
    try:
        raw = str(value).strip()
        if len(raw) < 14:
            return None
        dt = datetime.strptime(raw[:14], "%Y%m%d%H%M%S")
        if len(raw) >= 20 and raw[15] in "+-":
            sign = 1 if raw[15] == "+" else -1
            hh = int(raw[16:18])
            mm = int(raw[18:20])
            dt = dt.replace(tzinfo=timezone(sign * timedelta(hours=hh, minutes=mm)))
        else:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except Exception:
        return None


def normalized_title(title):
    return re.sub(r"\s+", " ", (title or "").strip().lower())

SLOT_PLACEHOLDER_RE = re.compile(r"^(program|programme|show|slot)\s*@\s*\d")


def is_slot_placeholder(title):
    return bool(SLOT_PLACEHOLDER_RE.match(normalized_title(title)))


def title_score(title):
    t = normalized_title(title)
    if not t or t in GENERIC_TITLES or len(t) <= 2 or is_slot_placeholder(t):
        return 0
    return 1.0 + min(len(t), 80) / 400.0

ALWAYS_DROP_GENERIC_TITLES = {"movie", "movies"} | PLACEHOLDER_TITLES


def channel_key(text):
    return re.sub(r"[^a-z0-9]", "", re.sub(r"\(.*?\)", "", (text or "").lower()))

NAME_FILLER_MIN_SHARE = 0.8
NAME_FILLER_MIN_SIMILARITY = 0.9
_NAME_NOISE_SUFFIXES = ("channel", "network", "live", "tv", "hd", "sd")


def _core_name_key(key):
    """Drop trailing generic words (tv, hd, channel...) so 'AmarBanglaTV' ~ 'AmarBangla'."""
    changed = True
    while changed:
        changed = False
        for suffix in _NAME_NOISE_SUFFIXES:
            if key.endswith(suffix) and len(key) - len(suffix) >= 4:
                key = key[: -len(suffix)]
                changed = True
    return key


def _identity_stem(target):
    """Name part of a tvg-id such as 'ZeeBanglaSonar.in@SD' -> 'ZeeBanglaSonar'."""
    return re.split(r"[.@]", target or "", maxsplit=1)[0]


def repeats_channel_name(title, channel_name, target=None):
    """True when a programme title merely repeats the channel's own name.

    The match is exact on the playlist name, or on the tvg-id's name part, or a
    near-identical spelling (e.g. 'Amar Bangla TV' vs 'Aamar Bangla'). The caller
    only applies this to channels where most rows repeat the name, so a genuine
    programme that happens to share a channel's name is left alone.
    """
    title_key = channel_key(title)
    if not title_key:
        return False
    candidates = {k for k in (channel_key(channel_name), channel_key(_identity_stem(target))) if k}
    if title_key in candidates:
        return True
    core_title = _core_name_key(title_key)
    for candidate in candidates:
        core = _core_name_key(candidate)
        if len(core) >= 4 and len(core_title) >= 4 and SequenceMatcher(None, core_title, core).ratio() >= NAME_FILLER_MIN_SIMILARITY:
            return True
    return False


def name_filled_targets(by_target, channel_names):
    if not channel_names:
        return set()
    filled = set()
    for target, records in by_target.items():
        if not records or target in SINGLE_SHOW_CHANNEL_IDS:
            continue
        name = channel_names.get(target, "")
        same = sum(1 for r in records if repeats_channel_name(r["title"], name, target))
        if same / len(records) >= NAME_FILLER_MIN_SHARE:
            filled.add(target)
    return filled


def filter_generic_candidates(by_target, channel_names=None):
    filled_targets = name_filled_targets(by_target, channel_names)
    named_targets = {
        target for target, records in by_target.items()
        if any(title_score(record["title"]) > 0 and not (target in filled_targets and repeats_channel_name(record["title"], channel_names.get(target, ""), target)) for record in records)
    }
    removed = 0
    for target, records in list(by_target.items()):
        kept = []
        for record in records:
            title = normalized_title(record["title"])
            if title in ALWAYS_DROP_GENERIC_TITLES or is_slot_placeholder(title):
                removed += 1
                continue
            if target in filled_targets and repeats_channel_name(record["title"], channel_names.get(target, ""), target):
                removed += 1
                continue
            if target in named_targets and title_score(record["title"]) <= 0:
                removed += 1
                continue
            kept.append(record)
        by_target[target] = kept
    return removed


def clone_children(elem):
    preferred = preferred_title_element(elem)
    children = []
    for child in list(elem):
        if child.tag == "title":
            if child is preferred:
                children.append(ET.fromstring(ET.tostring(child, encoding="utf-8")))
            continue
        children.append(ET.fromstring(ET.tostring(child, encoding="utf-8")))
    return children


def shift_xmltv_timestamp(value, delta):
    raw = (value or "").strip()
    if not raw or not delta:
        return raw
    try:
        base = raw[:14]
        suffix = raw[14:].strip()
        dt = datetime.strptime(base, "%Y%m%d%H%M%S")
        if suffix and re.fullmatch(r"[+-]\d{4}", suffix):
            sign = 1 if suffix[0] == "+" else -1
            hh = int(suffix[1:3])
            mm = int(suffix[3:5])
            tz = timezone(sign * timedelta(hours=hh, minutes=mm))
            dt = dt.replace(tzinfo=tz) + delta
            return dt.strftime("%Y%m%d%H%M%S") + " " + suffix
        dt = dt + delta
        return dt.strftime("%Y%m%d%H%M%S") + ((" " + suffix) if suffix else "")
    except Exception:
        return raw


def interval_weight(record):
    start = record["start_dt"]
    stop = record["stop_dt"]
    duration = (stop - start).total_seconds() if stop else 0
    hours = duration / 3600.0 if duration > 0 else 0
    weight = 100.0
    if title_score(record["title"]) > 0:
        weight += 8.0
    weight += {3: 30.0, 2: 20.0, 1: 10.0}.get(record.get("language_rank", 1), 10.0)
    source_index = record["source_index"]
    weight += max(0.0, (len(SOURCES) - source_index) / len(SOURCES)) * 3.0
    if 0.25 <= hours <= 8:
        weight += 1.0
    elif hours > 12:
        weight -= min(5.0, (hours - 12) * 0.25)
    return max(1.0, weight)


def clean_schedule(records):
    unique = {}
    for r in records:
        if not r["stop_dt"] or r["stop_dt"] <= r["start_dt"]:
            continue
        key = (r["start_dt"], r["stop_dt"], normalized_title(r["title"]))
        old = unique.get(key)
        if old is None:
            unique[key] = r
        else:
            old_quality = (old.get("language_rank", 1), title_score(old["title"]), -old["source_index"])
            new_quality = (r.get("language_rank", 1), title_score(r["title"]), -r["source_index"])
            if new_quality > old_quality:
                unique[key] = r
    items = sorted(unique.values(), key=lambda r: (r["stop_dt"], r["start_dt"], normalized_title(r["title"])))
    if not items:
        return []
    stops = [r["stop_dt"] for r in items]
    prev = [bisect.bisect_right(stops, r["start_dt"]) - 1 for r in items]
    dp_score = [0.0] * (len(items) + 1)
    dp_count = [0] * (len(items) + 1)
    take = [False] * len(items)
    for i, r in enumerate(items, start=1):
        skip_score = dp_score[i - 1]
        skip_count = dp_count[i - 1]
        j = prev[i - 1] + 1
        take_score = dp_score[j] + interval_weight(r)
        take_count = dp_count[j] + 1
        if (take_score > skip_score + 1e-9) or (abs(take_score - skip_score) <= 1e-9 and take_count > skip_count):
            dp_score[i] = take_score
            dp_count[i] = take_count
            take[i - 1] = True
        else:
            dp_score[i] = skip_score
            dp_count[i] = skip_count
    chosen = []
    i = len(items)
    while i > 0:
        if take[i - 1]:
            chosen.append(items[i - 1])
            i = prev[i - 1] + 1
        else:
            i -= 1
    chosen.reverse()
    return chosen


def infer_source_offsets(records):
    signatures = {}
    for r in records:
        start, stop = r.get("start_dt"), r.get("stop_dt")
        title = normalized_title(r.get("title"))
        if not start or not stop or stop <= start or title_score(title) == 0:
            continue
        duration_bin = round((stop - start).total_seconds() / 300)
        key = (title, duration_bin)
        signatures.setdefault(key, {}).setdefault((r["source_index"], r["source_id"]), []).append(r)
    proposals = {}
    for source_map in signatures.values():
        unique = {source_key: rows[0] for source_key, rows in source_map.items() if len(rows) == 1}
        if len(unique) < 3:
            continue
        ordered = sorted(unique.items(), key=lambda item: item[1]["start_dt"])
        clusters = []
        for item in ordered:
            start = item[1]["start_dt"]
            if not clusters or (start - clusters[-1][-1][1]["start_dt"]).total_seconds() > 600:
                clusters.append([item])
            else:
                clusters[-1].append(item)
        if len(clusters) < 2:
            continue
        consensus = max(clusters, key=len)
        if len(consensus) < 2:
            continue
        consensus_sources = {item[0] for item in consensus}
        consensus_start = sorted(item[1]["start_dt"] for item in consensus)[len(consensus) // 2]
        for cluster in clusters:
            if cluster is consensus or len(cluster) != 1:
                continue
            source_key, record = cluster[0]
            if source_key in consensus_sources:
                continue
            delta = consensus_start - record["start_dt"]
            minutes = round(delta.total_seconds() / 300) * 5
            if abs(minutes) >= 120:
                proposals.setdefault(source_key, []).append(minutes)
    corrections = {}
    for source_key, minutes_list in proposals.items():
        buckets = {}
        for minutes in minutes_list:
            buckets[minutes] = buckets.get(minutes, 0) + 1
        best_minutes, best_count = max(buckets.items(), key=lambda item: item[1])
        if best_count >= 4 and best_count / len(minutes_list) >= 0.75:
            corrections[source_key] = timedelta(minutes=best_minutes)
    return corrections


SOURCE_OFFSET_PATTERN_MIN_IDS = 5


def source_offset_patterns(events):
    """Flag feeds whose channels are repeatedly corrected by the same large offset.

    events: iterable of (source_label, target_id, delta). A feed with at least
    SOURCE_OFFSET_PATTERN_MIN_IDS distinct channels shifted by the identical delta most
    likely has a timezone problem for the whole feed. This only reports the pattern; it
    never applies the shift to channels that lack cross-source evidence.
    """
    grouped = {}
    for label, target, delta in events:
        grouped.setdefault((label, delta), set()).add(target)
    lines = []
    for (label, delta), targets in sorted(grouped.items(), key=lambda item: (-len(item[1]), item[0][0])):
        if len(targets) >= SOURCE_OFFSET_PATTERN_MIN_IDS:
            lines.append(
                "- **{}**: {} channels were corrected by the same {:+g} hours. This looks like a feed-wide timezone problem; "
                "other channels from this feed without cross-source overlap may still be shifted and should be reviewed.".format(
                    label, len(targets), delta.total_seconds() / 3600))
    return lines


def main():
    channels = playlist_channels()
    groups = playlist_groups()
    reverse = load_mapping()
    print(f"EPG generator inputs: active playlist IDs={len(channels)}; source-to-playlist mapping IDs={len(reverse)}; mapping file={MAPPING}; exists={MAPPING.exists()}")
    if not channels:
        raise SystemExit("No active playlist channel IDs found in the two playlists")
    if not reverse:
        raise SystemExit("EPG mapping registry has no source IDs; inspect reports/epg-channel-mapping.csv generated by epg_coverage.py")
    mapped_targets = {}
    for source_id, targets in reverse.items():
        for target in targets:
            if target in channels:
                mapped_targets.setdefault(target, set()).add(source_id)
    if not mapped_targets:
        raise SystemExit("No mapped playlist channels found in EPG mapping")
    now = datetime.now(timezone.utc)
    lower = now - timedelta(hours=6)
    upper = now + timedelta(days=7)
    candidates = {}
    source_stats = {}
    source_urls = sources_with_mapped_channels(configured_sources())
    fetchable_count = sum(src not in (HUM_TV_SOURCE, RTV_SOURCE, BTV_SOURCE, MAASRANGA_SOURCE) and not src.startswith("file://") for src in source_urls)
    print(f"EPG source fetch: {fetchable_count} XMLTV feeds, max_workers={SOURCE_FETCH_WORKERS}, timeout={SOURCE_FETCH_TIMEOUT_SECONDS}s")
    source_payloads, source_errors = fetch_xmltv_sources_concurrently(source_urls)
    print(f"EPG source fetch complete: {len(source_payloads)} succeeded, {len(source_errors)} failed")
    for source_index, src in enumerate(source_urls):
        try:
            if src in (HUM_TV_SOURCE, RTV_SOURCE, BTV_SOURCE, MAASRANGA_SOURCE):
                if src == HUM_TV_SOURCE:
                    schedule_id, schedule_fetch, schedule_label = (HUM_TV_CHANNEL_ID, fetch_hum_tv_programmes, "HUM TV")
                elif src == RTV_SOURCE:
                    schedule_id, schedule_fetch, schedule_label = (RTV_CHANNEL_ID, fetch_rtv_programmes, "RTV")
                elif src == BTV_SOURCE:
                    schedule_id, schedule_fetch, schedule_label = (BTV_CHANNEL_ID, fetch_btv_programmes, "BTV National")
                else:
                    schedule_id, schedule_fetch, schedule_label = (MAASRANGA_CHANNEL_ID, fetch_maasranga_programmes, "Maasranga TV")
                schedule_targets = [target for target in reverse.get(schedule_id, []) if target in mapped_targets]
                if not schedule_targets:
                    source_stats[src] = f"SKIPPED: no active exact {schedule_label} mapping"
                    continue
                schedule_programmes = schedule_fetch(now)
                source_stats[src] = f"OK: {len(schedule_programmes)} timed official slots"
                for programme in schedule_programmes:
                    source_id = programme["channel_id"]
                    title = programme["title"]
                    start_dt = programme["start_dt"]
                    stop_dt = programme["stop_dt"]
                    attrs = {"channel": schedule_id, "start": start_dt.strftime("%Y%m%d%H%M%S %z"), "stop": stop_dt.strftime("%Y%m%d%H%M%S %z")}
                    title_elem = ET.Element("title", {"lang": "bn"} if src == MAASRANGA_SOURCE else {})
                    title_elem.text = title
                    for target in schedule_targets:
                        channel_attrs = dict(attrs)
                        channel_attrs["channel"] = target
                        rec = {
                            "attrs": channel_attrs,
                            "title": title,
                            "language_rank": language_priority(title_elem),
                            "children": [ET.fromstring(ET.tostring(title_elem, encoding="utf-8"))],
                            "start_dt": start_dt,
                            "stop_dt": stop_dt,
                            "source_index": source_index,
                            "source": src,
                            "source_id": source_id,
                        }
                        candidates.setdefault((target, source_index, source_id), []).append(rec)
                continue
            if src in source_errors:
                raise RuntimeError(f"bounded source fetch failed: {source_errors[src]}")
            if src not in source_payloads:
                raise RuntimeError("source fetch returned no payload")
            source_stats[src] = "OK"
            data = source_payloads[src]
            for _, elem in ET.iterparse(io.BytesIO(data), events=("end",)):
                if elem.tag != "programme":
                    continue
                source_id = elem.attrib.get("channel", "").strip()
                targets = [target for target in reverse.get(source_id, []) if target in mapped_targets]
                if not targets:
                    elem.clear()
                    continue
                start_dt = stamp(elem.attrib.get("start", ""))
                stop_dt = stamp(elem.attrib.get("stop", "")) if elem.attrib.get("stop") else None
                if not start_dt or start_dt > upper or (stop_dt and stop_dt < lower):
                    elem.clear()
                    continue
                title_elem = preferred_title_element(elem)
                title = (title_elem.text or "").strip() if title_elem is not None else ""
                children = clone_children(elem)
                for target in targets:
                    if title_elem is None or not (title_elem.text or "").strip() or not is_english_text_element(title_elem):
                        continue
                    safe_children = []
                    for child in children:
                        if child.tag in TEXT_FIELDS and not is_english_text_element(child):
                            continue
                        safe_children.append(ET.fromstring(ET.tostring(child, encoding="utf-8")))
                    attrs = dict(elem.attrib)
                    attrs["channel"] = target
                    rec = {
                        "attrs": attrs,
                        "title": title,
                        "language_rank": language_priority(title_elem),
                        "children": safe_children,
                        "start_dt": start_dt,
                        "stop_dt": stop_dt,
                        "source_index": source_index,
                        "source": src,
                        "source_id": source_id,
                    }
                    candidates.setdefault((target, source_index, source_id), []).append(rec)
                elem.clear()
        except Exception as exc:
            source_stats[src] = f"FAILED: {exc}"
    by_target = {}
    for (target, source_index, source_id), records in candidates.items():
        by_target.setdefault(target, []).extend(records)
    generic_removed = filter_generic_candidates(by_target, channels)
    root = ET.Element("tv", {"generator-info-name": "BDIX-IPTV EPG", "generator-info-url": "https://github.com/saeidrahmanbd/BDIX-IPTV"})
    for target in sorted(mapped_targets):
        ch = ET.SubElement(root, "channel", {"id": target})
        ET.SubElement(ch, "display-name").text = channels[target]
    final_count = 0
    raw_count = 0
    removed_count = 0
    generic_counts = 0
    timing_audit = [
        "# EPG Timing Audit",
        "",
        "Automatic corrections require repeated cross-source title and duration matches, at least four consistent matches, >=75% agreement, at least three source IDs, and a displacement of two hours or more.",
        "",
        "## Detected corrections",
        "",
    ]
    correction_count = 0
    offset_events = []
    for target in sorted(mapped_targets):
        records = by_target.get(target, [])
        corrections = infer_source_offsets(records)
        for source_key, delta in corrections.items():
            source_index, source_id = source_key
            matching = [r for r in records if r["source_index"] == source_index and r["source_id"] == source_id]
            for r in matching:
                r["start_dt"] = r["start_dt"] + delta
                if r["stop_dt"]:
                    r["stop_dt"] = r["stop_dt"] + delta
                r["source_offset"] = delta
            correction_count += 1
            offset_events.append((source_label(source_urls[source_index]), target, delta))
            timing_audit.append("- **{}** ({}): source ID {} from {} shifted by {:+g} hours after repeated cross-source agreement.".format(channels[target], target, source_id, source_label(source_urls[source_index]), delta.total_seconds() / 3600))
        cleaned = clean_schedule(records)
        raw_count += len(records)
        removed_count += len(records) - len(cleaned)
        generic_counts += sum(1 for r in cleaned if title_score(r["title"]) == 0)
        channel_offset = CHANNEL_TIME_OFFSETS.get(target, timedelta(0))
        for r in cleaned:
            attrs = dict(r["attrs"])
            total_offset = channel_offset + r.get("source_offset", timedelta(0))
            if total_offset:
                attrs["start"] = shift_xmltv_timestamp(attrs.get("start", ""), total_offset)
                if attrs.get("stop"):
                    attrs["stop"] = shift_xmltv_timestamp(attrs.get("stop", ""), total_offset)
            p = ET.Element("programme", attrs)
            for child in r["children"]:
                p.append(ET.fromstring(ET.tostring(child, encoding="utf-8")))
            root.append(p)
            final_count += 1
        print(f"  {target}: candidates {len(records)}, clean {len(cleaned)}, removed {len(records) - len(cleaned)}")
    if final_count == 0:
        raise SystemExit("No current/future programmes were generated; refusing to publish empty guide")
    print(f"EPG candidate pool: {raw_count} mapped programmes before cleanup")
    print(f"EPG cleanup: removed {removed_count} exact-duplicate/overlapping programmes")
    print(f"EPG cleanup: retained {generic_counts} generic-title programmes where no named schedule was available")
    print(f"EPG cleanup: excluded {generic_removed} generic-title placeholder candidates")
    print(f"EPG generated: {len(mapped_targets)} mapped channels, {final_count} programmes")
    if correction_count == 0:
        timing_audit.append("- No source offsets met the strict automatic-correction threshold.")
    pattern_lines = source_offset_patterns(offset_events)
    if pattern_lines:
        timing_audit.extend(["", "## Feed-wide offset patterns", ""] + pattern_lines)
    timing_audit.extend(["", f"Detected source-ID corrections: **{correction_count}**", ""])
    Path("reports").mkdir(parents=True, exist_ok=True)
    Path("reports/epg-timing-audit.md").write_text("\n".join(timing_audit), encoding="utf-8")
    ET.indent(root, space="  ")
    OUTPUT.write_bytes(b'<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(root, encoding="utf-8"))

if __name__ == "__main__":
    main()
