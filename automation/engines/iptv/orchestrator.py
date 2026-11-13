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
