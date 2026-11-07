"""Ordering policy for automated IPTV playlist audits."""

PROTECTED_REVIEW_GROUPS = frozenset({"backup", "review", "not playing", "new channels", "new backups"})


def should_check_alphabetical_order(group: str) -> bool:
    """Return False for review queues whose internal order is manually protected."""
    return str(group or "").strip().casefold() not in PROTECTED_REVIEW_GROUPS
