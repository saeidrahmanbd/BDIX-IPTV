# Update Report

_Last generated: **2026-10-11 04:23 UTC**_

| Metric | Current |
|---|---:|
| Streams | **1136** |
| Active Channel Identities | **617** |
| Active Primary Streams | **617** |
| Bangladesh | **59** |
| India | **283** |
| Backup Streams | **450** |
| New Channels | **0** |
| New Backup Streams | **0** |
| Local Logos | **98.4%** |
| EPG Programme Coverage | **78.4%** |
| EPG Mapping | **81.6%** |
| Stream Health Tested | **1083** |
| Stream Health Failures | **156** |
| Persistent Failures | **141** |
| Near-Duplicate URL Families | **0** |
| Audit Blocking Issues | **44** |
| Pre-Publish Gate | **BLOCK** |
| Pre-Publish Gate Generated | **2026-10-11T04:22:56+00:00** |

## Quality Controls
- Duplicate stream URLs: **0**
- Metadata conflicts: **0**
- Same-name / different-ID collisions: **0**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **23**
- Logo exceptions: **17**
- Not Playing logo exceptions: **1**
- Malformed EXTINF entries: **0**
- Category block-order issues: **0**
- Alphabetical ordering issues: **3**
- Signed/tokenized URLs: **9**

## Safety & Automation
- Stream health is non-destructive and keeps per-URL failure history.
- Backup streams are never automatically deleted because of health failures.
- Review queues remain user-controlled.
- Pre-publish gate status: **BLOCK**
- Canonical channel identity index: reports/channel-identity-index.json

## EPG
- Indian channels audited: **283**
- Mapped: **231 (81.6%)**
- Current/future programme coverage: **222/283 (78.4%)**
- No mapping: **52**
- Publication remains subject to source-policy approval.

## Freshness
| Report | Last generated |
|---|---|
| Playlist audit | **2026-10-11T04:22:56.314469+00:00** |
| EPG coverage | **2026-10-11T04:22:02+00:00** |
| Stream health | **2026-10-11T04:23:47+00:00** |
| Pre-publish gate | **2026-10-11T04:22:56+00:00** |

## Maintenance History
- Records retained: **30**
- Latest entries change: **1152 → 1136**
- Latest health failures: **173 → 156**

Historical records are retained in reports/maintenance-history.json.
