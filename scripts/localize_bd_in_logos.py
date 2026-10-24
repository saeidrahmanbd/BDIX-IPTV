#!/usr/bin/env python3
"""Validate and localize logo images for BD.IN-Playlist.m3u.

Only logo attributes and repository logo assets are modified. Stream URLs, names, groups, and IDs
are preserved. Image validation does not independently certify broadcaster authenticity.
"""
from __future__ import annotations
import hashlib
import ipaddress
import json
import re
import urllib.error
import urllib.parse
import urllib.request
from io import BytesIO
from pathlib import Path
from PIL import Image, UnidentifiedImageError

ROOT = Path(__file__).resolve().parents[1]
PLAYLIST = ROOT / "BD.IN-Playlist.m3u"
MANIFEST = ROOT / "reports" / "bd-in-logo-sources.json"
REPORT = ROOT / "reports" / "bd-in-logo-localization.md"
LOGOS = ROOT / "logos"
LOCAL_BASE = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/"
MAX_BYTES = 3 * 1024 * 1024
MAX_DIMENSION = 4096
MIN_DIMENSION = 24
ATTR_RE = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
LOGO_RE = re.compile(r'tvg-logo="[^"]*"')
BAD_URL_WORDS = re.compile(r"(placeholder|no[-_]?image|generic[-_]?logo|default[-_]?logo|no[-_]?logo|nologo|blank[-_]?logo)", re.I)


def attrs(line: str) -> dict[str, str]:
    return dict(ATTR_RE.findall(line))


def safe_public_https(url: str) -> bool:
    try:
        p = urllib.parse.urlparse(url)
        if p.scheme != "https" or not p.hostname or p.username or p.password:
            return False
        host = p.hostname.lower().rstrip(".")
        if host in {"localhost", "localhost.localdomain"} or host.endswith((".local", ".internal", ".localhost")):
            return False
        if BAD_URL_WORDS.search(url):
            return False
        try:
            ip = ipaddress.ip_address(host)
            if not ip.is_global:
                return False
        except ValueError:
            pass
        if re.search(r"[?&](token|auth|authorization|sig|signature|expires|session|jwt|hdnts|username|password|passwd|access_token)=", p.query, re.I):
            return False
        return True
    except Exception:
        return False


class SafeRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        resolved = urllib.parse.urljoin(req.full_url, newurl)
        if not safe_public_https(resolved):
            raise urllib.error.URLError("Rejected unsafe logo redirect")
        return super().redirect_request(req, fp, code, msg, headers, resolved)


def download(url: str) -> bytes:
    if not safe_public_https(url):
        raise ValueError("source URL is not a safe public HTTPS URL")
    opener = urllib.request.build_opener(SafeRedirectHandler())
    req = urllib.request.Request(url, headers={"User-Agent": "BDIX-IPTV-Local-Logo-Validator/1.0", "Accept": "image/*"})
    with opener.open(req, timeout=18) as response:
        if not safe_public_https(response.geturl()):
            raise ValueError("redirect destination rejected")
        data = response.read(MAX_BYTES + 1)
    if not data or len(data) > MAX_BYTES:
        raise ValueError("empty image or image exceeds 3 MiB")
    return data


def to_png(data: bytes) -> bytes:
    try:
        with Image.open(BytesIO(data)) as im:
            im.verify()
        with Image.open(BytesIO(data)) as im:
            im.load()
            if im.width < MIN_DIMENSION or im.height < MIN_DIMENSION:
                raise ValueError("image is too small to be a useful logo")
            if im.width > MAX_DIMENSION or im.height > MAX_DIMENSION:
                im.thumbnail((MAX_DIMENSION, MAX_DIMENSION), Image.Resampling.LANCZOS)
            if im.mode not in ("RGB", "RGBA"):
                im = im.convert("RGBA" if "A" in im.getbands() else "RGB")
            out = BytesIO()
            im.save(out, format="PNG", optimize=True)
            return out.getvalue()
    except (UnidentifiedImageError, OSError):
        pass
    if b"<svg" in data[:4096].lower():
        try:
            import cairosvg
            png = cairosvg.svg2png(bytestring=data, output_width=512, output_height=512)
            with Image.open(BytesIO(png)) as im:
                im.load()
                if im.width < MIN_DIMENSION or im.height < MIN_DIMENSION:
                    raise ValueError("SVG logo is too small")
            return png
        except Exception as exc:
            raise ValueError(f"SVG conversion failed: {exc}") from exc
    raise ValueError("download is not a supported raster image or SVG")


