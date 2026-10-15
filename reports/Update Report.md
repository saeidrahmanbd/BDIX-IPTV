# Update Report

_Last generated: **2026-10-15 07:19 UTC**_

| Metric | Current |
|---|---:|
| Streams | **1043** |
| Active Channel Identities | **635** |
| Active Primary Streams | **635** |
| Bangladesh | **59** |
| India | **285** |
| Backup Streams | **408** |
| Local Logos | **100.0%** |
| EPG Programme Coverage | **60.3%** |
| EPG Mapping | **63.9%** |
| Stream Health Tested | **1043** |
| Stream Health Failures | **20** |
| Persistent Failures | **9** |
| Near-Duplicate URL Families | **0** |
| Audit Blocking Issues | **0** |
| Pre-Publish Gate | **PASS** |
| Pre-Publish Gate Generated | **2026-10-15T07:18:53+00:00** |

## Quality Controls
- Duplicate stream URLs: **0**
- Metadata conflicts: **0**
- Same-name / different-ID collisions: **80**
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
- Active channel IDs audited: **690**
- Mapped: **441 (63.9%)**
- Current/future programme coverage: **416/690 (60.3%)**
- No mapping: **249**
- Publication remains subject to source-policy approval.

## Freshness
| Report | Last generated |
|---|---|
| Playlist audit | **2026-10-15T07:18:52.929612+00:00** |
| EPG coverage | **2026-10-15T07:18:23+00:00** |
| Stream health | **2026-10-15T07:19:19+00:00** |
| Pre-publish gate | **2026-10-15T07:18:53+00:00** |

## Maintenance History
- Records retained: **30**
- Latest entries change: **1043 → 1043**
- Latest health failures: **16 → 20**

Historical records are retained in reports/maintenance-history.json.
