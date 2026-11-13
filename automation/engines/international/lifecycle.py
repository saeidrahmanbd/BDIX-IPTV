"""Pure decision layer for International playlist lifecycle; emits plans, never edits files."""
from __future__ import annotations
from dataclasses import dataclass
from datetime import date
from stream_failure_policy import Probe, consecutive_definitive_failure_days, action_for_failure_streak

@dataclass(frozen=True)
class ChannelState:
    identity: str
    current_group: str
    primary_group: str | None = None
    alternate_is_eligible: bool = False
    probes: tuple[Probe, ...] = ()

@dataclass(frozen=True)
class LifecycleDecision:
    identity: str
    current_group: str
    target_group: str
    action: str
    failure_streak: int

def decide_channel(state: ChannelState, today: date) -> LifecycleDecision:
    """Return a proposed group/action; never performs playlist or Git operations."""
    if not state.identity.strip():
        raise ValueError("channel identity is required")
    current = state.current_group.strip() or "Review"
    streak = consecutive_definitive_failure_days(list(state.probes), today)
    failure_action = action_for_failure_streak(streak)

    if failure_action == "MOVE_TO_REVIEW":
        return LifecycleDecision(state.identity, current, "Review", "MOVE_TO_REVIEW", streak)
    if failure_action == "ELIGIBLE_FOR_REMOVAL_REVIEW":
        return LifecycleDecision(state.identity, current, "Review", "REQUIRES_OWNER_REMOVAL_REVIEW", streak)

    if current.casefold() == "review":
        if state.primary_group and state.alternate_is_eligible:
            target = state.primary_group.strip()
            action = "RESTORE_TO_PRIMARY"
        elif state.primary_group:
            target = "Backup"
            action = "RESTORE_TO_BACKUP"
        else:
            target = "Review"
            action = "KEEP_REVIEW_UNCLASSIFIED"
        return LifecycleDecision(state.identity, current, target, action, streak)

    return LifecycleDecision(state.identity, current, current, "KEEP_CURRENT_GROUP", streak)
