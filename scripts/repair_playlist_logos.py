#!/usr/bin/env python3
"""Repair missing, generic and known-contaminated logos across the three core maintained playlists.

# [manual-logo-localization] Explicit owner-requested retry after a guard-only run.

Policy: search this repository's /logos tree first (including /logos/unused),
then use exact channel/ID matches from curated sources, IPTV-org, or Wikimedia
Commons. Never invent a broadcaster logo or use an unrelated lookalike.\nActive groups require verified local logo assets; Review queues may retain missing\nlogo metadata while awaiting manual identity/source verification.
"""
import argparse
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import html
import json
import re
import shutil
import time
import unicodedata
import urllib.error
import urllib.parse

import logo_provenance
import logo_source_catalog as source

ROOT = Path(".")
LOGOS = Path("logos")
RAW_BASE = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/"
PLAYLISTS = ["IPTV-Playlist.m3u", "International-Playlist.m3u"]
REPORT = Path("reports/playlist-logo-repair-results.md")
REGISTRY_PATH = Path("reports/logo-source-registry.json")

# Manual rerun requested after correcting the verified Channel 52 allowlist and regression tests.
# [manual-logo-localization] Retry once with the collision-safe canonical asset fallback.
# The following files were visually inspected and found contaminated, generic,
# or mismatched. A bad file is never reused, even if its filename is an exact
# channel-name match.
BAD_ASSETS = {
    "atn-news.png",
    "a-sports-5485adff.png",
    "a-sports-hd.png",
    "bein-sports-3.png",
    "bangla-tv.png",
    "btv-news.png",  # M3U World 4K branding is embedded in the image.
    "colors.png",
    "duronto-tv.png",
    "duronto-tv-1ad55c95.png",  # alternate contains an embedded phone number.
    "ekushey-tv.png",
    "global-tv.png",
    "green-tv.png",
    "mohona-tv.png",
    "nagorik-tv.png",
    "nagorik.png",
    "nick-bangla.png",
    "sananda-tv.png",
    "sananda.png",  # SUN Bangla image, not Sananda.
    "star-gold-select.png",
    "star-gold.png",
    "star-plus.png",
    "zee-tv.png",
    "tom-and-jerry.png",
    "arirang-tv.png",  # KBS WORLD wordmark under an Arirang filename.
    "channel-52-converted-56518832e7.png",  # Superseded contaminated conversion; channel-52.png is the authentic historic broadcaster mark.
    "jtv-bangla.png", "jtv-bangla-converted-91bd17c8e4.png",  # Generic text-only artwork, not a verified JTV Bangla broadcaster logo.
    "classic-movies-27994c39.png",  # Unofficial generated label artwork; clean local logo is in /logos/unused.
    "wow-kidz-tamil.png",  # Contains the Hindi-language suffix; not correct for the Tamil feed.
    "16-a308b78988.png",  # Provenance maps this image to Channel16.ru; it was reused on unrelated channels.
    # Same 160x60 placeholder artwork was reused for three unrelated stations.
    "shikor-tv-canada-ac43f0fa9e.png",
    "ten-tv-prime-ac43f0fa9e.png",
    "tv-one-uk-ac43f0fa9e.png",
}
# Generated fallback artwork is disabled: never invent channel logos.
# If an authentic local or source-attributed logo cannot be verified, leave
# the logo unresolved for manual review rather than assigning a fake mark.
GENERIC_ASSETS = {
    "placeholder-btv-news.png",
    "placeholder-channel-1.png",
    "placeholder-channel-16.png",
    "placeholder-channel-52.png",
}
BAD_ASSETS = {name.casefold() for name in BAD_ASSETS}
GENERIC_ASSETS = {name.casefold() for name in GENERIC_ASSETS}

# This alternate was visually inspected in /logos/unused and is clean.
# Use it instead of the contaminated root copy for Global TV.
LOCAL_OVERRIDES = {
    "global tv": "unused/global-tv-1080p-5ffc043912.png",
    "channel 1": "channel-1.png",
    "classic movies": "unused/classic-movies-channel-1d5f82d98a.png",
    "allo cine": "allo-cine-1080p.png",
    # Exact existing local channel marks visually checked against their channel identities.
    "asian sony max 2": "sony-max-2.png",
    "raj music telugu": "raj-musix-telugu-720p-e8fd0fb178.png",
    "rengoni tv": "rengoni.png",
    "news 21 bangla": "news-21-bangla-tv.png",
    # Exact channel-name matches already present in the repository logo library.
    "vevo 70s 80s": "vevo-70s-80s.png",
    "vevo 90s 00s": "vevo-90s-00s.png",
    # The stream is the XITE Celebrates feed; this is its existing local artwork.
    "xite summer": "xite-celebrates-0178ee79a4.png",
}
FORCED_CHANNEL_LOGOS = {
    "bollygold": "nh-bollygold-dbedeff9.png",
    "manoranjan grand": "manoranjan-grand.png",
    "zainabia channel": "zainabia-channel.png",  # user-supplied official channel logo
}

