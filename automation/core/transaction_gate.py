"""Pure all-gates transaction readiness evaluator. It never publishes or writes files."""
from __future__ import annotations
from dataclasses import dataclass
from automation.core.candidate_manifest import CandidateManifest, validate_manifest

@dataclass(frozen=True)
class ArtifactEvidence:
    path: str
    baseline_sha256: str
    candidate_sha256: str
    baseline_current_sha256: str
    candidate_current_sha256: str
    validator_passed: bool

@dataclass(frozen=True)
class TransactionDecision:
    ready_for_owner_review: bool
    publish: bool
    errors: tuple[str, ...]

def _valid_sha256(value: str) -> bool:
    return len(value) == 64 and all(char in "0123456789abcdefABCDEF" for char in value)

def evaluate_transaction(manifest: CandidateManifest, artifacts: list[ArtifactEvidence],
                         expected_baseline_commit: str) -> TransactionDecision:
    """Require fresh baseline, matching fingerprints and passing validators for every path."""
    errors = validate_manifest(manifest)
    if manifest.baseline_commit != expected_baseline_commit:
        errors.append("baseline commit does not match the approved migration baseline")
    by_path = {item.path: item for item in artifacts}
    if len(by_path) != len(artifacts):
        errors.append("duplicate artifact evidence")
    if set(by_path) != set(manifest.changed_paths):
        errors.append("artifact evidence does not exactly match manifest paths")
    for path, evidence in by_path.items():
        if not _valid_sha256(evidence.baseline_sha256) or not _valid_sha256(evidence.baseline_current_sha256):
            errors.append(f"invalid baseline SHA-256 evidence: {path}")
        if not _valid_sha256(evidence.candidate_sha256) or not _valid_sha256(evidence.candidate_current_sha256):
            errors.append(f"invalid candidate SHA-256 evidence: {path}")
        if evidence.baseline_sha256 != evidence.baseline_current_sha256:
            errors.append(f"stale baseline input: {path}")
        if evidence.candidate_sha256 != evidence.candidate_current_sha256:
            errors.append(f"candidate fingerprint mismatch: {path}")
        if manifest.candidate_fingerprints.get(path) != evidence.candidate_sha256:
            errors.append(f"manifest fingerprint mismatch: {path}")
        if not evidence.validator_passed:
            errors.append(f"validator failed: {path}")
    ready = not errors
    return TransactionDecision(ready,False,tuple(errors))
