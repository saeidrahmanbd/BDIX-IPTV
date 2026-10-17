# Playlist Audit

Generated: **2026-10-17**

Scope: live `IPTV-Playlist.m3u` only. The distinct `BDIX-Playlist.m3u` was not edited.

## Summary

| Check | Result |
|---|---:|
| Playlist entries | 1095 |
| Distinct `tvg-id` values | 676 |
| Distinct `channel-id` values | 676 |
| IDs used for multiple streams (including backups) | 222 |
| Missing required identity, logo, group, or stream fields | 0 |
| Duplicate stream URLs | 0 |
| Duplicate channel numbers | 0 |
| Duplicate primary IDs | 0 |
| Primary same-name / different-ID conflicts | 0 |
| Repeated-ID metadata conflicts (name, channel ID, or logo) | 0 |
| Orphan backup entries | 0 |
| Malformed `#EXTINF` records | 0 |
| Noncanonical attribute-order records | 0 |
| Active/primary entries missing `tvg-chno` | 0 |
| Invalid numeric channel numbers (zero, non-numeric, or negative) | 0 |
| Logo refs outside the repository `/logos/` path or empty | 0 |
| Unique local logo paths | 666 |

## Structural and numbering checks

- All 13 declared categories are present and in the established order.
- Category blocks remain contiguous.
- Active channels remain alphabetically sorted within each category.
- 398 `Backup` and 22 `Not Playing` entries have no channel number; all primary channels have a channel number. These non-primary values were retained rather than inventing channel numbers.
- Every backup entry matches a primary entry by `tvg-id`, `channel-id`, or normalized channel name.
- Stream URLs were preserved through logo repair and metadata normalization.

## Logo policy

- Every entry has exactly one non-empty `tvg-logo` reference pointing to `https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/`.
- No third-party image-host URLs remain in the playlist.
- 36 missing logo attributes were populated; 5 third-party logo references were replaced with local repository assets.
- 20 localized logo SVG wrappers and 19 explicitly labelled unofficial fallback SVGs were added under `/logos/`. Twenty channel entries use fallback art because A Sports HD's primary and backup entries share one file.
- Source attribution and fallback status are recorded in `reports/logo-source-registry.json`.

## Metadata formatting

- Attribute sequence is normalized to `tvg-id`, `tvg-name`, `tvg-logo`, `tvg-chno` (when applicable), `channel-id`, optional `tvg-language` / `tvg-country`, then `group-title`.
- 37 noncanonical `#EXTINF` records were normalized without changing attribute values, display names, or stream URLs.
- Duplicate attributes: 0.
- A final newline is present.
