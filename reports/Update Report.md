# Update Report

_Last generated: **2026-10-11 12:24 UTC**_

| Metric | Current |
|---|---:|
| Streams | **1145** |
| Active Channel Identities | **652** |
| Active Primary Streams | **652** |
| Bangladesh | **60** |
| India | **299** |
| Backup Streams | **493** |
| Local Logos | **100.0%** |
| EPG Programme Coverage | **77.9%** |
| EPG Mapping | **81.3%** |
| Stream Health Tested | **1145** |
| Stream Health Failures | **186** |
| Persistent Failures | **160** |
| Near-Duplicate URL Families | **0** |
| Audit Blocking Issues | **0** |
| Pre-Publish Gate | **PASS** |
| Pre-Publish Gate Generated | **2026-10-11T12:24:12+00:00** |

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
- Indian channels audited: **299**
- Mapped: **243 (81.3%)**
- Current/future programme coverage: **233/299 (77.9%)**
- No mapping: **56**
- Publication remains subject to source-policy approval.

## Freshness
| Report | Last generated |
|---|---|
| Playlist audit | **2026-10-11T12:22:36.498927+00:00** |
| EPG coverage | **2026-10-11T12:22:35+00:00** |
| Stream health | **2026-10-11T12:24:12+00:00** |
| Pre-publish gate | **2026-10-11T12:24:12+00:00** |

## Maintenance History
- Records retained: **30**
- Latest entries change: **1145 → 1145**
- Latest health failures: **167 → 186**

Historical records are retained in reports/maintenance-history.json.
