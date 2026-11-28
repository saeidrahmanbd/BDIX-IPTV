# Cross-Playlist Metadata Backfill

Generated: **2026-11-28T00:17:21+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **bc20e905e2a4c4935f2a0ce061b61ef523f9a4a5a2e11e8e632cfc87b79fc57c**
- International-Playlist.m3u SHA-256: **99ac5c04870550e837f821df53041f75621972fcf1c79c162b887e66d67a9dc8**

Only missing tvg-country and tvg-language values were filled. Sources: exact playlist tvg-id/channel-id, unique exact channel names, and iptv-org channel/feed metadata. Unresolved broadcast languages are marked und (ISO 639-2 undetermined), never guessed. iptv-org catalogue status: loaded.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Review/Adult/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Language marked undetermined | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 0 | 0 | unchanged (2b0f43c9e325...) | bc20e905e2a4c4935f2a0ce061b61ef523f9a4a5a2e11e8e632cfc87b79fc57c |
| International-Playlist.m3u | 0 | 0 | 0 | 0 | 7 | unchanged (213b6f917c7e...) | 99ac5c04870550e837f821df53041f75621972fcf1c79c162b887e66d67a9dc8 |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

