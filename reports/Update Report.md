# Update Report

_Last generated: **2026-11-11 06:35 UTC**_

Source playlist SHA-256: **8ef94f81f3cac966cc88b0eac2b173686e44c385802f6d1a02e6e42227e97ae8**

| Metric | Current |
|---|---:|
| Streams | **1184** |
| Active Channel Identities | **592** |
| Active Primary Streams | **592** |
| Bangladesh | **54** |
| India | **291** |
| Backup Stream Entries | **406** |
| IPTV Local Logos | **100.0%** |
| IPTV EPG Programme Coverage | **52%** |
| IPTV EPG Mapping | **61.1%** |
| Stream Health Tested | **1184** |
| Stream Health Failures | **204** |
| Persistent Failures | **183** |
| Near-Duplicate URL Families | **2** |
| Audit Blocking Issues | **0** |
| Pre-Publish Gate | **PASS** |
| Pre-Publish Gate Generated | **2026-11-11T06:34:09+00:00** |

## Quality Controls 
- Duplicate stream URLs: **0**
- Metadata conflicts (canonical primary scope): **0**
- Same-name / different-ID collisions (canonical primary scope): **0**
- Cross-queue metadata identity variants: **1**
- Cross-queue same-name / different-ID collisions: **1**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **0**
- Logo exceptions: **0**
- Malformed EXTINF entries: **0**
- Category block-order issues: **0**
- Alphabetical ordering issues: **0**
- Signed/tokenized URLs: **19**

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
- EPG IDs audited: **592**
- Mapped: **362 (61.1%)**
- Current/future programme coverage: **309/592 (52.2%)**
- No mapping: **230**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (verified against both current playlist inventories)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-11T06:34:08.839501+00:00** | **CURRENT** |
| EPG coverage / two-playlist inventory | **2026-11-11T03:29:51+00:00** | **CURRENT** |
| Stream health | **2026-11-11T06:34:56+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-11T06:34:09+00:00** | **CURRENT** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **1188 → 1184**
- Latest health failures: **194 → 204**

Historical records are retained in reports/maintenance-history.json.
