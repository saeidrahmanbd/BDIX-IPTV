# Update Report

_Last generated: **2026-11-11 19:26 UTC**_

Source playlist SHA-256: **a98bfb7e890a2d639d238b957b98d47678e6aef0a035b526716557990ef5c04f**

| Metric | Current |
|---|---:|
| Streams | **1331** |
| Active Channel Identities | **685** |
| Active Primary Streams | **685** |
| Bangladesh | **67** |
| India | **301** |
| Backup Stream Entries | **463** |
| IPTV Local Logos | **STALE** |
| IPTV EPG Programme Coverage | **52%** |
| IPTV EPG Mapping | **59.1%** |
| Stream Health Tested | **STALE** |
| Stream Health Failures | **STALE** |
| Persistent Failures | **STALE** |
| Near-Duplicate URL Families | **STALE / UNKNOWN** |
| Audit Blocking Issues | **STALE / UNKNOWN** |
| Pre-Publish Gate | **STALE / UNKNOWN** |
| Pre-Publish Gate Generated | **2026-11-11T14:59:54+00:00** |

## Quality Controls (STALE / UNKNOWN — saved audit values shown for reference)
- Duplicate stream URLs: **STALE / UNKNOWN (last saved: 0)**
- Metadata conflicts (canonical primary scope): **STALE / UNKNOWN (last saved: 0)**
- Same-name / different-ID collisions (canonical primary scope): **STALE / UNKNOWN (last saved: 3)**
- Cross-queue metadata identity variants: **1**
- Cross-queue same-name / different-ID collisions: **16**
- Duplicate primary identities: **STALE / UNKNOWN (last saved: 1)**
- Primary channel-number collisions: **STALE / UNKNOWN (last saved: 2)**
- Primary entries missing channel numbers: **STALE / UNKNOWN (last saved: 0)**
- Logo exceptions: **STALE / UNKNOWN (last saved: 46)**
- Malformed EXTINF entries: **STALE / UNKNOWN (last saved: 0)**
- Category block-order issues: **STALE / UNKNOWN (last saved: 30)**
- Alphabetical ordering issues: **STALE / UNKNOWN (last saved: 98)**
- Signed/tokenized URLs: **STALE / UNKNOWN (last saved: 26)**

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
- EPG IDs audited: **685**
- Mapped: **405 (59.1%)**
- Current/future programme coverage: **356/685 (52.0%)**
- No mapping: **280**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (verified against both current playlist inventories)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-11T14:59:53.689044+00:00** | **STALE** |
| EPG coverage / two-playlist inventory | **2026-11-11T19:26:32+00:00** | **CURRENT** |
| Stream health | **2026-11-11T15:01:04+00:00** | **STALE** |
| Pre-publish gate | **2026-11-11T14:59:54+00:00** | **STALE** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **1143 → 1391**
- Latest health failures: **190 → 237**

Historical records are retained in reports/maintenance-history.json.
