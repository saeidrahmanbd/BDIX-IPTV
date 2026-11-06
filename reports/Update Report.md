# Update Report

_Last generated: **2026-11-06 14:21 UTC**_

Source playlist SHA-256: **d8ac07ce135cde8d024e6a4945c377175132e290d02e275bcd0e376fdddc692e**

| Metric | Current |
|---|---:|
| Streams | **1121** |
| Active Channel Identities | **656** |
| Active Primary Streams | **656** |
| Bangladesh | **65** |
| India | **312** |
| Backup Stream Entries | **321** |
| IPTV Local Logos | **99.9%** |
| IPTV EPG Programme Coverage | **PENDING** |
| IPTV EPG Mapping | **PENDING** |
| Stream Health Tested | **1121** |
| Stream Health Failures | **146** |
| Persistent Failures | **127** |
| Near-Duplicate URL Families | **3** |
| Audit Blocking Issues | **1** |
| Pre-Publish Gate | **BLOCK** |
| Pre-Publish Gate Generated | **2026-11-06T14:20:46+00:00** |

## Quality Controls 
- Duplicate stream URLs: **0**
- Metadata conflicts (canonical primary scope): **0**
- Same-name / different-ID collisions (canonical primary scope): **0**
- Cross-queue metadata identity variants: **1**
- Cross-queue same-name / different-ID collisions: **2**
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
- EPG IDs audited: **PENDING — guide not current**
- Mapped: **PENDING — no current validated guide**
- Current/future programme coverage: **PENDING — no current validated guide**
- No mapping: **PENDING — guide not current**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (awaiting a valid, fresh published guide)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-06T14:20:45.871940+00:00** | **CURRENT** |
| EPG coverage / two-playlist inventory | **2026-11-06T14:12:26+00:00** | **PENDING — guide missing or freshness not PASS** |
| Stream health | **2026-11-06T14:21:25+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-06T14:20:46+00:00** | **CURRENT** |

## Maintenance History
- Records retained: **30**
- Latest entries change: **1120 → 1121**
- Latest health failures: **139 → 146**

Historical records are retained in reports/maintenance-history.json.
