# Backup Orphan Audit

Generated: **2026-10-15T08:51:45.591Z**

An orphan is a Backup route whose channel ID and normalized channel name both fail to match a primary record in `IPTV-Playlist.m3u`.
Backup routes for existing primary channels remain in Backup. Standalone orphan channels identified in the latest audit have been migrated into their canonical categories; no URLs were added from outside the repository.

## Summary

- Primary entries checked: **652**
- Backup routes checked: **385**
- Orphan Backup routes: **0**
- Distinct orphan channel labels: **0**
- Backup channels migrated in this change: **18**

| Channel label | Channel ID | Stream host | Source line |
|---|---|---|---:|
| None | — | — | — |

## Actions
- Restored requested streams/routes: **3**
- Exact duplicate URLs removed: **1**
- Duronto TV alternate routes now share `DurontoTV.bd` as their canonical identity.
- Backup routes for channels with an existing primary remain in Backup.
- Stream reachability was not inferred from this metadata migration.
