# Update Report

_Last generated: **2026-11-28 11:14 UTC**_

Source playlist SHA-256: **77b11e20f1d6d12ac974d1ea5e1940787857026b38d4f3574619dbdb69eb28f3**

| Metric | Current |
|---|---:|
| Streams | **1373** |
| Active Channel Identities | **702** |
| Active Primary Streams | **824** |
| Bangladesh | **67** |
| India | **320** |
| Backup Stream Entries | **489** |
| IPTV Local Logos | **99.4%** |
| IPTV EPG Programme Coverage | **PENDING** |
| IPTV EPG Mapping | **PENDING** |
| Stream Health Tested | **1373** |
| Stream Health Failures | **76** |
| Persistent Failures | **0** |
| Near-Duplicate URL Families | **3** |
| Audit findings (review warnings included) | **148** |
| Pre-Publish Gate | **PASS** |
| Pre-Publish Gate Generated | **2026-11-28T11:13:15+00:00** |

## Quality Controls 
- Duplicate stream URLs: **0**
- Metadata conflicts (canonical primary scope): **0**
- Same-name / different-ID collisions (canonical primary scope): **32**
- Cross-queue metadata identity variants: **0**
- Cross-queue same-name / different-ID collisions: **21**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **125**
- Logo exceptions: **8**
- Malformed EXTINF entries: **0**
- Category block-order issues: **3**
- Alphabetical ordering issues: **12**
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
| Playlist audit | **2026-11-28T11:13:14.671498+00:00** | **CURRENT** |
| EPG coverage / two-playlist inventory | **2026-11-28T10:57:01+00:00** | **PENDING — guide missing or freshness not PASS** |
| Stream health | **2026-11-28T11:14:01+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-28T11:13:15+00:00** | **CURRENT** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **1373 → 1373**
- Latest health failures: **68 → 76**

Historical records are retained in reports/maintenance-history.json.
