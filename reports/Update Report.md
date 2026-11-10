# Update Report

_Last generated: **2026-11-10 13:07 UTC**_

Source playlist SHA-256: **810bd296df25477c8020711267bf2062f97b9386ab54cd783171bac96e9d7bc0**

| Metric | Current |
|---|---:|
| Streams | **1151** |
| Active Channel Identities | **590** |
| Active Primary Streams | **590** |
| Bangladesh | **54** |
| India | **289** |
| Backup Stream Entries | **390** |
| IPTV Local Logos | **STALE** |
| IPTV EPG Programme Coverage | **53%** |
| IPTV EPG Mapping | **61.0%** |
| Stream Health Tested | **STALE** |
| Stream Health Failures | **STALE** |
| Persistent Failures | **STALE** |
| Near-Duplicate URL Families | **STALE / UNKNOWN** |
| Audit Blocking Issues | **STALE / UNKNOWN** |
| Pre-Publish Gate | **STALE / UNKNOWN** |
| Pre-Publish Gate Generated | **2026-11-10T09:57:03+00:00** |

## Quality Controls (STALE / UNKNOWN — saved audit values shown for reference)
- Duplicate stream URLs: **STALE / UNKNOWN (last saved: 0)**
- Metadata conflicts (canonical primary scope): **STALE / UNKNOWN (last saved: 0)**
- Same-name / different-ID collisions (canonical primary scope): **STALE / UNKNOWN (last saved: 0)**
- Cross-queue metadata identity variants: **0**
- Cross-queue same-name / different-ID collisions: **1**
- Duplicate primary identities: **STALE / UNKNOWN (last saved: 0)**
- Primary channel-number collisions: **STALE / UNKNOWN (last saved: 0)**
- Primary entries missing channel numbers: **STALE / UNKNOWN (last saved: 6)**
- Logo exceptions: **STALE / UNKNOWN (last saved: 1)**
- Malformed EXTINF entries: **STALE / UNKNOWN (last saved: 1)**
- Category block-order issues: **STALE / UNKNOWN (last saved: 1)**
- Alphabetical ordering issues: **STALE / UNKNOWN (last saved: 4)**
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
- EPG IDs audited: **590**
- Mapped: **360 (61.0%)**
- Current/future programme coverage: **311/590 (52.7%)**
- No mapping: **230**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (verified against both current playlist inventories)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-10T09:57:03.261070+00:00** | **STALE** |
| EPG coverage / two-playlist inventory | **2026-11-10T13:07:49+00:00** | **CURRENT** |
| Stream health | **2026-11-10T09:57:42+00:00** | **STALE** |
| Pre-publish gate | **2026-11-10T09:57:03+00:00** | **STALE** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **1066 → 1121**
- Latest health failures: **195 → 199**

Historical records are retained in reports/maintenance-history.json.
