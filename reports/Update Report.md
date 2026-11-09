# Update Report

_Last generated: **2026-11-09 19:14 UTC**_

Source playlist SHA-256: **fef2a109e2349dbd620cb09d4d8f529d164723c199fbdea3fff4527e4912b1c7**

| Metric | Current |
|---|---:|
| Streams | **1068** |
| Active Channel Identities | **599** |
| Active Primary Streams | **599** |
| Bangladesh | **49** |
| India | **301** |
| Backup Stream Entries | **328** |
| IPTV Local Logos | **100.0%** |
| IPTV EPG Programme Coverage | **53%** |
| IPTV EPG Mapping | **61.0%** |
| Stream Health Tested | **1068** |
| Stream Health Failures | **187** |
| Persistent Failures | **187** |
| Near-Duplicate URL Families | **2** |
| Audit Blocking Issues | **0** |
| Pre-Publish Gate | **BLOCK** |
| Pre-Publish Gate Generated | **2026-11-09T18:43:14+00:00** |

## Quality Controls 
- Duplicate stream URLs: **0**
- Metadata conflicts (canonical primary scope): **0**
- Same-name / different-ID collisions (canonical primary scope): **0**
- Cross-queue metadata identity variants: **0**
- Cross-queue same-name / different-ID collisions: **2**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **0**
- Logo exceptions: **0**
- Malformed EXTINF entries: **0**
- Category block-order issues: **0**
- Alphabetical ordering issues: **0**
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
- Mapped: **364 (61.0%)**
- Current/future programme coverage: **315/597 (52.8%)**
- No mapping: **233**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (verified against both current playlist inventories)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-09T18:43:13.872964+00:00** | **CURRENT** |
| EPG coverage / two-playlist inventory | **2026-11-09T19:14:47+00:00** | **CURRENT** |
| Stream health | **2026-11-09T18:43:56+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-09T18:43:14+00:00** | **CURRENT** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **1068 → 1068**
- Latest health failures: **226 → 187**

Historical records are retained in reports/maintenance-history.json.
