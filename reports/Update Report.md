# Update Report

_Last generated: **2026-11-13 08:39 UTC**_

Source playlist SHA-256: **006cd670ecdde84fe0481c6405214f3fb618e234a7abe12f8bce3f1553bb6c8d**

| Metric | Current |
|---|---:|
| Streams | **1280** |
| Active Channel Identities | **646** |
| Active Primary Streams | **646** |
| Bangladesh | **64** |
| India | **293** |
| Backup Stream Entries | **424** |
| IPTV Local Logos | **99.7%** |
| IPTV EPG Programme Coverage | **PENDING** |
| IPTV EPG Mapping | **PENDING** |
| Stream Health Tested | **1280** |
| Stream Health Failures | **202** |
| Persistent Failures | **197** |
| Near-Duplicate URL Families | **1** |
| Audit Blocking Issues | **107** |
| Pre-Publish Gate | **PASS** |
| Pre-Publish Gate Generated | **2026-11-13T08:39:06+00:00** |

## Quality Controls 
- Duplicate stream URLs: **0**
- Metadata conflicts (canonical primary scope): **0**
- Same-name / different-ID collisions (canonical primary scope): **6**
- Cross-queue metadata identity variants: **2**
- Cross-queue same-name / different-ID collisions: **26**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **13**
- Logo exceptions: **4**
- Malformed EXTINF entries: **0**
- Category block-order issues: **31**
- Alphabetical ordering issues: **59**
- Signed/tokenized URLs: **18**

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
| Playlist audit | **2026-11-13T08:39:06.090267+00:00** | **CURRENT** |
| EPG coverage / two-playlist inventory | **2026-11-13T01:32:49+00:00** | **PENDING — guide missing or freshness not PASS** |
| Stream health | **2026-11-13T08:39:54+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-13T08:39:06+00:00** | **CURRENT** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **1280 → 1280**
- Latest health failures: **204 → 202**

Historical records are retained in reports/maintenance-history.json.
