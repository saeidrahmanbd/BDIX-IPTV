# Cross-Playlist Metadata Backfill

Generated: **2026-11-26T00:17:47+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **3eed831257f2645543d1d7b58829ecd86618988210a25acb0891f26815860bc1**
- International-Playlist.m3u SHA-256: **ae090b7bdd1fb00106c6b28ce85030047395270f2023a1c39cf3c8e4922d51a6**

Only missing tvg-country and tvg-language values were filled. Sources: exact playlist tvg-id/channel-id, unique exact channel names, and iptv-org channel/feed metadata. Unresolved broadcast languages are marked und (ISO 639-2 undetermined), never guessed. iptv-org catalogue status: loaded.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Review/Adult/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Language marked undetermined | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 0 | 0 | unchanged (f4308f76911e...) | 3eed831257f2645543d1d7b58829ecd86618988210a25acb0891f26815860bc1 |
| International-Playlist.m3u | 0 | 0 | 0 | 0 | 7 | unchanged (2f2f1544697f...) | ae090b7bdd1fb00106c6b28ce85030047395270f2023a1c39cf3c8e4922d51a6 |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

