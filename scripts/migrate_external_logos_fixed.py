#!/usr/bin/env python3
"""Resolve missing/external channel logos and store them as local PNG files."""
import io, json, re, urllib.request
from pathlib import Path
from PIL import Image
try:
    import cairosvg
except ImportError:
    cairosvg = None

PLAYLIST = Path("IPTV-Playlist.m3u")
LOGOS = Path("logos")
RAW_BASE = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/"
CHANNELS_API = "https://iptv-org.github.io/api/channels.json"
LOGOS_API = "https://iptv-org.github.io/api/logos.json"
ATTR_RE = re.compile(r'([\w-]+)="([^"]*)"')

FALLBACK_LOGOS = {
    "aamarbangla": "https://jiotvimages.cdn.jio.com/dare_images/images/Amaar_Bangla.png",
    "amarbangladigital": "https://jiotvimages.cdn.jio.com/dare_images/images/Amar_Digital_TV.png",
    "actionhollywoodmovies": "https://provider-static.plex.tv/epg/cms/production/c94e3220-9a45-42e9-8bdb-01fc43e0f27c/white_textAction_Hollywood_Movies_logo_dark_-_Angela_Chan.png",
    "amctriller": "https://github.com/tv-logo/tv-logos/blob/main/misc/vod/amc-thrillers-vod.png?raw=true",
    "bangbangtv": "https://alchetron.com/cdn/bang-bang-tv-channel-86505200-5377-43bb-ac56-4a72cc2c786-resize-750.jpg",
    "barazamusictv": "https://i.imgur.com/djhtmFQ.png",
    "loltv": "https://d229kpbsb5jevy.cloudfront.net/yuppfast/content/common/channel/logos/lol-tv.png",
    "mytimemovie": "https://images-3.rakuten.tv/storage/global-live-channel/translation/artwork/8cb0d25f-b096-4e26-a957-6b271f7f0560.jpeg",
    "mytimemovienetworkbr": "https://i.imgur.com/aiGQtzI.png",
    "rakutenmovies": "https://s3.aynaott.com/storage/22af43810a37af9a151f1e0a23adde63",
    "sparklemovies": "https://tvpnlogopeu.samsungcloud.tv/platform/image/sourcelogo/vc/00/02/34/GBAJ400042T1_20250107T025804SQUARE.png",
    "vevohiphoprb": "https://tvpnlogopeu.samsungcloud.tv/platform/image/sourcelogo/vc/00/02/34/GBBD2300001C0_20250107T030829SQUARE.png",
    "documentaryinternational": "https://images-cdn1.welcomesoftware.com/assets/Documentaryplus-hero.jpg/Zz0yNjViNjNhZWEwNjIxMWVmOTAwY2NlYjBjYTI5N2FjYw%3D%3D?width=1200",
    "historywarwarenow": "https://www.tvchannellists.com/wiki/images/d/d9/History_%26_Warfare_Now_%28SamsungTV%2B%29.png",
    "mysteriesxplored": "https://tvpnlogopus.samsungcloud.tv/platform/image/sourcelogo/vc/00/02/34/USBB5200028MM_20260120T230343SQUARE.png",
    "moviedomefamily": "https://www.senselan.ch/files/img/NexTV2/Sender/406.png",
    "sanandatv": "https://www.jagobd.com/wp-content/uploads/2024/10/sananda.jpg",
    "sonicbangla": "https://xstreamcp-assets-msp.streamready.in/assets/LIVETV/LIVECHANNEL/LIVETV_LIVETVCHANNEL_SONIC/images/LOGO_HD/image.png",
    "marqueesportsnetwork": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Marquee_Sports_Network_Logo.svg/512px-Marquee_Sports_Network_Logo.svg.png",
    "adithyatv": "https://xstreamcp-assets-msp.streamready.in/assets/LIVETV/LIVECHANNEL/LIVETV_LIVETVCHANNEL_ADITHYA_TV/images/LOGO_HD/image.png",
    "zeesarthak": "https://xstreamcp-assets-msp.streamready.in/assets/LIVETV/LIVECHANNEL/LIVETV_LIVETVCHANNEL_ZEE_SARTHAK/images/LOGO_HD/LOGO_HD_image.png",
}

