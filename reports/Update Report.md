# Update Report

_Last generated: **2026-11-19 04:15 UTC**_

Source playlist SHA-256: **8611340c6b07807062028b490d6f6cd925bf5fb18ac79bb174f637872523e81e**

| Metric | Current |
|---|---:|
| Streams | **1390** |
| Active Channel Identities | **714** |
| Active Primary Streams | **714** |
| Bangladesh | **70** |
| India | **302** |
| Backup Stream Entries | **463** |
| IPTV Local Logos | **99.9%** |
| IPTV EPG Programme Coverage | **54%** |
| IPTV EPG Mapping | **60.8%** |
| Stream Health Tested | **1390** |
| Stream Health Failures | **234** |
| Persistent Failures | **50** |
| Near-Duplicate URL Families | **1** |
| Audit findings (review warnings included) | **1** |
| Pre-Publish Gate | **PASS** |
| Pre-Publish Gate Generated | **2026-11-19T03:49:29+00:00** |

## Quality Controls 
- Duplicate stream URLs: **0**
- Metadata conflicts (canonical primary scope): **0**
- Same-name / different-ID collisions (canonical primary scope): **0**
- Cross-queue metadata identity variants: **4**
- Cross-queue same-name / different-ID collisions: **8**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **0**
- Logo exceptions: **1**
- Malformed EXTINF entries: **0**
- Category block-order issues: **0**
- Alphabetical ordering issues: **0**
- Signed/tokenized URLs: **11**

## Safety & Automation
- Stream health is non-destructive and keeps per-URL failure history.
- Backup streams are never automatically deleted because of health failures.
- `Backup` stores alternate streams; `Review`, `New Channels`, and `New Backups` are review-only queues and are excluded from Xtream.
- Pre-publish gate status: **PASS**
- Canonical channel identity index: reports/channel-identity-index.json

## Counting Scope
- **Active Channel Identities / Active Primary Streams** count only canonical playlist groups.
- `Backup`, `Review`, `New Channels`, and `New Backups` are excluded from the active-primary count.
- EPG identity/programme coverage is reported only when the published XMLTV is valid, current, and its freshness report is PASS.
- **Backup Stream Entries** count playlist rows, not independent CDN/origin infrastructures. Backup independence is reviewed separately.

## EPG
- EPG IDs audited: **714**
- Mapped: **434 (60.8%)**
- Current/future programme coverage: **386/714 (54.1%)**
- No mapping: **280**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (verified against both current playlist inventories)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-19T03:49:29.060900+00:00** | **CURRENT** |
| EPG coverage / two-playlist inventory | **2026-11-19T04:15:52+00:00** | **CURRENT** |
| Stream health | **2026-11-19T03:50:24+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-19T03:49:29+00:00** | **CURRENT** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **1378 → 1390**
- Latest health failures: **264 → 234**

Historical records are retained in reports/maintenance-history.json.
