# Update Report

_Last generated: **2026-10-12 03:13 UTC**_

| Metric | Current |
|---|---:|
| Streams | **1145** |
| Active Channel Identities | **652** |
| Active Primary Streams | **652** |
| Bangladesh | **60** |
| India | **299** |
| Backup Streams | **493** |
| Local Logos | **100.0%** |
| EPG Programme Coverage | **77.7%** |
| EPG Mapping | **80.9%** |
| Stream Health Tested | **1145** |
| Stream Health Failures | **221** |
| Persistent Failures | **195** |
| Near-Duplicate URL Families | **0** |
| Audit Blocking Issues | **0** |
| Pre-Publish Gate | **PASS** |
| Pre-Publish Gate Generated | **2026-10-12T03:13:49+00:00** |

## Quality Controls
- Duplicate stream URLs: **0**
- Metadata conflicts: **0**
- Same-name / different-ID collisions: **0**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **0**
- Logo exceptions: **0**
- Malformed EXTINF entries: **0**
- Category block-order issues: **0**
- Alphabetical ordering issues: **0**
- Signed/tokenized URLs: **9**

## Safety & Automation
- Stream health is non-destructive and keeps per-URL failure history.
- Backup streams are never automatically deleted because of health failures.
- Discovery queues are retired; only the approved canonical playlist categories are maintained.
- Pre-publish gate status: **PASS**
- Canonical channel identity index: reports/channel-identity-index.json

## EPG
- Indian channels audited: **341**
- Mapped: **276 (80.9%)**
- Current/future programme coverage: **265/341 (77.7%)**
- No mapping: **65**
- Publication remains subject to source-policy approval.

## Freshness
| Report | Last generated |
|---|---|
| Playlist audit | **2026-10-12T03:12:13.859907+00:00** |
| EPG coverage | **2026-10-12T03:12:08+00:00** |
| Stream health | **2026-10-12T03:13:49+00:00** |
| Pre-publish gate | **2026-10-12T03:13:49+00:00** |

## Maintenance History
- Records retained: **30**
- Latest entries change: **1145 → 1145**
- Latest health failures: **203 → 221**

Historical records are retained in reports/maintenance-history.json.
