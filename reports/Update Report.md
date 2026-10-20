# Update Report

_Last generated: **2026-10-20 13:16 UTC**_

| Metric | Current |
|---|---:|
| Streams | **1088** |
| Active Channel Identities | **639** |
| Active Primary Streams | **639** |
| Bangladesh | **60** |
| India | **289** |
| Backup Streams | **426** |
| Local Logos | **2.8%** |
| EPG Programme Coverage | **6.4%** |
| EPG Mapping | **65.7%** |
| Stream Health Tested | **1094** |
| Stream Health Failures | **62** |
| Persistent Failures | **38** |
| Near-Duplicate URL Families | **0** |
| Audit Blocking Issues | **0** |
| Pre-Publish Gate | **PASS** |
| Pre-Publish Gate Generated | **2026-10-20T13:13:28+00:00** |

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
- Active channel IDs audited: **639**
- Mapped: **420 (65.7%)**
- Current/future programme coverage: **41/639 (6.4%)**
- No mapping: **219**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row**
- Publication remains subject to source-policy approval.

## Freshness
| Report | Last generated |
|---|---|
| Playlist audit | **2026-10-20T13:13:28.254175+00:00** |
| EPG coverage | **2026-10-20T13:16:21+00:00** |
| Stream health | **2026-10-17T10:01:04+00:00** |
| Pre-publish gate | **2026-10-20T13:13:28+00:00** |

## Maintenance History
- Records retained: **30**
- Latest entries change: **1094 → 1094**
- Latest health failures: **41 → 62**

Historical records are retained in reports/maintenance-history.json.
