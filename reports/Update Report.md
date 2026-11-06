# Update Report

_Last generated: **2026-11-06 14:12 UTC**_

Source playlist SHA-256: **9984e08ae9e3a60145c9376882c244a81d0f8526b9794a3978714b5dab6d9ed9**

| Metric | Current |
|---|---:|
| Streams | **1121** |
| Active Channel Identities | **656** |
| Active Primary Streams | **656** |
| Bangladesh | **65** |
| India | **312** |
| Backup Stream Entries | **321** |
| IPTV Local Logos | **STALE** |
| IPTV EPG Programme Coverage | **57%** |
| IPTV EPG Mapping | **63.8%** |
| Stream Health Tested | **STALE** |
| Stream Health Failures | **STALE** |
| Persistent Failures | **STALE** |
| Near-Duplicate URL Families | **STALE / UNKNOWN** |
| Audit Blocking Issues | **STALE / UNKNOWN** |
| Pre-Publish Gate | **STALE / UNKNOWN** |
| Pre-Publish Gate Generated | **2026-11-06T13:30:25+00:00** |

## Quality Controls (STALE / UNKNOWN — saved audit values shown for reference)
- Duplicate stream URLs: **STALE / UNKNOWN (last saved: 0)**
- Metadata conflicts (canonical primary scope): **STALE / UNKNOWN (last saved: 0)**
- Same-name / different-ID collisions (canonical primary scope): **STALE / UNKNOWN (last saved: 0)**
- Cross-queue metadata identity variants: **1**
- Cross-queue same-name / different-ID collisions: **2**
- Duplicate primary identities: **STALE / UNKNOWN (last saved: 0)**
- Primary channel-number collisions: **STALE / UNKNOWN (last saved: 0)**
- Primary entries missing channel numbers: **STALE / UNKNOWN (last saved: 0)**
- Logo exceptions: **STALE / UNKNOWN (last saved: 2)**
- Malformed EXTINF entries: **STALE / UNKNOWN (last saved: 0)**
- Category block-order issues: **STALE / UNKNOWN (last saved: 0)**
- Alphabetical ordering issues: **STALE / UNKNOWN (last saved: 0)**
- Signed/tokenized URLs: **STALE / UNKNOWN (last saved: 9)**

## Safety & Automation
- Stream health is non-destructive and keeps per-URL failure history.
- Backup streams are never automatically deleted because of health failures.
- `New Channels` and `New Backup` are active review queues used by discovery and validation; they are not retired categories.
- Pre-publish gate status: **STALE / UNKNOWN**
- Canonical channel identity index: reports/channel-identity-index.json

## Counting Scope
- **Active Channel Identities / Active Primary Streams** count only canonical playlist groups.
- `New Channels`, `New Backup`, and `Not Playing` are review queues and are excluded from the active-primary count.
- EPG identity/programme coverage is reported only when the published XMLTV is valid, current, and its freshness report is PASS.
- **Backup Stream Entries** count playlist rows, not independent CDN/origin infrastructures. Backup independence is reviewed separately.

## EPG
- EPG IDs audited: **672**
- Mapped: **429 (63.8%)**
- Current/future programme coverage: **386/672 (57.4%)**
- No mapping: **243**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (verified against both current playlist inventories)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-06T13:30:25.529472+00:00** | **STALE** |
| EPG coverage / two-playlist inventory | **2026-11-06T14:12:26+00:00** | **CURRENT** |
| Stream health | **2026-11-06T13:30:57+00:00** | **STALE** |
| Pre-publish gate | **2026-11-06T13:30:25+00:00** | **STALE** |

## Maintenance History
- Records retained: **30**
- Latest entries change: **1120 → 1120**
- Latest health failures: **135 → 139**

Historical records are retained in reports/maintenance-history.json.
