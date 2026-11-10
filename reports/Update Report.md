# Update Report

_Last generated: **2026-11-10 09:57 UTC**_

Source playlist SHA-256: **963a30fd1d7f8b62a5c75208c6fa67adc11d24316ad9d3ff6b7ad3927000737d**

| Metric | Current |
|---|---:|
| Streams | **1121** |
| Active Channel Identities | **580** |
| Active Primary Streams | **580** |
| Bangladesh | **50** |
| India | **284** |
| Backup Stream Entries | **379** |
| IPTV Local Logos | **99.9%** |
| IPTV EPG Programme Coverage | **52%** |
| IPTV EPG Mapping | **60.9%** |
| Stream Health Tested | **1121** |
| Stream Health Failures | **199** |
| Persistent Failures | **166** |
| Near-Duplicate URL Families | **2** |
| Audit Blocking Issues | **13** |
| Pre-Publish Gate | **BLOCK** |
| Pre-Publish Gate Generated | **2026-11-10T09:57:03+00:00** |

## Quality Controls 
- Duplicate stream URLs: **0**
- Metadata conflicts (canonical primary scope): **0**
- Same-name / different-ID collisions (canonical primary scope): **0**
- Cross-queue metadata identity variants: **0**
- Cross-queue same-name / different-ID collisions: **1**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **6**
- Logo exceptions: **1**
- Malformed EXTINF entries: **1**
- Category block-order issues: **1**
- Alphabetical ordering issues: **4**
- Signed/tokenized URLs: **11**

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
- EPG IDs audited: **580**
- Mapped: **353 (60.9%)**
- Current/future programme coverage: **304/580 (52.4%)**
- No mapping: **227**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (verified against both current playlist inventories)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-10T09:57:03.261070+00:00** | **CURRENT** |
| EPG coverage / two-playlist inventory | **2026-11-10T09:55:19+00:00** | **CURRENT** |
| Stream health | **2026-11-10T09:57:42+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-10T09:57:03+00:00** | **CURRENT** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **1066 → 1121**
- Latest health failures: **195 → 199**

Historical records are retained in reports/maintenance-history.json.
