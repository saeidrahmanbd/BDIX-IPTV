"""Candidate-only International maintenance orchestrator over supplied stream targets."""
from __future__ import annotations
from dataclasses import dataclass, replace
from datetime import date
from concurrent.futures import ThreadPoolExecutor, as_completed
from automation.engines.international import monitor
from automation.engines.international.probe_ledger import parse_ledger, probes_for, record_probe, url_fingerprint
from automation.engines.international.engine import InternationalCandidate, build_international_candidate
from automation.engines.international.planner import RowLifecycleInput
from automation.engines.iptv.candidate_engine import DiscoveryCandidate
from automation.core.playlist_contract import parse_rows, ATTR_RE

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
    if timeout < 1 or timeout > 30:
        raise ValueError("probe timeout must be between 1 and 30 seconds")
    ordered_targets=sorted(targets,key=lambda item:item.row_index)
    row_indexes=set()
    identities=set()
    ledger=parse_ledger(ledger_text)
    pending=[]
    reused=0
    for target in ordered_targets:
        if target.row_index in row_indexes:
            raise ValueError("duplicate stream target row index")
        if target.identity.strip().casefold() in identities:
            raise ValueError("duplicate stream target identity")
        row_indexes.add(target.row_index)
        identities.add(target.identity.strip().casefold())
        fingerprint=url_fingerprint(target.url)
        history=tuple(item for item in probes_for(ledger,target.identity) if item.url_fingerprint == fingerprint)
        if any(item.day == today for item in history):
            reused += 1
        else:
            pending.append(target)

    # Probe independent stream URLs concurrently, but apply observations to the
    # ledger in row order so serialized state remains deterministic.
    observations={}
    if pending:
        with ThreadPoolExecutor(max_workers=min(8,len(pending))) as pool:
            futures={
                pool.submit(monitor.probe_stream,target.url,today,timeout): target
                for target in pending
            }
            for future in as_completed(futures):
                target=futures[future]
                try:
                    observations[target.identity]=replace(
                        future.result(),url_fingerprint=url_fingerprint(target.url)
                    )
                except ValueError:
                    # Malformed or unsafe URLs are inconclusive, never a dead stream.
                    from automation.engines.international.stream_failure_policy import Probe
                    observations[target.identity]=Probe(
                        today,None,network_error=True,
                        url_fingerprint=url_fingerprint(target.url),
                    )

    current_ledger=ledger_text or ""
    for target in pending:
        current_ledger=record_probe(
            current_ledger,target.identity,observations[target.identity]
        )

    probed=len(pending)
    lifecycle_inputs=[]
    final_ledger=parse_ledger(current_ledger)
    for target in ordered_targets:
        fingerprint=url_fingerprint(target.url)
        probe_history=tuple(
            item for item in probes_for(final_ledger,target.identity)
            if item.url_fingerprint == fingerprint
        )
        latest=probe_history[-1] if probe_history else None
        verified_role=(
            target.verified_stream_role
            if latest is not None and latest.stream_state == "verified"
            else None
        )
        lifecycle_inputs.append(RowLifecycleInput(
            target.row_index,target.identity,target.primary_group,
            verified_role,probe_history
        ))
    candidate=build_international_candidate(playlist_text,lifecycle_inputs,today,discoveries=discoveries)
    return InternationalMaintenanceResult(candidate,current_ledger or "",probed,reused,False)



def run_international_candidate_persisted(playlist_text: str, targets: list[StreamTarget] | None,
                                          today: date, baseline_commit: str, store,
                                          timeout: int = 8,
                                          discoveries: list[DiscoveryCandidate] | None = None):
    """Run International maintenance with durable dated probes and an idempotent run reservation."""
    import hashlib
    import json
    from automation.core.github_state_store import execute_remote_run
    from automation.core.run_ledger import RunRequest
    from automation.engines.international.probe_ledger import parse_ledger

    if targets is None:
        targets = derive_primary_stream_targets(playlist_text)
    target_material = [
        (item.row_index, item.identity, item.url, item.primary_group, item.verified_stream_role)
        for item in sorted(targets, key=lambda item: item.row_index)
    ]
    discovery_material = [
        (item.extinf, item.url, item.backup) for item in (discoveries or [])
    ]
    fingerprint = hashlib.sha256((
        playlist_text + "\0" +
        json.dumps(target_material, ensure_ascii=False) + "\0" +
        json.dumps(discovery_material, ensure_ascii=False)
    ).encode("utf-8")).hexdigest()
    request = RunRequest("international", today, baseline_commit, fingerprint)

    def operation():
        snapshot = store.load()
        ledger_text = json.dumps(snapshot.state["international_probe_ledger"])
        result = run_international_candidate(
            playlist_text, ledger_text, targets, today, timeout, discoveries
        )
        updated = dict(snapshot.state)
        updated["international_probe_ledger"] = parse_ledger(result.ledger_json)
        store.save(updated, snapshot.blob_sha)
        return result

    return execute_remote_run(store, request, operation)


def _review_primary_group(attrs: dict[str, str]) -> str | None:
    """Infer a Review row's destination only from explicit, unambiguous metadata."""
    country = (attrs.get("tvg-country") or "").strip()
    language = (attrs.get("tvg-language") or "").strip().casefold()
    content = (attrs.get("tvg-content") or "").strip().casefold()
    country_key = country.casefold()
    if country_key in {"bd", "bangladesh"}:
        return "Bangladesh"
    if country_key in {"pk", "pakistan"}:
        return "Pakistani"
    if country_key in {"in", "india"}:
        if language in {"bn", "ben", "bengali", "bangla"}:
            return "Indian Bangla"
        if any(token in content for token in ("movie", "film")):
            return "Indian Movies"
        if "music" in content:
            return "Indian Music"
        if any(token in content for token in ("entertainment", "series", "serial")):
            return "Indian Entertainment"
        return "India"
    # Accept an explicit country name; do not guess a display name from a 2-letter code.
    if len(country) > 2 and country.replace(" ", "").isalpha():
        return country.title()
    return None


def derive_primary_stream_targets(playlist_text: str) -> list[StreamTarget]:
    """Select unique primary and Review rows; never probe Backup or discovery queues."""
    rows = parse_rows(playlist_text)
    excluded_groups = {"backup", "backups", "new channels", "new backups", "new backup", "not playing", "test"}
    candidates = []
    counts = {}
    for index, row in enumerate(rows):
        attrs = dict(ATTR_RE.findall(row.extinf))
        identity = (attrs.get("tvg-id") or "").strip()
        group = row.group.strip()
        if not identity or group.casefold() in excluded_groups:
            continue
        if not row.url.startswith(("http://", "https://")):
            continue
        if group.casefold() == "review":
            destination = _review_primary_group(attrs)
            role = "primary" if destination else None
        else:
            destination = group
            role = "primary"
        counts[identity.casefold()] = counts.get(identity.casefold(), 0) + 1
        candidates.append((index, identity, row.url, destination, role))
    # Duplicate tvg-id values are ambiguous and remain untouched for owner review.
    return [
        StreamTarget(index, identity, url, group, role)
        for index, identity, url, group, role in candidates
        if counts[identity.casefold()] == 1
    ]
