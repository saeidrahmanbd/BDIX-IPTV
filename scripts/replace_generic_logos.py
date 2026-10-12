#!/usr/bin/env python3
"""Replace generic NVisionBD CHANNEL MARK assets with source-verified channel logos.

Resolution order:
1. Reuse a matching, non-generic logo already in /logos.
2. Use a unique exact-name / exact-ID match from the IPTV-org public logo dataset.
3. Use a unique, explicitly titled and licensed logo file from Wikimedia Commons.
Anything ambiguous remains untouched and is reported for manual review.
"""
import json
import html
import shutil
import re
import time
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode, urlparse, unquote, urljoin
from urllib.request import Request, urlopen

PLAYLIST = Path("NVisionBD-Playlist.m3u")
LOGOS = Path("logos")
REPORT = Path("reports/generic-logo-replacement-results.md")
AUDIT = Path("reports/generic-logo-audit.md")
RAW_BASE = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/"
UA = "BDIX-IPTV-logo-audit/2.0 (https://github.com/saeidrahmanbd/BDIX-IPTV)"
IPTV_CHANNELS_URL = "https://iptv-org.github.io/api/channels.json"
IPTV_LOGOS_URL = "https://iptv-org.github.io/api/logos.json"

# These three lookalike matches from the prior pass were not the right logo.
REJECTED_PREVIOUS_MATCHES = {
    "nvisionbd-action-24.jpg": ("nvisionbd-action-24.svg", "Prior match was an event photo, not the channel logo"),
    "nvisionbd-digital-fashion.png": ("nvisionbd-digital-fashion.svg", "Prior match was a different business logo"),
    "nvisionbd-sport-2.jpg": ("nvisionbd-sport-2.svg", "Prior match was a different regional sports channel"),
    "nvisionbd-official-digital-fashion.png": ("nvisionbd-digital-fashion.svg", "Commons result was a business agency, not this TV channel"),
    "nvisionbd-official-sport-2.jpg": ("nvisionbd-sport-2.svg", "Commons result was Polsat Sport 2, a different service"),
    "nvisionbd-official-the-q.png": ("nvisionbd-the-q.svg", "Commons result was a standalone Q mark with ambiguous channel identity"),
}

# Repository-first policy: scan every eligible file in /logos before any external lookup.
# Known exact local assets. Use only if the target file exists and is non-generic.
LOCAL_LOGO_FILES = {
    "Zee Cinema HD": "zee-cinema.png",
    "Zee TV HD": "zee-tv.png",
    "Zee Cafe HD": "zee-cafe.png",
    "Zing": "zing.png",
    "Zoom Music": "zoom-music.png",
    "Wild Earth": "wildearth.png",
    "Cowboy Movie Channel": "cowboy-movie-channel.png",
    "NBC Sports": "nbc-sports.png",
    "Talk Sport": "talksport.png",
    "Ducktv": "duck-tv.png",
    "Afrobeats": "afrobeats.png",
    "24/7 Batul The Great": "bantul-the-great-35f9777f.png",
    "Ktv Sports Plus": "ktv-sport-plus.png",
    "Spondon Radio": "spondon.png",
    "Sony Cine": "cine-sony-720p-c27cf4bb09.png",
    "Oman Sports": "oman-sports-tv.png",
    "Wow Kids": "wow-kidz.png",
    "Wild Life": "wildearth.png",
}

# Exact channel/region matches from the public tv-logo/tv-logos collection.
# Use only where the playlist name or its known channel identity identifies region.
TV_LOGO_HINTS = {
    "Boomerang": "countries/united-states/boomerang-us.png",
    "Boomerang UK": "countries/united-kingdom/boomerang-uk.png",
    "Bt Sports 2": "countries/united-kingdom/hd/bt-sport-2-hd-uk.png",
    "Comedy Central": "countries/united-states/comedy-central-us.png",
    "Cosmote Sports 1": "countries/greece/cosmote-sport-1-gr.png",
    "Cosmote Sports 4": "countries/greece/cosmote-sport-4-gr.png",
    "Digi Sport 1": "countries/romania/digi-sport-1-ro.png",
    "Digi Sport 2": "countries/romania/digi-sport-2-ro.png",
    "Epic": "countries/india/epic-in.png",
    "Fashion TV HD": "countries/international/fashion-tv-int.png",
    "FX TV": "countries/united-states/fx-us.png",
    "Golf Channel": "countries/united-states/nbc-golf-channel-us.png",
    "Laff TV": "countries/united-states/laff-us.png",
    "Laligatv": "countries/nordic/norway/laliga-tv-no.png",
    "Magenta Sports 2": "countries/austria/magenta-sport-2-at.png",
    "Movie Sphere": "countries/united-states/movie-sphere-us.png",
    "Movie Sphere Au": "countries/united-states/movie-sphere-us.png",
    "My Time Movie": "misc/vod/my-time-movie-network-vod.png",
    "Premier Sports 1": "countries/united-kingdom/premier-sports-1-uk.png",
    "Sports Grid": "misc/vod/sports-grid-vod-us.png",
    "The Q": "countries/india/the-q-in.png",
    "Tsn Aq1": "countries/canada/tsn-1-ca.png",
    "UK TNT Sports 1 HD": "countries/united-kingdom/hd/tnt-sports-1-hd-uk.png",
    "UK TNT Sports 2 HD": "countries/united-kingdom/hd/tnt-sports-2-hd-uk.png",
    "UK TNT Sports 3 HD": "countries/united-kingdom/hd/tnt-sports-3-hd-uk.png",
    "UK TNT Sports 4 HD": "countries/united-kingdom/hd/tnt-sports-4-hd-uk.png",
    "US Sky Sports Main Event": "countries/united-kingdom/hd/sky-sports-main-event-hd-uk.png",
    "US Sky Sports Premier League": "countries/united-kingdom/hd/sky-sports-premier-league-hd-uk.png",
    "US Willow By Cricbuzz": "countries/united-states/willow-us.png",
    "Ziggo Sport Live": "countries/netherlands/ziggo-sport-nl.png",
}
TV_LOGO_BASE = "https://raw.githubusercontent.com/tv-logo/tv-logos/main/"
TV_LOGO_REPO = "https://github.com/tv-logo/tv-logos"

# Official station pages used only as a last-mile image lookup. The page parser
# accepts explicit logo-marked <img> elements; OG images are allowed only for
# station profile pages where they are commonly the station avatar.
DIRECT_PAGE_HINTS = {
    "Global Panjab": ("https://globalpunjabtv.com/", True),
    "Nick Bangla": ("https://www.nick.com.bd/", False),
    "10 TV": ("https://10tv.in/", True),
    "88 Stereo [not 24/7]": ("https://www.88stereo.com/", False),
    "Radio Adamya": ("https://zeno.fm/radio/radio-adamya/", True),
    "Radio Barakah": ("https://zeno.fm/radio/radio-barakah/", True),
    "Radio Zenith FM": ("https://zeno.fm/radio/radio-zenith-fm/", True),
    "Dream Music Prime": ("https://zeno.fm/radio/dream-music-prime/", True),
    "Wifm 100.9": ("https://www.wifmradio.com/", False),
    "Tapmad": ("https://www.tapmad.com/", False),
}


