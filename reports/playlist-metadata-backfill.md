# Cross-Playlist Metadata Backfill

Generated: **2026-11-10T03:41:14+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **3a82bd3bb723138e3d18d13e4a394f6fe0c1e806e1159349bd3bcf4611413c78**
- International-Playlist.m3u SHA-256: **058f10a9eee15c2a4bda72db44a2e0cf83ba81a767e151537de6393d5d6cf5cf**

Only missing tvg-country and tvg-language values were filled. Source evidence was an exact tvg-id match or an unambiguous exact tvg-name match. Unknown or ambiguous values remain blank.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Review/Adult/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 0 | unchanged (00cd7fbaeb05...) | 3a82bd3bb723138e3d18d13e4a394f6fe0c1e806e1159349bd3bcf4611413c78 |
| International-Playlist.m3u | 0 | 0 | 0 | 884 | unchanged (5669223a5ff2...) | 058f10a9eee15c2a4bda72db44a2e0cf83ba81a767e151537de6393d5d6cf5cf |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

