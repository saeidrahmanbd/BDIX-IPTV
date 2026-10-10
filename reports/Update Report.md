# Update Report

_Last generated: **2026-10-10 13:14 UTC**_

| Metric | Current |
|---|---:|
| Streams | **1061** |
| Active Channel Identities | **594** |
| Active Primary Streams | **594** |
| Bangladesh | **57** |
| India | **276** |
| Backup Streams | **398** |
| New Channels | **0** |
| New Backup Streams | **0** |
| Local Logos | **99.9%** |
| EPG Programme Coverage | **79.0%** |
| EPG Mapping | **81.9%** |
| Stream Health Tested | **1008** |
| Stream Health Failures | **173** |
| Persistent Failures | **168** |
| Near-Duplicate URL Families | **0** |
| Audit Blocking Issues | **6** |
| Pre-Publish Gate | **PASS** |
| Pre-Publish Gate Generated | **2026-10-10T13:13:33+00:00** |

## Quality Controls
- Duplicate stream URLs: **0**
- Metadata conflicts: **0**
- Same-name / different-ID collisions: **28**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **0**
- Logo exceptions: **0**
- Not Playing logo exceptions: **1**
- Malformed EXTINF entries: **0**
- Category block-order issues: **0**
- Alphabetical ordering issues: **5**
- Signed/tokenized URLs: **9**

## Safety & Automation
- Stream health is non-destructive and keeps per-URL failure history.
- Backup streams are never automatically deleted because of health failures.
- Review queues remain user-controlled.
- Pre-publish gate status: **PASS**
- Canonical channel identity index: reports/channel-identity-index.json

## EPG
- Indian channels audited: **276**
- Mapped: **226 (81.9%)**
- Current/future programme coverage: **218/276 (79.0%)**
- No mapping: **50**
- Publication remains subject to source-policy approval.

## Freshness
| Report | Last generated |
|---|---|
| Playlist audit | **2026-10-10T13:13:33.766831+00:00** |
| EPG coverage | **2026-10-10T13:12:41+00:00** |
| Stream health | **2026-10-10T13:14:24+00:00** |
| Pre-publish gate | **2026-10-10T13:13:33+00:00** |

## Maintenance History
- Records retained: **30**
- Latest entries change: **1152 → 1152**
- Latest health failures: **185 → 173**

Historical records are retained in reports/maintenance-history.json.
