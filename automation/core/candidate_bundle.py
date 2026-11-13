"""Build in-memory candidate manifests and validation evidence; never writes or publishes."""
from __future__ import annotations
import hashlib
from dataclasses import dataclass
from automation.core.candidate_manifest import CandidateManifest
from automation.core.transaction_gate import ArtifactEvidence, TransactionDecision, evaluate_transaction

@dataclass(frozen=True)
class CandidateBundle:
    manifest: CandidateManifest
    evidence: tuple[ArtifactEvidence, ...]
    decision: TransactionDecision
    publish: bool = False

def _sha256(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()

def build_candidate_bundle(engine: str, baseline_commit: str,
                           baseline_contents: dict[str,str],
                           candidate_contents: dict[str,str],
                           validator_results: dict[str,bool]) -> CandidateBundle:
    """Create a deterministic evidence bundle; all declared paths must have baseline and validator evidence."""
    if not candidate_contents:
        raise ValueError("candidate bundle cannot be empty")
    paths = tuple(sorted(candidate_contents))
    if set(paths) != set(baseline_contents):
        raise ValueError("candidate and baseline path sets must match exactly")
    if set(paths) != set(validator_results):
        raise ValueError("every candidate path requires an explicit validator result")
    fingerprints = {path:_sha256(candidate_contents[path]) for path in paths}
    manifest = CandidateManifest(engine,baseline_commit,paths,fingerprints)
    evidence = tuple(
        ArtifactEvidence(
            path,
            _sha256(baseline_contents[path]),
            fingerprints[path],
            _sha256(baseline_contents[path]),
            _sha256(candidate_contents[path]),
            validator_results[path],
        )
        for path in paths
    )
    decision = evaluate_transaction(manifest,list(evidence),baseline_commit)
    return CandidateBundle(manifest,evidence,decision,False)
