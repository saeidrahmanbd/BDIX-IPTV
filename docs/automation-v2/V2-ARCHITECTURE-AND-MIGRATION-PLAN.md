# BDIX-IPTV Automation V2 — Architecture and Migration Plan

## Goal
Replace overlapping automation with one policy source, isolated playlist engines, one publication boundary, and read-only downstream consumers. This is a design and branch-only implementation; it does not authorize production changes.

## Ownership
- IPTV-Playlist.m3u is owner-curated. Existing stream URL occurrences, groups, channel numbers and relative order are immutable for routine automation. Existing rows cannot be deleted, replaced, promoted or demoted. Evidence-based metadata and authentic local-logo repair are allowed. New discoveries append only to New Channels or New Backups; uncertainty is warning-only.
- International-Playlist.m3u is automation-controlled. First definitive failure goes to Review; removal requires three consecutive definitive failed Bangladesh calendar days. Missed days reset the streak. Authentication, rate limits, geo-blocks, network errors and inconclusive results never authorize removal.
- New Channels and New Backups are manual-review queues and must not appear in Xtream output.
- Bangladesh and India remain fixed groups. Other country groups require five unique primary identities; Backup, Review and discovery rows do not count.
- EPG uses candidate generation, independent validation and atomic last-known-good publication.
- Logo repair uses authentic local assets only. Reporting is read-only and never mutates playlists.

## Target flow
scheduler -> run ledger -> policy resolver -> scoped engine -> candidate artifact -> validators -> single publisher -> read-only consumers

## Migration phases
1. Inventory and baseline preservation — completed.
2. Central policy and contract tests — in progress.
3. Port parsers and identity helpers with equivalence tests.
4. Build isolated IPTV and International engines that produce candidates only.
5. Port discovery, logos and EPG behind scoped interfaces.
6. Run all existing and V2 tests; classify obsolete tests instead of deleting blindly.
7. Generate dry-run candidates from baseline copies and prove invariants.
8. Test transaction failure, stale-input rejection, rollback and last-known-good EPG.
9. Open a draft PR with exact workflow retirement/replacement map.
10. Only after all checks pass, prepare a separate owner-reviewed production cutover.

## Non-negotiable safeguards
- No V2 workflow may publish production playlists during migration.
- Do not delete old scripts/workflows until replacements are tested and mapped.
- Never weaken owner-protection checks to make failed runs green.
- Do not disable existing workflows before full replacement validation and rollback testing.
- Never force-push; rollback uses revert or safe ref restoration.
