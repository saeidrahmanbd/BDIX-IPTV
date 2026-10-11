# Update Report

_Last generated: **2026-10-11 10:12 UTC**_

| Metric | Current |
|---|---:|
| Streams | **1186** |
| Active Channel Identities | **625** |
| Active Primary Streams | **625** |
| Bangladesh | **59** |
| India | **291** |
| Backup Streams | **474** |
| New Channels | **22** |
| New Backup Streams | **19** |
| Local Logos | **100.0%** |
| EPG Programme Coverage | **78.0%** |
| EPG Mapping | **81.4%** |
| Stream Health Tested | **1186** |
| Stream Health Failures | **194** |
| Persistent Failures | **143** |
| Near-Duplicate URL Families | **0** |
| Audit Blocking Issues | **104** |
| Pre-Publish Gate | **BLOCK** |
| Pre-Publish Gate Generated | **2026-10-11T10:11:39+00:00** |

## Quality Controls
- Duplicate stream URLs: **0**
- Metadata conflicts: **29**
- Same-name / different-ID collisions: **0**
- Duplicate primary identities: **1**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **71**
- Logo exceptions: **0**
- Not Playing logo exceptions: **0**
- Malformed EXTINF entries: **0**
- Category block-order issues: **3**
- Alphabetical ordering issues: **0**
- Signed/tokenized URLs: **9**

## Safety & Automation
- Stream health is non-destructive and keeps per-URL failure history.
- Backup streams are never automatically deleted because of health failures.
- Review queues remain user-controlled.
- Pre-publish gate status: **BLOCK**
- Canonical channel identity index: reports/channel-identity-index.json

## EPG
- Indian channels audited: **291**
- Mapped: **237 (81.4%)**
- Current/future programme coverage: **227/291 (78.0%)**
- No mapping: **54**
- Publication remains subject to source-policy approval.

## Freshness
| Report | Last generated |
|---|---|
| Playlist audit | **2026-10-11T10:11:39.417454+00:00** |
| EPG coverage | **2026-10-11T10:10:39+00:00** |
| Stream health | **2026-10-11T10:12:35+00:00** |
| Pre-publish gate | **2026-10-11T10:11:39+00:00** |

## Maintenance History
- Records retained: **30**
- Latest entries change: **1186 → 1186**
- Latest health failures: **195 → 194**

Historical records are retained in reports/maintenance-history.json.