# Exact, source-attributed fallback URLs for unresolved channels. These are
# only consulted after the repository-wide local logo search. Keep them here
# so all playlist variants reuse the same locally stored image.
EXTRA_DIRECT_HINTS = {
    "WOW Kidz Tamil": {
        "url": "https://yt3.ggpht.com/a/AATXAJytH39NO3s4QEpDhzrKSGGEg0tf1c6c29ZzsQ%3Ds900-c-k-c0xffffffff-no-rj-mo",
        "format": "",
        "page": "https://www.youtube.com/channel/UCN8S4CqMRy6tVKVXvs7Bzeg",
        "license": "Official WowKidz channel avatar from the broadcaster\u2019s YouTube channel; shared brand wordmark without the incorrect Hindi-language suffix, used for the Tamil feed. Source attribution only; no separate copyright licence asserted.",
        "license_url": "",
    },
    # Owner-requested correction: exact historic logo shown in RisingBD's unveiling report.
    "Channel 52": {
        "url": "https://wsrv.nl/?url=cdn.risingbd.com%2Fmedia%2FimgAll%2F2013December%2F4420131228144155.jpg",
        "format": "JPEG",
        "page": "https://www.risingbd.com/চ্যানেল-৫২-এর-লোগো-উন্মোচন/30677",
        "license": "Exact Channel 52 logo image published with RisingBD\u2019s 28 December 2013 report on the broadcaster\u2019s logo unveiling; source attribution only, no separate copyright licence asserted.",
        "license_url": "",
    },
    "FIGHT | MVMT Culture": {
        "url": "https://media.unreel.me/prod/freelivesports/logo/98403785-3bba-4f7d-bee8-0eada4d790c8",
        "format": "",
        "page": "https://gist.github.com/sh400sp-ctrl/6bbd74b685e6bd0b79d329767e237949",
        "license": "Exact FIGHT | MVMT Culture logo paired with the same channel identity in a public Free Live Sports playlist; validate image bytes before localization",
        "license_url": "",
    },
    "WWE Superstar Central": {
        "url": "https://static.trademarkia.com/images/99048431",
        "format": "",
        "page": "https://www.trademarkia.com/ww-superstar-central-99048431",
        "license": "Exact figurative mark owned by World Wrestling Entertainment, LLC (WWE), from trademark filing serial 99048431; served by the trademark record image host, with source attribution only and no copyright licence implied",
        "license_url": "",
    },
    "Diema": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/d/d5/Diema_Bulgaria_logo.svg",
        "format": "SVG",
        "page": "https://commons.wikimedia.org/wiki/File:Diema_Bulgaria_logo.svg",
        "license": "Wikimedia Commons PD-textlogo; source credited to Nova Broadcasting Group via Predavatel; current Diema logo dated 12 May 2024",
        "license_url": "https://commons.wikimedia.org/wiki/Template:PD-textlogo",
    },
    "MBC Mood": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/1/12/MBC_Mood_Logo.png",
        "format": "PNG",
        "page": "https://commons.wikimedia.org/wiki/File:MBC_Mood_Logo.png",
        "license": "Wikimedia Commons PD-textlogo; source author MBC Group; 2026 MBC Mood logo; trademark notice retained",
        "license_url": "https://commons.wikimedia.org/wiki/Template:PD-textlogo",
    },
    "Tarab": {
        "url": "https://assets.mbcmood.com/channels/1738059679TARAB_Logo.png",
        "format": "PNG",
        "page": "https://github.com/iptv-org/database/issues/15624",
        "license": "Official MBC Mood CDN logo URL cited by the approved iptv-org/database Tarab channel record; source attribution only, no separate copyright licence asserted",
        "license_url": "",
    },
    "EKids": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/8/8f/E-Kids_logo_2024.svg",
        "format": "SVG",
        "page": "https://commons.wikimedia.org/wiki/File:E-Kids_logo_2024.svg",
        "license": "Original EKids channel artwork uploaded from the broadcaster's official ekids.bg website; Creative Commons Attribution 4.0 International",
        "license_url": "https://creativecommons.org/licenses/by/4.0/",
    },
    "FloRacing": {
        "url": "https://a.jsrdn.com/hls/22883/floracing-247/logo_20231219_225054_24.png",
        "format": "PNG",
        "page": "https://github.com/iptv-org/database/issues/27573",
        "license": "Exact FloRacing 24/7 channel logo URL listed in the approved iptv-org channel record; source attribution only, no separate copyright licence asserted",
        "license_url": "",
    },
    "Stingray Greatest Hits": {
        "url": "https://provider-static.plex.tv/epg/cms/production/b91ee9d9-43db-4505-bd6b-d76e6544156c/Greatest_hits_RDX_VERT.jpg",
        "format": "JPEG",
        "page": "https://watch.plex.tv/live-tv/channel/stingray-greatest-hits",
        "license": "Exact Stingray Greatest Hits channel artwork displayed on Plex's channel page; third-party source attribution only, no separate copyright licence asserted.",
        "license_url": "",
    },
    "Cinecanal Panregional": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/e/e6/CinecanalLA.png",
        "format": "PNG",
        "page": "https://commons.wikimedia.org/wiki/File:CinecanalLA.png",
        "license": "Wikimedia Commons PD-textlogo; source credited to Fox Networks Group Latin America; logo introduced September 2018",
        "license_url": "https://commons.wikimedia.org/wiki/Template:PD-textlogo",
    },
    "Channel Fight": {
        "url": "https://cdn.castify.ai/files/app/web/channelfightfutterlogo.png",
        "format": "PNG",
        "page": "https://www.channelfight.com/about",
        "license": "Official Channel Fight website image asset; channel identity confirmed on broadcaster's About page",
        "license_url": "",
    },
    "10 TV": {
        "url": "https://xstreamcp-assets-msp.streamready.in/assets/LIVETV/LIVECHANNEL/LIVETV_LIVETVCHANNEL_10TV/images/LOGO_HD/image.png",
        "format": "PNG",
        "page": "https://10tv.in/",
        "license": "10TV Telugu logo served by its live-TV asset CDN; channel identity matched to 10TV Telugu",
        "license_url": "",
    },
    "Espn5 HD": {
        "url": "https://media.philstar.com/photos/2021/10/13/espn-5_2021-10-13_11-24-12.jpg",
        "format": "JPEG",
        "page": "https://www.philstar.com/sports/2021/10/13/2133868/final-buzzer-sounds-espn5s-sports-website",
        "license": "Attributable ESPN5 brand image reproduced by Philstar; verify visual match before acceptance",
        "license_url": "",
    },
    "Htv Sport": {
        "url": "https://s935.cdn.mytvnet.vn/vimages/69/92/28/83/3b/b0/69283-phtvththao-channel-unkn.png",
        "format": "PNG",
        "page": "https://mytv.com.vn/truyen-hinh/18",
        "license": "HTV Thể thao channel logo shown on MyTV's channel page",
        "license_url": "",
    },
    "Wifm 100.9": {
        "url": "https://cdn-radiotime-logos.tunein.com/s29540g.png",
        "format": "PNG",
        "page": "https://tunein.com/radio/WIFM-FM-1009-s29540/",
        "license": "WIFM-FM 100.9 station logo served by TuneIn; verify exact station identity",
        "license_url": "",
    },
    "Bangla Hits": {
        "url": "https://proxy.zeno.fm/content/stations/agxzfnplbm8tc3RhdHNyMgsSCkF1dGhDbGllbnQYgICQ1rKLugsMCxIOU3RhdGlvblByb2ZpbGUbw/image/?u=1659476812000",
        "format": "",
        "page": "https://zeno.fm/radio/bangla-hits/",
        "license": "Exact station profile image from Zeno; inspect for watermark/phone overlays",
        "license_url": "",
    },
    "Doyel Radio": {
        "url": "https://proxy.zeno.fm/content/stations/37f5f5b0-24c4-41ac-bf3a-6e9232a16f57/image/?u=1667505462000",
        "format": "",
        "page": "https://zeno.fm/radio/doyel-radio/",
        "license": "Exact station profile image from Zeno",
        "license_url": "",
    },
    "Moner Radio": {
        "url": "https://proxy.zeno.fm/content/stations/agxzfnplbm8tc3RhdHNyMgsSCkF1dGhDbGllbnQYgICQ_6Wx8wsMCxIOU3RhdGlvblByb2ZpbGUbw/image/?u=1660620409000",
        "format": "",
        "page": "https://zeno.fm/radio/monarul/",
        "license": "Station profile image served by Zeno",
        "license_url": "",
    },
    "Radio Janata": {
        "url": "https://proxy.zeno.fm/content/stations/agxzfnplbm8tc3RhdHNyMgsSCkF1dGhDbGllbnQYgICQveDlzwoMCxIOU3RhdGlvblByb2ZpbGUbw/image/?u=1664520294000",
        "format": "",
        "page": "https://zeno.fm/radio/radio-janata/",
        "license": "Exact station profile image from Zeno",
        "license_url": "",
    },
    "Sagor FM": {
        "url": "https://proxy.zeno.fm/content/stations/agxzfnplbm8tc3RhdHNyMgsSCkF1dGhDbGllbnQYgICw4IKiugkMCxIOU3RhdGlvblByb2ZpbGUbw/image/?u=1661089415000",
        "format": "",
        "page": "https://zeno.fm/radio/sagor-fm/",
        "license": "Exact station profile image from Zeno; inspect for watermark/phone overlays",
        "license_url": "",
    },
    "Global Panjab": {
        "url": "https://is1-ssl.mzstatic.com/image/thumb/Purple116/v4/3c/d5/0d/3cd50d43-1337-94f9-dbcb-fc40334d51c8/App_Icon-marketing.lsr/1200x630bb.png",
        "format": "PNG",
        "page": "https://apps.apple.com/ca/app/global-punjab-tv/id1408487692",
        "license": "Global Punjab TV app branding served by Apple's App Store; original branding rights belong to broadcaster",
        "license_url": "",
    },
    "Nick Bangla": {
        "url": "https://otapp.store/uploads/tv_image/sm/nick-bangla.png",
        "format": "PNG",
        "page": "https://github.com/channeliptv0/IPTV/blob/f26247efa6b641fda8d6bb16f01f99f4948d8a3b/Master/Bangla.m3u",
        "license": "Channel-specific logo URL found in a public IPTV logo listing; original logo rights belong to broadcaster",
        "license_url": "",
    },
    "Alistiqamah": {
        "url": "https://i.imgur.com/2FPtYZr.png",
        "format": "PNG",
        "page": "https://iptv-org.github.io/channels/om/AlistiqamaTV",
        "license": "Station logo from IPTV-org channel listing",
        "license_url": "https://iptv-org.github.io/channels/om/AlistiqamaTV",
    },
    "Alone": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Alone_%28Leftfield_Pictures_TV_series%29_logo.svg",
        "format": "SVG",
        "page": "https://commons.wikimedia.org/wiki/File:Alone_(Leftfield_Pictures_TV_series)_logo.svg",
        "license": "Official Alone series logo from Wikimedia Commons; sourced to the HISTORY show page. The live feed is the A+E Networks Alone channel, so the series wordmark matches the branded channel.",
        "license_url": "https://www.history.com/shows/alone",
    },
    "Zainabia Channel": {
        "url": "https://shialivetv.com/shialive/assets/img/t3bepyRDu65zIkcaQB2Q_3_small.png",
        "format": "PNG",
        "page": "https://shialivetv.com/play.php?ch=Al-Kawthar+TV&t=0",
        "license": "Exact Zainabia Channel mark shown in a third-party channel listing; the channel identity is independently corroborated by its official website.",
        "license_url": "https://www.zainabiachannel.co.in/",
    },
    "Cafe Film": {
        "url": "https://raw.githubusercontent.com/shayanline/iptv-iran/main/assets/logos/CafeFilm.ir.png",
        "format": "PNG",
        "page": "https://github.com/shayanline/iptv-iran/blob/main/assets/logos/CafeFilm.ir.png",
        "license": "Public IPTV logo repository; original logo rights belong to broadcaster",
        "license_url": "https://github.com/shayanline/iptv-iran",
    },
    "Persiana Travel": {
        "url": "https://raw.githubusercontent.com/shayanline/iptv-iran/main/assets/logos/PersianaTravel.fr.png",
        "format": "PNG",
        "page": "https://github.com/shayanline/iptv-iran/blob/main/assets/logos/PersianaTravel.fr.png",
        "license": "Public IPTV logo repository; original logo rights belong to broadcaster",
        "license_url": "https://github.com/shayanline/iptv-iran",
    },
    "Aurora Media Flims": {
        "url": "https://i.imgur.com/DVC5w6H.png",
        "format": "PNG",
        "page": "https://github.com/nsdevaraj/48239b1a55a1df69be38126ed1092e13",
        "license": "Public playlist logo reference; original logo rights belong to broadcaster",
        "license_url": "",
    },
    "Radio Bangla Rock": {
        "url": "https://cdn-radiotime-logos.tunein.com/s253847d.png",
        "format": "PNG",
        "page": "https://tunein.com/radio/Radio-Bangla-Rock-s253847/",
        "license": "Station logo served by TuneIn",
        "license_url": "",
    },
    "Tapmad": {
        "url": "https://www.tapmad.com/tapmad-icon.svg",
        "format": "SVG",
        "page": "https://www.tapmad.com/",
        "license": "Tapmad brand asset from its official website",
        "license_url": "",
    },
    "88 Stereo [not 24/7]": {
        "url": "https://cdn-profiles.tunein.com/s10749/images/logod.jpg?t=637503840760000000",
        "format": "JPEG",
        "page": "https://tunein.com/radio/Radio-88-Stereo-887-s10749/",
        "license": "Station logo served by TuneIn",
        "license_url": "",
    },
    "Power Turk": {
        "url": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/turkey/powerturk-tr.png",
        "format": "PNG",
        "page": "https://github.com/tv-logo/tv-logos/blob/main/countries/turkey/powerturk-tr.png",
        "license": "Public TV logo repository; original logo rights belong to broadcaster",
        "license_url": "https://github.com/tv-logo/tv-logos",
    },
    "Dream Music Prime": {
        "url": "https://images.zeno.fm/qCoeGkoZ7uMDvdOso_NCx_7ZVgkxpHVWtvkP9RcAy1k/rs%3Afill%3A152%3A152/q%3A75/g%3Ace%3A0%3A0/aHR0cHM6Ly9wcm94eS56ZW5vLmZtL2NvbnRlbnQvc3RhdGlvbnMvYjg4OGM3NGItNzAzMS00NmM3LTg5MGEtNDg3MzczYjYzMDQ5L2ltYWdlLz91PTE2NzI4MjgxNzMwMDA",
        "format": "",
        "page": "https://zeno.fm/radio/dream-music-prime/",
        "license": "Station logo served by Zeno",
        "license_url": "",
    },
    "Radio Barakah": {
        "url": "https://images.zeno.fm/wSOx1NwNUG6eJNFe2MbZTKU6BvXBDMX5vjbef7G2k_s/rs%3Afill%3A152%3A152/q%3A75/g%3Ace%3A0%3A0/aHR0cHM6Ly9wcm94eS56ZW5vLmZtL2NvbnRlbnQvc3RhdGlvbnMvYWd4emZucGxibTh0YzNSaGRITnlNZ3NTQ2tGMWRHaERiR2xsYm5RWWdJQ3dnNWVUbXdzTUN4SU9VM1JoZEdsdmJsQnliMlpwYkdVWWdJQ3dvX3o0aFFrTW9nRUVlbVZ1YncvaW1hZ2UvP3U9MTY2MTYxNDM0MzAwMA",
        "format": "",
        "page": "https://zeno.fm/radio/radiobarakah/",
        "license": "Station logo served by Zeno",
        "license_url": "",
    },
    "In Sony Sports Ten 3 HD": {
        "url": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/india/sony-ten-3-hd-in.png",
        "format": "PNG",
        "page": "https://github.com/tv-logo/tv-logos/blob/main/countries/india/sony-ten-3-hd-in.png",
        "license": "Channel-specific Sony Sports Ten 3 logo from the TV-logo catalog; broadcaster retains rights",
        "license_url": "https://github.com/tv-logo/tv-logos",
    },
    "Sony Sports Ten 3 HD": {
        "url": "https://www.sonypicturesnetworks.com/images/logos/Sony_Sports_Ten_3_Hindi_HD.png",
        "format": "PNG",
        "page": "https://www.sonypicturesnetworks.com/channels",
        "license": "Sony Pictures Networks India official channel logo; broadcaster retains rights",
        "license_url": "https://www.sonypicturesnetworks.com/",
    },
    "beIN Sports Arabic HD": {
        "url": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/world-middle-east/bein-sports/bein-sports-arabic-mea.png",
        "format": "PNG",
        "page": "https://github.com/tv-logo/tv-logos/blob/main/countries/world-middle-east/bein-sports/bein-sports-arabic-mea.png",
        "license": "Public TV logo repository; original logo rights belong to broadcaster",
        "license_url": "https://github.com/tv-logo/tv-logos",
    },
    "beIN Sports Extra HD": {
        "url": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/international/beinsports/old/horizontal/bein-sports-xtra-hz-int.png",
        "format": "PNG",
        "page": "https://github.com/tv-logo/tv-logos/blob/main/countries/international/beinsports/old/horizontal/bein-sports-xtra-hz-int.png",
        "license": "Public TV logo repository; original logo rights belong to broadcaster",
        "license_url": "https://github.com/tv-logo/tv-logos",
    },
    "TNT Sport 1": {
        "url": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/united-kingdom/hd/tnt-sports-1-hd-uk.png",
        "format": "PNG",
        "page": "https://github.com/tv-logo/tv-logos/blob/main/countries/united-kingdom/hd/tnt-sports-1-hd-uk.png",
        "license": "Public TV logo repository; original logo rights belong to broadcaster",
        "license_url": "https://github.com/tv-logo/tv-logos",
    },
    "Disney Channel Big City Greens": {
        "url": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/international/disney-channel-int.png",
        "format": "PNG",
        "page": "https://github.com/tv-logo/tv-logos/blob/main/countries/international/disney-channel-int.png",
        "license": "Public TV logo repository; original logo rights belong to broadcaster",
        "license_url": "https://github.com/tv-logo/tv-logos",
    },
}

