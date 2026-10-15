# Update Report

_Last generated: **2026-10-15 11:45 UTC**_

| Metric | Current |
|---|---:|
| Streams | **1020** |
| Active Channel Identities | **638** |
| Active Primary Streams | **638** |
| Bangladesh | **63** |
| India | **288** |
| Backup Streams | **382** |
| Local Logos | **100.0%** |
| EPG Programme Coverage | **60.5%** |
| EPG Mapping | **64.1%** |
| Stream Health Tested | **1020** |
| Stream Health Failures | **66** |
| Persistent Failures | **65** |
| Near-Duplicate URL Families | **0** |
| Audit Blocking Issues | **0** |
| Pre-Publish Gate | **PASS** |
| Pre-Publish Gate Generated | **2026-10-15T11:45:37+00:00** |

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
- Active channel IDs audited: **693**
- Mapped: **444 (64.1%)**
- Current/future programme coverage: **419/693 (60.5%)**
- No mapping: **249**
- Publication remains subject to source-policy approval.

## Freshness
| Report | Last generated |
|---|---|
| Playlist audit | **2026-10-15T11:44:44.026139+00:00** |
| EPG coverage | **2026-10-15T11:44:42+00:00** |
| Stream health | **2026-10-15T11:45:37+00:00** |
| Pre-publish gate | **2026-10-15T11:45:37+00:00** |

## Maintenance History
- Records retained: **30**
- Latest entries change: **1020 → 1020**
- Latest health failures: **66 → 66**

Historical records are retained in reports/maintenance-history.json.
