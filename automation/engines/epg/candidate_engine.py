"""End-to-end in-memory EPG candidate engine with approved aliases and regression gates."""
from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from automation.engines.epg.alias_apply import ApprovedAlias, apply_approved_aliases
from automation.engines.epg.candidate_gate import EpgCandidateDecision, evaluate_candidate

@dataclass(frozen=True)
class EpgCandidate:
    xml_text: str
    decision: EpgCandidateDecision
    publish: bool = False

def build_epg_candidate(playlist_text: str, last_known_good_xml: str,
                        source_candidate_xml: str | None = None,
                        approved_aliases: list[ApprovedAlias] | None = None,
                        as_of: datetime | None = None) -> EpgCandidate:
    """Validate a provider candidate, apply only approved aliases, and reject coverage/freshness regression."""
    candidate=source_candidate_xml if source_candidate_xml is not None else last_known_good_xml
    aliases=approved_aliases or []
    if aliases:
        candidate=apply_approved_aliases(playlist_text,candidate,aliases)
    decision=evaluate_candidate(last_known_good_xml,candidate,playlist_text,as_of)
    return EpgCandidate(candidate,decision,False)
