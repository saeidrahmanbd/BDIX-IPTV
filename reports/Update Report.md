# Update Report

_Last generated: **2026-11-15 08:14 UTC**_

Source playlist SHA-256: **80cee209bddaaed878591d9fb195a8619ba2663a375dd834edd7e8c70c2c1518**

| Metric | Current |
|---|---:|
| Streams | **1276** |
| Active Channel Identities | **645** |
| Active Primary Streams | **645** |
| Bangladesh | **63** |
| India | **295** |
| Backup Stream Entries | **423** |
| IPTV Local Logos | **STALE** |
| IPTV EPG Programme Coverage | **50%** |
| IPTV EPG Mapping | **58.9%** |
| Stream Health Tested | **STALE** |
| Stream Health Failures | **STALE** |
| Persistent Failures | **STALE** |
| Near-Duplicate URL Families | **STALE / UNKNOWN** |
| Audit findings (review warnings included) | **STALE / UNKNOWN** |
| Pre-Publish Gate | **STALE / UNKNOWN** |
| Pre-Publish Gate Generated | **2026-11-15T02:24:51+00:00** |

## Quality Controls (STALE / UNKNOWN — saved audit values shown for reference)
- Duplicate stream URLs: **STALE / UNKNOWN (last saved: 0)**
- Metadata conflicts (canonical primary scope): **STALE / UNKNOWN (last saved: 0)**
- Same-name / different-ID collisions (canonical primary scope): **STALE / UNKNOWN (last saved: 1)**
- Cross-queue metadata identity variants: **1**
- Cross-queue same-name / different-ID collisions: **14**
- Duplicate primary identities: **STALE / UNKNOWN (last saved: 0)**
- Primary channel-number collisions: **STALE / UNKNOWN (last saved: 0)**
- Primary entries missing channel numbers: **STALE / UNKNOWN (last saved: 13)**
- Logo exceptions: **STALE / UNKNOWN (last saved: 0)**
- Malformed EXTINF entries: **STALE / UNKNOWN (last saved: 0)**
- Category block-order issues: **STALE / UNKNOWN (last saved: 30)**
- Alphabetical ordering issues: **STALE / UNKNOWN (last saved: 48)**
- Signed/tokenized URLs: **STALE / UNKNOWN (last saved: 18)**

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
- EPG IDs audited: **645**
- Mapped: **380 (58.9%)**
- Current/future programme coverage: **326/645 (50.5%)**
- No mapping: **265**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (verified against both current playlist inventories)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-15T02:24:50.754118+00:00** | **STALE** |
| EPG coverage / two-playlist inventory | **2026-11-15T08:14:46+00:00** | **CURRENT** |
| Stream health | **2026-11-15T02:25:32+00:00** | **STALE** |
| Pre-publish gate | **2026-11-15T02:24:51+00:00** | **STALE** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **1284 → 1284**
- Latest health failures: **188 → 189**

Historical records are retained in reports/maintenance-history.json.
