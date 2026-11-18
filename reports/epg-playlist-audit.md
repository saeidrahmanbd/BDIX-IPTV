# EPG Audit — Published Playlists

Generated: **2026-11-18T12:49:22+00:00**

This report measures the two maintained M3U playlists included in the automated EPG pipeline. This report covers only the two maintained playlists.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1378 | 714 | 434 | 401 | 434 | 384 | 280 | OK |
| International-Playlist.m3u | 3281 | 1817 | 623 | 563 | 610 | 549 | 1194 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 366 | 13 | 13 | 353 |
| Argentina | 14 | 1 | 0 | 13 |
| Bangladesh | 81 | 5 | 4 | 76 |
| Brazil | 13 | 7 | 7 | 6 |
| Bulgaria | 21 | 6 | 4 | 15 |
| Canada | 27 | 20 | 15 | 7 |
| Chile | 11 | 0 | 0 | 11 |
| China | 9 | 3 | 3 | 6 |
| Colombia | 9 | 0 | 0 | 9 |
| Costa Rica | 9 | 0 | 0 | 9 |
| Czech Republic | 22 | 17 | 16 | 5 |
| DO | 10 | 1 | 1 | 9 |
| Documentary & Wildlife | 60 | 45 | 36 | 15 |
| Estonia | 6 | 0 | 0 | 6 |
| France | 43 | 18 | 17 | 25 |
| Germany | 74 | 18 | 12 | 56 |
| Greece | 7 | 1 | 1 | 6 |
| Hungary | 15 | 7 | 6 | 8 |
| Indian Bangla | 42 | 32 | 28 | 10 |
| Indian Entertainment | 204 | 168 | 158 | 36 |
| Indian Movies | 86 | 64 | 63 | 22 |
| Indian Music | 65 | 55 | 52 | 10 |
| International | 187 | 49 | 42 | 138 |
| Iran | 13 | 1 | 0 | 12 |
| Italy | 25 | 12 | 12 | 13 |
| Kids | 45 | 24 | 22 | 21 |
| Lebanon | 6 | 1 | 0 | 5 |
| Mexico | 17 | 8 | 2 | 9 |
| Netherlands | 15 | 9 | 9 | 6 |
| News | 2 | 0 | 0 | 2 |
| North Macedonia | 5 | 0 | 0 | 5 |
| Pakistani | 23 | 1 | 1 | 22 |
| Panama | 5 | 0 | 0 | 5 |
| Paraguay | 5 | 0 | 0 | 5 |
| Peru | 7 | 0 | 0 | 7 |
| Poland | 23 | 11 | 10 | 12 |
| Religious | 28 | 6 | 6 | 22 |
| Romania | 28 | 9 | 7 | 19 |
| Russia | 74 | 20 | 18 | 54 |
| Saudi Arabia | 8 | 0 | 0 | 8 |
| Singapore | 5 | 1 | 0 | 4 |
| Spain | 20 | 6 | 5 | 14 |
| Sports | 115 | 70 | 68 | 45 |
| Sweden | 49 | 12 | 12 | 37 |
| Turkey | 13 | 0 | 0 | 13 |
| Ukraine | 28 | 8 | 8 | 20 |
| United Kingdom | 16 | 3 | 3 | 13 |
| United States | 206 | 98 | 94 | 108 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 6 | 0 | 0 | 6 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **002e4acc43c2210fe25ceb35ed68582b869af2706f3754964d43a274d3618baf**
- International-Playlist.m3u SHA-256: **6d1d591b0908c7830c2a5707ede1d74861cd69936a64903e4f98201a86df6706**
