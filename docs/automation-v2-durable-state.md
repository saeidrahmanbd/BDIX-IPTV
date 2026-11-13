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

The manual/push-triggered workflow `Automation V2 State Store Check` verifies read/write access without changing ledger entries. The shadow candidate-bundle runner now connects the IPTV discovery engine, International discovery/maintenance engine, and isolated EPG source generator. It validates all three outputs against one baseline, verifies the remote `main` ref both before generation and immediately before staging, stages them as one atomic owner-review transaction, and checkpoints the dated International probe ledger immediately after stream probing, before the slower EPG stage, then persists the final run outcome to the state branch. This preserves completed probe history even if EPG acquisition subsequently fails. Review rows are probed as well; a recovery destination is inferred only from explicit country/language/content metadata, while ambiguous identities remain untouched. Primary and Review rows are removed from the candidate only after three consecutive Bangladesh-calendar-day HTTP 404/410 failures for the same exact URL; transient, authentication, rate-limit, geo-block, missing-day, and changed-URL observations never carry a removal streak. Backup and discovery-queue rows are protected from automatic removal. Each probe is bound to a SHA-256 fingerprint of its exact stream URL, so a changed URL is probed again and cannot inherit the previous URL's failure streak. The Automation V2 Candidate Bundle workflow runs on a main-branch push affecting the V2 candidate runner and can also be dispatched manually. It uploads candidate artifacts and does not publish production files.

The existing scheduled production workflows remain on the legacy path. The V2 shadow workflow must first complete a real mainline run and produce a valid three-engine candidate artifact. Failure-injection, stale-baseline, state-store conflict/recovery, and migration acceptance checks must then pass before production workflow cutover. No V2 candidate may be published to production before that acceptance gate; three-day removals remain candidate-only until an approved production cutover.
