# EPG Coverage & Mapping Report

Generated: **2026-10-22T04:22:12+00:00**

This report audits active unique channel identities across the playlist files in the repository. A source mapping is not counted as usable current/future coverage unless it has a valid programme interval and valid non-empty multilingual title data within the generator's -6-hour/+7-day window; English titles rank first, then Bengali, then other valid languages.
The XMLTV guide is published at **epg/epg.xml**. The published guide uses the playlist's tvg-id as the XMLTV channel ID, not the upstream provider's source ID.

## Overall Coverage

- Active unique playlist channel IDs audited: **680**
- IDs with an EPG source mapping: **460/680 (67.6%)**
- IDs with usable current/future source schedules (nonblank multilingual titles (English preferred, then Bengali, then other valid languages)): **442/680 (65.0%)**
- IDs with no EPG source mapping: **220**

## Coverage by Playlist Group

| Group | Active IDs | Mapped IDs | Current/future | No mapping |
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

## Source Status

- **FAILED** — https://free-epg.de/api/epg/bd.xml.gz — 0 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window; HTTP Error 404: Not Found
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_IN1.xml.gz — 1166 channel IDs; 771 IDs with usable current/future programmes; 75436 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_IN2.xml.gz — 54 channel IDs; 2 IDs with usable current/future programmes; 21 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz — 557 channel IDs; 530 IDs with usable current/future programmes; 15523 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-in.xml.gz — 415 channel IDs; 415 IDs with usable current/future programmes; 56957 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://i.mjh.nz/SamsungTVPlus/in.xml — 206 channel IDs; 199 IDs with usable current/future programmes; 2233 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://i.mjh.nz/SamsungTVPlus/us.xml — 585 channel IDs; 585 IDs with usable current/future programmes; 5008 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epg.pw/xmltv/epg_IN.xml — 528 channel IDs; 528 IDs with usable current/future programmes; 19671 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epg.pw/api/epg.xml?channel_id=9374 — 1 channel IDs; 1 IDs with usable current/future programmes; 81 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epg.pw/api/epg.xml?channel_id=12504 — 1 channel IDs; 1 IDs with usable current/future programmes; 72 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml — 692 channel IDs; 638 IDs with usable current/future programmes; 62716 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz — 717 channel IDs; 716 IDs with usable current/future programmes; 21661 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml — 762 channel IDs; 761 IDs with usable current/future programmes; 83996 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml — 1490 channel IDs; 1420 IDs with usable current/future programmes; 87303 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/yupptv.xml — 282 channel IDs; 282 IDs with usable current/future programmes; 6327 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/zee5.xml — 112 channel IDs; 98 IDs with usable current/future programmes; 19570 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://avkb.short.gy/epg.xml.gz — 2073 channel IDs; 766 IDs with usable current/future programmes; 22302 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://avkb.short.gy/jioepg.xml.gz — 1279 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://avkb.short.gy/tsepg.xml.gz — 717 channel IDs; 716 IDs with usable current/future programmes; 21661 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_DISTROTV1.xml.gz — 90 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz — 690 channel IDs; 685 IDs with usable current/future programmes; 58878 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_RAKUTEN1.xml.gz — 1640 channel IDs; 1510 IDs with usable current/future programmes; 111634 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/nasimali/epg-auto/release/main-epg/epg_data/merged_epg.xml — 11 channel IDs; 10 IDs with usable current/future programmes; 1568 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz — 486 channel IDs; 385 IDs with usable current/future programmes; 22032 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://www.open-epg.com/files/unitedkingdom.xml.gz — 562 channel IDs; 535 IDs with usable current/future programmes; 18740 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz — 769 channel IDs; 753 IDs with usable current/future programmes; 45171 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-us.xml.gz — 12991 channel IDs; 12967 IDs with usable current/future programmes; 921709 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_AE1.xml.gz — 804 channel IDs; 632 IDs with usable current/future programmes; 38049 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_AU1.xml.gz — 345 channel IDs; 280 IDs with usable current/future programmes; 37909 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz — 696 channel IDs; 695 IDs with usable current/future programmes; 48845 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_CH1.xml.gz — 751 channel IDs; 730 IDs with usable current/future programmes; 48626 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_CZ1.xml.gz — 1087 channel IDs; 531 IDs with usable current/future programmes; 31376 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_DE1.xml.gz — 266 channel IDs; 250 IDs with usable current/future programmes; 21315 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_DO1.xml.gz — 56 channel IDs; 55 IDs with usable current/future programmes; 2269 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_ES1.xml.gz — 373 channel IDs; 339 IDs with usable current/future programmes; 17832 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_FR1.xml.gz — 574 channel IDs; 517 IDs with usable current/future programmes; 38914 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_GR1.xml.gz — 321 channel IDs; 304 IDs with usable current/future programmes; 16668 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_HK1.xml.gz — 143 channel IDs; 133 IDs with usable current/future programmes; 11033 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_HU1.xml.gz — 193 channel IDs; 166 IDs with usable current/future programmes; 18507 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_IT1.xml.gz — 195 channel IDs; 154 IDs with usable current/future programmes; 11360 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_MY1.xml.gz — 163 channel IDs; 131 IDs with usable current/future programmes; 7306 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_MX1.xml.gz — 178 channel IDs; 168 IDs with usable current/future programmes; 9878 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_NL1.xml.gz — 159 channel IDs; 158 IDs with usable current/future programmes; 18037 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_PL1.xml.gz — 636 channel IDs; 584 IDs with usable current/future programmes; 89376 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_RO1.xml.gz — 370 channel IDs; 354 IDs with usable current/future programmes; 25839 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_SA2.xml.gz — 31 channel IDs; 30 IDs with usable current/future programmes; 3424 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_TR1.xml.gz — 178 channel IDs; 141 IDs with usable current/future programmes; 10056 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_BEIN1.xml.gz — 80 channel IDs; 66 IDs with usable current/future programmes; 2211 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_BR1.xml.gz — 266 channel IDs; 108 IDs with usable current/future programmes; 13939 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_BR2.xml.gz — 97 channel IDs; 92 IDs with usable current/future programmes; 6355 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://hum.tv/schedule/ — 1 channel IDs; 1 IDs with usable current/future programmes; 21 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epg.lat/files/in.xml.gz — 1166 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epg.lat/files/us.xml.gz — 4456 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://www.free-epg.de/api/epg/in.xml.gz — 2289 channel IDs; 436 IDs with usable current/future programmes; 57536 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://www.free-epg.de/api/epg/us.xml.gz — 6006 channel IDs; 5476 IDs with usable current/future programmes; 52197 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://www.open-epg.com/files/india.xml.gz — 1184 channel IDs; 814 IDs with usable current/future programmes; 46601 eligible programme rows with valid non-empty titles in any language in the guide window