def find_page_logo(page_url, allow_og_image=False):
    """Find a logo image URL on an official station page without copying page art."""
    raw, mime = fetch_bytes(page_url, timeout=20, max_bytes=2_000_000)
    if "html" not in mime and not raw.lstrip().startswith((b"<!DOCTYPE html", b"<html")):
        return None
    source = raw.decode("utf-8", errors="ignore")
    img_candidates = []
    for tag in re.findall(r"<img\b[^>]*>", source, flags=re.I):
        attrs = {
            key.lower(): html.unescape(value)
            for key, _, value in re.findall(r"""([\w:-]+)\s*=\s*["']([^"']*)["']""", tag)
        }
        src = attrs.get("src") or attrs.get("data-src") or ""
        if not src or src.startswith(("data:", "blob:")):
            continue
        descriptor = " ".join([attrs.get("alt", ""), attrs.get("title", ""), attrs.get("class", ""), attrs.get("id", ""), src]).lower()
        score = sum(2 for word in ("logo", "brand", "station") if word in descriptor)
        if score:
            img_candidates.append((score, urljoin(page_url, src)))
    if img_candidates:
        img_candidates.sort(key=lambda item: item[0], reverse=True)
        return img_candidates[0][1]
    if allow_og_image:
        meta_tags = re.findall(r"<meta\b[^>]*>", source, flags=re.I)
        for tag in meta_tags:
            attrs = {
                key.lower(): html.unescape(value)
                for key, _, value in re.findall(r"""([\w:-]+)\s*=\s*["']([^"']*)["']""", tag)
            }
            property_name = (attrs.get("property") or attrs.get("name") or "").lower()
            image_url = attrs.get("content") or ""
            if property_name in ("og:image", "twitter:image") and image_url.startswith(("http://", "https://")):
                return image_url
    return None

