"""Manual read/write smoke test for the isolated Automation V2 state branch."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from automation.core.github_state_store import store_from_environment

def main() -> int:
    store = store_from_environment()
    snapshot = store.load()
    # Saving the exact validated snapshot exercises GitHub's conditional write
    # without changing either ledger's semantic contents.
    new_sha = store.save(snapshot.state, snapshot.blob_sha)
    reloaded = store.load()
    if reloaded.state != snapshot.state or reloaded.blob_sha != new_sha:
        raise RuntimeError("durable state read-after-write verification failed")
    print("Automation V2 durable state read/write check passed.")
    print(f"State branch: {store.branch}")
    print(f"State file: automation-v2-state.json")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
