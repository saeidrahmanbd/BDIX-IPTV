# Update Report

_Last generated: **2026-11-08 16:58 UTC**_

Source playlist SHA-256: **dee4c0905162325bb433379bae254831ad1834640807c7670b213f343caec9f3**

| Metric | Current |
|---|---:|
| Streams | **999** |
| Active Channel Identities | **597** |
| Active Primary Streams | **597** |
| Bangladesh | **58** |
| India | **291** |
| Backup Stream Entries | **324** |
| IPTV Local Logos | **100.0%** |
| IPTV EPG Programme Coverage | **51%** |
| IPTV EPG Mapping | **61.3%** |
| Stream Health Tested | **999** |
| Stream Health Failures | **136** |
| Persistent Failures | **52** |
| Near-Duplicate URL Families | **2** |
| Audit Blocking Issues | **18** |
| Pre-Publish Gate | **BLOCK** |
| Pre-Publish Gate Generated | **2026-11-08T16:57:00+00:00** |

## Quality Controls 
- Duplicate stream URLs: **0**
- Metadata conflicts (canonical primary scope): **0**
- Same-name / different-ID collisions (canonical primary scope): **0**
- Cross-queue metadata identity variants: **0**
- Cross-queue same-name / different-ID collisions: **3**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **1**
- Logo exceptions: **0**
- Malformed EXTINF entries: **0**
- Category block-order issues: **14**
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
- EPG IDs audited: **597**
- Mapped: **366 (61.3%)**
- Current/future programme coverage: **305/597 (51.1%)**
- No mapping: **231**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (verified against both current playlist inventories)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-08T16:57:00.344386+00:00** | **CURRENT** |
| EPG coverage / two-playlist inventory | **2026-11-08T16:55:30+00:00** | **CURRENT** |
| Stream health | **2026-11-08T16:57:32+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-08T16:57:00+00:00** | **CURRENT** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **934 → 999**
- Latest health failures: **60 → 136**

Historical records are retained in reports/maintenance-history.json.