# Exact station assets discovered on broadcaster/streaming-service pages.
DIRECT_LOGO_HINTS = {
    "BTV Sangsad": {
        "url": "https://i.imgur.com/jkouxLg.png",
        "format": "PNG",
        "page": "https://iptv-org.github.io/channels/bd/SangsadTV",
        "source": "IPTV-org Sangsad TV channel page",
        "license": "Station logo sourced from IPTV-org channel listing",
        "license_url": "",
    },
    "92.8 FM Radio Bhumi": {
        "url": "https://cdn-radiotime-logos.tunein.com/s260643g.png",
        "format": "PNG",
        "page": "https://tunein.com/radio/Radio-Bhumi-928-s260643/",
        "source": "TuneIn station logo",
        "license": "Station logo served by TuneIn",
        "license_url": "",
    },
    "Radio Bhumi 92.80 FM": {
        "url": "https://cdn-radiotime-logos.tunein.com/s260643g.png",
        "format": "PNG",
        "page": "https://tunein.com/radio/Radio-Bhumi-928-s260643/",
        "source": "TuneIn station logo",
        "license": "Station logo served by TuneIn",
        "license_url": "",
    },
    "Radio Capital FM 94.8": {
        "url": "https://static2.mytuner.mobi/media/tvos_radios/t5fqtbwxajbg.png",
        "format": "PNG",
        "page": "https://mytuner-radio.com/radio/radio-capital-fm-429052/",
        "source": "myTuner station logo",
        "license": "Station logo served by myTuner",
        "license_url": "",
    },
    "Bangla Radio": {
        "url": "https://cdn.instant.audio/images/logos/radio-bd-com/bangla-95.png",
        "format": "PNG",
        "page": "https://radio-bd.com/bangla-95/",
        "source": "Radio-bd.com station logo",
        "license": "Station logo served by Radio-bd.com",
        "license_url": "",
    },
    "Radio Shadhin - 92.4 FM": {
        "url": "https://static2.mytuner.mobi/media/tvos_radios/bpa8gzkd9hsp.jpg",
        "format": "JPEG",
        "page": "https://mytuner-radio.com/radio/radio-shadhin-429049/",
        "source": "myTuner station logo",
        "license": "Station logo served by myTuner",
        "license_url": "",
    },
    "Radio Shadin": {
        "url": "https://static2.mytuner.mobi/media/tvos_radios/bpa8gzkd9hsp.jpg",
        "format": "JPEG",
        "page": "https://mytuner-radio.com/radio/radio-shadhin-429049/",
        "source": "myTuner station logo",
        "license": "Station logo served by myTuner",
        "license_url": "",
    },
    "Radio Din Raat 93.6 FM": {
        "url": "https://static2.mytuner.mobi/media/tvos_radios/9vhbuhzmucws.jpg",
        "format": "JPEG",
        "page": "https://mytuner-radio.com/radio/radio-din-raat-468346/",
        "source": "myTuner station logo",
        "license": "Station logo served by myTuner",
        "license_url": "",
    },
    "Radio Mahananda - 98.8": {
        "url": "https://static2.mytuner.mobi/media/tvos_radios/658/radio-mahananda-988-fm.717ad31a.png",
        "format": "PNG",
        "page": "https://mytuner-radio.com/radio/radio-mahananda-988-fm-491658/",
        "source": "myTuner station logo",
        "license": "Station logo served by myTuner",
        "license_url": "",
    },
    "Peoples Radio": {
        "url": "https://static2.mytuner.mobi/media/tvos_radios/vsn68ujrhaxj.jpg",
        "format": "JPEG",
        "page": "https://mytuner-radio.com/radio/peoples-radio-916-fm-429045/",
        "source": "myTuner station logo",
        "license": "Station logo served by myTuner",
        "license_url": "",
    },
    "Radio Bushra": {
        "url": "https://cdn.instant.audio/images/logos/radio-bd-com/bushra.png",
        "format": "PNG",
        "page": "https://radio-bd.com/bushra/",
        "source": "Radio-bd.com station logo",
        "license": "Station logo served by Radio-bd.com",
        "license_url": "",
    },
    "Radio Padma – 99.2 FM": {
        "url": "https://i1.sndcdn.com/avatars-yIzlzJLEhaHQVxe9-lbOLvA-t1080x1080.jpg",
        "format": "JPEG",
        "page": "https://soundcloud.com/radiopadma",
        "source": "Radio Padma SoundCloud profile",
        "license": "Station artwork served by SoundCloud",
        "license_url": "",
    },
    "Radio Tangail": {
        "url": "https://zenoimages.s3.us-west-001.backblazeb2.com/0932bfac-ea04-4f30-9e3e-e268bc9462e8/images/logo",
        "format": "PNG",
        "page": "https://zeno.fm/radio/radiotangail/",
        "source": "Radio Tangail Zeno station page",
        "license": "Station logo served by Zeno",
        "license_url": "",
    },
    "My 90s Bengali Online": {
        "url": "https://proxy.zeno.fm/content/stations/agxzfnplbm8tc3RhdHNyMgsSCkF1dGhDbGllbnQYgIDQwZOSmAoMCxIOU3RhdGlvblByb2ZpbGUYgICwjMSC4AgMogEEemVubw/image/?u=1700245114000",
        "format": "",
        "page": "https://zeno.fm/radio/mybangla/",
        "source": "My Bangla Zeno station page",
        "license": "Station artwork served by Zeno",
        "license_url": "",
    },
    "Afra Film": {
        "url": "https://afratv.com/images/Logo4.png",
        "format": "PNG",
        "page": "https://afratv.com/AFRAFILM.html",
        "source": "AFRA Film official page",
        "license": "Broadcaster logo served on its official website",
        "license_url": "",
    },
    "Amar Ujala": {
        "url": "https://commons.wikimedia.org/wiki/Special:FilePath/Amar_Ujala_Logo.png",
        "format": "PNG",
        "page": "https://commons.wikimedia.org/wiki/File:Amar_Ujala_Logo.png",
        "source": "Wikimedia Commons",
        "license": "Public domain text logo",
        "license_url": "https://creativecommons.org/publicdomain/zero/1.0/",
    },
    "News 18 Assam": {
        "url": "https://images.seeklogo.com/logo-png/60/1/news18-assam-logo-png_seeklogo-606384.png",
        "format": "PNG",
        "page": "https://seeklogo.com/vector-logo/606384/news18-assam",
        "source": "Seeklogo News18 Assam brand listing",
        "license": "Source listing; reuse rights not specified",
        "license_url": "",
    },
    "CTVN AKD Plus": {
        "url": "https://pbs.twimg.com/profile_images/1150729632125091840/G4nLPu2__400x400.jpg",
        "format": "JPEG",
        "page": "https://x.com/CalcuttaNetwork",
        "source": "Calcutta Television Network profile image",
        "license": "Channel logo used as profile artwork",
        "license_url": "",
    },
    "Madani TV Bangla": {
        "url": "https://images.muslimandquran.com/frontend/images/Madani_Channel_Bangla_Live",
        "format": "",
        "page": "https://muslimandquran.com/islamic-media/live-islamic-tv-channels/madani-channel-bangla-live",
        "source": "Madani Channel Bangla Live listing",
        "license": "Station logo shown on third-party channel listing",
        "license_url": "",
    },
    "Nexus Television": {
        "url": "https://en.wikipedia.org/wiki/Special:FilePath/Nexus_Television_Logo.png",
        "format": "PNG",
        "page": "https://en.wikipedia.org/wiki/Nexus_Television",
        "source": "Nexus Television channel article",
        "license": "File license applies; see source page",
        "license_url": "",
    },
    "Cricbuzz": {
        "url": "https://commons.wikimedia.org/wiki/Special:FilePath/Cricbuzz_Logo.png",
        "format": "PNG",
        "page": "https://commons.wikimedia.org/wiki/File:Cricbuzz_Logo.png",
        "source": "Wikimedia Commons",
        "license": "Public domain text logo",
        "license_url": "https://creativecommons.org/publicdomain/zero/1.0/",
    },
    "Oman Sports": {
        "url": "https://i.imgur.com/1omi7p8.png",
        "format": "PNG",
        "page": "https://iptv-org.github.io/channels/om/OmanSportsTV",
        "source": "IPTV-org Oman Sports TV channel page",
        "license": "Station logo sourced from IPTV-org channel listing",
        "license_url": "",
    },
    "Dhaka FM 90.4": {
        "url": "https://dhakafm904.com/assets/images/dhakafm-logo.png",
        "format": "PNG",
        "page": "https://dhakafm904.com/overview.html",
        "source": "Dhaka FM official website",
        "license": "Station logo served by the broadcaster",
        "license_url": "",
    },
    "Global Panjab": {
        "url": "https://globalpunjabtv.in/wp-content/uploads/2019/08/logo-2.png",
        "format": "PNG",
        "page": "https://globalpunjabtv.in/",
        "source": "Global Punjab TV website",
        "license": "Broadcaster logo served on its website",
        "license_url": "",
    },
    "Pk Geo Super": {
        "url": "https://upload.wikimedia.org/wikipedia/en/5/5f/Geo_Super_logo.png",
        "format": "PNG",
        "page": "https://iptv-org.github.io/channels/pk/GeoSuper",
        "source": "IPTV-org Geo Super channel page",
        "license": "Channel logo from IPTV-org listing",
        "license_url": "",
    },
    "Radio Vivid Voice | Mymensingh": {
        "url": "https://radio.streamitter.com/images/logos/EFVAMB.png",
        "format": "PNG",
        "page": "https://github.com/junguler/m3u-radio-music-playlists/blob/4f7f422c65652805edf56a71b7ab17ac417b2755/strea-m-itter/bangladesh.m3u",
        "source": "Streamitter Bangladesh radio logo reference",
        "license": "Station artwork; reuse rights not specified",
        "license_url": "",
    },
    "Fuel TV Apac": {
        "url": "https://commons.wikimedia.org/wiki/Special:FilePath/Fuel_TV.svg",
        "format": "SVG",
        "page": "https://commons.wikimedia.org/wiki/File:Fuel_TV.svg",
        "source": "Wikimedia Commons Fuel TV logo",
        "license": "See the Commons file page for source and licensing",
        "license_url": "",
    },
    "Fuel TV Europe": {
        "url": "https://commons.wikimedia.org/wiki/Special:FilePath/Fuel_TV.svg",
        "format": "SVG",
        "page": "https://commons.wikimedia.org/wiki/File:Fuel_TV.svg",
        "source": "Wikimedia Commons Fuel TV logo",
        "license": "See the Commons file page for source and licensing",
        "license_url": "",
    },
    "Radio Bangla Rock": {
        "url": "https://radio.streamitter.com/images/logos/R13IIV.png",
        "format": "PNG",
        "page": "https://radio.bongonet.net:8020/radiobanglarock",
        "source": "Radio Bangla Rock public playlist logo reference",
        "license": "Station logo; reuse rights not specified",
        "license_url": "",
    },
    "Radio Gaan Baksho": {
        "url": "https://radiospinner.com/media/logos/180/84732/logo_t6wxUJOvSy.png",
        "format": "PNG",
        "page": "https://github.com/junguler/m3u-radio-music-playlists/blob/4f7f422c65652805edf56a71b7ab17ac417b2755/radio_spinner/bangladeshi.m3u",
        "source": "RadioSpinner Bangladeshi radio logo reference",
        "license": "Station artwork; reuse rights not specified",
        "license_url": "",
    },
    "Love Gold Bangla": {
        "url": "https://i.imgur.com/pLqV8yN.png",
        "format": "PNG",
        "page": "https://github.com/alaminislam203/my_playlist",
        "source": "Public radio playlist logo reference",
        "license": "Station logo; reuse rights not specified",
        "license_url": "",
    },
    "Madina Live": {
        "url": "https://images-na.ssl-images-amazon.com/images/I/71CywdrFaZL.png",
        "format": "PNG",
        "page": "https://cdn-globecast.akamaized.net/live/eds/saudi_sunnah/hls_roku/index.m3u8",
        "source": "Madina Live public playlist logo reference",
        "license": "Station logo; reuse rights not specified",
        "license_url": "",
    },
    "Persiana Travel": {
        "url": "https://s3.aynaott.com/storage/be9b48d87dcd7711cac19c17d8e01b27",
        "fallback_urls": ["https://www.lyngsat.com/logo/tv/pp/persiana-travel-fr.png"],
        "format": "",
        "page": "https://github.com/judy-gotv/iptv/blob/fb3fc31b1d46c2aef55bcadbe5f0be65ab3c5796/BD.m3u",
        "source": "Ayna OTT logo reference in a public playlist",
        "license": "Logo image; reuse rights not specified",
        "license_url": "",
    },
    "Setanta Sport": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/5/5d/Setanta-logo.jpg",
        "format": "JPEG",
        "page": "https://github.com/kilirushi/iptv/blob/f8765b54e7b66080201e07d168418e302c672c7d/cate/bein_sport.m3u",
        "source": "Setanta Sport logo reference in public playlist",
        "license": "Source/rights should be verified separately",
        "license_url": "",
    },
    "51 Radio TV [geo-blocked]": {
        "url": "https://raw.githubusercontent.com/iprtl/p1/master/logo/51radiotv.webp",
        "format": "WEBP",
        "page": "https://github.com/iprtl/p1/tree/master/logo",
        "source": "IPRTL logo collection exact 51 Radio TV match",
        "license": "Logo source found in public repository; reuse rights not stated",
        "license_url": "",
    },
    "Uttorbango Betar": {
        "url": "https://d371i8ihhgym7w.cloudfront.net/95642916.png",
        "format": "PNG",
        "page": "https://github.com/junguler/m3u-radio-music-playlists/blob/4f7f422c65652805edf56a71b7ab17ac417b2755/radio-ly/bd.m3u",
        "source": "Public Bangladesh radio playlist exact logo reference",
        "license": "Station artwork; reuse rights not specified",
        "license_url": "",
    },
    "Abc Music Radio": {
        "url": "https://cdn.instant.audio/images/logos/radio-bd-com/abc.png",
        "format": "PNG",
        "page": "https://radio-bd.com/",
        "source": "Radio-bd.com station logo collection",
        "license": "Station logo served by directory; reuse rights not specified",
        "license_url": "",
    },
    "Bangla Hits": {
        "url": "https://radio.streamitter.com/images/logos/R13IIV.png",
        "format": "PNG",
        "page": "https://radio.bongonet.net:8020/radiobanglarock",
        "source": "Bangladesh radio station logo collection",
        "license": "Station artwork; confirm exact station identity during visual review",
        "license_url": "",
    },
    "Magical Blade FM": {
        "url": "https://cdn.instant.audio/images/logos/radio-bd-com/magical-blade-fm.png",
        "format": "PNG",
        "page": "https://radio-bd.com/",
        "source": "Radio-bd.com station logo collection",
        "license": "Station logo served by directory; reuse rights not specified",
        "license_url": "",
    },
    "Radio Janata": {
        "url": "https://cdn.instant.audio/images/logos/radio-bd-com/janata.png",
        "format": "PNG",
        "page": "https://radio-bd.com/",
        "source": "Radio-bd.com station logo collection",
        "license": "Station logo served by directory; reuse rights not specified",
        "license_url": "",
    },
    "Radio Barakah": {
        "url": "https://cdn.instant.audio/images/logos/radio-bd-com/barakah.png",
        "format": "PNG",
        "page": "https://radio-bd.com/",
        "source": "Radio-bd.com station logo collection",
        "license": "Station logo served by directory; reuse rights not specified",
        "license_url": "",
    },
    "Radio Zenith FM": {
        "url": "https://cdn.instant.audio/images/logos/radio-bd-com/zenith.png",
        "format": "PNG",
        "page": "https://radio-bd.com/",
        "source": "Radio-bd.com station logo collection",
        "license": "Station logo served by directory; reuse rights not specified",
        "license_url": "",
    },
    "Radio Ritmo On Line": {
        "url": "https://cdn.instant.audio/images/logos/radio-bd-com/ritmo.png",
        "format": "PNG",
        "page": "https://radio-bd.com/",
        "source": "Radio-bd.com station logo collection",
        "license": "Station logo served by directory; reuse rights not specified",
        "license_url": "",
    },
    "Wc Music": {
        "url": "https://cdn.instant.audio/images/logos/radio-bd-com/wc-music.png",
        "format": "PNG",
        "page": "https://radio-bd.com/",
        "source": "Radio-bd.com station logo collection",
        "license": "Station logo served by directory; reuse rights not specified",
        "license_url": "",
    },
}

