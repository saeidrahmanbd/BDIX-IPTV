"""Single authoritative permanent-removal policy for IPTV channels.

Both the maintenance pipeline (maintenance_helpers) and the protected-queue
restoration logic (restore_protected_review) import this module, and so does the
discovery pipeline, so an owner-authorized removal cannot be reintroduced by any
automated path. This module has no imports from other repository scripts, which
keeps the dependency graph acyclic.

Adding a name here is an owner decision. Do not add names automatically.
"""
from __future__ import annotations

import re
import unicodedata

PERMANENTLY_REMOVED_NAMES = {
    "60 Days In",
    "Aaj Tak",
    "AccuWeather",
    "Al-Mahdi TV",
    "America's Got Talent",
    "American Idol",
    "Angel TV",
    "Baraza Music TV",
    "Bollywood Masala",
    "Calvary TV",
    "CBN TV USA",
    "Crime + Investigation",
    "Deadly Women",
    "Dios Te Ve Kids",
    "FX 2",
    "GNT",
    "Good News Today",
    "Grace Network",
    "Highway Thru Hell",
    "History Hunters",
    "Hosanna TV",
    "Hosanna TV Hindi",
    "IBN TV",
    "IBN TV Africa",
    "Jeremiah TV",
    "Joshua TV",
    "King TV",
    "MINI",
    "Mundial",
    "Network 10",
    "Popflix",
    "Prarthana TV",
    "Safeer TV",
    "Santvani Channel",
    "Sharnam TV",
    "The Walking Dead Universe",
    "True History",
    "TVC Arabic Kids",
    "ZB Bhakti",
}


def canonical_channel_name(value: str) -> str:
    """Normalize display names for exact allowlist matching only."""
    value = unicodedata.normalize("NFKD", str(value or "")).casefold()
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    value = re.sub(
        r"\b(?:backup|hd|fhd|uhd|sd|4k|1080p|720p|576p|480p|360p)\b",
        " ",
        value,
    )
    return re.sub(r"[^a-z0-9]+", "", value)


PERMANENTLY_REMOVED_KEYS = frozenset(canonical_channel_name(name) for name in PERMANENTLY_REMOVED_NAMES)


def is_permanently_removed_name(name: str) -> bool:
    """True when a display name matches an owner-authorized permanent removal."""
    return canonical_channel_name(name) in PERMANENTLY_REMOVED_KEYS
