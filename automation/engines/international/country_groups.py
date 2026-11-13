"""International country-group eligibility rules, independent of playlist I/O."""
from __future__ import annotations
from dataclasses import dataclass

FIXED_GROUPS = {"bangladesh", "india"}
NON_PRIMARY_GROUPS = {"backup", "review", "new channels", "new backups"}

@dataclass(frozen=True)
class ChannelIdentity:
    identity: str
    country_group: str
    is_primary: bool = True

def eligible_country_groups(channels: list[ChannelIdentity], minimum: int = 5) -> set[str]:
    """Return non-fixed country groups meeting the unique-primary-identity threshold."""
    if minimum < 1:
        raise ValueError("minimum must be positive")
    identities: dict[str, set[str]] = {}
    for channel in channels:
        group = channel.country_group.strip()
        normalized = group.casefold()
        if not channel.is_primary or normalized in NON_PRIMARY_GROUPS or not channel.identity.strip():
            continue
        if normalized in FIXED_GROUPS:
            continue
        identities.setdefault(group, set()).add(channel.identity.strip().casefold())
    return {group for group, members in identities.items() if len(members) >= minimum}

def should_create_country_group(group: str, channels: list[ChannelIdentity], minimum: int = 5) -> bool:
    normalized = group.strip().casefold()
    if normalized in FIXED_GROUPS:
        return True
    return group in eligible_country_groups(channels, minimum)
