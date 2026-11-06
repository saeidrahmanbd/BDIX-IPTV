# Cross-Playlist Metadata Backfill

Generated: **2026-11-06T12:24:02+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **c1e170f5553fb67bfd7966dc803db253fd14b6e20a94375f13cf7f6b50710bc0**
- International-Playlist.m3u SHA-256: **7762b2644675b92a5ab0d59ae1983e213855f70f78ebf265ae7bd62e9430e84a**

Only missing tvg-country and tvg-language values were filled. Source evidence was an exact tvg-id match or an unambiguous exact tvg-name match. Unknown or ambiguous values remain blank.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 0 | unchanged (c3d3966c20ca...) | c1e170f5553fb67bfd7966dc803db253fd14b6e20a94375f13cf7f6b50710bc0 |
| International-Playlist.m3u | 0 | 0 | 0 | 1876 | unchanged (03b084500b37...) | 7762b2644675b92a5ab0d59ae1983e213855f70f78ebf265ae7bd62e9430e84a |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

