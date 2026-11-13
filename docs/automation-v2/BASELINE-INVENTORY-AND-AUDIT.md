# BDIX-IPTV Automation V2 — Baseline Inventory & Audit

**Audit date:** 2026-11-13  
**Baseline branch:** `main`  
**Baseline commit:** `aec37357dfbb47f0792682af744ccaf111416d7a`  
**Audit branch:** `automation-v2/inventory-audit`  
**Production mutation status:** NONE. This audit branch is a snapshot plus audit documentation only.

## 1. Preservation and rollback boundary

The audit branch was created from the exact production main commit above. That Git commit preserves the complete repository tree, including both production M3U playlists, all logo assets, the EPG guide, source registers, reports, scripts, tests, site files, and Workers. No production playlist, logo, EPG file, workflow, or main-branch ref was changed for this audit.

Key immutable baseline blob IDs:
- `IPTV-Playlist.m3u`: `eb46b5ef4ddfde11a010389d1f0202a7bd418b0a` (445,629 bytes)
- `International-Playlist.m3u`: `f98c433afa7df88b9345a7191e58ea83f833d1b9` (987,903 bytes)
- `epg/epg.xml`: `b28414c75937bd155067c6db5e6e2083ee4004b4` (30,944,668 bytes)
- `README.md`: `95c17697b536218d30c6f1eb3dcf5be8aa0cc93d`

The branch's common ancestor is the baseline main commit. Rollback is by returning to the untouched main ref; no destructive cleanup has been performed.

## 2. Repository inventory

The recursive Git tree is complete (GitHub reported `truncated=false`): 5,633 tree entries.

| Area | Files | Bytes |
|---|---:|---:|
| Root | 5 | 1,449,106 |
| .github | 18 | 118,419 |
| analytics | 4 | 13,499 |
| assets | 10 | 1,138,255 |
| docs | 25 | 137,038 |
| epg | 3 | 30,985,548 |
| logos | 5,372 | 306,093,613 |
| maintenance | 1 | 2,897 |
| reports | 44 | 5,946,938 |
| scripts | 79 | 1,078,245 |
| tests | 50 | 449,513 |
| xtream-main | 2 | 9,299 |
| xtream | 1 | 4,078 |

There are 17 GitHub Actions workflow files (118,015 bytes), 79 Python scripts, 50 test files, and 5,372 logo files. The largest repository payload is the logo directory (about 306 MB), not the workflow source.

### Workflow inventory

1. `changelog.yml`
2. `check-xtream.yml`
3. `deploy-analytics.yml`
4. `deploy-xtream.yml`
5. `discovery-schedule-watchdog.yml`
6. `epg-bangladesh-source-probe.yml`
7. `epg-external-source-probe.yml`
8. `epg-refresh.yml`
9. `indexnow.yml`
10. `international-channel-discovery.yml`
11. `international-stream-health.yml`
12. `iptv-maintenance.yml`
13. `logo-localization.yml`
14. `new-channel-discovery.yml`
15. `playlist-logo-localization.yml`
16. `seo-validation.yml`
17. `test-suite.yml`

## 3. Recent Actions evidence

The latest 100 workflow runs were inspected. In that sample:
- `IPTV Playlist Update`: 6 failures.
- `Test Suite`: 3 successes, 1 failure, 2 cancellations.
- `Refresh IPTV EPG`: 17 successes.
- `Daily Xtream Health Check`: 20 successes.
- Multiple `workflow_run`-triggered downstream runs were skipped.
- Pages deployment and Changelog also show cancelled/skipped runs.

This is a sample of the latest 100 runs, not a lifetime failure-rate calculation.

### Reproduced maintenance failure

Runs #1588 and #1589 failed in the `maintain` job. The early maintenance helper tests passed. The main failure was the owner-protection check:

- Existing channel number changed for **GTC Punjabi**
- Existing channel number changed for **Manoranjan TV**
- Existing channel number changed for **The Movie Club**
- Existing channel number changed for **Thikana TV**

The step exited non-zero with: `IPTV owner-protection gate failed with 4 issue(s)`.

This is a concrete ordering/authority defect: the maintenance mutation sequence modifies numbering and the subsequent preservation gate rejects those changes. The safety gate is doing its job; it must not be weakened to make the workflow green. V2 must ensure routine maintenance cannot renumber protected existing rows.

The same logs also show:
- The International protected-stream test helper runs as part of the IPTV maintenance job, although its output is diagnostic and its 13 tests passed.
- The maintenance job runs a large chain of mutations, then runs audits/gates, then runs a second mutation pass when checks fail.
- A separate dashboard-recovery path continues to generate and publish reports even when the main maintenance path fails.
- Dashboard recovery logs report stale auxiliary reports and mismatched playlist fingerprints.
- A logo-source request for WWE Superstar Central returned HTTP 403; this was logged as one logo download failure, not the final job-stopping error.

## 4. Architecture and coupling risks confirmed

