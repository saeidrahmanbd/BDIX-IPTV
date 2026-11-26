# Update Report

_Last generated: **2026-11-26 10:37 UTC**_

Source playlist SHA-256: **8360de3894d65813a1852f915a24ce62d26f2b69e04af590da5ae31538270ea7**

| Metric | Current |
|---|---:|
| Streams | **1143** |
| Active Channel Identities | **708** |
| Active Primary Streams | **708** |
| Bangladesh | **67** |
| India | **322** |
| Backup Stream Entries | **434** |
| IPTV Local Logos | **STALE** |
| IPTV EPG Programme Coverage | **54%** |
| IPTV EPG Mapping | **60.3%** |
| Stream Health Tested | **STALE** |
| Stream Health Failures | **STALE** |
| Persistent Failures | **STALE** |
| Near-Duplicate URL Families | **STALE / UNKNOWN** |
| Audit findings (review warnings included) | **STALE / UNKNOWN** |
| Pre-Publish Gate | **STALE / UNKNOWN** |
| Pre-Publish Gate Generated | **2026-11-26T05:34:17+00:00** |

## Quality Controls (STALE / UNKNOWN — saved audit values shown for reference)
- Duplicate stream URLs: **STALE / UNKNOWN (last saved: 0)**
- Metadata conflicts (canonical primary scope): **STALE / UNKNOWN (last saved: 0)**
- Same-name / different-ID collisions (canonical primary scope): **STALE / UNKNOWN (last saved: 0)**
- Cross-queue metadata identity variants: **1**
- Cross-queue same-name / different-ID collisions: **4**
- Duplicate primary identities: **STALE / UNKNOWN (last saved: 0)**
- Primary channel-number collisions: **STALE / UNKNOWN (last saved: 1)**
- Primary entries missing channel numbers: **STALE / UNKNOWN (last saved: 0)**
- Logo exceptions: **STALE / UNKNOWN (last saved: 0)**
- Malformed EXTINF entries: **STALE / UNKNOWN (last saved: 1)**
- Category block-order issues: **STALE / UNKNOWN (last saved: 0)**
- Alphabetical ordering issues: **STALE / UNKNOWN (last saved: 3)**
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
- EPG IDs audited: **708**
- Mapped: **427 (60.3%)**
- Current/future programme coverage: **379/708 (53.5%)**
- No mapping: **281**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (verified against both current playlist inventories)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-26T05:34:16.131705+00:00** | **STALE** |
| EPG coverage / two-playlist inventory | **2026-11-26T10:37:30+00:00** | **CURRENT** |
| Stream health | **2026-11-26T05:35:29+00:00** | **STALE** |
| Pre-publish gate | **2026-11-26T05:34:17+00:00** | **STALE** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **1371 → 1430**
- Latest health failures: **266 → 275**

Historical records are retained in reports/maintenance-history.json.
