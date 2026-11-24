# Update Report

_Last generated: **2026-11-24 01:29 UTC**_

Source playlist SHA-256: **95ca9078eca1ae8371b7c211029a02bfed62a01de35303f09627ec12f3ba8bc7**

| Metric | Current |
|---|---:|
| Streams | **1350** |
| Active Channel Identities | **716** |
| Active Primary Streams | **716** |
| Bangladesh | **69** |
| India | **321** |
| Backup Stream Entries | **410** |
| IPTV Local Logos | **100.0%** |
| IPTV EPG Programme Coverage | **57%** |
| IPTV EPG Mapping | **63.7%** |
| Stream Health Tested | **1350** |
| Stream Health Failures | **250** |
| Persistent Failures | **56** |
| Near-Duplicate URL Families | **1** |
| Audit findings (review warnings included) | **1** |
| Pre-Publish Gate | **PASS** |
| Pre-Publish Gate Generated | **2026-11-24T00:17:34+00:00** |

## Quality Controls 
- Duplicate stream URLs: **0**
- Metadata conflicts (canonical primary scope): **0**
- Same-name / different-ID collisions (canonical primary scope): **0**
- Cross-queue metadata identity variants: **2**
- Cross-queue same-name / different-ID collisions: **19**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **0**
- Logo exceptions: **0**
- Malformed EXTINF entries: **0**
- Category block-order issues: **0**
- Alphabetical ordering issues: **1**
- Signed/tokenized URLs: **11**

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
- EPG IDs audited: **716**
- Mapped: **456 (63.7%)**
- Current/future programme coverage: **407/716 (56.8%)**
- No mapping: **260**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (verified against both current playlist inventories)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-24T00:17:32.978741+00:00** | **CURRENT** |
| EPG coverage / two-playlist inventory | **2026-11-24T01:29:12+00:00** | **CURRENT** |
| Stream health | **2026-11-24T00:18:41+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-24T00:17:34+00:00** | **CURRENT** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **1355 → 1350**
- Latest health failures: **254 → 250**

Historical records are retained in reports/maintenance-history.json.
