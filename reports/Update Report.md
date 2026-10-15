# Update Report

_Last generated: **2026-10-15 10:06 UTC**_

| Metric | Current |
|---|---:|
| Streams | **1037** |
| Active Channel Identities | **652** |
| Active Primary Streams | **652** |
| Bangladesh | **63** |
| India | **290** |
| Backup Streams | **385** |
| Local Logos | **100.0%** |
| EPG Programme Coverage | **60.6%** |
| EPG Mapping | **64.3%** |
| Stream Health Tested | **1037** |
| Stream Health Failures | **73** |
| Persistent Failures | **38** |
| Near-Duplicate URL Families | **0** |
| Audit Blocking Issues | **0** |
| Pre-Publish Gate | **PASS** |
| Pre-Publish Gate Generated | **2026-10-15T10:06:20+00:00** |

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
- Active channel IDs audited: **703**
- Mapped: **452 (64.3%)**
- Current/future programme coverage: **426/703 (60.6%)**
- No mapping: **251**
- Publication remains subject to source-policy approval.

## Freshness
| Report | Last generated |
|---|---|
| Playlist audit | **2026-10-15T10:05:26.988492+00:00** |
| EPG coverage | **2026-10-15T10:05:25+00:00** |
| Stream health | **2026-10-15T10:06:20+00:00** |
| Pre-publish gate | **2026-10-15T10:06:20+00:00** |

## Maintenance History
- Records retained: **30**
- Latest entries change: **1037 → 1037**
- Latest health failures: **68 → 73**

Historical records are retained in reports/maintenance-history.json.
