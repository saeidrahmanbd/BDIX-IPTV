# BDIX-IPTV Automation V2 — Architecture and Migration Plan

## Goal
Replace overlapping automation with one policy source, isolated playlist engines, one publication boundary, durable state, and read-only downstream consumers. This remains a branch-only implementation; it does not authorize production changes.

## Ownership and non-negotiable rules
- IPTV-Playlist.m3u is owner-curated. Existing stream URL occurrences, groups, channel numbers and relative order are immutable for routine automation. Existing rows cannot be deleted, replaced, promoted or demoted. Evidence-approved metadata/logo repairs are restricted to explicit fields. New discoveries append only to New Channels or New Backups; uncertainty is warning-only.
- International-Playlist.m3u is automation-controlled. First definitive failure goes to Review; removal requires three consecutive definitive failed Bangladesh calendar days. Missed days, ambiguous duplicate daily observations and inconclusive results reset the streak. Authentication, rate limits, geo-blocks, network errors and other HTTP failures never authorize removal.
- A recovered Review row can leave Review only after an explicitly verified working stream and classification as primary or alternate.
- New Channels and New Backups are manual-review queues and must not appear in Xtream output.
- Bangladesh and India remain fixed groups. Other country groups require five unique primary identities; group-name matching is case-insensitive. Backup, Review and discovery rows do not count.
- EPG uses candidate generation, independent XMLTV validation, active-channel mapping/schedule comparison, current/future freshness checks and explicit-approval-only aliases against last-known-good. Publication remains disabled.
- Logo repair uses authentic local assets only. Reporting is read-only and never mutates playlists.
- All candidate and state outputs use a shared transaction lock and atomic candidate-directory staging. No GitHub production publisher exists yet. Rollback will use revert or safe ref restoration, never force-push.

## Current implementation status

| Area | Current state |
|---|---|
| Baseline inventory and backup | Complete on branch; baseline commit aec37357dfbb47f0792682af744ccaf111416d7a |
| Dependency and side-effect audits | Repository-wide Python static inventory and workflow shell-boundary inventory run in the candidate bundle; dynamic/import/external-action runtime tracing remains incomplete |
| Central policy and conformance | JSON policy, schema and conformance validator implemented |
| Playlist contracts | IPTV existing-row order, URLs, groups and channel numbers protected; approved metadata repairs and queue-only discovery supported |
| IPTV engine | Combined candidate engine applies evidence-approved local metadata/logo patches and appends discoveries to manual-review queues; no production I/O |
| International engine | HTTP probe adapter, idempotent daily probe ledger, 404/410-only failure policy, verified recovery, five-identity grouping, row-identity-bound lifecycle planner, batch orchestrator and group-only candidate engine implemented |
| EPG engine | XMLTV structural/timezone validation, coverage, schedule freshness, conservative alias suggestions, explicit-approved alias application and candidate regression gate implemented |
| Run ledger | Idempotent run reservations, validated JSON serialization, Bangladesh-date probe ledger, GitHub `automation-v2-state` branch persistence and compare-and-swap writes implemented; EPG-timeout/probe-checkpoint failure injection and rollback integration tests passed in PR #154 |
| Transaction safety | Engine path allowlists, SHA-256 candidate evidence, stale-input checks, fail-closed gate, shared lock and atomic candidate-directory staging implemented; no production publisher |
| Logo audit | Playlist/runtime/report references separated; exact duplicate hashes reported; no deletion, quarantine or move |
| V2 CI | V2 contract tests and immutable baseline dry run passed in PR #154; the current missed-run scheduler branch adds date/commit-aware retry tests and must pass CI before merge |
| Legacy regression | Latest full repository regression run passed 754 tests on commit 4c66cd6e5e4822633b3f9a8fcc20710fdb2216fe |
| Real-baseline measurements | Exact production blob fingerprints verified; IPTV 1,280 rows; International 3,120 rows; EPG 30,944,668 bytes |
| Workflow migration/cutover | Shadow candidate workflow includes dashboard snapshot/mirror and runtime inventory; legacy production workflows remain enabled and unchanged; replacement/cutover is blocked by incomplete equivalence and runtime tracing |

## Verified EPG baseline
- IPTV: 776 active IDs, 411 mapped, 363 with at least one programme, 321 with current/future schedules.
- International: 2,684 active IDs, 662 mapped, 586 with at least one programme, 541 with current/future schedules.
- The baseline audit produced 19 IPTV and 60 International alias suggestions; all remain manual-review-only. Ambiguous and locale-conflicting suggestions are not auto-applied.
- No EPG alias has been published or written into the production guide.

## Verified logo audit
Repository-wide CI audit found 5,366 image assets, 2,395 distinct playlist-referenced assets, 2,691 distinct runtime-referenced assets, 2,675 assets with no explicit runtime-source reference, 718 byte-identical duplicate groups and 75 missing runtime-source targets. None of the 75 missing targets is directly referenced by either production playlist. These are review candidates only; no logo was deleted, moved or quarantined.

## Remaining migration phases
1. Inventory and baseline preservation — completed.
2. Central policy, parser contracts and regression harness — implemented; 707 full repository tests passed.
3. Candidate-only IPTV, International and EPG engines — implemented for supplied, evidence-backed inputs; real discovery/source adapters and full production-scale maintenance orchestration remain.
4. Durable state and transaction staging — JSON ledgers, per-engine allowlists, fingerprint checks, symlink-safe shared lock and atomic candidate bundle staging implemented; failure-injection and recovery tests still need expansion.
5. Immutable production baseline dry run — passed. All three candidate engines accepted unchanged baseline copies: IPTV 1,280/1,280 rows, International 3,120/3,120 rows, EPG accepted for both playlists; zero candidate changes, publish=false, production_files_modified=false.
6. Substantive candidate tests — still required for broader real discovery inputs, multi-day probe histories, approved metadata changes, large EPG candidate changes and logo quarantine manifests. A targeted EPG-timeout/probe-checkpoint failure-injection test and rollback-policy/integration tests are being added.
7. Workflow replacement — partially implemented: exact legacy writer map, missed-run recovery dispatcher, candidate-only logo proposal/approval tooling, immutable dashboard input snapshot, separate dashboard parity mirror and runtime inventory are present. Independent dashboard metric parity, dynamic logo-reference parity, resolved runtime boundaries, full workflow equivalence and one-writer acceptance across every legacy writer remain.
8. Publication and rollback — candidate publication is prepared as a three-file owner-review PR only; a separate explicit-confirmation workflow now prepares a revert PR for a previously merged V2 publication, restricted to the three allowlisted outputs. Both remain PR-only; automatic main publication/merge is deliberately absent.
9. Prepare a reviewable migration PR with exact workflow retirement/replacement map — map is in place; cutover PR remains blocked by incomplete parity and acceptance.
10. Only after all gates pass, prepare a separate owner-reviewed production cutover — not authorized or started.

## Safety boundary
- No V2 workflow may publish production playlists or EPG during migration.
- Do not delete old scripts/workflows until replacements are tested and mapped.
- Never weaken owner-protection checks to make failed runs green.
- Do not disable existing workflows before full replacement validation and rollback testing.
- Never force-push; rollback uses revert or safe ref restoration.
