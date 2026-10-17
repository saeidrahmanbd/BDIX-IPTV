# Update Report

_Last generated: **2026-10-17 07:32 UTC**_

| Metric | Current |
|---|---:|
| Streams | **1094** |
| Active Channel Identities | **667** |
| Active Primary Streams | **667** |
| Bangladesh | **60** |
| India | **287** |
| Backup Streams | **427** |
| Local Logos | **100.0%** |
| EPG Programme Coverage | **61.4%** |
| EPG Mapping | **65.2%** |
| Stream Health Tested | **1094** |
| Stream Health Failures | **61** |
| Persistent Failures | **26** |
| Near-Duplicate URL Families | **0** |
| Audit Blocking Issues | **0** |
| Pre-Publish Gate | **PASS** |
| Pre-Publish Gate Generated | **2026-10-17T07:32:21+00:00** |

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
- Signed/tokenized URLs: **11**

## Safety & Automation
- Stream health is non-destructive and keeps per-URL failure history.
- Backup streams are never automatically deleted because of health failures.
- Discovery queues are retired; only the approved canonical playlist categories are maintained.
- Pre-publish gate status: **PASS**
- Canonical channel identity index: reports/channel-identity-index.json

## EPG
- Active channel IDs audited: **721**
- Mapped: **470 (65.2%)**
- Current/future programme coverage: **443/721 (61.4%)**
- No mapping: **251**
- Publication remains subject to source-policy approval.

## Freshness
| Report | Last generated |
|---|---|
| Playlist audit | **2026-10-17T07:31:39.797191+00:00** |
| EPG coverage | **2026-10-17T07:31:38+00:00** |
| Stream health | **2026-10-17T07:32:21+00:00** |
| Pre-publish gate | **2026-10-17T07:32:21+00:00** |

## Maintenance History
- Records retained: **30**
- Latest entries change: **1060 → 1094**
- Latest health failures: **31 → 61**

Historical records are retained in reports/maintenance-history.json.