### A. Multiple independent writers

The current architecture has distinct workflows capable of writing to production:
- IPTV maintenance
- International discovery
- Bangladesh/India discovery
- International stream health
- Two separate logo localization workflows
- EPG refresh
- Changelog/dashboard/report generation

The common writer concurrency group serializes some writes, but it does not provide a single owner for policy, mutation authorization, idempotency, and publication. Each writer can still make decisions based on different snapshots and different validation sequences.

### B. Trigger fan-out and skip noise

EPG refresh is triggered by playlist pushes, a schedule, manual dispatch, and completion of several upstream workflows. Xtream checks are also triggered by multiple upstream workflow completions. A `workflow_run` event can occur when an upstream workflow completed but its meaningful job was skipped; downstream jobs then appear as skipped. This creates noisy run history and makes the actual daily pipeline hard to understand.

### C. Too many recovery checkpoints

`discovery-schedule-watchdog.yml` defines nine daily cron checkpoints. This is a symptom of best-effort scheduling and missed-run recovery being implemented as repeated dispatch checkpoints rather than one clear orchestrator with a durable daily run ledger.

### D. Duplicate/specialized logo paths

Both `logo-localization.yml` and `playlist-logo-localization.yml` can write playlist/logo changes. Their scope and triggers differ; the latter currently touches both playlists and has its own preservation check. V2 should have one logo engine with explicit per-playlist scope and one publisher.

### E. Maintenance is a long shell-embedded pipeline

`iptv-maintenance.yml` is approximately 21 KB and contains an extensive inline mutation sequence, conditional retry/correction logic, and a separate dashboard recovery path. The sequence is difficult to test as a single coherent transaction. V2 should move orchestration into versioned Python entrypoints and keep workflow YAML thin.

### F. Policy exists but execution ownership is fragmented

`docs/PLAYLIST-AUTOMATION-POLICY.md` already defines strong playlist boundaries:
- IPTV playlist is owner-curated; existing stream URLs, group assignments, channel numbers, category positions and relative row order are protected except explicit authorization.
- International playlist is automation-controlled; definitive failures require three consecutive Bangladesh-calendar-day failures before removal.
- New Channels/New Backups are manual review queues.
- Shared writer serialization and regression coverage are required.

V2 should promote these requirements into a machine-readable central policy and enforce them through one mutation authorization layer. Documentation and executable policy must be generated/validated against each other.

## 5. V2 design constraints

1. **No production changes during inventory and design.**
2. A new engine must operate on copies/fixtures and write to a temporary output path.
3. IPTV and International playlist mutation APIs must be separate; no implicit all-playlist mutator.
4. IPTV existing stream URL occurrences, groups, channel numbers, category positions and row order are immutable unless a one-time owner authorization explicitly permits a specific operation.
5. International health policy: first definitive failed day goes to Review; deletion only after three consecutive definitive failed Bangladesh dates; inconclusive, auth, rate-limit, geo-block, and global network incidents never authorize deletion.
6. New Channels and New Backups remain manual-review queues and must not be exposed through Xtream.
7. Country group threshold is five unique primary channel identities; fixed Bangladesh and India groups remain.
8. Logos must be authentic repository-local assets. Logo/country metadata uncertainty in discovery queues is warning-only and must not suppress discovery.
9. EPG uses candidate generation, validation, and last-known-good atomic publication.
10. All writers use a single transaction/publish layer, a durable daily run ledger, and a single queue/lock.
11. Workflow dispatch and downstream chaining must be idempotent; only successful, meaningful upstream outputs can advance dependent stages.
12. Rollback is an atomic ref rollback or revert, never a force push to production.

## 6. Planned migration sequence

- [x] Create separate audit branch from exact main baseline.
- [x] Capture complete recursive tree inventory and key production blob IDs.
- [x] Inspect latest 100 Actions runs and retrieve logs for two recent failed maintenance runs.
- [x] Complete workflow-to-script/test dependency graph (static workflow and critical-path mapping).
- [x] Complete critical script import/call overlap audit; [ ] finish exhaustive nested subprocess/runtime tracing.
- [x] Define central machine-readable policy and schema.
- [x] Add the first V2 contract layer and 10 policy/invariant tests on this branch; [ ] implement scoped playlist engines.
- [ ] Run read-only dry-run comparisons against baseline playlists.
- [ ] Require all regression tests and invariants to pass before any production publication.
- [ ] Open reviewable migration PR; keep main production workflows unchanged until approval and staged validation.

## 7. Phase 2 progress\n\nThe branch now contains a central JSON policy, a JSON Schema, a dependency-free policy conformance validator, a pure IPTV existing-row preservation contract, a manual-queue visibility guard, 10 focused contract tests, and a read-only branch-only CI workflow. The local contract test run passed all 10 tests. GitHub Actions status for the new branch CI has not yet been independently observed through the available GitHub interface. A further side-effect audit identified nested subprocess calls and a hidden git-staging side effect in the logo provenance manifest generator; see RUNTIME-SIDE-EFFECT-AUDIT.md.\n\n## 8. Safety gate

