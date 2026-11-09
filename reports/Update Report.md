# Update Report

_Last generated: **2026-11-09 11:37 UTC**_

Source playlist SHA-256: **c0c115f5324a59094ecc502e03a3358f243ec4f6e74dc583e650e5009bf997b6**

| Metric | Current |
|---|---:|
| Streams | **1069** |
| Active Channel Identities | **584** |
| Active Primary Streams | **584** |
| Bangladesh | **57** |
| India | **294** |
| Backup Stream Entries | **335** |
| IPTV Local Logos | **99.7%** |
| IPTV EPG Programme Coverage | **PENDING** |
| IPTV EPG Mapping | **PENDING** |
| Stream Health Tested | **1069** |
| Stream Health Failures | **180** |
| Persistent Failures | **179** |
| Near-Duplicate URL Families | **2** |
| Audit Blocking Issues | **18** |
| Pre-Publish Gate | **BLOCK** |
| Pre-Publish Gate Generated | **2026-11-09T11:36:42+00:00** |

## Quality Controls 
- Duplicate stream URLs: **0**
- Metadata conflicts (canonical primary scope): **0**
- Same-name / different-ID collisions (canonical primary scope): **1**
- Cross-queue metadata identity variants: **0**
- Cross-queue same-name / different-ID collisions: **3**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **1**
- Primary entries missing channel numbers: **9**
- Logo exceptions: **3**
- Malformed EXTINF entries: **0**
- Category block-order issues: **1**
- Alphabetical ordering issues: **4**
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
- EPG IDs audited: **PENDING — guide not current**
- Mapped: **PENDING — no current validated guide**
- Current/future programme coverage: **PENDING — no current validated guide**
- No mapping: **PENDING — guide not current**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (awaiting a valid, fresh published guide)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-09T11:36:41.777240+00:00** | **CURRENT** |
| EPG coverage / two-playlist inventory | **2026-11-09T09:19:49+00:00** | **PENDING — guide missing or freshness not PASS** |
| Stream health | **2026-11-09T11:37:18+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-09T11:36:42+00:00** | **CURRENT** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **1069 → 1069**
- Latest health failures: **182 → 180**

Historical records are retained in reports/maintenance-history.json.
