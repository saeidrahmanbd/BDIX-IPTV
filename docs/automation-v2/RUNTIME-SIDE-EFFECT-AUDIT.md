# BDIX-IPTV Automation V2 — Runtime Side-Effect Audit

**Baseline:** 46275f5ebafa2ae1b56f3e480f684ac1e85ae45e  
**Method:** Static search for subprocess invocation, git staging/commit commands, workflow command blocks and explicit staging lists. This is not a sandbox execution trace; dynamic behavior outside searched call sites remains subject to further review.

## Confirmed hidden and transitive execution

| Entry point | Observed behavior | V2 risk / required correction |
|---|---|---|
| scripts/run_generate_epg.py | Calls additional-source mapping in-process, then launches scripts/augment_epg_mapping_from_iptv_org.py through subprocess before invoking the generator. | EPG dependency chain is wider than the workflow's top-level command list. V2 must declare every stage explicitly and return one candidate artifact. |
| scripts/fetch_iptv_org_epg.py | Clones/uses an external iptv-org/epg working tree and runs external commands with finite timeouts. | External catalogue retrieval must remain isolated from the publication step; optional-source failure must not damage last-known-good guide. |
| scripts/refresh_dashboard_diagnostics.py | Launches a long sequence of scripts, including audits, stream checks, identity indexing, logo manifest, reports and dashboard generation. It then resets staged logos. | Recovery path is an orchestration pipeline of its own. V2 reporting should consume immutable snapshots and must not call playlist mutators or stage assets. |
| scripts/generate_logo_authenticity_manifest.py | Writes a provenance manifest. Its hidden `git add logos/` behavior has been removed in the V2 migration branch and is covered by a source-level regression test. | Keep report generation filesystem-only; callers explicitly stage declared outputs. |
| scripts/audit_playlist.py | Reads a previous playlist version from Git history using subprocess git show. | Historical comparisons must be passed an explicit immutable baseline rather than depending on ambient HEAD. |

## Workflow staging and publication patterns

The current workflows use multiple, non-equivalent staging scopes:
- International discovery stages International-Playlist.m3u, a discovery report, logos, and selected validator/test files.
- IPTV discovery stages IPTV-Playlist.m3u and its discovery report.
- Playlist logo localization stages both playlists, logos, and a set of logo reports/registries.
- EPG refresh has separate guide generation and dashboard-only publication paths with different staged file lists.
- Maintenance contains a long shell-embedded sequence and a dashboard recovery path; the exact staged files differ by path.

This means a helper can stage files outside the apparent workflow step that called it. V2 must make every engine return a declared artifact manifest and make the publisher reject any staged path outside that manifest.


## Additional repository-wide source search (2026-11-14)

A second source-level search across the current mainline Python code found these additional execution paths:

| Entry point | Confirmed behavior | V2 treatment |
|---|---|---|
| `scripts/refresh_dashboard_diagnostics.py` | Its `run_script(relative)` helper dynamically launches a sequence of audit, stream-health, identity-index, logo-manifest, report and dashboard scripts. At the end it runs `git reset -- logos/`. | Treat this as an orchestration entrypoint with an explicit dependency list, not as a read-only report generator. V2 reporting must consume immutable snapshots and must not reset or stage the Git index. |
| `scripts/generate_logo_authenticity_manifest.py` | Previously called `git add logos/` internally after generating the manifest. The V2 migration branch removes this hidden staging behavior and adds a regression test. | Report generation is filesystem-only; workflow/publisher owns explicit staging. Legacy workflow callers must stage only their declared output set. |
| `scripts/fetch_iptv_org_epg.py` | Clones the external iptv-org/epg repository, runs `npm ci`, and invokes the scraper with bounded timeouts. | Keep acquisition isolated from candidate validation and publication; preserve last-known-good EPG if acquisition fails. |
| `automation/engines/epg/source_provider.py` | Executes configured source-provider commands through subprocess with timeout and checked exit status. | Declare provider commands and expected outputs in the EPG source manifest; never allow provider code to publish. |
| `scripts/run_generate_epg.py` | Launches `augment_epg_mapping_from_iptv_org.py` as a nested subprocess after additional-source mapping. | Preserve the nested stage in the dependency contract or replace it with an explicit in-process EPG engine stage. |
| `scripts/generate_changelog.py`, `scripts/classify_international_backups.py`, `scripts/audit_playlist.py`, `scripts/pre_publish_gate.py` | Read prior playlist/commit state using Git history commands such as `git show`; no Git write was found in these call sites. | Pass an explicit immutable baseline ref into V2 instead of relying on ambient `HEAD`. |
| `scripts/prepare_automation_v2_publish_pr.py` | Uses Git subprocess calls to validate ancestry, clean worktree and exact allowlisted diffs before preparing a review branch. | Keep this code exclusively in the owner-review PR preparation boundary; never call it from a candidate engine. |