# Exact playlist ID -> explicit logo source. Add only verified mappings here.
# These are intentionally keyed by playlist identity, never by stream URL or display name.
ID_LOGO_MAP = {
    "aamarbangla.in": "https://jiotvimages.cdn.jio.com/dare_images/images/Amaar_Bangla.png",
    "local.1d6cdda4509e": "https://jiotvimages.cdn.jio.com/dare_images/images/Amar_Digital_TV.png",
    "colorsbangla.in": "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/colors-bangla.png",
    "local.bb3c3114fb20": "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/colors-bangla-hd.png",
    "local.sun-bangla": "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/sun-bangla.png",
    "sunbangla.in": "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/sun-bangla.png",
    "local.matri-bhumi-tv": "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/matri-bhumi-tv.png",
    "matribhumiTV.bd": "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/matri-bhumi-tv.png",
    "zeebangla.in": "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/zee-bangla.png",
    "local.072484feec7e": "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/zee-bangla-hd.png",
    "zeebanglasonar.in": "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/zee-bangla-sonar.png",
    "local.zee-bangla-cinema": "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/zee-bangla-sonar.png",
    "sonyentertainmenttelevision": "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/sony-entertainment-tv.png",
    "sonyyay.in": "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/sonic.png",
    "sonyyay.in@sd": "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/sony-yay.png",
    "meiahmoviechannel.hk": "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/mei-ah-movie-channel-1080p-427874b362.png",
    "meiahmoviechannel.hk@sd": "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/mei-ah-movie-channel-1080p-427874b362.png",
    "cartoonnetwork.uk": "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/cartoon-network.png",
    "cartoonnetworkhdplus.in": "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/cartoon-network-hd.png",
    "mytimemovienetwork.br@sd": "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/mytime-movie-network-br.png",
    "mytimemovienetwork.br": "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/mytime-movie-network-720p-cc34ff46f5.png",
    "mytimemovienetworkeast.us": "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/mytime-movie-network-1080p-79e6ec3226.png",
    "rajdhanitv.bd": "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/rajdhani-tv.png",
    "local.rajdhani-alt": "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/rajdhani-alt.png",
    "ekamrabharatodia.in@sd": "https://jiotv.catchup.cdn.jio.com/dare_images/images/Ekamra_Bharat_Odia.png",
    "etvplus.in@sd": "https://xstreamcp-assets-msp.streamready.in/assets/LIVETV/LIVECHANNEL/LIVETV_LIVETVCHANNEL_ETV_PLUS/images/LOGO_HD/image.png",
    "zee24ghanta.in@sd": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYy4jJoltvhvpRSuk8i6Wm03s40xqEpsla9Q&s",
    "axnblack.us@czechrepublic": "https://i.imgur.com/Peo1QiZ.png",
    "axnblack.us@poland": "https://i.imgur.com/Peo1QiZ.png",
    "axncee.es@hungary": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/AXN_logo_%282015%29.svg/960px-AXN_logo_%282015%29.svg.png",
    "axnlatinamerica.us@centralamerica": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/AXN_logo_%282015%29.svg/960px-AXN_logo_%282015%29.svg.png",
    "filmbox.nl@netherlands": "https://i.imgur.com/VyaslIY.png",
    "mbcplusdrama.sa@sd": "https://i.imgur.com/lxWdjXG.png",
    "moviesthriller.sa@sd": "https://i.imgur.com/JWihdcl.png",
    "musicboxhits.cz@sd": "https://musicboxhits.com/music_box_hits_logo.png",
    "sonyonefavoris.fr@hd": "https://i.imgur.com/RO4AM4b.png",
    "sonyonehitsaction.fr@hd": "https://i.imgur.com/pXsZEsR.png",
    "sonyonehitscomedie.fr@hd": "https://i.imgur.com/8sHuxxS.png",
    "pbskids.us@sd": "https://i.imgur.com/q4cUQKW.png",
    "bahrainsports2.bh@sd": "https://i.imgur.com/ZkuZmIo.png",
    "cricketgold.au@sd": "https://resources.cricket-australia.pulselive.com/cricket-australia/photo/2025/07/25/836eddae-4329-4542-ad17-dcd37e9d951a/Cricket-Gold-1920x1080_noBG.png",
    "fite247.us@sd": "https://i.imgur.com/ESV6qgH.png",
    "pgatour.us@sd": "https://i.imgur.com/J0TY9dG.png",
    "realmadridtvenglish.es@sd": "https://i.imgur.com/5pMo7dL.png",
    "redbulltv.at@eumena": "https://images.pluto.tv/channels/5e7cb84a172a0f0007da69e4/colorLogoPNG.png",
    "talksport.uk@sd": "https://upload.wikimedia.org/wikipedia/en/9/9d/Talksport_logo.png",
    "wildtv.ca@sd": "https://sales.wildtv.ca/hubfs/WildTV%20Media%20Centre%20Packages/WildTV-White-XXL.png?hsLang=en-ca&noresize=",
    "marqueesportsnetwork.us": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Marquee_Sports_Network_Logo.svg/512px-Marquee_Sports_Network_Logo.svg.png",
    "adithyatv.in@sd": "https://xstreamcp-assets-msp.streamready.in/assets/LIVETV/LIVECHANNEL/LIVETV_LIVETVCHANNEL_ADITHYA_TV/images/LOGO_HD/image.png",
    "zeesarthak.in@sd": "https://xstreamcp-assets-msp.streamready.in/assets/LIVETV/LIVECHANNEL/LIVETV_LIVETVCHANNEL_ZEE_SARTHAK/images/LOGO_HD/LOGO_HD_image.png",
    "zeebiskope.in@sd": "https://xstreamcp-assets-msp.streamready.in/assets/LIVETV/LIVECHANNEL/LIVETV_LIVETVCHANNEL_ZEE_BISKOPE/images/LOGO_HD/LOGO_HD_image.png",
    "ekamracinema.in@sd": "http://jiotv.catchup.cdn.jio.com/dare_images/images/Ekamra_Cinema.png",
    "ekamramanoranjan.in@sd": "http://jiotv.catchup.cdn.jio.com/dare_images/images/Ekamra_Manoranjan.png",
    "ekamramusiq.in@sd": "http://jiotv.catchup.cdn.jio.com/dare_images/images/Ekamra_Music.png",
    "ekamranilachakra.in@sd": "http://jiotv.catchup.cdn.jio.com/dare_images/images/Ekamra_Nilach_akra.png",
    "jatraekamra.in@sd": "http://jiotv.catchup.cdn.jio.com/dare_images/images/Jatra_Ekamra.png",
    "jayamax.in@sd": "https://xstreamcp-assets-msp.streamready.in/assets/LIVETV/LIVECHANNEL/LIVETV_LIVETVCHANNEL_JAYA_MAX/images/LOGO_HD/image.png",
    "jayatv.in@hd": "https://xstreamcp-assets-msp.streamready.in/assets/LIVETV/LIVECHANNEL/LIVETV_LIVETVCHANNEL_JAYA_TV/images/LOGO_HD/image.png",
    "moviesnow.in@hd": "https://xstreamcp-assets-msp.streamready.in/assets/LIVETV/LIVECHANNEL/LIVETV_LIVETVCHANNEL_MOVIES_NOW/images/LOGO_HD/image.png",
    "sangeetbhojpuri.in@sd": "https://dtil.tmsimg.com/assets/s143757_ld_h15_aa.png?lock=720x540",
    "starchannel.bg@sd": "https://upload.wikimedia.org/wikipedia/commons/c/cd/Star_Channel_2023.svg",
    "starsuvarna.in@hd": "http://smumcdnems03.cdnsrv.jio.com/mumsite.cdnsrv.jio.com/jiotv.catchup.cdn.jio.com/dare_images/images/Suvarna.png",
    "udayamovies.in@sd": "https://xstreamcp-assets-msp.streamready.in/assets/LIVETV/LIVECHANNEL/LIVETV_LIVETVCHANNEL_UDAYA_MOVIES/images/LOGO_HD/image.png",
    "zeebiskope.in@sd": "https://xstreamcp-assets-msp.streamready.in/assets/LIVETV/LIVECHANNEL/LIVETV_LIVETVCHANNEL_ZEE_BISKOPE/images/LOGO_HD/LOGO_HD_image.png",
}

