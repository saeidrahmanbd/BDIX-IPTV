"""End-to-end candidate-only International discovery and maintenance orchestration."""
from __future__ import annotations
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from automation.engines.international.discovery import InternationalDiscoveryBatch, build_international_discovery_batch, fetch_international_source
from automation.engines.international.orchestrator import InternationalMaintenanceResult, StreamTarget, run_international_candidate
from automation.engines.iptv.probe_candidates import DiscoveryProbeBatch, probe_discovery_candidates

@dataclass(frozen=True)
class InternationalDiscoveryRun:
    maintenance: InternationalMaintenanceResult
    discovery: InternationalDiscoveryBatch
    probes: DiscoveryProbeBatch
    source_warnings: tuple[str,...]
    publish: bool = False

def run_international_discovery(playlist_text: str, ledger_text: str | None,
                                targets: list[StreamTarget], today: date,
                                repository_root: str | Path,
                                source_text: str | None = None,
                                timeout: int = 8) -> InternationalDiscoveryRun:
    """Fetch source, keep eligible candidates in manual queues, probe new streams, and run lifecycle maintenance."""
    warnings=[]
    if source_text is None:
        try:
            source_text=fetch_international_source()
        except Exception as exc:
            source_text=""
            warnings.append(f"International source unavailable: {type(exc).__name__}")
    discovery=build_international_discovery_batch(playlist_text,source_text,repository_root)
    probes=probe_discovery_candidates(discovery.candidates,today,timeout)
    maintenance=run_international_candidate(
        playlist_text,ledger_text,targets,today,timeout,
        discoveries=list(probes.retained),
    )
    return InternationalDiscoveryRun(maintenance,discovery,probes,tuple(warnings),False)
