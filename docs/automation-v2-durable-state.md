# Automation V2 durable state

Automation V2 keeps run reservations and International stream observations across disposable GitHub Actions runners in the dedicated `automation-v2-state` branch. The branch contains only the state snapshot file as its mutable state payload:

- `automation-v2-state.json`
- `run_ledger`: idempotency reservations and terminal outcomes
- `international_probe_ledger`: dated stream observations used by the three-definitive-days policy

## Safety contract

- State writes use the GitHub Contents API and the branch's current blob SHA (compare-and-swap).
- A 409/422 conflict, malformed state, missing credentials, API outage, or unsupported schema fails closed. Callers must not proceed using empty in-memory state after a failed remote read.
- Writers must share the `automation-v2-state-store` GitHub Actions concurrency group. The blob SHA check is an additional guard against lost updates.
- The state branch is separate from `main`; it is never merged into production.
- No playlist, EPG, logo, or workflow file is written by the state-store module.
- State must be treated as operational data, not as a backup of production playlists.

## API use

Set `GITHUB_REPOSITORY`, `AUTOMATION_V2_STATE_BRANCH=automation-v2-state`, and `GITHUB_TOKEN` in the calling workflow. The token requires `contents: write` only for the dedicated state operation. Load a `StateSnapshot`, update the validated ledgers, then save using the snapshot's `blob_sha`. If a write conflicts, reload and recompute; never retry the stale payload.

The manual workflow `Automation V2 State Store Check` verifies read/write access without changing ledger entries. The store adapter is not yet wired into the IPTV, International, or EPG scheduled engines; that integration remains a migration gate. Until it is integrated and exercised by end-to-end tests, no stream-removal or production publication decision may rely on this store.
