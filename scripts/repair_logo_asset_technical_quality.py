#!/usr/bin/env python3
"""Audit and safely repair logo file formats and excessive raster dimensions.

This tool never changes logo names, playlist references, stream URLs, or source
attribution. A raster file with a misleading extension is re-encoded to match
its existing extension when that conversion is safe. Images wider/taller than
the configured maximum are downscaled with aspect ratio preserved.
"""
import argparse
import hashlib
import re
import tempfile
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

from PIL import Image, ImageOps

LOGOS = Path("logos")
PLAYLISTS = ("IPTV-Playlist.m3u", "BDIX-Playlist.m3u", "International-Playlist.m3u")
REPORT = Path("reports/logo-asset-quality-audit.md")
ATTR_RE = re.compile(r'([\w-]+)="([^"]*)"')
DEFAULT_MAX_DIMENSION = 1600
DEFAULT_MAX_BYTES = 500 * 1024
EXPECTED_FORMAT = {
    ".png": "PNG",
    ".jpg": "JPEG",
    ".jpeg": "JPEG",
    ".webp": "WEBP",
    ".avif": "AVIF",
}


def attrs(line):
    return dict(ATTR_RE.findall(line))


def playlist_logo_refs():
    refs = defaultdict(set)
    active = defaultdict(set)
    review_groups = {"backup", "not playing", "not playing...", "not playing…"}
    for playlist in PLAYLISTS:
        path = Path(playlist)
        if not path.is_file():
            continue
        for line in path.read_text(encoding="utf-8-sig", errors="replace").splitlines():
            if not line.startswith("#EXTINF:"):
                continue
            meta = attrs(line)
            logo = meta.get("tvg-logo", "").strip()
            if not logo:
                continue
            filename = Path(urlsplit(logo).path).name
            if not filename:
                continue
            refs[filename].add(playlist)
            if meta.get("group-title", "").strip().casefold() not in review_groups:
                active[filename].add(playlist)
    return refs, active


def _save_image(image, path, fmt):
    info = {}
    if image.info.get("icc_profile"):
        info["icc_profile"] = image.info["icc_profile"]
    if fmt == "PNG":
        image.save(path, format="PNG", optimize=True, **info)
    elif fmt == "JPEG":
        if image.mode not in ("RGB", "L"):
            if "A" in image.getbands() and image.getchannel("A").getextrema() != (255, 255):
                raise ValueError("alpha channel cannot be safely represented by JPEG")
            image = image.convert("RGB")
        image.save(path, format="JPEG", quality=92, optimize=True, progressive=True, **info)
    elif fmt == "WEBP":
        image.save(path, format="WEBP", quality=92, method=6, **info)
    elif fmt == "AVIF":
        image.save(path, format="AVIF", quality=90, **info)
    else:
        raise ValueError(f"unsupported encoder: {fmt}")


