# Update Report

_Last generated: **2026-11-07 04:32 UTC**_

Source playlist SHA-256: **b21a4dad6ee749428f415bb044c876dc88c6e8cada2c5e50c155b3c9397a16ff**

| Metric | Current |
|---|---:|
| Streams | **1010** |
| Active Channel Identities | **659** |
| Active Primary Streams | **659** |
| Bangladesh | **65** |
| India | **315** |
| Backup Stream Entries | **351** |
| IPTV Local Logos | **99.9%** |
| IPTV EPG Programme Coverage | **PENDING** |
| IPTV EPG Mapping | **PENDING** |
| Stream Health Tested | **1010** |
| Stream Health Failures | **47** |
| Persistent Failures | **46** |
| Near-Duplicate URL Families | **3** |
| Audit Blocking Issues | **16** |
| Pre-Publish Gate | **BLOCK** |
| Pre-Publish Gate Generated | **2026-11-07T04:31:40+00:00** |

## Quality Controls 
- Duplicate stream URLs: **0**
- Metadata conflicts (canonical primary scope): **0**
- Same-name / different-ID collisions (canonical primary scope): **1**
- Cross-queue metadata identity variants: **0**
- Cross-queue same-name / different-ID collisions: **1**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **1**
- Primary entries missing channel numbers: **10**
- Logo exceptions: **1**
- Malformed EXTINF entries: **0**
- Category block-order issues: **0**
- Alphabetical ordering issues: **4**
- Signed/tokenized URLs: **9**

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
| Playlist audit | **2026-11-07T04:31:40.392119+00:00** | **CURRENT** |
| EPG coverage / two-playlist inventory | **2026-11-06T21:42:01+00:00** | **PENDING — guide missing or freshness not PASS** |
| Stream health | **2026-11-07T04:32:01+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-07T04:31:40+00:00** | **CURRENT** |

## Maintenance History
- Records retained: **30**
- Latest entries change: **1007 → 1010**
- Latest health failures: **48 → 47**

Historical records are retained in reports/maintenance-history.json.
