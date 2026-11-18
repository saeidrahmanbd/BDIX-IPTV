# Update Report

_Last generated: **2026-11-18 13:25 UTC**_

Source playlist SHA-256: **002e4acc43c2210fe25ceb35ed68582b869af2706f3754964d43a274d3618baf**

| Metric | Current |
|---|---:|
| Streams | **1378** |
| Active Channel Identities | **714** |
| Active Primary Streams | **714** |
| Bangladesh | **70** |
| India | **302** |
| Backup Stream Entries | **463** |
| IPTV Local Logos | **STALE** |
| IPTV EPG Programme Coverage | **54%** |
| IPTV EPG Mapping | **60.8%** |
| Stream Health Tested | **1378** |
| Stream Health Failures | **264** |
| Persistent Failures | **49** |
| Near-Duplicate URL Families | **1** |
| Audit findings (review warnings included) | **STALE / UNKNOWN** |
| Pre-Publish Gate | **STALE / UNKNOWN** |
| Pre-Publish Gate Generated | **2026-11-18T03:24:09+00:00** |

## Quality Controls (STALE / UNKNOWN — saved audit values shown for reference)
- Duplicate stream URLs: **STALE / UNKNOWN (last saved: 0)**
- Metadata conflicts (canonical primary scope): **STALE / UNKNOWN (last saved: 0)**
- Same-name / different-ID collisions (canonical primary scope): **STALE / UNKNOWN (last saved: 1)**
- Cross-queue metadata identity variants: **2**
- Cross-queue same-name / different-ID collisions: **7**
- Duplicate primary identities: **STALE / UNKNOWN (last saved: 0)**
- Primary channel-number collisions: **STALE / UNKNOWN (last saved: 0)**
- Primary entries missing channel numbers: **STALE / UNKNOWN (last saved: 15)**
- Logo exceptions: **STALE / UNKNOWN (last saved: 1)**
- Malformed EXTINF entries: **STALE / UNKNOWN (last saved: 0)**
- Category block-order issues: **STALE / UNKNOWN (last saved: 0)**
- Alphabetical ordering issues: **STALE / UNKNOWN (last saved: 2)**
- Signed/tokenized URLs: **STALE / UNKNOWN (last saved: 11)**

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
- EPG IDs audited: **714**
- Mapped: **434 (60.8%)**
- Current/future programme coverage: **384/714 (53.8%)**
- No mapping: **280**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (verified against both current playlist inventories)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-18T03:24:09.019889+00:00** | **STALE** |
| EPG coverage / two-playlist inventory | **2026-11-18T12:49:22+00:00** | **CURRENT** |
| Stream health | **2026-11-18T03:25:29+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-18T03:24:09+00:00** | **STALE** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **1378 → 1378**
- Latest health failures: **215 → 264**

Historical records are retained in reports/maintenance-history.json.