def repair_one(path, fix=False, max_dimension=DEFAULT_MAX_DIMENSION, max_bytes=DEFAULT_MAX_BYTES):
    """Assess an image and optionally repair format, dimensions, or excessive byte size."""
    path = Path(path)
    try:
        size_before = path.stat().st_size
    except OSError as exc:
        size_before = 0
        return {"path": path.as_posix(), "format_before": "", "format_expected": EXPECTED_FORMAT.get(path.suffix.lower(), ""),
                "width_before": 0, "height_before": 0, "format_mismatch": False, "oversized": False,
                "large": False, "format_repaired": False, "resized": False, "compressed": False,
                "bytes_before": 0, "bytes_after": 0, "error": str(exc)}
    result = {
        "path": path.as_posix(),
        "format_before": "",
        "format_expected": EXPECTED_FORMAT.get(path.suffix.lower(), ""),
        "width_before": 0,
        "height_before": 0,
        "format_mismatch": False,
        "oversized": False,
        "large": size_before > max_bytes,
        "format_repaired": False,
        "resized": False,
        "compressed": False,
        "bytes_before": size_before,
        "bytes_after": size_before,
        "error": "",
    }
    if path.suffix.lower() == ".svg":
        try:
            content = path.read_text(encoding="utf-8", errors="ignore")[:20000].lower()
            if "<svg" not in content:
                result["error"] = "invalid or unreadable SVG"
        except OSError as exc:
            result["error"] = str(exc)
        return result
    if path.suffix.lower() not in EXPECTED_FORMAT:
        return result

    try:
        with Image.open(path) as source:
            source.load()
            fmt = (source.format or "").upper()
            width, height = source.size
            result.update(
                format_before=fmt,
                width_before=width,
                height_before=height,
                format_mismatch=bool(fmt and fmt != result["format_expected"]),
                oversized=max(width, height) > max_dimension,
            )
            target_fmt = result["format_expected"]
            needs_format = result["format_mismatch"]
            needs_resize = result["oversized"]
            needs_compress = size_before > max_bytes
            if not fix or not (needs_format or needs_resize or needs_compress):
                return result

            working = ImageOps.exif_transpose(source.copy())
            if needs_resize:
                ratio = max_dimension / max(working.size)
                new_size = (
                    max(1, round(working.width * ratio)),
                    max(1, round(working.height * ratio)),
                )
                working = working.resize(new_size, Image.Resampling.LANCZOS)

            # First try a high-quality, same-size re-encode. If the file remains
            # above the byte budget, shrink in small steps until it fits or the
            # image is already too small to downscale responsibly.
            original_size = size_before
            candidate = working
            accepted = False
            output_format = target_fmt or fmt
            for attempt in range(12):
                temp_path = None
                try:
                    with tempfile.NamedTemporaryFile(
                        prefix=path.stem + "-", suffix=path.suffix, dir=path.parent, delete=False
                    ) as tmp:
                        temp_path = Path(tmp.name)
                    _save_image(candidate, temp_path, output_format)
                    with Image.open(temp_path) as check:
                        check.load()
                        if (check.format or "").upper() != output_format:
                            raise ValueError(f"encoder wrote {check.format}, expected {output_format}")
                    output_size = temp_path.stat().st_size
                    force_repair = needs_format or needs_resize
                    smaller = output_size < original_size
                    within_budget = output_size <= max_bytes
                    last_attempt = attempt == 11 or min(candidate.size) <= 96
                    if force_repair or smaller or within_budget:
                        if within_budget or not needs_compress or last_attempt:
                            temp_path.replace(path)
                            result["format_repaired"] = needs_format
                            result["resized"] = needs_resize or candidate.size != source.size
                            result["compressed"] = output_size < original_size
                            result["bytes_after"] = output_size
                            accepted = True
                            break
                finally:
                    if temp_path is not None and temp_path.exists():
                        temp_path.unlink()

                if attempt == 11 or min(candidate.size) <= 96:
                    break
                ratio = min(0.90, max(0.70, (max_bytes / max(1, output_size)) ** 0.5 * 0.95))
                new_size = (
                    max(1, round(candidate.width * ratio)),
                    max(1, round(candidate.height * ratio)),
                )
                if new_size == candidate.size:
                    break
                candidate = candidate.resize(new_size, Image.Resampling.LANCZOS)

            if needs_compress and not accepted and result["bytes_after"] > max_bytes:
                result["error"] = f"could not reduce asset below {max_bytes} bytes without excessive downscaling"

            with Image.open(path) as check:
                check.load()
                result["width_after"], result["height_after"] = check.size
                result["format_after"] = (check.format or "").upper()
                result["format_mismatch"] = result["format_after"] != target_fmt
                result["oversized"] = max(check.size) > max_dimension
                result["bytes_after"] = path.stat().st_size
                result["large"] = result["bytes_after"] > max_bytes
    except Exception as exc:
        result["error"] = str(exc)
    return result


def slug(value):
    value = str(value or "").casefold()
    value = re.sub(r"\b(hd|sd|uhd|fhd|4k|tv|channel)\b", " ", value)
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-")


def clean_asset_stem(value):
    stem = Path(value).stem.casefold()
    stem = re.sub(r"^(nvisionbd-verified-|nvisionbd-official-|local-logo-|generated-fallback-)", "", stem)
    stem = re.sub(r"-[a-f0-9]{8,}$", "", stem)
    stem = re.sub(r"-\d{3,4}p(?:-[a-f0-9]{8,})?$", "", stem)
    stem = re.sub(r"-custom$", "", stem)
    return stem.strip("-")