STOP_WORDS = {"hd", "uhd", "fhd", "sd", "4k", "8k", "1080p", "720p", "576p", "hevc", "h265", "h264"}
COMMONS_STOP_WORDS = {"the"}
SUPPORTED_FORMATS = {"SVG", "PNG", "JPEG", "JPG", "WEBP"}


def norm(value):
    value = unicodedata.normalize("NFKD", str(value or "")).encode("ascii", "ignore").decode().lower()
    value = value.replace("&", " and ").replace("+", " plus ")
    return re.sub(r"[^a-z0-9]+", " ", value).strip()


def clean_channel_name(value):
    words = norm(value).split()
    while words and (words[-1] in STOP_WORDS or re.fullmatch(r"\d{3,4}p", words[-1])):
        words.pop()
    return " ".join(words)


def slug(value):
    return re.sub(r"[^a-z0-9]+", "-", clean_channel_name(value)).strip("-") or "channel"


def basename(value):
    path = unquote(urlparse(value).path) if "://" in value else value
    return Path(path).name


def raw_logo_url(filename):
    return RAW_BASE + filename


def fetch_bytes(url, timeout=30, max_bytes=5_000_000):
    request = Request(url, headers={"User-Agent": UA})
    last_error = None
    for attempt in range(3):
        try:
            with urlopen(request, timeout=timeout) as response:
                raw = response.read(max_bytes + 1)
                content_type = response.headers.get("Content-Type", "").split(";", 1)[0].strip().lower()
            if len(raw) > max_bytes:
                raise ValueError("download exceeds 5 MB limit")
            return raw, content_type
        except Exception as error:
            last_error = error
            if attempt < 2 and ("Temporary failure in name resolution" in str(error) or "timed out" in str(error).lower()):
                time.sleep(attempt + 1)
                continue
            raise
    raise last_error


