# Update Report

_Last generated: **2026-10-12 12:13 UTC**_

| Metric | Current |
|---|---:|
| Streams | **1018** |
| Active Channel Identities | **624** |
| Active Primary Streams | **625** |
| Bangladesh | **58** |
| India | **283** |
| Backup Streams | **393** |
| Local Logos | **100.0%** |
| EPG Programme Coverage | **80.4%** |
| EPG Mapping | **83.5%** |
| Stream Health Tested | **1018** |
| Stream Health Failures | **141** |
| Persistent Failures | **129** |
| Near-Duplicate URL Families | **0** |
| Audit Blocking Issues | **1** |
| Pre-Publish Gate | **PASS** |
| Pre-Publish Gate Generated | **2026-10-12T12:13:33+00:00** |

## Quality Controls
- Duplicate stream URLs: **0**
- Metadata conflicts: **1**
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
- Indian channels audited: **291**
- Mapped: **243 (83.5%)**
- Current/future programme coverage: **234/291 (80.4%)**
- No mapping: **48**
- Publication remains subject to source-policy approval.

## Freshness
| Report | Last generated |
|---|---|
| Playlist audit | **2026-10-12T12:12:17.984372+00:00** |
| EPG coverage | **2026-10-12T12:12:12+00:00** |
| Stream health | **2026-10-12T12:13:33+00:00** |
| Pre-publish gate | **2026-10-12T12:13:33+00:00** |

## Maintenance History
- Records retained: **30**
- Latest entries change: **1018 → 1018**
- Latest health failures: **132 → 141**

Historical records are retained in reports/maintenance-history.json.
