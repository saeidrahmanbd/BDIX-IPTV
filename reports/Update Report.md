# Update Report

_Last generated: **2026-10-07 10:52 UTC**_

| Metric | Current |
|---|---:|
| Streams | **1142** |
| Active Channel Identities | **593** |
| Active Primary Streams | **594** |
| Bangladesh | **57** |
| India | **276** |
| Backup Streams | **400** |
| New Channels | **40** |
| New Backup Streams | **49** |
| Local Logos | **99.9%** |
| EPG Programme Coverage | **77.9%** |
| EPG Mapping | **82.2%** |
| Stream Health Tested | **1011** |
| Stream Health Failures | **114** |
| Persistent Failures | **112** |
| Near-Duplicate URL Families | **0** |
| Audit Blocking Issues | **15** |
| Pre-Publish Gate | **PASS** |
| Pre-Publish Gate Generated | **2026-10-07T10:52:30+00:00** |

## Quality Controls
- Duplicate stream URLs: **0**
- Metadata conflicts: **1**
- Same-name / different-ID collisions: **2**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **0**
- Logo exceptions: **1**
- Not Playing logo exceptions: **0**
- Malformed EXTINF entries: **0**
- Category block-order issues: **2**
- Alphabetical ordering issues: **11**
- Signed/tokenized URLs: **9**

## Safety & Automation
- Stream health is non-destructive and keeps per-URL failure history.
- Backup streams are never automatically deleted because of health failures.
- Review queues remain user-controlled.
- Pre-publish gate status: **PASS**
- Canonical channel identity index: reports/channel-identity-index.json

## EPG
- Indian channels audited: **276**
- Mapped: **227 (82.2%)**
- Current/future programme coverage: **215/276 (77.9%)**
- No mapping: **49**
- Publication remains subject to source-policy approval.

## Freshness
| Report | Last generated |
|---|---|
| Playlist audit | **2026-10-07T10:51:41.070260+00:00** |
| EPG coverage | **2026-10-07T10:51:39+00:00** |
| Stream health | **2026-10-07T10:52:30+00:00** |
| Pre-publish gate | **2026-10-07T10:52:30+00:00** |

## Maintenance History
- Records retained: **30**
- Latest entries change: **1101 → 1142**
- Latest health failures: **120 → 114**

Historical records are retained in reports/maintenance-history.json.
