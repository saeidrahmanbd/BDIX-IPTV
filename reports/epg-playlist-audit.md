# EPG Audit — Published Playlists

Generated: **2026-11-12T01:32:23+00:00**

This report measures the two maintained M3U playlists included in the automated EPG pipeline. This report covers only the two maintained playlists.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1331 | 685 | 407 | 370 | 407 | 354 | 278 | OK |
| International-Playlist.m3u | 3094 | 1690 | 577 | 536 | 569 | 499 | 1113 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 329 | 8 | 8 | 321 |
| Argentina | 13 | 1 | 0 | 12 |
| Bangladesh | 82 | 5 | 3 | 77 |
| Brazil | 13 | 7 | 7 | 6 |
| Bulgaria | 21 | 6 | 6 | 15 |
| Canada | 29 | 22 | 16 | 7 |
| Chile | 11 | 0 | 0 | 11 |
| China | 9 | 3 | 3 | 6 |
| Colombia | 9 | 1 | 0 | 8 |
| Costa Rica | 9 | 0 | 0 | 9 |
| Czech Republic | 22 | 17 | 17 | 5 |
| DO | 10 | 1 | 0 | 9 |
| Documentary & Wildlife | 52 | 40 | 28 | 12 |
| Estonia | 6 | 0 | 0 | 6 |
| France | 40 | 15 | 14 | 25 |
| Germany | 74 | 18 | 18 | 56 |
| Greece | 8 | 2 | 2 | 6 |
| Hungary | 15 | 7 | 7 | 8 |
| Indian Bangla | 34 | 27 | 25 | 7 |
| Indian Entertainment | 200 | 165 | 160 | 35 |
| Indian Movies | 87 | 66 | 59 | 21 |
| Indian Music | 72 | 62 | 58 | 10 |
| International | 163 | 32 | 24 | 131 |
| Iran | 13 | 1 | 0 | 12 |
| Italy | 28 | 12 | 12 | 16 |
| Kids | 33 | 19 | 18 | 14 |
| Lebanon | 5 | 1 | 0 | 4 |
| Mexico | 16 | 7 | 6 | 9 |
| Netherlands | 15 | 9 | 6 | 6 |
| Pakistani | 28 | 1 | 1 | 27 |
| Panama | 5 | 0 | 0 | 5 |
| Peru | 7 | 0 | 0 | 7 |
| Poland | 25 | 13 | 12 | 12 |
| Religious | 26 | 5 | 5 | 21 |
| Romania | 28 | 9 | 9 | 19 |
| Russia | 64 | 17 | 17 | 47 |
| Saudi Arabia | 8 | 0 | 0 | 8 |
| Spain | 19 | 4 | 4 | 15 |
| Sports | 125 | 65 | 64 | 60 |
| Sweden | 49 | 12 | 12 | 37 |
| Turkey | 14 | 0 | 0 | 14 |
| Ukraine | 24 | 7 | 7 | 17 |
| United Kingdom | 15 | 2 | 2 | 13 |
| United States | 192 | 89 | 88 | 103 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 6 | 0 | 0 | 6 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **5a54e040bb664441fb8a4bfa95c7348db27946fd99c5e762144dc1308cf95225**
- International-Playlist.m3u SHA-256: **649d07a3b17461e5e99879bed2563de5e9d4e74ca79495fd0fc32c5d873058e7**
