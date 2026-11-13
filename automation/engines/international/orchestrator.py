"""Candidate-only International maintenance orchestrator over supplied stream targets."""
from __future__ import annotations
from dataclasses import dataclass
from datetime import date
from automation.engines.international.monitor import probe_and_record
from automation.engines.international.probe_ledger import parse_ledger, probes_for
from automation.engines.international.engine import InternationalCandidate, build_international_candidate
from automation.engines.international.planner import RowLifecycleInput
from automation.engines.iptv.candidate_engine import DiscoveryCandidate

@dataclass(frozen=True)
class StreamTarget:
    row_index: int
    identity: str
    url: str
    primary_group: str | None = None
    verified_stream_role: str | None = None

@dataclass(frozen=True)
class InternationalMaintenanceResult:
    candidate: InternationalCandidate
    ledger_json: str
    probed_count: int
    reused_count: int
    publish: bool = False

def run_international_candidate(playlist_text: str, ledger_text: str | None,
                               targets: list[StreamTarget], today: date,
                               timeout: int = 8,
                               discoveries: list[DiscoveryCandidate] | None = None) -> InternationalMaintenanceResult:
    """Probe once per Bangladesh date, update candidate ledger in memory, and propose safe group changes."""
    row_indexes=set()
    identities=set()
    current_ledger=ledger_text
    lifecycle_inputs=[]
    probed=reused=0
    for target in sorted(targets,key=lambda item:item.row_index):
        if target.row_index in row_indexes:
            raise ValueError("duplicate stream target row index")
        if target.identity.strip().casefold() in identities:
            raise ValueError("duplicate stream target identity")
        row_indexes.add(target.row_index)
        identities.add(target.identity.strip().casefold())
        observation=probe_and_record(current_ledger,target.identity,target.url,today,timeout)
        current_ledger=observation.ledger_json
        if observation.already_probed_today:
            reused+=1
        else:
            probed+=1
        lifecycle_inputs.append(RowLifecycleInput(
            target.row_index,target.identity,target.primary_group,
            target.verified_stream_role,probes_for(parse_ledger(current_ledger),target.identity)
        ))
    candidate=build_international_candidate(playlist_text,lifecycle_inputs,today,discoveries=discoveries)
    return InternationalMaintenanceResult(candidate,current_ledger or "",probed,reused,False)
