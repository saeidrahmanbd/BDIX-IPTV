# Update Report

_Last generated: **2026-11-04 01:49 UTC**_

Source playlist SHA-256: **f9899be34933deceb7b8eb79fc830c4bfbe7e6d1f902e499f09ddc54c9c0d315**

| Metric | Current |
|---|---:|
| Streams | **1090** |
| Active Channel Identities | **680** |
| Active Primary Streams | **680** |
| Bangladesh | **63** |
| India | **327** |
| Backup Stream Entries | **346** |
| IPTV Local Logos | **STALE** |
| IPTV EPG Programme Coverage | **59%** |
| IPTV EPG Mapping | **65.9%** |
| Stream Health Tested | **1090** |
| Stream Health Failures | **110** |
| Persistent Failures | **87** |
| Near-Duplicate URL Families | **2** |
| Audit Blocking Issues | **STALE / UNKNOWN** |
| Pre-Publish Gate | **STALE / UNKNOWN** |
| Pre-Publish Gate Generated | **2026-11-03T09:36:46+00:00** |

## Quality Controls (STALE / UNKNOWN — saved audit values shown for reference)
- Duplicate stream URLs: **STALE / UNKNOWN (last saved: 0)**
- Metadata conflicts (canonical primary scope): **STALE / UNKNOWN (last saved: 0)**
- Same-name / different-ID collisions (canonical primary scope): **STALE / UNKNOWN (last saved: 0)**
- Cross-queue metadata identity variants: **0**
- Cross-queue same-name / different-ID collisions: **4**
- Duplicate primary identities: **STALE / UNKNOWN (last saved: 0)**
- Primary channel-number collisions: **STALE / UNKNOWN (last saved: 0)**
- Primary entries missing channel numbers: **STALE / UNKNOWN (last saved: 0)**
- Logo exceptions: **STALE / UNKNOWN (last saved: 7)**
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
- EPG IDs audited: **741**
- Mapped: **488 (65.9%)**
- Current/future programme coverage: **439/741 (59.2%)**
- No mapping: **253**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (verified against both current playlist inventories)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-03T09:36:46.031762+00:00** | **STALE** |
| EPG coverage / two-playlist inventory | **2026-11-04T01:49:16+00:00** | **CURRENT** |
| Stream health | **2026-11-03T09:37:30+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-03T09:36:46+00:00** | **STALE** |

## Maintenance History
- Records retained: **30**
- Latest entries change: **1090 → 1090**
- Latest health failures: **91 → 110**

Historical records are retained in reports/maintenance-history.json.
