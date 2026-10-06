# Update Report

_Last generated: **2026-10-06 06:09 UTC**_

| Metric | Current |
|---|---:|
| Streams | **1085** |
| Active Channel Identities | **598** |
| Active Primary Streams | **598** |
| Bangladesh | **58** |
| India | **274** |
| Backup Streams | **360** |
| New Review Queue | **103** |
| New Backup Streams | **0** |
| Local Logos | **99.9%** |
| EPG Programme Coverage | **78.8%** |
| EPG Mapping | **83.2%** |
| Stream Health Tested | **982** |
| Stream Health Failures | **130** |
| Persistent Failures | **125** |
| Near-Duplicate URL Families | **0** |
| Audit Blocking Issues | **15** |
| Pre-Publish Gate | **PASS** |
| Pre-Publish Gate Generated | **2026-10-06T06:09:49+00:00** |

## Quality Controls
- Duplicate stream URLs: **0**
- Metadata conflicts: **0**
- Same-name / different-ID collisions: **0**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **0**
- Logo exceptions: **1**
- Not Playing logo exceptions: **0**
- Malformed EXTINF entries: **0**
- Category block-order issues: **0**
- Alphabetical ordering issues: **14**
- Signed/tokenized URLs: **9**

## Safety & Automation
- Stream health is non-destructive and keeps per-URL failure history.
- Backup streams are never automatically deleted because of health failures.
- Review queues remain user-controlled.
- Pre-publish gate status: **PASS**
- Canonical channel identity index: reports/channel-identity-index.json

## EPG
- Indian channels audited: **274**
- Mapped: **228 (83.2%)**
- Current/future programme coverage: **216/274 (78.8%)**
- No mapping: **46**
- Publication remains subject to source-policy approval.

## Freshness
| Report | Last generated |
|---|---|
| Playlist audit | **2026-10-06T06:09:01.090790+00:00** |
| EPG coverage | **2026-10-06T06:08:59+00:00** |
| Stream health | **2026-10-06T06:09:49+00:00** |
| Pre-publish gate | **2026-10-06T06:09:49+00:00** |

## Maintenance History
- Records retained: **30**
- Latest entries change: **995 → 1085**
- Latest health failures: **152 → 130**

Historical records are retained in reports/maintenance-history.json.
