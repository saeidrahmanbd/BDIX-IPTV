"""Fail-closed EPG candidate gate; validates candidate against last-known-good text."""
from __future__ import annotations
import hashlib
from dataclasses import dataclass
from automation.engines.epg.validator import validate_xmltv

@dataclass(frozen=True)
class EpgCandidateDecision:
    accepted: bool
    baseline_sha256: str
    candidate_sha256: str
    reason: str

def _digest(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()

def evaluate_candidate(baseline_xml: str, candidate_xml: str) -> EpgCandidateDecision:
    """Accept only valid candidate XMLTV when the last-known-good baseline is also valid."""
    baseline_hash = _digest(baseline_xml)
    candidate_hash = _digest(candidate_xml)
    baseline = validate_xmltv(baseline_xml)
    if not baseline.valid:
        return EpgCandidateDecision(False,baseline_hash,candidate_hash,"last-known-good baseline failed validation")
    candidate = validate_xmltv(candidate_xml)
    if not candidate.valid:
        return EpgCandidateDecision(False,baseline_hash,candidate_hash,"candidate failed validation: " + "; ".join(candidate.errors[:5]))
    if candidate.channel_count < baseline.channel_count:
        return EpgCandidateDecision(False,baseline_hash,candidate_hash,"candidate channel count regressed")
    if candidate.programme_count == 0:
        return EpgCandidateDecision(False,baseline_hash,candidate_hash,"candidate contains no programmes")
    return EpgCandidateDecision(True,baseline_hash,candidate_hash,"candidate passed structural checks; publication remains disabled")
