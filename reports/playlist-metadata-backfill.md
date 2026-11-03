# Cross-Playlist Metadata Backfill

Generated: **2026-11-03T09:08:58+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **9066c575b7ec57f8cecc46f47ef89584a8b2398c1023122866e72e480bd571ee**
- International-Playlist.m3u SHA-256: **cc183f0ce5b4dc843eaf2a231b62e4c11f0fd4d48341ceb89a189d2374e5c021**

Only missing tvg-country and tvg-language values were filled. Source evidence was an exact tvg-id match or an unambiguous exact tvg-name match. Unknown or ambiguous values remain blank.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 64 | unchanged (7a7ffbdf898d...) | 9066c575b7ec57f8cecc46f47ef89584a8b2398c1023122866e72e480bd571ee |
| International-Playlist.m3u | 0 | 0 | 0 | 1645 | unchanged (8eb353e90276...) | cc183f0ce5b4dc843eaf2a231b62e4c11f0fd4d48341ceb89a189d2374e5c021 |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

