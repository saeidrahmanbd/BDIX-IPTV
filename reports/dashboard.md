# Project Dashboard

Last audited directly from the current main playlist: **2026-10-01 09:12 UTC**

> **Audit status: NEEDS REPAIR** — the current playlist differs from the previous dashboard snapshot.

| Metric | Current |
|---|---:|
| Total Streams | **1,000** |
| Active Primary Entries | **587** |
| Unique Channel IDs | **624** |
| Bangladesh | **57** |
| Indian Categories | **259** |
| Backup Streams | **413** |
| Local Logos | **100.0%** |
| New Channels | **0** |
| New Backup Streams | **0** |
| EPG Mapping | **158 / 259 = 61.0%*** |
| Structural Blockers | **36** |
| Duplicate Stream URLs | **0** |
| Signed/Tokenized URLs | **15** |
| Identity Warnings | **6** |

*The existing EPG report is stale: it still uses a 244-channel denominator while the current playlist has 259 Indian entries. Regenerate it before treating its percentages as current.

## Quality Controls

- Duplicate stream URLs: **0**
- Duplicate primary identities: **5**
- Primary channel-number collisions: **0**
- Primary entries missing tvg-chno: **31**
- Missing tvg-id: **0**
- Missing channel-id: **0**
- Missing tvg-name: **0**
- Missing tvg-logo: **0**
- External logo references: **0**
- Suspicious credential/malformed URLs: **0**
- Signed/tokenized stream URLs: **15**
- Same-name / different-ID collisions: **6**

## Structural Blockers

**36 total:** 5 duplicate primary identities + 31 missing primary channel numbers.

## Important Reporting Correction

The previous dashboard reported **1,033 streams, 560 active channels, 244 Indian entries, 420 backups, and 0 blocking issues**. Those figures are not current.

The live main playlist contains **1,000 entries**, including **587 active primary entries and 413 backups**.

## EPG Status

The existing EPG report says 244 Indian channels, 158 mappings, 86 unmapped, and 146/244 programme coverage (59.8%). Because the current playlist has 259 Indian entries, the EPG report requires regeneration.

## Stream Health

This dashboard does not claim that streams are online. The structural audit verifies playlist integrity only. A separate health probe is required for reachability.

## Reports

- reports/playlist-audit.md — current structural audit.
- reports/epg-coverage.md — EPG mapping/coverage; currently requires regeneration.
- reports/maintenance-report.md — maintenance summary.
- reports/maintenance-history.json — historical automation records.