def exact_id(metadata):
    """Return the strongest playlist identity available; never infer it from a stream URL."""
    return (metadata.get("tvg-id") or metadata.get("channel-id") or "").strip().lower()

def explicit_logo_for_id(channel_id):
    """Return only a verified exact-ID logo mapping."""
    return ID_LOGO_MAP.get(channel_id)
def attrs(line): return dict(ATTR_RE.findall(line))
def clean_name(value):
    value = re.sub(r"\[[^]]*\]|\([^)]*\)", " ", value)
    value = re.sub(r"\b(?:hd|fhd|uhd|sd|4k|1080p|720p|576p|480p|360p)\b", " ", value, flags=re.I)
    return re.sub(r"[^a-z0-9]+", "", value.lower())
def safe_name(value): return (re.sub(r"[^A-Za-z0-9]+", "-", value).strip("-").lower()[:90] or "channel")
def is_local(value): return value.startswith(RAW_BASE) or value.startswith("logos/") or "raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV" in value
def fetch_bytes(url):
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read(), response.headers.get("Content-Type", "")
def download_png(url, target):
    data, content_type = fetch_bytes(url)
    try:
        Image.open(io.BytesIO(data)).convert("RGBA").save(target, format="PNG", optimize=True)
        return
    except Exception:
        if cairosvg is None: raise
        if data.lstrip().startswith(b"<svg") or "svg" in content_type.lower() or url.lower().split("?")[0].endswith(".svg"):
            png = cairosvg.svg2png(bytestring=data, output_width=1000)
            Image.open(io.BytesIO(png)).convert("RGBA").save(target, format="PNG", optimize=True)
            return
        raise