IMAGE_EXTS = {".svg", ".png", ".jpg", ".jpeg", ".webp", ".avif"}
QUALITY_SUFFIX = re.compile(
    r"-(?:1080p|720p|576p|480p|360p|4k|8k|uhd|fhd|hd|sd|hevc|h265|h264)$",
    re.I,
)
ATTR_RE = re.compile(r'([\w-]+)="([^"]*)"')


def parse_extinf(line):
    attrs = dict(ATTR_RE.findall(line))
    label = line.split(",", 1)[-1].strip() if "," in line else ""
    return attrs, label


def set_logo(line, url):
    """Change only the tvg-logo attribute; preserve every other EXTINF byte."""
    if re.search(r'tvg-logo="[^"]*"', line):
        return re.sub(r'tvg-logo="[^"]*"', 'tvg-logo="' + url + '"', line, count=1)
    # Insert before group-title when present, without reordering existing attributes.
    group = re.search(r'\s+group-title="', line)
    if group:
        return line[:group.start()] + ' tvg-logo="' + url + '"' + line[group.start():]
    comma = line.find(",")
    if comma < 0:
        return line
    return line[:comma] + ' tvg-logo="' + url + '"' + line[comma:]


def render_updated_playlist(output_lines, original_text):
    """Replace logo-bearing lines while preserving the playlist's newline style."""
    newline = "\r\n" if original_text.count("\r\n") >= max(1, original_text.count("\n") // 2) else "\n"
    trailing_newlines = len(original_text) - len(original_text.rstrip("\n"))
    body = newline.join(output_lines).rstrip("\r\n")
    return body + (newline * trailing_newlines)


def clean_channel(value):
    value = str(value or "").strip()
    value = re.sub(r"\s*\[[^\]]*\]", " ", value)
    value = re.sub(r"\s*\((?:alt|backup|mirror)\s*#?\s*\d+\)\s*$", "", value, flags=re.I)
    value = re.sub(r"\s+(?:alt|backup|mirror)\s*#?\s*\d+\s*$", "", value, flags=re.I)
    return source.clean_channel_name(value)


def norm_key(value):
    return source.norm(clean_channel(value))


ADULT_BACKUP_CHANNEL_NAMES = (
    "Evil Angel", "Pink Erotic 2", "Pink Erotic 3", "Pink Erotic 5", "Pink Erotic 7", "Pink Erotic 8",
)
ADULT_BACKUP_CHANNEL_KEYS = {norm_key(name) for name in ADULT_BACKUP_CHANNEL_NAMES}

# Use authentic broadcaster artwork first. As explicitly approved, create a clearly
# labelled unofficial fallback only when every exact/local/attributable source fails.
# Review/Backup/discovery queues remain untouched by fallback generation.
ALLOW_GENERATED_FALLBACKS = False


def is_adult_playlist_entry(playlist, group_name, channel_id, channel_key):
    """Identify all adult entries in the International playlist, including mislabeled backup rows."""
    if playlist != "International-Playlist.m3u":
        return False
    group_key = str(group_name or "").strip().casefold()
    id_key = str(channel_id or "").strip().casefold()
    return (
        group_key in {"adult", "xxx", "adult movies"}
        or ".xxx" in id_key
        or str(channel_key or "").casefold() in ADULT_BACKUP_CHANNEL_KEYS
    )


def file_is_valid(path):
    try:
        raw = path.read_bytes()
        if len(raw) < 100:
            return False
        suffix = path.suffix.lower()
        if suffix == ".png":
            return raw.startswith(b"\x89PNG\r\n\x1a\n")
        if suffix in (".jpg", ".jpeg"):
            return raw.startswith(b"\xff\xd8\xff")
        if suffix == ".webp":
            return raw[:4] == b"RIFF" and raw[8:12] == b"WEBP"
        if suffix == ".svg":
            text = raw.decode("utf-8", errors="ignore")
            return "<svg" in text.lower() and "CHANNEL MARK" not in text.upper() and "<script" not in text.lower()
        if suffix == ".avif":
            return b"ftypavif" in raw[:40] or b"ftypavis" in raw[:40]
    except OSError:
        return False
    return False


def asset_key(path):
    stem = path.stem.casefold()
    # All Nvision-branded asset files are prohibited, including "official"
    # and "verified" variants.
    if stem.startswith("nvisionbd-"):
        return ""
    elif stem.startswith("verified-"):
        stem = stem[len("verified-"):]
    stem = re.sub(r"-[a-f0-9]{8,}$", "", stem)
    previous = None
    while stem != previous:
        previous = stem
        stem = QUALITY_SUFFIX.sub("", stem)
    return clean_channel(stem)


def prepare_local_asset(path):
    """Return a stable root-relative filename, copying from /unused if needed."""
    path = Path(path)
    if not path.is_file() or not file_is_valid(path):
        return None
    if path.name.casefold() in BAD_ASSETS or path.name.casefold() in GENERIC_ASSETS:
        return None
    if path.parent == LOGOS:
        return path.name
    destination = LOGOS / path.name
    if destination.exists():
        # Do not overwrite a different file or revive a quarantined root asset.
        digest = hashlib.sha256(path.read_bytes()).hexdigest()[:10]
        destination = LOGOS / f"verified-{path.stem}-{digest}{path.suffix.lower()}"
    if not destination.exists():
        shutil.copyfile(path, destination)
    return destination.name if file_is_valid(destination) else None


def find_local_logo(channel):
    target = norm_key(channel)
    if not target:
        return None

    override = LOCAL_OVERRIDES.get(target)
    if override:
        path = LOGOS / override
        result = prepare_local_asset(path)
        if result:
            return result

    candidates = []
    for path in LOGOS.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in IMAGE_EXTS:
            continue
        lower = path.name.casefold()
        if lower in BAD_ASSETS or lower in GENERIC_ASSETS or lower.startswith("nvisionbd-"):
            continue
        if lower.startswith(("placeholder-", "generated-fallback-", "generic-", "unknown-", "unidentified-")):
            continue
        if "channel mark" in (path.read_text(encoding="utf-8", errors="ignore").casefold()
                              if path.suffix.lower() == ".svg" else ""):
            continue
        if re.search(r"(?:-backup-?\d*|-alt-\d+)(?:\.|$)", lower):
            continue
        key = asset_key(path)
        if key != target:
            continue
        # Exact file first, then clean vector/raster formats and root-level
        # assets before items archived under /unused.
        exact_stem = 0 if source.norm(path.stem) == source.norm(channel) else 1
        quality_penalty = 1 if QUALITY_SUFFIX.search(path.stem) else 0
        unused_penalty = 1 if "unused" in path.parts else 0
        ext_rank = {".svg": 0, ".png": 1, ".webp": 2, ".jpg": 3, ".jpeg": 4, ".avif": 5}.get(path.suffix.lower(), 9)
        candidates.append((exact_stem, quality_penalty, unused_penalty, ext_rank, str(path).casefold(), path))

    if not candidates:
        return None
    candidates.sort(key=lambda item: item[:-1])
    # Avoid arbitrary choice between two different assets with the same exact
    # channel stem. Duplicate bytes are fine; different bytes require review.
    best_rank = candidates[0][:-2]
    tied = [item[-1] for item in candidates if item[:-2] == best_rank]
    distinct = {}
    for path in tied:
        distinct.setdefault(hashlib.sha256(path.read_bytes()).hexdigest(), path)
    if len(distinct) > 1:
        # A channel-name match may be ambiguous (for example, regional feeds).
        return None
    return prepare_local_asset(next(iter(distinct.values())))


def find_mapping(mapping, channel):
    target = norm_key(channel)
    for name, value in mapping.items():
        if norm_key(name) == target:
            return value
    return None


def candidate_for(channel, attrs, iptv_indexes, history_index):
    # Hand-checked exact fallback URLs, after the repository-wide local search.
    item = find_mapping(EXTRA_DIRECT_HINTS, channel)
    if item:
        return dict(item), "Exact external logo asset"

    # Curated exact source hints are the first external step, after a local scan.
    item = find_mapping(source.DIRECT_LOGO_HINTS, channel)
    if item:
        item = dict(item)
        source_name = item.pop("source", "Curated broadcaster/station source")
        return item, source_name

    item = find_mapping(source.TV_LOGO_HINTS, channel)
    if item:
        hint_path = item
        return {
            "url": source.TV_LOGO_BASE + hint_path,
            "format": Path(hint_path).suffix.lstrip(".").upper(),
            "page": source.TV_LOGO_REPO + "/blob/main/" + hint_path,
            "license": "Source repository; license must be checked at source",
            "license_url": "",
        }, "Curated exact channel/region asset"

    page_hint = find_mapping(source.DIRECT_PAGE_HINTS, channel)
    if page_hint:
        page_hints = page_hint if isinstance(page_hint, list) else [page_hint]
        for page_url, allow_og in page_hints:
            try:
                image_url = source.find_page_logo(page_url, allow_og_image=allow_og)
            except (OSError, ValueError, TimeoutError, urllib.error.URLError, json.JSONDecodeError) as exc:
                print(f"Page-logo lookup failed for {channel} at {page_url}: {type(exc).__name__}: {exc}")
                image_url = None
            if image_url:
                return {
                    "url": image_url,
                    "format": "",
                    "page": page_url,
                    "license": "Logo image served on the broadcaster/station page",
                    "license_url": "",
                }, "Broadcaster/station page"

    if iptv_indexes:
        result = source.get_iptv_org_candidate(channel, attrs.get("tvg-id", ""), iptv_indexes)
        if result and result[0].get("url"):
            logo, source_name = result
            return {
                "url": logo.get("url", ""),
                "format": str(logo.get("format") or "").upper(),
                "page": logo.get("url", ""),
                "license": "IPTV-org public logo dataset",
                "license_url": "https://github.com/iptv-org/database",
            }, source_name

    historical = history_index.get(norm_key(channel))
    if historical and Path(urllib.parse.urlparse(historical.get("url", "")).path).name.casefold() not in BAD_ASSETS | GENERIC_ASSETS:
        item = dict(historical)
        source_name = item.pop("source", "Exact-name historical playlist logo mapping")
        return item, source_name

    # The International playlist's Adult group includes many individual names
    # and VOD-style titles, not established TV channels. Do not search Commons
    # for profile pictures or unrelated artwork as substitutes for channel logos.
    group_name = str(attrs.get("group-title", "")).strip().casefold()
    if group_name in {"adult", "xxx", "adult movies"}:
        return None, "No verified TV logo source for this Adult-group entry; Commons lookup skipped"

    try:
        item = source.commons_candidate(channel)
        if item:
            item = dict(item)
            source_name = "Wikimedia Commons exact-logo search"
            return item, source_name
    except (OSError, ValueError, TimeoutError, urllib.error.URLError, json.JSONDecodeError) as exc:
        print(f"Commons-logo lookup failed for {channel}: {type(exc).__name__}: {exc}")
    return None, ""


def detected_image_extension(raw, content_type="", file_format="", source_url=""):
    """Use image signatures when a CDN serves bytes as application/octet-stream."""
    fmt = str(file_format or "").upper()
    if fmt or content_type in {
        "image/svg+xml", "image/png", "image/jpeg", "image/jpg",
        "image/webp", "image/avif",
    }:
        return source.extension_for(content_type, fmt, source_url)
    if raw.startswith(b"\x89PNG\r\n\x1a\n"):
        return ".png"
    if raw.startswith(b"\xff\xd8\xff"):
        return ".jpg"
    if raw[:4] == b"RIFF" and raw[8:12] == b"WEBP":
        return ".webp"
    if b"ftypavif" in raw[:40] or b"ftypavis" in raw[:40]:
        return ".avif"
    if b"<svg" in raw.lstrip()[:500].lower():
        return ".svg"
    return source.extension_for(content_type, fmt, source_url)


def download_exact_asset(channel, candidate, canonical_name=False):
    """Fetch and validate exact source bytes, then store them locally.

    The optional canonical-name mode is used for one-off replacement of explicitly
    labelled fallback assets; it avoids adding a process prefix to normal filenames.
    """
    url = candidate.get("url", "")
    if not url.startswith(("https://", "http://")):
        raise ValueError("source URL is missing or not HTTP(S)")
    raw, mime = source.fetch_bytes(url, timeout=35, max_bytes=5_000_000)
    fmt = str(candidate.get("format") or "").upper()
    if not source.valid_image(raw, mime, fmt):
        raise ValueError("source response is not a valid supported image")
    ext = detected_image_extension(raw, mime, fmt, url)
    slug = source.slug(channel)
    digest = hashlib.sha256(raw).hexdigest()[:20]
    # Keep channel logos repository-local without adding the prohibited
    # Nvision prefix. The digest prevents collisions between regional variants.
    filename = f"{slug}{ext}" if canonical_name else f"{slug}-{digest}{ext}"
    dest = LOGOS / filename
    if dest.exists():
        if hashlib.sha256(dest.read_bytes()).digest() != hashlib.sha256(raw).digest():
            if canonical_name:
                # A canonical filename may already belong to a different regional
                # variant or an older source. Preserve that asset and store the
                # verified new bytes under a content-addressed filename instead
                # of abandoning an otherwise valid exact channel match.
                filename = f"{slug}-{digest}{ext}"
                dest = LOGOS / filename
            else:
                raise ValueError(f"content-addressed logo filename collision: {filename}")
    if not dest.exists():
        dest.write_bytes(raw)
    if not file_is_valid(dest):
        raise ValueError("downloaded image failed local validation")
    return filename


def raw_url(filename):
    """Absolute raw URL written into playlists. Relative logos/ paths are never written."""
    return RAW_BASE + urllib.parse.quote(filename, safe="/")


def absolute_logo_reference(value):
    """Upgrade a repository-relative logos/ reference to the canonical absolute raw URL."""
    if value.startswith("logos/"):
        return raw_url(urllib.parse.unquote(value[len("logos/"):]))
    return value


def is_valid_local_logo_reference(value, allow_generated_fallback=False):
    value = (value or "").strip()
    if not value:
        return False
    basename = Path(urllib.parse.urlparse(value).path).name.casefold()
    blocked_prefixes = ("nvisionbd-", "placeholder-", "generic-", "unknown-", "unidentified-")
    if not allow_generated_fallback:
        blocked_prefixes = blocked_prefixes + ("generated-fallback-",)
    elif basename.startswith("generated-fallback-") and not basename.endswith(".svg"):
        return False
    if basename.startswith(blocked_prefixes) or re.search(r"(?:placeholder|generic-logo)", basename) or basename in BAD_ASSETS or basename in GENERIC_ASSETS:
        return False
    if value.startswith("logos/"):
        candidate = Path(urllib.parse.unquote(value))
    elif value.startswith(RAW_BASE):
        candidate = Path("logos") / urllib.parse.unquote(value[len(RAW_BASE):].split("?", 1)[0].split("#", 1)[0])
    else:
        return False
    try:
        candidate = candidate.resolve()
        candidate.relative_to(LOGOS.resolve())
    except (OSError, RuntimeError, ValueError):
        return False
    return candidate.is_file() and file_is_valid(candidate)


def find_registered_logo(playlist_name, meta, channel):
    try:
        registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8")) if REGISTRY_PATH.exists() else {}
    except (OSError, UnicodeError, json.JSONDecodeError):
        return None
    channel_id = (meta.get("tvg-id") or meta.get("channel-id") or "").strip().casefold()
    options = []
    for key, value in registry.items():
        # Generated fallback art is never treated as a verified source match;
        # keep searching for an authentic logo on later repair runs.
        if value.get("status") == "generated_fallback":
            continue
        parts = key.split("|", 3)
        if len(parts) != 4 or parts[0] != playlist_name:
            continue
        if channel_id and parts[1].strip().casefold() != channel_id:
            continue
        if not is_valid_local_logo_reference(parts[3]):
            continue
        name_score = 0 if norm_key(parts[2]) == norm_key(channel) else 1
        fallback_score = 1 if value.get("status") == "generated_fallback" else 0
        options.append((name_score, fallback_score, parts[3]))
    if not options:
        return None
    options.sort()
    rel = urllib.parse.unquote(options[0][2][len(RAW_BASE):].split("?", 1)[0].split("#", 1)[0])
    return prepare_local_asset(LOGOS / rel)


def make_generated_fallback(channel, category):
    """Create a unique, clearly tracked fallback only after source lookup fails.

    The artwork uses a channel-specific label, a category-aware symbol and a
    deterministic palette. It is not represented as a broadcaster-original logo;
    the provenance manifest identifies it as generated_fallback.
    """
    category = (category or "Channel").strip()
    channel = (channel or "Channel").strip()
    safe_slug = source.slug(channel) or "channel"
    digest = hashlib.sha256((channel + "|" + category).encode("utf-8")).hexdigest()[:8]
    filename = f"generated-fallback-{safe_slug}-{digest}.svg"
    destination = LOGOS / filename
    if destination.is_file() and file_is_valid(destination):
        return filename

    palettes = [
        ("#111827", "#22D3EE", "#F8FAFC"), ("#25113D", "#FB7185", "#FFF7ED"),
        ("#0B2B36", "#FBBF24", "#F8FAFC"), ("#173321", "#A3E635", "#F7FEE7"),
        ("#182044", "#A78BFA", "#F5F3FF"), ("#402018", "#FDBA74", "#FFF7ED"),
        ("#192A48", "#60A5FA", "#EFF6FF"), ("#3B1737", "#F472B6", "#FDF2F8"),
        ("#132F2A", "#34D399", "#ECFDF5"), ("#35220F", "#FDE047", "#FEFCE8"),
        ("#172033", "#F97316", "#FFF7ED"), ("#20223A", "#2DD4BF", "#F0FDFA"),
    ]
    palette_idx = int(digest[:2], 16) % len(palettes)
    background, accent, ink = palettes[palette_idx]
    cat = category.casefold()
    if "radio" in cat or "music" in cat:
        motif = (
            f'<circle cx="91" cy="168" r="9" fill="{accent}"/>'
            f'<path d="M72 149 Q51 168 72 187 M110 149 Q131 168 110 187" fill="none" stroke="{ink}" stroke-width="5" stroke-linecap="round"/>'
            f'<path d="M60 136 Q25 168 60 200 M122 136 Q157 168 122 200" fill="none" stroke="{accent}" stroke-width="4" stroke-linecap="round"/>'
        )
    elif "sport" in cat:
        motif = (
            f'<circle cx="91" cy="168" r="42" fill="none" stroke="{ink}" stroke-width="5"/>'
            f'<path d="M91 146 L110 160 L103 182 L79 182 L72 160 Z M91 146 L91 126 M110 160 L129 153 M103 182 L115 198 M79 182 L67 198 M72 160 L53 153" fill="none" stroke="{accent}" stroke-width="5" stroke-linejoin="round"/>'
        )
    elif "kid" in cat or "cartoon" in channel.casefold() or "jerry" in channel.casefold() or "mr been" in channel.casefold():
        motif = (
            f'<path d="M91 124 L102 151 L131 153 L109 172 L116 200 L91 185 L66 200 L73 172 L51 153 L80 151 Z" fill="{accent}"/>'
            f'<circle cx="54" cy="130" r="6" fill="{ink}"/><circle cx="127" cy="205" r="5" fill="{ink}"/><circle cx="130" cy="127" r="4" fill="{accent}"/>'
        )
    elif "fashion" in cat:
        motif = (
            f'<path d="M91 123 L135 168 L91 213 L47 168 Z" fill="{accent}"/>'
            f'<path d="M91 139 L118 168 L91 197 L64 168 Z" fill="none" stroke="{ink}" stroke-width="4"/>'
        )
    elif "movie" in cat or "cinema" in channel.casefold() or "film" in channel.casefold() or "flix" in channel.casefold():
        motif = (
            f'<rect x="49" y="132" width="84" height="72" rx="10" fill="none" stroke="{ink}" stroke-width="5"/>'
            f'<path d="M50 150 H132 M50 186 H132 M70 133 V149 M93 133 V149 M116 133 V149 M70 187 V203 M93 187 V203 M116 187 V203" stroke="{accent}" stroke-width="5"/>'
        )
    else:
        motif = (
            f'<circle cx="91" cy="168" r="43" fill="none" stroke="{ink}" stroke-width="5"/>'
            f'<path d="M80 143 L111 168 L80 193 Z" fill="{accent}"/>'
            f'<path d="M55 120 Q91 98 127 120 M55 216 Q91 238 127 216" fill="none" stroke="{accent}" stroke-width="4" stroke-linecap="round"/>'
        )

    words = channel.split()
    wrapped, current = [], ""
    for word in words:
        candidate = (current + " " + word).strip()
        if current and len(candidate) > 17:
            wrapped.append(current)
            current = word
        else:
            current = candidate
    if current:
        wrapped.append(current)
    if len(wrapped) > 3:
        wrapped = wrapped[:2] + [" ".join(wrapped[2:])]
    longest = max((len(x) for x in wrapped), default=8)
    font_size = 31 if longest <= 13 else 27 if longest <= 17 else 23
    start_y = 168 - (len(wrapped) - 1) * 18
    text_lines = []
    for i, line in enumerate(wrapped):
        text_lines.append(
            f'<text x="181" y="{start_y + i * 36}" font-family="Arial,Helvetica,sans-serif" '
            f'font-size="{font_size}" font-weight="700" fill="{ink}">{html.escape(line)}</text>'
        )
    category_label = html.escape(category.upper())
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" width="600" height="340" viewBox="0 0 600 340">'
        f'<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">'
        f'<stop offset="0" stop-color="{background}"/><stop offset="1" stop-color="#0A0F1C"/></linearGradient></defs>'
        '<rect width="600" height="340" rx="30" fill="url(#bg)"/>'
        f'<circle cx="555" cy="38" r="126" fill="{accent}" opacity=".10"/>'
        f'<path d="M0 284 L600 177 L600 340 L0 340 Z" fill="{accent}" opacity=".08"/>'
        f'<rect x="16" y="16" width="568" height="308" rx="24" fill="none" stroke="{accent}" stroke-width="2" opacity=".7"/>'
        f'<rect x="34" y="32" width="116" height="276" rx="22" fill="{accent}" opacity=".12"/>'
        f'<g>{motif}</g>'
        + "".join(text_lines) +
        f'<rect x="181" y="235" width="7" height="31" rx="3" fill="{accent}"/>'
        f'<text x="202" y="255" font-family="Arial,Helvetica,sans-serif" font-size="15" '
        f'font-weight="700" letter-spacing="2" fill="{accent}">{category_label}</text>'
        f'<text x="566" y="300" text-anchor="end" font-family="Arial,Helvetica,sans-serif" '
        f'font-size="10" font-weight="600" letter-spacing="1.4" fill="{ink}" opacity=".55">UNOFFICIAL FALLBACK ART</text>'
        '</svg>'
    )
    destination.write_text(svg, encoding="utf-8")
    return filename if file_is_valid(destination) else None


