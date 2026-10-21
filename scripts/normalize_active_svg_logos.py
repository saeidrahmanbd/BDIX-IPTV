#!/usr/bin/env python3
"""Normalize active SVG logos to PNG and replace verified fallback artwork."""
from pathlib import Path
import re
import urllib.request
import cairosvg

ROOT = Path(__file__).resolve().parents[1]
PLAYLISTS = [ROOT / "IPTV-Playlist.m3u", ROOT / "BDIX-Playlist.m3u"]
LOGOS = ROOT / "logos"
RAW_BASE = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/"
ATTR_RE = re.compile(r'(tvg-logo=")([^"]+)(")')

# Exact, channel-specific sources verified from reliable public sources.
FALLBACK_SOURCES = {
    "generated-fallback-alone": "https://commons.wikimedia.org/wiki/Special:FilePath/Alone_(Leftfield_Pictures_TV_series)_logo.svg",
    "generated-fallback-fox-5": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/united-states/us-local/fox-5-wnyw-us.png",
    "generated-fallback-pix-11": "https://commons.wikimedia.org/wiki/Special:FilePath/PIX11_2017.svg",
    "generated-fallback-dd-mizoram": "https://ltsk-cdn.s3.eu-west-1.amazonaws.com/jumpstart/Temp_Live/cdn/HLS/Channel/transparentImages/DD-Mizoram_2000_X_1125_transpharent.png",
    "generated-fallback-a-sports-hd": "https://upload.wikimedia.org/wikipedia/en/0/0c/A_Sports_Logo.png",
    "generated-fallback-t-sports-hd": "https://commons.wikimedia.org/wiki/Special:FilePath/T_Sports_logo.svg",
}

def download(url):
    req = urllib.request.Request(url, headers={"User-Agent": "BDIX-IPTV-logo-maintenance/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read(), r.headers.get_content_type()

def save_png(stem, data, content_type=None):
    out = LOGOS / (stem + ".png")
    if content_type == "image/svg+xml" or data.lstrip().startswith(b"<svg"):
        cairosvg.svg2png(bytestring=data, write_to=str(out), output_width=1024)
    else:
        from PIL import Image
        import io
        img = Image.open(io.BytesIO(data))
        img.save(out, format="PNG")
    return out

def fix_verified_fallbacks(text):
    changed = 0
    fixed = []
    for stem, source in FALLBACK_SOURCES.items():
        # Handle both the original SVG reference and the PNG created by the first normalization pass.
        old_urls = [RAW_BASE + stem + ".svg", RAW_BASE + stem + ".png"]
        if not any(u in text for u in old_urls):
            continue
        try:
            data, ctype = download(source)
            png = save_png(stem, data, ctype)
            new_url = RAW_BASE + png.name
            for old_url in old_urls:
                text = text.replace(old_url, new_url)
            changed += 1
            fixed.append((stem, png.name, source))
        except Exception as exc:
            print(f"WARN: fallback replacement failed for {stem}: {exc}")
    return text, changed, fixed

def convert_active_svgs(text):
    changed = 0
    converted = []
    for match in list(ATTR_RE.finditer(text)):
        url = match.group(2)
        if not url.startswith(RAW_BASE) or not url.lower().endswith(".svg"):
            continue
        name = Path(url.split("?", 1)[0].split("#", 1)[0]).name
        src = LOGOS / name
        if not src.is_file():
            continue
        png = LOGOS / (src.stem + ".png")
        try:
            cairosvg.svg2png(url=str(src), write_to=str(png), output_width=1024)
        except Exception as exc:
            print(f"WARN: SVG conversion failed for {name}: {exc}")
            continue
        text = text.replace(url, RAW_BASE + png.name)
        changed += 1
        converted.append((name, png.name))
    return text, changed, converted

def main():
    total_svg = 0
    total_fallback = 0
    for playlist in PLAYLISTS:
        if not playlist.exists():
            continue
        text = playlist.read_text(encoding="utf-8")
        before = text
        # Fallback repair MUST happen before generic SVG conversion, otherwise the
        # original generated-fallback SVG URL disappears before its source mapping runs.
        text, n_fallback, fixed = fix_verified_fallbacks(text)
        text, n_svg, converted = convert_active_svgs(text)
        if text != before:
            playlist.write_text(text, encoding="utf-8", newline="\n")
        total_svg += n_svg
        total_fallback += n_fallback
        print(f"{playlist.name}: fallback_fixed={n_fallback} converted_svg={n_svg}")
        for x in fixed:
            print(f"  FALLBACK->VERIFIED: {x[0]} -> {x[1]} source={x[2]}")
        for x in converted:
            print(f"  SVG->PNG: {x[0]} -> {x[1]}")
    print(f"TOTAL fallback_fixed={total_fallback} converted_svg={total_svg}")

if __name__ == "__main__":
    main()
