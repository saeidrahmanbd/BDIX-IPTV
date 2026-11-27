# Cross-Playlist Metadata Backfill

Generated: **2026-11-27T05:25:20+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **9558746a36438c06848914c1906a5f2210f5c8e6c367af65c65a1529bbcf4c49**
- International-Playlist.m3u SHA-256: **ac590fd34726acfe479ba48aca0ea1d4da3ca5262f97fc21a0963c54d27d8fd6**

Only missing tvg-country and tvg-language values were filled. Sources: exact playlist tvg-id/channel-id, unique exact channel names, and iptv-org channel/feed metadata. Unresolved broadcast languages are marked und (ISO 639-2 undetermined), never guessed. iptv-org catalogue status: loaded.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Review/Adult/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Language marked undetermined | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 0 | 0 | unchanged (11ad8ab8c97e...) | 9558746a36438c06848914c1906a5f2210f5c8e6c367af65c65a1529bbcf4c49 |
| International-Playlist.m3u | 0 | 0 | 0 | 0 | 7 | unchanged (711705c6ffde...) | ac590fd34726acfe479ba48aca0ea1d4da3ca5262f97fc21a0963c54d27d8fd6 |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