The source search found no direct `os.system` or `subprocess.Popen` call sites in the searched repository index. This is not proof that all dynamic command construction or imported helper behavior has been traced.

### Remaining runtime-tracing gap

The dashboard recovery helper invokes scripts by a runtime `relative` argument, and the EPG source provider uses configured commands. These indirect call chains still need to be resolved against every workflow invocation and fixture-tested before workflow retirement. This document is therefore a strengthened static audit, not a claim of exhaustive runtime tracing.

## V2 requirements derived from this audit

1. No engine or report generator may call git add, git commit, git push, or reset.
2. All subprocess calls must be declared in the engine manifest, bounded by timeouts, and checked for expected outputs.
3. Reporting is read-only and cannot invoke mutation engines.
4. Candidate generation and publication are separate processes.
5. The publisher accepts only a fixed allowlist of artifact paths for the selected engine and playlist.
6. EPG source fetches run before candidate generation; validation and atomic publication remain separate.
7. Runtime dependency tracing is still incomplete. Before cutover, inspect every script invoked from workflows and every nested subprocess target, then map those targets to contract tests.

## V2 inventory instrumentation (branch-only)

The V2 static inventory has been expanded to scan repository-owned Python files outside `scripts/`, report literal and dynamic subprocess calls, flag `eval()`/`exec()`, and record each GitHub Actions YAML `run:` block as an opaque shell boundary. These boundaries are counted as unresolved rather than treated as successfully traced.

The candidate-bundle workflow runs this inventory and uploads `runtime-dependency-inventory.json` with the shadow artifacts. This improves repeatability and makes unresolved execution paths visible on each candidate run; it does **not** resolve shell interpolation, imported-module side effects, external GitHub Actions, npm scripts, network-loaded code, or runtime-generated command arguments. Those still require targeted trace evidence before any legacy writer can be retired.

The dashboard shadow artifact also now reports the availability and SHA-256 provenance of each captured legacy report input. It continues to mirror the legacy dashboard markdown verbatim; it is not an independently recomputed metric-equivalence proof.


## Independent dashboard metric acceptance (branch-only)

The candidate bundle now runs `scripts/audit_automation_v2_dashboard_equivalence.py`. It does not import or execute the legacy dashboard generator. It independently parses the IPTV playlist, audit/EPG/health/gate reports and XMLTV freshness evidence, recomputes every displayed dashboard summary metric, and compares the results with `reports/Update Report.md`. The JSON result records per-input freshness, source fingerprints, expected/actual metrics and mismatches. It writes only under `reports/automation-v2/`; it does not modify the production dashboard or its inputs.

A passing unit test is not production acceptance. The first current-main candidate artifact must show zero metric mismatches and current input fingerprints. If any source is stale, the corresponding expected values remain explicitly stale/pending rather than being treated as current.


