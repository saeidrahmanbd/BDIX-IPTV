# Update Report

_Last generated: **2026-11-14 16:50 UTC**_

Source playlist SHA-256: **51bbb54fb8cb3b0e88dde76f1867e227a4e12489d0a86c3e2d74ad0bb410d253**

| Metric | Current |
|---|---:|
| Streams | **1284** |
| Active Channel Identities | **646** |
| Active Primary Streams | **646** |
| Bangladesh | **64** |
| India | **293** |
| Backup Stream Entries | **424** |
| IPTV Local Logos | **100.0%** |
| IPTV EPG Programme Coverage | **PENDING** |
| IPTV EPG Mapping | **PENDING** |
| Stream Health Tested | **1284** |
| Stream Health Failures | **230** |
| Persistent Failures | **179** |
| Near-Duplicate URL Families | **1** |
| Audit findings (review warnings included) | **111** |
| Pre-Publish Gate | **PASS** |
| Pre-Publish Gate Generated | **2026-11-14T16:49:35+00:00** |

## Quality Controls 
- Duplicate stream URLs: **0**
- Metadata conflicts (canonical primary scope): **0**
- Same-name / different-ID collisions (canonical primary scope): **1**
- Cross-queue metadata identity variants: **1**
- Cross-queue same-name / different-ID collisions: **15**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **13**
- Logo exceptions: **0**
- Malformed EXTINF entries: **0**
- Category block-order issues: **32**
- Alphabetical ordering issues: **66**
- Signed/tokenized URLs: **18**

## Safety & Automation
- Stream health is non-destructive and keeps per-URL failure history.
- Backup streams are never automatically deleted because of health failures.
- `Backup` stores alternate streams; `Review`, `New Channels`, and `New Backups` are review-only queues and are excluded from Xtream.
- Pre-publish gate status: **PASS**
- Canonical channel identity index: reports/channel-identity-index.json

## Counting Scope
- **Active Channel Identities / Active Primary Streams** count only canonical playlist groups.
- `Backup`, `Review`, `New Channels`, and `New Backups` are excluded from the active-primary count.
- EPG identity/programme coverage is reported only when the published XMLTV is valid, current, and its freshness report is PASS.
- **Backup Stream Entries** count playlist rows, not independent CDN/origin infrastructures. Backup independence is reviewed separately.

## EPG
- EPG IDs audited: **PENDING — guide not current**
- Mapped: **PENDING — no current validated guide**
- Current/future programme coverage: **PENDING — no current validated guide**
- No mapping: **PENDING — guide not current**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (awaiting a valid, fresh published guide)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-14T16:49:34.209356+00:00** | **CURRENT** |
| EPG coverage / two-playlist inventory | **2026-11-14T14:32:42+00:00** | **PENDING — guide missing or freshness not PASS** |
| Stream health | **2026-11-14T16:50:38+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-14T16:49:35+00:00** | **CURRENT** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **1284 → 1284**
- Latest health failures: **193 → 230**

Historical records are retained in reports/maintenance-history.json.
