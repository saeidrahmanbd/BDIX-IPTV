# Update Report

_Last generated: **2026-11-11 15:01 UTC**_

Source playlist SHA-256: **0923016ca9694c93b3ec171f3ceb07b921cbf2187a7858070c4154aaeb354cb7**

| Metric | Current |
|---|---:|
| Streams | **1391** |
| Active Channel Identities | **733** |
| Active Primary Streams | **736** |
| Bangladesh | **59** |
| India | **304** |
| Backup Stream Entries | **463** |
| IPTV Local Logos | **96.7%** |
| IPTV EPG Programme Coverage | **PENDING** |
| IPTV EPG Mapping | **PENDING** |
| Stream Health Tested | **1391** |
| Stream Health Failures | **237** |
| Persistent Failures | **178** |
| Near-Duplicate URL Families | **2** |
| Audit Blocking Issues | **177** |
| Pre-Publish Gate | **BLOCK** |
| Pre-Publish Gate Generated | **2026-11-11T14:59:54+00:00** |

## Quality Controls 
- Duplicate stream URLs: **0**
- Metadata conflicts (canonical primary scope): **0**
- Same-name / different-ID collisions (canonical primary scope): **3**
- Cross-queue metadata identity variants: **1**
- Cross-queue same-name / different-ID collisions: **24**
- Duplicate primary identities: **1**
- Primary channel-number collisions: **2**
- Primary entries missing channel numbers: **0**
- Logo exceptions: **46**
- Malformed EXTINF entries: **0**
- Category block-order issues: **30**
- Alphabetical ordering issues: **98**
- Signed/tokenized URLs: **26**

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
| Playlist audit | **2026-11-11T14:59:53.689044+00:00** | **CURRENT** |
| EPG coverage / two-playlist inventory | **2026-11-11T12:51:58+00:00** | **PENDING — guide missing or freshness not PASS** |
| Stream health | **2026-11-11T15:01:04+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-11T14:59:54+00:00** | **CURRENT** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **1143 → 1391**
- Latest health failures: **190 → 237**

Historical records are retained in reports/maintenance-history.json.
