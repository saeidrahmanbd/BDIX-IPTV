# EPG baseline coverage audit

Baseline commit: 46275f5ebafa2ae1b56f3e480f684ac1e85ae45e

Dry-run source: CI run 87, immutable production baseline check. The dry-run verified the Git blob fingerprints of both production playlists and epg/epg.xml before parsing them. It generated no candidate changes and did not publish anything.

## Current coverage

| Metric | IPTV-Playlist.m3u | International-Playlist.m3u |
|---|---:|---:|
| Playlist rows | 1,280 | 3,120 |
| Unique active tvg-id values | 776 | 2,684 |
| IDs present in XMLTV | 411 (52.96%) | 662 (24.66%) |
| IDs with at least one programme | 363 (46.78%) | 586 (21.83%) |
| IDs with current/future programmes | 321 (41.37%) | 541 (20.16%) |
| Mapped IDs with only past programmes | 42 | 45 |
| Mapped IDs with no programme | 48 | 76 |
| Active IDs absent from XMLTV | 365 | 2,022 |

The guide contained 42,425 programmes with stop times later than the dry-run timestamp.

## Interpretation

- XMLTV is structurally parseable, but mapping coverage is insufficient, especially for International.
- A channel ID being present in the XMLTV channel list does not mean it has any programme data.
- A channel with programme entries may still have only expired schedules.
- Current/future schedule coverage is the most useful operational measure for this migration.
- These figures are baseline diagnostics, not proof that every unmapped ID should be mapped. Some playlist channels may be intentionally unsupported or not have a valid guide source.

## Migration requirements

1. Build a conservative alias suggestion report using playlist channel names and XMLTV display names. Suggestions must not be auto-applied.
2. Classify unmapped IDs into exact-name matches, high-confidence fuzzy matches, ambiguous matches and no-match.
3. Identify stale-only and mapped-without-schedule channels separately.
4. Add approved aliases to the central EPG mapping registry and test for collisions.
5. Rebuild a candidate guide and compare per-channel mapping and current/future schedule coverage with this baseline.
6. Reject any candidate that loses an existing mapped or currently scheduled active channel without explicit owner-reviewed justification.
7. Do not replace the published EPG until the candidate passes all checks and the production cutover is separately approved.

The V2 EPG candidate gate currently rejects structural errors, channel-count regressions, mapping regressions and current/future schedule regressions. It does not publish or modify epg.xml.
