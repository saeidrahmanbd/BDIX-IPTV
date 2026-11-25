# Update Report

_Last generated: **2026-11-25 03:30 UTC**_

Source playlist SHA-256: **a2ef9bb3e7d03dbfffd4f78e796027e4f5e46374fe9717d89785190c04f23e6a**

| Metric | Current |
|---|---:|
| Streams | **1354** |
| Active Channel Identities | **695** |
| Active Primary Streams | **704** |
| Bangladesh | **70** |
| India | **315** |
| Backup Stream Entries | **396** |
| IPTV Local Logos | **100.0%** |
| IPTV EPG Programme Coverage | **54%** |
| IPTV EPG Mapping | **62.2%** |
| Stream Health Tested | **1354** |
| Stream Health Failures | **254** |
| Persistent Failures | **57** |
| Near-Duplicate URL Families | **1** |
| Audit findings (review warnings included) | **19** |
| Pre-Publish Gate | **BLOCK** |
| Pre-Publish Gate Generated | **2026-11-25T03:29:24+00:00** |

## Quality Controls 
- Duplicate stream URLs: **0**
- Metadata conflicts (canonical primary scope): **0**
- Same-name / different-ID collisions (canonical primary scope): **0**
- Cross-queue metadata identity variants: **1**
- Cross-queue same-name / different-ID collisions: **17**
- Duplicate primary identities: **4**
- Primary channel-number collisions: **1**
- Primary entries missing channel numbers: **9**
- Logo exceptions: **0**
- Malformed EXTINF entries: **0**
- Category block-order issues: **0**
- Alphabetical ordering issues: **5**
- Signed/tokenized URLs: **14**

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
- EPG IDs audited: **695**
- Mapped: **432 (62.2%)**
- Current/future programme coverage: **376/695 (54.1%)**
- No mapping: **263**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (verified against both current playlist inventories)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-25T03:29:23.525594+00:00** | **CURRENT** |
| EPG coverage / two-playlist inventory | **2026-11-25T01:29:32+00:00** | **CURRENT** |
| Stream health | **2026-11-25T03:30:21+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-25T03:29:24+00:00** | **CURRENT** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **1354 → 1354**
- Latest health failures: **293 → 254**

Historical records are retained in reports/maintenance-history.json.
