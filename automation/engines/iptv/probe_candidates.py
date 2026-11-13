"""Discovery-time stream verification: remove only definitively dead new candidates."""
from __future__ import annotations
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import date
from automation.engines.iptv.candidate_engine import DiscoveryCandidate
from automation.engines.international.stream_probe import probe_stream

@dataclass(frozen=True)
class DiscoveryProbeBatch:
    retained: tuple[DiscoveryCandidate,...]
    verified_count: int
    inconclusive_count: int
    removed_dead: tuple[str,...]
    warnings: tuple[str,...]

def probe_discovery_candidates(candidates: list[DiscoveryCandidate] | tuple[DiscoveryCandidate,...],
                               today: date, timeout: int = 8,
                               max_workers: int = 12) -> DiscoveryProbeBatch:
    """Probe only new rows; dead/invalid media is removed, inconclusive results stay in manual review."""
    if timeout < 1 or timeout > 30:
        raise ValueError("probe timeout must be between 1 and 30 seconds")
    if max_workers < 1 or max_workers > 32:
        raise ValueError("max_workers must be between 1 and 32")
    results={}
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures={pool.submit(probe_stream,item.url,today,timeout):index for index,item in enumerate(candidates)}
        for future in as_completed(futures):
            index=futures[future]
            try:
                results[index]=future.result()
            except ValueError as exc:
                results[index]=None

    retained=[]
    removed=[]
    warnings=[]
    verified=0
    inconclusive=0
    for index,item in enumerate(candidates):
        result=results[index]
        if result is None:
            removed.append(item.extinf.split(",",1)[-1].strip())
            warnings.append(f"{item.extinf.split(',',1)[-1].strip()}: unsafe or malformed stream URL rejected")
            continue
        if result.stream_state=="dead":
            removed.append(item.extinf.split(",",1)[-1].strip())
            continue
        retained.append(item)
        if result.stream_state=="verified":
            verified+=1
        else:
            inconclusive+=1
            warnings.append(f"{item.extinf.split(',',1)[-1].strip()}: stream probe inconclusive; retained for manual review")
    return DiscoveryProbeBatch(tuple(retained),verified,inconclusive,tuple(removed),tuple(warnings))