def fetch_json(url):
    raw, _ = fetch_bytes(url, timeout=45, max_bytes=20_000_000)
    return json.loads(raw.decode("utf-8"))


def is_generic_file(path):
    path = Path(path)
    if not path.is_file():
        return False
    if path.suffix.lower() == ".svg":
        return "CHANNEL MARK" in path.read_text(encoding="utf-8", errors="ignore").upper()
    return False


def is_generic_logo_url(value):
    return is_generic_file(LOGOS / basename(value))


def valid_image(raw, content_type, file_format=""):
    if len(raw) < 200:
        return False
    fmt = (file_format or "").upper()
    if content_type == "image/svg+xml" or fmt == "SVG" or raw.lstrip().startswith(b"<?xml") or b"<svg" in raw[:1000].lower():
        text = raw.decode("utf-8", errors="ignore")
        return "<svg" in text.lower() and "CHANNEL MARK" not in text.upper() and "<script" not in text.lower()
    if content_type == "image/png" or fmt == "PNG":
        return raw.startswith(b"\x89PNG\r\n\x1a\n")
    if content_type in ("image/jpeg", "image/jpg") or fmt in ("JPEG", "JPG"):
        return raw.startswith(b"\xff\xd8\xff")
    if content_type == "image/webp" or fmt == "WEBP":
        return raw[:4] == b"RIFF" and raw[8:12] == b"WEBP"
    if content_type == "image/avif" or fmt == "AVIF":
        return b"ftypavif" in raw[:40] or b"ftypavis" in raw[:40]
    # Some station/image CDNs send application/octet-stream or an empty MIME.
    # For source entries with no forced format, sniff standard image signatures.
    if not fmt:
        if raw.startswith(bytes([137, 80, 78, 71, 13, 10, 26, 10])):
            return True
        if raw.startswith(bytes([255, 216, 255])):
            return True
        if raw[:4] == b"RIFF" and raw[8:12] == b"WEBP":
            return True
        if b"ftypavif" in raw[:40] or b"ftypavis" in raw[:40]:
            return True
        head = raw.lstrip()[:500].lower()
        if b"<svg" in head:
            text = raw.decode("utf-8", errors="ignore")
            return "CHANNEL MARK" not in text.upper() and "<script" not in text.lower()
    return False


def extension_for(content_type, file_format="", source_url=""):
    fmt = (file_format or "").upper()
    by_fmt = {"SVG": ".svg", "PNG": ".png", "JPEG": ".jpg", "JPG": ".jpg", "WEBP": ".webp"}
    if fmt in by_fmt:
        return by_fmt[fmt]
    by_mime = {"image/svg+xml": ".svg", "image/png": ".png", "image/jpeg": ".jpg", "image/jpg": ".jpg", "image/webp": ".webp", "image/avif": ".avif"}
    if content_type in by_mime:
        return by_mime[content_type]
    suffix = Path(urlparse(source_url).path).suffix.lower()
    return suffix if suffix in (".svg", ".png", ".jpg", ".jpeg", ".webp") else ".png"


def parse_extinf(line):
    attrs = dict(re.findall(r'([\w-]+)="([^"]*)"', line))
    label = line.split(",", 1)[-1].strip() if "," in line else ""
    return attrs, label


def set_tvg_logo(line, url):
    return re.sub(r'tvg-logo="[^"]*"', 'tvg-logo="' + url + '"', line, count=1)


# Read original channel-logo URLs from the last pre-placeholder revision.
# This recovers exact historical channel-to-image mappings and avoids guessing
# based on approximate names from general logo catalogs.
HISTORICAL_PLAYLIST_URL = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/cde4fc51a5fe73858c167366ae5651b138433fb8/NVisionBD-Playlist.m3u"
HISTORICAL_PLAYLIST_PAGE = "https://github.com/saeidrahmanbd/BDIX-IPTV/blob/cde4fc51a5fe73858c167366ae5651b138433fb8/NVisionBD-Playlist.m3u"


def load_historical_logo_index():
    raw, _ = fetch_bytes(HISTORICAL_PLAYLIST_URL, timeout=45, max_bytes=25_000_000)
    historical = raw.decode("utf-8", errors="replace")
    by_name = {}
    url_users = {}
    for line in historical.splitlines():
        if not line.startswith("#EXTINF:"):
            continue
        attrs, label = parse_extinf(line)
        url = (attrs.get("tvg-logo") or "").strip()
        if not url.startswith(("http://", "https://")):
            continue
        base = basename(url).lower()
        if (base in ("unidentified.png", "unknown.png", "no-logo.png")
                or "placeholder" in base or "generic" in base
                or "nvisionbd-" in base):
            continue
        key = norm(label)
        if not key:
            continue
        by_name.setdefault(key, set()).add(url)
        url_users.setdefault(url, set()).add(key)

    # Do not reuse one old image for many unrelated channels; some historic
    # metadata entries shared a single generic sports image by mistake.
    output = {}
    for key, urls in by_name.items():
        if len(urls) != 1:
            continue
        url = next(iter(urls))
        if len(url_users.get(url, set())) > 2:
            continue
        extension = Path(urlparse(url).path).suffix.lower()
        fmt = {".png": "PNG", ".jpg": "JPEG", ".jpeg": "JPEG", ".webp": "WEBP", ".svg": "SVG"}.get(extension, "")
        output[key] = {
            "url": url,
            "format": fmt,
            "page": HISTORICAL_PLAYLIST_PAGE,
            "source": "Exact original tvg-logo URL from playlist history",
            "license": "Historical source URL; reuse rights not specified",
            "license_url": "",
        }
    return output


def load_iptv_org_indexes():
    channels = fetch_json(IPTV_CHANNELS_URL)
    logos = fetch_json(IPTV_LOGOS_URL)
    by_id = {}
    name_to_ids = {}
    for channel in channels:
        cid = str(channel.get("id") or "")
        if not cid:
            continue
        by_id[cid.casefold()] = channel
        aliases = [channel.get("name", "")] + list(channel.get("alt_names") or [])
        for alias in aliases:
            key = clean_channel_name(alias)
            if key:
                name_to_ids.setdefault(key, set()).add(cid)
    logos_by_id = {}
    for logo in logos:
        cid = str(logo.get("channel") or "")
        fmt = str(logo.get("format") or "").upper()
        if cid and fmt in SUPPORTED_FORMATS and logo.get("url"):
            logos_by_id.setdefault(cid.casefold(), []).append(logo)
    return by_id, name_to_ids, logos_by_id


