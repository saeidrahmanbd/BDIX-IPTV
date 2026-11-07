#!/usr/bin/env python3
"""Replace three audited IPTV logo defects with sourced channel-brand artwork.

The script is intentionally limited to these three local logo assets. It does
not change stream URLs, channel IDs, grouping or any other playlist metadata.
"""
from __future__ import annotations

from io import BytesIO
from pathlib import Path
from urllib.request import Request, urlopen

from PIL import Image
import cairosvg

ROOT = Path(__file__).resolve().parents[1]
LOGOS = ROOT / "logos"
REPORT = ROOT / "reports" / "logo-repair-2026-11-07.md"

SOURCES = {
    "animal_planet": "https://upload.wikimedia.org/wikipedia/commons/2/20/2018_Animal_Planet_logo.svg",
    "b4u_music": "https://upload.wikimedia.org/wikipedia/commons/7/74/B4U_Music_logo.png",
    "sangeet_bangla": "https://adgully.com/img/800/202108/sangeet-bangla-new-logo.jpeg",
}

def download(url: str, *, referer: str | None = None) -> bytes:
    headers = {"User-Agent": "BDIX-IPTV-Logo-Maintenance/1.0"}
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

    # Animal Planet's 2018 global identity: retain the complete blue elephant
    # and lowercase wordmark, not just the cropped symbol in the old asset.
    animal_svg = download(SOURCES["animal_planet"])
    if b"<svg" not in animal_svg[:1000].lower():
        raise RuntimeError("Animal Planet source is not an SVG.")
    animal_png = cairosvg.svg2png(bytestring=animal_svg, output_width=1200)
    animal = Image.open(BytesIO(animal_png)).convert("RGBA")
    save_png(animal, LOGOS / "animal-planet.png")

    # B4U Music-specific lockup (B4U Media source; Wikimedia file record).
    b4u_data = download(SOURCES["b4u_music"])
    b4u = Image.open(BytesIO(b4u_data)).convert("RGBA")
    if min(b4u.size) < 160:
        raise RuntimeError(f"Unexpectedly small B4U logo: {b4u.size}")
    # Keep the complete square composition and improve display resolution.
    if max(b4u.size) < 600:
        b4u = b4u.resize((600, 600), Image.Resampling.LANCZOS)
    save_png(b4u, LOGOS / "b4u-music.png")

    # Sangeet Bangla's post-August-2021 rebrand artwork. The media mirror has
    # thin page-rule lines at the top/bottom; remove only those outer rows.
    sangeet_data = download(
        SOURCES["sangeet_bangla"],
        referer="https://www.adgully.com/",
    )
    sangeet = Image.open(BytesIO(sangeet_data)).convert("RGB")
    if min(sangeet.size) < 300:
        raise RuntimeError(f"Unexpectedly small Sangeet Bangla logo: {sangeet.size}")
    w, h = sangeet.size
    # Remove the thin horizontal editorial rules without cutting the logo or
    # its Bengali tagline. Keep the white field and full lockup intact.
    margin = max(4, round(h * 0.012))
    sangeet = sangeet.crop((0, margin, w, h - margin))
    save_png(sangeet, LOGOS / "sangeet-bangla.png")

    rows = [
        "# Logo repair — 7 November 2026",
        "",
        "Replaced only three existing local assets. Playlist logo paths, channel IDs, stream URLs and group assignments were not changed.",
        "",
        "| Asset | Source | Notes |",
        "|---|---|---|",
        f"| logos/animal-planet.png | [Wikimedia Commons — 2018 Animal Planet logo.svg]({SOURCES['animal_planet']}) | Global blue-elephant lockup introduced in the 2018 rebrand; converted from SVG to PNG for player compatibility. Commons identifies the artwork as by Animal Planet and classifies the text logo as public domain. |",
        f"| logos/b4u-music.png | [Wikimedia Commons — B4U Music logo.png]({SOURCES['b4u_music']}) | B4U Music-specific artwork; file record attributes source and author to B4U media and records CC BY-SA 4.0. Upscaled with high-quality resampling; no design elements added. |",
        f"| logos/sangeet-bangla.png | [Adgully rebrand image]({SOURCES['sangeet_bangla']}); corroborated by [SVF's 5 November 2021 rebrand release](https://svf.in/press/sangeet-bangla-the-undisputed-pioneer-television-channel-in-bengali-music-entertainment-gets-rebranded/attachment/sb-logho/) | Replaces the pre-2021 logo with the red/black Hullor Hoyejaak lockup. The SVF attachment currently serves a placeholder; the image is taken from Adgully's preserved rebrand coverage. Reuse permission for this rehosted image is not independently established and remains a provenance review item. |",
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
