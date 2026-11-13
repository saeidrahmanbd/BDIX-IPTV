# BDIX-IPTV Automation V2 — Runtime Side-Effect Audit

**Baseline:** 46275f5ebafa2ae1b56f3e480f684ac1e85ae45e  
**Method:** Static search for subprocess invocation, git staging/commit commands, workflow command blocks and explicit staging lists. This is not a sandbox execution trace; dynamic behavior outside searched call sites remains subject to further review.

## Confirmed hidden and transitive execution

| Entry point | Observed behavior | V2 risk / required correction |
|---|---|---|
| scripts/run_generate_epg.py | Calls additional-source mapping in-process, then launches scripts/augment_epg_mapping_from_iptv_org.py through subprocess before invoking the generator. | EPG dependency chain is wider than the workflow's top-level command list. V2 must declare every stage explicitly and return one candidate artifact. |
| scripts/fetch_iptv_org_epg.py | Clones/uses an external iptv-org/epg working tree and runs external commands with finite timeouts. | External catalogue retrieval must remain isolated from the publication step; optional-source failure must not damage last-known-good guide. |
| scripts/refresh_dashboard_diagnostics.py | Launches a long sequence of scripts, including audits, stream checks, identity indexing, logo manifest, reports and dashboard generation. It then resets staged logos. | Recovery path is an orchestration pipeline of its own. V2 reporting should consume immutable snapshots and must not call playlist mutators or stage assets. |
| scripts/generate_logo_authenticity_manifest.py | Writes a provenance manifest and executes git add logos/ internally. | A report generator has a hidden repository staging side effect. V2 engines must never stage/commit; only the central publisher may stage an allowlisted artifact set. |
| scripts/audit_playlist.py | Reads a previous playlist version from Git history using subprocess git show. | Historical comparisons must be passed an explicit immutable baseline rather than depending on ambient HEAD. |

## Workflow staging and publication patterns

The current workflows use multiple, non-equivalent staging scopes:
- International discovery stages International-Playlist.m3u, a discovery report, logos, and selected validator/test files.
- IPTV discovery stages IPTV-Playlist.m3u and its discovery report.
- Playlist logo localization stages both playlists, logos, and a set of logo reports/registries.
- EPG refresh has separate guide generation and dashboard-only publication paths with different staged file lists.
- Maintenance contains a long shell-embedded sequence and a dashboard recovery path; the exact staged files differ by path.

This means a helper can stage files outside the apparent workflow step that called it. V2 must make every engine return a declared artifact manifest and make the publisher reject any staged path outside that manifest.

## V2 requirements derived from this audit

1. No engine or report generator may call git add, git commit, git push, or reset.
2. All subprocess calls must be declared in the engine manifest, bounded by timeouts, and checked for expected outputs.
3. Reporting is read-only and cannot invoke mutation engines.
4. Candidate generation and publication are separate processes.
5. The publisher accepts only a fixed allowlist of artifact paths for the selected engine and playlist.
6. EPG source fetches run before candidate generation; validation and atomic publication remain separate.
7. Runtime dependency tracing is still incomplete. Before cutover, inspect every script invoked from workflows and every nested subprocess target, then map those targets to contract tests.
