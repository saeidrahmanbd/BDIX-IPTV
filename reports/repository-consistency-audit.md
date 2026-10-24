# Repository Consistency Audit

_Last reviewed: 2026-10-24 (UTC)_

## Scope

This re-audit covers repository identity, documentation, workflow references and concurrency, report generation, International playlist metadata/logo references, EPG communication, and repository hygiene. It does **not** test stream playback or intentionally alter individual stream URLs.

## Confirmed fixes

| Area | Current disposition |
|---|---|
| Repository identity | README positions the project as a **Bangladesh & India IPTV Hub**, with selected international channels as secondary scope. The GitHub repository description already names Bangladesh and India. |
| Playlist access | README, Download Center, and Wiki list the main, BDIX, and International playlists. |
| Report generation | Fixed the dashboard EPG-table parser that failed with an IndexError, added a scalar near-duplicate URL-family metric, and separated IPTV-only EPG metrics from combined-guide metrics. |
| Workflow script references | Replaced missing epg_publish_gate.py calls with epg_publish_gate_v2.py and removed obsolete missing-script references. Current workflow-reference validation and Python compilation tests passed on commit 0897596. |
| Writer coordination | Changelog, maintenance, and International playlist writers use the common iptv-playlist-main-writer concurrency group with pending-run queuing. |
| International playlist | Restored the attribution block, rebuilt the category registry, removed 18 dangling logo attributes without inventing replacements, and preserved the stream-URL multiset during the metadata-only edit. |
| International validation | Added a reusable validator for attribution, category order/registry, forbidden staging groups, duplicate URLs, and broken/external logo references. It does not test stream playback; missing logo attributes are counted, not concealed. |
| International discovery | New primary feeds go to an established/threshold country group or content category; alternates go to Backup. The five-channel threshold counts unique eligible primary identities rather than URL variants. |
| Public reports | Sanitized the International audit report so it no longer prints stream URLs or credentials and does not enumerate Adult-category items. The report generator was changed accordingly. |
| Documentation | Clarified the EPG redistribution-rights caveat, replaced the obsolete logo gallery with a concise policy/index, and removed dated no-op changelog entries. |
| Repository hygiene | Added .gitignore and weekly GitHub Actions Dependabot updates. Existing LICENSE, SECURITY.md, and CONTRIBUTING.md remain present. |
| Superseded automation | Removed duplicate consistency-repair workflows, an unused report-reconciliation script, an unused duplicate International-discovery script, and the unused International restore-trigger file. |

## Report freshness warning

The committed Update Report still shows the older 1,265-entry snapshot and old playlist fingerprint. The current IPTV playlist had 1,272 entries at the last direct inventory check. The dashboard crash is fixed, but generated totals should be treated as **stale until the queued IPTV Playlist Update workflow completes successfully** and regenerates them from one current revision.

The validation failure at commit 226674d only reported validate_international_playlist.py missing because that run's commit predates the new script. A later workflow-reference validation run completed successfully after the file was added. Do not interpret the older failed run as the current branch's validation status.

## Remaining items needing review, not guessed fixes

- **Logo provenance:** the provenance report has shown many unresolved source records. Local storage is not proof of authenticity or permission to redistribute. Do not claim that all logos are verified.
- **Missing logo metadata:** the International playlist still has entries without logo attributes. No generic or unrelated artwork was substituted to make coverage appear complete.
- **Metadata gaps and ID variants:** missing language fields, same-name/different-ID variants, and country/language ambiguity need source-specific decisions. The new cross-queue counts are diagnostic signals; they are not authorization to merge distinct channels.
- **EPG availability and rights:** Bangladesh guide coverage remains weak, and redistribution rights are not confirmed for every source. Technical mapping/coverage percentages are not a licensing approval.
- **BDIX Test entries:** the misleading Test group and its repeated Bangla Vision label/logo remain a separate playlist-content cleanup item. This re-audit did not guess replacement identities.
- **Asset inventory:** the repository has many unreferenced and duplicate logo files. They were not bulk-deleted because filenames alone cannot establish that an asset is unused by a restore workflow or historical playlist.
- **Image file naming:** renamed the banner asset path to assets/Saeid Rahman.jpg by reusing the original Git blob, preserving the binary bytes exactly; updated the README reference.
- **Action pinning:** checkout v7, setup-python v7, setup-node v4, upload-artifact v4, and Wrangler Action v4 are pinned to reviewed commit SHAs. Dependabot surfaces future GitHub Actions updates; updates should pass validation before merging.
- **Generated report timing:** audit, EPG, stream-health, logo, and Update Report files should be regenerated and reviewed together after the current maintenance run; values from different timestamps must not be compared as though they came from one snapshot.

## Counting rules

- Active primary stream counts exclude New Channels, New Backup, and Not Playing review queues.
- EPG IDs audited use the scope stated by the relevant report; the combined three-playlist guide count is not the same metric as IPTV-only published-programme coverage.
- Backup rows count URL references, not guaranteed independent origins/CDNs/renditions.
- HTTP reachability is not proof of playback availability in Bangladesh or India.

