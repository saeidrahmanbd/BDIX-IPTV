# Update Report

_Last generated: **2026-11-10 15:02 UTC**_

Source playlist SHA-256: **8b798099a5a4fd789da0456a308e8091c7d2c5da6795cd227c44c1e6258a7ef7**

| Metric | Current |
|---|---:|
| Streams | **1171** |
| Active Channel Identities | **606** |
| Active Primary Streams | **606** |
| Bangladesh | **54** |
| India | **304** |
| Backup Stream Entries | **394** |
| IPTV Local Logos | **100.0%** |
| IPTV EPG Programme Coverage | **53%** |
| IPTV EPG Mapping | **61.2%** |
| Stream Health Tested | **1171** |
| Stream Health Failures | **231** |
| Persistent Failures | **174** |
| Near-Duplicate URL Families | **2** |
| Audit Blocking Issues | **2** |
| Pre-Publish Gate | **BLOCK** |
| Pre-Publish Gate Generated | **2026-11-10T15:01:33+00:00** |

## Quality Controls 
- Duplicate stream URLs: **0**
- Metadata conflicts (canonical primary scope): **0**
- Same-name / different-ID collisions (canonical primary scope): **0**
- Cross-queue metadata identity variants: **0**
- Cross-queue same-name / different-ID collisions: **1**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **1**
- Logo exceptions: **0**
- Malformed EXTINF entries: **0**
- Category block-order issues: **0**
- Alphabetical ordering issues: **1**
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
- EPG IDs audited: **606**
- Mapped: **371 (61.2%)**
- Current/future programme coverage: **321/606 (53.0%)**
- No mapping: **235**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (verified against both current playlist inventories)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-10T15:01:32.847495+00:00** | **CURRENT** |
| EPG coverage / two-playlist inventory | **2026-11-10T14:51:24+00:00** | **CURRENT** |
| Stream health | **2026-11-10T15:02:35+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-10T15:01:33+00:00** | **CURRENT** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **1171 → 1171**
- Latest health failures: **195 → 231**

Historical records are retained in reports/maintenance-history.json.
