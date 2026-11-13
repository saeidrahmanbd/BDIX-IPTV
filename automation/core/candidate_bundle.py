"""Build in-memory candidate manifests and validation evidence; never writes or publishes."""
from __future__ import annotations
import hashlib
import json
import os
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
import re
import tempfile
from automation.core.atomic_output import transaction_lock
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


def write_candidate_bundle(root: str | Path, run_id: str, bundle: CandidateBundle,
                           candidate_contents: dict[str,str]) -> Path:
    """Publish a complete candidate directory atomically; production files remain untouched."""
    if not re.fullmatch(r"[A-Za-z0-9._-]{1,128}",run_id):
        raise ValueError("run_id is invalid")
    if not bundle.decision.ready_for_owner_review or bundle.publish:
        raise ValueError("candidate bundle has not passed all gates or is marked publishable")
    if set(candidate_contents) != set(bundle.manifest.changed_paths):
        raise ValueError("candidate content paths do not match the validated manifest")
    base=Path(root).resolve()
    parent=base/"reports"/"automation-v2"/"candidates"
    parent.mkdir(parents=True,exist_ok=True)
    target=parent/run_id
    with transaction_lock(base):
        if target.exists():
            raise FileExistsError(f"candidate bundle already exists: {run_id}")
        stage=Path(tempfile.mkdtemp(prefix=".staging-",dir=parent))
        try:
            for relative,content in candidate_contents.items():
                path=PurePosixPath(relative)
                if path.is_absolute() or ".." in path.parts:
                    raise ValueError("candidate content path is unsafe")
                output=stage/Path(*path.parts)
                output.parent.mkdir(parents=True,exist_ok=True)
                with output.open("w",encoding="utf-8",newline="") as stream:
                    stream.write(content)
                    stream.flush()
                    os.fsync(stream.fileno())
            metadata={
                "engine":bundle.manifest.engine,
                "baseline_commit":bundle.manifest.baseline_commit,
                "changed_paths":list(bundle.manifest.changed_paths),
                "candidate_fingerprints":bundle.manifest.candidate_fingerprints,
                "ready_for_owner_review":bundle.decision.ready_for_owner_review,
                "publish":False,
                "errors":list(bundle.decision.errors),
            }
            metadata_path=stage/"candidate-bundle.json"
            with metadata_path.open("w",encoding="utf-8") as stream:
                json.dump(metadata,stream,indent=2,sort_keys=True)
                stream.write("\\n")
                stream.flush()
                os.fsync(stream.fileno())
            os.replace(stage,target)
            dir_fd=os.open(parent,os.O_RDONLY)
            try:
                os.fsync(dir_fd)
            finally:
                os.close(dir_fd)
        except Exception:
            import shutil
            shutil.rmtree(stage,ignore_errors=True)
            raise
    return target
