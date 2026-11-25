# Cross-Playlist Metadata Backfill

Generated: **2026-11-25T09:21:43+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **72b27febe9a11669f9351b81beac6ff23b82b10f241a4052af20783e38fde0cf**
- International-Playlist.m3u SHA-256: **2438e137ff42a85a52747a9f71def8892548dac805d8fec236ddd53bdfe094e9**

Only missing tvg-country and tvg-language values were filled. Sources: exact playlist tvg-id/channel-id, unique exact channel names, and iptv-org channel/feed metadata. Unresolved broadcast languages are marked und (ISO 639-2 undetermined), never guessed. iptv-org catalogue status: loaded.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Review/Adult/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Language marked undetermined | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 0 | 0 | unchanged (753411e72283...) | 72b27febe9a11669f9351b81beac6ff23b82b10f241a4052af20783e38fde0cf |
| International-Playlist.m3u | 11 | 0 | 11 | 4 | 7 | unchanged (cbc76f0b1ccb...) | 2438e137ff42a85a52747a9f71def8892548dac805d8fec236ddd53bdfe094e9 |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