def set_logo(line: str, local_url: str) -> str:
    if LOGO_RE.search(line):
        return LOGO_RE.sub(f'tvg-logo="{local_url}"', line, count=1)
    m = re.search(r'\s(channel-id|group-title)=', line)
    if m:
        return line[:m.start()] + f' tvg-logo="{local_url}"' + line[m.start():]
    comma = line.find(",")
    if comma < 0:
        return line
    return line[:comma] + f' tvg-logo="{local_url}"' + line[comma:]


def slug(value: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")
    return s[:56] or "channel"


def generated_path(channel_id: str, name: str, source_url: str) -> str:
    digest = hashlib.sha256((channel_id + "|" + source_url).encode("utf-8")).hexdigest()[:8]
    return f"bd-in-{slug(name)}-{digest}.png"


def main() -> int:
    LOGOS.mkdir(parents=True, exist_ok=True)
    sources = {}
    if MANIFEST.exists():
        payload = json.loads(MANIFEST.read_text(encoding="utf-8"))
        for row in payload.get("logo_sources", []):
            cid = str(row.get("tvg_id", "")).strip()
            if cid and row.get("source_url"):
                sources[cid] = row

    original = PLAYLIST.read_text(encoding="utf-8-sig")
    lines = original.replace("\r", "").splitlines()
    localized: dict[str, str] = {}
    failures: list[tuple[str, str]] = []
    changed_files: list[str] = []
    changed_lines = 0
    total_entries = 0
    already_local = 0
    for i, line in enumerate(lines):
        if not line.startswith("#EXTINF:"):
            continue
        total_entries += 1
        a = attrs(line)
        cid = (a.get("tvg-id") or a.get("channel-id") or "").strip()
        name = (a.get("tvg-name") or line.split(",", 1)[-1]).strip()
        logo = (a.get("tvg-logo") or "").strip()
        if logo.startswith(LOCAL_BASE):
            already_local += 1
            continue
        row = sources.get(cid)
        source_url = logo if logo and safe_public_https(logo) else ""
        if not source_url and row:
            source_url = str(row.get("source_url", "")).strip()
        if not source_url:
            if logo:
                lines[i] = LOGO_RE.sub("", line)
                if lines[i] != line:
                    changed_lines += 1
            continue
        target_name = str(row.get("path", "")).strip() if row else ""
        if not target_name:
            target_name = generated_path(cid, name, source_url)
        if "/" in target_name or "\\" in target_name or not target_name.lower().endswith(".png"):
            failures.append((name, "manifest path rejected"))
            continue
        target = LOGOS / target_name
        try:
            if not target.exists():
                target.write_bytes(to_png(download(source_url)))
                changed_files.append(target_name)
            local_url = LOCAL_BASE + urllib.parse.quote(target_name)
            new_line = set_logo(line, local_url)
            if new_line != line:
                lines[i] = new_line
                changed_lines += 1
            localized[name] = target_name
        except Exception as exc:
            failures.append((name, str(exc)[:200]))
            if logo and not logo.startswith(LOCAL_BASE):
                lines[i] = LOGO_RE.sub("", line)
                if lines[i] != line:
                    changed_lines += 1

    updated = "\n".join(lines).rstrip() + "\n"
    if updated != original:
        PLAYLIST.write_text(updated, encoding="utf-8")
    report = [
        "# BD.IN Playlist Logo Localization",
        "",
        f"- Playlist entries scanned: **{total_entries}**",
        f"- Existing repository-local logo entries: **{already_local}**",
        f"- Channel names localized in this run: **{len(localized)}**",
        f"- New local logo files created: **{len(changed_files)}**",
        f"- Playlist metadata lines changed: **{changed_lines}**",
        f"- Logo sources failed or rejected: **{len(failures)}**",
        "",
        "Images are checked for file validity and usable dimensions, then stored as repository-local PNG assets. This technical check does not independently certify broadcaster authenticity.",
        "",
        "## Localized logos",
        "",
        *(f"- {name} — logos/{path}" for name, path in sorted(localized.items(), key=lambda x: x[0].casefold())),
        "",
        "## Failed / unavailable logo sources",
        "",
        *(f"- {name}: {reason}" for name, reason in sorted(failures, key=lambda x: x[0].casefold())),
        "",
    ]
    REPORT.write_text("\n".join(report), encoding="utf-8")
    print(f"Logo localization: {len(localized)} channel names localized; {len(changed_files)} files created; {len(failures)} source failures.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
