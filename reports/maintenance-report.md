# IPTV Maintenance Report

Generated from the current main playlist audit: **2026-10-01 09:12 UTC**

## Current Reconciliation

| Item | Result |
|---|---:|
| Current playlist entries | **1,000** |
| Active primary entries | **587** |
| Backup entries | **413** |
| Unique channel IDs | **624** |
| Duplicate stream URLs | **0** |
| Duplicate primary identities | **5** |
| Missing primary channel numbers | **31** |
| External/missing logos | **0** |
| Signed/tokenized URLs | **15** |
| Same-name / different-ID warnings | **6** |

## Findings

The previous generated dashboard was stale relative to the current playlist. The current playlist is 33 entries smaller than the previous reported 1,033-entry snapshot.

The playlist is structurally incomplete because five active identity collisions remain and 31 active entries have no tvg-chno.

No stream URL was removed by this audit.

## EPG Reconciliation

The current playlist contains **259 Indian-category entries**, while the existing EPG report was generated against **244**. Its mapping/coverage figures therefore need a fresh EPG run.

## Stream Health

No reachability result is claimed here. The existing audit is metadata/structure-focused and does not perform live stream probing.

## Recommended Next Maintenance Actions

1. Resolve the 5 duplicate primary identities with controlled alternate IDs where they are genuinely separate stream records.
2. Assign unique tvg-chno values to the 31 missing primary entries.
3. Regenerate EPG coverage against the current playlist.
4. Add a separate health-check stage; do not automatically delete Backup entries from a single failed probe.
