"""International country-group eligibility rules, independent of playlist I/O."""
from __future__ import annotations
from dataclasses import dataclass

FIXED_GROUPS = {"bangladesh", "india"}
NON_COUNTRY_PRIMARY_GROUPS = {
    "indian bangla", "indian movies", "indian music", "indian entertainment",
    "international", "fashion tv", "documentary & wildlife", "kids",
    "religious", "sports", "adult", "test",
}
FIXED_PRIMARY_GROUPS = FIXED_GROUPS | NON_COUNTRY_PRIMARY_GROUPS
NON_PRIMARY_GROUPS = {
    "backup", "review", "new channels", "new backups", "new backup",
    "not playing", "not playing...",
} | NON_COUNTRY_PRIMARY_GROUPS

@dataclass(frozen=True)
class ChannelIdentity:
    identity: str
    country_group: str
    is_primary: bool = True

def eligible_country_groups(channels: list[ChannelIdentity], minimum: int = 5) -> set[str]:
    """Return display names for non-fixed groups meeting the case-insensitive identity threshold."""
    if minimum < 1:
        raise ValueError("minimum must be positive")
    identities: dict[str, set[str]] = {}
    display_names: dict[str, str] = {}
    for channel in channels:
        group = channel.country_group.strip()
        normalized = group.casefold()
        identity = channel.identity.strip().casefold()
        if not channel.is_primary or normalized in NON_PRIMARY_GROUPS or not identity:
            continue
        if normalized in FIXED_GROUPS:
            continue
        identities.setdefault(normalized, set()).add(identity)
        display_names.setdefault(normalized, group)
    return {display_names[key] for key, members in identities.items() if len(members) >= minimum}

def should_create_country_group(group: str, channels: list[ChannelIdentity], minimum: int = 5) -> bool:
    normalized = group.strip().casefold()
    if normalized in FIXED_GROUPS:
        return True
    return any(candidate.casefold() == normalized for candidate in eligible_country_groups(channels, minimum))
