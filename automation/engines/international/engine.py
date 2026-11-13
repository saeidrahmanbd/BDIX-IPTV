"""End-to-end in-memory International candidate engine; no deletion or publication."""
from __future__ import annotations
from dataclasses import dataclass
from datetime import date
from automation.engines.international.candidate_engine import build_candidate
from automation.engines.international.planner import InternationalPlan, RowLifecycleInput, plan_lifecycle

@dataclass(frozen=True)
class InternationalCandidate:
    text: str
    plan: InternationalPlan
    baseline_rows: int
    candidate_rows: int
    publish: bool = False

def build_international_candidate(playlist_text: str, inputs: list[RowLifecycleInput],
                                  today: date, minimum_country_group_size: int = 5,
                                  discoveries: list | None = None) -> InternationalCandidate:
    """Apply only planned group changes while preserving every stream URL and row."""
    plan=plan_lifecycle(playlist_text,inputs,today,minimum_country_group_size)
    candidate=build_candidate(playlist_text,list(plan.changes))
    if discoveries:
        from automation.engines.international.candidate_engine import append_discovery_candidates
        candidate=append_discovery_candidates(candidate,discoveries)
    from automation.core.playlist_contract import parse_rows
    baseline_count=len(parse_rows(playlist_text))
    candidate_count=len(parse_rows(candidate))
    if candidate_count != baseline_count:
        raise ValueError("International candidate cannot add or remove stream rows")
    return InternationalCandidate(candidate,plan,baseline_count,candidate_count,False)
