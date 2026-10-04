# Update Report

_Last generated: **2026-10-04 17:43 UTC**_

| Metric | Current |
|---|---:|
| Streams | **1021** |
| Active Channel Identities | **592** |
| Active Primary Streams | **592** |
| Bangladesh | **58** |
| India | **268** |
| Backup Streams | **353** |
| New Channels | **0** |
| New Backup Streams | **0** |
| Local Logos | **100.0%** |
| EPG Programme Coverage | **78.7%** |
| EPG Mapping | **83.6%** |
| Stream Health Tested | **969** |
| Stream Health Failures | **125** |
| Persistent Failures | **114** |
| Near-Duplicate URL Families | **0** |
| Audit Blocking Issues | **3** |
| Pre-Publish Gate | **PASS** |
| Pre-Publish Gate Generated | **2026-10-04T17:43:12+00:00** |

## Quality Controls
- Duplicate stream URLs: **0**
- Metadata conflicts: **0**
- Same-name / different-ID collisions: **0**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **0**
- Logo exceptions: **0**
- Not Playing logo exceptions: **0**
- Malformed EXTINF entries: **0**
- Category block-order issues: **1**
- Alphabetical ordering issues: **2**
- Signed/tokenized URLs: **9**

## Safety & Automation
- Stream health is non-destructive and keeps per-URL failure history.
- Backup streams are never automatically deleted because of health failures.
- Review queues remain user-controlled.
- Pre-publish gate status: **PASS**
- Canonical channel identity index: reports/channel-identity-index.json

## EPG
- Indian channels audited: **268**
- Mapped: **224 (83.6%)**
- Current/future programme coverage: **211/268 (78.7%)**
- No mapping: **44**
- Publication remains subject to source-policy approval.

## Freshness
| Report | Last generated |
|---|---|
| Playlist audit | **2026-10-04T17:42:25.226635+00:00** |
| EPG coverage | **2026-10-04T17:42:23+00:00** |
| Stream health | **2026-10-04T17:43:12+00:00** |
| Pre-publish gate | **2026-10-04T17:43:12+00:00** |

## Maintenance History
- Records retained: **30**
- Latest entries change: **1026 → 1021**
- Latest health failures: **120 → 125**

Historical records are retained in reports/maintenance-history.json.
