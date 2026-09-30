# Playlist Audit

Non-destructive audit of the current `IPTV-Playlist.m3u` on `main`.

## Summary

- Playlist entries: **823**
- Unique channel IDs: **563**
- IDs with multiple streams: **156**
- Duplicate stream URLs: **0**
- Metadata conflicts: **0**
- Same-name / different-ID collisions: **4**
- Cross-country backup collisions: **0**
- IDs with multiple logo references: **2**
- Protected primary-entry changes: **0**
- Logo exceptions: **0**
- Duplicate primary identities: **1**
- Primary channel-number collisions: **0**
- Suspicious URL credentials/syntax: **0**

## Category Distribution

| Category | Channels |
|---|---:|
| Bangladesh | 51 |
| Indian Bangla | 36 |
| Indian Movies | 55 |
| Indian Music | 42 |
| Indian Entertainment | 87 |
| International | 68 |
| Documentary & Wildlife | 62 |
| Kids | 48 |
| Religious | 18 |
| Sports | 35 |
| Backup | 321 |
| Not Playing | 0 |
| **Total** | **823** |

## Duplicate Primary Identities

One primary identity currently appears more than once:

- **Pop.uk** — Kids — POP / Pop (1080p)

This is a playlist integrity issue and is reported here without modifying the playlist.

## Duplicate IDs

**156 channel IDs have multiple streams.** These are expected where a channel has a primary stream plus Backup/Not Playing streams and are not, by themselves, errors.

## Duplicate Stream URLs

None.

## Metadata Conflicts

None.

## Same-Name / Different-ID Collisions

- **30a music**
- **Amar Bangla Digital**
- **Bangla TV**
- **Zee Cinema**

These are identity/name collisions detected by the audit and are not automatically changed.

## Cross-Country Backup Collisions

None.

## Logo Integrity

- Healthy/local repository references: **823**
- Missing: **0**
- Broken local: **0**
- External: **0**
- Non-PNG: **0**
- Invalid dimensions: **0**
- Corrupt: **0**
- Other: **0**
- IDs with multiple logo references: **2**

## Protected Primary Entries

No protected primary-entry removals or URL/identity changes detected against the immediately previous playlist version used for this reconciliation.

## Reconciliation

This report was reconciled to the current **823-entry** playlist on **2026-09-30**. It replaces the stale 851-entry audit report.
