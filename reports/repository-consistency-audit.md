# Repository Consistency Audit

Generated: 2026-10-23

## Scope

This audit covers the repository description, README scope, playlist/report counting, active review queues, metadata identity, backup reporting, health-check semantics, EPG wording, Xtream documentation, workflow concurrency, and repository hygiene.

## Findings and disposition

| Area | Finding | Disposition |
|---|---|---|
| Repository identity | Repository description already correctly says Bangladesh & India | Verified |
| Playlist scope | README presents Bangladesh, India and selected international content | Kept; clarified hub positioning in project documentation |
| Review queues | `New Channels` and `New Backup` are active discovery/validation queues | Kept active; documentation is aligned |
| Primary counts | Active-primary counts must exclude review queues | Enforced in dashboard/report scope |
| EPG counts | EPG IDs audited use a separate published-guide scope | Explicitly documented |
| Near-duplicate families | Health report detected URL families but dashboard parsed the wrong metric | Added report reconciliation so the count is explicit and current |
| Metadata conflicts | Audit originally focused on non-review records, allowing queue variants to escape the headline count | Added cross-queue metadata reconciliation and known-name normalization |
| Raw name tags | Resolution and geo-block presentation tags are not channel identity | Consistency repair strips them from `tvg-name` |
| Backup independence | Backup rows are not guaranteed independent infrastructure | README/report wording treats backups as references; independence is audited separately |
| Health failures | GitHub-hosted runner results can be affected by geography/authentication | Health report identifies runner context and treats 401/403/timeouts as review signals |
| EPG marketing | Programme coverage is measured, not guaranteed | README uses monitoring language |
| Xtream docs | `xtream/README.md` exists | Verified; links target the Xtream documentation structure |
| Writer concurrency | Playlist writers must share one concurrency group | `iptv-playlist-main-writer` is the shared writer queue |
| Repository hygiene | LICENSE, SECURITY and CONTRIBUTING are present | Verified |
| Static maintenance badge | A dynamic Actions badge is used in the current README | Verified |

## Automated safeguards added

1. `scripts/reconcile_playlist_consistency.py`
   - normalizes known channel-name variants;
   - strips presentation-only resolution/geo-block tags from names;
   - canonicalizes unambiguous review IDs to the established primary identity;
   - removes only redundant review records;
   - never changes stream URLs or removes canonical primary entries.

2. `scripts/reconcile_generated_reports.py`
   - derives the near-duplicate family count from the health report;
   - detects same-ID name variants across all playlist queues;
   - reconciles those metrics into the Update Report.

3. `.github/workflows/repository-consistency-repair.yml`
   - runs the consistency repair, playlist audit, stream-health check and dashboard/report reconciliation;
   - uses the shared `iptv-playlist-main-writer` concurrency group;
   - publishes only actual changes.

## Important counting rule

`New Channels`, `New Backup`, and `Not Playing` are review queues, not canonical primary categories. Their entries are still tested and audited, but they must not inflate the active-primary count.

Backup entry counts are also not counts of independent infrastructure. Multiple URLs can belong to the same CDN, origin, rendition or delivery family.

## Current repository identity

The repository's GitHub description is:

> BDIX IPTV playlist for Bangladesh & India | M3U/M3U8, Live TV, EPG, Channel Logos, Stream Audits & Backups

That positioning is retained as the repository's Bangladesh-and-India hub identity, with selected international channels as a controlled secondary scope.
