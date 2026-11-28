# Update Report

_Last generated: **2026-11-28 08:49 UTC**_

Source playlist SHA-256: **4107c2a899815b766d255eb543c7acf9b7f538f6e1e9c3ef6070118e22361521**

| Metric | Current |
|---|---:|
| Streams | **1400** |
| Active Channel Identities | **711** |
| Active Primary Streams | **837** |
| Bangladesh | **70** |
| India | **322** |
| Backup Stream Entries | **499** |
| IPTV Local Logos | **STALE** |
| IPTV EPG Programme Coverage | **54%** |
| IPTV EPG Mapping | **60.3%** |
| Stream Health Tested | **STALE** |
| Stream Health Failures | **STALE** |
| Persistent Failures | **STALE** |
| Near-Duplicate URL Families | **STALE / UNKNOWN** |
| Audit findings (review warnings included) | **STALE / UNKNOWN** |
| Pre-Publish Gate | **STALE / UNKNOWN** |
| Pre-Publish Gate Generated | **2026-11-28T05:06:08+00:00** |

## Quality Controls (STALE / UNKNOWN — saved audit values shown for reference)
- Duplicate stream URLs: **STALE / UNKNOWN (last saved: 0)**
- Metadata conflicts (canonical primary scope): **STALE / UNKNOWN (last saved: 0)**
- Same-name / different-ID collisions (canonical primary scope): **STALE / UNKNOWN (last saved: 0)**
- Cross-queue metadata identity variants: **0**
- Cross-queue same-name / different-ID collisions: **17**
- Duplicate primary identities: **STALE / UNKNOWN (last saved: 0)**
- Primary channel-number collisions: **STALE / UNKNOWN (last saved: 0)**
- Primary entries missing channel numbers: **STALE / UNKNOWN (last saved: 0)**
- Logo exceptions: **STALE / UNKNOWN (last saved: 0)**
- Malformed EXTINF entries: **STALE / UNKNOWN (last saved: 0)**
- Category block-order issues: **STALE / UNKNOWN (last saved: 2)**
- Alphabetical ordering issues: **STALE / UNKNOWN (last saved: 0)**
- Signed/tokenized URLs: **STALE / UNKNOWN (last saved: 14)**

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
- EPG IDs audited: **711**
- Mapped: **429 (60.3%)**
- Current/future programme coverage: **381/711 (53.6%)**
- No mapping: **282**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (verified against both current playlist inventories)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-28T05:06:07.660919+00:00** | **STALE** |
| EPG coverage / two-playlist inventory | **2026-11-28T08:49:48+00:00** | **CURRENT** |
| Stream health | **2026-11-28T05:07:05+00:00** | **STALE** |
| Pre-publish gate | **2026-11-28T05:06:08+00:00** | **STALE** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **1197 → 1198**
- Latest health failures: **55 → 99**

Historical records are retained in reports/maintenance-history.json.
