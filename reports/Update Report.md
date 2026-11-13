# Update Report

_Last generated: **2026-11-13 01:32 UTC**_

Source playlist SHA-256: **4757dc831cd0ebeecd432ee55cb3d5529eaf7e11858aa6a72ac73eff4ad7e4eb**

| Metric | Current |
|---|---:|
| Streams | **1242** |
| Active Channel Identities | **646** |
| Active Primary Streams | **646** |
| Bangladesh | **64** |
| India | **293** |
| Backup Stream Entries | **424** |
| IPTV Local Logos | **STALE** |
| IPTV EPG Programme Coverage | **50%** |
| IPTV EPG Mapping | **58.7%** |
| Stream Health Tested | **1242** |
| Stream Health Failures | **181** |
| Persistent Failures | **161** |
| Near-Duplicate URL Families | **1** |
| Audit Blocking Issues | **STALE / UNKNOWN** |
| Pre-Publish Gate | **STALE / UNKNOWN** |
| Pre-Publish Gate Generated | **2026-11-12T15:30:27+00:00** |

## Quality Controls (STALE / UNKNOWN — saved audit values shown for reference)
- Duplicate stream URLs: **STALE / UNKNOWN (last saved: 0)**
- Metadata conflicts (canonical primary scope): **STALE / UNKNOWN (last saved: 0)**
- Same-name / different-ID collisions (canonical primary scope): **STALE / UNKNOWN (last saved: 6)**
- Cross-queue metadata identity variants: **2**
- Cross-queue same-name / different-ID collisions: **25**
- Duplicate primary identities: **STALE / UNKNOWN (last saved: 0)**
- Primary channel-number collisions: **STALE / UNKNOWN (last saved: 0)**
- Primary entries missing channel numbers: **STALE / UNKNOWN (last saved: 13)**
- Logo exceptions: **STALE / UNKNOWN (last saved: 1)**
- Malformed EXTINF entries: **STALE / UNKNOWN (last saved: 0)**
- Category block-order issues: **STALE / UNKNOWN (last saved: 31)**
- Alphabetical ordering issues: **STALE / UNKNOWN (last saved: 59)**
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
- EPG IDs audited: **646**
- Mapped: **379 (58.7%)**
- Current/future programme coverage: **325/646 (50.3%)**
- No mapping: **267**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (verified against both current playlist inventories)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-12T15:30:26.814600+00:00** | **STALE** |
| EPG coverage / two-playlist inventory | **2026-11-13T01:32:49+00:00** | **CURRENT** |
| Stream health | **2026-11-12T15:31:10+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-12T15:30:27+00:00** | **STALE** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **1242 → 1242**
- Latest health failures: **167 → 181**

Historical records are retained in reports/maintenance-history.json.
