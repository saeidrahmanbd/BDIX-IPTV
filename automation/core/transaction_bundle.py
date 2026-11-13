"""Cross-engine transaction bundle gate for the future single publisher."""
from __future__ import annotations
from dataclasses import dataclass
from automation.core.candidate_manifest import CandidateManifest
from automation.core.transaction_gate import ArtifactEvidence, evaluate_transaction

@dataclass(frozen=True)
class TransactionBundleDecision:
    ready_for_owner_review: bool
    publish: bool
    errors: tuple[str, ...]

def evaluate_bundle(manifests: list[CandidateManifest], artifacts: list[ArtifactEvidence],
                    expected_baseline_commit: str,
                    active_transaction_id: str | None = None) -> TransactionBundleDecision:
    """Validate a multi-engine candidate set; publication is unconditionally disabled."""
    errors: list[str] = []
    if active_transaction_id:
        errors.append("another publication transaction holds the global lock")
    if not manifests:
        errors.append("transaction bundle contains no engine manifests")
    engines = [manifest.engine for manifest in manifests]
    if len(set(engines)) != len(engines):
        errors.append("transaction bundle contains duplicate engine manifests")
    paths = [path for manifest in manifests for path in manifest.changed_paths]
    if len(set(paths)) != len(paths):
        errors.append("transaction bundle contains overlapping output paths")
    if any(manifest.baseline_commit != expected_baseline_commit for manifest in manifests):
        errors.append("all engine manifests must use the same approved baseline commit")
    artifact_map = {item.path:item for item in artifacts}
    if len(artifact_map) != len(artifacts):
        errors.append("transaction bundle contains duplicate artifact evidence")
    if set(artifact_map) != set(paths):
        errors.append("transaction bundle evidence does not exactly match declared output paths")
    for manifest in manifests:
        scoped = [artifact_map[path] for path in manifest.changed_paths if path in artifact_map]
        decision = evaluate_transaction(manifest,scoped,expected_baseline_commit)
        errors.extend(f"{manifest.engine}: {error}" for error in decision.errors)
    ready = not errors
    return TransactionBundleDecision(ready,False,tuple(errors))
