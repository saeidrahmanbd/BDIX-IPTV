# Cross-Playlist Metadata Backfill

Generated: **2026-11-09T00:39:48+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **8675200ab8b37acc114ba0d5fc456d80611f2715c3226f08837681133391c6b5**
- International-Playlist.m3u SHA-256: **78f1aa33f238b6584576ea03b006d78132bd54bbafb7f665f62da461309aa5e0**

Only missing tvg-country and tvg-language values were filled. Source evidence was an exact tvg-id match or an unambiguous exact tvg-name match. Unknown or ambiguous values remain blank.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Review/Adult/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 0 | unchanged (7dab727fe836...) | 8675200ab8b37acc114ba0d5fc456d80611f2715c3226f08837681133391c6b5 |
| International-Playlist.m3u | 0 | 0 | 0 | 761 | unchanged (d9d8857c7d13...) | 78f1aa33f238b6584576ea03b006d78132bd54bbafb7f665f62da461309aa5e0 |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

