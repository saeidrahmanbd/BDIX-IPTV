#!/usr/bin/env python3
"""Convert every supported image under logos/ to validated PNG files.

Playlist tvg-logo references are updated without changing any other metadata.
After every PNG and playlist update is validated, non-PNG source files are
removed from logos/; Git history remains the rollback/provenance source.
"""
from __future__ import annotations

import hashlib
import io
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote, unquote

import cairosvg
from PIL import Image, ImageOps

import repair_playlist_logos as logo_repair
from logo_embedded_png import DATA_URI, recover_embedded_png_from_svg

ROOT = Path(__file__).resolve().parents[1]
LOGOS = ROOT / "logos"
PLAYLISTS = ("IPTV-Playlist.m3u", "International-Playlist.m3u")
RAW_BASE = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/"
REPORT = ROOT / "reports" / "logo-format-conversion.md"
# Every raster/vector logo asset is normalized to PNG. Original files remain as
# rollback/provenance sources; all active playlist metadata points to PNG.
CONVERTIBLE_EXTENSIONS = {
    ".jpg", ".jpeg", ".webp", ".svg", ".avif", ".gif", ".bmp", ".tif", ".tiff", ".ico",
}
BLOCKED_OUTPUT_NAMES = set(logo_repair.BAD_ASSETS | logo_repair.GENERIC_ASSETS) | {
    "atn-news.png", "a-sports-5485adff.png", "a-sports-hd.png", "bein-sports-3.png",
    "bangla-tv.png", "btv-news.png", "colors.png", "duronto-tv.png",
    "duronto-tv-1ad55c95.png", "ekushey-tv.png", "global-tv.png", "green-tv.png",
    "mohona-tv.png", "nagorik-tv.png", "nagorik.png", "nick-bangla.png",
    "sananda-tv.png", "sananda.png", "star-gold-select.png", "star-gold.png",
    "star-plus.png", "zee-tv.png", "tom-and-jerry.png", "arirang-tv.png",
}
LOGO_RE = re.compile(r'tvg-logo="([^"]*)"')


def without_logo_attributes(text: str) -> str:
    return re.sub(r'\s+tvg-logo="[^"]*"', "", text)


def image_bytes_to_png(raw: bytes, source_extension: str) -> bytes:
    """Decode a local raster/vector logo and emit a normalized PNG."""
    extension = source_extension.casefold()
    if extension == ".svg":
        svg = raw.decode("utf-8", errors="strict")
        if re.search(r"<\s*script\b|<\s*foreignObject\b|javascript:", svg, re.I):
            raise ValueError("unsafe SVG content")
        if re.search(r"""(?:href|src)\s*=\s*["']\s*(?:https?:|file:|//)""", svg, re.I) or re.search(r"""url\(\s*["']?\s*(?:https?:|file:|//)""", svg, re.I):
            raise ValueError("SVG contains an external resource reference")
        try:
            raw = cairosvg.svg2png(bytestring=raw, output_width=1024)
        except Exception as render_error:
            # Repair only narrowly defined embedded-PNG CRC/IEND defects.
            recovered = recover_embedded_png_from_svg(raw)
            if recovered is None:
                raise ValueError(
                    f"SVG rendering failed and no safely recoverable embedded PNG was found: "
                    f"{type(render_error).__name__}: {render_error}"
                ) from render_error
            try:
                with Image.open(io.BytesIO(recovered)) as embedded:
                    embedded.load()
            except Exception as embedded_error:
                raise ValueError(
                    f"SVG rendering failed; recovered embedded PNG did not decode: "
                    f"{type(embedded_error).__name__}: {embedded_error}"
                ) from render_error
            # When an SVG is only a wrapper around an embedded PNG, CairoSVG
            # may reject a damaged ancillary/IDAT CRC even though the embedded
            # pixel stream is recoverable. Use the fully decoded, structurally
            # repaired raster directly instead of asking CairoSVG to decode it
            # a second time. The common downstream Pillow path normalizes it.
            raw = recovered

    try:
        with Image.open(io.BytesIO(raw)) as source_image:
            source_image.seek(0)
            image = ImageOps.exif_transpose(source_image)
            image.load()
            if image.width < 1 or image.height < 1:
                raise ValueError("image has invalid dimensions")
            image.thumbnail((1024, 1024), Image.Resampling.LANCZOS)
            if image.mode in ("RGBA", "LA") or "transparency" in image.info:
                image = image.convert("RGBA")
            else:
                image = image.convert("RGB")
            output = io.BytesIO()
            image.save(output, format="PNG", optimize=True)
            png = output.getvalue()
    except Exception as exc:
        raise ValueError(f"cannot decode {extension} logo: {type(exc).__name__}: {exc}") from exc

    if not png.startswith(b"\x89PNG\r\n\x1a\n"):
        raise ValueError("PNG encoder returned invalid bytes")
    with Image.open(io.BytesIO(png)) as check:
        check.verify()
    return png


