# Update Report

_Last generated: **2026-11-21 07:19 UTC**_

Source playlist SHA-256: **0e135710f0964eb757aa03c22ce16c8b1d48cad03639d48f28903aadee255a73**

| Metric | Current |
|---|---:|
| Streams | **1389** |
| Active Channel Identities | **694** |
| Active Primary Streams | **694** |
| Bangladesh | **70** |
| India | **299** |
| Backup Stream Entries | **443** |
| IPTV Local Logos | **STALE** |
| IPTV EPG Programme Coverage | **55%** |
| IPTV EPG Mapping | **62.1%** |
| Stream Health Tested | **1389** |
| Stream Health Failures | **239** |
| Persistent Failures | **51** |
| Near-Duplicate URL Families | **1** |
| Audit findings (review warnings included) | **STALE / UNKNOWN** |
| Pre-Publish Gate | **STALE / UNKNOWN** |
| Pre-Publish Gate Generated | **2026-11-21T04:22:45+00:00** |

## Quality Controls (STALE / UNKNOWN — saved audit values shown for reference)
- Duplicate stream URLs: **STALE / UNKNOWN (last saved: 0)**
- Metadata conflicts (canonical primary scope): **STALE / UNKNOWN (last saved: 0)**
- Same-name / different-ID collisions (canonical primary scope): **STALE / UNKNOWN (last saved: 0)**
- Cross-queue metadata identity variants: **10**
- Cross-queue same-name / different-ID collisions: **9**
- Duplicate primary identities: **STALE / UNKNOWN (last saved: 0)**
- Primary channel-number collisions: **STALE / UNKNOWN (last saved: 0)**
- Primary entries missing channel numbers: **STALE / UNKNOWN (last saved: 0)**
- Logo exceptions: **STALE / UNKNOWN (last saved: 0)**
- Malformed EXTINF entries: **STALE / UNKNOWN (last saved: 0)**
- Category block-order issues: **STALE / UNKNOWN (last saved: 4)**
- Alphabetical ordering issues: **STALE / UNKNOWN (last saved: 1)**
- Signed/tokenized URLs: **STALE / UNKNOWN (last saved: 11)**

## Safety & Automation
- Stream health is non-destructive and keeps per-URL failure history.
- Backup streams are never automatically deleted because of health failures.
- `Backup` stores alternate streams; `Review`, `New Channels`, and `New Backups` are review-only queues and are excluded from Xtream.
- Pre-publish gate status: **STALE / UNKNOWN**
- Canonical channel identity index: reports/channel-identity-index.json

## Counting Scope
- **Active Channel Identities / Active Primary Streams** count only canonical playlist groups.
- `Backup`, `Review`, `New Channels`, and `New Backups` are excluded from the active-primary count.
- EPG identity/programme coverage is reported only when the published XMLTV is valid, current, and its freshness report is PASS.
- **Backup Stream Entries** count playlist rows, not independent CDN/origin infrastructures. Backup independence is reviewed separately.

## EPG
- EPG IDs audited: **694**
- Mapped: **431 (62.1%)**
- Current/future programme coverage: **383/694 (55.2%)**
- No mapping: **263**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (verified against both current playlist inventories)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-21T04:22:44.779824+00:00** | **STALE** |
| EPG coverage / two-playlist inventory | **2026-11-21T07:19:38+00:00** | **CURRENT** |
| Stream health | **2026-11-21T04:23:43+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-21T04:22:45+00:00** | **STALE** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **1394 → 1389**
- Latest health failures: **227 → 239**

Historical records are retained in reports/maintenance-history.json.
