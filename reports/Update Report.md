# Update Report

_Last generated: **2026-10-15 06:33 UTC**_

| Metric | Current |
|---|---:|
| Streams | **1043** |
| Active Channel Identities | **634** |
| Active Primary Streams | **634** |
| Bangladesh | **58** |
| India | **285** |
| Backup Streams | **409** |
| Local Logos | **99.9%** |
| EPG Programme Coverage | **60.4%** |
| EPG Mapping | **64.0%** |
| Stream Health Tested | **1043** |
| Stream Health Failures | **16** |
| Persistent Failures | **10** |
| Near-Duplicate URL Families | **0** |
| Audit Blocking Issues | **22** |
| Pre-Publish Gate | **PASS** |
| Pre-Publish Gate Generated | **2026-10-15T06:33:30+00:00** |

## Quality Controls
- Duplicate stream URLs: **0**
- Metadata conflicts: **0**
- Same-name / different-ID collisions: **80**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **0**
- Logo exceptions: **1**
- Malformed EXTINF entries: **0**
- Category block-order issues: **12**
- Alphabetical ordering issues: **9**
- Signed/tokenized URLs: **9**

## Safety & Automation
- Stream health is non-destructive and keeps per-URL failure history.
- Backup streams are never automatically deleted because of health failures.
- Discovery queues are retired; only the approved canonical playlist categories are maintained.
- Pre-publish gate status: **PASS**
- Canonical channel identity index: reports/channel-identity-index.json

## EPG
- Active channel IDs audited: **689**
- Mapped: **441 (64.0%)**
- Current/future programme coverage: **416/689 (60.4%)**
- No mapping: **248**
- Publication remains subject to source-policy approval.

## Freshness
| Report | Last generated |
|---|---|
| Playlist audit | **2026-10-15T06:33:30.071658+00:00** |
| EPG coverage | **2026-10-15T06:33:07+00:00** |
| Stream health | **2026-10-15T06:33:48+00:00** |
| Pre-publish gate | **2026-10-15T06:33:30+00:00** |

## Maintenance History
- Records retained: **30**
- Latest entries change: **1043 → 1043**
- Latest health failures: **53 → 16**

Historical records are retained in reports/maintenance-history.json.
