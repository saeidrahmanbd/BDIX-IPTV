# BDIX-IPTV Automation V2 — Architecture and Migration Plan

## Goal
Replace overlapping automation with one policy source, isolated playlist engines, one publication boundary, and read-only downstream consumers. This remains a branch-only implementation; it does not authorize production changes.

## Ownership and non-negotiable rules
- IPTV-Playlist.m3u is owner-curated. Existing stream URL occurrences, groups, channel numbers and relative order are immutable for routine automation. Existing rows cannot be deleted, replaced, promoted or demoted. New discoveries append only to New Channels or New Backups; uncertainty is warning-only.
- International-Playlist.m3u is automation-controlled. First definitive failure goes to Review; removal requires three consecutive definitive failed Bangladesh calendar days. Missed days, ambiguous duplicate daily observations and inconclusive results reset the streak. Authentication, rate limits, geo-blocks, network errors and other HTTP failures never authorize removal.
- A recovered Review row can leave Review only after an explicitly verified working stream and classification as primary or alternate.
- New Channels and New Backups are manual-review queues and must not appear in Xtream output.
- Bangladesh and India remain fixed groups. Other country groups require five unique primary identities; group-name matching is case-insensitive. Backup, Review and discovery rows do not count.
- EPG uses candidate generation, independent XMLTV validation, active-channel mapping/schedule comparison, current/future freshness checks and manual-only alias suggestions against last-known-good. Publication remains disabled.
- Logo repair uses authentic local assets only. Reporting is read-only and never mutates playlists.
- A deterministic run ledger and cross-engine transaction bundle gate are implemented as pure policies. A future serialized publisher is the only permitted write boundary. Rollback uses revert or safe ref restoration, never force-push.

## Current implementation status

| Area | Current state |
|---|---|
| Baseline inventory and backup | Complete on branch; baseline commit 46275f5ebafa2ae1b56f3e480f684ac1e85ae45e |
| Dependency and side-effect audits | Static audit complete; dynamic runtime tracing remains incomplete |
| Central policy and policy conformance | Initial policy, schema and conformance checks added |
| Playlist contracts | IPTV existing rows must remain an unchanged prefix; metadata/logo repair allowed; discovery rows append only |
| IPTV engine | Candidate-only discovery append and evidence-gated local metadata/logo repair engines added; no production file I/O |
| International engine | Failure lifecycle, verified recovery decisions, five-identity country-group threshold and group-only candidate builder added |
| EPG engine | XMLTV structural, mapping coverage, future-schedule freshness and conservative alias suggestion checks added |
| Run ledger | Deterministic idempotency keys, per-engine run exclusion and global transaction-lock policy added; durable persistence not yet implemented |
| Transaction safety | Per-engine manifests, stale-input checks and cross-engine bundle gate added; no publisher |
| Logo audit | Playlist/runtime/report references separated; exact duplicate hashes reported; no deletion or quarantine |
| V2 CI | Latest verified branch CI passed **118 tests** and completed the immutable production dry run |
| Legacy regression | Latest full repository run passed **649 tests** with repository-declared image dependencies installed |
| Real-baseline dry runs | Completed read-only: exact production blob fingerprints verified; IPTV 1,280 rows; International 3,120 rows; EPG 30,944,668 bytes |
| EPG mapping review | Baseline coverage audited; 79 manual-only alias suggestions and 14 ambiguous cases produced; none applied |
| Workflow migration/cutover | Not started; legacy workflows remain enabled |

## Verified EPG baseline

- IPTV: 776 active IDs, 411 mapped, 363 with any programme, 321 with current/future schedules.
- International: 2,684 active IDs, 662 mapped, 586 with any programme, 541 with current/future schedules.
- Alias suggestions are manual-only and include locale-conflict and ambiguous-match checks. See EPG-BASELINE-COVERAGE-AUDIT.md.

## Verified logo audit

Repository-wide CI audit found 5,366 image assets, 2,395 distinct playlist-referenced assets, 2,691 distinct runtime-referenced assets, 2,675 assets with no explicit runtime-source reference, 718 byte-identical duplicate groups and 75 missing runtime-source targets. No missing target was directly referenced by either production playlist. These remain review candidates only; no logo was deleted or moved. See LOGO-STORAGE-AUDIT.md.

## Migration phases
1. Inventory and baseline preservation — completed.
2. Central policy and contract tests — initial implementation added and passing.
3. Port parsers and identity helpers with equivalence tests — initial parser and invariants added; real-playlist equivalence coverage still needs expansion.
4. Build isolated IPTV and International engines that produce candidates only — initial candidate engines added; broader normalization, identity resolution, stream-health evidence integration and category ordering remain.
5. Port discovery, logos and EPG behind scoped interfaces — logo scanner, EPG validation/coverage/freshness/alias suggestions and run-ledger policy added; discovery source integration and durable state remain.
6. Run all V2 tests and relevant legacy regression tests — **639 repository tests passed**; continue adding regression cases as engines are ported.
7. Generate dry-run candidates from immutable baseline copies and prove all invariants — first exact-baseline dry run passed; substantive discovery/maintenance candidates still pending.
8. Test transaction failure, stale-input rejection, durable lock recovery, rollback and last-known-good EPG — pure gates tested; persistence, failure injection and rollback integration tests pending.
9. Prepare a draft migration PR with exact workflow retirement/replacement map — pending.
10. Only after all checks pass, prepare a separate owner-reviewed production cutover — not authorized or started.

## Safety boundary
- No V2 workflow may publish production playlists or EPG during migration.
- Do not delete old scripts/workflows until replacements are tested and mapped.
- Never weaken owner-protection checks to make failed runs green.
- Do not disable existing workflows before full replacement validation and rollback testing.
- Never force-push; rollback uses revert or safe ref restoration.
