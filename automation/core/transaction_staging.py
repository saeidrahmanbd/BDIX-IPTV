"""Atomic multi-engine candidate transaction staging; production publishing is deliberately absent."""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import tempfile
from automation.core.atomic_output import transaction_lock
from automation.core.candidate_manifest import CandidateManifest
from automation.core.transaction_bundle import TransactionBundleDecision, evaluate_bundle
from automation.core.transaction_gate import ArtifactEvidence

def _digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def stage_transaction_bundle(root: str | Path, transaction_id: str,
                             manifests: list[CandidateManifest],
                             artifacts: list[ArtifactEvidence],
                             candidate_contents: dict[str,str],
                             expected_baseline_commit: str) -> Path:
    """Stage every engine output together only when all transaction gates and content hashes pass."""
    if not re.fullmatch(r"[A-Za-z0-9._-]{1,128}",transaction_id):
        raise ValueError("transaction_id is invalid")
    decision=evaluate_bundle(manifests,artifacts,expected_baseline_commit)
    if not decision.ready_for_owner_review or decision.publish:
        raise ValueError("transaction bundle has not passed all gates or is marked publishable")
    declared={path for manifest in manifests for path in manifest.changed_paths}
    if set(candidate_contents)!=declared:
        raise ValueError("candidate content paths do not match transaction manifests")
    for manifest in manifests:
        for path in manifest.changed_paths:
            if manifest.candidate_fingerprints.get(path)!=_digest(candidate_contents[path]):
                raise ValueError(f"candidate content fingerprint mismatch: {path}")
    base=Path(root).resolve()
    parent=base
    for part in ("reports","automation-v2","candidates","transactions"):
        parent=parent/part
        if parent.is_symlink():
            raise ValueError("transaction output directory cannot traverse a symlink")
        parent.mkdir(exist_ok=True)
        if not parent.resolve().is_relative_to(base):
            raise ValueError("transaction output directory escapes repository root")
    target=parent/transaction_id
    with transaction_lock(base):
        if target.exists():
            raise FileExistsError(f"transaction bundle already exists: {transaction_id}")
        stage=Path(tempfile.mkdtemp(prefix=".staging-",dir=parent))
        try:
            for relative,content in sorted(candidate_contents.items()):
                path=PurePosixPath(relative)
                if path.is_absolute() or ".." in path.parts or not path.parts:
                    raise ValueError("candidate content path is unsafe")
                output=stage/Path(*path.parts)
                output.parent.mkdir(parents=True,exist_ok=True)
                with output.open("w",encoding="utf-8",newline="") as stream:
                    stream.write(content)
                    stream.flush()
                    os.fsync(stream.fileno())
            metadata={
                "schema_version":1,
                "transaction_id":transaction_id,
                "baseline_commit":expected_baseline_commit,
                "engines":sorted(manifest.engine for manifest in manifests),
                "candidate_fingerprints":{path:_digest(value) for path,value in sorted(candidate_contents.items())},
                "ready_for_owner_review":True,
                "publish":False,
                "errors":[],
            }
            metadata_path=stage/"transaction-bundle.json"
            with metadata_path.open("w",encoding="utf-8") as stream:
                json.dump(metadata,stream,indent=2,sort_keys=True)
                stream.write("\n")
                stream.flush()
                os.fsync(stream.fileno())
            os.replace(stage,target)
            directory_fd=os.open(parent,os.O_RDONLY)
            try:
                os.fsync(directory_fd)
            finally:
                os.close(directory_fd)
        except Exception:
            import shutil
            shutil.rmtree(stage,ignore_errors=True)
            raise
    return target
