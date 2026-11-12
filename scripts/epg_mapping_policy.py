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
) -> bool:
    """Reject mismatched regional IDs or regional feeds unless an alias is curated.

    A country suffix/territory on the XMLTV channel ID is the strongest signal.
    When the source ID carries no region, a known country-specific feed provides
    the secondary guard. Global/unknown feeds remain eligible for manual aliases.
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
    # A matching suffix does not excuse a contradictory country-specific feed.
    if target and feeds and target not in feeds:
        return False
    return True