## Channels Requiring Attention

The table includes every active channel identity without usable current/future guide data, not only Indian channels. NO_GUIDE_HIT means no configured source could be matched; MAPPED_ID_ONLY means an identity was found but no usable schedule was available; MAPPED_NOT_CURRENTLY_FOUND means a retained mapping was not found in the currently configured feeds.

| Group | Channel | Playlist ID | EPG source ID | Status |
|---|---|---|---|---|
| Bangladesh | Ananda TV | AnandaTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Asian TV | AsianTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | ATN Bangla | ATNBangla.bd | - | NO_GUIDE_HIT |
| Bangladesh | ATN News | ATNNews.bd | - | NO_GUIDE_HIT |
| Bangladesh | Bangla TV | BanglaTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Bangla Vision | BanglaVision.bd | - | NO_GUIDE_HIT |
| Bangladesh | Bengali Beats | custom.bengali.beats | - | NO_GUIDE_HIT |
| Bangladesh | Bijoy TV | BijoyTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | BOISHAKHAI TV HD | custom.bdix.boishakhai | - | NO_GUIDE_HIT |
| Bangladesh | Boishakhi TV | BoishakhiTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | BTV Chattogram | BTVChattogram.bd | - | NO_GUIDE_HIT |
| Bangladesh | BTV CTG | custom.bdix.btvctg | - | NO_GUIDE_HIT |
| Bangladesh | BTV National | BTVNational.bd | - | NO_GUIDE_HIT |
| Bangladesh | BTV News | custom.btv.news | - | NO_GUIDE_HIT |
| Bangladesh | Channel 1 | custom.channel.1 | - | NO_GUIDE_HIT |
| Bangladesh | Channel 16 | custom.channel.16 | - | NO_GUIDE_HIT |
| Bangladesh | Channel 24 | Channel24.bd | - | NO_GUIDE_HIT |
| Bangladesh | Channel 52 | custom.channel.52 | - | NO_GUIDE_HIT |
| Bangladesh | Channel 9 | Channel9.bd | - | NO_GUIDE_HIT |
| Bangladesh | Channel I | ChannelI.bd | - | NO_GUIDE_HIT |
| Bangladesh | Channel S | ChannelS.uk | - | NO_GUIDE_HIT |
| Bangladesh | DBC News | DBCNews.bd | - | NO_GUIDE_HIT |
| Bangladesh | Deepto TV | DeeptoTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Desh TV | DeshTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Deshe Bideshe | custom.deshe.bideshe | - | NO_GUIDE_HIT |
| Bangladesh | Deshi TV | DeshiTV.ca@SD | - | NO_GUIDE_HIT |
| Bangladesh | Doyel TV | DoyelTV.ca@SD | - | NO_GUIDE_HIT |
| Bangladesh | Duronto TV | DurontoTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Ekattor TV | EkattorTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Ekhon TV | EkhonTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Ekushey TV | EkusheyTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Enter TV | custom.enter.tv | - | NO_GUIDE_HIT |
| Bangladesh | G Series Drama | custom.gseriesdrama | - | NO_GUIDE_HIT |
| Bangladesh | G TV | GaziTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | GAZI TV HD | custom.bdix.gazi | - | NO_GUIDE_HIT |
| Bangladesh | Global TV | GlobalTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Green TV | GreenTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Independent TV | IndependentTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Jago News 24 | JagoNews24.bd | - | NO_GUIDE_HIT |
| Bangladesh | Jamuna TV | JamunaTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Jonmobhumi TV | custom.jonmobhumitv | - | NO_GUIDE_HIT |
| Bangladesh | Maasranga TV | MaasrangaTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Matribhumi TV | MatribhumiTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | ME TV | METV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Mohona TV | MohonaTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Movie Bangla | MovieBangla.bd | - | NO_GUIDE_HIT |
| Bangladesh | My TV | MyTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Nagorik TV | NagorikTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | News 21 | News21BanglaTV.bd@SD | - | NO_GUIDE_HIT |
| Bangladesh | News 24 | News24.bd | - | NO_GUIDE_HIT |
| Bangladesh | Nexus TV | NexusTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | NRB TV | NRBTV.ca | - | NO_GUIDE_HIT |
| Bangladesh | NTV | NTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Probashi TV | custom.probashitv | - | NO_GUIDE_HIT |
| Bangladesh | Rajdhani TV | RajdhaniTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Rajdhani TV | custom.rajdhanitv | - | NO_GUIDE_HIT |
| Bangladesh | RTV | RTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | SA TV | SATV.bd | - | NO_GUIDE_HIT |
| Bangladesh | SATV HD | custom.bdix.satv | - | NO_GUIDE_HIT |
| Bangladesh | Somoy TV | SomoyNewsTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | SRK | custom.srk | - | NO_GUIDE_HIT |
| Bangladesh | Star News | custom.star.news | - | NO_GUIDE_HIT |
| Bangladesh | TBN24 | TBN24.us | - | NO_GUIDE_HIT |
| Bangladesh | Time Television | TimeTelevision.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | 4K Travel | custom.4k.travel | 4K.TRAVEL.TV.distro | MAPPED_ID_ONLY |
| Documentary & Wildlife | Adventure Earth | custom.adventure.earth | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Alone | custom.alone | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Amazing Discoveries TV | custom.amazing.discoveries.tv | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Autentic Adventure Earth | custom.autentic.adventure.earth | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Autentic History | AutenticHistory.de | - | NO_GUIDE_HIT |
| Documentary & Wildlife | DISCOVERY BANGLA | custom.bdix.discoverybangla | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Documentary+ 2 | custom.documentary.2 | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Documentary+ USA | custom.documentary.usa | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Inside Crime | InsideCrime.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Mystery TV | MysteryTV.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | PBS Arts | custom.pbsarts | - | NO_GUIDE_HIT |
| Documentary & Wildlife | RT Documentary | RTDocumentary.ru | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Terra Mater WILD English | custom.terra.mater.wild.english | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Watch Mojo (EU) | custom.watch.mojo.eu | - | NO_GUIDE_HIT |
| Documentary & Wildlife | WaterBear | WaterBear.ch | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Wild Planet | custom.wild.planet | - | NO_GUIDE_HIT |
| Indian Bangla | Tara TV | custom.taratv | Tara.TV.in | MAPPED_ID_ONLY |
| Indian Bangla | Bangla Plus | BanglaPlus.in | - | NO_GUIDE_HIT |
| Indian Bangla | Jalsha Bangla BD | custom.jalsha.bangla.bd | - | NO_GUIDE_HIT |
| Indian Bangla | Jhankar TV | JhankarTV.ca | - | NO_GUIDE_HIT |
| Indian Bangla | JTV Bangla | JTVBangla.in@SD | - | NO_GUIDE_HIT |
| Indian Bangla | JTV Classic | custom.jtv.classic | - | NO_GUIDE_HIT |
| Indian Bangla | Orange Bangla TV | OrangeBanglaTV.in@SD | - | NO_GUIDE_HIT |
| Indian Bangla | Sananda | SanandaTV.in | - | NO_GUIDE_HIT |
| Indian Bangla | SNB Cinema | custom.snb.cinema | - | NO_GUIDE_HIT |
| Indian Bangla | Star Bangla | custom.starbangla | - | NO_GUIDE_HIT |
| Indian Entertainment | Manoranjan Prime | ManoranjanPrime.in@SD | 154892 | MAPPED_ID_ONLY |
| Indian Entertainment | One Paschima | OnePaschima.in@SD | One.Paschima.in | MAPPED_ID_ONLY |
| Indian Entertainment | Prarthana TV | PrarthanaTV.in@SD | Prarthana.TV.in | MAPPED_ID_ONLY |
| Indian Entertainment | Sony Entertainment TV | SonyEntertainmentTelevision.in@SD | Sony.Entertainment.Television.in | MAPPED_ID_ONLY |
| Indian Entertainment | Suriyan TV | SuriyanTV.in@SD | ts1384 | MAPPED_ID_ONLY |
| Indian Entertainment | Odisha TV | OdishaTV.in@SD | OdishaTV.in | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Entertainment | Baiscope TV | custom.baiscope.tv | - | NO_GUIDE_HIT |
| Indian Entertainment | C Malayalam TV | CMalayalamTV.ca@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Colors MENA | custom.colors.mena | - | NO_GUIDE_HIT |
| Indian Entertainment | Flowers US | custom.flowers.us | - | NO_GUIDE_HIT |
| Indian Entertainment | Kairali Arabia | KairaliArabia.in | - | NO_GUIDE_HIT |
| Indian Entertainment | Kerala Vision | KeralaVision.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Mei Alai TV | MeiAlaiTV.in | - | NO_GUIDE_HIT |
| Indian Entertainment | MH One Prime | Mh1Prime.in | - | NO_GUIDE_HIT |
| Indian Entertainment | MNTV (Tamil) | MarutamTV.in | - | NO_GUIDE_HIT |
| Indian Entertainment | NKR TV Kannada | NKRTVKannada.in | - | NO_GUIDE_HIT |
| Indian Entertainment | Oli TV | OliTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Pardesi TV | PardesiTV.ca | - | NO_GUIDE_HIT |
| Indian Entertainment | Pulari TV | PulariTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Q TV | QTV.in | - | NO_GUIDE_HIT |
| Indian Entertainment | SADA TV | SADATV.in | - | NO_GUIDE_HIT |
| Indian Entertainment | Sooriyan TV | SooriyanTV.ca@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Starnet | Starnet.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Swantham | Swantham.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | UTV Palakkad | UTVPalakkad.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | Ekamra Cinema | custom.ekamra.cinema | Ekamra.Cinema.in | MAPPED_ID_ONLY |
| Indian Movies | Bangla Cinema | custom.banglacinema | - | NO_GUIDE_HIT |
| Indian Movies | Goldmines 2 | Goldmines2.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | Goldmines Action | GoldminesAction.in | - | NO_GUIDE_HIT |
| Indian Movies | Hindi Movie Classic 24 | new.hindi.movie.classic.24 | - | NO_GUIDE_HIT |
| Indian Movies | Indywood TV | IndywoodTV.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | K Cine | custom.kcine | - | NO_GUIDE_HIT |
| Indian Movies | Maha Movie | MahaMovie.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | Mango | Mango.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | MH One Movies | MHOneMovies.in | - | NO_GUIDE_HIT |
| Indian Movies | Shubh Cinema TV | ShubhCinemaTV.in | - | NO_GUIDE_HIT |
| Indian Movies | South Movies | custom.south.movies | - | NO_GUIDE_HIT |
| Indian Music | Ekamra Musiq | custom.ekamra.musiq | Ekamra.Musiq.in | MAPPED_ID_ONLY |
| Indian Music | Mastiii | Mastiii.in@SD | Mastiii.in | MAPPED_ID_ONLY |
| Indian Music | Steelbird Music | SteelbirdMusic.in@SD | Steelbird.Music.in | MAPPED_ID_ONLY |
| Indian Music | 7X Punjabi | custom.7x.punjabi | - | NO_GUIDE_HIT |
| Indian Music | Andy Haryana | AndyHaryana.in@SD | - | NO_GUIDE_HIT |
| Indian Music | Deewana | DeewanaHD.in | - | NO_GUIDE_HIT |
| Indian Music | Hindi Hits | HindiHits.in | - | NO_GUIDE_HIT |
| Indian Music | Rang Rangoli | custom.rang.rangoli | - | NO_GUIDE_HIT |
| Indian Music | YRF Music Nepal | YRFMusic.in@Nepal | - | NO_GUIDE_HIT |
| International | BBC Drama | BBCDrama.uk | BBCDrama.au | MAPPED_ID_ONLY |
| International | Fashion One | FashionOne.uk | Fashion.One.cz | MAPPED_ID_ONLY |
| International | Shanson TV | ShansonTV.ru | Shanson.TV.cz | MAPPED_ID_ONLY |
| International | 1Mus | custom.1mus | - | NO_GUIDE_HIT |
| International | Afrobeats | custom.afrobeats | - | NO_GUIDE_HIT |
| International | AMG TV Classic | custom.amgtvclassic | - | NO_GUIDE_HIT |
| International | Arabica TV | custom.arabicatv | - | NO_GUIDE_HIT |
| International | AVA FAMILY | custom.ava.family | - | NO_GUIDE_HIT |
| International | AVA SERIES | custom.ava.series | - | NO_GUIDE_HIT |
| International | CANADA ONE | custom.bdix.canadaone | - | NO_GUIDE_HIT |
| International | CBS TV | custom.cbs.tv | - | NO_GUIDE_HIT |
| International | Classic Movies | custom.classic.movies | - | NO_GUIDE_HIT |
| International | Dance TV | custom.dancetv | - | NO_GUIDE_HIT |
| International | Digital Fashion | custom.digitalfashion | - | NO_GUIDE_HIT |
| International | DW News | DWNews.de | - | NO_GUIDE_HIT |
| International | FON Music | custom.fon.music | - | NO_GUIDE_HIT |
| International | iFilm English | iFilmEnglish.ir | - | NO_GUIDE_HIT |
| International | Kronehit | custom.kronehit | - | NO_GUIDE_HIT |
| International | M20 Music | custom.m20.music | - | NO_GUIDE_HIT |
| International | MBC Drama USA | MBCDramaUSA.us | - | NO_GUIDE_HIT |
| International | Mei Ah Movie Channel | MeiAhMovieChannel.hk | - | NO_GUIDE_HIT |
| International | Movie Dome Family | custom.moviedomefamily | - | NO_GUIDE_HIT |
| International | Movies Thriller | MoviesThriller.sa@SD | - | NO_GUIDE_HIT |
| International | My Cinema | MyCinema.us | - | NO_GUIDE_HIT |
| International | MyTime Movie | MyTimeMovieNetwork.uk@SD | - | NO_GUIDE_HIT |
| International | MyTime Movie Network East | MyTimeMovieNetworkEast.us | - | NO_GUIDE_HIT |
| International | Oxygen Music | custom.oxygen.music | - | NO_GUIDE_HIT |
| International | POP World TV | POPWorldTV.es | - | NO_GUIDE_HIT |
| International | PowerTürk TV | PowerTurkTV.tr | - | NO_GUIDE_HIT |
| International | Rakuten Movies | RakutenMovies | - | NO_GUIDE_HIT |
| International | Rakuten TV Action Movies UK | RakutenTVActionMovies.es@UK | - | NO_GUIDE_HIT |
| International | Rakuten TV Comedy Movies UK | RakutenTVComedyMovies.es@UK | - | NO_GUIDE_HIT |
| International | Rakuten TV Drama Movies UK | RakutenTVDramaMovies.es@UK | - | NO_GUIDE_HIT |
| International | Rakuten TV Family Movies UK | RakutenTVFamilyMovies.es@UK | - | NO_GUIDE_HIT |
| International | Sony Movies | SonyMovies.in | - | NO_GUIDE_HIT |
| International | Sparkle Movies | GBAJ400042T1 | - | NO_GUIDE_HIT |
| International | Stingray Rock Alternative | StingrayRockAlternative.ca | - | NO_GUIDE_HIT |
| International | Teleritmo | custom.teleritmo | - | NO_GUIDE_HIT |
| International | Totalmusic | Totalmusic.uk | - | NO_GUIDE_HIT |
| International | Trace UK | TraceUK.uk | - | NO_GUIDE_HIT |
| International | Vevo '70s & '80s | custom.vevo.70s.80s | - | NO_GUIDE_HIT |
| International | Vevo '90s & '00s | custom.vevo.90s.00s | - | NO_GUIDE_HIT |
| International | Vevo Hip Hop & R&B | GBBD2300001C0 | - | NO_GUIDE_HIT |
| International | XITE Hits UK | XITEHits.nl@UK | - | NO_GUIDE_HIT |
| International | Young Hollywood | custom.young.hollywood | - | NO_GUIDE_HIT |
| Kids | ADN TV+ | ADNTVPlus.fr | - | NO_GUIDE_HIT |
| Kids | Afarin TV | AfarinTV.iq | - | NO_GUIDE_HIT |
| Kids | Bantul the Great | custom.bantul.the.great | - | NO_GUIDE_HIT |
| Kids | Doraemon TV | custom.doraemon.tv | - | NO_GUIDE_HIT |
| Kids | Epic Kids Digital | custom.epic.kids.digital | - | NO_GUIDE_HIT |
| Kids | Lego Channel | LegoChannel.us@SD | - | NO_GUIDE_HIT |
| Kids | Moonbug Kids | MoonbugKids.uk | - | NO_GUIDE_HIT |
| Kids | Powerkids Kartoon Channel | custom.powerkids.kartoon.channel | - | NO_GUIDE_HIT |
| Kids | Smurf TV | SmurfTV.us | - | NO_GUIDE_HIT |
| Kids | Tom and Jerry | TomAndJerry.do | - | NO_GUIDE_HIT |
| Kids | Tooku | Tooku.ru | - | NO_GUIDE_HIT |
| Kids | Toon Goggles Junior | custom.toon.goggles.junior | - | NO_GUIDE_HIT |
| Kids | WOW Kidz Hindi | WOWKidz.in@Hindi | - | NO_GUIDE_HIT |
| Kids | WOW Kidz Tamil | custom.wow.kidz.tamil | - | NO_GUIDE_HIT |
| Kids | WOW Kidz Telugu | WOWKidz.in@Telugu | - | NO_GUIDE_HIT |
| Pakistani | 8XM | 8XM.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | aur LIFE | aurLIFE.pk | - | NO_GUIDE_HIT |
| Pakistani | Discover Pakistan | DiscoverPakistan.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | Falak TV | FalakTV.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | HUM Sitaray | custom.humsitaray | - | NO_GUIDE_HIT |
| Pakistani | Jalwa TV | JalwaTV.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | Joo Music | JooMusic.pk | - | NO_GUIDE_HIT |
| Pakistani | Paighan TV | PaighanTV.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | See TV | custom.seetv | - | NO_GUIDE_HIT |
| Pakistani | Tag TV | custom.tag.tv | - | NO_GUIDE_HIT |
| Pakistani | Waseb TV | custom.wasebtv | - | NO_GUIDE_HIT |
| Religious | Makkah TV | MakkahTV.sa | Makkah.TV.ae | MAPPED_ID_ONLY |
| Religious | Al Quran Al Kareem TV | AlQuranAlKareemTV.sa | - | NO_GUIDE_HIT |
| Religious | Al-Zahra TV Turkic | custom.alzahratvturkic | - | NO_GUIDE_HIT |
| Religious | ARY Q TV | custom.ary.q.tv | - | NO_GUIDE_HIT |
| Religious | Bahrain Quran | custom.bahrain.quran | - | NO_GUIDE_HIT |
| Religious | Islamic TV | custom.islamic.tv | - | NO_GUIDE_HIT |
| Religious | Madani TV | custom.madani.tv | - | NO_GUIDE_HIT |
| Religious | MADANI TV BANGLA | custom.bdix.madanibangla | - | NO_GUIDE_HIT |
| Religious | MADINA LIVE | custom.bdix.madinalive | - | NO_GUIDE_HIT |
| Religious | Makkah Live | custom.makkah.live | - | NO_GUIDE_HIT |
| Religious | Medina Live | MedinaLive.bd | - | NO_GUIDE_HIT |
| Religious | Peace TV Bangla | PeaceTVBangla.ae | - | NO_GUIDE_HIT |
| Religious | Peace TV Bangla | custom.peacetvbangla | - | NO_GUIDE_HIT |
| Religious | Peace TV English | custom.peace.tv.english | - | NO_GUIDE_HIT |
| Religious | Peace TV Urdu | custom.peace.tv.urdu | - | NO_GUIDE_HIT |
| Religious | Quran TV | QuranTV.iq | - | NO_GUIDE_HIT |
| Religious | Zainabia Channel | custom.zainabia.channel | - | NO_GUIDE_HIT |
| Sports | FITE 24/7 | FITE247.us@SD | FITE247.us | MAPPED_ENDED |
| Sports | Sky Sports Cricket | SkySportsCricket.ie | SkySportsCricket.ie | MAPPED_NOT_CURRENTLY_FOUND |
| Sports | A Sports | custom.a.sports.hd | - | NO_GUIDE_HIT |
| Sports | Bahrain Sports 2 | BahrainSports2.bh@SD | - | NO_GUIDE_HIT |
| Sports | Goal TV | GoalTV.in | - | NO_GUIDE_HIT |
| Sports | PK Sports | PKSports.pk@SD | - | NO_GUIDE_HIT |
| Sports | PK: GEO SUPER | custom.bdix.geosuper | - | NO_GUIDE_HIT |
| Sports | PTV Sports | PTVSports.pk | - | NO_GUIDE_HIT |
| Sports | T Sports | TSports.bd | - | NO_GUIDE_HIT |
| Sports | T Sports | custom.t.sports.hd | - | NO_GUIDE_HIT |
| Sports | Ten Sports | TenSports.pk | - | NO_GUIDE_HIT |
| Sports | Willow | custom.willow.hd | - | NO_GUIDE_HIT |
| Sports | Willow TV | custom.willow.tv | - | NO_GUIDE_HIT |

