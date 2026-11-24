# Cross-Playlist Metadata Backfill

Generated: **2026-11-24T00:17:02+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **95ca9078eca1ae8371b7c211029a02bfed62a01de35303f09627ec12f3ba8bc7**
- International-Playlist.m3u SHA-256: **21bb925089e872099dfa3bd8ac0e1567e723bad28fa3294020917ed6d6bbbfee**

Only missing tvg-country and tvg-language values were filled. Sources: exact playlist tvg-id/channel-id, unique exact channel names, and iptv-org channel/feed metadata. Unresolved broadcast languages are marked und (ISO 639-2 undetermined), never guessed. iptv-org catalogue status: loaded.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Review/Adult/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Language marked undetermined | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 0 | 0 | unchanged (ef43f07efe3e...) | 95ca9078eca1ae8371b7c211029a02bfed62a01de35303f09627ec12f3ba8bc7 |
| International-Playlist.m3u | 0 | 0 | 0 | 0 | 6 | unchanged (b366cd24707f...) | 21bb925089e872099dfa3bd8ac0e1567e723bad28fa3294020917ed6d6bbbfee |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

