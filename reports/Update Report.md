# Update Report

_Last generated: **2026-11-11 12:12 UTC**_

Source playlist SHA-256: **81708ed765570d9c3d509cd9a471595b621b5f2145e4decc0d8bed1cea81d3ce**

| Metric | Current |
|---|---:|
| Streams | **1143** |
| Active Channel Identities | **579** |
| Active Primary Streams | **580** |
| Bangladesh | **53** |
| India | **293** |
| Backup Stream Entries | **385** |
| IPTV Local Logos | **100.0%** |
| IPTV EPG Programme Coverage | **53%** |
| IPTV EPG Mapping | **61.7%** |
| Stream Health Tested | **1143** |
| Stream Health Failures | **190** |
| Persistent Failures | **183** |
| Near-Duplicate URL Families | **1** |
| Audit Blocking Issues | **24** |
| Pre-Publish Gate | **BLOCK** |
| Pre-Publish Gate Generated | **2026-11-11T09:29:34+00:00** |

## Quality Controls 
- Duplicate stream URLs: **0**
- Metadata conflicts (canonical primary scope): **0**
- Same-name / different-ID collisions (canonical primary scope): **0**
- Cross-queue metadata identity variants: **1**
- Cross-queue same-name / different-ID collisions: **1**
- Duplicate primary identities: **1**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **22**
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
- EPG IDs audited: **579**
- Mapped: **357 (61.7%)**
- Current/future programme coverage: **308/579 (53.2%)**
- No mapping: **222**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (verified against both current playlist inventories)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-11T09:29:34.207066+00:00** | **CURRENT** |
| EPG coverage / two-playlist inventory | **2026-11-11T12:12:13+00:00** | **CURRENT** |
| Stream health | **2026-11-11T09:30:17+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-11T09:29:34+00:00** | **CURRENT** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **1143 → 1143**
- Latest health failures: **189 → 190**

Historical records are retained in reports/maintenance-history.json.
