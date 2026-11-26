# Cross-Playlist Metadata Backfill

Generated: **2026-11-26T10:38:17+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **6ed75613aa2965cc341a0d144242ed4fab07eebdd8f1175ab003c66d0f701a97**
- International-Playlist.m3u SHA-256: **3615fbfe99b6cc86d5c469f9e152f1d11c60b81f76765fc7353857b2de59e155**

Only missing tvg-country and tvg-language values were filled. Sources: exact playlist tvg-id/channel-id, unique exact channel names, and iptv-org channel/feed metadata. Unresolved broadcast languages are marked und (ISO 639-2 undetermined), never guessed. iptv-org catalogue status: loaded.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Review/Adult/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Language marked undetermined | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 0 | 0 | unchanged (ef7b1c5c1992...) | 6ed75613aa2965cc341a0d144242ed4fab07eebdd8f1175ab003c66d0f701a97 |
| International-Playlist.m3u | 0 | 0 | 0 | 0 | 7 | unchanged (3c5a3028e53f...) | 3615fbfe99b6cc86d5c469f9e152f1d11c60b81f76765fc7353857b2de59e155 |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

