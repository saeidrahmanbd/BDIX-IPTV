# Update Report

_Last generated: **2026-10-09 14:39 UTC**_

| Metric | Current |
|---|---:|
| Streams | **1151** |
| Active Channel Identities | **594** |
| Active Primary Streams | **594** |
| Bangladesh | **57** |
| India | **276** |
| Backup Streams | **398** |
| New Channels | **40** |
| New Backup Streams | **50** |
| Local Logos | **99.9%** |
| EPG Programme Coverage | **77.9%** |
| EPG Mapping | **81.9%** |
| Stream Health Tested | **1008** |
| Stream Health Failures | **165** |
| Persistent Failures | **127** |
| Near-Duplicate URL Families | **0** |
| Audit Blocking Issues | **16** |
| Pre-Publish Gate | **PASS** |
| Pre-Publish Gate Generated | **2026-10-09T14:39:43+00:00** |

## Quality Controls
- Duplicate stream URLs: **0**
- Metadata conflicts: **0**
- Same-name / different-ID collisions: **1**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **0**
- Logo exceptions: **1**
- Not Playing logo exceptions: **0**
- Malformed EXTINF entries: **0**
- Category block-order issues: **2**
- Alphabetical ordering issues: **13**
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
- Current/future programme coverage: **215/276 (77.9%)**
- No mapping: **50**
- Publication remains subject to source-policy approval.

## Freshness
| Report | Last generated |
|---|---|
| Playlist audit | **2026-10-09T14:38:49.663981+00:00** |
| EPG coverage | **2026-10-09T14:38:49+00:00** |
| Stream health | **2026-10-09T14:39:43+00:00** |
| Pre-publish gate | **2026-10-09T14:39:43+00:00** |

## Maintenance History
- Records retained: **30**
- Latest entries change: **1151 → 1151**
- Latest health failures: **168 → 165**

Historical records are retained in reports/maintenance-history.json.
