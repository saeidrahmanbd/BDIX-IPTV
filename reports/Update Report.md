# Update Report

_Last generated: **2026-10-15 08:38 UTC**_

| Metric | Current |
|---|---:|
| Streams | **1035** |
| Active Channel Identities | **632** |
| Active Primary Streams | **632** |
| Bangladesh | **59** |
| India | **283** |
| Backup Streams | **403** |
| Local Logos | **100.0%** |
| EPG Programme Coverage | **60.6%** |
| EPG Mapping | **64.2%** |
| Stream Health Tested | **1035** |
| Stream Health Failures | **27** |
| Persistent Failures | **11** |
| Near-Duplicate URL Families | **0** |
| Audit Blocking Issues | **7** |
| Pre-Publish Gate | **BLOCK** |
| Pre-Publish Gate Generated | **2026-10-15T08:38:31+00:00** |

## Quality Controls
- Duplicate stream URLs: **1**
- Metadata conflicts: **0**
- Same-name / different-ID collisions: **1**
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
- Pre-publish gate status: **BLOCK**
- Canonical channel identity index: reports/channel-identity-index.json

## EPG
- Active channel IDs audited: **687**
- Mapped: **441 (64.2%)**
- Current/future programme coverage: **416/687 (60.6%)**
- No mapping: **246**
- Publication remains subject to source-policy approval.

## Freshness
| Report | Last generated |
|---|---|
| Playlist audit | **2026-10-15T08:37:55.533819+00:00** |
| EPG coverage | **2026-10-15T08:37:53+00:00** |
| Stream health | **2026-10-15T08:38:31+00:00** |
| Pre-publish gate | **2026-10-15T08:38:31+00:00** |

## Maintenance History
- Records retained: **30**
- Latest entries change: **1043 → 1035**
- Latest health failures: **22 → 27**

Historical records are retained in reports/maintenance-history.json.
