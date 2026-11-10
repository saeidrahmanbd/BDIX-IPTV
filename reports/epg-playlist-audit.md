# EPG Audit — Published Playlists

Generated: **2026-11-10T13:07:49+00:00**

This report measures the two maintained M3U playlists included in the automated EPG pipeline. This report covers only the two maintained playlists.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1151 | 590 | 360 | 322 | 360 | 311 | 230 | OK |
| International-Playlist.m3u | 3075 | 1667 | 566 | 527 | 558 | 494 | 1101 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 325 | 8 | 8 | 317 |
| Argentina | 13 | 1 | 0 | 12 |
| Bangladesh | 68 | 4 | 2 | 64 |
| Brazil | 13 | 7 | 7 | 6 |
| Bulgaria | 21 | 6 | 6 | 15 |
| Canada | 29 | 22 | 16 | 7 |
| Chile | 11 | 0 | 0 | 11 |
| China | 9 | 3 | 3 | 6 |
| Colombia | 9 | 1 | 0 | 8 |
| Costa Rica | 9 | 0 | 0 | 9 |
| Czech Republic | 22 | 17 | 17 | 5 |
| DO | 10 | 1 | 0 | 9 |
| Documentary & Wildlife | 54 | 42 | 30 | 12 |
| Estonia | 6 | 0 | 0 | 6 |
| France | 40 | 15 | 14 | 25 |
| Germany | 74 | 18 | 18 | 56 |
| Greece | 8 | 2 | 2 | 6 |
| Hungary | 15 | 7 | 7 | 8 |
| Indian Bangla | 37 | 28 | 26 | 9 |
| Indian Entertainment | 184 | 152 | 146 | 32 |
| Indian Movies | 83 | 62 | 59 | 21 |
| Indian Music | 67 | 59 | 56 | 8 |
| International | 166 | 32 | 24 | 134 |
| Iran | 13 | 1 | 0 | 12 |
| Italy | 27 | 11 | 11 | 16 |
| Kids | 37 | 22 | 20 | 15 |
| Lebanon | 5 | 1 | 0 | 4 |
| Mexico | 16 | 7 | 6 | 9 |
| Netherlands | 15 | 9 | 6 | 6 |
| Pakistani | 24 | 1 | 1 | 23 |
| Panama | 5 | 0 | 0 | 5 |
| Peru | 7 | 0 | 0 | 7 |
| Poland | 25 | 13 | 12 | 12 |
| Religious | 25 | 5 | 5 | 20 |
| Romania | 28 | 9 | 9 | 19 |
| Russia | 61 | 16 | 16 | 45 |
| Saudi Arabia | 8 | 0 | 0 | 8 |
| Singapore | 3 | 1 | 1 | 2 |
| Spain | 19 | 4 | 4 | 15 |
| Sports | 47 | 26 | 23 | 21 |
| Sweden | 46 | 12 | 12 | 34 |
| Turkey | 14 | 0 | 0 | 14 |
| Ukraine | 24 | 7 | 7 | 17 |
| United Kingdom | 15 | 2 | 2 | 13 |
| United States | 190 | 88 | 87 | 102 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 6 | 0 | 0 | 6 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **810bd296df25477c8020711267bf2062f97b9386ab54cd783171bac96e9d7bc0**
- International-Playlist.m3u SHA-256: **088cc6fee8e2211d4c5731a8f086e9ad91b51d302a33d9297b979ce4432e3cf6**
