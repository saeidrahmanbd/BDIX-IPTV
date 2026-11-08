# EPG Research Inventory — IPTV-Playlist.m3u only

Generated: **2026-11-08T15:13:37+00:00**

Scope: IPTV-Playlist.m3u only. International-Playlist.m3u is out of scope and is not read.
Usable = a titled programme with stop at or after the generation time and start within 7 days.
Categories are exclusive: each channel is assigned the first failing stage listed below.

- IPTV-Playlist.m3u SHA-256: **4bb2bf08e6f01e3a0d601db0964c9678f3e376602df92c4a02f8c1ba5ba36aee**
- epg/epg.xml SHA-256: **8bb59fd91cf740d42ecbb988fce3fb93f6f829d43c5bf3a6f04c18f08a9f49e9**
- Active identities (excluding queue groups): **597**
- Usable now: **304**
- Channels needing research: **293** (check: 597 − 304 = 293)
- Mapped records in this inventory without a recorded source URL: **35**
- Mapped active IDs: **363**; duplicate epg_id values among them: **0**
- last_verified: UNKNOWN for every record; the mapping snapshot has no verification timestamps.

## Counts by category

| Category | Channels | Meaning | Recommended next action |
|---|---:|---|---|
| PUBLISHED_CHANNEL_NO_PROGRAMMES | 36 | XMLTV declares the channel but has no programme nodes. | Find a verified source for this tvg-id with programme nodes; verify identity before recording an epg_id. |
| NO_MAPPING_ROW | 0 | No mapping snapshot row for this tvg-id. | Search public sources for an exact or strongly verified ID; add only after identity review. |
| NO_SOURCE_MAPPING_ID | 217 | Mapping row exists, but no epg_id is recorded. | Research candidate IDs in public sources; keep ambiguous name matches in manual review. |
| SOURCE_NOT_VERIFIED_LATEST_FETCH | 14 | epg_id is recorded, but the latest fetch did not verify it. | Re-fetch the recorded source and confirm the ID and schedule; do not reuse it unverified. |
| SOURCE_MAPPED_NO_PUBLISHED_CHANNEL | 2 | epg_id is recorded, but no XMLTV channel exists for the tvg-id. | Confirm the epg_id in a fetched feed; publish only after it carries future programmes. |
| PROGRAMMES_EXPIRED | 23 | Programme nodes exist, and all are valid but ended before now. | Look for a current feed for the recorded epg_id; expired schedules are not a mapping error by themselves. |
| PROGRAMMES_INVALID_TIMESTAMPS | 0 | Programme nodes exist, but none has parseable start and stop times. | Inspect the source's timestamp format and offsets before using it. |
| PROGRAMMES_PLACEHOLDER_TITLES | 1 | Programme nodes have valid times, but every title is a placeholder or generic text. | Check the source's title quality; reject sources that only publish placeholder titles. |
| PROGRAMMES_FUTURE_BEYOND_7_DAYS | 0 | Programme nodes exist, but future ones start more than 7 days ahead, so none is usable in the window. | Check whether the source refreshes near-term schedules; do not extend the window to pass the check. |

## Counts by group

| Group | PUBLISHED_CHANNEL_NO_PROGRAMMES | NO_MAPPING_ROW | NO_SOURCE_MAPPING_ID | SOURCE_NOT_VERIFIED_LATEST_FETCH | SOURCE_MAPPED_NO_PUBLISHED_CHANNEL | PROGRAMMES_EXPIRED | PROGRAMMES_INVALID_TIMESTAMPS | PROGRAMMES_PLACEHOLDER_TITLES | PROGRAMMES_FUTURE_BEYOND_7_DAYS | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Bangladesh | 2 | 0 | 54 | 0 | 0 | 0 | 0 | 0 | 0 | 56 |
| Documentary & Wildlife | 5 | 0 | 10 | 5 | 0 | 6 | 0 | 0 | 0 | 26 |
| Indian Bangla | 5 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 13 |
| Indian Entertainment | 8 | 0 | 21 | 1 | 0 | 0 | 0 | 1 | 0 | 31 |
| Indian Movies | 3 | 0 | 16 | 2 | 0 | 6 | 0 | 0 | 0 | 27 |
| Indian Music | 5 | 0 | 10 | 0 | 0 | 1 | 0 | 0 | 0 | 16 |
| International | 6 | 0 | 32 | 2 | 1 | 2 | 0 | 0 | 0 | 43 |
| Kids | 0 | 0 | 15 | 3 | 0 | 5 | 0 | 0 | 0 | 23 |
| Pakistani | 0 | 0 | 13 | 0 | 0 | 0 | 0 | 0 | 0 | 13 |
| Religious | 2 | 0 | 16 | 0 | 1 | 0 | 0 | 0 | 0 | 19 |
| Sports | 0 | 0 | 22 | 1 | 0 | 3 | 0 | 0 | 0 | 26 |

## Manual review: non-BD tvg-country in the Bangladesh group

