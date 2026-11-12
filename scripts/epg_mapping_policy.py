"""Shared region-compatibility policy for EPG channel-to-source identity mapping."""
from __future__ import annotations

# These two global channels are intentionally carried under a GB XMLTV identity
# in the maintained US playlist. They were explicitly verified as the same
# services; this narrow exception must not become a general regional bypass.
CURATED_REGION_OVERRIDES = {
    "TravelxpEnglish.us": {"Travelxp.uk"},
    "WorldWarTV.us": {"WorldWarTV.uk"},
}


def mapping_id_region_compatible(
    target_country: str,
    source_id_country: str,
    source_feed_countries=(),
    *,
    explicit_override: bool = False,
    require_feed_match: bool = False,
) -> bool:
    """Reject mismatched regional IDs or regional feeds unless an alias is curated.

    A country suffix/territory on an exact XMLTV ID is authoritative. When
    the source ID carries no region, a country-specific feed provides a fallback
    guard. Name-derived candidates set require_feed_match=True so that the feed
    territory must also agree, even when its IDs carry a country suffix.
    """
    if explicit_override:
        return True

    target = str(target_country or "").strip().upper()
    source = str(source_id_country or "").strip().upper()
    feeds = {
        str(value or "").strip().upper()
        for value in source_feed_countries
        if str(value or "").strip()
    }

    if target and source and target != source:
        return False
    if target and feeds and target not in feeds and (require_feed_match or not source):
        return False
    return True
