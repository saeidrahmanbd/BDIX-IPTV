# Update Report

_Last generated: **2026-11-09 07:00 UTC**_

Source playlist SHA-256: **a905c8a79fc9167d61323692f4a7b8df541e7e086f76552bc5632544ac4f00d7**

| Metric | Current |
|---|---:|
| Streams | **996** |
| Active Channel Identities | **580** |
| Active Primary Streams | **580** |
| Bangladesh | **58** |
| India | **284** |
| Backup Stream Entries | **327** |
| IPTV Local Logos | **99.9%** |
| IPTV EPG Programme Coverage | **46%** |
| IPTV EPG Mapping | **61.4%** |
| Stream Health Tested | **996** |
| Stream Health Failures | **159** |
| Persistent Failures | **127** |
| Near-Duplicate URL Families | **2** |
| Audit Blocking Issues | **16** |
| Pre-Publish Gate | **BLOCK** |
| Pre-Publish Gate Generated | **2026-11-09T06:59:53+00:00** |

## Quality Controls 
- Duplicate stream URLs: **0**
- Metadata conflicts (canonical primary scope): **0**
- Same-name / different-ID collisions (canonical primary scope): **0**
- Cross-queue metadata identity variants: **0**
- Cross-queue same-name / different-ID collisions: **2**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **1**
- Logo exceptions: **1**
- Malformed EXTINF entries: **0**
- Category block-order issues: **11**
- Alphabetical ordering issues: **3**
- Signed/tokenized URLs: **8**

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
- EPG IDs audited: **580**
- Mapped: **356 (61.4%)**
- Current/future programme coverage: **268/580 (46.2%)**
- No mapping: **224**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (verified against both current playlist inventories)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-09T06:59:52.892469+00:00** | **CURRENT** |
| EPG coverage / two-playlist inventory | **2026-11-09T06:57:42+00:00** | **CURRENT** |
| Stream health | **2026-11-09T07:00:28+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-09T06:59:53+00:00** | **CURRENT** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **996 → 996**
- Latest health failures: **154 → 159**

Historical records are retained in reports/maintenance-history.json.
