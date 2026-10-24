# BD.IN-Playlist Fresh Audit Report — Logo Repository Search

- Audit source: current playlist at `608789f258d1f50723ede6ce8a53b91b81b27074`.
- Final playlist: **460 entries**, **261 primary channels**, **199 backups**.
- Orphan backup entries: **0** (each backup resolves to a primary by normalized name or channel ID).
- Duplicate stream URLs: **0**. Duplicate primary identities: **0**. Invalid/external logo URLs: **0**.
- New repository logo matches applied to rows that previously had no logo: **18 rows**. Remaining unique primary identities without a reliable local logo: **22**.

## Existing local logos matched

| Channel | Logo asset |
|---|---|
| Amar Digital TV | `logos/amar-bangla-digital.png` |
| AMC TV | `logos/amc.png` |
| Dangal TV | `logos/dangal.png` |
| Hindi Classic 24 | `logos/hindi-movie-classic-24.png` |
| Rang TV | `logos/rang.png` |
| Hum | `logos/hum-tv.png` |
| HUM TV | `logos/hum-tv.png` |
| DEEN TV UK | `logos/deen-tv-576p.png` |
| South Indian Movies | `logos/south-movies.png` |
| iON TV UK | `logos/ion-tv-uk.png` |
| Sony One Hits Action | `logos/sony-one-hits-action.png` |
| SRK TV | `logos/srk.png` |
| Ten Cricket | `logos/nvisionbd-official-pk-ten-cricket.png` |
| Willow Sports | `logos/us-willow-sports-hd.png` |
| Willow Sports 2 | `logos/us-willow-sports-hd.png` |
| ZB Cartoon TV | `logos/zb-cartoon.png` |
| TSN 2 | `logos/nvisionbd-official-tsn-aq1.png` |
| TSN 3 | `logos/nvisionbd-official-tsn-aq1.png` |
| Red Bull TV | `logos/red-bull-tv.png` |
| HUM TV | `logos/hum-tv.png` |
| iON TV UK | `logos/ion-tv-uk.png` |
| SRK TV | `logos/srk.png` |

## Rule-based removal

- Removed 1 row(s) labeled `NK` / referencing the Republic Bangla FAST playlist path. The stream path identifies an Indian news feed, which violates the repository's no-Indian-news rule; it was not assigned the unrelated `nk-tv-bangla.png` logo.

## Missing logos — no reliable asset match

- Aakaash Bangla
- Albania Music
- Bahrain Sports 1
- beIN SPORTS 4
- beIN SPORTS 5
- Channel Europe
- CNA
- DTV
- ETV Bangla
- Fox 5
- Gopal Bhar TV
- HK Music TV
- IBTV USA
- ISLAM CHANNEL
- ITV Bangla
- Korean TV
- MINI
- Nicktoons
- OAN
- Pix 11
- TVC Arabic Kids
- USA TV

## Repository search notes

- Searched all **2999** image assets in `logos/`, including nested folders.
- Exact logo assets under `logos/unused/` were deliberately not used. Logo matches were assigned only from active repository logo paths, not placeholders or generated fallback files.
- Lookalike but different channels (for example Aakaash Aath vs Aakaash Bangla, Islam TV vs ISLAM CHANNEL, and Bahrain Sports 2 vs Bahrain Sports 1) were left unmatched to avoid incorrect logos.
