# Update Report

_Last generated: **2026-10-15 06:06 UTC**_

| Metric | Current |
|---|---:|
| Streams | **1043** |
| Active Channel Identities | **567** |
| Active Primary Streams | **636** |
| Bangladesh | **59** |
| India | **286** |
| Backup Streams | **407** |
| Local Logos | **94.9%** |
| EPG Programme Coverage | **0.0%** |
| EPG Mapping | **64.0%** |
| Stream Health Tested | **1043** |
| Stream Health Failures | **53** |
| Persistent Failures | **4** |
| Near-Duplicate URL Families | **0** |
| Audit Blocking Issues | **116** |
| Pre-Publish Gate | **BLOCK** |
| Pre-Publish Gate Generated | **2026-10-15T06:05:49+00:00** |

## Quality Controls
- Duplicate stream URLs: **0**
- Metadata conflicts: **2**
- Same-name / different-ID collisions: **77**
- Duplicate primary identities: **1**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **57**
- Logo exceptions: **53**
- Malformed EXTINF entries: **0**
- Category block-order issues: **0**
- Alphabetical ordering issues: **3**
- Signed/tokenized URLs: **9**

## Safety & Automation
- Stream health is non-destructive and keeps per-URL failure history.
- Backup streams are never automatically deleted because of health failures.
- Discovery queues are retired; only the approved canonical playlist categories are maintained.
- Pre-publish gate status: **BLOCK**
- Canonical channel identity index: reports/channel-identity-index.json

## EPG
- Active channel IDs audited: **689**
- Mapped: **441 (64.0%)**
- Current/future programme coverage: **0/689 (0.0%)**
- No mapping: **248**
- Publication remains subject to source-policy approval.

## Freshness
| Report | Last generated |
|---|---|
| Playlist audit | **2026-10-15T06:05:49.729605+00:00** |
| EPG coverage | **2026-10-15T06:05:04+00:00** |
| Stream health | **2026-10-15T06:06:33+00:00** |
| Pre-publish gate | **2026-10-15T06:05:49+00:00** |

## Maintenance History
- Records retained: **30**
- Latest entries change: **940 → 1043**
- Latest health failures: **30 → 53**

Historical records are retained in reports/maintenance-history.json.
