#!/usr/bin/env python3
"""Resolve missing/external channel logos and store them as local PNG files."""
import io, json, re, urllib.request
from pathlib import Path
from PIL import Image
try:
    import cairosvg
except ImportError:
    cairosvg = None

PLAYLIST = Path("IPTV Playlist.m3u")
LOGOS = Path("logos")
RAW_BASE = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/"
CHANNELS_API = "https://iptv-org.github.io/api/channels.json"
LOGOS_API = "https://iptv-org.github.io/api/logos.json"
ATTR_RE = re.compile(r'([\w-]+)="([^"]*)"')

FALLBACK_LOGOS = {
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
}

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

local_by_name = {}
for line in lines:
    if not line.startswith("#EXTINF"): continue
    metadata = attrs(line)
    logo = metadata.get("tvg-logo", "").strip()
    if logo and is_local(logo) and logo.lower().endswith(".png"):
        title = metadata.get("tvg-name") or line.rsplit(",", 1)[-1].strip()
        local_by_name.setdefault(clean_name(title), logo)

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
        if key: channel_by_name.setdefault(key, c)

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

    if logo and is_local(logo):
        if logo.lower().endswith(".png"):
            output.append(line)
            continue
        filename = f"{safe_name(title)}.png"
        target = LOGOS / filename
        replacement = RAW_BASE + filename
        try:
            if not target.exists():
                download_png(logo, target); downloaded += 1
            output.append(force_local(line, replacement))
            changed += 1; converted_local += 1
            local_by_name[base_title] = replacement
            continue
        except Exception as exc:
            failed += 1
            print(f"Local logo conversion failed: {title}: {exc}")

    existing_logo = local_by_name.get(base_title)
    if existing_logo:
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
            local_by_name[base_title] = replacement
            continue
        except Exception as exc:
            failed += 1
            print(f"Fallback logo failed: {title}: {exc}")

    candidate = None
    cid = metadata.get("tvg-id", "").strip().lower()
    if cid:
        candidate = channel_by_id.get(cid) or channel_by_id.get(cid.split("@", 1)[0])
    if candidate is None:
        candidate = channel_by_name.get(base_title)

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
                local_by_name[base_title] = replacement
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