def local_logo_path(logo: str, raw_base: str) -> tuple[str, str]:
    """Return (relative path, URL prefix style) for a repository-local logo."""
    if logo.startswith(raw_base):
        relative = unquote(logo[len(raw_base):].split("?", 1)[0].split("#", 1)[0])
        return relative, "raw"
    if logo.startswith("logos/"):
        return unquote(logo[len("logos/"):]), "relative"
    raise ValueError(f"external or unsupported logo reference: {logo[:160]}")


def _safe_logo_file(root: Path, relative: str) -> Path:
    if not relative or relative.startswith(("/", "\\")):
        raise ValueError("empty or absolute logo path")
    candidate = (root / "logos" / Path(relative)).resolve()
    try:
        candidate.relative_to((root / "logos").resolve())
    except ValueError as exc:
        raise ValueError("logo path escapes the logos directory") from exc
    if not candidate.is_file():
        raise FileNotFoundError(f"referenced local logo is missing: {relative}")
    return candidate


def convert_referenced_logos(
    root: Path = ROOT,
    playlist_names: tuple[str, ...] = PLAYLISTS,
    raw_base: str = RAW_BASE,
    report_path: Path | None = None,
) -> dict:
    root = Path(root).resolve()
    logos_dir = root / "logos"
    asset_cache: dict[str, tuple[str, bytes]] = {}
    pending_assets: dict[Path, bytes] = {}
    source_files_to_remove: set[Path] = set()
    updated_playlists: dict[Path, str] = {}
    source_formats: dict[str, int] = {}
    updated_references = 0

    def convert_one(relative: str) -> str:
        if relative in asset_cache:
            return asset_cache[relative][0]
        source_path = _safe_logo_file(root, relative)
        extension = source_path.suffix.casefold()
        if extension == ".png":
            asset_cache[relative] = (relative, source_path.read_bytes())
            return relative
        if extension not in CONVERTIBLE_EXTENSIONS:
            raise ValueError(f"unsupported referenced logo format {extension}: {relative}")

        try:
            png_bytes = image_bytes_to_png(source_path.read_bytes(), extension)
            source_files_to_remove.add(source_path)
        except Exception as exc:
            raise ValueError(
                f"failed to convert logo {relative}: {type(exc).__name__}: {exc}"
            ) from exc
        digest = hashlib.sha256(png_bytes).hexdigest()[:10]
        target = source_path.with_suffix(".png")
        if (
            target.name.casefold() in BLOCKED_OUTPUT_NAMES
            or (target.exists() and target.read_bytes() != png_bytes)
        ):
            target = source_path.with_name(f"{source_path.stem}-converted-{digest}.png")
        if target.exists():
            if target.read_bytes() != png_bytes:
                raise ValueError(f"PNG target collision for {relative}")
        else:
            pending_assets[target] = png_bytes
        new_relative = target.relative_to(logos_dir).as_posix()
        asset_cache[relative] = (new_relative, png_bytes)
        source_formats[extension.lstrip(".")] = source_formats.get(extension.lstrip("."), 0) + 1
        return new_relative

    # Normalize the complete logos/ image inventory, including assets not
    # currently referenced by either playlist. Non-image files (README, etc.)
    # and existing PNGs are left untouched.
    inventory_image_assets = 0
    for source_path in sorted(logos_dir.rglob("*")):
        if not source_path.is_file() or source_path.suffix.casefold() not in CONVERTIBLE_EXTENSIONS:
            continue
        inventory_image_assets += 1
        relative = source_path.relative_to(logos_dir).as_posix()
        convert_one(relative)

    for playlist_name in playlist_names:
        playlist_path = root / playlist_name
        with playlist_path.open("r", encoding="utf-8", newline="") as stream:
            original = stream.read()
        references_changed = 0

        def replace_logo(match: re.Match) -> str:
            nonlocal references_changed
            logo = match.group(1).strip()
            if not logo:
                return match.group(0)
            relative, style = local_logo_path(logo, raw_base)
            if Path(relative).suffix.casefold() == ".png":
                return match.group(0)
            converted_relative = convert_one(relative)
            if converted_relative == relative:
                return match.group(0)
            encoded = quote(converted_relative, safe="/-._~")
            new_logo = raw_base + encoded if style == "raw" else "logos/" + encoded
            references_changed += 1
            return f'tvg-logo="{new_logo}"'

        updated = LOGO_RE.sub(replace_logo, original)
        if without_logo_attributes(updated) != without_logo_attributes(original):
            raise RuntimeError(f"non-logo playlist content changed: {playlist_name}")
        updated_playlists[playlist_path] = updated
        updated_references += references_changed

    # All sources and all conversions are validated before any file is written.
    for target, png_bytes in pending_assets.items():
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(png_bytes)
        with Image.open(target) as image:
            image.verify()
        if not target.read_bytes().startswith(b"\x89PNG\r\n\x1a\n"):
            raise ValueError(f"written asset is not PNG: {target}")

    for playlist_path, updated in updated_playlists.items():
        with playlist_path.open("r", encoding="utf-8", newline="") as stream:
            current = stream.read()
        if updated != current:
            with playlist_path.open("w", encoding="utf-8", newline="") as stream:
                stream.write(updated)

    # Remove originals only after all generated PNGs and playlist writes validate.
    # Git history preserves the exact original bytes for rollback/provenance.
    removed_source_count = 0
    for source_path in sorted(source_files_to_remove):
        source_path.unlink()
        removed_source_count += 1

    converted_count = sum(source_formats.values())
    remaining_non_png = 0
    for updated in updated_playlists.values():
        for match in LOGO_RE.finditer(updated):
            logo = match.group(1).strip()
            if logo:
                relative, _style = local_logo_path(logo, raw_base)
                if Path(relative).suffix.casefold() != ".png":
                    remaining_non_png += 1
    if remaining_non_png:
        raise RuntimeError(f"non-PNG logo references remain after conversion: {remaining_non_png}")
    summary = {
        "playlists": list(playlist_names),
        "unique_assets_converted": converted_count,
        "inventory_image_assets": inventory_image_assets,
        "updated_references": updated_references,
        "source_formats": dict(sorted(source_formats.items())),
        "png_assets_created": len(pending_assets),
        "original_assets_removed": removed_source_count,
        "remaining_non_png_references": remaining_non_png,
    }
    if report_path is None:
        report_path = root / "reports" / "logo-format-conversion.md"
    report_path = Path(report_path)
    if converted_count:
        report_path.parent.mkdir(parents=True, exist_ok=True)
        lines = [
            "# Logo Format Conversion",
            "",
            f"Generated: **{datetime.now(timezone.utc).isoformat()}**",
            "",
            f"- Playlists checked: **{', '.join(playlist_names)}**",
            f"- Unique non-PNG assets converted: **{converted_count}**",
            f"- Playlist logo references updated: **{updated_references}**",
            f"- New PNG assets created: **{len(pending_assets)}**",
            f"- Supported non-PNG image assets found in logos/: **{inventory_image_assets}**",
            f"- Non-PNG source files removed after successful validation: **{removed_source_count}**",
            "- Rollback/provenance: **Original bytes remain recoverable from Git history**",
            "- Non-PNG active playlist references remaining: **0**",
            "",
            "Every supported image asset under logos/ was converted to a validated PNG. Active local tvg-logo metadata was updated to PNG paths. Non-PNG source files were removed only after successful conversion and playlist validation; their exact originals remain recoverable from Git history. Channel rows, stream URLs, IDs, groups, and channel numbers were preserved.",
            "",
            "## Source formats",
            "",
        ]
        lines.extend(f"- {extension.upper()}: **{count}**" for extension, count in sorted(source_formats.items()))
        report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return summary


def main() -> int:
    summary = convert_referenced_logos()
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
