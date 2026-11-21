# Cross-Playlist Metadata Backfill

Generated: **2026-11-21T00:56:23+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **9bbdc0608673318c3fc970a8904a67dc47387c4068ee8bc6dc3bab1594a1def7**
- International-Playlist.m3u SHA-256: **1ffb8f01cbc5694b718e2ba0f78cd5a5e25903fa37066a3a5459a36984333cb6**

Only missing tvg-country and tvg-language values were filled. Sources: exact playlist tvg-id/channel-id, unique exact channel names, and iptv-org channel/feed metadata. Unresolved broadcast languages are marked und (ISO 639-2 undetermined), never guessed. iptv-org catalogue status: loaded.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Review/Adult/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Language marked undetermined | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 0 | 0 | unchanged (18df896ba494...) | 9bbdc0608673318c3fc970a8904a67dc47387c4068ee8bc6dc3bab1594a1def7 |
| International-Playlist.m3u | 10 | 0 | 10 | 4 | 0 | unchanged (cceae617d0bb...) | 1ffb8f01cbc5694b718e2ba0f78cd5a5e25903fa37066a3a5459a36984333cb6 |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

