# Update Report

_Last generated: **2026-11-16 03:33 UTC**_

Source playlist SHA-256: **910e85f0a79f101b8afe550c781126fb156b183e4c678472f2fe3f1699777d73**

| Metric | Current |
|---|---:|
| Streams | **1298** |
| Active Channel Identities | **657** |
| Active Primary Streams | **657** |
| Bangladesh | **66** |
| India | **300** |
| Backup Stream Entries | **438** |
| IPTV Local Logos | **100.0%** |
| IPTV EPG Programme Coverage | **50%** |
| IPTV EPG Mapping | **58.8%** |
| Stream Health Tested | **1298** |
| Stream Health Failures | **200** |
| Persistent Failures | **0** |
| Near-Duplicate URL Families | **1** |
| Audit findings (review warnings included) | **128** |
| Pre-Publish Gate | **PASS** |
| Pre-Publish Gate Generated | **2026-11-16T02:50:59+00:00** |

## Quality Controls 
- Duplicate stream URLs: **0**
- Metadata conflicts (canonical primary scope): **0**
- Same-name / different-ID collisions (canonical primary scope): **0**
- Cross-queue metadata identity variants: **2**
- Cross-queue same-name / different-ID collisions: **12**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **22**
- Logo exceptions: **0**
- Malformed EXTINF entries: **0**
- Category block-order issues: **36**
- Alphabetical ordering issues: **70**
- Signed/tokenized URLs: **12**

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
- EPG IDs audited: **657**
- Mapped: **386 (58.8%)**
- Current/future programme coverage: **331/657 (50.4%)**
- No mapping: **271**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (verified against both current playlist inventories)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-16T02:50:59.144515+00:00** | **CURRENT** |
| EPG coverage / two-playlist inventory | **2026-11-16T03:33:33+00:00** | **CURRENT** |
| Stream health | **2026-11-16T02:51:42+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-16T02:50:59+00:00** | **CURRENT** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **1284 → 1298**
- Latest health failures: **189 → 200**

Historical records are retained in reports/maintenance-history.json.
