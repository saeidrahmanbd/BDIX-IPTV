# IPTV Playlist Logo Repair Results

Generated: **2026-10-17**

Target: `IPTV-Playlist.m3u` in `saeidrahmanbd/BDIX-IPTV`. `BDIX-Playlist.m3u` was not edited by this repair.

## Results

| Measure | Result |
|---|---:|
| Playlist entries retained | 1095 |
| Logo references repaired | 41 |
| Previously missing `tvg-logo` attributes completed | 36 |
| Third-party logo URLs replaced | 5 |
| Logo references now pointing to the repository `/logos/` path | 1095/1095 |
| Empty or non-repository logo references remaining | 0 |
| Unique local logo paths in the playlist | 666 |
| New self-contained localized logo SVG assets | 20 |
| New unofficial fallback SVG assets | 19 |
| Playlist rows referencing fallback artwork | 20 |

## Localized image assets

Twenty SVG files were added under `/logos/`. Each contains the chosen source image embedded locally, so a player does not need to contact an external image host. Provenance records are stored in `reports/logo-source-registry.json`.

## Unofficial fallback artwork

Where an exact, source-matched broadcaster mark could not be verified, channel-labelled SVG art was added under `/logos/`. Each is explicitly labelled **UNOFFICIAL FALLBACK ART** and is not presented as an official broadcaster logo. The A Sports HD primary and backup entries share the same fallback asset.

## External logo references removed

- A Sports HD (primary and backup)
- Euro Sports HD
- Mundial
- Willow HD

All five former third-party references were replaced by local repository asset references. No channel entries or stream URLs were removed for logo repair.
