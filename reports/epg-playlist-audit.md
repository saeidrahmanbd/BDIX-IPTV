# EPG Audit — Published Playlists

Generated: **2026-11-16T03:33:33+00:00**

This report measures the two maintained M3U playlists included in the automated EPG pipeline. This report covers only the two maintained playlists.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1298 | 657 | 386 | 338 | 386 | 331 | 271 | OK |
| International-Playlist.m3u | 3135 | 1764 | 604 | 515 | 593 | 521 | 1160 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 343 | 11 | 11 | 332 |
| Argentina | 14 | 1 | 0 | 13 |
| Bangladesh | 80 | 5 | 3 | 75 |
| Brazil | 13 | 7 | 7 | 6 |
| Bulgaria | 21 | 6 | 0 | 15 |
| Canada | 30 | 23 | 15 | 7 |
| Chile | 11 | 0 | 0 | 11 |
| China | 9 | 3 | 3 | 6 |
| Colombia | 9 | 0 | 0 | 9 |
| Costa Rica | 9 | 0 | 0 | 9 |
| Czech Republic | 22 | 17 | 16 | 5 |
| DO | 10 | 1 | 0 | 9 |
| Documentary & Wildlife | 52 | 40 | 26 | 12 |
| Estonia | 6 | 0 | 0 | 6 |
| France | 41 | 16 | 14 | 25 |
| Germany | 72 | 18 | 11 | 54 |
| Greece | 8 | 2 | 2 | 6 |
| Hungary | 15 | 7 | 6 | 8 |
| Indian Bangla | 43 | 34 | 31 | 9 |
| Indian Entertainment | 203 | 165 | 155 | 38 |
| Indian Movies | 89 | 66 | 60 | 23 |
| Indian Music | 69 | 60 | 56 | 9 |
| International | 166 | 33 | 23 | 133 |
| Iran | 13 | 1 | 0 | 12 |
| Italy | 27 | 12 | 12 | 15 |
| Kids | 33 | 19 | 17 | 14 |
| Lebanon | 6 | 1 | 0 | 5 |
| Mexico | 17 | 8 | 2 | 9 |
| Netherlands | 15 | 9 | 6 | 6 |
| North Macedonia | 5 | 0 | 0 | 5 |
| Pakistani | 29 | 1 | 1 | 28 |
| Panama | 5 | 0 | 0 | 5 |
| Paraguay | 6 | 0 | 0 | 6 |
| Peru | 7 | 0 | 0 | 7 |
| Poland | 24 | 12 | 9 | 12 |
| Religious | 24 | 5 | 5 | 19 |
| Romania | 28 | 9 | 7 | 19 |
| Russia | 73 | 20 | 16 | 53 |
| Saudi Arabia | 8 | 0 | 0 | 8 |
| Singapore | 5 | 1 | 0 | 4 |
| Spain | 20 | 5 | 3 | 15 |
| Sports | 101 | 50 | 46 | 51 |
| Sweden | 49 | 12 | 12 | 37 |
| Turkey | 14 | 0 | 0 | 14 |
| Ukraine | 27 | 6 | 6 | 21 |
| United Kingdom | 16 | 3 | 2 | 13 |
| United States | 213 | 98 | 89 | 115 |
| Vietnam | 6 | 0 | 0 | 6 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **910e85f0a79f101b8afe550c781126fb156b183e4c678472f2fe3f1699777d73**
- International-Playlist.m3u SHA-256: **8507c6ec2bf25f980e31949568dfa241761449aff4ed2a12e3cd85039f430643**
