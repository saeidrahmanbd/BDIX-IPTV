# Update Report

_Last generated: **2026-11-26 10:39 UTC**_

Source playlist SHA-256: **6ed75613aa2965cc341a0d144242ed4fab07eebdd8f1175ab003c66d0f701a97**

| Metric | Current |
|---|---:|
| Streams | **1143** |
| Active Channel Identities | **708** |
| Active Primary Streams | **708** |
| Bangladesh | **67** |
| India | **322** |
| Backup Stream Entries | **434** |
| IPTV Local Logos | **100.0%** |
| IPTV EPG Programme Coverage | **PENDING** |
| IPTV EPG Mapping | **PENDING** |
| Stream Health Tested | **1143** |
| Stream Health Failures | **73** |
| Persistent Failures | **1** |
| Near-Duplicate URL Families | **1** |
| Audit findings (review warnings included) | **0** |
| Pre-Publish Gate | **PASS** |
| Pre-Publish Gate Generated | **2026-11-26T10:38:42+00:00** |

## Quality Controls 
- Duplicate stream URLs: **0**
- Metadata conflicts (canonical primary scope): **0**
- Same-name / different-ID collisions (canonical primary scope): **0**
- Cross-queue metadata identity variants: **0**
- Cross-queue same-name / different-ID collisions: **4**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **0**
- Logo exceptions: **0**
- Malformed EXTINF entries: **0**
- Category block-order issues: **0**
- Alphabetical ordering issues: **0**
- Signed/tokenized URLs: **14**

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
- EPG IDs audited: **PENDING — guide not current**
- Mapped: **PENDING — no current validated guide**
- Current/future programme coverage: **PENDING — no current validated guide**
- No mapping: **PENDING — guide not current**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (awaiting a valid, fresh published guide)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-26T10:38:41.939503+00:00** | **CURRENT** |
| EPG coverage / two-playlist inventory | **2026-11-26T10:37:30+00:00** | **PENDING — guide missing or freshness not PASS** |
| Stream health | **2026-11-26T10:39:38+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-26T10:38:42+00:00** | **CURRENT** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **1430 → 1143**
- Latest health failures: **275 → 73**

Historical records are retained in reports/maintenance-history.json.