def force_local(line, replacement):
    if 'tvg-logo="' in line:
        return re.sub(r'(tvg-logo=")[^"]*(")', r'\1' + replacement + r'\2', line, count=1)
    comma = line.find(",")
    return line if comma == -1 else line[:comma] + f' tvg-logo="{replacement}"' + line[comma:]
def fetch_json(url):
    data, _ = fetch_bytes(url)
    return json.loads(data.decode("utf-8"))

LOGOS.mkdir(parents=True, exist_ok=True)
original = PLAYLIST.read_text(encoding="utf-8-sig").replace("\r", "")
lines = original.splitlines()

local_by_id = {}
local_by_name = {}
for line in lines:
    if not line.startswith("#EXTINF"): continue
    metadata = attrs(line)
    logo = metadata.get("tvg-logo", "").strip()
    if logo and is_local(logo) and logo.lower().endswith(".png"):
        channel_id = exact_id(metadata)
        title = metadata.get("tvg-name") or line.rsplit(",", 1)[-1].strip()
        filename = logo[len(RAW_BASE):].split("?", 1)[0] if logo.startswith(RAW_BASE) else Path(logo).name
        if not (LOGOS / filename).is_file():
            continue
        if channel_id:
            local_by_id.setdefault(channel_id, set()).add(logo)
        local_by_name.setdefault(clean_name(title), set()).add(logo)

channels, logos = [], []
try:
    channels = fetch_json(CHANNELS_API)
    logos = fetch_json(LOGOS_API)
except Exception as exc:
    print(f"Logo catalogue unavailable: {exc}")

channel_by_id = {str(c.get("id","")).lower(): c for c in channels if c.get("id")}
channel_by_name = {}
for c in channels:
    for n in [c.get("name","")] + list(c.get("alt_names") or []):
        key = clean_name(str(n))
        if key: channel_by_name.setdefault(key, []).append(c)

logo_by_channel = {}
for item in logos:
    cid = str(item.get("channel","")).lower()
    if not cid: continue
    score = (1000 if item.get("in_use") else 0, 100 if str(item.get("format","")).upper() in {"PNG","SVG"} else 0, int(item.get("width") or 0) * int(item.get("height") or 0))
    if cid not in logo_by_channel or score > logo_by_channel[cid][0]:
        logo_by_channel[cid] = (score, item)

changed = downloaded = failed = resolved_from_existing = resolved_from_catalogue = resolved_from_fallback = converted_local = 0
unresolved = []
output = []

