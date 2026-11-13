"""Serialized, atomic writes restricted to V2 candidate/state outputs; never production playlist paths."""
from __future__ import annotations
from contextlib import contextmanager
import os
from pathlib import Path, PurePosixPath
import tempfile
import fcntl

ALLOWED_PREFIXES = ("reports/automation-v2/candidates/","reports/automation-v2/state/")

def _safe_target(root: Path, relative_path: str) -> Path:
    relative=PurePosixPath(relative_path)
    if relative.is_absolute() or ".." in relative.parts or not any(relative_path.startswith(prefix) for prefix in ALLOWED_PREFIXES):
        raise ValueError("write target is outside V2 candidate/state output directories")
    resolved_root=root.resolve()
    target=(resolved_root/Path(*relative.parts)).resolve()
    if not target.is_relative_to(resolved_root):
        raise ValueError("write target escapes repository root")
    return target

@contextmanager
def transaction_lock(root: str | Path):
    """Acquire the one shared V2 publisher lock."""
    base=Path(root).resolve()
    state_dir=base/"reports"/"automation-v2"/"state"
    state_dir.mkdir(parents=True,exist_ok=True)
    resolved_state=state_dir.resolve()
    if not resolved_state.is_relative_to(base):
        raise ValueError("publisher lock directory escapes repository root")
    lock_path=resolved_state/".publisher.lock"
    if lock_path.is_symlink():
        raise ValueError("publisher lock file cannot be a symlink")
    descriptor=os.open(lock_path,os.O_CREAT|os.O_RDWR,0o600)
    try:
        fcntl.flock(descriptor,fcntl.LOCK_EX)
        yield
    finally:
        fcntl.flock(descriptor,fcntl.LOCK_UN)
        os.close(descriptor)

def atomic_write_v2_output(root: str | Path, relative_path: str, content: str) -> Path:
    """Atomically replace a V2 candidate/state output under the shared publisher lock."""
    base=Path(root).resolve()
    target=_safe_target(base,relative_path)
    target.parent.mkdir(parents=True,exist_ok=True)
    encoded=content.encode("utf-8")
    with transaction_lock(base):
        descriptor,temp_name=tempfile.mkstemp(prefix=".v2-tmp-",dir=target.parent)
        try:
            with os.fdopen(descriptor,"wb") as stream:
                stream.write(encoded)
                stream.flush()
                os.fsync(stream.fileno())
            os.replace(temp_name,target)
            directory_fd=os.open(target.parent,os.O_RDONLY)
            try:
                os.fsync(directory_fd)
            finally:
                os.close(directory_fd)
        except Exception:
            try:
                os.unlink(temp_name)
            except FileNotFoundError:
                pass
            raise
    return target
