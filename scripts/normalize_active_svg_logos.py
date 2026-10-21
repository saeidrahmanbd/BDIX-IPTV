#!/usr/bin/env python3
"""Normalize active SVG logos to PNG and replace only verified fallback artwork."""
from pathlib import Path
import re
import urllib.request
import hashlib
import cairosvg

ROOT = Path(__file__).resolve().parents[1]
PLAYLISTS = [ROOT / "IPTV-Playlist.m3u", ROOT / "BDIX-Playlist.m3u"]
LOGOS = ROOT / "logos"
RAW_BASE = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/"
ATTR_RE = re.compile(r'(tvg-logo=")([^"]+)(")')

# Exact, channel-specific sources verified from reliable public sources.
FALLBACK_SOURCES = {
    "generated-fallback-alone.svg": "https://commons.wikimedia.org/wiki/Special:FilePath/Alone_(Leftfield_Pictures_TV_series)_logo.svg",
    "generated-fallback-fox-5.svg": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/united-states/us-local/fox-5-wnyw-us.png",
    "generated-fallback-pix-11.svg": "https://commons.wikimedia.org/wiki/Special:FilePath/PIX11_2017.svg",
    "generated-fallback-dd-mizoram.svg": "https://ltsk-cdn.s3.eu-west-1.amazonaws.com/jumpstart/Temp_Live/cdn/HLS/Channel/transparentImages/DD-Mizoram_2000_X_1125_transpharent.png",
    "generated-fallback-a-sports-hd.svg": "https://upload.wikimedia.org/wikipedia/en/0/0c/A_Sports_Logo.png",
    "generated-fallback-t-sports-hd.svg": "https://commons.wikimedia.org/wiki/Special:FilePath/T_Sports_logo.svg",
}

def download(url):
    req = urllib.request.Request(url, headers={"User-Agent": "BDIX-IPTV-logo-maintenance/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read(), r.headers.get_content_type()

def save_png(name, data, content_type=None):
    out = LOGOS / (Path(name).stem + ".png")
    if content_type == "image/svg+xml" or data.lstrip().startswith(b"<svg"):
        cairosvg.svg2png(bytestring=data, write_to=str(out), output_width=1024)
    else:
        # Convert raster source to PNG through Pillow, preserving transparency where possible.
        from PIL import Image
        import io
        img = Image.open(io.BytesIO(data))
        img.save(out, format="PNG")
    return out

def local_name(url):
    return Path(url.split("?", 1)[0].split("#", 1)[0]).name

def convert_active_svgs(text):
    changed = 0
    converted = []
    for match in list(ATTR_RE.finditer(text)):
        url = match.group(2)
        if not url.startswith(RAW_BASE) or not url.lower().endswith(".svg"):
            continue
        name = local_name(url)
        src = LOGOS / name
        if not src.is_file():
            continue
        png = LOGOS / (src.stem + ".png")
        try:
            cairosvg.svg2png(url=str(src), write_to=str(png), output_width=1024)
        except Exception as exc:
            print(f"WARN: SVG conversion failed for {name}: {exc}")
            continue
        new_url = RAW_BASE + png.name
        text = text.replace(url, new_url)
        changed += 1
        converted.append((name, png.name))
    return text, changed, converted

def fix_verified_fallbacks(text):
    changed = 0
    fixed = []
    for old_name, source in FALLBACK_SOURCES.items():
        old_url = RAW_BASE + old_name
        if old_url not in text:
            continue
        try:
            data, ctype = download(source)
            png = save_png(old_name, data, ctype)
            new_url = RAW_BASE + png.name
            text = text.replace(old_url, new_url)
            changed += 1
            fixed.append((old_name, png.name, source))
        except Exception as exc:
            print(f"WARN: fallback replacement failed for {old_name}: {exc}")
    return text, changed, fixed

def main():
    total_svg = 0
    total_fallback = 0
    for playlist in PLAYLISTS:
        if not playlist.exists():
            continue
        text = playlist.read_text(encoding="utf-8")
        before = text
        text, n_svg, converted = convert_active_svgs(text)
        text, n_fallback, fixed = fix_verified_fallbacks(text)
        if text != before:
            playlist.write_text(text, encoding="utf-8", newline="\n")
        total_svg += n_svg
        total_fallback += n_fallback
        print(f"{playlist.name}: converted_svg={n_svg} fallback_fixed={n_fallback}")
        for x in converted:
            print(f"  SVG->PNG: {x[0]} -> {x[1]}")
        for x in fixed:
            print(f"  FALLBACK->VERIFIED: {x[0]} -> {x[1]} source={x[2]}")
    print(f"TOTAL converted_svg={total_svg} fallback_fixed={total_fallback}")

if __name__ == "__main__":
    main()
