"""Fail-closed EPG candidate gate; validates candidate against last-known-good text."""
from __future__ import annotations
import hashlib
from datetime import datetime
from dataclasses import dataclass
from automation.engines.epg.validator import validate_xmltv
from automation.engines.epg.coverage import compare_coverage
from automation.engines.epg.freshness import compare_freshness

@dataclass(frozen=True)
class EpgCandidateDecision:
    accepted: bool
    baseline_sha256: str
    candidate_sha256: str
    reason: str

def _digest(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()

def evaluate_candidate(baseline_xml: str, candidate_xml: str,
                       active_playlist_text: str | None = None,
                       as_of: datetime | None = None) -> EpgCandidateDecision:
    """Accept only structurally valid, non-regressing candidates; publication remains disabled."""
    baseline_hash = _digest(baseline_xml)
    candidate_hash = _digest(candidate_xml)
    baseline = validate_xmltv(baseline_xml)
    if not baseline.valid:
        return EpgCandidateDecision(False,baseline_hash,candidate_hash,"last-known-good baseline failed validation")
    candidate = validate_xmltv(candidate_xml)
    if not candidate.valid:
        return EpgCandidateDecision(False,baseline_hash,candidate_hash,"candidate failed validation: " + "; ".join(candidate.errors[:5]))
    # A generated guide may intentionally drop orphaned/retired XMLTV channels.
    # When active playlists are available, the playlist-scoped coverage gate below
    # is authoritative; raw global counts include unused IDs and can reject a safe guide.
    if active_playlist_text is None and candidate.channel_count < baseline.channel_count:
        return EpgCandidateDecision(False,baseline_hash,candidate_hash,"candidate channel count regressed")
    if active_playlist_text is not None:
        try:
            comparison = compare_coverage(active_playlist_text,baseline_xml,candidate_xml)
        except ValueError as exc:
            return EpgCandidateDecision(False,baseline_hash,candidate_hash,f"coverage evaluation failed: {exc}")
        if not comparison.accepted:
            return EpgCandidateDecision(False,baseline_hash,candidate_hash,"candidate coverage regressed: " + "; ".join(comparison.reasons))
        try:
            freshness = compare_freshness(active_playlist_text,baseline_xml,candidate_xml,as_of)
        except ValueError as exc:
            return EpgCandidateDecision(False,baseline_hash,candidate_hash,f"freshness evaluation failed: {exc}")
        if not freshness.accepted:
            return EpgCandidateDecision(False,baseline_hash,candidate_hash,"candidate schedule freshness regressed: " + "; ".join(freshness.reasons))
    return EpgCandidateDecision(True,baseline_hash,candidate_hash,"candidate passed structural and configured coverage checks; publication remains disabled")