def choose_iptv_logo(channel_id, logos_by_id):
    found = logos_by_id.get(channel_id.casefold(), [])
    if not found:
        return None
    active = [logo for logo in found if logo.get("in_use") is True]
    if active:
        found = active
    def rank(logo):
        tags = {str(tag).lower() for tag in (logo.get("tags") or [])}
        white_penalty = 1 if "white" in tags else 0
        horizontal = 1 if "horizontal" in tags else 0
        default_feed = 1 if not logo.get("feed") else 0
        pixels = int(logo.get("width") or 0) * int(logo.get("height") or 0)
        vector = 1 if str(logo.get("format") or "").upper() == "SVG" else 0
        return (default_feed, horizontal, -white_penalty, vector, pixels)
    found.sort(key=rank, reverse=True)
    return found[0]


def get_iptv_org_candidate(channel_label, tvg_id, indexes):
    by_id, name_to_ids, logos_by_id = indexes
    raw_id = (tvg_id or "").strip()
    if raw_id and not raw_id.lower().startswith(("custom.", "new.", "local.")):
        candidate_id = raw_id.split("@", 1)[0].strip()
        channel = by_id.get(candidate_id.casefold())
        if channel and choose_iptv_logo(candidate_id, logos_by_id):
            return choose_iptv_logo(candidate_id, logos_by_id), "IPTV-org exact ID: " + candidate_id
    key = clean_channel_name(channel_label)
    ids = name_to_ids.get(key, set())
    if len(ids) != 1:
        # Some channel catalogs write a brand as one token (10TV) while the
        # playlist uses a separator (10 TV). Accept this only if the compact
        # spelling resolves to one unique channel ID across all known aliases.
        compact_key = re.sub(r"\s+", "", key)
        compact_ids = set()
        for alias, alias_ids in name_to_ids.items():
            if re.sub(r"\s+", "", alias) == compact_key:
                compact_ids.update(alias_ids)
        if len(compact_ids) == 1:
            ids = compact_ids
        else:
            return None
    candidate_id = next(iter(ids))
    logo = choose_iptv_logo(candidate_id, logos_by_id)
    if not logo:
        return None
    return logo, "IPTV-org exact unique channel name: " + candidate_id


def download_to_repo(source_url, channel, source_format=""):
    raw, mime = fetch_bytes(source_url)
    if not valid_image(raw, mime, source_format):
        raise ValueError("source bytes are not a supported channel image")
    ext = extension_for(mime, source_format, source_url)
    filename = "nvisionbd-official-" + slug(channel) + ext
    destination = LOGOS / filename
    if destination.exists() and not is_generic_file(destination):
        return filename
    LOGOS.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(raw)
    return filename


def commons_candidate(channel):
    query = '"' + str(channel).replace('"', "") + '" logo'
    params = {
        "action": "query", "format": "json", "generator": "search",
        "gsrsearch": query, "gsrnamespace": 6, "gsrlimit": 12,
        "prop": "imageinfo", "iiprop": "url|size|mime|extmetadata"
    }
    data = fetch_json("https://commons.wikimedia.org/w/api.php?" + urlencode(params))
    target_words = [word for word in clean_channel_name(channel).split() if word not in COMMONS_STOP_WORDS]
    found = []
    for page in ((data.get("query") or {}).get("pages") or {}).values():
        title = page.get("title", "").replace("File:", "")
        stem_words = norm(Path(title).stem).split()
        if not target_words or not all(word in stem_words for word in target_words):
            continue
        # Require an explicit logo/wordmark title, and reject extra brand names
        # or organization types that imply a different logo. Extra tokens are
        # limited to format/quality descriptors and the occasional channel label.
        if not any(word in stem_words for word in ("logo", "logotype", "wordmark")):
            continue
        harmless_extras = {
            "logo", "logotype", "wordmark", "channel", "tv", "network", "official",
            "transparent", "white", "black", "hd", "uhd", "sd", "4k", "png", "svg",
            "webp", "jpg", "jpeg", "2023", "2024", "2025", "2026"
        }
        extra_tokens = set(stem_words) - set(target_words) - harmless_extras
        if extra_tokens:
            continue
        infos = page.get("imageinfo") or []
        if not infos:
            continue
        info = infos[0]
        mime = str(info.get("mime") or "").lower()
        fmt = {"image/svg+xml": "SVG", "image/png": "PNG", "image/jpeg": "JPEG", "image/webp": "WEBP"}.get(mime, "")
        if fmt not in SUPPORTED_FORMATS:
            continue
        if int(info.get("width") or 0) < 40 or int(info.get("height") or 0) < 25:
            continue
        metadata = info.get("extmetadata") or {}
        license_name = str((metadata.get("LicenseShortName") or {}).get("value") or "").strip()
        license_url = str((metadata.get("LicenseUrl") or {}).get("value") or "").strip()
        if not license_name or not license_url or not info.get("url"):
            continue
        pixels = int(info.get("width") or 0) * int(info.get("height") or 0)
        found.append((pixels, page, info, fmt, license_name, license_url))
    found.sort(key=lambda item: item[0], reverse=True)
    if not found:
        return None
    if len(found) > 1 and found[0][0] <= found[1][0] * 1.15:
        return None
    _, page, info, fmt, license_name, license_url = found[0]
    return {
        "url": info["url"], "format": fmt, "title": page.get("title", ""),
        "page": info.get("descriptionurl", ""), "license": license_name,
        "license_url": license_url,
    }


