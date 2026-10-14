# Update Report

_Last generated: **2026-10-14 03:58 UTC**_

| Metric | Current |
|---|---:|
| Streams | **940** |
| Active Channel Identities | **561** |
| Active Primary Streams | **578** |
| Bangladesh | **55** |
| India | **275** |
| Backup Streams | **362** |
| Local Logos | **93.1%** |
| EPG Programme Coverage | **80.0%** |
| EPG Mapping | **83.1%** |
| Stream Health Tested | **940** |
| Stream Health Failures | **52** |
| Persistent Failures | **16** |
| Near-Duplicate URL Families | **0** |
| Audit Blocking Issues | **79** |
| Pre-Publish Gate | **BLOCK** |
| Pre-Publish Gate Generated | **2026-10-14T03:57:50+00:00** |

## Quality Controls
- Duplicate stream URLs: **0**
- Metadata conflicts: **3**
- Same-name / different-ID collisions: **35**
- Duplicate primary identities: **2**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **35**
- Logo exceptions: **14**
- Malformed EXTINF entries: **19**
- Category block-order issues: **0**
- Alphabetical ordering issues: **6**
- Signed/tokenized URLs: **9**

## Safety & Automation
- Stream health is non-destructive and keeps per-URL failure history.
- Backup streams are never automatically deleted because of health failures.
- Discovery queues are retired; only the approved canonical playlist categories are maintained.
- Pre-publish gate status: **BLOCK**
- Canonical channel identity index: reports/channel-identity-index.json

## EPG
- Indian channels audited: **290**
- Mapped: **241 (83.1%)**
- Current/future programme coverage: **232/290 (80.0%)**
- No mapping: **49**
- Publication remains subject to source-policy approval.

## Freshness
| Report | Last generated |
|---|---|
| Playlist audit | **2026-10-14T03:57:50.037442+00:00** |
| EPG coverage | **2026-10-14T03:57:01+00:00** |
| Stream health | **2026-10-14T03:58:34+00:00** |
| Pre-publish gate | **2026-10-14T03:57:50+00:00** |

## Maintenance History
- Records retained: **30**
- Latest entries change: **1031 → 940**
- Latest health failures: **143 → 52**

Historical records are retained in reports/maintenance-history.json.
