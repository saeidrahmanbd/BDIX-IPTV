# Update Report

_Last generated: **2026-11-23 01:31 UTC**_

Source playlist SHA-256: **edc2e1edbb195131dceb66cfedc7a3d7d3fcf9901d4a7c41066b9f052a4e3e0b**

| Metric | Current |
|---|---:|
| Streams | **1346** |
| Active Channel Identities | **716** |
| Active Primary Streams | **716** |
| Bangladesh | **69** |
| India | **322** |
| Backup Stream Entries | **410** |
| IPTV Local Logos | **100.0%** |
| IPTV EPG Programme Coverage | **56%** |
| IPTV EPG Mapping | **63.8%** |
| Stream Health Tested | **1346** |
| Stream Health Failures | **262** |
| Persistent Failures | **55** |
| Near-Duplicate URL Families | **1** |
| Audit findings (review warnings included) | **8** |
| Pre-Publish Gate | **PASS** |
| Pre-Publish Gate Generated | **2026-11-23T01:29:43+00:00** |

## Quality Controls 
- Duplicate stream URLs: **0**
- Metadata conflicts (canonical primary scope): **0**
- Same-name / different-ID collisions (canonical primary scope): **0**
- Cross-queue metadata identity variants: **1**
- Cross-queue same-name / different-ID collisions: **18**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **8**
- Logo exceptions: **0**
- Malformed EXTINF entries: **0**
- Category block-order issues: **0**
- Alphabetical ordering issues: **0**
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
- Mapped: **457 (63.8%)**
- Current/future programme coverage: **403/716 (56.3%)**
- No mapping: **259**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (verified against both current playlist inventories)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-23T01:29:42.804826+00:00** | **CURRENT** |
| EPG coverage / two-playlist inventory | **2026-11-23T01:28:31+00:00** | **CURRENT** |
| Stream health | **2026-11-23T01:30:53+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-23T01:29:43+00:00** | **CURRENT** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **1346 → 1346**
- Latest health failures: **253 → 262**

Historical records are retained in reports/maintenance-history.json.