def get_local_logo(channel):
    """Search the repository's entire /logos folder before any external lookup.

    Match by normalized channel name only. Generic template assets, nvisionbd-
    placeholders, placeholder-* files, backups and unrelated fuzzy name matches
    are never accepted automatically.
    """
    target = clean_channel_name(channel)
    if not target:
        return None

    # Exact, curated overrides remain first in line. Search nested folders
    # such as /logos/unused too, then promote the exact file to /logos root.
    explicit = LOCAL_LOGO_FILES.get(channel)
    if explicit:
        path = LOGOS / explicit
        if not path.is_file():
            path = next((p for p in LOGOS.rglob(explicit) if p.is_file()), None)
        if path and path.is_file() and not is_generic_file(path):
            destination = LOGOS / explicit
            if path.parent != LOGOS and not destination.exists():
                shutil.copyfile(path, destination)
            return explicit

    supported = {".svg", ".png", ".jpg", ".jpeg", ".webp", ".avif"}
    matches = []
    # Recursive scan includes logos/unused as requested; an exact match there
    # is copied into /logos root so playlist URLs remain simple and stable.
    for path in LOGOS.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in supported:
            continue
        lower_name = path.name.lower()
        if lower_name.startswith("placeholder-"):
            continue
        if lower_name.startswith("nvisionbd-") and not lower_name.startswith("nvisionbd-official-"):
            continue
        if re.search(r"-backup-?\d*(?:\.|$)", lower_name):
            continue
        if is_generic_file(path):
            continue

        stem = path.stem.lower()
        # Already source-checked logos saved by this workflow can also be reused.
        if stem.startswith("nvisionbd-official-"):
            stem = stem[len("nvisionbd-official-"):]
        # Remove generated hash and quality/resolution suffixes from filenames.
        stem = re.sub(r"-[a-f0-9]{8,}$", "", stem)
        previous = None
        while stem != previous:
            previous = stem
            stem = re.sub(
                r"-(?:1080p|720p|576p|480p|360p|4k|8k|uhd|fhd|hd|sd|hevc|h265|h264)$",
                "", stem, flags=re.I
            )
        candidate = clean_channel_name(stem)
        if candidate != target:
            continue

        # Prefer a canonical filename over a hashed / resolution-specific copy.
        original_norm = clean_channel_name(path.stem)
        has_hash = bool(re.search(r"-[a-f0-9]{8,}$", path.stem.lower()))
        has_quality = bool(re.search(
            r"-(?:1080p|720p|576p|480p|360p|4k|8k|uhd|fhd|hd|sd|hevc|h265|h264)$",
            path.stem.lower()
        ))
        ext_rank = {".svg": 0, ".png": 1, ".webp": 2, ".jpg": 3, ".jpeg": 4}.get(path.suffix.lower(), 9)
        matches.append((has_hash, has_quality, ext_rank, path.name.casefold(), path.name))

    if not matches:
        return None
    matches.sort()
    # Prefer a canonical copy in /logos root. If the exact match lives in
    # /logos/unused, restore a root copy rather than leaving the playlist to
    # depend on the unused subfolder.
    chosen = next((item for item in matches if (LOGOS / item[-1]).is_file()), matches[0])
    source_path = next(path for path in LOGOS.rglob(chosen[-1]) if path.is_file())
    destination = LOGOS / source_path.name
    if source_path.parent != LOGOS:
        if not destination.exists():
            shutil.copyfile(source_path, destination)
        elif is_generic_file(destination):
            destination.unlink()
            shutil.copyfile(source_path, destination)
    return destination.name

def build_audit():
    playlist_names = ["IPTV-Playlist.m3u", "BDIX-Playlist.m3u", "NVisionBD-Playlist.m3u"]
    rows = []
    for playlist_name in playlist_names:
        path = Path(playlist_name)
        if not path.is_file():
            rows.append((playlist_name, 0, 0, []))
            continue
        content = path.read_text(encoding="utf-8", errors="replace")
        labels, generic_files = set(), set()
        entry_count = 0
        for line in content.splitlines():
            if not line.startswith("#EXTINF:"):
                continue
            entry_count += 1
            attrs, label = parse_extinf(line)
            logo = attrs.get("tvg-logo", "")
            if logo and is_generic_logo_url(logo):
                generic_files.add(basename(logo))
                labels.add(label)
        rows.append((playlist_name, entry_count, len(generic_files), sorted(labels)))
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# Generic Channel Logo Audit — Three Playlists", "",
        f"Audit date: {timestamp}  ",
        "Repository: https://github.com/saeidrahmanbd/BDIX-IPTV  ",
        "Method: scans current playlist metadata and checks referenced local SVG files for the generic CHANNEL MARK template.", "",
        "## Summary", "",
        "| Playlist | Entries | Unique generic placeholder assets |",
        "|---|---:|---:|",
    ]
    for playlist_name, entries_count, generic_count, _ in rows:
        lines.append(f"| {playlist_name} | {entries_count} | {generic_count} |")
    target = next((row for row in rows if row[0] == "NVisionBD-Playlist.m3u"), ("", 0, 0, []))
    lines += ["", f"Current NVisionBD placeholder assets: **{target[2]} unique files**.", "",
              "## Remaining affected NVisionBD channel labels", ""]
    for label in target[3]:
        lines.append("- " + label.replace("\n", " "))
    lines += ["", "## Scope and quality rules", "",
              "- Only NVisionBD-Playlist.m3u is modified by the replacement workflow.",
              "- A replacement must be a validated image, must not contain the CHANNEL MARK template, and must have a source recorded in the replacement-results report.",
              "- If multiple channels share a name, or no trustworthy source is found, the placeholder is retained and listed for manual review.",
              "- Old generic files are not deleted automatically, to avoid breaking any other reference.", ""]
    AUDIT.parent.mkdir(parents=True, exist_ok=True)
    AUDIT.write_text("\n".join(lines), encoding="utf-8")


