# Cross-Playlist Metadata Backfill

Generated: **2026-11-21T04:22:18+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **6f0c1b004804ee4dc27caa489be97d275fb316526b22a13079e5fe7817aee82c**
- International-Playlist.m3u SHA-256: **c5dab98657a86fd204721157eb66952ef1e8bda7f06c338d2f3ec73737802c71**

Only missing tvg-country and tvg-language values were filled. Sources: exact playlist tvg-id/channel-id, unique exact channel names, and iptv-org channel/feed metadata. Unresolved broadcast languages are marked und (ISO 639-2 undetermined), never guessed. iptv-org catalogue status: loaded.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Review/Adult/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Language marked undetermined | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 0 | 0 | unchanged (a3a2f9e6329e...) | 6f0c1b004804ee4dc27caa489be97d275fb316526b22a13079e5fe7817aee82c |
| International-Playlist.m3u | 0 | 0 | 0 | 0 | 0 | unchanged (fc7585e7f80d...) | c5dab98657a86fd204721157eb66952ef1e8bda7f06c338d2f3ec73737802c71 |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

