# Update Report

_Last generated: **2026-10-31 01:07 UTC**_

Source playlist SHA-256: **2007da9d83805d6114936a5ea3b25f3bd16f4685fb4869fabca9f3da8a4712d4**

| Metric | Current |
|---|---:|
| Streams | **1161** |
| Active Channel Identities | **655** |
| Active Primary Streams | **655** |
| Bangladesh | **64** |
| India | **328** |
| Backup Stream Entries | **366** |
| IPTV Local Logos | **99.8%** |
| IPTV EPG Programme Coverage | **PENDING** |
| IPTV EPG Mapping | **PENDING** |
| Stream Health Tested | **1161** |
| Stream Health Failures | **167** |
| Persistent Failures | **131** |
| Near-Duplicate URL Families | **2** |
| Audit Blocking Issues | **0** |
| Pre-Publish Gate | **UNKNOWN** |
| Pre-Publish Gate Generated | **2026-10-31T01:06:34+00:00** |

## Quality Controls 
- Duplicate stream URLs: **0**
- Metadata conflicts (canonical primary scope): **0**
- Same-name / different-ID collisions (canonical primary scope): **0**
- Cross-queue metadata identity variants: **1**
- Cross-queue same-name / different-ID collisions: **4**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **0**
- Logo exceptions: **0**
- Malformed EXTINF entries: **0**
- Category block-order issues: **0**
- Alphabetical ordering issues: **0**
- Signed/tokenized URLs: **10**

## Safety & Automation
- Stream health is non-destructive and keeps per-URL failure history.
- Backup streams are never automatically deleted because of health failures.
- `New Channels` and `New Backup` are active review queues used by discovery and validation; they are not retired categories.
- Pre-publish gate status: **UNKNOWN**
- Canonical channel identity index: reports/channel-identity-index.json

## Counting Scope
- **Active Channel Identities / Active Primary Streams** count only canonical playlist groups.
- `New Channels`, `New Backup`, and `Not Playing` are review queues and are excluded from the active-primary count.
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
| Playlist audit | **2026-10-31T01:06:34.574472+00:00** | **CURRENT** |
| EPG coverage / three-playlist inventory | **2026-10-30T11:14:23+00:00** | **PENDING — guide missing or freshness not PASS** |
| Stream health | **2026-10-31T01:07:21+00:00** | **CURRENT** |
| Pre-publish gate | **2026-10-31T01:06:34+00:00** | **CURRENT** |

## Maintenance History
- Records retained: **30**
- Latest entries change: **1160 → 1161**
- Latest health failures: **138 → 167**

Historical records are retained in reports/maintenance-history.json.