for line in lines:
    if not line.startswith("#EXTINF"):
        output.append(line); continue

    metadata = attrs(line)
    logo = metadata.get("tvg-logo", "").strip()
    title = metadata.get("tvg-name") or line.rsplit(",", 1)[-1].strip()
    base_title = clean_name(title)
    channel_id = exact_id(metadata)
    mapped_logo = explicit_logo_for_id(channel_id) if channel_id else None

    # Explicit ID overrides are authoritative and run before any existing-logo shortcut.
    if mapped_logo:
        filename = f"{safe_name(title)}.png"
        target = LOGOS / filename
        replacement = RAW_BASE + filename
        try:
            if not target.exists():
                download_png(mapped_logo, target); downloaded += 1
            output.append(force_local(line, replacement))
            changed += 1; resolved_from_fallback += 1
            local_by_id.setdefault(channel_id, set()).add(replacement)
            continue
        except Exception as exc:
            failed += 1
            print(f"Explicit ID logo failed: {title} [{channel_id}]: {exc}")

    if logo and is_local(logo):
        if logo.lower().endswith(".png"):
            filename = logo[len(RAW_BASE):].split("?", 1)[0] if logo.startswith(RAW_BASE) else Path(logo).name
            target = LOGOS / filename
            if target.is_file():
                try:
                    with Image.open(target) as im:
                        im.verify()
                    output.append(line)
                    continue
                except Exception:
                    pass
            # Broken/missing local reference: fall through to ID/name/catalogue repair.
        filename = f"{safe_name(title)}.png"
        target = LOGOS / filename
        replacement = RAW_BASE + filename
        try:
            if not target.exists():
                download_png(logo, target); downloaded += 1
            output.append(force_local(line, replacement))
            changed += 1; converted_local += 1
            local_by_name.setdefault(base_title, set()).add(replacement)
            continue
        except Exception as exc:
            failed += 1
            print(f"Local logo conversion failed: {title}: {exc}")

    # 1) Exact playlist ID match — safest.
    existing_logos = local_by_id.get(channel_id, set()) if channel_id else set()
    if len(existing_logos) == 1:
        existing_logo = next(iter(existing_logos))
        output.append(force_local(line, existing_logo))
        changed += 1; resolved_from_existing += 1
        continue

    # 2) Name matching is allowed only when it resolves to one unique local logo.
    name_matches = local_by_name.get(base_title, set())
    if len(name_matches) == 1:
        existing_logo = next(iter(name_matches))
        output.append(force_local(line, existing_logo))
        changed += 1; resolved_from_existing += 1
        continue

    fallback = FALLBACK_LOGOS.get(base_title)
    if fallback:
        filename = f"{safe_name(title)}.png"
        target = LOGOS / filename
        replacement = RAW_BASE + filename
        try:
            if not target.exists():
                download_png(fallback, target); downloaded += 1
            output.append(force_local(line, replacement))
            changed += 1; resolved_from_fallback += 1
            local_by_name.setdefault(base_title, set()).add(replacement)
            continue
        except Exception as exc:
            failed += 1
            print(f"Fallback logo failed: {title}: {exc}")

    candidate = None
    cid = metadata.get("tvg-id", "").strip().lower()
    if cid:
        candidate = channel_by_id.get(cid) or channel_by_id.get(cid.split("@", 1)[0])
    if candidate is None:
        # Name fallback is safe only when the catalogue has exactly one identity
        # for that cleaned name. Never silently choose the first ambiguous match.
        candidates_by_name = channel_by_name.get(base_title, [])
        unique_candidates = {str(c.get("id","")).lower(): c for c in candidates_by_name if c.get("id")}
        candidate = next(iter(unique_candidates.values())) if len(unique_candidates) == 1 else None

    if candidate:
        cid = str(candidate.get("id","")).lower()
        logo_item = logo_by_channel.get(cid)
        if logo_item and logo_item[1].get("url"):
            filename = f"{safe_name(title)}.png"
            target = LOGOS / filename
            replacement = RAW_BASE + filename
            try:
                if not target.exists():
                    download_png(logo_item[1]["url"], target); downloaded += 1
                output.append(force_local(line, replacement))
                changed += 1; resolved_from_catalogue += 1
                local_by_name.setdefault(base_title, set()).add(replacement)
                continue
            except Exception as exc:
                failed += 1
                print(f"Catalogue logo failed: {title}: {exc}")

    unresolved.append(title)
    output.append(line)

new_text = "\n".join(output).rstrip() + "\n"
if new_text != original:
    PLAYLIST.write_text(new_text, encoding="utf-8", newline="\n")

print(f"Logo references fixed: {changed}")
print(f"New logos downloaded: {downloaded}")
print(f"Resolved from existing local logos: {resolved_from_existing}")
print(f"Resolved from explicit fallback sources: {resolved_from_fallback}")
print(f"Resolved from IPTV-org catalogue: {resolved_from_catalogue}")
print(f"Local non-PNG logos converted: {converted_local}")
print(f"Logo downloads failed: {failed}")
print(f"Still unresolved: {len(unresolved)}")
for title in unresolved: print(f"UNRESOLVED: {title}")
