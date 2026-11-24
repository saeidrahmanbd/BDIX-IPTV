# Repository-wide cleanup audit — 24 November 2026

**Repository:** `saeidrahmanbd/BDIX-IPTV`  
**Audited branch:** `main`  
**Pre-cleanup HEAD:** `bcab1ccf7233a01fef80978c193e5abb42d8c97a`  
**Scope:** Complete recursive Git tree plus targeted dependency checks across workflows, scripts, tests, documentation, reliability configuration, reports, logos and deployment components.

## Inventory before cleanup

- 5,708 recursive tree entries (5,671 files and 37 directories).
- GitHub-reported repository size: approximately 762.4 MiB.
- 5,255 logo files, approximately 238.0 MB in the current tree.
- 32 GitHub Actions workflow files.
- 94 Python scripts and 114 test files.
- Exact-blob audit found 746 groups of byte-identical files. Git deduplicates identical blob content, so duplicate paths do not necessarily represent equivalent Git storage overhead.

## Changes in this cleanup

1. Synchronized production and preview Reliability Worker registry JSON with `automation/reliability/workflow_registry.json`. Canonical schedules: 05:07, 05:17, 05:27, 05:37, 05:47 and 06:07 Asia/Dhaka. Registry version: `2026-11-24.1`.
2. Added a regression test requiring both Wrangler registry copies to match the canonical JSON exactly.
3. Consolidated overlapping local-playlist export workflows into one manual-dispatch workflow: `.github/workflows/export-playlists-for-local-reconciliation.yml`.
4. Removed the automatic push trigger from the one-time IPTV-to-International import. It now requires manual dispatch and explicit boolean confirmation.
5. Identified the 603 KB `logos/unused/README.md` as an obsolete hand-maintained gallery. The image assets in `logos/unused/` are retained because recovery tools search that directory.
6. Identified revoked owner-requested migration authorization for archival at `maintenance/archive/owner-requested-iptv-migration.json`; it is not active authorization.
7. Removed the unreferenced one-time source-editing helper `scripts/enable_review_queue_audit.py`.
8. Removed the redundant EPG Worker map synchronization helper and its manual-tool documentation. The active Xtream Worker passes playlist `tvg-id` directly to the shared XMLTV guide and does not require a static `EPG_ID_MAP`.
9. Marked the 2026-11-13 Automation v2 inventory and logo storage reports as historical snapshots.

## Explicitly preserved

- Both production playlists and every channel row, stream URL, group assignment, channel number and metadata field.
- All logo image assets, including the entire `logos/unused/` directory; no image was moved, deleted or renamed.
- EPG XMLTV data, mapping files, source configuration and publication workflows.
- Active discovery, maintenance, stream-health, logo localization, Xtream, analytics and reliability Worker code.
- Automation v2 candidate, state-store, rollback and audit infrastructure.
- Operational reports and current generated manifests.

## Deferred findings

- Exact duplicate logo paths need reference-level review before consolidation. Git already deduplicates identical blob content.
- Historical Git object and pack size needs a separate history analysis. Deleting current files does not erase previous versions.
- The two legacy logo localization workflows have different scopes and write permissions; they were not merged.
- Automation v2 remains a candidate/migration framework. Production legacy workflows were not retired.
- Additional scripts and reports require complete dependency and runtime checks before deletion.

## Verification

The Reliability Worker parity test and full repository test suite must pass in GitHub Actions after publication. The one-time import is manually gated and must not run as part of cleanup. No production playlist, EPG guide, logo image or stream URL was modified by these changes.
