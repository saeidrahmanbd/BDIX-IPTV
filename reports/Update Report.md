# Update Report

_Last generated: **2026-11-06 12:25 UTC**_

Source playlist SHA-256: **c1e170f5553fb67bfd7966dc803db253fd14b6e20a94375f13cf7f6b50710bc0**

| Metric | Current |
|---|---:|
| Streams | **1065** |
| Active Channel Identities | **676** |
| Active Primary Streams | **676** |
| Bangladesh | **65** |
| India | **323** |
| Backup Stream Entries | **304** |
| IPTV Local Logos | **99.9%** |
| IPTV EPG Programme Coverage | **PENDING** |
| IPTV EPG Mapping | **PENDING** |
| Stream Health Tested | **1065** |
| Stream Health Failures | **105** |
| Persistent Failures | **98** |
| Near-Duplicate URL Families | **3** |
| Audit Blocking Issues | **42** |
| Pre-Publish Gate | **BLOCK** |
| Pre-Publish Gate Generated | **2026-11-06T12:24:35+00:00** |

## Quality Controls 
- Duplicate stream URLs: **0**
- Metadata conflicts (canonical primary scope): **0**
- Same-name / different-ID collisions (canonical primary scope): **0**
- Cross-queue metadata identity variants: **1**
- Cross-queue same-name / different-ID collisions: **0**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **39**
- Logo exceptions: **1**
- Malformed EXTINF entries: **0**
- Category block-order issues: **1**
- Alphabetical ordering issues: **1**
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
- EPG IDs audited: **PENDING — guide not current**
- Mapped: **PENDING — no current validated guide**
- Current/future programme coverage: **PENDING — no current validated guide**
- No mapping: **PENDING — guide not current**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (awaiting a valid, fresh published guide)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-06T12:24:35.139245+00:00** | **CURRENT** |
| EPG coverage / two-playlist inventory | **2026-11-06T03:17:39+00:00** | **PENDING — guide missing or freshness not PASS** |
| Stream health | **2026-11-06T12:25:10+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-06T12:24:35+00:00** | **CURRENT** |

## Maintenance History
- Records retained: **30**
- Latest entries change: **1065 → 1065**
- Latest health failures: **111 → 105**

Historical records are retained in reports/maintenance-history.json.
