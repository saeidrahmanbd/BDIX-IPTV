# Update Report

_Last generated: **2026-11-02 09:09 UTC**_

Source playlist SHA-256: **c83a2db794504997f9441df2faae73c5ea42a78b7bf4e7bd8f4e3c1d397f5454**

| Metric | Current |
|---|---:|
| Streams | **1066** |
| Active Channel Identities | **680** |
| Active Primary Streams | **680** |
| Bangladesh | **63** |
| India | **327** |
| Backup Stream Entries | **346** |
| IPTV Local Logos | **99.2%** |
| IPTV EPG Programme Coverage | **PENDING** |
| IPTV EPG Mapping | **PENDING** |
| Stream Health Tested | **1066** |
| Stream Health Failures | **66** |
| Persistent Failures | **21** |
| Near-Duplicate URL Families | **2** |
| Audit Blocking Issues | **0** |
| Pre-Publish Gate | **BLOCK** |
| Pre-Publish Gate Generated | **2026-11-02T09:09:15+00:00** |

## Quality Controls 
- Duplicate stream URLs: **0**
- Metadata conflicts (canonical primary scope): **0**
- Same-name / different-ID collisions (canonical primary scope): **0**
- Cross-queue metadata identity variants: **0**
- Cross-queue same-name / different-ID collisions: **4**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **0**
- Logo exceptions: **0**
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
- EPG metric scope: **combined EPG report fallback (IPTV-only row unavailable) (awaiting a valid, fresh published guide)**
- Programme coverage and freshness are measured from the published XMLTV; technical validation checks data integrity, not upstream licensing.

## Freshness
| Report | Last generated | Input freshness |
|---|---|---|
| Playlist audit | **2026-11-02T09:09:15.428164+00:00** | **CURRENT** |
| EPG coverage / two-playlist inventory | **2026-11-02T08:30:49.124Z** | **PENDING — guide missing or freshness not PASS** |
| Stream health | **2026-11-02T09:09:44+00:00** | **CURRENT** |
| Pre-publish gate | **2026-11-02T09:09:15+00:00** | **CURRENT** |

## Maintenance History
- Records retained: **30**
- Latest entries change: **1161 → 1066**
- Latest health failures: **157 → 66**

Historical records are retained in reports/maintenance-history.json.
