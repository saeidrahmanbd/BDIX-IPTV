# Update Report

_Last generated: **2026-11-10 08:57 UTC**_

Source playlist SHA-256: **b9788f72fccc6068192664229352aba60bf534028a8d2362a740cf7623425e9c**

| Metric | Current |
|---|---:|
| Streams | **1066** |
| Active Channel Identities | **577** |
| Active Primary Streams | **577** |
| Bangladesh | **50** |
| India | **281** |
| Backup Stream Entries | **327** |
| IPTV Local Logos | **STALE** |
| IPTV EPG Programme Coverage | **52%** |
| IPTV EPG Mapping | **60.8%** |
| Stream Health Tested | **STALE** |
| Stream Health Failures | **STALE** |
| Persistent Failures | **STALE** |
| Near-Duplicate URL Families | **STALE / UNKNOWN** |
| Audit Blocking Issues | **STALE / UNKNOWN** |
| Pre-Publish Gate | **STALE / UNKNOWN** |
| Pre-Publish Gate Generated | **2026-11-10T06:28:17+00:00** |

## Quality Controls (STALE / UNKNOWN — saved audit values shown for reference)
- Duplicate stream URLs: **STALE / UNKNOWN (last saved: 0)**
- Metadata conflicts (canonical primary scope): **STALE / UNKNOWN (last saved: 0)**
- Same-name / different-ID collisions (canonical primary scope): **STALE / UNKNOWN (last saved: 0)**
- Cross-queue metadata identity variants: **0**
- Cross-queue same-name / different-ID collisions: **1**
- Duplicate primary identities: **STALE / UNKNOWN (last saved: 0)**
- Primary channel-number collisions: **STALE / UNKNOWN (last saved: 0)**
- Primary entries missing channel numbers: **STALE / UNKNOWN (last saved: 3)**
- Logo exceptions: **STALE / UNKNOWN (last saved: 0)**
- Malformed EXTINF entries: **STALE / UNKNOWN (last saved: 0)**
- Category block-order issues: **STALE / UNKNOWN (last saved: 1)**
- Alphabetical ordering issues: **STALE / UNKNOWN (last saved: 3)**
- Signed/tokenized URLs: **STALE / UNKNOWN (last saved: 8)**

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
- EPG IDs audited: **577**
- Mapped: **351 (60.8%)**
- Current/future programme coverage: **302/577 (52.3%)**
- No mapping: **226**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (verified against both current playlist inventories)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-10T06:28:17.192399+00:00** | **STALE** |
| EPG coverage / two-playlist inventory | **2026-11-10T08:57:31+00:00** | **CURRENT** |
| Stream health | **2026-11-10T06:28:55+00:00** | **STALE** |
| Pre-publish gate | **2026-11-10T06:28:17+00:00** | **STALE** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **1074 → 1066**
- Latest health failures: **227 → 195**

Historical records are retained in reports/maintenance-history.json.
