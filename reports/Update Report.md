# Update Report

_Last generated: **2026-11-05 08:31 UTC**_

Source playlist SHA-256: **f5795953ab6e9474334bc1dc17149eaf70528a4602c0084f59ecbe44665f78ef**

| Metric | Current |
|---|---:|
| Streams | **1113** |
| Active Channel Identities | **683** |
| Active Primary Streams | **683** |
| Bangladesh | **64** |
| India | **331** |
| Backup Stream Entries | **335** |
| IPTV Local Logos | **99.9%** |
| IPTV EPG Programme Coverage | **57%** |
| IPTV EPG Mapping | **65.3%** |
| Stream Health Tested | **1113** |
| Stream Health Failures | **127** |
| Persistent Failures | **90** |
| Near-Duplicate URL Families | **2** |
| Audit Blocking Issues | **1** |
| Pre-Publish Gate | **BLOCK** |
| Pre-Publish Gate Generated | **2026-11-05T01:45:15+00:00** |

## Quality Controls 
- Duplicate stream URLs: **0**
- Metadata conflicts (canonical primary scope): **0**
- Same-name / different-ID collisions (canonical primary scope): **0**
- Cross-queue metadata identity variants: **0**
- Cross-queue same-name / different-ID collisions: **1**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **0**
- Logo exceptions: **1**
- Malformed EXTINF entries: **0**
- Category block-order issues: **0**
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
- EPG IDs audited: **683**
- Mapped: **446 (65.3%)**
- Current/future programme coverage: **390/683 (57.1%)**
- No mapping: **237**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (verified against both current playlist inventories)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-05T01:45:15.108442+00:00** | **CURRENT** |
| EPG coverage / two-playlist inventory | **2026-11-05T08:30:54+00:00** | **CURRENT** |
| Stream health | **2026-11-05T01:45:44+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-05T01:45:15+00:00** | **CURRENT** |

## Maintenance History
- Records retained: **30**
- Latest entries change: **1113 → 1113**
- Latest health failures: **113 → 127**

Historical records are retained in reports/maintenance-history.json.
