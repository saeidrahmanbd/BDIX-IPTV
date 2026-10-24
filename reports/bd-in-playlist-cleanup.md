# BD.IN-Playlist Fresh Audit Report

- Audit base: current manually edited playlist at `68a9d80607026c324ffdc73fd7e43ee30307ac92`.
- Source rows inspected: **470**.
- Final playlist: **461 entries** — **265 primary channel identities** and **196 alternative streams in Backup**.
- Unique stream URLs: **461**; duplicates remaining: **0**.
- Duplicate primary identities remaining: **0**.
- Rejected rows: **9**.
- Local repository logos assigned: **414 of 461 entries**. No external, placeholder, generated-fallback or `unused/` assets were used.
- Unique channel identities without a confidently matched local logo: **44**.

## Rules applied

- Reclassified channels by identity, country/origin and genre; did not blindly keep the old group.
- Indian Bengali channels were moved to Indian Bangla; Indian movies and music were separated into Indian Movies and Indian Music.
- Documentary/wildlife channels were placed in Documentary & Wildlife, kids/cartoon channels in Kids, and sports in Sports rather than International.
- Excluded Indian news, sports and religious channels, non-Islamic religious channels, radio, test/VOD/catch-up, proxy/worker and signed/tokenized stream candidates.
- Normalized stream/provider/quality labels and known aliases; merged duplicate primary identities. Each identity has one primary URL and distinct alternatives under Backup.
- Removed repeated stream URLs after stripping non-functional URL fragments.
- Reused local logo assets only when a real repository file matched the channel; unknown logos were left blank rather than guessed.
- Reused trusted reference EPG IDs and metadata when available, assigned unique IDs/channel numbers, and alphabetized entries within groups.

## Group counts

| Group | Entries |
|---|---:|
| Bangladesh | 52 |
| Indian Bangla | 22 |
| Indian Movies | 22 |
| Indian Music | 16 |
| Indian Entertainment | 20 |
| Pakistani | 4 |
| International | 39 |
| Documentary & Wildlife | 24 |
| Kids | 25 |
| Religious | 14 |
| Sports | 27 |
| Backup | 196 |

## Group corrections

| Correction | Primary identities affected |
|---|---:|
| Indian Bangla → Indian Movies | 5 |
| Indian Bangla → Indian Music | 3 |
| Indian Movies → Indian Entertainment | 3 |
| Indian Entertainment → Indian Bangla | 1 |
| Documentary & Wildlife → Indian Bangla | 1 |
| Bangladesh → Indian Bangla | 1 |
| Indian Music → Indian Movies | 1 |
| International → Indian Movies | 1 |
| Indian Entertainment → Indian Music | 1 |
| International → Documentary & Wildlife | 1 |
| Indian Bangla → Kids | 1 |

## Merged channel identities and alternatives

