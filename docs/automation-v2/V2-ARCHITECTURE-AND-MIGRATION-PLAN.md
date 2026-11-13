# BDIX-IPTV Automation V2 — Architecture and Migration Plan

## Goal
Replace overlapping automation with one policy source, isolated playlist engines, one publication boundary, and read-only downstream consumers. This remains a branch-only implementation; it does not authorize production changes.

## Ownership and non-negotiable rules
- IPTV-Playlist.m3u is owner-curated. Existing stream URL occurrences, groups, channel numbers and relative order are immutable for routine automation. Existing rows cannot be deleted, replaced, promoted or demoted. New discoveries append only to New Channels or New Backups; uncertainty is warning-only.
- International-Playlist.m3u is automation-controlled. First definitive failure goes to Review; removal requires three consecutive definitive failed Bangladesh calendar days. Missed days, ambiguous duplicate daily observations and inconclusive results reset the streak. Authentication, rate limits, geo-blocks, network errors and other HTTP failures never authorize removal.
- A recovered Review row can leave Review only after an explicitly verified working stream and classification as primary or alternate.
- New Channels and New Backups are manual-review queues and must not appear in Xtream output.
- Bangladesh and India remain fixed groups. Other country groups require five unique primary identities; group-name matching is case-insensitive. Backup, Review and discovery rows do not count.
- EPG uses candidate generation, independent XMLTV validation and a last-known-good gate. Publication remains disabled.
- Logo repair uses authentic local assets only. Reporting is read-only and never mutates playlists.
- One future serialized publisher is the only permitted write boundary. Rollback uses revert or safe ref restoration, never force-push.

## Current implementation status

| Area | Current state |
|---|---|
| Baseline inventory and backup | Complete on branch; baseline commit 46275f5ebafa2ae1b56f3e480f684ac1e85ae45e |
| Dependency and side-effect audits | Static audit complete; dynamic runtime tracing remains incomplete |
| Central policy and policy conformance | Initial policy, schema and conformance checks added |
| Playlist contracts | IPTV preservation invariants and discovery queue visibility checks added |
| IPTV engine | Candidate-only discovery append engine added; no production file I/O |
| International engine | Failure lifecycle, verified recovery decisions, country-group threshold and group-only candidate builder added |
| EPG engine | XMLTV structural validator and last-known-good candidate gate added; full schedule coverage/freshness analysis pending |
| Logo audit | Explicit reference scan and exact byte-duplicate report added; no deletion or quarantine |
| Transaction safety | Candidate manifest and fail-closed transaction readiness evaluator added; no publisher |
| CI | Branch-only workflow exists; latest Actions run must complete successfully before tests can be called passed |
| Full migration and legacy regression | Not started |

## Logo audit status
The initial playlist-only exact-reference scan found 5,366 image assets, 2,395 referenced by the two playlist files, and 2,971 apparent non-references. These are not confirmed unused. The repository-wide scanner now checks explicit text references and byte-identical duplicates, but dynamically constructed references and visual duplicates with different bytes still need manual/automated review. No logo has been deleted, moved or quarantined.

## Migration phases
1. Inventory and baseline preservation — completed.
2. Central policy and contract tests — initial implementation added; CI result pending.
3. Port parsers and identity helpers with equivalence tests — initial parser and candidate invariants added; full equivalence suite pending.
4. Build isolated IPTV and International engines that produce candidates only — initial candidate engines added; broader normalization, identity resolution and category ordering remain.
5. Port discovery, logos and EPG behind scoped interfaces — logo scanner and EPG validator/gate added; source integration and coverage analysis remain.
6. Run all V2 tests and relevant legacy regression tests; classify obsolete tests rather than deleting blindly.
7. Generate dry-run candidates from immutable baseline copies and prove all invariants.
8. Test transaction failure, stale-input rejection, rollback and last-known-good EPG.
9. Prepare a draft migration PR with exact workflow retirement/replacement map.
10. Only after all checks pass, prepare a separate owner-reviewed production cutover.

## Safety boundary
- No V2 workflow may publish production playlists or EPG during migration.
- Do not delete old scripts/workflows until replacements are tested and mapped.
- Never weaken owner-protection checks to make failed runs green.
- Do not disable existing workflows before full replacement validation and rollback testing.
- Never force-push; rollback uses revert or safe ref restoration.
