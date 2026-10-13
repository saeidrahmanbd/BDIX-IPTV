# Update Report

_Last generated: **2026-10-13 04:28 UTC**_

| Metric | Current |
|---|---:|
| Streams | **1031** |
| Active Channel Identities | **624** |
| Active Primary Streams | **629** |
| Bangladesh | **60** |
| India | **283** |
| Backup Streams | **402** |
| Local Logos | **98.7%** |
| EPG Programme Coverage | **79.7%** |
| EPG Mapping | **83.5%** |
| Stream Health Tested | **1031** |
| Stream Health Failures | **146** |
| Persistent Failures | **139** |
| Near-Duplicate URL Families | **0** |
| Audit Blocking Issues | **12** |
| Pre-Publish Gate | **BLOCK** |
| Pre-Publish Gate Generated | **2026-10-13T04:27:22+00:00** |

## Quality Controls
- Duplicate stream URLs: **0**
- Metadata conflicts: **1**
- Same-name / different-ID collisions: **9**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **4**
- Logo exceptions: **4**
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
- Indian channels audited: **291**
- Mapped: **243 (83.5%)**
- Current/future programme coverage: **232/291 (79.7%)**
- No mapping: **48**
- Publication remains subject to source-policy approval.

## Freshness
| Report | Last generated |
|---|---|
| Playlist audit | **2026-10-13T04:27:22.211424+00:00** |
| EPG coverage | **2026-10-13T04:25:57+00:00** |
| Stream health | **2026-10-13T04:28:42+00:00** |
| Pre-publish gate | **2026-10-13T04:27:22+00:00** |

## Maintenance History
- Records retained: **30**
- Latest entries change: **1018 → 1031**
- Latest health failures: **145 → 146**

Historical records are retained in reports/maintenance-history.json.
