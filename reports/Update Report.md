# Update Report

_Last generated: **2026-11-12 07:12 UTC**_

Source playlist SHA-256: **b4bd82f1c2158f3f4cef5a6a16f9567e9db54d682a807b9dbc4ee64ccc0d59a4**

| Metric | Current |
|---|---:|
| Streams | **1242** |
| Active Channel Identities | **650** |
| Active Primary Streams | **650** |
| Bangladesh | **62** |
| India | **298** |
| Backup Stream Entries | **420** |
| IPTV Local Logos | **STALE** |
| IPTV EPG Programme Coverage | **51%** |
| IPTV EPG Mapping | **58.9%** |
| Stream Health Tested | **STALE** |
| Stream Health Failures | **STALE** |
| Persistent Failures | **STALE** |
| Near-Duplicate URL Families | **STALE / UNKNOWN** |
| Audit Blocking Issues | **STALE / UNKNOWN** |
| Pre-Publish Gate | **STALE / UNKNOWN** |
| Pre-Publish Gate Generated | **2026-11-12T05:40:29+00:00** |

## Quality Controls (STALE / UNKNOWN — saved audit values shown for reference)
- Duplicate stream URLs: **STALE / UNKNOWN (last saved: 0)**
- Metadata conflicts (canonical primary scope): **STALE / UNKNOWN (last saved: 0)**
- Same-name / different-ID collisions (canonical primary scope): **STALE / UNKNOWN (last saved: 2)**
- Cross-queue metadata identity variants: **1**
- Cross-queue same-name / different-ID collisions: **24**
- Duplicate primary identities: **STALE / UNKNOWN (last saved: 0)**
- Primary channel-number collisions: **STALE / UNKNOWN (last saved: 0)**
- Primary entries missing channel numbers: **STALE / UNKNOWN (last saved: 0)**
- Logo exceptions: **STALE / UNKNOWN (last saved: 7)**
- Malformed EXTINF entries: **STALE / UNKNOWN (last saved: 0)**
- Category block-order issues: **STALE / UNKNOWN (last saved: 0)**
- Alphabetical ordering issues: **STALE / UNKNOWN (last saved: 12)**
- Signed/tokenized URLs: **STALE / UNKNOWN (last saved: 23)**

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
- EPG IDs audited: **650**
- Mapped: **383 (58.9%)**
- Current/future programme coverage: **334/650 (51.4%)**
- No mapping: **267**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (verified against both current playlist inventories)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-12T05:40:28.612813+00:00** | **STALE** |
| EPG coverage / two-playlist inventory | **2026-11-12T07:12:48+00:00** | **CURRENT** |
| Stream health | **2026-11-12T05:41:10+00:00** | **STALE** |
| Pre-publish gate | **2026-11-12T05:40:29+00:00** | **STALE** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **1331 → 1331**
- Latest health failures: **185 → 185**

Historical records are retained in reports/maintenance-history.json.
