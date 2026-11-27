# Cross-Playlist Metadata Backfill

Generated: **2026-11-27T00:17:27+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **27dd311208b29f1f41fde3a978f942ae4148e708185c2bb63fff690b89065cbd**
- International-Playlist.m3u SHA-256: **841f85797d55550f76efe36ec201950ea40bcb60edbf02a916160ee0f37b37db**

Only missing tvg-country and tvg-language values were filled. Sources: exact playlist tvg-id/channel-id, unique exact channel names, and iptv-org channel/feed metadata. Unresolved broadcast languages are marked und (ISO 639-2 undetermined), never guessed. iptv-org catalogue status: loaded.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Review/Adult/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Language marked undetermined | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 0 | 0 | unchanged (e1085d597c85...) | 27dd311208b29f1f41fde3a978f942ae4148e708185c2bb63fff690b89065cbd |
| International-Playlist.m3u | 3 | 0 | 3 | 0 | 7 | unchanged (46e8fe901fa6...) | 841f85797d55550f76efe36ec201950ea40bcb60edbf02a916160ee0f37b37db |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

