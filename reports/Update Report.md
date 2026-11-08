# Update Report

_Last generated: **2026-11-08 10:56 UTC**_

Source playlist SHA-256: **42d6d2b01b52c16d2c9a8f0d0593b6df532bef90c37667e755cfc1b085f5540c**

| Metric | Current |
|---|---:|
| Streams | **943** |
| Active Channel Identities | **609** |
| Active Primary Streams | **609** |
| Bangladesh | **66** |
| India | **294** |
| Backup Stream Entries | **333** |
| IPTV Local Logos | **99.9%** |
| IPTV EPG Programme Coverage | **PENDING** |
| IPTV EPG Mapping | **PENDING** |
| Stream Health Tested | **943** |
| Stream Health Failures | **56** |
| Persistent Failures | **49** |
| Near-Duplicate URL Families | **2** |
| Audit Blocking Issues | **1** |
| Pre-Publish Gate | **BLOCK** |
| Pre-Publish Gate Generated | **2026-11-08T10:56:14+00:00** |

## Quality Controls 
- Duplicate stream URLs: **0**
- Metadata conflicts (canonical primary scope): **0**
- Same-name / different-ID collisions (canonical primary scope): **0**
- Cross-queue metadata identity variants: **0**
- Cross-queue same-name / different-ID collisions: **0**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **0**
- Logo exceptions: **1**
- Malformed EXTINF entries: **0**
- Category block-order issues: **0**
- Alphabetical ordering issues: **0**
- Signed/tokenized URLs: **8**

## Safety & Automation
- Stream health is non-destructive and keeps per-URL failure history.
- Backup streams are never automatically deleted because of health failures.
- `Backup` stores alternate streams; `Review`, `New Channels`, and `New Backups` are review-only queues and are excluded from Xtream.
- Pre-publish gate status: **BLOCK**
- Canonical channel identity index: reports/channel-identity-index.json

## Counting Scope
- **Active Channel Identities / Active Primary Streams** count only canonical playlist groups.
- `Backup`, `Review`, `New Channels`, and `New Backups` are excluded from the active-primary count.
- EPG identity/programme coverage is reported only when the published XMLTV is valid, current, and its freshness report is PASS.
- **Backup Stream Entries** count playlist rows, not independent CDN/origin infrastructures. Backup independence is reviewed separately.

## EPG
- EPG IDs audited: **PENDING — guide not current**
- Mapped: **PENDING — no current validated guide**
- Current/future programme coverage: **PENDING — no current validated guide**
- No mapping: **PENDING — guide not current**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (awaiting a valid, fresh published guide)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-08T10:56:14.381524+00:00** | **CURRENT** |
| EPG coverage / two-playlist inventory | **2026-11-08T02:50:41+00:00** | **PENDING — guide missing or freshness not PASS** |
| Stream health | **2026-11-08T10:56:43+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-08T10:56:14+00:00** | **CURRENT** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **952 → 943**
- Latest health failures: **54 → 56**

Historical records are retained in reports/maintenance-history.json.