def replace_orphaned_generated_fallback_assets(iptv_indexes, history_index):
    """Replace orphaned generated artwork with exact originals; retire unresolved fakes."""
    active_paths = set()
    for playlist in PLAYLISTS:
        path = Path(playlist)
        if not path.is_file():
            continue
        for line in path.read_text(encoding="utf-8-sig").splitlines():
            if line.startswith("#EXTINF:"):
                attrs, _ = parse_extinf(line)
                logo = (attrs.get("tvg-logo") or "").strip()
                if logo.startswith("logos/"):
                    active_paths.add(Path(urllib.parse.unquote(logo)).as_posix())
                elif logo.startswith(RAW_BASE):
                    active_paths.add((Path("logos") / urllib.parse.unquote(logo[len(RAW_BASE):].split("?", 1)[0].split("#", 1)[0])).as_posix())
    report = [
        "# Generated Fallback Asset Replacement", "",
        "Orphaned fabricated logos were checked against exact local assets and source-attributed sources.",
        "Unresolved fabricated artwork was retired rather than relabelled as an original.", "",
        "| Former fallback | Action | Original asset / reason |",
        "|---|---|---|",
    ]
    files = sorted((p for p in LOGOS.rglob("*") if p.is_file() and p.name.casefold().startswith("generated-fallback-")), key=lambda p:p.as_posix().casefold())
    replaced = unresolved = retained = 0
    retired = set()
    for path in files:
        rel = path.as_posix()
        if rel in active_paths:
            retained += 1
            report.append("| " + rel + " | Retained | Still referenced by playlist |")
            continue
        slug = path.stem[len("generated-fallback-"): ]
        slug = re.sub(r"-[a-f0-9]{8,}$", "", slug, flags=re.I)
        slug = re.sub(r"-converted$", "", slug, flags=re.I)
        channel = re.sub(r"[-_]+", " ", slug).strip()
        original = None
        reason = ""
        try:
            original = find_local_logo(channel)
            if original:
                reason = "Exact channel-name match in repository"
        except Exception as exc:
            reason = "Local lookup failed: " + str(exc)[:120]
        if not original:
            try:
                candidate, source_name = candidate_for(channel, {}, iptv_indexes, history_index)
                if candidate:
                    original = download_exact_asset(channel, candidate, canonical_name=True)
                    reason = source_name + ": " + candidate.get("page", candidate.get("url", ""))
            except Exception as exc:
                reason = "Source unavailable or invalid: " + str(exc)[:140]
        if original and file_is_valid(LOGOS / original):
            path.unlink()
            replaced += 1
            retired.add(rel)
            report.append("| " + rel + " | Replaced | logos/" + original + " — " + reason.replace("|", "/") + " |")
        else:
            path.unlink()
            unresolved += 1
            retired.add(rel)
            report.append("| " + rel + " | Fabricated artwork removed | No exact authentic original verified; " + (reason or "no matching source") + " |")
    report += ["", "## Summary", "",
        "- Fallback files found: **" + str(len(files)) + "**",
        "- Replaced with original assets: **" + str(replaced) + "**",
        "- Removed because no authentic original was verified: **" + str(unresolved) + "**",
        "- Retained because still referenced: **" + str(retained) + "**", "",
        "Playlist stream URLs and channel metadata are not changed by this asset-only cleanup.", ""]
    Path("reports").mkdir(parents=True, exist_ok=True)
    Path("reports/generated-fallback-replacement.md").write_text("\n".join(report), encoding="utf-8")
    print(json.dumps({"fallback_files":len(files),"replaced":replaced,"removed_unverified":unresolved,"retained_active":retained}))
    return retired

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--fallback-only",
        action="store_true",
        help="repair only active explicitly named generated-fallback logo references",
    )
    args = parser.parse_args()
    LOGOS.mkdir(parents=True, exist_ok=True)
    try:
        iptv_indexes = source.load_iptv_org_indexes()
        iptv_status = "loaded"
    except Exception as exc:
        iptv_indexes = None
        iptv_status = "unavailable: " + str(exc)[:140]
    try:
        history_index = source.load_historical_logo_index()
        # Keep only history entries with non-quarantined basenames.
        history_index = {
            key: value for key, value in history_index.items()
            if (
                Path(urllib.parse.urlparse(value.get("url", "")).path).name.casefold()
                not in BAD_ASSETS | GENERIC_ASSETS
                and not Path(urllib.parse.urlparse(value.get("url", "")).path).name.casefold().startswith("nvisionbd-")
            )
        }
        history_status = f"loaded {len(history_index)} historical name mappings"
    except Exception as exc:
        history_index = {}
        history_status = "unavailable: " + str(exc)[:140]

    fixes_cache = {}
    report_rows = []
    registry_updates = {}
    summary = {}
    for playlist in PLAYLISTS:
        path = Path(playlist)
        if not path.is_file():
            summary[playlist] = {"entries": 0, "changed": 0, "missing_after": 0, "flagged_after": 0, "unresolved": 0}
            continue
        with path.open("r", encoding="utf-8", newline="") as stream:
            original = stream.read()
        lines = original.splitlines()
        changed = unresolved = entries = fallback_count = adult_ignored = 0
        output = []
        for line_number, line in enumerate(lines, start=1):
            if not line.startswith("#EXTINF:"):
                output.append(line)
                continue
            entries += 1
            attrs, label = parse_extinf(line)
            channel = label or attrs.get("tvg-name", "")
            key = norm_key(channel)
            current = (attrs.get("tvg-logo") or "").strip()
            basename = Path(urllib.parse.urlparse(current).path).name.casefold() if current else ""
            group_name = (attrs.get("group-title") or "").strip().casefold()
            channel_id = (attrs.get("tvg-id") or attrs.get("channel-id") or "").strip().casefold()
            # The user explicitly exempts Adult entries from logo repair. The
            # custom.xxx identity also marks adult material when it sits in Backups.
            # Preserve these rows byte-for-byte, including their logo attributes.
            is_adult_entry = is_adult_playlist_entry(playlist, group_name, channel_id, key)
            if is_adult_entry:
                adult_ignored += 1
                output.append(line)
                continue
            # Existing repository-relative references are upgraded in place to the
            # absolute raw URL when the asset they name is still valid.
            if current.startswith("logos/") and is_valid_local_logo_reference(current):
                output.append(set_logo(line, absolute_logo_reference(current)))
                continue
            missing = not current
            broken = not is_valid_local_logo_reference(current)
            is_review_entry = group_name in {"backup", "review", "not playing", "not playing...", "not playing…", "new channels", "new backups", "new backup"}
            is_generated_fallback = basename.startswith("generated-fallback-")
            if args.fallback_only and (not is_generated_fallback or is_review_entry):
                output.append(line)
                continue
            forced_logo = FORCED_CHANNEL_LOGOS.get(key)
            forced_wrong = bool(forced_logo and basename != forced_logo.casefold())
            # A fallback is disclosed as unofficial, but active fallbacks now enter an
            # exact-source replacement attempt. Review queues remain manually managed.
            flagged = (
                broken or basename in BAD_ASSETS or basename in GENERIC_ASSETS
                or bool(re.search(r"(?:placeholder|generic-logo)", basename))
                or forced_wrong or (is_generated_fallback and not is_review_entry)
            )
            if not (missing or flagged):
                output.append(line)
                continue

            new_file = prepare_local_asset(LOGOS / forced_logo) if forced_logo else fixes_cache.get(key)
            source_name = "Forced verified local logo" if forced_logo and new_file else "Reused repaired exact-name logo"
            source_page = ""
            license_name = ""
            license_url = ""
            candidate_metadata = None
            generated_fallback = False

            if not new_file:
                try:
                    new_file = find_registered_logo(playlist, attrs, channel)
                    if new_file:
                        source_name = "Local asset from existing provenance registry"
                        source_page = "https://github.com/saeidrahmanbd/BDIX-IPTV/tree/main/logos"
                except Exception as exc:
                    report_rows.append((playlist, line_number, channel, basename, "", "local registry lookup", "", "", "Registry lookup failed: " + str(exc)[:120]))

            if not new_file:
                try:
                    new_file = find_local_logo(channel)
                    if new_file:
                        source_name = "Exact clean asset found in repository /logos (including /unused)"
                        source_page = "https://github.com/saeidrahmanbd/BDIX-IPTV/tree/main/logos"
                except Exception as exc:
                    report_rows.append((playlist, line_number, channel, basename, "", "local lookup", "", "", "Local asset lookup failed: " + str(exc)[:120]))

            if not new_file:
                try:
                    candidate, source_name = candidate_for(channel, attrs, iptv_indexes, history_index)
                    if candidate:
                        source_page = candidate.get("page", "")
                        license_name = candidate.get("license", "")
                        license_url = candidate.get("license_url", "")
                        new_file = download_exact_asset(channel, candidate, canonical_name=args.fallback_only)
                        # Provenance metadata is attached only once these exact bytes
                        # were downloaded and validated. If the download raises, the
                        # candidate must not survive to describe a fallback asset.
                        candidate_metadata = dict(candidate)
                except Exception as exc:
                    report_rows.append((playlist, line_number, channel, basename, "", source_name or "external lookup", "", "", "Download/validation failed: " + str(exc)[:150]))
                    new_file = None

            # Do not fabricate artwork when authentic source lookup fails. Unresolved
            # entries remain without a logo and are listed for manual verification.
            if ALLOW_GENERATED_FALLBACKS and not new_file and not is_adult_entry and not is_review_entry:
                fallback_file = make_generated_fallback(channel, attrs.get("group-title", ""))
                if fallback_file:
                    new_file = fallback_file
                    generated_fallback = True
                    fallback_count += 1
                    source_name = "Generated fallback artwork (unofficial; no exact logo source found)"
                    source_page = ""
                    license_name = "Unofficial generated fallback art; not a broadcaster-original logo"
                    license_url = ""

            # A source page can expose the same known placeholder image under
            # a fresh download. Validate the final repository-local reference,
            # not only its HTTP source metadata; if it is still quarantined,
            # discard it and remove the unsafe old reference below.
            if new_file and not is_valid_local_logo_reference(raw_url(new_file), allow_generated_fallback=generated_fallback):
                new_file = None

            if new_file:
                fixes_cache[key] = new_file
                logo_reference = raw_url(new_file)
                line = set_logo(line, logo_reference)
                channel_id = (attrs.get("tvg-id") or attrs.get("channel-id") or "").strip()
                # Fallback status always wins over candidate metadata, and candidate
                # metadata only exists for a successfully downloaded asset.
                registry_record = logo_provenance.build_registry_record(
                    generated_fallback=generated_fallback,
                    candidate=candidate_metadata,
                    source_name=source_name,
                )
                if registry_record:
                    registry_updates[logo_provenance.canonical_key(f"{playlist}|{channel_id}|{channel}|{logo_reference}")] = registry_record
                changed += 1
                report_rows.append((playlist, line_number, channel, basename, new_file, source_name, source_page, license_name + ((" — " + license_url) if license_url else ""), "replaced"))
            else:
                # Do not invent substitute artwork. Remove unsafe references when
                # no genuine replacement exists, and leave the channel for review.
                unresolved += 1
                original_line = line
                if current and (
                    not is_valid_local_logo_reference(current)
                    or basename in BAD_ASSETS | GENERIC_ASSETS
                    or basename.startswith(("placeholder-", "generated-fallback-", "generic-", "unknown-", "unidentified-", "nvisionbd-"))
                    or bool(re.search(r"(?:placeholder|generic-logo)", basename))
                ):
                    line = re.sub(r'\s+tvg-logo="[^"]*"', "", line, count=1)
                    if line != original_line:
                        changed += 1
                result_note = "Unsafe logo reference removed" if line != original_line else "No exact authentic logo source; logo left missing for manual review"
                report_rows.append((playlist, line_number, channel, basename, "", "none", "", "", result_note))
            output.append(line)

        new_text = render_updated_playlist(output, original)
        if new_text != original:
            path.write_text(new_text, encoding="utf-8")
        # Confirm reference counts against the resulting file.
        missing_after = flagged_after = 0
        for item in output:
            if not item.startswith("#EXTINF:"):
                continue
            meta, meta_label = parse_extinf(item)
            meta_group = (meta.get("group-title") or "").strip().casefold()
            meta_id = (meta.get("tvg-id") or meta.get("channel-id") or "").strip().casefold()
            meta_key = norm_key(meta_label or meta.get("tvg-name", ""))
            if is_adult_playlist_entry(playlist, meta_group, meta_id, meta_key):
                continue
            logo = (meta.get("tvg-logo") or "").strip()
            name = Path(urllib.parse.urlparse(logo).path).name.casefold() if logo else ""
            allow_fallback = bool(name.startswith("generated-fallback-") and (LOGOS / urllib.parse.unquote(name)).is_file())
            if not logo or not is_valid_local_logo_reference(logo, allow_generated_fallback=allow_fallback):
                missing_after += 1
            if (
                name in BAD_ASSETS or name in GENERIC_ASSETS
                or name.startswith(("nvisionbd-", "placeholder-", "generated-fallback-", "generic-", "unknown-", "unidentified-"))
                or bool(re.search(r"(?:placeholder|generic-logo)", name))
            ):
                flagged_after += 1
        summary[playlist] = {
            "entries": entries, "changed": changed, "missing_after": missing_after,
            "flagged_after": flagged_after, "generated_fallbacks": fallback_count,
            "unresolved": unresolved, "adult_entries_skipped": adult_ignored,
        }

    try:
        registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8")) if REGISTRY_PATH.exists() else {}
    except (OSError, UnicodeError, json.JSONDecodeError):
        registry = {}
    retired_fallback_assets = replace_orphaned_generated_fallback_assets(iptv_indexes, history_index)
    registry_before = json.dumps(registry, ensure_ascii=False, indent=2) + "\n"
    registry.update(registry_updates)
    # Heal any stale fallback record (wrong status, a source URL, or missing
    # disclosure wording) so it cannot contradict the asset it describes. This runs
    # on every execution, so a legacy record is repaired even when nothing else changed.
    registry, healed_fallback_keys = logo_provenance.normalize_registry(registry)
    if retired_fallback_assets:
        registry = {key: value for key, value in registry.items() if not (
            value.get("status") == "generated_fallback"
            and Path(urllib.parse.urlparse(key.split("|", 3)[-1]).path).name in {Path(p).name for p in retired_fallback_assets}
        )}
    if healed_fallback_keys:
        print(f"Normalized {len(healed_fallback_keys)} generated-fallback registry record(s).")
    registry_after = json.dumps(registry, ensure_ascii=False, indent=2) + "\n"
    if (registry_updates or healed_fallback_keys) and registry_after != registry_before:
        REGISTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
        REGISTRY_PATH.write_text(registry_after, encoding="utf-8")

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    report = [
        "# IPTV Playlist Logo Repair Results", "",
        f"Run time: **{now}**  ",
        f"Repository-first local logo search completed before external lookup.  ",
        f"IPTV-org data: {iptv_status}  ",
        f"Historical mapping index: {history_status}", "",
        "## Results by playlist", "",
        "| Playlist | Entries | References changed | Generated fallbacks | Missing after (Adult excluded) | Adult entries skipped | Known generic/contaminated refs after | Unresolved repair targets |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for name, data in summary.items():
        report.append(f"| {name} | {data['entries']} | {data['changed']} | {data['generated_fallbacks']} | {data['missing_after']} | {data.get('adult_entries_skipped', 0)} | {data['flagged_after']} | {data['unresolved']} |")
    report += ["", "## Repair log", "",
               "| Playlist | Line | Channel | Previous logo | Replacement | Source | Attribution | Result |",
               "|---|---:|---|---|---|---|---|---|"]
    for playlist, line_number, channel, previous, new_file, source_name, source_page, attribution, result in report_rows:
        src = f"[{source_name}]({source_page})" if source_page else source_name
        report.append(
            f"| {playlist} | {line_number} | {channel.replace('|', '/')} | {previous or '(missing)'} | "
            f"{new_file or '(none)'} | {src.replace('|', '/')} | {attribution.replace('|', '/')} | {result} |"
        )
    report += ["", "## Quality rule", "",
               "- Exact, clean local assets are searched first; then curated, source-attributed external logo URLs are downloaded and validated.",
               "- If no exact authentic asset is available, leave the logo unresolved for manual verification; never generate substitute artwork.",
               "- Contaminated, mismatched, placeholder, generic, and generated-fallback assets are never assigned to tvg-logo.",
               "- Nvision-branded filenames are prohibited in all maintained playlists.",
               "- Original playlist entries, channel metadata, categories, and stream URLs are preserved.", ""]
    REPORT.write_text("\n".join(report), encoding="utf-8")
    print(json.dumps({"summary": summary, "iptv_org": iptv_status, "history": history_status}, ensure_ascii=False))


if __name__ == "__main__":
    main()