def sha256_file(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fix", action="store_true", help="apply safe extension and dimension repairs")
    parser.add_argument("--max-dimension", type=int, default=DEFAULT_MAX_DIMENSION)
    parser.add_argument("--max-bytes", type=int, default=DEFAULT_MAX_BYTES, help="target maximum file size for raster assets; oversized files are re-encoded and downscaled cautiously")
    args = parser.parse_args()
    if args.max_dimension < 256:
        raise SystemExit("--max-dimension must be at least 256 pixels")
    if args.max_bytes < 64 * 1024:
        raise SystemExit("--max-bytes must be at least 65536 bytes")
    if not LOGOS.is_dir():
        raise SystemExit("logos directory is missing")

    logo_files = sorted(path for path in LOGOS.rglob("*") if path.is_file())
    first_pass = [repair_one(path, fix=args.fix, max_dimension=args.max_dimension, max_bytes=args.max_bytes) for path in logo_files]
    refs, active_refs = playlist_logo_refs()
    # Reassess assets after a possible repair, so the final issues section reflects disk state.
    final = [repair_one(path, fix=False, max_dimension=args.max_dimension, max_bytes=args.max_bytes) for path in logo_files]
    file_by_name = defaultdict(list)
    for path in logo_files:
        file_by_name[path.name].append(path)

    mismatches = [item for item in final if item["format_mismatch"]]
    oversized = [item for item in final if item["oversized"]]
    large_assets = [item for item in final if item["bytes_before"] > args.max_bytes]
    small = [item for item in final if item["width_before"] and min(item["width_before"], item["height_before"]) < 64]
    errors = [item for item in final if item["error"]]
    duplicate_assets = defaultdict(list)
    for path in logo_files:
        try:
            digest = sha256_file(path)
            duplicate_assets[digest].append(path.as_posix().replace("\\", "/"))
        except OSError:
            continue
    duplicate_groups = [sorted(values) for values in duplicate_assets.values() if len(set(values)) > 1]
    used_filenames = set(refs)
    unreferenced_root = [path for path in logo_files if path.parent == LOGOS and path.name not in used_filenames]
    naming_mismatches = []
    for playlist in PLAYLISTS:
        path = Path(playlist)
        if not path.is_file():
            continue
        for line in path.read_text(encoding="utf-8-sig", errors="replace").splitlines():
            if not line.startswith("#EXTINF:"):
                continue
            meta = attrs(line)
            logo = Path(urlsplit(meta.get("tvg-logo", "")).path).name
            name = meta.get("tvg-name", "").strip()
            if logo and name and clean_asset_stem(logo) != slug(name):
                naming_mismatches.append((playlist, name, logo, meta.get("group-title", "").strip()))

    changed = [item for item in first_pass if item["format_repaired"] or item["resized"] or item["compressed"]]
    lines = [
        "# Logo Asset Technical Quality Audit", "",
        f"Generated: **{datetime.now(timezone.utc).isoformat(timespec='seconds')}**", "",
        "This audit checks technical image encoding, dimensions, exact-byte duplicate assets, filename conventions and playlist references. Identical bytes or a non-slug filename are review signals, not proof that a logo is wrong.", "",
        "## Source playlist fingerprints", "",
    ]
    for playlist in PLAYLISTS:
        path = Path(playlist)
        if path.is_file():
            lines.append(f"- {playlist} SHA-256: **{sha256_file(path)}**")
    lines += [
        "", "## Summary", "",
        f"- Safe repairs applied this run: **{len(changed)}**" if args.fix else f"- Safe repairs applied this run: **0 (read-only mode)**",
        f"- File-format/extension mismatches remaining: **{len(mismatches)}**",
        f"- Raster assets still oversized (max side > {args.max_dimension}px): **{len(oversized)}**",
        f"- Raster assets over {args.max_bytes} bytes: **{len(large_assets)}**",
        f"- Raster/SVG assets with short side under 64 px: **{len(small)}**",
        f"- Exact-byte duplicate asset clusters: **{len(duplicate_groups)}**",
        f"- Playlist references whose asset stem differs from the normalized channel name: **{len(naming_mismatches)}**",
        f"- Unreferenced files immediately inside logos/: **{len(unreferenced_root)}** (not deleted; other tooling or playlists may use them)",
        f"- Technical read/repair errors: **{len(errors)}**",
        "", "## Safe repairs applied", "",
        "| Asset | Format before | Format after | Dimensions before | Dimensions after | Repair |",
        "|---|---|---|---:|---:|---|",
    ]
    if changed:
        for item in changed:
            path = Path(item["path"])
            after_format = item.get("format_after", item.get("format_before", ""))
            after_width = item.get("width_after", item["width_before"])
            after_height = item.get("height_after", item["height_before"])
            action = ", ".join(name for flag, name in ((item["format_repaired"], "re-encoded to match extension"), (item["resized"], "downscaled"), (item["compressed"], "re-encoded/compressed")) if flag)
            lines.append(f"| {path.name} | {item['format_before']} | {after_format} | {item['width_before']}×{item['height_before']} | {after_width}×{after_height} | {action} |")
    else:
        lines.append("| — | — | — | — | — | none |")

    def detail_table(title, rows, columns, formatter):
        lines.extend(["", f"## {title}", "", "| " + " | ".join(columns) + " |", "|" + "|".join(["---"] * len(columns)) + "|"])
        if rows:
            for row in rows:
                lines.append("| " + " | ".join(str(x).replace("|", "\\|").replace("\n", " ") for x in formatter(row)) + " |")
        else:
            lines.append("| " + " | ".join(["—"] * len(columns)) + " |")

    detail_table(
        "Remaining extension mismatches",
        mismatches,
        ["Asset", "Declared extension", "Detected format", "Dimensions", "Active reference"],
        lambda item: [Path(item["path"]).name, Path(item["path"]).suffix.lower(), item["format_before"], f'{item["width_before"]}×{item["height_before"]}', "yes" if Path(item["path"]).name in active_refs else "no"],
    )
    detail_table(
        "Remaining oversized assets",
        oversized,
        ["Asset", "Dimensions", "Bytes", "Active reference"],
        lambda item: [Path(item["path"]).name, f'{item["width_before"]}×{item["height_before"]}', Path(item["path"]).stat().st_size, "yes" if Path(item["path"]).name in active_refs else "no"],
    )
    detail_table(
        "Remaining large assets",
        large_assets,
        ["Asset", "Dimensions", "Bytes", "Active reference"],
        lambda item: [Path(item["path"]).name, f'{item["width_before"]}×{item["height_before"]}', Path(item["path"]).stat().st_size, "yes" if Path(item["path"]).name in active_refs else "no"],
    )
    detail_table(
        "Small assets requiring visual review",
        small,
        ["Asset", "Dimensions", "Active reference"],
        lambda item: [Path(item["path"]).name, f'{item["width_before"]}×{item["height_before"]}', "yes" if Path(item["path"]).name in active_refs else "no"],
    )
    lines.extend(["", "## Identical-byte duplicate asset clusters", ""])
    for cluster in duplicate_groups:
        lines.append("- " + ", ".join(cluster))
    if not duplicate_groups:
        lines.append("None found.")
    detail_table(
        "Potential filename/name mismatches",
        naming_mismatches,
        ["Playlist", "Channel", "Logo asset", "Group"],
        lambda item: item,
    )
    lines.extend(["", "## Policy", "",
        "- The tool does not delete unused assets or choose a channel identity based only on filename.",
        "- Duplicate logos across different channels remain a manual authenticity decision.",
        "- It never changes playlist stream URLs, tvg-id, tvg-name, tvg-chno or group placement.",
        "- Active generated-fallback logos are handled separately by the pre-publish gate.", "",
    ])
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(
        f"Logo asset audit complete: repaired={len(changed)}, "
        f"remaining_format_mismatches={len(mismatches)}, remaining_oversized={len(oversized)}, "
        f"duplicate_clusters={len(duplicate_groups)}"
    )


if __name__ == "__main__":
    main()
