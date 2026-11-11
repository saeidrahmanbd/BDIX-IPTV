# Update Report

_Last generated: **2026-11-11 03:29 UTC**_

Source playlist SHA-256: **8ef94f81f3cac966cc88b0eac2b173686e44c385802f6d1a02e6e42227e97ae8**

| Metric | Current |
|---|---:|
| Streams | **1184** |
| Active Channel Identities | **592** |
| Active Primary Streams | **592** |
| Bangladesh | **54** |
| India | **291** |
| Backup Stream Entries | **406** |
| IPTV Local Logos | **STALE** |
| IPTV EPG Programme Coverage | **52%** |
| IPTV EPG Mapping | **61.1%** |
| Stream Health Tested | **STALE** |
| Stream Health Failures | **STALE** |
| Persistent Failures | **STALE** |
| Near-Duplicate URL Families | **STALE / UNKNOWN** |
| Audit Blocking Issues | **STALE / UNKNOWN** |
| Pre-Publish Gate | **STALE / UNKNOWN** |
| Pre-Publish Gate Generated | **2026-11-10T15:12:04+00:00** |

## Quality Controls (STALE / UNKNOWN — saved audit values shown for reference)
- Duplicate stream URLs: **STALE / UNKNOWN (last saved: 0)**
- Metadata conflicts (canonical primary scope): **STALE / UNKNOWN (last saved: 0)**
- Same-name / different-ID collisions (canonical primary scope): **STALE / UNKNOWN (last saved: 0)**
- Cross-queue metadata identity variants: **1**
- Cross-queue same-name / different-ID collisions: **1**
- Duplicate primary identities: **STALE / UNKNOWN (last saved: 0)**
- Primary channel-number collisions: **STALE / UNKNOWN (last saved: 0)**
- Primary entries missing channel numbers: **STALE / UNKNOWN (last saved: 4)**
- Logo exceptions: **STALE / UNKNOWN (last saved: 0)**
- Malformed EXTINF entries: **STALE / UNKNOWN (last saved: 0)**
- Category block-order issues: **STALE / UNKNOWN (last saved: 0)**
- Alphabetical ordering issues: **STALE / UNKNOWN (last saved: 2)**
- Signed/tokenized URLs: **STALE / UNKNOWN (last saved: 19)**

## Safety & Automation
- Stream health is non-destructive and keeps per-URL failure history.
- Backup streams are never automatically deleted because of health failures.
- `Backup` stores alternate streams; `Review`, `New Channels`, and `New Backups` are review-only queues and are excluded from Xtream.
- Pre-publish gate status: **STALE / UNKNOWN**
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
| Playlist audit | **2026-11-10T15:12:03.962107+00:00** | **STALE** |
| EPG coverage / two-playlist inventory | **2026-11-11T03:29:51+00:00** | **CURRENT** |
| Stream health | **2026-11-10T15:12:51+00:00** | **STALE** |
| Pre-publish gate | **2026-11-10T15:12:04+00:00** | **STALE** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **1188 → 1188**
- Latest health failures: **238 → 194**

Historical records are retained in reports/maintenance-history.json.
