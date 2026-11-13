"""End-to-end in-memory International candidate engine; only three-day policy removals are permitted."""
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
    """Apply planned group changes and only the explicitly authorized three-day removals."""
    plan=plan_lifecycle(playlist_text,inputs,today,minimum_country_group_size)
    candidate=build_candidate(playlist_text,list(plan.changes),plan.remove_identities)
    group_candidate=candidate
    if discoveries:
        from automation.engines.international.candidate_engine import append_discovery_candidates, assert_international_existing_rows_preserved
        candidate=append_discovery_candidates(group_candidate,discoveries)
        assert_international_existing_rows_preserved(group_candidate,candidate)
    from automation.core.playlist_contract import parse_rows
    baseline_count=len(parse_rows(playlist_text))
    candidate_count=len(parse_rows(candidate))
    expected_count=baseline_count-len(plan.remove_identities)
    if candidate_count < expected_count:
        raise ValueError("International candidate removed more rows than the three-day policy authorized")
    if candidate_count > expected_count and not discoveries:
        raise ValueError("International candidate added unexpected stream rows")
    if not discoveries and candidate_count != baseline_count:
        raise ValueError("International maintenance candidate cannot add stream rows without discovery input")
    return InternationalCandidate(candidate,plan,baseline_count,candidate_count,False)
