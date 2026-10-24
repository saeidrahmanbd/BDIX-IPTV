# BD.IN-Playlist Organization Report

- Source: BD.IN-Playlist.m3u (772 entries before cleanup).
- Reference structure: IPTV-Playlist.m3u (category registry, canonical metadata and local logo assets).
- Organized output: 626 entries — 362 primary channel identities and 264 alternative streams in Backup.
- Unique stream URLs: 626; duplicate URLs remaining: 0.
- Rejected candidates: 146.
- Existing repository-local logos assigned: 500 of 626 entries.
- Missing local logo assets: 119 unique identities; 95 safe HTTPS source images queued for localization.
- No external logo URL or placeholder has been written into the playlist.
- Country/language metadata is copied from the reference where available; otherwise inferred from source group, channel identity or host. Unverified country values are left blank rather than fabricated.

## Rules applied

- Normalized channel display names and removed provider/quality decoration such as SkyM3U, [PAID], and trailing HD/FHD/SD tags.
- Removed duplicate stream URLs after stripping non-functional URL fragments such as #skym3u.dev.
- Kept one primary stream per channel identity; all alternative distinct streams are placed in Backup.
- Reused matching canonical metadata and authentic local logos from IPTV-Playlist.m3u where available.
- Excluded non-Bangladeshi news channels, Indian news/sports/religious channels, non-Islamic religious channels, radio/test/VOD candidates, proxy/worker hosts, and tokenized/signed URLs.
- Used standard Playlist Studio groups, current category order, and alphabetized names within groups.
- Preserved stream destinations except fragment removal; no channel was marked Not Playing without a stream test.

## Group counts

| Group | Entries |
|---|---:|
| Bangladesh | 80 |
| Indian Bangla | 46 |
| Indian Movies | 23 |
| Indian Music | 12 |
| Indian Entertainment | 25 |
| Pakistani | 6 |
| International | 74 |
| Documentary & Wildlife | 19 |
| Kids | 29 |
| Religious | 16 |
| Sports | 32 |
| Backup | 264 |

## Rejection counts

| Reason | Entries |
|---|---:|
| duplicate stream URL | 80 |
| Indian religious channel prohibited | 4 |
| Indian sports channel prohibited | 12 |
| non-Bangladesh news channel prohibited | 20 |
| non-Islamic religious channel prohibited | 5 |
| non-live/test/radio/VOD candidate | 1 |
| proxy/worker/invalid host | 8 |
| tokenized/signed stream URL | 8 |
| unsupported stream format | 3 |
| VOD/catch-up source | 5 |

## Missing local logos after repository lookup

- ✦●✦ BANGLADESH ✦●✦
- ✦●✦ IN BANGLA ✦●✦
- 4k Love Natural
- 9x Jalsha
- 9XM Music
- AAKAASH BANGLA
- Action Hollywood
- Albania Music
- AMAR BANGAL
- Amar Digital TV
- AMC TV
- Asian TV NF
- ATN Islamic TV
- ATN MUSIC TV
- Ayna TV NF
- Baallee
- Bahrain Sports 1
- Bangla channel
- Bangla Tv NF
- beIN SPORTS 4
- beIN SPORTS 5
- Boishakhi TV B
- BTV Lithuania
- BTV NF
- Cartoon Network HD +
- Channel 1 TV
- Channel Europe
- Channel S TV
- CN HD +
- CNA
- CNN BANGLA TV
- CP 24
- Dangal TV
- DANGAL2
- DEEN TV UK
- DEEPTO
- DESHE BIDESHE TV
- DHOOM MUSIC
- Discover
- Discover Pikstan
- DISCOVERY FHD BANGLA
- Discovery WiFi
- DTV
- Duronto
- ETV BANGAL
- ETV BANGLA
- Eurosports
- Fox 5
- Fox business
- Fox Weather
- GAAN BANGLA
- GAAN BANGLA-MUSIC
- Geography
- GOLDMINES MOVIE
- Gopal Bhar TV
- GTV
- Hindi Classic 24
- HK Music TV
- Hum
- IBTV USA
- iON TV
- ISLAM CHANNEL
- ITV BANGLA
- ITV MOVIE BANGLA
- Jalsha Movies 2
- Jalsha Movies 3
- KHUSBOO BANGLA
- Khushboo
- Korean TV
- LIFE TIME
- MANJARI TV
- MINI
- Music Mastii
- My Tv B
- NAT GEO HD BANGLA
- Nicktoons
- NK
- NTV UK
- OAN
- Oggy
- Oman Sports TV
- Party Universe
- Party Universe B
- Pix 11
- PTV WiFi
- RADBULL TV
- RANA MUSIC
- RANG TV
- SAGAMusic
- Song Max
- Sony Aath WiFi
- Sony Entertainment
- Sony One Hite
- South India Movie
- Space Toon
- Spice FM
- SRK Tv
- STAR JALSHA MOVIES
- Star Jalsha WiFi
- STAR JHALSA MOVIES
- Sun Bangla WiFi
- T Sports WiFi
- Ten Cricket
- TheQ
- TIME TV
- Tom & Jerry TV
- Travel XP English
- TSN 2
- TSN 3
- TV One Bangla
- TVC Arabic Kids
- TVCARiB Kids & Teens
- USA TV
- Weather SPY
- Wild
- Willow Sports
- Willow Sports 2
- Z Bangla WiFi
- ZB Cartun TV

## Automated logo localization

The workflow reads reports/bd-in-logo-sources.json, downloads and validates 95 safe HTTPS images, converts valid images to PNG, stores them in logos/, and updates tvg-logo to local URLs. Unavailable or invalid sources remain missing; no generic or fake fallback logos are generated.
