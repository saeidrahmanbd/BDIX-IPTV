# Legacy workflow retirement and V2 replacement map

This is a migration plan only. No legacy workflow is disabled, edited or retired by this document. Production workflows remain enabled until the separate cutover PR is approved.

## Workflows to consolidate under V2

| Legacy workflow | Exact legacy file | Current production responsibility | V2 replacement / owner | Retirement gate |
|---|---|---|---|---|
| Discovery Schedule Watchdog | `.github/workflows/discovery-schedule-watchdog.yml` | Dispatches multiple workflows at checkpoints; second scheduling authority | A single durable V2 scheduler using the run ledger. The candidate-bundle workflow currently has its own schedule, but a missed-run recovery scheduler is not yet implemented. | Prove idempotent scheduling, missed-run recovery, durable reservations and one-writer queue behavior. |
| IPTV Playlist Update | `.github/workflows/iptv-maintenance.yml` | Monolithic maintenance writes both playlists, reports, logos and dashboard | `.github/workflows/automation-v2-candidate-bundle.yml` plus `.github/workflows/automation-v2-prepare-publication-pr.yml`. Candidate generation is shadow-only; the PR preparer is review-only. | Prove exact workflow-to-script parity, IPTV owner-protection invariants, candidate validation and rollback. |
| IPTV New Channel Discovery | `.github/workflows/new-channel-discovery.yml` | Writes IPTV discovery rows and reports | IPTV discovery stage in `automation/core/v2_candidate_runner.py`; candidate outputs append only to manual-review queues. | Prove real source-adapter coverage, duplicate handling, queue visibility and candidate fixtures. |
| International Channel Discovery | `.github/workflows/international-channel-discovery.yml` | Writes International playlist and reports | International discovery stage in `automation/core/v2_candidate_runner.py`. | Prove real source-adapter coverage, country/identity/category rules and candidate fixtures. |
| International Stream Health | `.github/workflows/international-stream-health.yml` | Probes and may rewrite International playlist/history/reports | International probe ledger and lifecycle stage in `automation/core/v2_candidate_runner.py`, persisted to `automation-v2-state`. | Prove multi-day real-probe histories, state recovery, URL fingerprint isolation and removal-review gates. |
| Refresh IPTV EPG | `.github/workflows/epg-refresh.yml` | Multiple triggers/listeners; generates and publishes guide/mappings/reports/dashboard | EPG candidate stage in `automation/core/v2_candidate_runner.py` plus `.github/workflows/automation-v2-prepare-publication-pr.yml`. | Prove source parity, full-guide quality/coverage, freshness, atomic candidate validation and rollback. |
| IPTV Logo Localization | `.github/workflows/logo-localization.yml` | IPTV playlist/logo mutations | No complete V2 logo repair writer yet; current V2 includes a conservative logo-reference audit only. | Implement a candidate-only IPTV logo repair engine and prove local-asset authenticity and metadata-only scope. |
| Playlist Logo Repair and Localization | `.github/workflows/playlist-logo-localization.yml` | Mutates both playlists and logo assets/provenance | No complete V2 two-playlist logo repair writer yet; current V2 includes a conservative reference audit only. | Implement per-playlist scoped candidate repair, dynamic-reference coverage and rollback tests. |
| Generate Dashboard (nested) | `scripts/refresh_dashboard_diagnostics.py`, `scripts/generate_dashboard.py` | Multiple workflow paths regenerate dashboard/reports; recovery path launches a long helper chain | A read-only V2 report consumer of immutable published snapshots. No replacement dashboard workflow is enabled yet. | Prove one report producer, immutable inputs, snapshot freshness and zero playlist/logo staging side effects. |

## Workflows to retain as separate services