## Published Guide Validation

- XMLTV channel IDs published: **462**
- Active playlist IDs present in the published guide: **462/680 (67.9%)**
- Active playlist IDs with usable current/future programmes: **303/680 (44.6%)**
- Active playlist IDs with usable programmes anywhere in the guide window (-6h/+7d): **362/680 (53.2%)**
- Mapped playlist IDs present in the guide: **460/460 (100.0%)**
- Mapped playlist IDs with usable current/future programmes: **301/460 (65.4%)**
- Mapped playlist IDs with usable programmes anywhere in the guide window: **360/460 (78.3%)**
- Eligible programme rows published in the guide window: **22058**
- Mapped playlist IDs missing from the published XMLTV channel list: **0**
- Missing mapped playlist IDs: none
- Published mapped IDs without usable current/future programmes: **159**
- IDs without usable current/future programmes: AmritaTV.in@SD, AndTV.in@SD, AnimalPlanet.in@SD, B4UKadak.in@SD, B4UMovies.in@India, BBCDrama.uk, BBCEarth.ca, BBCNews.uk, BabySharkTV.us, BhojpuriCinema.in@SD, Bollygold.in@HD, CartoonNetwork.uk, CinevaultWesterns.us, Circle.us, Colors.Bangla.in, Colors.in, ColorsCineplex.in@SD, ColorsCineplexSuperhits.in@SD, ColorsRishteyAmericas.in, ColorsTamil.in@SD, DDChandana.in@SD, DDOdia.in@SD, DDSahyadri.in@SD, DDTamil.in@SD, Dangal2.in@SD, DangalTV.in@SD, DarshanaTV.in@SD, DiscoveryChannel.in@SD, DiscoveryKids.au, DocuBayTV.in, ETVBeats.in@HD, ETVComedy.in, ETVJosh.in, EkamraBharatOdia.in@SD, EpicBharat.in@SD, EpicBhojpuri.in@SD, EpicCrimes.in, EpicMusic.in@SD, FITE247.us@SD, FashionOne.uk, GoldminesBollywood.in@SD, GoldminesMovies.in@SD, GravitasMovies.us, HistoryWarfareNow.us, INFAST.nl, INWILD.nl, InWonder.nl, KartoonChannel.us, MakkahTV.sa, ManoranjanPrime.in@SD, Mastiii.in@SD, MazhavilManorama.in@SD, MovieSphere.us, MoviesNow.in@SD, MrBeanAnimated.uk, MyTimeMovieNetwork.br, NHBollyFlix.in, NHBollyRaga.in, NHTamilGold.in, NTVEurope.bd (and 99 more)