def main():
    if not PLAYLIST.is_file():
        raise SystemExit("NVisionBD-Playlist.m3u not found")
    text = PLAYLIST.read_text(encoding="utf-8", errors="replace")
    # Repair malformed URLs left by the previous script.
    text = re.sub(r"https:/raw\.githubusercontent\.com/", "https://raw.githubusercontent.com/", text)
    # Restore generic references where a previous run used a lookalike logo.
    # Remove only the rejected output assets produced by the earlier logo pass.
    for bad_name, (good_name, _reason) in REJECTED_PREVIOUS_MATCHES.items():
        text = re.sub(r'tvg-logo="[^"]*' + re.escape(bad_name) + r'"',
                      'tvg-logo="' + raw_logo_url(good_name) + '"', text)
        if bad_name.startswith("nvisionbd-official-"):
            rejected_path = LOGOS / bad_name
            if rejected_path.is_file():
                rejected_path.unlink()

    try:
        iptv_indexes = load_iptv_org_indexes()
        iptv_status = "loaded"
    except Exception as error:
        iptv_indexes = None
        iptv_status = "unavailable: " + str(error)[:160]
    try:
        historical_logo_index = load_historical_logo_index()
        historical_status = f"loaded {len(historical_logo_index)} exact historical logo mappings"
    except Exception as error:
        historical_logo_index = {}
        historical_status = "unavailable: " + str(error)[:160]

    targets = {}
    for line in text.splitlines():
        if not line.startswith("#EXTINF:"):
            continue
        attrs, label = parse_extinf(line)
        logo = attrs.get("tvg-logo", "")
        if logo and is_generic_logo_url(logo):
            targets.setdefault(basename(logo), {"label": label, "tvg_id": attrs.get("tvg-id", "")})

    replacements, unresolved = [], []
    replacements_by_file = {}
    download_cache = {}
    for old_file, item in sorted(targets.items()):
        channel = item["label"]
        try:
            local = get_local_logo(channel)
            if local:
                new_file = local
                source = "Existing verified repository asset"
                source_page = "https://github.com/saeidrahmanbd/BDIX-IPTV/tree/main/logos"
                license_name, license_url = "Existing repository asset", ""
            else:
                candidate = None
                source, source_page = "", ""
                license_name, license_url = "", ""
                # Curated exact sources take precedence over a name-based
                # catalog suggestion, which can identify a similarly named
                # channel from the wrong country or brand.
                if channel in DIRECT_LOGO_HINTS:
                    candidate = dict(DIRECT_LOGO_HINTS[channel])
                    source = candidate.pop("source", "Direct station source")
                    source_page = candidate.get("page", "")
                    license_name = candidate.get("license", "")
                    license_url = candidate.get("license_url", "")
                elif norm(channel) in historical_logo_index:
                    candidate = dict(historical_logo_index[norm(channel)])
                    source = candidate.pop("source", "Historical playlist logo URL")
                    source_page = candidate.get("page", "")
                    license_name = candidate.get("license", "")
                    license_url = candidate.get("license_url", "")
                elif channel in DIRECT_PAGE_HINTS:
                    page_url, allow_og_image = DIRECT_PAGE_HINTS[channel]
                    try:
                        logo_url = find_page_logo(page_url, allow_og_image=allow_og_image)
                    except Exception:
                        logo_url = None
                    if logo_url:
                        candidate = {
                            "url": logo_url,
                            "format": "",
                            "page": page_url,
                            "license": "Logo image served by the station website; reuse rights not specified",
                            "license_url": "",
                        }
                        source = "Station website logo image"
                elif channel in TV_LOGO_HINTS:
                    hint_path = TV_LOGO_HINTS[channel]
                    candidate = {
                        "url": TV_LOGO_BASE + hint_path,
                        "format": Path(hint_path).suffix.lstrip(".").upper(),
                        "page": TV_LOGO_REPO + "/blob/main/" + hint_path,
                        "license": "No license file found in source repository",
                        "license_url": "",
                    }
                    source = "tv-logo/tv-logos channel/region source"
                if not candidate and iptv_indexes:
                    result = get_iptv_org_candidate(channel, item["tvg_id"], iptv_indexes)
                    if result and result[0]:
                        logo_obj, source = result
                        candidate = {
                            "url": logo_obj.get("url", ""),
                            "format": str(logo_obj.get("format") or "").upper(),
                            "page": logo_obj.get("url", ""),
                            "license": "IPTV-org public logo dataset",
                            "license_url": "https://github.com/iptv-org/database",
                        }
                if not candidate:
                    candidate = commons_candidate(channel)
                    if candidate:
                        source = "Wikimedia Commons"
                if not candidate:
                    unresolved.append((channel, old_file, "No unique source-verified channel logo found"))
                    time.sleep(0.1)
                    continue
                candidate_urls = [candidate["url"]] + list(candidate.get("fallback_urls") or [])
                last_download_error = None
                new_file = None
                for src in candidate_urls:
                    try:
                        cache_key = (src, channel)
                        if cache_key in download_cache:
                            new_file = download_cache[cache_key]
                        else:
                            new_file = download_to_repo(src, channel, candidate.get("format", ""))
                            download_cache[cache_key] = new_file
                        if src != candidate["url"]:
                            source += " (fallback image URL)"
                        break
                    except Exception as download_error:
                        last_download_error = download_error
                        new_file = None
                if not new_file and channel in DIRECT_PAGE_HINTS:
                    # Retry from the official/station page if a direct image URL
                    # was dead or blocked. Only logo-marked images are accepted.
                    page_url, allow_og_image = DIRECT_PAGE_HINTS[channel]
                    try:
                        page_logo = find_page_logo(page_url, allow_og_image=allow_og_image)
                        if page_logo:
                            new_file = download_to_repo(page_logo, channel, "")
                            candidate["page"] = page_url
                            source += " (station-page image fallback)"
                    except Exception as page_error:
                        last_download_error = page_error
                # As a final recovery step, use a uniquely licensed Wikimedia
                # Commons logo when no curated image URL could be downloaded.
                if not new_file:
                    try:
                        fallback = commons_candidate(channel)
                        if fallback:
                            new_file = download_to_repo(fallback["url"], channel, fallback.get("format", ""))
                            source = "Wikimedia Commons exact logo fallback"
                            source_page = fallback.get("page", "")
                            license_name = fallback.get("license", "")
                            license_url = fallback.get("license_url", "")
                    except Exception as commons_error:
                        last_download_error = commons_error
                if not new_file:
                    raise ValueError("all logo image URLs failed: " + str(last_download_error)[:140])
                source_page = candidate.get("page", "")
                license_name = candidate.get("license", "")
                license_url = candidate.get("license_url", "")

            replacements_by_file[old_file] = raw_logo_url(new_file)
            replacements.append((channel, old_file, new_file, source, source_page, license_name, license_url))
        except Exception as error:
            unresolved.append((channel, old_file, "Lookup/download/validation error: " + str(error)[:160]))
        time.sleep(0.15)

    output_lines = []
    for line in text.splitlines():
        if line.startswith("#EXTINF:"):
            attrs, _ = parse_extinf(line)
            logo = attrs.get("tvg-logo", "")
            old_file = basename(logo) if logo else ""
            if old_file in replacements_by_file:
                line = set_tvg_logo(line, replacements_by_file[old_file])
        output_lines.append(line)
    new_text = "\n".join(output_lines).rstrip() + "\n"
    PLAYLIST.write_text(new_text, encoding="utf-8")

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Generic Logo Replacement Results", "",
        "This report covers the current NVisionBD-Playlist.m3u. Only confidently matched, validated artwork is applied; ambiguous sources remain unresolved.", "",
        f"- Run time: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        f"- IPTV-org dataset: {iptv_status}",
        f"- Historical logo mappings: {historical_status}",
        f"- Unique generic assets examined: {len(targets)}",
        f"- Successful replacements: {len(replacements)}",
        f"- Unresolved/manual review: {len(unresolved)}", "",
        "## Replacements", "",
        "| Channel | Former generic file | New local file | Source | License / attribution |",
        "|---|---|---|---|---|",
    ]
    for channel, old_file, new_file, source, source_page, license_name, license_url in replacements:
        source_link = f"[{source}]({source_page})" if source_page else source
        license_info = license_name + (f" ([license]({license_url}))" if license_url else "")
        lines.append(f"| {channel.replace('|', '/')} | {old_file} | [{new_file}]({RAW_BASE + new_file}) | {source_link} | {license_info} |")
    lines += ["", "## Unresolved — retained for manual source verification", "",
              "| Channel | Current placeholder asset | Reason |",
              "|---|---|---|"]
    for channel, old_file, reason in unresolved:
        lines.append(f"| {channel.replace('|', '/')} | {old_file} | {reason.replace('|', '/')} |")
    if not unresolved:
        lines += ["", "All identified generic assets were replaced with source-verified local logos."]
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    build_audit()
    print(f"examined={len(targets)} replaced={len(replacements)} unresolved={len(unresolved)} iptv_org={iptv_status}")


if __name__ == "__main__":
    main()
