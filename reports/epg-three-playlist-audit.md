# EPG Audit — Published Playlists

Generated: **2026-10-22T04:22:13+00:00**

This report measures the two M3U files currently published at the repository root. The historic filename epg-three-playlist-audit.md is retained for link compatibility; it does not mean a third playlist file exists.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1064 | 630 | 424 | 407 | 426 | 281 | 206 | OK |
| BDIX-Playlist.m3u | 139 | 131 | 76 | 75 | 78 | 45 | 55 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Bangladesh | 67 | 3 | 3 | 64 |
| Documentary & Wildlife | 77 | 61 | 60 | 16 |
| Indian Bangla | 44 | 35 | 34 | 9 |
| Indian Entertainment | 143 | 124 | 118 | 19 |
| Indian Movies | 63 | 52 | 51 | 11 |
| Indian Music | 53 | 47 | 44 | 6 |
| International | 109 | 67 | 64 | 42 |
| Kids | 46 | 31 | 31 | 15 |
| Pakistani | 14 | 3 | 3 | 11 |
| Religious | 25 | 9 | 8 | 16 |
| Sports | 39 | 28 | 26 | 11 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **addec3a4a8d31ba16ccc35375c378a3faf26983e635c0bf1615d979f1d73b4e7**
- BDIX-Playlist.m3u SHA-256: **9027e1a976113e360f03ee51c0c9cd5952ca25c2a53d88f63310b32f0dcd5b8d**
