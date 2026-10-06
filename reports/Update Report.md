# Update Report

_Last generated: **2026-10-06 11:10 UTC**_

| Metric | Current |
|---|---:|
| Streams | **1095** |
| Active Channel Identities | **587** |
| Active Primary Streams | **587** |
| Bangladesh | **55** |
| India | **267** |
| Backup Streams | **352** |
| New Channels | **43** |
| New Backup Streams | **60** |
| Local Logos | **99.9%** |
| EPG Programme Coverage | **79.4%** |
| EPG Mapping | **83.5%** |
| Stream Health Tested | **963** |
| Stream Health Failures | **139** |
| Persistent Failures | **120** |
| Near-Duplicate URL Families | **0** |
| Audit Blocking Issues | **29** |
| Pre-Publish Gate | **PASS** |
| Pre-Publish Gate Generated | **2026-10-06T11:10:14+00:00** |

## Quality Controls
- Duplicate stream URLs: **0**
- Metadata conflicts: **0**
- Same-name / different-ID collisions: **0**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **0**
- Logo exceptions: **0**
- Not Playing logo exceptions: **1**
- Malformed EXTINF entries: **0**
- Category block-order issues: **2**
- Alphabetical ordering issues: **26**
- Signed/tokenized URLs: **9**

## Safety & Automation
- Stream health is non-destructive and keeps per-URL failure history.
- Backup streams are never automatically deleted because of health failures.
- Review queues remain user-controlled.
- Pre-publish gate status: **PASS**
- Canonical channel identity index: reports/channel-identity-index.json

## EPG
- Indian channels audited: **267**
- Mapped: **223 (83.5%)**
- Current/future programme coverage: **212/267 (79.4%)**
- No mapping: **44**
- Publication remains subject to source-policy approval.

## Freshness
| Report | Last generated |
|---|---|
| Playlist audit | **2026-10-06T11:09:23.040633+00:00** |
| EPG coverage | **2026-10-06T11:09:21+00:00** |
| Stream health | **2026-10-06T11:10:14+00:00** |
| Pre-publish gate | **2026-10-06T11:10:14+00:00** |

## Maintenance History
- Records retained: **30**
- Latest entries change: **1095 → 1095**
- Latest health failures: **134 → 139**

Historical records are retained in reports/maintenance-history.json.
