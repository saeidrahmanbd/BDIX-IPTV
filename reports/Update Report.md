# Update Report

_Last generated: **2026-10-14 07:54 UTC**_

| Metric | Current |
|---|---:|
| Streams | **940** |
| Active Channel Identities | **577** |
| Active Primary Streams | **594** |
| Bangladesh | **56** |
| India | **285** |
| Backup Streams | **346** |
| Local Logos | **93.1%** |
| EPG Programme Coverage | **59.6%** |
| EPG Mapping | **63.7%** |
| Stream Health Tested | **940** |
| Stream Health Failures | **37** |
| Persistent Failures | **15** |
| Near-Duplicate URL Families | **0** |
| Audit Blocking Issues | **69** |
| Pre-Publish Gate | **BLOCK** |
| Pre-Publish Gate Generated | **2026-10-14T07:54:23+00:00** |

## Quality Controls
- Duplicate stream URLs: **0**
- Metadata conflicts: **1**
- Same-name / different-ID collisions: **35**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **51**
- Logo exceptions: **16**
- Malformed EXTINF entries: **0**
- Category block-order issues: **0**
- Alphabetical ordering issues: **1**
- Signed/tokenized URLs: **9**

## Safety & Automation
- Stream health is non-destructive and keeps per-URL failure history.
- Backup streams are never automatically deleted because of health failures.
- Discovery queues are retired; only the approved canonical playlist categories are maintained.
- Pre-publish gate status: **BLOCK**
- Canonical channel identity index: reports/channel-identity-index.json

## EPG
- Active channel IDs audited: **648**
- Mapped: **413 (63.7%)**
- Current/future programme coverage: **386/648 (59.6%)**
- No mapping: **235**
- Publication remains subject to source-policy approval.

## Freshness
| Report | Last generated |
|---|---|
| Playlist audit | **2026-10-14T07:54:22.927765+00:00** |
| EPG coverage | **2026-10-14T07:53:43+00:00** |
| Stream health | **2026-10-14T07:54:58+00:00** |
| Pre-publish gate | **2026-10-14T07:54:23+00:00** |

## Maintenance History
- Records retained: **30**
- Latest entries change: **940 → 940**
- Latest health failures: **16 → 37**

Historical records are retained in reports/maintenance-history.json.
