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
from urllib.parse import urlparse
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta
from pathlib import Path
from official_epg_sources import (
    HUM_TV_SOURCE, HUM_TV_CHANNEL_ID, fetch_hum_tv_programmes,
    RTV_SOURCE, RTV_CHANNEL_ID, fetch_rtv_programmes,
)

PLAYLISTS = [
    Path("IPTV-Playlist.m3u"),
    Path("BDIX-Playlist.m3u"),
    Path("International-Playlist.m3u"),
]
INACTIVE_GROUPS = {"Backup", "Test", "Not Playing"}
MAPPING = Path("reports/epg-channel-mapping.csv")
OUTPUT = Path("epg/epg.xml")

# Bound the worst-case wait for a batch of remote XMLTV feeds.
SOURCE_FETCH_TIMEOUT_SECONDS = 20
SOURCE_FETCH_WORKERS = 8

SOURCES = [
    "https://epgshare01.online/epgshare01/epg_ripper_IN1.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_IN2.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz",
    "https://iptv-epg.org/files/epg-in.xml.gz",
    # EPG.PW India guide supplements Indian-channel schedule coverage.
    "https://epg.pw/xmltv/epg_IN.xml.gz",
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


def sources_with_mapped_channels(source_urls):
    """Skip feeds that have no current mapped source IDs; retain local/official adapters.

    Coverage discovery runs immediately before generation and records which source
    feeds actually matched a playlist identity in the mapping CSV. Parsing large
    global feeds that have no mapped IDs wastes time and can stall publication.
    If the mapping snapshot cannot be read, fall back to all configured sources
    rather than silently shrinking the guide.
    """
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

    selected = [
        source for source in source_urls
        if source in mapped_sources
        or source in (HUM_TV_SOURCE, RTV_SOURCE)
        or source.startswith("file://")
    ]
    # A completely empty hit set is not evidence that no source can help.
    # Keep the configured list and let the regular quality gate decide.
    if not selected:
        print("EPG source pruning skipped: no mapped source URLs found.")
        return source_urls
    print(
        f"EPG source pruning: using {len(selected)} of {len(source_urls)} configured feeds "
        "with current mapping hits (plus local/official adapters)."
    )
    return selected


def source_label(src):
    if src == os.environ.get(PRIVATE_SOURCE_ENV, "").strip():
        return PRIVATE_SOURCE_LABEL
    return src


# Per-channel broadcast-delay corrections, in hours.
# Colors Cineplex's upstream guide is 2 hours behind the live stream.
CHANNEL_TIME_OFFSETS = {
    "ColorsCineplex.in@SD": timedelta(hours=2),
}

GENERIC_TITLES = {
    "movie", "movies", "program", "programme", "entertainment", "live", "live tv",
    "tba", "to be announced", "unknown", "schedule", "telecast", "show",
    "music", "test", "testing", "coming soon",
}

# Empty-content fillers that some feeds emit instead of a programme title
# (for example "No Data"). They carry no schedule information, so they are
# never published, even when they are the only rows a channel has.
PLACEHOLDER_TITLES = {
    "no data", "no information", "no info", "n/a", "none", "no title",
    "no program", "no programs", "no programme", "no programmes",
    "no schedule", "no schedule available", "not available",
    "program not available", "programme not available",
}
GENERIC_TITLES |= PLACEHOLDER_TITLES

# Channels that genuinely broadcast a single show, where a programme title that
# equals the channel name is real content rather than a feed filler.
SINGLE_SHOW_CHANNEL_IDS = {
    "Mythbusters.us", "AxMen.us", "StrawberryShortcake.us", "Teletubbies.uk",
}

def fetch(url):
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "BDIX-IPTV-EPG/1.0",
            "Accept": "application/gzip,application/xml,*/*",
        },
    )
    with urllib.request.urlopen(req, timeout=SOURCE_FETCH_TIMEOUT_SECONDS) as r:
        data = r.read()
    if data[:2] == b"\x1f\x8b" or url.endswith(".gz"):
        data = gzip.decompress(data)
    return data

def fetch_xmltv_sources_concurrently(source_urls, max_workers=SOURCE_FETCH_WORKERS):
    """Fetch ordinary XMLTV feeds concurrently, preserving per-URL results and errors.

    The caller still processes the returned dictionaries in the configured source
    order, so source-priority tie-breaking and generated schedule ordering do not
    depend on thread completion order. HUM TV / RTV use dedicated schedule
    parsers and are intentionally excluded from generic XMLTV retrieval.
    """
    urls = [
        url for url in source_urls
        if url not in (HUM_TV_SOURCE, RTV_SOURCE)
    ]
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
                # Isolate one bad feed; other sources remain available.
                errors[url] = exc
    return payloads, errors


def playlist_channels():