# Generic Channel Logo Audit — Three Playlists

Audit date: 2026-10-11 14:28 UTC  
Repository: https://github.com/saeidrahmanbd/BDIX-IPTV  
Method: scans current playlist metadata and checks referenced local SVG files for the generic CHANNEL MARK template.

## Summary

| Playlist | Entries | Unique generic placeholder assets |
|---|---:|---:|
| IPTV-Playlist.m3u | 1145 | 0 |
| BDIX-Playlist.m3u | 190 | 0 |
| NVisionBD-Playlist.m3u | 561 | 0 |

Current NVisionBD placeholder assets: **0 unique files**.

## Remaining affected NVisionBD channel labels


## Scope and quality rules

- Only NVisionBD-Playlist.m3u is modified by the replacement workflow.
- A replacement must be a validated image, must not contain the CHANNEL MARK template, and must have a source recorded in the replacement-results report.
- If multiple channels share a name, or no trustworthy source is found, the placeholder is retained and listed for manual review.
- Old generic files are not deleted automatically, to avoid breaking any other reference.