- **Ananda TV** — 6 distinct streams
- **Asian TV** — 6 distinct streams
- **ATN Bangla** — 6 distinct streams
- **ATN News** — 6 distinct streams
- **Bangla TV** — 3 distinct streams
- **Bangla Vision** — 3 distinct streams
- **Bijoy TV** — 2 distinct streams
- **Boishakhi TV** — 3 distinct streams
- **BTV National** — 2 distinct streams
- **BTV World** — 2 distinct streams
- **Channel 1** — 2 distinct streams
- **Channel 24** — 3 distinct streams
- **Channel I** — 3 distinct streams
- **Channel S** — 5 distinct streams
- **DBC News** — 4 distinct streams
- **Deepto TV** — 2 distinct streams
- **Desh TV** — 2 distinct streams
- **Deshe Bideshe** — 2 distinct streams
- **Duronto TV** — 2 distinct streams
- **Ekattor TV** — 4 distinct streams
- **Ekhon TV** — 3 distinct streams
- **Ekushey TV** — 5 distinct streams
- **Enter TV** — 2 distinct streams
- **Gazi TV** — 3 distinct streams
- **Global TV** — 4 distinct streams
- **Independent TV** — 2 distinct streams
- **Jago News 24** — 3 distinct streams
- **Jamuna TV** — 5 distinct streams
- **Maasranga TV** — 4 distinct streams
- **Matribhumi TV** — 4 distinct streams
- **Mohona TV** — 2 distinct streams
- **My TV** — 4 distinct streams
- **News 24** — 4 distinct streams
- **Nexus TV** — 3 distinct streams
- **NRB TV** — 2 distinct streams
- **NTV** — 8 distinct streams
- **RTV** — 4 distinct streams
- **SA TV** — 4 distinct streams
- **Somoy TV** — 4 distinct streams
- **Thikana** — 2 distinct streams
- **Aakaash Bangla** — 2 distinct streams
- **Channel 52** — 2 distinct streams
- **Colors Bangla** — 9 distinct streams
- **DD Bangla** — 2 distinct streams
- **Enter10 Bangla** — 8 distinct streams
- **ETV Bangla** — 2 distinct streams
- **ITV Bangla** — 2 distinct streams
- **Khushboo Bangla** — 2 distinct streams
- **Rongeen TV** — 2 distinct streams
- **Sony Aath** — 4 distinct streams
- **Star Jalsha** — 5 distinct streams
- **Sun Bangla** — 5 distinct streams
- **Zee Bangla** — 5 distinct streams
- **Zee Bangla Sonar** — 3 distinct streams
- **B4U Movies** — 4 distinct streams
- **Goldmines** — 2 distinct streams
- **Goldmines Movies** — 3 distinct streams
- **Jalsha Movies** — 7 distinct streams
- **Zee Bangla Cinema** — 3 distinct streams
- **Zee Cinema** — 3 distinct streams
- **9X Jalwa** — 3 distinct streams
- **9XM** — 2 distinct streams
- **Balle Balle** — 2 distinct streams
- **Dhoom Music Bangla** — 3 distinct streams
- **Mastiii** — 2 distinct streams
- **Sangeet Bangla** — 3 distinct streams
- **YRF Music** — 2 distinct streams
- **Colors** — 2 distinct streams
- **Dangal 2** — 2 distinct streams
- **Star Plus** — 2 distinct streams
- **Action Hollywood Movies** — 2 distinct streams
- **CNN** — 2 distinct streams
- **Adventure Earth** — 2 distinct streams
- **Animal Planet** — 3 distinct streams
- **Discovery** — 4 distinct streams
- **Discovery Bangla** — 2 distinct streams
- **HISTORY TV** — 2 distinct streams
- **Bantul the Great** — 2 distinct streams
- **Cartoon Network** — 3 distinct streams
- **Disney Channel** — 2 distinct streams
- **Doraemon TV** — 2 distinct streams
- **Motu Patlu** — 2 distinct streams
- **Mr Bean Animated** — 2 distinct streams
- **Oggy and the Cockroaches** — 2 distinct streams
- **Tom & Jerry TV** — 2 distinct streams
- **Zoo Moo** — 2 distinct streams
- **Iqra Bangla** — 3 distinct streams
- **Peace TV Bangla** — 2 distinct streams
- **QURAN** — 2 distinct streams
- **beIN SPORTS 1** — 2 distinct streams
- **beIN SPORTS XTRA** — 3 distinct streams
- **PTV Sports** — 2 distinct streams

## Rejections

| Reason | Count |
|---|---:|
| Indian news channel prohibited | 6 |
| radio channel | 3 |

## Missing local logos

- Aakaash Bangla
- Albania Music
- Amar Digital TV
- AMC TV
- Bahrain Sports 1
- beIN SPORTS 4
- beIN SPORTS 5
- Channel Europe
- CNA
- Dangal TV
- DEEN TV UK
- DTV
- Enter 10 Bangla
- ETV Bangla
- Fox 5
- Gopal Bhar TV
- Hindi Classic 24
- HK Music TV
- Hum
- IBTV USA
- iON TV
- ISLAM CHANNEL
- ITV Bangla
- Korean TV
- MINI
- Nicktoons
- NK
- OAN
- Pix 11
- RADBULL TV
- Rang TV
- Sony One Hits
- South Indian Movies
- SRK Tv
- STAR JALSHA MOVIES
- Ten Cricket
- TSN 2
- TSN 3
- TVC Arabic Kids
- USA TV
- Wild
- Willow Sports
- Willow Sports 2
- ZB Cartoon TV
