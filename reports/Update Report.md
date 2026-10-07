# Update Report

_Last generated: **2026-10-07 03:52 UTC**_

| Metric | Current |
|---|---:|
| Streams | **1101** |
| Active Channel Identities | **588** |
| Active Primary Streams | **589** |
| Bangladesh | **55** |
| India | **273** |
| Backup Streams | **329** |
| New Channels | **40** |
| New Backup Streams | **49** |
| Local Logos | **100.0%** |
| EPG Programme Coverage | **78.4%** |
| EPG Mapping | **82.8%** |
| Stream Health Tested | **934** |
| Stream Health Failures | **117** |
| Persistent Failures | **113** |
| Near-Duplicate URL Families | **0** |
| Audit Blocking Issues | **17** |
| Pre-Publish Gate | **PASS** |
| Pre-Publish Gate Generated | **2026-10-07T03:52:36+00:00** |

## Quality Controls
- Duplicate stream URLs: **0**
- Metadata conflicts: **1**
- Same-name / different-ID collisions: **0**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **0**
- Logo exceptions: **0**
- Not Playing logo exceptions: **0**
- Malformed EXTINF entries: **0**
- Category block-order issues: **2**
- Alphabetical ordering issues: **14**
- Signed/tokenized URLs: **9**

## Safety & Automation
- Stream health is non-destructive and keeps per-URL failure history.
- Backup streams are never automatically deleted because of health failures.
- Review queues remain user-controlled.
- Pre-publish gate status: **PASS**
- Canonical channel identity index: reports/channel-identity-index.json

## EPG
- Indian channels audited: **273**
- Mapped: **226 (82.8%)**
- Current/future programme coverage: **214/273 (78.4%)**
- No mapping: **47**
- Publication remains subject to source-policy approval.

## Freshness
| Report | Last generated |
|---|---|
| Playlist audit | **2026-10-07T03:51:48.609092+00:00** |
| EPG coverage | **2026-10-07T03:51:47+00:00** |
| Stream health | **2026-10-07T03:52:36+00:00** |
| Pre-publish gate | **2026-10-07T03:52:36+00:00** |

## Maintenance History
- Records retained: **30**
- Latest entries change: **1104 → 1101**
- Latest health failures: **137 → 117**

Historical records are retained in reports/maintenance-history.json.
