# Update Report

_Last generated: **2026-11-28 17:56 UTC**_

Source playlist SHA-256: **25206445454790f8cf1e4f60acef3d030b563cba93de4c0d68c3603eee1a077c**

| Metric | Current |
|---|---:|
| Streams | **1373** |
| Active Channel Identities | **780** |
| Active Primary Streams | **824** |
| Bangladesh | **67** |
| India | **320** |
| Backup Stream Entries | **489** |
| IPTV Local Logos | **99.5%** |
| IPTV EPG Programme Coverage | **PENDING** |
| IPTV EPG Mapping | **PENDING** |
| Stream Health Tested | **1373** |
| Stream Health Failures | **67** |
| Persistent Failures | **0** |
| Near-Duplicate URL Families | **3** |
| Audit findings (review warnings included) | **33** |
| Pre-Publish Gate | **BLOCK** |
| Pre-Publish Gate Generated | **2026-11-28T17:55:30+00:00** |

## Quality Controls 
- Duplicate stream URLs: **0**
- Metadata conflicts (canonical primary scope): **2**
- Same-name / different-ID collisions (canonical primary scope): **3**
- Cross-queue metadata identity variants: **2**
- Cross-queue same-name / different-ID collisions: **17**
- Duplicate primary identities: **8**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **0**
- Logo exceptions: **7**
- Malformed EXTINF entries: **0**
- Category block-order issues: **3**
- Alphabetical ordering issues: **13**
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
- EPG IDs audited: **PENDING — guide not current**
- Mapped: **PENDING — no current validated guide**
- Current/future programme coverage: **PENDING — no current validated guide**
- No mapping: **PENDING — guide not current**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (awaiting a valid, fresh published guide)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-28T17:55:29.454696+00:00** | **CURRENT** |
| EPG coverage / two-playlist inventory | **2026-11-28T10:57:01+00:00** | **PENDING — guide missing or freshness not PASS** |
| Stream health | **2026-11-28T17:56:11+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-28T17:55:30+00:00** | **CURRENT** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **1373 → 1373**
- Latest health failures: **66 → 67**

Historical records are retained in reports/maintenance-history.json.