| Workflow | Exact file | Planned treatment |
|---|---|---|
| Changelog | `.github/workflows/changelog.yml` | Retain as a post-publication report stage; remove any playlist mutation authority. |
| Daily Xtream Health Check | `.github/workflows/check-xtream.yml` | Retain as read-only gateway validation with simplified trigger policy. |
| Deploy IPTV Analytics | `.github/workflows/deploy-analytics.yml` | Retain as infrastructure deployment, not a playlist writer. |
| Deploy Xtream Gateway | `.github/workflows/deploy-xtream.yml` | Retain as infrastructure deployment with live verification. |
| Probe EPG sources for Bangladesh | `.github/workflows/epg-bangladesh-source-probe.yml` | Retain as isolated research/probe utility; outputs are candidate evidence only. |
| Probe external EPG sources | `.github/workflows/epg-external-source-probe.yml` | Retain as isolated research/probe utility; outputs are candidate evidence only. |
| IndexNow | `.github/workflows/indexnow.yml` | Retain as separate search-engine notification. |
| Validate Website SEO | `.github/workflows/seo-validation.yml` | Retain as read-only validation. |
| Test Suite | `.github/workflows/test-suite.yml` | Retain and expand as the central regression gate. |

## V2 workflows currently present

| V2 workflow | Exact file | Authority |
|---|---|---|
| Candidate Bundle | `.github/workflows/automation-v2-candidate-bundle.yml` | Shadow-only candidate generation; writes durable state and candidate artifacts, never production files. |
| Branch CI | `.github/workflows/automation-v2-ci.yml` | Read-only contract tests, immutable baseline dry run and PR regression gate. |
| Legacy Regression Audit | `.github/workflows/automation-v2-legacy-audit.yml` | Read-only full-repository regression audit on V2 branches and PRs. |
| State Store Check | `.github/workflows/automation-v2-state-store-check.yml` | Isolated durable-state branch read/write check. |
| Prepare Publication PR | `.github/workflows/automation-v2-prepare-publication-pr.yml` | Requires explicit confirmation; creates an owner-review PR containing only the three allowlisted outputs. No auto-merge. |
| Prepare Rollback PR | `.github/workflows/automation-v2-prepare-rollback-pr.yml` | Proposed in PR #154; requires explicit confirmation and prepares a revert PR for a previously merged V2 publication PR. No main write or auto-merge. |

## V2 readiness snapshot

- Candidate-only IPTV, International and EPG stages are orchestrated by the shadow candidate-bundle runner.
- Durable run reservations and International probe observations are stored on the dedicated `automation-v2-state` branch using compare-and-swap writes.
- Candidate transaction infrastructure includes engine path allowlists, SHA-256 evidence, stale-input rejection, a shared lock and atomic candidate-directory staging.
- The immutable production-baseline dry run has passed with zero production changes.
- A targeted EPG-timeout/probe-checkpoint recovery test, rollback-policy tests and workflow concurrency-boundary tests are proposed in PR #154; their latest CI results must pass before merge.
- The rollback PR preparer is a recovery mechanism for already-merged candidate PRs, not an automatic publisher.
- Not ready for production cutover: missed-run scheduler, complete logo candidate engines, dashboard snapshot consumer, exhaustive runtime dependency tracing, full workflow equivalence and rollback acceptance remain open.

## Required cutover sequence

1. Finish source-adapter, logo-engine and real-candidate fixture tests for every writer responsibility.
2. Finish exhaustive nested runtime tracing and exact workflow-to-script parity for every legacy writer.
3. Prove V2 is the only production writer, with a durable queue/lock and stale-baseline checks.
4. Prove atomic playlist+state+EPG transaction behavior, failure recovery and rollback on a disposable test branch.
5. Prepare a draft migration PR listing the exact legacy workflow files to retire and the V2 replacement files; do not disable any production workflow in this PR.
6. Review the migration PR and all candidate artifacts. Keep legacy production workflows active until a separate cutover change is ready.
7. In a separate owner-approved cutover PR, transfer schedules and disable only the replaced legacy writers. Keep read-only and infrastructure workflows.
8. Verify the first production transaction and rollback path before enabling recurring V2 schedules.

No force-push, broad workflow deletion, automatic merge or direct playlist mutation is permitted during migration.
