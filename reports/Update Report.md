# Update Report

_Last generated: **2026-11-09 09:40 UTC**_

Source playlist SHA-256: **d4bab23c700d8a1cfd18c45af6ffafabb6fcc5dece8fef83fa4f96629a9580eb**

| Metric | Current |
|---|---:|
| Streams | **1061** |
| Active Channel Identities | **592** |
| Active Primary Streams | **592** |
| Bangladesh | **60** |
| India | **294** |
| Backup Stream Entries | **376** |
| IPTV Local Logos | **99.5%** |
| IPTV EPG Programme Coverage | **53%** |
| IPTV EPG Mapping | **61.7%** |
| Stream Health Tested | **1061** |
| Stream Health Failures | **175** |
| Persistent Failures | **156** |
| Near-Duplicate URL Families | **2** |
| Audit Blocking Issues | **24** |
| Pre-Publish Gate | **BLOCK** |
| Pre-Publish Gate Generated | **2026-11-09T09:39:54+00:00** |

## Quality Controls 
- Duplicate stream URLs: **1**
- Metadata conflicts (canonical primary scope): **0**
- Same-name / different-ID collisions (canonical primary scope): **0**
- Cross-queue metadata identity variants: **0**
- Cross-queue same-name / different-ID collisions: **2**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **1**
- Logo exceptions: **5**
- Malformed EXTINF entries: **0**
- Category block-order issues: **11**
- Alphabetical ordering issues: **6**
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
- EPG IDs audited: **592**
- Mapped: **365 (61.7%)**
- Current/future programme coverage: **316/592 (53.4%)**
- No mapping: **227**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (verified against both current playlist inventories)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-09T09:39:53.555877+00:00** | **CURRENT** |
| EPG coverage / two-playlist inventory | **2026-11-09T09:19:49+00:00** | **CURRENT** |
| Stream health | **2026-11-09T09:40:29+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-09T09:39:54+00:00** | **CURRENT** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **1061 → 1061**
- Latest health failures: **166 → 175**

Historical records are retained in reports/maintenance-history.json.
