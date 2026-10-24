#!/usr/bin/env python3
"""Shared conservative logo basename policy for repair and publication gates."""
import hashlib
import re
from pathlib import Path

BAD_ASSETS = frozenset({
    "atn-news.png", "a-sports-5485adff.png", "a-sports-hd.png", "bein-sports-3.png",
    "bangla-tv.png", "btv-news.png", "colors.png", "duronto-tv.png",
    "duronto-tv-1ad55c95.png", "ekushey-tv.png", "global-tv.png", "green-tv.png",
    "mohona-tv.png", "nagorik-tv.png", "nagorik.png", "nick-bangla.png",
    "sananda-tv.png", "sananda.png", "star-gold-select.png", "star-gold.png",
    "star-plus.png", "zee-tv.png", "tom-and-jerry.png", "arirang-tv.png",
})
GENERIC_PREFIXES = ("placeholder-", "generic-", "unknown-", "unidentified-", "generated-fallback-")


def is_blocked_logo_basename(value):
    """Return True only for explicitly blocked or generic-looking basenames."""
    raw = str(value or "").split("?", 1)[0].split("#", 1)[0].replace("\\", "/")
    basename = Path(raw).name.casefold()
    return basename in BAD_ASSETS or basename.startswith(GENERIC_PREFIXES)


def safe_logo_filename(title):
    """Avoid emitting a path that the publication gate will intentionally block."""
    original = str(title or "").strip()
    slug = re.sub(r"[^A-Za-z0-9]+", "-", original).strip("-").lower()[:70].rstrip("-") or "channel"
    candidate = f"{slug}.png"
    if not is_blocked_logo_basename(candidate):
        return candidate
    digest = hashlib.sha256(original.casefold().encode("utf-8")).hexdigest()[:10]
    return f"repaired-{slug}-{digest}.png"
