# Legacy workflow retirement and V2 replacement map

Baseline: 46275f5ebafa2ae1b56f3e480f684ac1e85ae45e  
Audit branch: automation-v2/inventory-audit

This is a migration plan only. No legacy workflow is disabled, edited or retired by this document.

## Workflows to consolidate under V2

| Legacy workflow | Current production responsibility | Planned V2 owner | Retirement condition |
|---|---|---|---|
| Discovery Schedule Watchdog | Dispatches multiple workflows at checkpoints; second scheduling authority | One idempotent scheduler/run-ledger entry point | Durable run ledger, missed-run recovery and single-writer queue pass tests |
| IPTV Playlist Update | Monolithic maintenance writes both playlists, reports, logos and dashboard | Split IPTV and International candidate engines plus one publisher | Exact workflow-to-script dependency parity, owner-protection tests and rollback pass |
| IPTV New Channel Discovery | Writes IPTV discovery rows and reports | IPTV discovery input adapter; candidate engine appends only to New Channels/New Backups | Discovery source adapters, duplicate checks, queue visibility and candidate tests pass |
| International Channel Discovery | Writes International playlist and reports | International discovery input adapter and candidate engine | Discovery source adapters and country/identity/category tests pass |
| International Stream Health | Probes and may rewrite International playlist/history/reports | International probe ledger, lifecycle policy and group-only candidate engine | Multi-day real-probe fixture tests, state persistence, failure injection and removal-review gates pass |
| Refresh IPTV EPG | Multiple triggers/listeners; generates and publishes guide/mappings/reports/dashboard | EPG candidate engine, alias review and last-known-good publisher | Source adapters, full-guide quality/coverage tests, atomic publication and rollback pass |
| IPTV Logo Localization | IPTV playlist/logo mutations | Shared logo repair engine with local-asset validation | Full dynamic-reference audit and candidate-only logo repair tests pass |
| Playlist Logo Repair and Localization | Mutates both playlists and logo assets/provenance | Shared logo repair engine with per-playlist ownership scopes | Both playlist scopes and rollback proven; no hidden staging or cross-playlist writes |
| Generate Dashboard (nested) | Multiple workflow paths regenerate dashboard/reports | Read-only report consumer of immutable published snapshots | One report producer and snapshot freshness checks pass |

## Workflows to retain as separate services

| Workflow | Planned treatment |
|---|---|
| Changelog | Retain as a post-publication report stage; remove any playlist mutation authority |
| Daily Xtream Health Check | Retain as read-only gateway validation with simplified trigger policy |
| Deploy IPTV Analytics | Retain as infrastructure deployment, not playlist writer |
| Deploy Xtream Gateway | Retain as infrastructure deployment with live verification |
| Probe EPG sources for Bangladesh | Retain as isolated research/probe utility; its outputs are candidate evidence only |
| Probe amazeyourself EPG sources | Retain as isolated research/probe utility; its outputs are candidate evidence only |
| IndexNow | Retain as separate search-engine notification |
| Validate Website SEO | Retain as read-only validation |
| Test Suite | Retain and expand as central regression gate |

## V2 readiness snapshot

- Candidate-only IPTV engine: implemented for approved metadata/logo patches and supplied discovery candidates.
- Candidate-only International engine: implemented for supplied probe targets, durable probe ledger observations, lifecycle decisions and group-only changes.
- Candidate-only EPG engine: implemented for structural validation, active-channel coverage/freshness checks and explicit-approved alias additions.
- Candidate transaction infrastructure: per-engine allowlists, SHA-256 evidence, stale-input rejection, shared lock, append-only run ledger and atomic candidate-directory staging.
- Verification: 168 V2 tests and 699 full repository tests passed on commit 568177d9a87a1a693a52a7d7722cf1391689c0f8; all three candidate engines passed an immutable no-change baseline dry run.
- Not ready for production: discovery-source adapters, production Git publisher, durable state commit/recovery, exhaustive dynamic side-effect tracing, failure-injection/rollback and complete workflow equivalence remain open.

## Required cutover sequence

1. Finish source-adapter and real-candidate fixture tests for each engine.
2. Prove the V2 publisher is the only writer, with a durable queue/lock and stale-baseline checks.
3. Prove atomic playlist+state+EPG transaction behavior, failure recovery and rollback against a disposable test branch.
4. Create a draft PR with exact legacy workflow files to retire and their V2 replacements.
5. Review the PR and all candidate artifacts; keep main production workflows active until the cutover change is ready.
6. In a separate approved cutover change, transfer schedules and disable only the replaced legacy writers. Keep read-only and infrastructure workflows.
7. Verify the first production transaction and rollback path before enabling recurring schedules.

No force-push, broad workflow deletion or direct playlist mutation is permitted during migration.
