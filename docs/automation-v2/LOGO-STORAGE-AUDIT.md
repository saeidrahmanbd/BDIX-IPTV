# Logo storage audit — baseline and repository-wide findings

Baseline: 46275f5ebafa2ae1b56f3e480f684ac1e85ae45e

## Playlist-only baseline

- Logo image assets: **5,366** (PNG/JPEG/WebP/GIF/SVG).
- Unique normalized logo paths referenced by the two production playlist files: **2,395**.
- Exact logo assets referenced by those playlists: **2,395**.
- Apparent non-references from those two playlist files alone: **2,971**.
- Missing local targets among the playlist's normalized repository logo references: **0**.

The complete preliminary path list is in logo-reference-baseline.json.

## Repository-wide audit (CI run 69)

The repository-wide scanner now separates active playlist references, runtime code/config/registry references, and report-only references. It also checks exact byte-identical file hashes.

- Total logo image files: **5,366**.
- Distinct assets referenced by production playlists: **2,395**.
- Distinct assets referenced by runtime sources (playlists, scripts, workflows, automation and the two active logo registries/manifests): **2,691**.
- Assets with no explicit reference in any scanned text file: **1,796**.
- Assets with no explicit reference in the classified runtime sources: **2,675**.
- Exact byte-identical duplicate groups: **718**, containing **1,061** extra duplicate copies.
- Duplicate groups with no runtime-referenced member: **146 groups / 373 files**.
- Missing targets referenced by runtime sources: **75**. The audit did not find any of these 75 missing targets referenced directly by either production playlist; their listed sources are scripts and logo registries/manifests.

The full machine-readable report is uploaded as the automation-v2-logo-reference-audit artifact in CI run 69:
https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/43402368928

It includes exact file lists and source paths.

## Interpretation and limitations

These are **audit candidates, not deletion approvals**. The 2,675 runtime non-references can still be needed by dynamically constructed paths, older recovery scripts, connected clients, cached playlists or future channel discoveries. Exact byte duplicates may intentionally serve different regional channels or metadata paths. Registry/manifests may also contain historical paths that need reconciliation rather than asset deletion.

The 75 missing runtime targets require separate triage: some are stale registry/source-catalog entries or historical paths, not missing logos in the currently published playlists.

## Cleanup decision

**No logo has been deleted, moved or quarantined.** Cleanup will proceed only after:
1. Inspecting dynamic filename construction and external consumer assumptions.
2. Classifying the 2,675 runtime non-reference paths into safe, historical, recovery-dependent and uncertain groups.
3. Resolving the 75 missing registry/script targets and checking report freshness.
4. Creating a reversible quarantine manifest and branch-only move candidate.
5. Running playlist, logo integrity, report, EPG and rollback regression tests on the candidate.
6. Obtaining final production cutover approval.

The audit workflow itself is read-only; it never stages, moves or deletes logo assets.
