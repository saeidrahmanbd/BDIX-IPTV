# Update Report

_Last generated: **2026-11-01 08:38 UTC**_

Source playlist SHA-256: **5fd765d4d08348ea4786ab3f7b7d7135e495a80eb431b7b57f842601e3bbf70f**

| Metric | Current |
|---|---:|
| Streams | **1114** |
| Active Channel Identities | **640** |
| Active Primary Streams | **640** |
| Bangladesh | **61** |
| India | **324** |
| Backup Stream Entries | **313** |
| IPTV Local Logos | **STALE** |
| IPTV EPG Programme Coverage | **PENDING** |
| IPTV EPG Mapping | **PENDING** |
| Stream Health Tested | **STALE** |
| Stream Health Failures | **STALE** |
| Persistent Failures | **STALE** |
| Near-Duplicate URL Families | **STALE / UNKNOWN** |
| Audit Blocking Issues | **STALE / UNKNOWN** |
| Pre-Publish Gate | **STALE / UNKNOWN** |
| Pre-Publish Gate Generated | **2026-11-01T01:11:35+00:00** |

## Quality Controls (STALE / UNKNOWN — saved audit values shown for reference)
- Duplicate stream URLs: **STALE / UNKNOWN (last saved: 0)**
- Metadata conflicts (canonical primary scope): **STALE / UNKNOWN (last saved: 0)**
- Same-name / different-ID collisions (canonical primary scope): **STALE / UNKNOWN (last saved: 0)**
- Cross-queue metadata identity variants: **1**
- Cross-queue same-name / different-ID collisions: **3**
- Duplicate primary identities: **STALE / UNKNOWN (last saved: 0)**
- Primary channel-number collisions: **STALE / UNKNOWN (last saved: 0)**
- Primary entries missing channel numbers: **STALE / UNKNOWN (last saved: 0)**
- Logo exceptions: **STALE / UNKNOWN (last saved: 0)**
- Malformed EXTINF entries: **STALE / UNKNOWN (last saved: 0)**
- Category block-order issues: **STALE / UNKNOWN (last saved: 0)**
- Alphabetical ordering issues: **STALE / UNKNOWN (last saved: 0)**
- Signed/tokenized URLs: **STALE / UNKNOWN (last saved: 10)**

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
- EPG IDs audited: **PENDING — guide not current**
- Mapped: **PENDING — no current validated guide**
- Current/future programme coverage: **PENDING — no current validated guide**
- No mapping: **PENDING — guide not current**
- EPG metric scope: **IPTV-Playlist.m3u published-guide row (awaiting a valid, fresh published guide)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-01T01:11:34.614764+00:00** | **STALE** |
| EPG coverage / three-playlist inventory | **2026-11-01T08:38:13+00:00** | **PENDING — guide missing or freshness not PASS** |
| Stream health | **2026-11-01T01:12:25+00:00** | **STALE** |
| Pre-publish gate | **2026-11-01T01:11:35+00:00** | **STALE** |

## Maintenance History
- Records retained: **30**
- Latest entries change: **1161 → 1161**
- Latest health failures: **157 → 157**

Historical records are retained in reports/maintenance-history.json.
