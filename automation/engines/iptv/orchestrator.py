"""End-to-end candidate-only IPTV discovery orchestration."""
from __future__ import annotations
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from automation.engines.iptv.candidate_engine import IptvCandidate, build_iptv_candidate
from automation.engines.iptv.discovery import DiscoveryBatch, build_discovery_batch, fetch_all_source_feeds
from automation.engines.iptv.probe_candidates import DiscoveryProbeBatch, probe_discovery_candidates

@dataclass(frozen=True)
class IptvDiscoveryRun:
    candidate: IptvCandidate
    discovery: DiscoveryBatch
    probes: DiscoveryProbeBatch
    source_warnings: tuple[str,...]
    publish: bool = False

def run_iptv_discovery(playlist_text: str, repository_root: str | Path, today: date,
                       source_feeds: dict[str,str] | None = None,
                       timeout: int = 8) -> IptvDiscoveryRun:
    """Fetch or accept approved BD/IN feeds, keep uncertain metadata in manual queues, and probe new streams."""
    source_warnings: tuple[str,...]=()
    if source_feeds is None:
        source_feeds,source_warnings=fetch_all_source_feeds()
    discovery=build_discovery_batch(playlist_text,source_feeds,repository_root)
    probes=probe_discovery_candidates(discovery.candidates,today,timeout)
    candidate=build_iptv_candidate(playlist_text,list(probes.retained),[],repository_root)
    return IptvDiscoveryRun(candidate,discovery,probes,source_warnings,False)



def run_iptv_discovery_persisted(playlist_text: str, repository_root: str | Path,
                                today: date, baseline_commit: str, store,
                                source_feeds: dict[str, str] | None = None,
                                timeout: int = 8):
    """Reserve the daily candidate run in cross-run state before fetching sources/probing."""
    import hashlib
    import json
    from automation.core.github_state_store import execute_remote_run
    from automation.core.run_ledger import RunRequest

    source_fingerprint = (
        json.dumps(sorted(source_feeds.items()), ensure_ascii=False)
        if source_feeds is not None else "approved-live-source-registry"
    )
    fingerprint = hashlib.sha256(
        (playlist_text + "\0" + source_fingerprint).encode("utf-8")
    ).hexdigest()
    request = RunRequest("iptv", today, baseline_commit, fingerprint)
    return execute_remote_run(
        store, request,
        lambda: run_iptv_discovery(
            playlist_text, repository_root, today, source_feeds, timeout
        ),
    )
