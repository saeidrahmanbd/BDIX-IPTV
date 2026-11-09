# Cross-Playlist Metadata Backfill

Generated: **2026-11-09T00:02:06+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **a02d892fda4e692ec37814a8206c4ff6c6ab200d77b7592a17da1d7c01fd070b**
- International-Playlist.m3u SHA-256: **78f1aa33f238b6584576ea03b006d78132bd54bbafb7f665f62da461309aa5e0**

Only missing tvg-country and tvg-language values were filled. Source evidence was an exact tvg-id match or an unambiguous exact tvg-name match. Unknown or ambiguous values remain blank.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Review/Adult/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 0 | unchanged (7dab727fe836...) | a02d892fda4e692ec37814a8206c4ff6c6ab200d77b7592a17da1d7c01fd070b |
| International-Playlist.m3u | 0 | 0 | 0 | 761 | unchanged (d9d8857c7d13...) | 78f1aa33f238b6584576ea03b006d78132bd54bbafb7f665f62da461309aa5e0 |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

