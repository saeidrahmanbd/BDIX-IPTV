# Update Report

_Last generated: **2026-11-06 21:42 UTC**_

Source playlist SHA-256: **92a045f671165942d728082edaac08bdaa83c0320afde042d00ed9b6ea1da67a**

| Metric | Current |
|---|---:|
| Streams | **1121** |
| Active Channel Identities | **655** |
| Active Primary Streams | **655** |
| Bangladesh | **65** |
| India | **311** |
| Backup Stream Entries | **322** |
| IPTV Local Logos | **99.9%** |
| IPTV EPG Programme Coverage | **57%** |
| IPTV EPG Mapping | **63.8%** |
| Stream Health Tested | **1121** |
| Stream Health Failures | **162** |
| Persistent Failures | **135** |
| Near-Duplicate URL Families | **3** |
| Audit Blocking Issues | **13** |
| Pre-Publish Gate | **BLOCK** |
| Pre-Publish Gate Generated | **2026-11-06T16:36:36+00:00** |

## Quality Controls 
- Duplicate stream URLs: **0**
- Metadata conflicts (canonical primary scope): **0**
- Same-name / different-ID collisions (canonical primary scope): **0**
- Cross-queue metadata identity variants: **1**
- Cross-queue same-name / different-ID collisions: **2**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **0**
- Logo exceptions: **1**
- Malformed EXTINF entries: **0**
- Category block-order issues: **12**
- Alphabetical ordering issues: **0**
- Signed/tokenized URLs: **9**

## Safety & Automation
- Stream health is non-destructive and keeps per-URL failure history.
- Backup streams are never automatically deleted because of health failures.
- `New Channels` and `New Backup` are active review queues used by discovery and validation; they are not retired categories.
- Pre-publish gate status: **BLOCK**
- Canonical channel identity index: reports/channel-identity-index.json

## Counting Scope
- **Active Channel Identities / Active Primary Streams** count only canonical playlist groups.
- `New Channels`, `New Backup`, and `Not Playing` are review queues and are excluded from the active-primary count.
- EPG identity/programme coverage is reported only when the published XMLTV is valid, current, and its freshness report is PASS.
- **Backup Stream Entries** count playlist rows, not independent CDN/origin infrastructures. Backup independence is reviewed separately.

## EPG
- EPG IDs audited: **671**
- Mapped: **428 (63.8%)**
- Current/future programme coverage: **380/671 (56.6%)**
- No mapping: **243**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (verified against both current playlist inventories)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-06T16:36:35.958081+00:00** | **CURRENT** |
| EPG coverage / two-playlist inventory | **2026-11-06T21:42:01+00:00** | **CURRENT** |
| Stream health | **2026-11-06T16:37:29+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-06T16:36:36+00:00** | **CURRENT** |

## Maintenance History
- Records retained: **30**
- Latest entries change: **1121 → 1121**
- Latest health failures: **143 → 162**

Historical records are retained in reports/maintenance-history.json.