The runtime inventory also records every workflow \`uses:\` reference as a separate boundary. Local action paths are checked for an \`action.yml\`/\`action.yaml\` entrypoint; external actions are classified by whether the reference is pinned to a 40-character commit SHA. External action implementations remain unresolved until their exact pinned source and transitive runtime are inspected. Workflow shell bodies are retained without the former 4,000-character truncation and preserve original indentation and blank lines so heredocs and multiline commands remain reviewable.

## Latest evidence and remaining acceptance blockers (2026-11-14)

The current review branch has been synchronized with `main` using a normal merge commit. It is now zero commits behind main. The latest successful Automation V2 Branch CI artifact set reports:

- Immutable baseline dry run accepted all four candidate engines (IPTV, International, IPTV EPG, International EPG); candidate playlist changes = 0, candidate EPG changes = 0, publication = false, and production files modified = false.
- Independent dashboard recomputation: `equivalent=true`, zero mismatches. The playlist audit, stream-health report and pre-publish gate are current.
- Published EPG is not current. The audit reports `cutover_ready=false` with the single dashboard freshness blocker `published_epg`; EPG mapping and programme coverage remain explicitly `PENDING`.
- Runtime inventory: 100 workflow Python entrypoints, 65 unique targets, 151 nested process/shell boundaries, 111 workflow shell blocks, 67 external action references across 6 unique pinned implementations.
- All 9 detected dynamic Python process boundaries are reviewed; no mutable external source dependency, missing literal target, unpinned action reference or unreviewed Python process boundary remains.
- The 111 workflow shell blocks are classified by observed effect and owner, but remain unresolved pending exact end-to-end trace. The inventory identifies 51 shell blocks owned by legacy production-writer workflows and 10 direct repository-writer blocks. Classification is not treated as proof that the command's transitive behavior is fully traced.
- Six external action implementations are pinned and have reviewed metadata, but their full transitive implementations remain explicit unresolved boundaries.
- Logo audit: 5,367 image files and 5,367 explicit references; 111 missing explicit targets and 75 missing runtime targets; 2,665 files are apparently unreferenced by runtime sources. No deletion or quarantine was performed. These findings require path/provenance review, not bulk cleanup.

### Remaining cutover blockers

1. Publish and validate a fresh XMLTV guide against both current playlist fingerprints; do not mark EPG current merely because dashboard metrics match.
2. Trace all 111 shell blocks through their invoked scripts, environment inputs, network effects, Git staging and push behavior. Resolve the 51 legacy-writer boundaries against their V2 replacement engines.
3. Inspect the six pinned action implementations and transitive runtime dependencies, not only their metadata.
4. Complete authentic-logo provenance and missing-path disposition; do not delete assets based on the unreferenced-by-runtime heuristic.
5. Prove the complete legacy-to-V2 workflow replacement matrix, single-writer behavior, stale-input rejection, failure recovery and rollback on an isolated branch.
6. Keep the separate production cutover approval gate closed until every item above has current passing evidence.

The current successful checks establish branch-level regression and metric parity. They do not establish production cutover readiness.


### Follow-up: EPG workflow guard-only runs and shell trace links (2026-11-14)

- Inspected the latest main-branch `Refresh IPTV EPG` runs: `43571104404`, `43571202539`, and `43576391359`.
- Each run's `daily_guard` job completed successfully, but the actual `refresh` job was skipped. These green workflow conclusions are not evidence of a newly generated or published XMLTV guide.
- The Automation V2 dashboard artifact continues to report `published_epg=false`, and `cutover_ready=false` with blocker `published_epg`. Do not clear this blocker until the actual EPG publication step has completed and the guide freshness/fingerprint validators pass.
- The runtime inventory now links each shell block to any explicit Python entrypoints, records inline Python heredocs and recognized command lines, and resolves script existence against the audited repository root. It deliberately leaves transitive effects unresolved; entrypoint linkage is not a completed shell trace.
- Added a dedicated regression test for shell-to-Python entrypoint linkage and the non-complete trace status. The full test suite and legacy regression audit passed on commit `de954f28c6fc360ae59ad04ed232ad44d1eda639`; the subsequent Automation V2 Branch CI run is still in progress.

The EPG guard's skip behavior needs a separately isolated investigation before changing production workflow scheduling or dispatching a writer. No production EPG workflow, playlist or guide was modified by this review-branch work.


### Latest shell-link inventory (run 43576731241)

The refreshed runtime artifact confirms:

- 111 workflow shell blocks total.
- 48 blocks now link to one or more existing Python entrypoints; 9 blocks contain inline Python heredocs.
- 63 blocks still require manual shell trace because no repository Python entrypoint was extractable.
- Zero shell blocks are marked fully traced. This is intentional: linking a script path does not establish its imports, subprocess descendants, network access, credentials, Git writes or external package lifecycle effects.
- 10 shell blocks are identified as direct repository writers; 51 belong to legacy production-writer workflows. V2 shadow candidate workflow has 11 shell blocks.
- 67 external action references resolve to 6 unique immutable implementations; metadata is reviewed, but implementation-level/transitive code review remains a cutover item.
- The baseline dry-run continues to accept all four candidate engines with zero playlist or EPG candidate changes and publication disabled. EPG identity matching suggestions remain manual-review-only; no fuzzy or ambiguous mapping was auto-applied.

This is improved trace navigation, not completion of the full runtime trace or approval to retire any writer.


### Immutable external-action metadata review (2026-11-14)

The exact pinned `action.yml` files were fetched from their referenced repositories and commit SHAs for all six unique implementations:

| Action implementation | Confirmed runtime boundary | Review result |
|---|---|---|
| `actions/checkout` | Node 24, `dist/index.js` main and post; default `persist-credentials=true`; post-job credential cleanup. | Metadata confirmed. The V2 candidate workflow explicitly sets `persist-credentials: false`; each legacy caller still needs context-specific credential review. |
| `actions/setup-python` | Node 24 setup plus post cache-save step. | Metadata confirmed; Python installation and cache behavior remain external action code. |
| `actions/setup-node` | Node 24 setup plus post cache-save step. | Metadata confirmed; Node installation and cache behavior remain external action code. |
| `actions/upload-artifact` (two distinct SHAs) | One implementation uses Node 24; the older pinned implementation uses Node 20; both upload workflow artifacts and do not commit to the repository. | Metadata confirmed; retain both as separate immutable implementations. |
| `cloudflare/wrangler-action` | Node 24 action; configured `command` may deploy or otherwise mutate Cloudflare resources. | Metadata confirmed. The repository's Wrangler deployment workflow is an infrastructure writer, not a playlist/EPG writer, and remains outside the playlist cutover boundary. |

This confirms the action entrypoint/runtime declarations and documented inputs/outputs only. The compiled `dist/*` bundles, their imported modules, downloaded runtime packages and post-step implementation have not been fully audited. Do not change action SHAs or treat this metadata review as a source-code security audit. The candidate bundle uses a pinned artifact upload action; the six implementation records remain unresolved for full transitive review.
