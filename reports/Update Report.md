# Update Report

_Last generated: **2026-10-12 08:05 UTC**_

| Metric | Current |
|---|---:|
| Streams | **1013** |
| Active Channel Identities | **624** |
| Active Primary Streams | **625** |
| Bangladesh | **59** |
| India | **281** |
| Backup Streams | **388** |
| Local Logos | **100.0%** |
| EPG Programme Coverage | **77.2%** |
| EPG Mapping | **80.6%** |
| Stream Health Tested | **1013** |
| Stream Health Failures | **163** |
| Persistent Failures | **130** |
| Near-Duplicate URL Families | **0** |
| Audit Blocking Issues | **10** |
| Pre-Publish Gate | **BLOCK** |
| Pre-Publish Gate Generated | **2026-10-12T08:03:34+00:00** |

## Quality Controls
- Duplicate stream URLs: **0**
- Metadata conflicts: **0**
- Same-name / different-ID collisions: **0**
- Duplicate primary identities: **1**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **4**
- Logo exceptions: **0**
- Malformed EXTINF entries: **0**
- Category block-order issues: **0**
- Alphabetical ordering issues: **5**
- Signed/tokenized URLs: **9**

## Safety & Automation
- Stream health is non-destructive and keeps per-URL failure history.
- Backup streams are never automatically deleted because of health failures.
- Discovery queues are retired; only the approved canonical playlist categories are maintained.
- Pre-publish gate status: **BLOCK**
- Canonical channel identity index: reports/channel-identity-index.json

## EPG
- Indian channels audited: **324**
- Mapped: **261 (80.6%)**
- Current/future programme coverage: **250/324 (77.2%)**
- No mapping: **63**
- Publication remains subject to source-policy approval.

## Freshness
| Report | Last generated |
|---|---|
| Playlist audit | **2026-10-12T08:03:34.699576+00:00** |
| EPG coverage | **2026-10-12T08:02:00+00:00** |
| Stream health | **2026-10-12T08:05:06+00:00** |
| Pre-publish gate | **2026-10-12T08:03:34+00:00** |

## Maintenance History
- Records retained: **30**
- Latest entries change: **1013 → 1013**
- Latest health failures: **134 → 163**

Historical records are retained in reports/maintenance-history.json.
