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
