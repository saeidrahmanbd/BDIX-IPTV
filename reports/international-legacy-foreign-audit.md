# International legacy foreign entries: channel-by-channel audit

Scope: the 28 entries that fail the Movies/Music-only validator, excluding VIP TV. VIP TV is a separate, 29th failure. Nothing has been removed or relabelled. Stream URLs are not reproduced.

Evidence grades: **Web** = a source was found in web search; **Name only** = no source was found, so the decision rests on the name and declared metadata. Web search evidence is weak for these channels, so grades are conservative.

| # | Channel | tvg-id | Country | Group | Declared content | Evidence | Observed category | Recommended action |
|---|---|---|---|---|---|---|---|---|
| 1 | AXN (Brazil) | `AXN.br@SD` | BR | Brazil | Movies | Name and metadata only | AXN is a general entertainment brand. Playlist declares Movies. | Owner decision: general entertainment is outside Movie/Music-only. Remove or move to review. |
| 2 | Movie Music by Stingray | `custom.movie-music-by-stingray-ca-music` | CA | Canada | Music | Web: Stingray FAST "Movies and Music" brand exists | Stingray runs a FAST channel called Movie Music. The playlist declares Music, and the name combines Movies and Music. | Owner decision: confirm whether the combined Movies+Music channel is allowed. Keep if yes. |
| 3 | Canal Cine Dios | `custom.canal-cine-dios-co-movie` | CO | Colombia | Movies | Name only; no source found | Name suggests religious movies. Religious is prohibited for foreign countries. | Owner decision: religious movies. Likely remove or move to review. |
| 4 | MCI Television | `custom.mci-television-co-movie` | CO | Colombia | Movies | Name only; no source found | Declared Movies. Identity and category unverified. | Verify identity before any decision. Keep until verified. |
| 5 | AXN Black (United States) Czech Republic | `AXNBlack.us@CzechRepublic` | CZ | Czech Republic | Movies | Name only | AXN Black is a general entertainment feed. Declared Movies. | Owner decision as for AXN. |
| 6 | AXN CEE Czech Republic | `AXNCEE.es@CzechRepublic` | CZ | Czech Republic | Movies | Name only | AXN CEE is a general entertainment feed. Declared Movies. | Owner decision as for AXN. |
| 7 | Vos y TV | `custom.vos-y-tv-ec-music` | EC | Ecuador | Music | Web: no reliable source found | Declared Music. Identity and category unverified. | Verify identity and content before any decision. |
| 8 | Trace Gospel | `custom.trace-gospel-fr-music` | FR | France | Music | Web: TRACE Gospel is a Christian music channel (mytvguide listing) | Gospel music. Declared Music, but genre is Religious by name. | Owner decision: Christian music may count as Music. If not, remove or move to review. |
| 9 | Trace Gospel Nigeria and East Africa | `custom.trace-gospel-nigeria-and-east-africa-fr-music` | FR | France | Music | Web: TRACE Gospel regional feed (partnership with MultiChoice, capitalfm) | As Trace Gospel. Declared Music. | Owner decision as for Trace Gospel. |
| 10 | Trace Gospel Southern Africa | `custom.trace-gospel-southern-africa-fr-music` | FR | France | Music | Web: TRACE Gospel regional feed (bona.co.za reference) | As Trace Gospel. Declared Music. | Owner decision as for Trace Gospel. |
| 11 | AXN Black (United States) Hungary | `AXNBlack.us@Hungary` | HU | Hungary | Movies | Name only | AXN Black. Declared Movies. | Owner decision as for AXN. |
| 12 | AXN CEE | `AXNCEE.es@Hungary` | HU | Hungary | Movies | Name only | AXN CEE. Declared Movies. | Owner decision as for AXN. |
| 13 | Persiana Family | `custom.persiana-family-ir-movie` | IR | Iran | Movies | Web: Persiana is a Persian-language family/entertainment channel (lyngsat listing) | Family entertainment. Declared Movies. | Owner decision: general entertainment is outside Movie/Music-only. Remove or move to review. |
| 14 | Persiana Iranian | `custom.persiana-iranian-ir-movie` | IR | Iran | Movies | Web: Persiana network listing (lyngsat) | General Iranian entertainment. Declared Movies. | Owner decision as for Persiana Family. |
| 15 | Persiana Korea | `custom.persiana-korea-ir-movie` | IR | Iran | Movies | Web: Persiana Korea listing (lyngsat) | Korean-content entertainment. Declared Movies. | Owner decision as for Persiana Family. |
| 16 | Persiana Plus | `custom.persiana-plus-ir-movie` | IR | Iran | Movies | Web: Persiana + listing (lyngsat) | General entertainment. Declared Movies. | Owner decision as for Persiana Family. |
| 17 | AXN Black (United States) Poland | `AXNBlack.us@Poland` | PL | Poland | Movies | Name only | AXN Black. Declared Movies. | Owner decision as for AXN. |
| 18 | AXN Poland | `AXNPoland.pl@SD` | PL | Poland | Movies | Name only | AXN. Declared Movies. | Owner decision as for AXN. |
| 19 | AXN White (Poland) | `AXNWhite.pl@SD` | PL | Poland | Movies | Name only | AXN White. Declared Movies. | Owner decision as for AXN. |
| 20 | 3ABN Praise Him Music Network | `custom.3abn-praise-him-music-network-us-music` | US | United States | Music | Name only; 3ABN is a Christian broadcaster | Christian music. Declared Music, religious by name. | Owner decision as for Trace Gospel. |
| 21 | ABN Bible Movies Channel | `custom.abn-bible-movies-channel-us-movie` | US | United States | Movies | Name only | Religious movies. Declared Movies. | Owner decision as for Canal Cine Dios. |
| 22 | AXN Black (United States) | `AXNBlack.us@Bulgary` | US | United States | Movies | Name only | AXN Black. Declared Movies. | Owner decision as for AXN. |
| 23 | AXN Crime | `AXNCrime.us@SD` | US | United States | Movies | Name only | AXN Crime is a crime-drama general entertainment feed. Declared Movies. | Owner decision as for AXN. |
| 24 | AXN Latin America | `AXNLatinAmerica.us@CentralAmerica` | US | United States | Movies | Name only | AXN. Declared Movies. | Owner decision as for AXN. |
| 25 | AXN Latin America Andes | `AXNLatinAmerica.us@Andes` | US | United States | Movies | Name only | AXN. Declared Movies. | Owner decision as for AXN. |
| 26 | Harmony Gospel Music TV | `custom.harmony-gospel-music-tv-us-music` | US | United States | Music | Web: gospel music channel (search results inconclusive) | Gospel music. Declared Music, religious by name. | Owner decision as for Trace Gospel. |
| 27 | HMI PROMZ NEWS | `custom.hmi-promz-news-us-music` | US | United States | Music | Web: no source found | Name says News, which is prohibited for foreign countries. Metadata declares Music, which contradicts the name. | Metadata conflict. Remove or move to review unless verified as Music. |
| 28 | Paramount Network | `ParamountNetwork.us@East` | US | United States | Movies | Name only | Paramount Network is a general entertainment feed. Declared Movies. | Owner decision as for AXN. |

## Key findings

- All 28 fail the foreign Movies/Music-only policy under the current rules. No row was approved as Movies/Music by owner-verified evidence.
- Movies-declared AXN and Persiana entries are general entertainment brands, so they are outside the policy as written.
- Religious music and movies (Trace Gospel, 3ABN, Harmony Gospel, ABN Bible Movies, Canal Cine Dios) need an owner ruling on whether Christian music counts as Music.
- HMI PROMZ NEWS is internally contradictory (News name, Music metadata).
- VIP TV (Aruba) is a separate failure. SETAR's February 2026 lineup, the main Aruban provider, does not list VIP TV, so its identity is unverified. The exact-identity exception was reverted.

## Decisions requested

1. Confirm the policy reading for general entertainment (AXN, Persiana, Paramount) and religious music (Trace Gospel, 3ABN, Harmony Gospel).
2. Approve remove, move to review, or metadata correction for each row.
3. Confirm VIP TV: provide its source or approve removal. Any exception needs verified identity.
