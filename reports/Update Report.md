# Update Report

_Last generated: **2026-11-16 07:05 UTC**_

Source playlist SHA-256: **14620d0edd4971c15ff9b314789a11f7853374d0eb5dfb1dcf82e22387078a47**

| Metric | Current |
|---|---:|
| Streams | **1388** |
| Active Channel Identities | **712** |
| Active Primary Streams | **712** |
| Bangladesh | **66** |
| India | **302** |
| Backup Stream Entries | **473** |
| IPTV Local Logos | **STALE** |
| IPTV EPG Programme Coverage | **52%** |
| IPTV EPG Mapping | **59.3%** |
| Stream Health Tested | **STALE** |
| Stream Health Failures | **STALE** |
| Persistent Failures | **STALE** |
| Near-Duplicate URL Families | **STALE / UNKNOWN** |
| Audit findings (review warnings included) | **STALE / UNKNOWN** |
| Pre-Publish Gate | **STALE / UNKNOWN** |
| Pre-Publish Gate Generated | **2026-11-16T02:50:59+00:00** |

## Quality Controls (STALE / UNKNOWN — saved audit values shown for reference)
- Duplicate stream URLs: **STALE / UNKNOWN (last saved: 0)**
- Metadata conflicts (canonical primary scope): **STALE / UNKNOWN (last saved: 0)**
- Same-name / different-ID collisions (canonical primary scope): **STALE / UNKNOWN (last saved: 0)**
- Cross-queue metadata identity variants: **2**
- Cross-queue same-name / different-ID collisions: **12**
- Duplicate primary identities: **STALE / UNKNOWN (last saved: 0)**
- Primary channel-number collisions: **STALE / UNKNOWN (last saved: 0)**
- Primary entries missing channel numbers: **STALE / UNKNOWN (last saved: 22)**
- Logo exceptions: **STALE / UNKNOWN (last saved: 0)**
- Malformed EXTINF entries: **STALE / UNKNOWN (last saved: 0)**
- Category block-order issues: **STALE / UNKNOWN (last saved: 36)**
- Alphabetical ordering issues: **STALE / UNKNOWN (last saved: 70)**
- Signed/tokenized URLs: **STALE / UNKNOWN (last saved: 12)**

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
- EPG IDs audited: **712**
- Mapped: **422 (59.3%)**
- Current/future programme coverage: **374/712 (52.5%)**
- No mapping: **290**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (verified against both current playlist inventories)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-16T02:50:59.144515+00:00** | **STALE** |
| EPG coverage / two-playlist inventory | **2026-11-16T07:05:29+00:00** | **CURRENT** |
| Stream health | **2026-11-16T02:51:42+00:00** | **STALE** |
| Pre-publish gate | **2026-11-16T02:50:59+00:00** | **STALE** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **1284 → 1298**
- Latest health failures: **189 → 200**

Historical records are retained in reports/maintenance-history.json.
