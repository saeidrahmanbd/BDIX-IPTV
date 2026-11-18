"""Shared helpers for logo provenance / validation tests (not a test module)."""
import struct
import zlib
from pathlib import Path

SAMSUNG_URL = (
    "https://tvpnlogopus.samsungcloud.tv/platform/image/sourcelogo/vc/00/02/34/"
    "IN38000072R_20260325T012318SQUARE.png"
)
IPTV = "IPTV-Playlist.m3u"
INTL = "International-Playlist.m3u"
FALLBACK_NOTE = (
    "Unofficial fallback artwork generated after exact local and attributable "
    "online logo lookup failed; not an official broadcaster logo."
)


def png_bytes(pad=200):
    """A structurally valid PNG larger than the repository's 100-byte minimum."""
    def chunk(kind, data):
        body = kind + data
        return struct.pack(">I", len(data)) + body + struct.pack(">I", zlib.crc32(body) & 0xFFFFFFFF)

    header = struct.pack(">IIBBBBB", 1, 1, 8, 2, 0, 0, 0)
    raw = zlib.compress(b"\x00\xff\x00\x00")
    return (
        b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", header)
        + chunk(b"tEXt", b"Comment\x00" + b"x" * pad)
        + chunk(b"IDAT", raw) + chunk(b"IEND", b"")
    )


def write_png(path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(png_bytes())
    return path


def extinf(name, tvg_id, group="Indian Movies", logo=None, url="https://example.invalid/live.m3u8"):
    logo_attr = f' tvg-logo="{logo}"' if logo else ""
    return (
        f'#EXTINF:-1 tvg-id="{tvg_id}" tvg-name="{name}"{logo_attr} '
        f'group-title="{group}",{name}\n{url}\n'
    )


def playlist(*entries):
    return "#EXTM3U\n" + "".join(entries)


def fallback_record(notes=FALLBACK_NOTE, source_url=""):
    return {"status": "generated_fallback", "source_url": source_url, "notes": notes}


def verified_record(url="https://example.com/logo.png", notes="Exact source."):
    return {"status": "third_party_verified", "source_url": url, "notes": notes}
