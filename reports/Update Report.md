# Update Report

_Last generated: **2026-11-28 10:58 UTC**_

Source playlist SHA-256: **1430770e8c02dd64d1d03bab2f1809e4251e771e5737759c2ec945d0525e162c**

| Metric | Current |
|---|---:|
| Streams | **1373** |
| Active Channel Identities | **702** |
| Active Primary Streams | **824** |
| Bangladesh | **67** |
| India | **320** |
| Backup Stream Entries | **489** |
| IPTV Local Logos | **99.0%** |
| IPTV EPG Programme Coverage | **54%** |
| IPTV EPG Mapping | **60.5%** |
| Stream Health Tested | **1373** |
| Stream Health Failures | **68** |
| Persistent Failures | **0** |
| Near-Duplicate URL Families | **3** |
| Audit findings (review warnings included) | **154** |
| Pre-Publish Gate | **PASS** |
| Pre-Publish Gate Generated | **2026-11-28T10:58:07+00:00** |

## Quality Controls 
- Duplicate stream URLs: **0**
- Metadata conflicts (canonical primary scope): **0**
- Same-name / different-ID collisions (canonical primary scope): **32**
- Cross-queue metadata identity variants: **0**
- Cross-queue same-name / different-ID collisions: **21**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **125**
- Logo exceptions: **14**
- Malformed EXTINF entries: **0**
- Category block-order issues: **3**
- Alphabetical ordering issues: **12**
- Signed/tokenized URLs: **14**

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
- EPG IDs audited: **702**
- Mapped: **425 (60.5%)**
- Current/future programme coverage: **379/702 (54.0%)**
- No mapping: **277**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (verified against both current playlist inventories)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-28T10:58:06.302183+00:00** | **CURRENT** |
| EPG coverage / two-playlist inventory | **2026-11-28T10:57:01+00:00** | **CURRENT** |
| Stream health | **2026-11-28T10:58:49+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-28T10:58:07+00:00** | **CURRENT** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **1373 → 1373**
- Latest health failures: **69 → 68**

Historical records are retained in reports/maintenance-history.json.
