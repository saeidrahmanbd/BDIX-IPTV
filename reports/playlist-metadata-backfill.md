# Cross-Playlist Metadata Backfill

Generated: **2026-11-07T04:39:47+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **bca056bd163da5534c5919402db1640ccfae58240476c255e4cf422c46701346**
- International-Playlist.m3u SHA-256: **b85e17864c09029a1130b5d4bb0c56b20a3020e26ba774e37fff241018c0052f**

Only missing tvg-country and tvg-language values were filled. Source evidence was an exact tvg-id match or an unambiguous exact tvg-name match. Unknown or ambiguous values remain blank.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 0 | unchanged (ab340bad1d3d...) | bca056bd163da5534c5919402db1640ccfae58240476c255e4cf422c46701346 |
| International-Playlist.m3u | 2 | 0 | 2 | 1870 | unchanged (03b084500b37...) | b85e17864c09029a1130b5d4bb0c56b20a3020e26ba774e37fff241018c0052f |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

