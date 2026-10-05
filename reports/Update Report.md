# Update Report

_Last generated: **2026-10-05 03:54 UTC**_

| Metric | Current |
|---|---:|
| Streams | **978** |
| Active Channel Identities | **598** |
| Active Primary Streams | **598** |
| Bangladesh | **58** |
| India | **274** |
| Backup Streams | **356** |
| New Channels | **0** |
| New Backup Streams | **0** |
| Local Logos | **99.9%** |
| EPG Programme Coverage | **78.5%** |
| EPG Mapping | **83.2%** |
| Stream Health Tested | **978** |
| Stream Health Failures | **121** |
| Persistent Failures | **113** |
| Near-Duplicate URL Families | **0** |
| Audit Blocking Issues | **6** |
| Pre-Publish Gate | **PASS** |
| Pre-Publish Gate Generated | **2026-10-05T03:54:21+00:00** |

## Quality Controls
- Duplicate stream URLs: **0**
- Metadata conflicts: **0**
- Same-name / different-ID collisions: **0**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **0**
- Logo exceptions: **1**
- Not Playing logo exceptions: **0**
- Malformed EXTINF entries: **0**
- Category block-order issues: **0**
- Alphabetical ordering issues: **1**
- Signed/tokenized URLs: **9**

## Safety & Automation
- Stream health is non-destructive and keeps per-URL failure history.
- Backup streams are never automatically deleted because of health failures.
- Review queues remain user-controlled.
- Pre-publish gate status: **PASS**
- Canonical channel identity index: reports/channel-identity-index.json

## EPG
- Indian channels audited: **274**
- Mapped: **228 (83.2%)**
- Current/future programme coverage: **215/274 (78.5%)**
- No mapping: **46**
- Publication remains subject to source-policy approval.

## Freshness
| Report | Last generated |
|---|---|
| Playlist audit | **2026-10-05T03:53:35.104522+00:00** |
| EPG coverage | **2026-10-05T03:53:32+00:00** |
| Stream health | **2026-10-05T03:54:21+00:00** |
| Pre-publish gate | **2026-10-05T03:54:21+00:00** |

## Maintenance History
- Records retained: **30**
- Latest entries change: **1021 → 978**
- Latest health failures: **125 → 121**

Historical records are retained in reports/maintenance-history.json.
