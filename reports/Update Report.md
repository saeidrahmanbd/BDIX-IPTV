# Update Report

_Last generated: **2026-11-12 05:42 UTC**_

Source playlist SHA-256: **ebabf8e5d80fa4c1524209e86de1022f0c7195719266f81eccbad13b250bca95**

| Metric | Current |
|---|---:|
| Streams | **1331** |
| Active Channel Identities | **685** |
| Active Primary Streams | **685** |
| Bangladesh | **67** |
| India | **301** |
| Backup Stream Entries | **463** |
| IPTV Local Logos | **99.5%** |
| IPTV EPG Programme Coverage | **52%** |
| IPTV EPG Mapping | **59.4%** |
| Stream Health Tested | **1331** |
| Stream Health Failures | **185** |
| Persistent Failures | **175** |
| Near-Duplicate URL Families | **2** |
| Audit Blocking Issues | **19** |
| Pre-Publish Gate | **BLOCK** |
| Pre-Publish Gate Generated | **2026-11-12T05:40:29+00:00** |

## Quality Controls 
- Duplicate stream URLs: **0**
- Metadata conflicts (canonical primary scope): **0**
- Same-name / different-ID collisions (canonical primary scope): **2**
- Cross-queue metadata identity variants: **0**
- Cross-queue same-name / different-ID collisions: **16**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **0**
- Logo exceptions: **7**
- Malformed EXTINF entries: **0**
- Category block-order issues: **0**
- Alphabetical ordering issues: **12**
- Signed/tokenized URLs: **23**

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
- EPG IDs audited: **685**
- Mapped: **407 (59.4%)**
- Current/future programme coverage: **359/685 (52.4%)**
- No mapping: **278**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (verified against both current playlist inventories)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-12T05:40:28.612813+00:00** | **CURRENT** |
| EPG coverage / two-playlist inventory | **2026-11-12T05:23:28+00:00** | **CURRENT** |
| Stream health | **2026-11-12T05:41:10+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-12T05:40:29+00:00** | **CURRENT** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **1331 → 1331**
- Latest health failures: **185 → 185**

Historical records are retained in reports/maintenance-history.json.
