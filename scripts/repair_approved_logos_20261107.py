#!/usr/bin/env python3
"""Replace three audited IPTV logo defects with sourced channel-brand artwork.

The script is limited to these three local logo assets. It does not change
stream URLs, channel IDs, grouping or any other playlist metadata.
"""
from __future__ import annotations

from io import BytesIO
from pathlib import Path
from urllib.request import Request, urlopen

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
LOGOS = ROOT / "logos"
REPORT = ROOT / "reports" / "logo-repair-2026-11-07.md"

SOURCES = {
    # Full 2018 Animal Planet lockup (blue elephant + black wordmark).
    "animal_planet": "https://static.cdnlogo.com/logos/a/74/animal-planet.png",
    "b4u_music": "https://upload.wikimedia.org/wikipedia/commons/7/74/B4U_Music_logo.png",
    "sangeet_bangla": "https://adgully.com/img/800/202108/sangeet-bangla-new-logo.jpeg",
}

def download(url: str, *, referer: str | None = None) -> bytes:
    headers = {"User-Agent": "BDIX-IPTV-Logo-Maintenance/1.1"}
    if referer:
        headers["Referer"] = referer
    request = Request(url, headers=headers)
    with urlopen(request, timeout=45) as response:
        data = response.read()
        if response.status != 200 or not data:
            raise RuntimeError(f"Could not download source asset: {url}")
        return data

def save_png(image: Image.Image, path: Path) -> None:
    image.save(path, format="PNG", optimize=True)
    check = Image.open(path)
    check.verify()
    if check.format != "PNG":
        raise RuntimeError(f"Invalid PNG output: {path}")

def main() -> None:
    LOGOS.mkdir(parents=True, exist_ok=True)
    REPORT.parent.mkdir(parents=True, exist_ok=True)

    # Full Animal Planet wordmark; require dark lettering as well as the blue
    # symbol so a symbol-only file cannot silently pass this repair again.
    animal_data = download(SOURCES["animal_planet"])
    animal = Image.open(BytesIO(animal_data)).convert("RGBA")
    if min(animal.size) < 300:
        raise RuntimeError(f"Unexpectedly small Animal Planet logo: {animal.size}")
    rgb = animal.convert("RGB")
    dark_pixels = sum(1 for pixel in rgb.getdata() if max(pixel) < 90)
    if dark_pixels < 1500:
        raise RuntimeError("Animal Planet source appears to lack the black wordmark.")
    if max(animal.size) < 900:
        ratio = 900 / max(animal.size)
        animal = animal.resize(
            (round(animal.width * ratio), round(animal.height * ratio)),
            Image.Resampling.LANCZOS,
        )
    save_png(animal, LOGOS / "animal-planet.png")

    # B4U Music-specific lockup (B4U Media source; Wikimedia file record).
    b4u_data = download(SOURCES["b4u_music"])
    b4u = Image.open(BytesIO(b4u_data)).convert("RGBA")
    if min(b4u.size) < 160:
        raise RuntimeError(f"Unexpectedly small B4U logo: {b4u.size}")
    if max(b4u.size) < 600:
        b4u = b4u.resize((600, 600), Image.Resampling.LANCZOS)
    save_png(b4u, LOGOS / "b4u-music.png")

    # Sangeet Bangla's post-August-2021 rebrand artwork. Remove the thin
    # editorial frame by detecting the near-full-width/height black rule.
    sangeet_data = download(
        SOURCES["sangeet_bangla"],
        referer="https://www.adgully.com/",
    )
    sangeet = Image.open(BytesIO(sangeet_data)).convert("RGB")
    if min(sangeet.size) < 300:
        raise RuntimeError(f"Unexpectedly small Sangeet Bangla logo: {sangeet.size}")
    gray = ImageOps.grayscale(sangeet)
    w, h = sangeet.size
    row_lines = [
        y for y in range(h)
        if sum(gray.getpixel((x, y)) < 70 for x in range(w)) >= int(w * 0.78)
    ]
    col_lines = [
        x for x in range(w)
        if sum(gray.getpixel((x, y)) < 70 for y in range(h)) >= int(h * 0.78)
    ]
    if len(row_lines) < 2 or len(col_lines) < 2:
        raise RuntimeError("Could not confidently detect Sangeet Bangla editorial frame.")
    top, bottom = min(row_lines), max(row_lines)
    left, right = min(col_lines), max(col_lines)
    pad = 5
    if bottom - top < h * 0.65 or right - left < w * 0.65:
        raise RuntimeError("Sangeet Bangla frame detection produced an unsafe crop.")
    sangeet = sangeet.crop((left + pad, top + pad, right - pad + 1, bottom - pad + 1))
    save_png(sangeet, LOGOS / "sangeet-bangla.png")

    rows = [
        "# Logo repair — 7 November 2026",
        "",
        "Replaced only three existing local assets. Playlist logo paths, channel IDs, stream URLs and group assignments were not changed.",
        "",
        "| Asset | Source | Notes |",
        "|---|---|---|",
        f"| logos/animal-planet.png | [Full Animal Planet wordmark — CDNLogo](https://cdnlogo.com/logo/animal-planet_38748.html) | Full blue-elephant plus black lowercase wordmark; the source's dark lettering is checked before saving. The identity itself is corroborated by the official brand designer's [Animal Planet project](https://cghnyc.com/work/project/animal-planet). Third-party asset provenance/licensing remains subject to review. |",
        f"| logos/b4u-music.png | [Wikimedia Commons — B4U Music logo.png]({SOURCES['b4u_music']}) | B4U Music-specific artwork; file record attributes source and author to B4U media and records CC BY-SA 4.0. Upscaled with high-quality resampling; no design elements added. |",
        f"| logos/sangeet-bangla.png | [Adgully rebrand image]({SOURCES['sangeet_bangla']}); corroborated by [SVF's 5 November 2021 rebrand release](https://svf.in/press/sangeet-bangla-the-undisputed-pioneer-television-channel-in-bengali-music-entertainment-gets-rebranded/attachment/sb-logho/) | Post-2021 red/black Hullor Hoyejaak lockup, with editorial frame removed. The SVF attachment currently serves a placeholder; this image is taken from Adgully's preserved rebrand coverage. Reuse permission for this rehosted image is not independently established and remains a provenance review item. |",
        "",
        "The assets are stored locally under logos/; no playlist entry points to an external image URL.",
        "",
    ]
    REPORT.write_text("\n".join(rows), encoding="utf-8")

    for path in (
        LOGOS / "animal-planet.png",
        LOGOS / "b4u-music.png",
        LOGOS / "sangeet-bangla.png",
    ):
        image = Image.open(path)
        print(f"{path.relative_to(ROOT)}: {image.size[0]}x{image.size[1]} PNG, {path.stat().st_size} bytes")

if __name__ == "__main__":
    main()
