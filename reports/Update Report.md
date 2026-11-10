# Update Report

_Last generated: **2026-11-10 13:26 UTC**_

Source playlist SHA-256: **1fecff40e4b2f5a4a6e31805dc88b93179bdf2d752f56b8ae8cfc6aaacd8a6db**

| Metric | Current |
|---|---:|
| Streams | **1169** |
| Active Channel Identities | **605** |
| Active Primary Streams | **605** |
| Bangladesh | **54** |
| India | **304** |
| Backup Stream Entries | **393** |
| IPTV Local Logos | **100.0%** |
| IPTV EPG Programme Coverage | **PENDING** |
| IPTV EPG Mapping | **PENDING** |
| Stream Health Tested | **1169** |
| Stream Health Failures | **184** |
| Persistent Failures | **177** |
| Near-Duplicate URL Families | **2** |
| Audit Blocking Issues | **0** |
| Pre-Publish Gate | **BLOCK** |
| Pre-Publish Gate Generated | **2026-11-10T13:25:46+00:00** |

## Quality Controls 
- Duplicate stream URLs: **0**
- Metadata conflicts (canonical primary scope): **0**
- Same-name / different-ID collisions (canonical primary scope): **0**
- Cross-queue metadata identity variants: **0**
- Cross-queue same-name / different-ID collisions: **1**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **0**
- Logo exceptions: **0**
- Malformed EXTINF entries: **0**
- Category block-order issues: **0**
- Alphabetical ordering issues: **0**
- Signed/tokenized URLs: **19**

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
| Playlist audit | **2026-11-10T13:25:46.094034+00:00** | **CURRENT** |
| EPG coverage / two-playlist inventory | **2026-11-10T13:07:49+00:00** | **PENDING — guide missing or freshness not PASS** |
| Stream health | **2026-11-10T13:26:36+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-10T13:25:46+00:00** | **CURRENT** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **1169 → 1169**
- Latest health failures: **187 → 184**

Historical records are retained in reports/maintenance-history.json.