No file in the production playlist, logo, EPG, or live workflow areas has been edited by this audit. This branch currently exists only to hold the audit baseline and this documentation. Do not merge or promote it to production until the migration tests, dry-run invariants, and publication rollback checks pass.


## 9. Automation V2 implementation progress (branch-only)

- Central JSON policy and JSON Schema added.
- Read-only parser and IPTV existing-row preservation contract added.
- Candidate validation explicitly reports `publish=false`; International currently reports `PARSE_ONLY` until its full invariants are implemented.
- Candidate manifest path allowlists added to prevent cross-playlist engine writes.
- International stream-failure lifecycle primitive added: only definitive 404/410, first/second day Review, third consecutive day eligible for a separate removal review.
- International country-group threshold primitive added: five unique primary identities; fixed Bangladesh and India groups.
- Conservative logo reference inventory added: 5,366 image files, 2,395 exact playlist references, 2,971 apparent non-references from playlist-only matching. These are not approved for deletion.
- Repository-wide explicit logo reference scanner added. It is report-only and never deletes assets.
- Branch CI expanded to include all `test_automation_v2_*.py` tests and the logo scanner.
- The GitHub connector currently returns no workflow run or status records for the latest branch commit, so CI execution has not been independently confirmed. The new tests must be treated as pending until an actual Actions result is observed.
- Production playlist, EPG and legacy workflow blob SHAs were rechecked against `main` and remain identical to the baseline.

## 10. Remaining before migration can be called test-passed

1. Confirm and repair any CI failures; run all V2 tests and all applicable legacy tests.
2. Build complete candidate-only IPTV and International orchestration engines.
3. Port stream identity, logo, discovery and EPG behaviors behind explicit contracts.
4. Run repository-wide logo reference scan on a checked-out baseline; inspect dynamic references and duplicates.
5. Generate dry-run candidates from immutable baseline files and validate all invariants.
6. Test stale baseline rejection, concurrent-run locking, partial failure, rollback and last-known-good EPG.
7. Only then prepare a draft PR and owner-reviewed cutover plan.


## 11. Updated V2 verification status (2026-11-13)

This section supersedes the early Phase 2 progress notes above.

- Latest verified V2 branch CI: run 43409563969, commit 568177d9a87a1a693a52a7d7722cf1391689c0f8 — 168 V2 tests passed; policy conformance, immutable baseline dry run, and repository-wide logo audit all passed.
- Latest full repository regression: 699 tests passed on the same commit.
- The all-engine baseline dry run exercised the IPTV, International and EPG candidate engines using immutable production copies. All four engine checks were accepted (IPTV, International, EPG/IPTV and EPG/International); candidate playlist rows remained 1,280 and 3,120 respectively; EPG and playlist candidate changes were zero; publish=false; production_files_modified=false.
- Baseline EPG measurement: IPTV 776 active IDs / 411 mapped / 363 scheduled / 321 with current or future schedules; International 2,684 active IDs / 662 mapped / 586 scheduled / 541 with current or future schedules.
- Alias review: 19 IPTV and 60 International suggestions, plus 14 ambiguous cases. Suggestions are manual-review-only; no alias was applied.
- Logo audit: 5,366 images; 2,395 playlist-referenced assets; 2,691 runtime-referenced assets; 2,675 without explicit runtime-source references; 718 exact duplicate groups; 75 missing runtime-source targets. Zero missing targets are directly referenced by either production playlist. No logos were deleted, moved or quarantined.
- V2 now includes candidate-only IPTV metadata/discovery, International stream probe/ledger/lifecycle, EPG candidate/approved-alias, run-ledger, transaction-gate and atomic candidate-bundle components.
- Still not implemented: production Git publisher, full discovery-source integration, complete legacy workflow retirement/replacement, exhaustive dynamic side-effect tracing, failure-injection/rollback testing, and production cutover.
- Production playlists, EPG and legacy workflows remain unchanged. No V2 production publishing is enabled.


## 12. Latest hardening verification (2026-11-13)

- Full repository regression: **707 tests passed** on commit f4af3fe24e8cef5192c13c31e425d9a660f3878a.
- The latest additions cover idempotent daily International probes, malformed URL handling as inconclusive, batch lifecycle orchestration, row-index/tvg-id identity binding, symlink-safe transaction locks and candidate staging.
- V2 contract CI for this latest hardening commit is queued; the preceding V2 CI run passed 168 focused tests, policy checks, all-engine immutable baseline dry run and logo audit.
- The successful all-engine baseline dry run accepted IPTV, International and both EPG candidates without changes; candidate playlist changes=0, EPG changes=0, publish=false and production_files_modified=false.
- The legacy workflow retirement map is documented in LEGACY-WORKFLOW-RETIREMENT-MAP.md. No legacy workflow has been disabled or replaced on main.
