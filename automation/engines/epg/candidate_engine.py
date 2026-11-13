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



def build_epg_candidate_persisted(playlist_text: str, last_known_good_xml: str,
                                  baseline_commit: str, store,
                                  source_candidate_xml: str | None = None,
                                  approved_aliases: list[ApprovedAlias] | None = None,
                                  as_of: datetime | None = None,
                                  repository_root: str | None = None):
    """Build one idempotently reserved EPG candidate; no publication or production writes."""
    import hashlib
    import json
    from zoneinfo import ZoneInfo
    from automation.core.github_state_store import execute_remote_run
    from automation.core.run_ledger import RunRequest

    alias_material = [
        (item.source_id, item.target_id, item.evidence, item.approved)
        for item in (approved_aliases or [])
    ]
    material = "\0".join((
        playlist_text,
        last_known_good_xml,
        source_candidate_xml or ("isolated-live-source-generation" if repository_root else ""),
        json.dumps(alias_material, ensure_ascii=False, sort_keys=True),
        as_of.isoformat() if as_of else "",
    ))
    fingerprint = hashlib.sha256(material.encode("utf-8")).hexdigest()
    request = RunRequest("epg", (as_of.date() if as_of else datetime.now(ZoneInfo("Asia/Dhaka")).date()),
                         baseline_commit, fingerprint)
    def operation():
        candidate_xml = source_candidate_xml
        if candidate_xml is None and repository_root is not None:
            from automation.engines.epg.source_provider import build_epg_source_candidate
            candidate_xml = build_epg_source_candidate(repository_root)
        return build_epg_candidate(
            playlist_text, last_known_good_xml, candidate_xml,
            approved_aliases, as_of
        )

    return execute_remote_run(store, request, operation)
