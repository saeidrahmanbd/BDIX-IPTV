# Cross-Playlist Metadata Backfill

Generated: **2026-11-23T08:50:59+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **8605b2b64684072ed4bc3d53d8d3ba804983ef9b81f96d2cb91e551df9841a7c**
- International-Playlist.m3u SHA-256: **e399bcc9869261b4e9f7d33bf015df494374c1394911ade718b3ae98417a2375**

Only missing tvg-country and tvg-language values were filled. Sources: exact playlist tvg-id/channel-id, unique exact channel names, and iptv-org channel/feed metadata. Unresolved broadcast languages are marked und (ISO 639-2 undetermined), never guessed. iptv-org catalogue status: loaded.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Review/Adult/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Language marked undetermined | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 0 | 0 | unchanged (62f1b1c083a0...) | 8605b2b64684072ed4bc3d53d8d3ba804983ef9b81f96d2cb91e551df9841a7c |
| International-Playlist.m3u | 336 | 0 | 336 | 111 | 6 | unchanged (aa3b48a720a4...) | e399bcc9869261b4e9f7d33bf015df494374c1394911ade718b3ae98417a2375 |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

