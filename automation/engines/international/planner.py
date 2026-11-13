"""Pure International lifecycle planner. It emits group changes and policy-authorized three-day removals."""
from __future__ import annotations
from dataclasses import dataclass
from datetime import date
from automation.core.playlist_contract import parse_rows, ATTR_RE
from automation.engines.international.candidate_engine import GroupChange
from automation.engines.international.lifecycle import ChannelState, decide_channel
from automation.engines.international.country_groups import ChannelIdentity, eligible_country_groups, FIXED_PRIMARY_GROUPS

@dataclass(frozen=True)
class RowLifecycleInput:
    row_index: int
    identity: str
    primary_group: str | None = None
    verified_stream_role: str | None = None
    probes: tuple = ()

@dataclass(frozen=True)
class InternationalPlan:
    changes: tuple[GroupChange, ...]
    remove_identities: tuple[str, ...]
    review_identities: tuple[str, ...]
    publish: bool = False

def plan_lifecycle(playlist_text: str, inputs: list[RowLifecycleInput], today: date,
                   minimum_country_group_size: int = 5) -> InternationalPlan:
    """Plan safe group moves and three-day removals; never writes files or publishes."""
    rows = parse_rows(playlist_text)
    by_index: dict[int, RowLifecycleInput] = {}
    for item in inputs:
        if item.row_index < 0 or item.row_index >= len(rows):
            raise ValueError(f"row index out of range: {item.row_index}")
        if item.row_index in by_index:
            raise ValueError(f"duplicate lifecycle input for row: {item.row_index}")
        if not item.identity.strip():
            raise ValueError("lifecycle identity is required")
        actual_identity=dict(ATTR_RE.findall(rows[item.row_index].extinf)).get("tvg-id","").strip()
        if not actual_identity:
            raise ValueError(f"International row {item.row_index} has no tvg-id identity")
        if actual_identity.casefold() != item.identity.strip().casefold():
            raise ValueError(f"lifecycle identity does not match row {item.row_index} tvg-id")
        by_index[item.row_index] = item

    primary_identities = [
        ChannelIdentity(item.identity, item.primary_group or rows[index].group, True)
        for index, item in by_index.items()
        if item.primary_group and item.verified_stream_role == "primary"
    ]
    eligible_groups = eligible_country_groups(primary_identities, minimum_country_group_size)
    fixed = FIXED_PRIMARY_GROUPS

    changes: list[GroupChange] = []
    remove: list[str] = []
    review: list[str] = []
    for index, item in sorted(by_index.items()):
        row = rows[index]
        decision = decide_channel(
            ChannelState(item.identity,row.group,item.primary_group,item.verified_stream_role,item.probes),
            today,
        )
        target = decision.target_group
        if decision.action == "RESTORE_TO_PRIMARY":
            if target.casefold() not in fixed and target.casefold() not in {g.casefold() for g in eligible_groups}:
                target = "Backup"
        if decision.action == "REMOVE":
            remove.append(item.identity)
            continue
        if target.casefold() == "review":
            review.append(item.identity)
        if target != row.group:
            changes.append(GroupChange(index,target,decision.action))
    return InternationalPlan(tuple(changes),tuple(remove),tuple(review),False)
