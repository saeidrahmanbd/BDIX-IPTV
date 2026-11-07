# Cross-Playlist Metadata Backfill

Generated: **2026-11-07T05:10:30+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **84c02ef014377e5b6ba95a227f9783389650950895cfd82aece9c12b369a6a98**
- International-Playlist.m3u SHA-256: **c9542371251dc1172e23e2ae39d8c42e29a2df18a0ef4391efc4fdefcb49fff1**

Only missing tvg-country and tvg-language values were filled. Source evidence was an exact tvg-id match or an unambiguous exact tvg-name match. Unknown or ambiguous values remain blank.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 0 | unchanged (7d8aad9a3fe2...) | 84c02ef014377e5b6ba95a227f9783389650950895cfd82aece9c12b369a6a98 |
| International-Playlist.m3u | 0 | 0 | 0 | 1867 | unchanged (c331553d8966...) | c9542371251dc1172e23e2ae39d8c42e29a2df18a0ef4391efc4fdefcb49fff1 |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

