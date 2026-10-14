# Update Report

_Last generated: **2026-10-14 10:00 UTC**_

| Metric | Current |
|---|---:|
| Streams | **940** |
| Active Channel Identities | **577** |
| Active Primary Streams | **594** |
| Bangladesh | **56** |
| India | **285** |
| Backup Streams | **346** |
| Local Logos | **100.0%** |
| EPG Programme Coverage | **0.0%** |
| EPG Mapping | **65.2%** |
| Stream Health Tested | **940** |
| Stream Health Failures | **99** |
| Persistent Failures | **88** |
| Near-Duplicate URL Families | **0** |
| Audit Blocking Issues | **52** |
| Pre-Publish Gate | **BLOCK** |
| Pre-Publish Gate Generated | **2026-10-14T10:00:16+00:00** |

## Quality Controls
- Duplicate stream URLs: **0**
- Metadata conflicts: **1**
- Same-name / different-ID collisions: **35**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **51**
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
- Active channel IDs audited: **647**
- Mapped: **422 (65.2%)**
- Current/future programme coverage: **0/647 (0.0%)**
- No mapping: **225**
- Publication remains subject to source-policy approval.

## Freshness
| Report | Last generated |
|---|---|
| Playlist audit | **2026-10-14T10:00:16.539094+00:00** |
| EPG coverage | **2026-10-14T09:59:48+00:00** |
| Stream health | **2026-10-14T10:00:42+00:00** |
| Pre-publish gate | **2026-10-14T10:00:16+00:00** |

## Maintenance History
- Records retained: **30**
- Latest entries change: **940 → 940**
- Latest health failures: **90 → 99**

Historical records are retained in reports/maintenance-history.json.
