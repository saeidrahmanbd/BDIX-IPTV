# Update Report

_Last generated: **2026-11-24 10:06 UTC**_

Source playlist SHA-256: **ff15c8ceffaa71c72e6b9f2c387ff941dc227454cb482bb4a2943966640ec13c**

| Metric | Current |
|---|---:|
| Streams | **1339** |
| Active Channel Identities | **695** |
| Active Primary Streams | **704** |
| Bangladesh | **70** |
| India | **316** |
| Backup Stream Entries | **396** |
| IPTV Local Logos | **100.0%** |
| IPTV EPG Programme Coverage | **56%** |
| IPTV EPG Mapping | **62.3%** |
| Stream Health Tested | **1339** |
| Stream Health Failures | **271** |
| Persistent Failures | **56** |
| Near-Duplicate URL Families | **1** |
| Audit findings (review warnings included) | **35** |
| Pre-Publish Gate | **BLOCK** |
| Pre-Publish Gate Generated | **2026-11-24T07:08:52+00:00** |

## Quality Controls 
- Duplicate stream URLs: **0**
- Metadata conflicts (canonical primary scope): **0**
- Same-name / different-ID collisions (canonical primary scope): **0**
- Cross-queue metadata identity variants: **1**
- Cross-queue same-name / different-ID collisions: **15**
- Duplicate primary identities: **4**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **9**
- Logo exceptions: **0**
- Malformed EXTINF entries: **0**
- Category block-order issues: **7**
- Alphabetical ordering issues: **15**
- Signed/tokenized URLs: **14**

## Safety & Automation
- Stream health is non-destructive and keeps per-URL failure history.
- Backup streams are never automatically deleted because of health failures.
- `Backup` stores alternate streams; `Review`, `New Channels`, and `New Backups` are review-only queues and are excluded from Xtream.
- Pre-publish gate status: **BLOCK**
- Canonical channel identity index: reports/channel-identity-index.json

## Counting Scope
- **Active Channel Identities / Active Primary Streams** count only canonical playlist groups.
- `Backup`, `Review`, `New Channels`, and `New Backups` are excluded from the active-primary count.
- EPG identity/programme coverage is reported only when the published XMLTV is valid, current, and its freshness report is PASS.
- **Backup Stream Entries** count playlist rows, not independent CDN/origin infrastructures. Backup independence is reviewed separately.

## EPG
- EPG IDs audited: **695**
- Mapped: **433 (62.3%)**
- Current/future programme coverage: **387/695 (55.7%)**
- No mapping: **262**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (verified against both current playlist inventories)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-24T07:08:51.619307+00:00** | **CURRENT** |
| EPG coverage / two-playlist inventory | **2026-11-24T10:06:29+00:00** | **CURRENT** |
| Stream health | **2026-11-24T07:09:44+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-24T07:08:52+00:00** | **CURRENT** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **1350 → 1339**
- Latest health failures: **250 → 271**

Historical records are retained in reports/maintenance-history.json.
