# Update Report

_Last generated: **2026-10-10 — corrected against live IPTV-Playlist.m3u**_

| Metric | Current |
|---|---:|
| Streams | **1061** |
| Active Channel Identities | **Not refreshed in this correction** |
| Active Primary Streams | **Not refreshed in this correction** |
| Bangladesh | **Not refreshed in this correction** |
| India | **Not refreshed in this correction** |
| Backup Streams | **Not refreshed in this correction** |
| New Channels | **Not refreshed in this correction** |
| New Backup Streams | **Not refreshed in this correction** |
| Local Logos | **100.0%** |
| EPG Programme Coverage | **79.0%** |
| EPG Mapping | **81.9%** |
| Stream Health Tested | **Not refreshed in this correction** |
| Stream Health Failures | **Not refreshed in this correction** |
| Persistent Failures | **Not refreshed in this correction** |
| Near-Duplicate URL Families | **0** |
| Audit Blocking Issues | **Not refreshed in this correction** |
| Pre-Publish Gate | **Not rerun in this correction** |
| Pre-Publish Gate Generated | **Not rerun in this correction** |

## Quality Controls
- Duplicate stream URLs: **0**
- Metadata conflicts: **0**
- Same-name / different-ID collisions: **1**
- Duplicate primary identities: **0**
- Primary channel-number collisions: **0**
- Primary entries missing channel numbers: **0**
- Logo exceptions: **0**
- Not Playing logo exceptions: **0**
- Malformed EXTINF entries: **0**
- Category block-order issues: **2**
- Alphabetical ordering issues: **13**
- Signed/tokenized URLs: **9**

## Safety & Automation
- Stream health is non-destructive and keeps per-URL failure history.
- Backup streams are never automatically deleted because of health failures.
- Review queues remain user-controlled.
- Pre-publish gate status: **PASS**
- Canonical channel identity index: reports/channel-identity-index.json

## EPG
- Indian channels audited: **276**
- Mapped: **226 (81.9%)**
- Current/future programme coverage: **218/276 (79.0%)**
- No mapping: **50**
- Publication remains subject to source-policy approval.

## Freshness
| Report | Last generated |
|---|---|
| Playlist audit | **2026-10-10T12:20:58.572529+00:00** |
| EPG coverage | **2026-10-10T12:20:58+00:00** |
| Stream health | **2026-10-10T12:21:52+00:00** |
| Pre-publish gate | **2026-10-10T12:21:53+00:00** |

## Data freshness note

The stream total above was verified directly against the current `IPTV-Playlist.m3u` (1,061 entries). Other historical metrics are deliberately marked as not refreshed rather than presenting stale values as current. Run the IPTV Playlist Update workflow to regenerate all reports from the same playlist revision.

## Maintenance History
- Records retained: **30**
- Latest entries change: **1152 → 1152**
- Latest health failures: **188 → 185**

Historical records are retained in reports/maintenance-history.json.
