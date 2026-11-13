# Logo storage audit — baseline findings

Baseline: `46275f5ebafa2ae1b56f3e480f684ac1e85ae45e`

## Preliminary exact-reference result

- Logo image assets: **5,366** (PNG/JPEG/WebP/GIF/SVG).
- Unique normalized logo paths referenced by the two production playlist files: **2,395**.
- Exact logo assets referenced by those playlists: **2,395**.
- Apparent non-references from those two playlist files alone: **2,971**.
- Missing local targets among the playlist's normalized repository logo references: **0**.

The complete preliminary path list is in [logo-reference-baseline.json](logo-reference-baseline.json).

## Important limitation

The 2,971 files are **not yet proven unused**. This first pass checks only the two playlists' `tvg-logo` values against exact paths in the baseline tree. It does not establish whether a logo is referenced by scripts, registries, JSON/YAML configuration, EPG mappings, reports, web pages, archived recovery data, generated filenames, or external clients.

A conservative repository-wide scanner has therefore been added at `scripts/audit_logo_references.py`. It reads text files and reports explicit `logos/<filename>` references. It does not delete, move, rewrite, or stage assets. Dynamic filename construction, binary references and consumers outside this repository still require review.

## Cleanup decision

**No deletion is authorized by this audit.** The next cleanup stage must:
1. Run the repository-wide scanner against the exact baseline checkout.
2. Review every script/config/registry reference and dynamic logo-name construction.
3. Compare image hashes to identify byte-identical duplicates without removing them.
4. Generate a quarantine manifest and candidate branch-only move plan.
5. Run playlist, website, report, logo integrity and rollback tests against the candidate.
6. Obtain a final cutover approval before any production asset removal.

The quarantine candidate must be reversible and must not delete from production during migration.
