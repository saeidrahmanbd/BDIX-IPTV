# Cross-Playlist Metadata Backfill

Generated: **2026-11-19T03:48:53+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **8611340c6b07807062028b490d6f6cd925bf5fb18ac79bb174f637872523e81e**
- International-Playlist.m3u SHA-256: **1b9c33053a2fea019d939811e2d0061979dc81026b71d1308fa4f5c704940773**

Only missing tvg-country and tvg-language values were filled. Sources: exact playlist tvg-id/channel-id, unique exact channel names, and iptv-org channel/feed metadata. Unresolved broadcast languages are marked und (ISO 639-2 undetermined), never guessed. iptv-org catalogue status: loaded.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Review/Adult/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Language marked undetermined | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 0 | 0 | unchanged (6ac5cbe21fc6...) | 8611340c6b07807062028b490d6f6cd925bf5fb18ac79bb174f637872523e81e |
| International-Playlist.m3u | 22 | 0 | 22 | 12 | 0 | unchanged (c3ffcddc8b72...) | 1b9c33053a2fea019d939811e2d0061979dc81026b71d1308fa4f5c704940773 |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

