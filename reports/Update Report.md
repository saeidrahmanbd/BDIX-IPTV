# Update Report

_Last generated: **2026-11-12 09:22 UTC**_

Source playlist SHA-256: **9035b8514990d9681dc96a8d7ea6999c2c0777762e2945cdaf2edbd8fdce224e**

| Metric | Current |
|---|---:|
| Streams | **1242** |
| Active Channel Identities | **650** |
| Active Primary Streams | **650** |
| Bangladesh | **63** |
| India | **297** |
| Backup Stream Entries | **420** |
| IPTV Local Logos | **99.9%** |
| IPTV EPG Programme Coverage | **PENDING** |
| IPTV EPG Mapping | **PENDING** |
| Stream Health Tested | **1242** |
| Stream Health Failures | **166** |
| Persistent Failures | **164** |
| Near-Duplicate URL Families | **1** |
| Audit Blocking Issues | **35** |
| Pre-Publish Gate | **BLOCK** |
| Pre-Publish Gate Generated | **2026-11-12T09:22:14+00:00** |

## Quality Controls 
- Duplicate stream URLs: **0**
- Metadata conflicts (canonical primary scope): **0**
- Same-name / different-ID collisions (canonical primary scope): **6**
- Cross-queue metadata identity variants: **1**
- Cross-queue same-name / different-ID collisions: **24**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **13**
- Logo exceptions: **1**
- Malformed EXTINF entries: **0**
- Category block-order issues: **3**
- Alphabetical ordering issues: **18**
- Signed/tokenized URLs: **18**

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
| Playlist audit | **2026-11-12T09:22:14.343472+00:00** | **CURRENT** |
| EPG coverage / two-playlist inventory | **2026-11-12T08:55:48+00:00** | **PENDING — guide missing or freshness not PASS** |
| Stream health | **2026-11-12T09:22:53+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-12T09:22:14+00:00** | **CURRENT** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **1242 → 1242**
- Latest health failures: **168 → 166**

Historical records are retained in reports/maintenance-history.json.
