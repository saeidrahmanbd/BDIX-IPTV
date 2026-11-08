# Update Report

_Last generated: **2026-11-08 02:50 UTC**_

Source playlist SHA-256: **6da7347dcf4d355f3469116aea87f011f70e2699cfc38f2c08ff136138f1680e**

| Metric | Current |
|---|---:|
| Streams | **1004** |
| Active Channel Identities | **674** |
| Active Primary Streams | **674** |
| Bangladesh | **65** |
| India | **322** |
| Backup Stream Entries | **330** |
| IPTV Local Logos | **STALE** |
| IPTV EPG Programme Coverage | **56%** |
| IPTV EPG Mapping | **63.5%** |
| Stream Health Tested | **1004** |
| Stream Health Failures | **58** |
| Persistent Failures | **47** |
| Near-Duplicate URL Families | **3** |
| Audit Blocking Issues | **STALE / UNKNOWN** |
| Pre-Publish Gate | **STALE / UNKNOWN** |
| Pre-Publish Gate Generated | **2026-11-07T21:51:06+00:00** |

## Quality Controls (STALE / UNKNOWN — saved audit values shown for reference)
- Duplicate stream URLs: **STALE / UNKNOWN (last saved: 0)**
- Metadata conflicts (canonical primary scope): **STALE / UNKNOWN (last saved: 0)**
- Same-name / different-ID collisions (canonical primary scope): **STALE / UNKNOWN (last saved: 0)**
- Cross-queue metadata identity variants: **0**
- Cross-queue same-name / different-ID collisions: **1**
- Duplicate primary identities: **STALE / UNKNOWN (last saved: 0)**
- Primary channel-number collisions: **STALE / UNKNOWN (last saved: 0)**
- Primary entries missing channel numbers: **STALE / UNKNOWN (last saved: 0)**
- Logo exceptions: **STALE / UNKNOWN (last saved: 0)**
- Malformed EXTINF entries: **STALE / UNKNOWN (last saved: 0)**
- Category block-order issues: **STALE / UNKNOWN (last saved: 0)**
- Alphabetical ordering issues: **STALE / UNKNOWN (last saved: 1)**
- Signed/tokenized URLs: **STALE / UNKNOWN (last saved: 8)**

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
- EPG IDs audited: **674**
- Mapped: **428 (63.5%)**
- Current/future programme coverage: **380/674 (56.4%)**
- No mapping: **246**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (verified against both current playlist inventories)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-07T21:51:05.678483+00:00** | **STALE** |
| EPG coverage / two-playlist inventory | **2026-11-08T02:50:41+00:00** | **CURRENT** |
| Stream health | **2026-11-07T21:51:26+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-07T21:51:06+00:00** | **STALE** |

## Maintenance History
- Recent records displayed: **30** (latest 30 entries; the stored history is retained separately)
- Latest entries change: **1005 → 1004**
- Latest health failures: **54 → 58**

Historical records are retained in reports/maintenance-history.json.
