# Update Report

_Last generated: **2026-11-09 01:08 UTC**_

Source playlist SHA-256: **8675200ab8b37acc114ba0d5fc456d80611f2715c3226f08837681133391c6b5**

| Metric | Current |
|---|---:|
| Streams | **998** |
| Active Channel Identities | **596** |
| Active Primary Streams | **596** |
| Bangladesh | **58** |
| India | **291** |
| Backup Stream Entries | **324** |
| IPTV Local Logos | **100.0%** |
| IPTV EPG Programme Coverage | **47%** |
| IPTV EPG Mapping | **61.4%** |
| Stream Health Tested | **998** |
| Stream Health Failures | **137** |
| Persistent Failures | **122** |
| Near-Duplicate URL Families | **2** |
| Audit Blocking Issues | **0** |
| Pre-Publish Gate | **PASS** |
| Pre-Publish Gate Generated | **2026-11-09T00:40:13+00:00** |

## Quality Controls 
- Duplicate stream URLs: **0**
- Metadata conflicts (canonical primary scope): **0**
- Same-name / different-ID collisions (canonical primary scope): **0**
- Cross-queue metadata identity variants: **0**
- Cross-queue same-name / different-ID collisions: **2**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **0**
- Logo exceptions: **0**
- Malformed EXTINF entries: **0**
- Category block-order issues: **0**
- Alphabetical ordering issues: **0**
- Signed/tokenized URLs: **8**

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
- EPG IDs audited: **596**
- Mapped: **366 (61.4%)**
- Current/future programme coverage: **278/596 (46.6%)**
- No mapping: **230**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (verified against both current playlist inventories)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-09T00:40:12.986589+00:00** | **CURRENT** |
| EPG coverage / two-playlist inventory | **2026-11-09T01:08:13+00:00** | **CURRENT** |
| Stream health | **2026-11-09T00:40:41+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-09T00:40:13+00:00** | **CURRENT** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **998 → 998**
- Latest health failures: **157 → 137**

Historical records are retained in reports/maintenance-history.json.