Country codes are not changed automatically. Each entry needs a review of whether it is a Bangladeshi diaspora service or incorrect metadata.
Bangladesh's unrestricted genre policy is unchanged.

Rows found: **10**

| tvg-id | tvg-country | Channel | Usable now |
|---|---|---|---|
| ATNBanglaUK.uk | GB | ATN Bangla UK | usable |
| ChannelEurope.uk | GB | Channel Europe | unusable |
| ChannelS.uk | GB | Channel S | unusable |
| ChannelS.uk@679aa9 | GB | Channel S UK | unusable |
| DesheBideshe.ca | CA | Deshe Bideshe | unusable |
| DeshiTV.ca@SD | CA | Deshi TV | unusable |
| DoyelTV.ca@SD | CA | Doyel TV | unusable |
| NRBTV.ca | CA | NRB TV | unusable |
| ThikanaTV.us | US | Thikana | unusable |
| TimeTelevision.us | US | Time Television | unusable |

## Full list

Candidate IDs are limited to the epg_id values already recorded in reports/epg-channel-mapping.csv.
Provenance fields are UNKNOWN where the mapping snapshot has no value. Full detail is in epg-research-inventory.csv.

| Category | Group | Channel | tvg-id | Recorded epg_id | Status | Source name | Declared in guide | Programme nodes |
|---|---|---|---|---|---|---|---|---:|
| NO_SOURCE_MAPPING_ID | Bangladesh | Ananda TV | AnandaTV.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Asian TV | AsianTV.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | ATN Bangla | ATNBangla.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | ATN News | ATNNews.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Bangla TV | BanglaTV.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Bangla Vision | BanglaVision.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Bengali Beats | BengaliBeats.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Bijoy TV | BijoyTV.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Boishakhi TV | BoishakhiTV.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | BTV Chattogram | BTVChattogram.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Channel 1 | Channel1.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Channel 24 | Channel24.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Channel 52 | Channel52.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Channel Europe | ChannelEurope.uk | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Channel I | ChannelI.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Channel S | ChannelS.uk | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Channel S UK | ChannelS.uk@679aa9 | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | DBC News | DBCNews.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Deepto TV | DeeptoTV.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Desh TV | DeshTV.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Deshe Bideshe | DesheBideshe.ca | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Deshi TV | DeshiTV.ca@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Doyel TV | DoyelTV.ca@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Duronto TV | DurontoTV.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Ekattor TV | EkattorTV.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Ekhon TV | EkhonTV.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Ekushey TV | EkusheyTV.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Enter TV | EnterTV.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | G Series Drama | GSeriesDrama.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | G TV | GaziTV.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Global TV | GlobalTV.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Independent TV | IndependentTV.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | JA TV | JATV.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Jago News 24 | JagoNews24.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Jalsha Bangla BD | JalshaBanglaBD.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Jamuna TV | JamunaTV.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Jonmobhumi TV | JonmobhumiTV.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| PUBLISHED_CHANNEL_NO_PROGRAMMES | Bangladesh | Maasranga TV | MaasrangaTV.bd | MaasrangaTV.bd | MAPPED_NOT_CURRENTLY_FOUND | UNKNOWN | yes | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | ME TV | METV.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Mohona TV | MohonaTV.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Movie Bangla | MovieBangla.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | My TV | MyTV.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Nagorik TV | NagorikTV.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | News 24 | News24.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Nexus TV | NexusTV.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | NRB TV | NRBTV.ca | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | NTV | NTV.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Probashi TV | ProbashiTV.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Rajdhani TV | RajdhaniTV.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| PUBLISHED_CHANNEL_NO_PROGRAMMES | Bangladesh | RTV | RTV.bd | RTV.bd | MAPPED_NOT_CURRENTLY_FOUND | UNKNOWN | yes | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | SA TV | SATV.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Somoy TV | SomoyNewsTV.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | SRK | SRK.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Star News | StarNews.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Thikana | ThikanaTV.us | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Bangladesh | Time Television | TimeTelevision.us | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| PUBLISHED_CHANNEL_NO_PROGRAMMES | Documentary & Wildlife | 4K Travel | Travel.us | 4K.TRAVEL.TV.distro | MAPPED_NOT_CURRENTLY_FOUND | UNKNOWN | yes | 0 |
| NO_SOURCE_MAPPING_ID | Documentary & Wildlife | Adventure Earth | AdventureEarth.us | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Documentary & Wildlife | Alone | Alone.us | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Documentary & Wildlife | Autentic Adventure Earth | AutenticAdventureEarth.us | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Documentary & Wildlife | Autentic History | AutenticHistory.de | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| PUBLISHED_CHANNEL_NO_PROGRAMMES | Documentary & Wildlife | Crime & Justice | CrimeJustice.us | plex.tv.Crime.&.Justice.plex | MAPPED_NOT_CURRENTLY_FOUND | UNKNOWN | yes | 0 |
| SOURCE_NOT_VERIFIED_LATEST_FETCH | Documentary & Wildlife | Crime Scene TV | CrimeSceneTV.us | IN24000030L | MAPPED_NOT_CURRENTLY_FOUND | UNKNOWN | yes | 7 |
| PROGRAMMES_EXPIRED | Documentary & Wildlife | Epic Crimes | EpicCrimes.in | IN8000171I | MAPPED | i.mjh.nz | yes | 7 |
| SOURCE_NOT_VERIFIED_LATEST_FETCH | Documentary & Wildlife | House of Crime | HouseOfCrime.us | IN4600004HW | MAPPED_NOT_CURRENTLY_FOUND | UNKNOWN | yes | 9 |
| SOURCE_NOT_VERIFIED_LATEST_FETCH | Documentary & Wildlife | InFast | INFAST.nl | INBA4900004W9 | USBA300022JX | MAPPED_NOT_CURRENTLY_FOUND | UNKNOWN | yes | 13 |
| NO_SOURCE_MAPPING_ID | Documentary & Wildlife | Inside Crime | InsideCrime.us | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| SOURCE_NOT_VERIFIED_LATEST_FETCH | Documentary & Wildlife | InWonder | InWonder.nl | INBA4900005PV | USBA300023G8 | MAPPED_NOT_CURRENTLY_FOUND | UNKNOWN | yes | 11 |
| PUBLISHED_CHANNEL_NO_PROGRAMMES | Documentary & Wildlife | Love the Planet | LoveThePlanet.us | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | yes | 0 |
| PROGRAMMES_EXPIRED | Documentary & Wildlife | Mysteries Xplored | USBB5200028MM | USBB5200028MM | MAPPED | i.mjh.nz | yes | 7 |
| NO_SOURCE_MAPPING_ID | Documentary & Wildlife | Mystery TV | MysteryTV.us | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Documentary & Wildlife | Nat Geo TV | NatGeoTV.us | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| PROGRAMMES_EXPIRED | Documentary & Wildlife | OuterSphere | OuterSphere.us | USBD1200007FE | MAPPED | i.mjh.nz | yes | 4 |
| NO_SOURCE_MAPPING_ID | Documentary & Wildlife | PBS Arts | PBSArts.us | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| PUBLISHED_CHANNEL_NO_PROGRAMMES | Documentary & Wildlife | Real Wild | RealWild.uk | RealWild.uk | MAPPED_NOT_CURRENTLY_FOUND | UNKNOWN | yes | 0 |
| PUBLISHED_CHANNEL_NO_PROGRAMMES | Documentary & Wildlife | Robot Wars by Mech+ | RobotWarsByMech.us | plex.tv.Robot.Wars.by.Mech+.plex | MAPPED_NOT_CURRENTLY_FOUND | UNKNOWN | yes | 0 |
| PROGRAMMES_EXPIRED | Documentary & Wildlife | Survivor | Survivor.us | US3900014MX | MAPPED | i.mjh.nz | yes | 7 |
| NO_SOURCE_MAPPING_ID | Documentary & Wildlife | Watch Mojo | WatchMojo.us | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| SOURCE_NOT_VERIFIED_LATEST_FETCH | Documentary & Wildlife | Wheel World | WheelWorld.us | IN460000250 | MAPPED_NOT_CURRENTLY_FOUND | UNKNOWN | yes | 13 |
| PROGRAMMES_EXPIRED | Documentary & Wildlife | Wild Flix Hindi | WildFlixHindi.in | IN460000585 | MAPPED | i.mjh.nz | yes | 9 |
| NO_SOURCE_MAPPING_ID | Documentary & Wildlife | Wild Planet | WildPlanet.us | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| PROGRAMMES_EXPIRED | Documentary & Wildlife | Witness to Justice | WitnessToJustice.us | US700010XK | MAPPED | i.mjh.nz | yes | 12 |
| PUBLISHED_CHANNEL_NO_PROGRAMMES | Indian Bangla | Amar Bangla | AamarBangla.in | Amar.Bangla.TV.in | AmarBanglaTV.in | jtv1962 | 1962 | MAPPED | avkb.short.gy, epgshare01.online, m3u-edit.com, raw.githubusercontent.com, www.open-epg.com | yes | 0 |
| NO_SOURCE_MAPPING_ID | Indian Bangla | Bangla Plus | BanglaPlus.in | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Indian Bangla | Jhankar TV | JhankarTV.ca | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| PUBLISHED_CHANNEL_NO_PROGRAMMES | Indian Bangla | KTV Bangla | KTVBangla.in@SD | jtv1891 | MAPPED | raw.githubusercontent.com | yes | 0 |
| NO_SOURCE_MAPPING_ID | Indian Bangla | Matribhumi TV | MatribhumiTV.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Indian Bangla | News 21 | News21BanglaTV.bd@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Indian Bangla | Orange Bangla TV | OrangeBanglaTV.in@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Indian Bangla | Sananda | SanandaTV.in | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Indian Bangla | SNB Cinema | SNBCinema.in | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| PUBLISHED_CHANNEL_NO_PROGRAMMES | Indian Bangla | Sonar Bangla | SonarBangla.in@SD | jtv3602 | MAPPED | raw.githubusercontent.com | yes | 0 |
| PUBLISHED_CHANNEL_NO_PROGRAMMES | Indian Bangla | Tara TV | TaraTV.in | Tara.TV.in | MAPPED_NOT_CURRENTLY_FOUND | UNKNOWN | yes | 0 |
| PUBLISHED_CHANNEL_NO_PROGRAMMES | Indian Bangla | ZB Cinema | ZBCinema.in | jtv3322 | 3322 | MAPPED_NOT_CURRENTLY_FOUND | UNKNOWN | yes | 0 |
| NO_SOURCE_MAPPING_ID | Indian Bangla | Zodiak TV | ZodiakTV.in@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| PUBLISHED_CHANNEL_NO_PROGRAMMES | Indian Entertainment | Aaryaa TV | AaryaaTV.in | jtv3395 | MAPPED | raw.githubusercontent.com | yes | 0 |
| NO_SOURCE_MAPPING_ID | Indian Entertainment | Asianet Middle East | AsianetMiddleEast.in@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Indian Entertainment | Baiscope TV | BaiscopeTV.in | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Indian Entertainment | C Malayalam TV | CMalayalamTV.ca@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Indian Entertainment | CCV | CCV.in@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Indian Entertainment | Colors MENA | ColorsMENA.in | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| PROGRAMMES_PLACEHOLDER_TITLES | Indian Entertainment | DD Chhattisgarh | DDChhattisgarh.in@SD | 154889 | ts1216 | MAPPED | avkb.short.gy, m3u-edit.com, raw.githubusercontent.com | yes | 25 |
| PUBLISHED_CHANNEL_NO_PROGRAMMES | Indian Entertainment | Ekamra Bharat Odia | EkamraBharatOdia.in@SD | ts1196 | Ekamra.Bharat.Odia.in | MAPPED_NOT_CURRENTLY_FOUND | UNKNOWN | yes | 0 |
| NO_SOURCE_MAPPING_ID | Indian Entertainment | Flowers US | Flowers.us | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Indian Entertainment | GTC Punjabi US | GTCPunjabi.in@US | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Indian Entertainment | Kairali Arabia | KairaliArabia.in | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Indian Entertainment | Kalika TV | KalikaTV.in@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Indian Entertainment | Kerala Vision | KeralaVision.in@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Indian Entertainment | Maha Punjabi | MahaPunjabi.in@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| PUBLISHED_CHANNEL_NO_PROGRAMMES | Indian Entertainment | Manoranjan Prime | ManoranjanPrime.in@SD | 154892 | 10000000075992492 | MAPPED_NOT_CURRENTLY_FOUND | UNKNOWN | yes | 0 |
| NO_SOURCE_MAPPING_ID | Indian Entertainment | MNTV (Tamil) | MarutamTV.in | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| PUBLISHED_CHANNEL_NO_PROGRAMMES | Indian Entertainment | NTC TV | NTCTV.in@SD | jtv3393 | MAPPED | raw.githubusercontent.com | yes | 0 |
| PUBLISHED_CHANNEL_NO_PROGRAMMES | Indian Entertainment | One Paschima | OnePaschima.in@SD | One.Paschima.in | MAPPED_NOT_CURRENTLY_FOUND | UNKNOWN | yes | 0 |
| NO_SOURCE_MAPPING_ID | Indian Entertainment | Pardesi TV | PardesiTV.ca | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Indian Entertainment | Pulari TV | PulariTV.in@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Indian Entertainment | Punjabi TV | PunjabiTV.in@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Indian Entertainment | Q TV | QTV.in | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Indian Entertainment | SADA TV | SADATV.in | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| SOURCE_NOT_VERIFIED_LATEST_FETCH | Indian Entertainment | Shemaroo Umang | ShemarooUmang.in@SD | ShemarooUmang.in | 143779 | SHEMAROO.UMANG.in | Shemaroo.Umang.in | jtv2078 | MAPPED_NOT_CURRENTLY_FOUND | UNKNOWN | yes | 1 |
| NO_SOURCE_MAPPING_ID | Indian Entertainment | Sooriyan TV | SooriyanTV.ca@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| PUBLISHED_CHANNEL_NO_PROGRAMMES | Indian Entertainment | Suriya TV | SuriyaTV.in | jtv3394 | 3394 | MAPPED | avkb.short.gy, raw.githubusercontent.com | yes | 0 |
| PUBLISHED_CHANNEL_NO_PROGRAMMES | Indian Entertainment | Suriyan TV | SuriyanTV.in@SD | ts1384 | MAPPED_NOT_CURRENTLY_FOUND | UNKNOWN | yes | 0 |
| NO_SOURCE_MAPPING_ID | Indian Entertainment | Swantham | Swantham.in@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Indian Entertainment | Thendral TV | ThendralTV.in@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Indian Entertainment | UTV Palakkad | UTVPalakkad.in@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| PUBLISHED_CHANNEL_NO_PROGRAMMES | Indian Entertainment | Zingabad | Zingabad.in@SD | 7258 | MAPPED_NOT_CURRENTLY_FOUND | UNKNOWN | yes | 0 |
| NO_SOURCE_MAPPING_ID | Indian Movies | B4U Bhojpuri Plus | B4UBhojpuri.in@Plus | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| SOURCE_NOT_VERIFIED_LATEST_FETCH | Indian Movies | Bollygold | Bollygold.in@HD | IN4000600Q | MAPPED_NOT_CURRENTLY_FOUND | UNKNOWN | yes | 1 |
| NO_SOURCE_MAPPING_ID | Indian Movies | Chhaya Chitram Telugu | ChhayaChitramTelugu.in@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| PUBLISHED_CHANNEL_NO_PROGRAMMES | Indian Movies | Ekamra Cinema | EkamraCinema.in | Ekamra.Cinema.in | MAPPED_NOT_CURRENTLY_FOUND | UNKNOWN | yes | 0 |
| NO_SOURCE_MAPPING_ID | Indian Movies | Goldmines 2 | Goldmines2.in@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Indian Movies | Goldmines Action | GoldminesAction.in | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| SOURCE_NOT_VERIFIED_LATEST_FETCH | Indian Movies | Goldmines Movies | GoldminesMovies.in@SD | 142881 | ts1499 | GoldminesMovies.in@SD | Goldmines.Movies.in | MAPPED_NOT_CURRENTLY_FOUND | UNKNOWN | yes | 1 |
| NO_SOURCE_MAPPING_ID | Indian Movies | Hindi Movie Classic 24 | new.hindi.movie.classic.24 | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Indian Movies | India Talkies | IndiaTalkies.in@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Indian Movies | Indywood TV | IndywoodTV.in@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Indian Movies | K Cine | KCine.in | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Indian Movies | Maha Movie | MahaMovie.in@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Indian Movies | Mango | Mango.in@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Indian Movies | MH One Movies | MHOneMovies.in@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Indian Movies | Movie Punjab | MoviePunjab.in@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| PUBLISHED_CHANNEL_NO_PROGRAMMES | Indian Movies | Namma Bangalore | NammaBangalore.in@SD | 3237 | Namma.Bangalore.in | jtv3237 | MAPPED_NOT_CURRENTLY_FOUND | UNKNOWN | yes | 0 |
| PROGRAMMES_EXPIRED | Indian Movies | NH Tamil Gold | NHTamilGold.in | IN400061DB | MAPPED | i.mjh.nz | yes | 3 |
| NO_SOURCE_MAPPING_ID | Indian Movies | Pravasi Channel | PravasiChannel.in@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| PUBLISHED_CHANNEL_NO_PROGRAMMES | Indian Movies | Public Movies | PublicMovies.in@SD | PublicMovies.in@SD | 143686 | 1633 | 577132 | LIVETV_LIVETVCHANNEL_PUBLIC_MOVIES | PUBLIC.MOVIES.in | Public.Movies.in | jtv1633 | ts661 | MAPPED_NOT_CURRENTLY_FOUND | UNKNOWN | yes | 0 |
| NO_SOURCE_MAPPING_ID | Indian Movies | Shubh Cinema TV | ShubhCinemaTV.in | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Indian Movies | Soneri Cinema | SoneriCinema.in@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Indian Movies | Sony Movies | SonyMovies.in | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| PROGRAMMES_EXPIRED | Indian Movies | South Station | SouthStation.in | IN3800008CX | MAPPED | i.mjh.nz | yes | 3 |
| PROGRAMMES_EXPIRED | Indian Movies | Thalaa TV | ThalaaTV.in@HD | 6601 | MAPPED | raw.githubusercontent.com | yes | 18 |
| PROGRAMMES_EXPIRED | Indian Movies | The Movie Club | TheMovieClub.in@HD | IN38000072R | MAPPED | i.mjh.nz | yes | 3 |
| PROGRAMMES_EXPIRED | Indian Movies | The Movie Club +2 | TheMovieClub.in@Plus2 | IN40000100Y | MAPPED | i.mjh.nz | yes | 3 |
| PROGRAMMES_EXPIRED | Indian Movies | Tolly TV | TollyTV.in | 6613 | MAPPED | raw.githubusercontent.com | yes | 19 |
| NO_SOURCE_MAPPING_ID | Indian Music | 7X Punjabi | 7XPunjabi.in | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Indian Music | AMN TV | AMNTV.in@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Indian Music | Andy Haryana | AndyHaryana.in@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Indian Music | Deewana | DeewanaHD.in | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| PUBLISHED_CHANNEL_NO_PROGRAMMES | Indian Music | Ekamra Musiq | EkamraMusiq.in | Ekamra.Musiq.in | MAPPED_NOT_CURRENTLY_FOUND | UNKNOWN | yes | 0 |
| PROGRAMMES_EXPIRED | Indian Music | ETV Beats | ETVBeats.in@HD | IN4900002RV | MAPPED | i.mjh.nz | yes | 3 |
| NO_SOURCE_MAPPING_ID | Indian Music | Hindi Hits | HindiHits.in | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| PUBLISHED_CHANNEL_NO_PROGRAMMES | Indian Music | Mastiii | Mastiii.in@SD | Mastiii.in | 143308 | MAPPED_NOT_CURRENTLY_FOUND | UNKNOWN | yes | 0 |
| NO_SOURCE_MAPPING_ID | Indian Music | Oli TV | OliTV.in@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| PUBLISHED_CHANNEL_NO_PROGRAMMES | Indian Music | Only Music | Only.Music.in | Only.Music.in | jtv903 | MAPPED | epgshare01.online, m3u-edit.com, raw.githubusercontent.com | yes | 0 |
| NO_SOURCE_MAPPING_ID | Indian Music | Punjabi Music | PunjabiMusicHD.in@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Indian Music | Rang Rangoli | RangRangoli.in | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| PUBLISHED_CHANNEL_NO_PROGRAMMES | Indian Music | Steelbird Music | SteelbirdMusic.in@SD | Steelbird.Music.in | MAPPED_NOT_CURRENTLY_FOUND | UNKNOWN | yes | 0 |
| PUBLISHED_CHANNEL_NO_PROGRAMMES | Indian Music | Ultimate TV | UltimateTV.in@SD | jtv3396 | MAPPED | raw.githubusercontent.com | yes | 0 |
| NO_SOURCE_MAPPING_ID | Indian Music | Vision Beats | VisionBeats.in@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Indian Music | YRF Music Nepal | YRFMusic.in@Nepal | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | International | 24 Hour Free Movies | custom.24hourfreemovies | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | International | 30A Music | custom.30amusic | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | International | 4ever Cinema | custom.4evercinema | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | International | 4ever Music | custom.4evermusic | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| PUBLISHED_CHANNEL_NO_PROGRAMMES | International | Action Hollywood Movies | plex.tv.Action.Hollywood.Movies.plex | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | yes | 0 |
| NO_SOURCE_MAPPING_ID | International | Afrobeats | Afrobeats.us | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| PUBLISHED_CHANNEL_NO_PROGRAMMES | International | AMC Thrillers | plex.tv.AMC.Thrillers.plex | plex.tv.AMC.Thrillers.plex | MAPPED_NOT_CURRENTLY_FOUND | UNKNOWN | yes | 0 |
| SOURCE_NOT_VERIFIED_LATEST_FETCH | International | Bang Bang TV | BangBangTV | 6590 | MAPPED_NOT_CURRENTLY_FOUND | UNKNOWN | yes | 3 |
| NO_SOURCE_MAPPING_ID | International | Baraza Music TV | custom.barazamusictv | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | International | CMC TV | custom.cmctv | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | International | Dance TV | DanceTV.us | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | International | DW News | DWNews.de | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | International | EU Music | custom.eumusic | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | International | FON Music | FONMusic.us | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | International | iFilm English | iFilmEnglish.ir | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | International | M20 Music | M20Music.us | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | International | Mix Hollywood | custom.mixhollywood | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | International | Movie Dome Family | MovieDomeFamily.us | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | International | Movies Thriller | MoviesThriller.sa@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | International | MovieSphere UK | custom.moviesphereuk | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | International | My Cinema | MyCinema.us | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| PROGRAMMES_EXPIRED | International | MyTime Movie Network East | MyTimeMovieNetworkEast.us | USBC3900018K6 | MAPPED | i.mjh.nz | yes | 5 |
| NO_SOURCE_MAPPING_ID | International | Ocko Expres | custom.ockoexpres | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | International | Oxygen Music | OxygenMusic.us | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | International | POP World TV | POPWorldTV.es | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| SOURCE_MAPPED_NO_PUBLISHED_CHANNEL | International | Radio Norba TV | RadionorbaTV.it | RADIONORBATV.it | RADIONORBA.TV.it | MAPPED | epgshare01.online, iptv-epg.org | no | 0 |
| NO_SOURCE_MAPPING_ID | International | Rakuten Movies | RakutenMovies | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | International | Rakuten TV Action Movies UK | RakutenTVActionMovies.es@UK | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | International | Rakuten TV Comedy Movies UK | RakutenTVComedyMovies.es@UK | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | International | Rakuten TV Family Movies UK | RakutenTVFamilyMovies.es@UK | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| PUBLISHED_CHANNEL_NO_PROGRAMMES | International | Shanson TV | ShansonTV.ru | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | yes | 0 |
| NO_SOURCE_MAPPING_ID | International | Sparkle Movies | GBAJ400042T1 | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| PUBLISHED_CHANNEL_NO_PROGRAMMES | International | Stingray The Spa | StingrayTheSpa.ca | StingrayTheSpa.ca | Stingray.The.Spa.ca2 | MAPPED | epgshare01.online, iptv-epg.org | yes | 0 |
| PUBLISHED_CHANNEL_NO_PROGRAMMES | International | Stingray Today's KPOP | StingrayTodaySKPOP.us | USBD3500016NH | MAPPED | i.mjh.nz | yes | 0 |
| PUBLISHED_CHANNEL_NO_PROGRAMMES | International | Stingray Today's Latin Pop | StingrayTodaysLatinPop.ca | USBD3500009Y3 | MAPPED_NOT_CURRENTLY_FOUND | UNKNOWN | yes | 0 |
| NO_SOURCE_MAPPING_ID | International | Totalmusic | Totalmusic.uk | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | International | Totalmusic Dance | custom.totalmusicdance | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | International | Trace UK | custom.traceuk | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | International | V2 Beat | custom.v2beat | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | International | Vevo Hip Hop & R&B | GBBD2300001C0 | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| SOURCE_NOT_VERIFIED_LATEST_FETCH | International | XITE Hits | XITEHits.nl | USBD3300004RH | MAPPED_NOT_CURRENTLY_FOUND | UNKNOWN | yes | 3 |
| PROGRAMMES_EXPIRED | International | XITE Just Chill | custom.xitejustchill | USBB2300003JZ | MAPPED | i.mjh.nz | yes | 4 |
| NO_SOURCE_MAPPING_ID | International | XITE Summer | custom.xitesummer | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Kids | ADN TV+ | ADNTVPlus.fr | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Kids | Afarin TV | AfarinTV.iq | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| PROGRAMMES_EXPIRED | Kids | Baby Shark TV | BabySharkTV.us | US17000208H | MAPPED | i.mjh.nz | yes | 12 |
| NO_SOURCE_MAPPING_ID | Kids | Bantul the Great | BantulTheGreat.us | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Kids | Doraemon TV | DoraemonTV.us | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Kids | Epic Kids Digital | EpicKidsDigital.us | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| PROGRAMMES_EXPIRED | Kids | Hooray Kids | custom.hooraykids | IN4600009F9 | MAPPED | i.mjh.nz | yes | 3 |
| SOURCE_NOT_VERIFIED_LATEST_FETCH | Kids | KidDo MATIX | KidDoMATIX.us | IN4600008T4 | MAPPED_NOT_CURRENTLY_FOUND | UNKNOWN | yes | 5 |
| NO_SOURCE_MAPPING_ID | Kids | Lego Channel | LegoChannel.us@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Kids | Moonbug Kids | MoonbugKids.uk | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| SOURCE_NOT_VERIFIED_LATEST_FETCH | Kids | Mr Bean Animated | MrBeanAnimated.uk | IN3000010V5 | US170002608 | MAPPED_NOT_CURRENTLY_FOUND | UNKNOWN | yes | 15 |
| NO_SOURCE_MAPPING_ID | Kids | Powerkids Kartoon Channel | PowerkidsKartoonChannel.us | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| PROGRAMMES_EXPIRED | Kids | RetroCrush | RetroCrush.us | USBC36000073J | MAPPED | i.mjh.nz | yes | 11 |
| NO_SOURCE_MAPPING_ID | Kids | Smurf TV | SmurfTV.us | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| PROGRAMMES_EXPIRED | Kids | Sonic The Hedgehog | custom.sonicthehedgehog | USBD3300020PM | MAPPED | i.mjh.nz | yes | 15 |
| PROGRAMMES_EXPIRED | Kids | Strawberry Shortcake | StrawberryShortcake.us | USBC4400012QS | MAPPED | i.mjh.nz | yes | 13 |
| SOURCE_NOT_VERIFIED_LATEST_FETCH | Kids | Teletubbies | Teletubbies.uk | USBD3500015R5 | MAPPED_NOT_CURRENTLY_FOUND | UNKNOWN | yes | 13 |
| NO_SOURCE_MAPPING_ID | Kids | Tom and Jerry | TomAndJerry.do | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Kids | Tooku | Tooku.ru | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Kids | Toon Goggles Junior | ToonGogglesJunior.us | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Kids | WOW Kidz Hindi | WOWKidz.in@Hindi | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Kids | WOW Kidz Tamil | WOWKidzTamil.in | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Kids | WOW Kidz Telugu | WOWKidz.in@Telugu | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Pakistani | 8XM | 8XM.pk@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Pakistani | aur LIFE | aurLIFE.pk | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Pakistani | Bol Entertainment | BolEntertainment.pk@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Pakistani | BS Film | BSFilm.pk@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Pakistani | Discover Pakistan | DiscoverPakistan.pk@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Pakistani | Falak TV | FalakTV.pk@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Pakistani | HUM Sitaray | HUMSitaray.pk | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Pakistani | Jalwa TV | JalwaTV.pk@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Pakistani | Joo Music | JooMusic.pk | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Pakistani | Paighan TV | PaighanTV.pk@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Pakistani | See TV | SeeTV.pk | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Pakistani | Tag TV | TagTV.pk | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Pakistani | Waseb TV | WasebTV.pk | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Religious | Al Quran Al Kareem TV | AlQuranAlKareemTV.sa | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Religious | Al-Zahra TV Turkic | AlZahraTVTurkic.sa | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Religious | ARY Q TV | ARYQTV.pk | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Religious | Azan TV | custom.azantv | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Religious | Bahrain Quran | BahrainQuran.bh | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| SOURCE_MAPPED_NO_PUBLISHED_CHANNEL | Religious | Eman Channel | EmanChannel | EmanChannel.uk | Eman.Channel.uk | MAPPED | epgshare01.online, iptv-epg.org, www.open-epg.com | no | 0 |
| PUBLISHED_CHANNEL_NO_PROGRAMMES | Religious | Iqraa TV | IqraaTV | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | yes | 0 |
| NO_SOURCE_MAPPING_ID | Religious | Islam Channel Bangla | custom.islamchannelbangla | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Religious | Islam TV | IslamTV.sa | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Religious | Islamic TV | IslamicTV.sa | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Religious | Madani TV | MadaniTV.sa | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Religious | Makkah Live | MakkahLive.sa | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| PUBLISHED_CHANNEL_NO_PROGRAMMES | Religious | Makkah TV | MakkahTV.sa | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | yes | 0 |
| NO_SOURCE_MAPPING_ID | Religious | Medina Live | MedinaLive.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Religious | Peace TV Bangla | PeaceTVBangla.ae | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Religious | Peace TV English | PeaceTVEnglish.ae | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Religious | Peace TV Urdu | PeaceTVUrdu.pk | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Religious | Quran TV | QuranTV.iq | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Religious | Zainabia Channel | ZainabiaChannel.sa | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Sports | A Sports | ASports.pk | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Sports | ACCDN | custom.accdn | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Sports | ATG Live | custom.atglive | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Sports | Bahrain Sports 2 | BahrainSports2.bh@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Sports | beIN Sports XTRA en Espanol | custom.beinsportsxtraenespanol | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| SOURCE_NOT_VERIFIED_LATEST_FETCH | Sports | FIFA+ | custom.fifa | IN270000230 | USBD12000255B | MAPPED_NOT_CURRENTLY_FOUND | UNKNOWN | yes | 4 |
| NO_SOURCE_MAPPING_ID | Sports | Fight Network | custom.fightnetwork | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| PROGRAMMES_EXPIRED | Sports | FITE 24/7 | FITE247.us@SD | FITE247.us | MAPPED | iptv-epg.org | yes | 7 |
| NO_SOURCE_MAPPING_ID | Sports | Goal TV | GoalTV.in | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Sports | Inter TV (Italy) | custom.intertv | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Sports | Kabaddi 24x7 | Kabaddi24x7.in@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Sports | MTRSPT1 | custom.mtrspt | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| PROGRAMMES_EXPIRED | Sports | Pac 12 Insider | custom.pac12insider | USBA300034DB | MAPPED | i.mjh.nz | yes | 8 |
| PROGRAMMES_EXPIRED | Sports | PGA Tour | PGATour.us@SD | US400001M2 | MAPPED | i.mjh.nz | yes | 3 |
| NO_SOURCE_MAPPING_ID | Sports | PK Sports | PKSports.pk@SD | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Sports | PTV Sports | PTVSports.pk | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Sports | Rally TV | custom.rallytv | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Sports | Realitatea Sportiva | custom.realitateasportiva | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Sports | Sportivnyy | custom.sportivnyy | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Sports | T Sports | TSports.bd | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Sports | TAPMAD | custom.tapmad | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Sports | TR Sport | custom.trsport | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Sports | Trace Sport | custom.tracesport | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Sports | TSN The Ocho | custom.tsntheocho | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Sports | TYC Sports | custom.tycsports | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |
| NO_SOURCE_MAPPING_ID | Sports | World of Freesports | custom.worldoffreesports | UNKNOWN | NO_GUIDE_HIT | UNKNOWN | no | 0 |

## Scripts and data needed for online source research

Nothing in this inventory has been fetched or verified online. Source discovery is a separate, online step.

- Data: IPTV-Playlist.m3u, epg/epg.xml, reports/epg-channel-mapping.csv, reports/epg-research-inventory.csv
- Discovery and probing: scripts/fetch_iptv_org_epg.py, scripts/probe_epg_sources_for_bangladesh.py, scripts/official_epg_sources.py
- Mapping augmentation: scripts/augment_epg_mapping_from_iptv_org.py, scripts/augment_epg_mapping_from_additional_sources.py, scripts/epg_mapping_policy.py
- Coverage and caching: scripts/epg_coverage.py, scripts/epg_source_cache.py
- Rights gate (must pass before any source is used): scripts/check_epg_source_rights.py
- Generation and publication: scripts/generate_epg.py, scripts/run_generate_epg.py, scripts/epg_publish_gate_v2.py, scripts/validate_epg_freshness.py
- Reports: reports/bangladesh-epg-source-audit.md, reports/epg-unmapped-audit.md, reports/epg-source-audit.md
