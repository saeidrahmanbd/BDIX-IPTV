# Cross-Playlist Metadata Backfill

Generated: **2026-11-02T09:08:42+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **c83a2db794504997f9441df2faae73c5ea42a78b7bf4e7bd8f4e3c1d397f5454**
- International-Playlist.m3u SHA-256: **8dae8a50d77b2f9e31bbc330aa8424a3363d1b9cff5cfca459eec9476586166a**

Only missing tvg-country and tvg-language values were filled. Source evidence was an exact tvg-id match or an unambiguous exact tvg-name match. Unknown or ambiguous values remain blank.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 40 | unchanged (48918945dfb7...) | c83a2db794504997f9441df2faae73c5ea42a78b7bf4e7bd8f4e3c1d397f5454 |
| International-Playlist.m3u | 11 | 0 | 11 | 1535 | unchanged (274e944ab45b...) | 8dae8a50d77b2f9e31bbc330aa8424a3363d1b9cff5cfca459eec9476586166a |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