## Source / Published Schedule Reconciliation

- IDs with usable current/future source schedule data: **442/680 (65.0%)**
- IDs with usable current/future schedules in published XMLTV at report time: **303/680 (44.6%)**
- IDs with usable programmes in the published guide's common -6h/+7d window: **362/680 (53.2%)**
- Current/future source IDs without any usable published programme in that common window: **83**
- Source-scheduled IDs without a usable published programme in the common window: B4U Movies (`B4UMovies.in@India`), BBC Earth (`BBCEarth.ca`), BBC News (`BBCNews.uk`), Baby Shark TV (`BabySharkTV.us`), Bollygold (`Bollygold.in@HD`), Cinevault Westerns (`CinevaultWesterns.us`), Circle (`Circle.us`), Colors Cineplex (`ColorsCineplex.in@SD`), Colors Rishtey (`ColorsRishteyAmericas.in`), Dangal 2 (`Dangal2.in@SD`), DocuBay TV (`DocuBayTV.in`), ETV Beats (`ETVBeats.in@HD`), ETV Comedy (`ETVComedy.in`), ETV Josh (`ETVJosh.in`), Ekamra Bharat Odia (`EkamraBharatOdia.in@SD`), Epic Bharat (`EpicBharat.in@SD`), Epic Bhojpuri (`EpicBhojpuri.in@SD`), Epic Crimes (`EpicCrimes.in`), Epic Music (`EpicMusic.in@SD`), Goldmines Bollywood (`GoldminesBollywood.in@SD`), Goldmines Movies (`GoldminesMovies.in@SD`), Gravitas Movies (`GravitasMovies.us`), History & Warfare Now (`HistoryWarfareNow.us`), InFast (`INFAST.nl`), InWild (`INWILD.nl`), InWonder (`InWonder.nl`), Kartoon Channel! (`KartoonChannel.us`), MovieSphere (`MovieSphere.us`), Mr Bean Animated (`MrBeanAnimated.uk`), MyTime Movie Network (`MyTimeMovieNetwork.br`), NH BollyFlix (`NHBollyFlix.in`), NH BollyRaga (`NHBollyRaga.in`), NH Tamil Gold (`NHTamilGold.in`), OuterSphere (`OuterSphere.us`), PBS Kids (`PBSKids.us@SD`), PGA Tour (`PGATour.us@SD`), Punjabi Shorts (`PunjabiShorts.in`), Qello Concerts by Stingray (`QelloConcertsbyStingray.ca@SD`), RetroCrush (`RetroCrush.us`), South Station (`SouthStation.in`), STAR GOLD ROMANCE (`Star Gold Romance.in`), IN: -HINDI- STAR SPORTS 1 HD (`Star Sports 1 Hindi HD.in`), Star Gold (`StarGold.in@HD`), Star Gold 2 (`StarGold2.in@HD`), Star Movies Select (`StarMoviesSelect.in@HD`), Stingray DJAZZ (`StingrayDJAZZ.ca@SD`), Stingray Naturescape (`StingrayNaturescape.ca`), Stingray Today's Latin Pop (`StingrayTodaysLatinPop.ca`), Survivor (`Survivor.us`), Teletubbies (`Teletubbies.uk`), Telugu One (`TeluguOne.in@HD`), The Movie Club (`TheMovieClub.in@HD`), The Movie Club +2 (`TheMovieClub.in@Plus2`), Toon Goggles (`ToonGoggles.us`), Trace Urban (`TraceUrban.fr`), Mysteries Xplored (`USBB5200028MM`), Unidentified (`Unidentified.us`), XITE Hits (`XITEHits.nl`), Zoo Moo (`ZooMoo.sg`), beIN SPORTS XTRA (`beINSPORTSXTRA.us`), Ax Men (`custom.ax.men`), TRACE Sport Stars HD (`custom.bdix.tracesportstars`), Bloomberg TV (`custom.bloomberg.tv`), Bon Voyage (`custom.bon.voyage`), Cook & Bake (`custom.cookandbake`), Crime Scene TV (`custom.crime.scene.tv`), Ekamra Manoranjan (`custom.ekamra.manoranjan`), Epic Bhojpuri Digital (`custom.epic.bhojpuri.digital`), House of Crime (`custom.house.of.crime`), KidDo MATIX (`custom.kiddo.matix`), Life+Style (`custom.life.style`), Mayday: Air Disaster (`custom.maydayairdisaster`), Nature Time (`custom.nature.time`), Star Gold (`custom.star.gold`), Star Movies (`custom.star.movies`), Stingray Today's KPOP (`custom.stingraytodayskpop`), Strawberry Shortcake (`custom.strawberry.shortcake`), Travel Channel (`custom.travel.channel`), Vevo Pop (`custom.vevopop`), Wheel World (`custom.wheelworld`), Wild Flix Hindi (`custom.wild.flix.hindi`), Witness to Justice (`custom.witnesstojustice`), XXTreme Jobs Hindi (`custom.xxtreme.jobs.hindi`)
- IDs with an in-window published programme but no current/future source match at the later scan: **3**
- In-window published IDs not counted source-current/future: Channel 24 (`Channel24.bd`), FITE 24/7 (`FITE247.us@SD`), News 24 (`News24.bd`)
- Source-current/future IDs whose published programme is no longer current by report time: **141**
- Source-current/future IDs no longer current in the published guide: Amrita TV (`AmritaTV.in@SD`), &TV (`AndTV.in@SD`), Animal Planet (`AnimalPlanet.in@SD`), B4U Kadak (`B4UKadak.in@SD`), B4U Movies (`B4UMovies.in@India`), BBC Earth (`BBCEarth.ca`), BBC News (`BBCNews.uk`), Baby Shark TV (`BabySharkTV.us`), Bhojpuri Cinema (`BhojpuriCinema.in@SD`), Bollygold (`Bollygold.in@HD`), Cartoon Network UK (`CartoonNetwork.uk`), Cinevault Westerns (`CinevaultWesterns.us`), Circle (`Circle.us`), Colors Bangla (`Colors.Bangla.in`), Colors (`Colors.in`), Colors Cineplex (`ColorsCineplex.in@SD`), Colors Cineplex Superhits (`ColorsCineplexSuperhits.in@SD`), Colors Rishtey (`ColorsRishteyAmericas.in`), Colors Tamil (`ColorsTamil.in@SD`), DD Chandana (`DDChandana.in@SD`), DD Odia (`DDOdia.in@SD`), DD Sahyadri (`DDSahyadri.in@SD`), DD Tamil (`DDTamil.in@SD`), Dangal 2 (`Dangal2.in@SD`), Dangal (`DangalTV.in@SD`), Darshana TV (`DarshanaTV.in@SD`), Discovery (`DiscoveryChannel.in@SD`), Discovery Kids (`DiscoveryKids.au`), DocuBay TV (`DocuBayTV.in`), ETV Beats (`ETVBeats.in@HD`), ETV Comedy (`ETVComedy.in`), ETV Josh (`ETVJosh.in`), Ekamra Bharat Odia (`EkamraBharatOdia.in@SD`), Epic Bharat (`EpicBharat.in@SD`), Epic Bhojpuri (`EpicBhojpuri.in@SD`), Epic Crimes (`EpicCrimes.in`), Epic Music (`EpicMusic.in@SD`), Goldmines Bollywood (`GoldminesBollywood.in@SD`), Goldmines Movies (`GoldminesMovies.in@SD`), Gravitas Movies (`GravitasMovies.us`), History & Warfare Now (`HistoryWarfareNow.us`), InFast (`INFAST.nl`), InWild (`INWILD.nl`), InWonder (`InWonder.nl`), Kartoon Channel! (`KartoonChannel.us`), Mazhavil Manorama (`MazhavilManorama.in@SD`), MovieSphere (`MovieSphere.us`), Movies Now (`MoviesNow.in@SD`), Mr Bean Animated (`MrBeanAnimated.uk`), MyTime Movie Network (`MyTimeMovieNetwork.br`), NH BollyFlix (`NHBollyFlix.in`), NH BollyRaga (`NHBollyRaga.in`), NH Tamil Gold (`NHTamilGold.in`), NTV Europe (`NTVEurope.bd`), Nick Jr (`NickJr.in@SD`), OuterSphere (`OuterSphere.us`), PBS Kids (`PBSKids.us@SD`), PGA Tour (`PGATour.us@SD`), Pogo (`Pogo.in@SD`), Punjabi Shorts (`PunjabiShorts.in`), Qello Concerts by Stingray (`QelloConcertsbyStingray.ca@SD`), Raj Musix Malayalam (`RajMusixMalayalam.in@SD`), Raj Musix Telugu (`RajMusixTelugu.in@SD`), Rang (`Rang.in@SD`), Rengoni (`Rengoni.in@SD`), RetroCrush (`RetroCrush.us`), Roja Movies (`RojaMovies.in@SD`), Ruposhi Bangla (`RupasiBangla.in@SD`), IN: SONY SPORTS TEN 1 HD (`SONY SPORTS TEN 1 HD.in`), Sony PAL (`SonyPal.in@SD`), Sony SAB (`SonySAB.in@HD`), Sony Sports Ten 3 (`SonySportsTen3.in`), Sony Yay (`SonyYay.in@SD`), South Station (`SouthStation.in`), STAR GOLD ROMANCE (`Star Gold Romance.in`), IN: -HINDI- STAR SPORTS 1 HD (`Star Sports 1 Hindi HD.in`), Star Jalsha (`Star.Jalsha.in`), Star Gold (`StarGold.in@HD`), Star Gold 2 (`StarGold2.in@HD`), Star Movies (`StarMovies.in@SD`), Star Movies Select (`StarMoviesSelect.in@HD`), Star Plus (`StarPlus.in@SD`), Star Pravah (`StarPravah.in@HD`), Star Sports 1 (`StarSports1.in@HD`), Star Sports 1 Hindi (`StarSports1Hindi.in@HD`), Star Sports 3 (`StarSports3.in@SD`), Star Sports Select 1 (`StarSportsSelect1.in@SD`), Stingray DJAZZ (`StingrayDJAZZ.ca@SD`), Stingray Naturescape (`StingrayNaturescape.ca`), Stingray Today's Latin Pop (`StingrayTodaysLatinPop.ca`), Survivor (`Survivor.us`), Tarang Music (`TarangMusic.in@SD`), Tarang TV (`TarangTV.in@SD`), Teletubbies (`Teletubbies.uk`), Telugu One (`TeluguOne.in@HD`), The Movie Club (`TheMovieClub.in@HD`), The Movie Club +2 (`TheMovieClub.in@Plus2`), Toon Goggles (`ToonGoggles.us`), Trace Urban (`TraceUrban.fr`), Mysteries Xplored (`USBB5200028MM`), Unidentified (`Unidentified.us`), XITE Hits (`XITEHits.nl`), Zee Bangla (`ZeeBangla.in@HD`), Zee Kannada (`ZeeKannada.in@SD`), Zee Marathi (`ZeeMarathi.in@HD`), Zee TV (`ZeeTV.in@SD`), Zee Tamil (`ZeeTamil.in@SD`), Zoo Moo (`ZooMoo.sg`), beIN SPORTS XTRA (`beINSPORTSXTRA.us`), Ax Men (`custom.ax.men`), AAKASH AATH (`custom.bdix.aakashaath`), TRACE Sport Stars HD (`custom.bdix.tracesportstars`), Bloomberg TV (`custom.bloomberg.tv`), Bon Voyage (`custom.bon.voyage`), Cartoon Network (`custom.cartoon.network.hd`), Cook & Bake (`custom.cookandbake`), Crime Scene TV (`custom.crime.scene.tv`), Discovery (`custom.discovery`), Discovery Turbo (`custom.discovery.turbo`), Ekamra Manoranjan (`custom.ekamra.manoranjan`), Epic Bhojpuri Digital (`custom.epic.bhojpuri.digital`), HISTORY TV (`custom.history.tv`), House of Crime (`custom.house.of.crime`), KidDo MATIX (`custom.kiddo.matix`), Life+Style (`custom.life.style`), Mayday: Air Disaster (`custom.maydayairdisaster`), Nature Time (`custom.nature.time`), Star Gold (`custom.star.gold`), Star Movies (`custom.star.movies`), Star Sports 2 (`custom.star.sports.2`), Star Gold Select (`custom.stargoldselect`), Star Utsav (`custom.starutsav`), Star Utsav Movies (`custom.starutsavmovies`), Stingray Today's KPOP (`custom.stingraytodayskpop`), Strawberry Shortcake (`custom.strawberry.shortcake`), Travel Channel (`custom.travel.channel`), Vevo Pop (`custom.vevopop`), Wheel World (`custom.wheelworld`), Wild Flix Hindi (`custom.wild.flix.hindi`), Witness to Justice (`custom.witnesstojustice`), XXTreme Jobs Hindi (`custom.xxtreme.jobs.hindi`)
- Published current/future IDs not counted source-current/future: **2**
- Published current/future IDs not counted source-current/future: Channel 24 (`Channel24.bd`), News 24 (`News24.bd`)


## Playlist EPG Headers

| Playlist | Header status |
|---|---|
| IPTV-Playlist.m3u | OK |
| BDIX-Playlist.m3u | OK |

## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **addec3a4a8d31ba16ccc35375c378a3faf26983e635c0bf1615d979f1d73b4e7**
- BDIX-Playlist.m3u SHA-256: **9027e1a976113e360f03ee51c0c9cd5952ca25c2a53d88f63310b32f0dcd5b8d**

