# Update Report

_Last generated: **2026-11-07 05:05 UTC**_

Source playlist SHA-256: **84c02ef014377e5b6ba95a227f9783389650950895cfd82aece9c12b369a6a98**

| Metric | Current |
|---|---:|
| Streams | **1005** |
| Active Channel Identities | **674** |
| Active Primary Streams | **674** |
| Bangladesh | **65** |
| India | **322** |
| Backup Stream Entries | **331** |
| IPTV Local Logos | **100.0%** |
| IPTV EPG Programme Coverage | **PENDING** |
| IPTV EPG Mapping | **PENDING** |
| Stream Health Tested | **1005** |
| Stream Health Failures | **71** |
| Persistent Failures | **46** |
| Near-Duplicate URL Families | **3** |
| Audit Blocking Issues | **0** |
| Pre-Publish Gate | **PASS** |
| Pre-Publish Gate Generated | **2026-11-07T05:04:29+00:00** |

## Quality Controls 
- Duplicate stream URLs: **0**
- Metadata conflicts (canonical primary scope): **0**
- Same-name / different-ID collisions (canonical primary scope): **0**
- Cross-queue metadata identity variants: **0**
- Cross-queue same-name / different-ID collisions: **0**
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
- EPG IDs audited: **PENDING — guide not current**
- Mapped: **PENDING — no current validated guide**
- Current/future programme coverage: **PENDING — no current validated guide**
- No mapping: **PENDING — guide not current**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (awaiting a valid, fresh published guide)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-07T05:04:28.780064+00:00** | **CURRENT** |
| EPG coverage / two-playlist inventory | **2026-11-06T21:42:01+00:00** | **PENDING — guide missing or freshness not PASS** |
| Stream health | **2026-11-07T05:05:06+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-07T05:04:29+00:00** | **CURRENT** |

## Maintenance History
- Records retained: **30**
- Latest entries change: **1005 → 1005**
- Latest health failures: **50 → 71**

Historical records are retained in reports/maintenance-history.json.
