"""Candidate-only International maintenance orchestrator over supplied stream targets."""
from __future__ import annotations
from dataclasses import dataclass
from datetime import date
from automation.engines.international.monitor import probe_and_record
from automation.engines.international.probe_ledger import parse_ledger, probes_for
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
        probe_history = probes_for(parse_ledger(current_ledger),target.identity)
        latest = probe_history[-1] if probe_history else None
        verified_role = (
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


def derive_primary_stream_targets(playlist_text: str) -> list[StreamTarget]:
    """Derive only unambiguous primary rows; queues/backups and duplicate IDs are excluded."""
    rows = parse_rows(playlist_text)
    queue_groups = {"backup", "review", "new channels", "new backups", "new backup", "not playing"}
    candidates = []
    counts = {}
    for index, row in enumerate(rows):
        attrs = dict(ATTR_RE.findall(row.extinf))
        identity = (attrs.get("tvg-id") or "").strip()
        if not identity or row.group.strip().casefold() in queue_groups:
            continue
        if not row.url.startswith(("http://", "https://")):
            continue
        counts[identity.casefold()] = counts.get(identity.casefold(), 0) + 1
        candidates.append((index, identity, row.url, row.group.strip()))
    return [
        StreamTarget(index, identity, url, group, "primary")
        for index, identity, url, group in candidates
        if counts[identity.casefold()] == 1
    ]
