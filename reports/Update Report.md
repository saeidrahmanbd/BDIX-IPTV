# Update Report

_Last generated: **2026-11-13 18:33 UTC**_

Source playlist SHA-256: **18961862f7ba2836ff0f867724779b2bdd3afbba16d9882faf394eca6f55b469**

| Metric | Current |
|---|---:|
| Streams | **1284** |
| Active Channel Identities | **646** |
| Active Primary Streams | **646** |
| Bangladesh | **64** |
| India | **293** |
| Backup Stream Entries | **424** |
| IPTV Local Logos | **STALE** |
| IPTV EPG Programme Coverage | **51%** |
| IPTV EPG Mapping | **58.7%** |
| Stream Health Tested | **STALE** |
| Stream Health Failures | **STALE** |
| Persistent Failures | **STALE** |
| Near-Duplicate URL Families | **STALE / UNKNOWN** |
| Audit Blocking Issues | **STALE / UNKNOWN** |
| Pre-Publish Gate | **STALE / UNKNOWN** |
| Pre-Publish Gate Generated | **2026-11-13T08:50:16+00:00** |

## Quality Controls (STALE / UNKNOWN — saved audit values shown for reference)
- Duplicate stream URLs: **STALE / UNKNOWN (last saved: 0)**
- Metadata conflicts (canonical primary scope): **STALE / UNKNOWN (last saved: 0)**
- Same-name / different-ID collisions (canonical primary scope): **STALE / UNKNOWN (last saved: 6)**
- Cross-queue metadata identity variants: **2**
- Cross-queue same-name / different-ID collisions: **26**
- Duplicate primary identities: **STALE / UNKNOWN (last saved: 0)**
- Primary channel-number collisions: **STALE / UNKNOWN (last saved: 0)**
- Primary entries missing channel numbers: **STALE / UNKNOWN (last saved: 13)**
- Logo exceptions: **STALE / UNKNOWN (last saved: 4)**
- Malformed EXTINF entries: **STALE / UNKNOWN (last saved: 0)**
- Category block-order issues: **STALE / UNKNOWN (last saved: 31)**
- Alphabetical ordering issues: **STALE / UNKNOWN (last saved: 59)**
- Signed/tokenized URLs: **STALE / UNKNOWN (last saved: 18)**

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
- EPG IDs audited: **646**
- Mapped: **379 (58.7%)**
- Current/future programme coverage: **328/646 (50.8%)**
- No mapping: **267**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (verified against both current playlist inventories)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-13T08:50:15.218356+00:00** | **STALE** |
| EPG coverage / two-playlist inventory | **2026-11-13T18:33:43+00:00** | **CURRENT** |
| Stream health | **2026-11-13T08:51:00+00:00** | **STALE** |
| Pre-publish gate | **2026-11-13T08:50:16+00:00** | **STALE** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **1280 → 1280**
- Latest health failures: **204 → 207**

Historical records are retained in reports/maintenance-history.json.
