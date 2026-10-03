const DEFAULT_PLAYLIST_URL = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u";
const CACHE_KEY = "https://bdix-iptv.internal/playlist";
const CACHE_TTL = 60;

const EPG_PUBLIC_URL = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/epg.xml";
const EPG_URLS = [
  // IN1 is the broad India guide. IN4 is a smaller complementary India guide
  // with additional regional/channel IDs. Keep the live set to these two to
  // avoid the memory pressure caused by the much larger ALL_SOURCES feed.
  "https://epgshare01.online/epgshare01/epg_ripper_IN1.xml.gz",
  "https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz",
  "https://iptv-epg.org/files/epg-in.xml",
  "https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz"
];
const EPG_CACHE_KEY = "https://bdix-iptv.internal/epg-xml-v11";
const EPG_CACHE_TTL = 900;
// Direct M3U EPG endpoint deployment trigger. v10: IN1 + complementary IN4.

// Cross-map playlist tvg-id variants to canonical EPG IDs used by public guides.
const EPG_ID_MAP = {"7SMusic.in@SD":["7S.MUSIC.in","LIVETV_LIVETVCHANNEL_7S_MUSIC"],"7XMusic.in@SD":["7X.Music.in","ts1019","jtv1871","1871"],"9XJalwa.in":["9X.Jalwa.in","9XJalwa.in","407811","LIVETV_LIVETVCHANNEL_9X_JALWA","jtv440","440"],"9XJhakaas.in@SD":["9x.Jhakaas.in","9X.JHAKAAS.in","543161","9XJhakaas.in","jtv441","441"],"9XM.in@SD":["9XM.in","543367","ts139","LIVETV_LIVETVCHANNEL_9XM","jtv587","587"],"9XTashan.in@SD":["9X.Tashan.in","9X.TASHAN.in","9XTashan.in","543036","LIVETV_LIVETVCHANNEL_9X_TASHAN","jtv732","732"],"AakaashAath.in@SD":["AakaashAath.in","ts129"],"AamarBangla.in":["Amar.Bangla.TV.in","jtv1962","1962"],"AaryaaTV.in":["jtv3395","3395"],"AlankarTV.in@SD":["Alankar.TV.in","ALANKAR.in","543118","AlankarTV.in","LIVETV_LIVETVCHANNEL_ALANKAR","jtv686","686"],"AllTimeMovies.in@SD":["ALL.Time.MOVIES.in","ALLTimeMOVIES.in","ts1321","RUNNTV_LIVECHANNEL_128"],"AmritaTV.in@SD":["Amrita.TV.in","AMRITA.in","AmritaTV.in","543102","ts178","jtv723","723"],"AnandTV.in@SD":["Anand.TV.in","jtv3294","3294"],"AndPictures.in@SD":["And.Pictures.in","and.PICTURES.in","AndPictures.in","10000000024300000","ts267","ts148","LIVETV_LIVETVCHANNEL_SYMANDPICTURES","LIVETV_LIVETVCHANNEL_SYMAND_PICTURES_HD"],"AndTV.in@SD":["&TV.HD.in","and.TV.in","andtv.in","AndTV.in","ts578","ts40","LIVETV_LIVETVCHANNEL_SYMANDTV","LIVETV_LIVETVCHANNEL_SYMAND_TV_HD"],"AndpriveHD.in":["And.Prive.HD.in","and.PRIVE.HD.in","AndpriveHD.in"],"AndxplorHD.in":["&Xplor.HD.in","and.xplorHD.in","LIVETV_LIVETVCHANNEL_SYMANDXPLOR_HD","And.Xplor.HD.in","And.XplorHD.in"],"AnimalPlanet.in@SD":["Animal.Planet.HD.in","ANIMAL.PLANET.in","AnimalPlanet.in","543099","10000000024790000","ts130","ts287","LIVETV_LIVETVCHANNEL_ANIMAL_PLANET"],"AsianetMovies.in@SD":["Asianet.Movies.HD.in","ASIANET.MOVIES.in","AsianetMovies.in","543022","543281","ts933","LIVETV_LIVETVCHANNEL_ASIANET_MOVIES","LIVETV_LIVETVCHANNEL_ASIANET_MOVIES_HD"],"B4UKadak.in@SD":["B4U.Kadak.in","B4U.KADAK.in","B4UKadak.in","543225","ts730","LIVETV_LIVETVCHANNEL_B4U_KADAK","jtv1295","1295"],"B4UMovies.in@India":["B4U.Movies.in","B4UMovies.in","543309","ts7","LIVETV_LIVETVCHANNEL_B4U_MOVIES","jtv182","182"],"B4UMusic.in@India":["B4U.Music.in","B4U.MUSIC.in","B4UMusic.in","543038","ts9","LIVETV_LIVETVCHANNEL_B4U_MUSIC","jtv183","183"],"BBCNews.uk":["ts188","LIVETV_LIVETVCHANNEL_BBC_NEWS"],"BHI.Channel.in":["BHI.Channel.in","ts1460","jtv2914","2914"],"BSTV.pk@SD":["BSTV.in","jtv2765","2765"],"BalleBalle.in@SD":["Balle.Balle.TV.in","BALLE.BALLE.in","543327","BalleBalle.in","jtv1453","6437","1453"],"BangBangTV":["6590"],"BhojpuriCinema.in@SD":["Bhojpuri.Cinema.in","BHOJPURI.CINEMA.in","BhojpuriCinema.in","543361","LIVETV_LIVETVCHANNEL_BHOJPURI_CINEMA","jtv486","486"],"CartoonNetwork.uk":["Cartoon.Network.HD+.in","Cartoon.Network.in","CARTOON.NETWORK.in","CartoonNetwork+.in","CartoonNetwork.in","543449","ts238","ts681"],"Channel24.bd":["LIVETV_LIVETVCHANNEL_TV_24","4261"],"Colors.Bangla.in":["Colors.Bangla.in","COLORS.BANGLA.in","COLORSBANGLA.in","543370","543469","ColorsBangla.in","ts26","ts305"],"ColorsBanglaCinema.in@SD":["Colors.Bangla.Cinema.in","COLORS.BANGLA.CINEMA.in","543218","ColorsBanglaCinema.in","ts896","LIVETV_LIVETVCHANNEL_COLORS_BANGLA_CINEMA","jtv1657","1657"],"ColorsCineplex.in@SD":["Colors.Cineplex.in","COLORS.CINEPLEX.in","543298","ColorsCineplex.in","ts61","ts53","LIVETV_LIVETVCHANNEL_COLORS_CINEPLEX","LIVETV_LIVETVCHANNEL_COLORS_CINEPLEX_HD"],"ColorsCineplexSuperhits.in@SD":["Colors.Cineplex.Superhits.in","COLORS.CINEPLEX.SUPERHITS.in","543230","LIVETV_LIVETVCHANNEL_COLORS_CINEPLEX_SUPERHITS","ts1025"],"ColorsGujarati.in@SD":["Colors.Gujarati.in","COLORS.GUJARATI.in","543314","ColorsGujarati.in","ts107","LIVETV_LIVETVCHANNEL_COLORS_GUJARATI","jtv196","196"],"ColorsGujaratiCinema.in@SD":["Colors.Gujarati.Cinema.in","COLORS.GUJARATI.CINEMA.in","543362","ColorsGujaratiCinema.in","ts692","LIVETV_LIVETVCHANNEL_COLORS_GUJARATI_CINEMA","jtv1324","1324"],"ColorsKannada.in@SD":["Colors.Kannada.SD.in","Colors.Kannada.HD.in","COLORS.KANNADA.in","COLORSKANNADA.in","543329","543147","ts108","ts612"],"ColorsKannadaCinema.in@SD":["Colors.Kannada.Cinema.in","ts667","LIVETV_LIVETVCHANNEL_COLORS_KANNADA_CINEMA","jtv1632","1632"],"ColorsMarathi.in@SD":["Colors.Marathi.HD.in","Colors.Marathi.SD.in","COLORS.MARATHI.in","COLORSMARATHI.in","543065","543277","ColorsMarathi.in","ts134"],"ColorsRishteyAmericas.in":["Colors.Rishtey.in","COLORS.RISHTEY.in","ColorsRishtey.in","543236","ts438","LIVETV_LIVETVCHANNEL_COLORS_RISHTEY","jtv279","279"],"ColorsSuper.in":["Colors.Super.in","COLORS.SUPER.in","543284","ts533","LIVETV_LIVETVCHANNEL_COLORS_SUPER","jtv785","785"],"ColorsTamil.in@SD":["Colors.Tamil.in","COLORSTAMIL.in","543334","543302","ts674","ts418","LIVETV_LIVETVCHANNEL_COLORS_TAMIL_HD","LIVETV_LIVETVCHANNEL_COLORS_TAMIL"],"CricketGold.au@SD":["6995"],"DDArunPrabha.in@SD":["DD.Arunprabha.in","DD.ARUN.PRABHA.in","543094","DDArunPrabha.in","ts758","LIVETV_LIVETVCHANNEL_DD_ARUNPRABHA","jtv1328","1328"],"DDAssam.in@SD":["DDAssam.in","LIVETV_LIVETVCHANNEL_DD_NORTH_EAST"],"DDBangla.in@SD":["DD.Bangla.in","543434","DDBangla.in","ts314","LIVETV_LIVETVCHANNEL_DD_BANGLA","jtv690","690"],"DDBharati.in@SD":["DD.bharati.in","DDBharati.in","ts316","LIVETV_LIVETVCHANNEL_DD_BHARATI","jtv580","580"],"DDChandana.in@SD":["DD.Chandana.in","DDChandana.in","543175","ts321","LIVETV_LIVETVCHANNEL_DD_CHANDANA"],"DDGirnar.in@SD":["DD.Girnar.in","DD.GIRNAR.in","DDGirnar.in","543062","ts323","LIVETV_LIVETVCHANNEL_DD_GIRNAR","jtv714","714"],"DDGoa.in@SD":["ts1215"],"DDHaryana.in@SD":["ts1212"],"DDHimachalPradesh.in@SD":["ts1217","LIVETV_LIVETVCHANNEL_DD_SHIMLA"],"DDJharkhand.in@SD":["ts1188"],"DDKashir.in@SD":["DD.Kashir.in","543500","DDKashir.in","ts325","LIVETV_LIVETVCHANNEL_DD_KASHIR","jtv716","716"],"DDMadhyaPradesh.in@SD":["DD.Madhya.Pradesh.in","DDMadhyaPradesh.in","ts330","LIVETV_LIVETVCHANNEL_DD_MP","jtv536","536"],"DDMalayalam.in@SD":["DD.Malayalam.in","DD.MALAYALAM.in","DDMalayalam.in","543259","ts328","LIVETV_LIVETVCHANNEL_DD_MALAYALAM","jtv699","699"],"DDManipur.in@SD":["ts329","LIVETV_LIVETVCHANNEL_DD_IMPHAL"],"DDMeghalaya.in@SD":["ts991","LIVETV_LIVETVCHANNEL_DD_SHILLONG"],"DDNagaland.in@SD":["ts1214"],"DDNational.in@SD":["DD.National.in","DDNational.in","543184","ts191","ts1218","LIVETV_LIVETVCHANNEL_DD_NATIONAL","LIVETV_LIVETVCHANNEL_DD_NATIONAL_HD","jtv202"],"DDOdia.in@SD":["DD.ODIA.in","DDOdia.in","543028","ts333","LIVETV_LIVETVCHANNEL_DD_ORIYA"],"DDPunjabi.in@SD":["DD.Punjabi.in","DD.PUNJABI.in","DDPunjabi.in","543437","ts335","LIVETV_LIVETVCHANNEL_DD_PUNJABI","jtv715","715"],"DDSahyadri.in@SD":["DD.SAHYADRI.in","DDSahyadri.in","543462","ts336","LIVETV_LIVETVCHANNEL_DD_SAHYADRI"],"DDSaptagiri.in@SD":["DD.Saptagiri.in","DDSaptagiri.in","543376","ts337","LIVETV_LIVETVCHANNEL_DD_SAPTAGIRI","jtv706","706"],"DDSports.in@SD":["DD.Sports.in","DDSports.in","543389","10000000074760000","ts1191","ts223","LIVETV_LIVETVCHANNEL_DD_SPORTS","LIVETV_LIVETVCHANNEL_DD_SPORTS_HD"],"DDTamil.in@SD":["DD.TAMIL.in","DDTamil.in","543273","ts334","LIVETV_LIVETVCHANNEL_DD_TAMIL","jtv726","726"],"DDTripura.in@SD":["ts1210","LIVETV_LIVETVCHANNEL_DD_TRIPURA"],"DDUrdu.in@SD":["DD.urdu.in","DD.URDU.in","543021","DDUrdu.in","ts338","LIVETV_LIVETVCHANNEL_DD_URDU","jtv712","712"],"Dangal2.in@SD":["Dangal.2.in","Dangal2.in","543069","LIVETV_LIVETVCHANNEL_DANGAL_2","ts194"],"DangalTV.in@SD":["Dangal.in","DANGAL.in","543037","LIVETV_LIVETVCHANNEL_DANGAL","jtv701","ts51","701"],"DarshanaTV.in@SD":["DARSHANA.in","543481"],"DesiChannel.in":["Desi.Channel.in","jtv906","906"],"DhoolTV.in@SD":["jtv3610"],"DhoomMusic.in@SD":["Dhoom.Music.Bangla.in","DHOOM.MUSIC.in","DhoomMusic.in","jtv3006","3006"],"DiscoveryChannel.in@SD":["Discovery.in","DISCOVERY.CHANNEL.in","543256","DiscoveryChannel.in","ts219","LIVETV_LIVETVCHANNEL_DISCOVERY_CHANNEL"],"DiscoveryKids.au":["Discovery.Kids.in","DISCOVERY.KIDS.in","DiscoveryKids.in","543485","ts119","LIVETV_LIVETVCHANNEL_DISCOVERY_KIDS"],"DisneyChannel.in@HD":["DISNEY.CHANNEL.in","DisneyChannel.in"],"DocuBayTV.in":["jtv3402","3402"],"E24.in":["E.24.in","LIVETV_LIVETVCHANNEL_E24","591"],"ETVBalBharat.in@SD":["ETV.BAL.BHARAT.in","543412","10000000075992191","LIVETV_LIVETVCHANNEL_ETV_BAL_BHARAT","ts905"],"ETVBeats.in@HD":["3559"],"ETVCinema.in":["ETV.Cinema.in","ETV.CINEMA.in","ETVCinema.in","543267","LIVETV_LIVETVCHANNEL_ETV_CINEMA","jtv1665","jtv252","1665"],"ETVComedy.in":["jtv3561","3561"],"ETVJosh.in":["jtv3560","3560"],"ETVMusic.in":["ts358","LIVETV_LIVETVCHANNEL_ETV_ABHIRUCHI","jtv3559","565"],"EkamraBharatOdia.in@SD":["Ekamra.Bharat.Odia.in","ts1196"],"Enterr10Bangla.in@SD":["ENTER10.BANGLA.in","Enterr10Bangla.in","543030","LIVETV_LIVETVCHANNEL_ENTERR10_BANGLA"],"EpicBharat.in@SD":["ts1184","SWIFTTV_LIVECHANNEL_86","jtv3383","3383"],"EpicBhojpuri.in@SD":["ts830","LIVETV_LIVETVCHANNEL_FILAMCHI_BHOJPURI","jtv3384","3384"],"EpicMusic.in@SD":["ts733","LIVETV_LIVETVCHANNEL_SHOWBOX"],"FaktMarathi.in@SD":["Fakt.Marathi.in","FAKT.MARATHI.in","FaktMarathi.in","543453","LIVETV_LIVETVCHANNEL_FAKT_MARATHI","jtv738","738"],"FoodFood.in@SD":["Food.Food.in","FoodFood.in","ts117","jtv561","561"],"GREATmovies.uk":["0-9-9z5910243"],"Gangaur.in@SD":["Gangaur.in","ts1859","jtv2077","2077"],"Goldmines.in@SD":["Goldmines.in","ts823","LIVETV_LIVETVCHANNEL_GOLDMINES"],"GoldminesBollywood.in@SD":["Goldmines.Bollywood.in","LIVETV_LIVETVCHANNEL_GOLDMINES_BOLLYWOOD"],"GoldminesMovies.in@SD":["Goldmines.Movies.in","ts1499"],"HMTV.in@SD":["HM.TV.in","HMTV.in","60"],"History.us":["HISTORY.CHANNEL.in","543138"],"HistoryTV18.in@SD":["History.TV18.SD.in","History.TV18.HD.in","HISTORY.TV18.HD.in","543336","HistoryTV18.in","LIVETV_LIVETVCHANNEL_HISTORY_TV18","LIVETV_LIVETVCHANNEL_HISTORY_TV18_HD","jtv1471"],"Hungama.in@SD":["Hungama.in","HUNGAMA.in","543181","HungamaTV.in","LIVETV_LIVETVCHANNEL_HUNGAMA","jtv1391","1391","ts345"],"INWILD.nl":["jtv3389","3389"],"InTravel.in@HD":["jtv3392","3392"],"Insync.in":["Insync.in","jtv1286","6633","1286"],"InvestigationDiscovery.in@SD":["Investigation.Discovery.in","InvestigationDiscovery.in","543196","ts633","ts1276","LIVETV_LIVETVCHANNEL_INVESTIGATION_DISCOVERY_HD","LIVETV_LIVETVCHANNEL_INVESTIGATION_DISCOVERY"],"IsaiAruvi.in@SD":["ISAI.ARUVI.in","Isaiaruvi.in","543163","ts647","LIVETV_LIVETVCHANNEL_ISAI_ARUVI"],"KairaliTV.in@SD":["Kairali.TV.in","KAIRALI.in","543357","ts25","LIVETV_LIVETVCHANNEL_KAIRALI_TV","jtv710","710"],"KairaliWe.in@SD":["Kairali.WE.TV.in","LIVETV_LIVETVCHANNEL_KAIRALI_WE","jtv731","731"],"KalaignarMurasu.in":["MURASU.in"],"KalaignarTV.in@SD":["Kalaignar.TV.in","KALAIGNAR.in","KalaignarTV.in","543395","ts200","LIVETV_LIVETVCHANNEL_KALAIGNAR_TV","jtv1209","1209"],"KappaTV.in@SD":["Kappa.TV.in"],"KhushbooBangla.in@SD":["KhushbooBangla.in","ts379","LIVETV_LIVETVCHANNEL_KHUSHBOO_BANGLA"],"LoLTV.in":["6609"],"MHOneDilSe.in@SD":["MH One Dil Se.in","MH-One-Dil-Se.in"],"MKSix.in":["MK.Six.in","jtv1647","1647"],"MNX.in@SD":["MNX.in","543194","ts234","ts599","LIVETV_LIVETVCHANNEL_MNX","LIVETV_LIVETVCHANNEL_MNX_HD","jtv877","jtv462"],"MONTVBangla.in":["Mon.TV.Bangla.in","jtv3298","3298"],"MTVIndia.in@SD":["jtv248","248"],"MadhimugamTV.in":["Madhimugam.TV.in","jtv843","843"],"MahaaMax.in":["Mahaa.Max.in","LIVETV_LIVETVCHANNEL_MAHAA_MAX","jtv3143","7052","3143"],"ManoranjanGrand.in@SD":["Manoranjan.Grand.in","ManoranjanGrand.in"],"ManoranjanMovies.in@SD":["ManoranjanMovies.in"],"ManoranjanPrime.in@SD":["10000000075992492"],"Mastiii.in@SD":["Mastiii.in"],"MazhavilManorama.in@SD":["Mazhavil.Manorama.in","MAZHAVIL.MANORAMA.in","MAZHAVILMANORAMA.in","543130","543345","ts395","ts31","LIVETV_LIVETVCHANNEL_MAZHAVIL_MANORAMA"],"Mh1Music.in@SD":["mh1.(Music).in","Mh1Music.in","jtv742","742"],"MoviesNow.in@SD":["Movies.Now.in","MOVIES.NOW.in","MoviesNow.in","543174","ts562","ts173","LIVETV_LIVETVCHANNEL_MOVIES_NOW_HD","LIVETV_LIVETVCHANNEL_MOVIES_NOW"],"MoviesNowPlus.in@SD":["MN+.HD.in","543209","MoviesNowPlus.in","ts210","LIVETV_LIVETVCHANNEL_MNSYMPLUS","jtv477","477"],"MusicIndia.in@SD":["Music.India.in","MusicIndia.in","jtv250","250"],"NHBollyFlix.in":["RUNNTV_LIVECHANNEL_40","jtv3336","3336"],"NHBollyGold.in":["RUNNTV_LIVECHANNEL_39","jtv3338","3338"],"NHBollyRaga.in":["RUNNTV_LIVECHANNEL_41","jtv3343","3343"],"NKTVBangla.bd":["NK.TV.Bangla.in","jtv2933","2933"],"NTV.bd":["NTV.in","543153","ts1386","LIVETV_LIVETVCHANNEL_NTV","jtv646","58","646"],"NationalGeographic.in@SD":["National.Geographic.HD.in","NATIONAL.GEOGRAPHIC.in","543180","543108","NationalGeographic.in","LIVETV_LIVETVCHANNEL_NATIONAL_GEOGRAPHIC_CHANNEL","LIVETV_LIVETVCHANNEL_NATIONAL_GEOGRAPHIC_CHANNEL_HD","jtv1335"],"NationalGeographicWild.in@SD":["Nat.Geo.Wild.HD.in","NAT.GEO.WILD.in","NAT.GEO.WILD.HD.in","NatGeoWild.in","543356","543052","NationalGeographicWild.in","LIVETV_LIVETVCHANNEL_NAT_GEO_WILD_HD"],"Nazara.in@SD":["NAZARA.in"],"News24.bd":["News.24.in","NEWS.24.in","News24.in","543354","ts209","LIVETV_LIVETVCHANNEL_NEWS24","jtv501","501"],"NickJr.in@SD":["Nick.Jr.in","NICK.JR.in","543502","ts118"],"Nickelodeon.in@SD":["Nick.HD+.in","Nick.in","NICK.in","NICK.HD+.in","543260","543090","Nickelodeon.in","ts433"],"OnePaschima.in@SD":["One.Paschima.in"],"Only.Music.in":["Only.Music.in","jtv903","903"],"OscarMoviesBhojpuri.in@SD":["Oscar.Movies.Bhojpuri.in","OscarMoviesBhojpuri.in","ts431"],"PTCChakde.in@SD":["PTC.Chak.De.in","PTC.CHAK.DE.in","PTCChakDe.in","543198","PTCChakde.in","ts92","LIVETV_LIVETVCHANNEL_PTC_CHAKDE","jtv1172"],"PTCMusic.in@SD":["PTC.Music.in","PTCMusic.in","543071","ts922","LIVETV_LIVETVCHANNEL_PTC_MUSIC","jtv1189","1189"],"PTCPunjabi.in@SD":["PTC.Punjabi.in","PTC.PUNJABI.in","PTCPunjabi.in","543360","ts122","LIVETV_LIVETVCHANNEL_PTC_PUNJABI","jtv1171","1171"],"PTCPunjabiGold.in@SD":["PTC.Punjabi.Gold..in","PTC.Punjabi.Gold.in","PTC.PUNJABI.GOLD.in","PTCPunjabiGold.in","543031","ts794","LIVETV_LIVETVCHANNEL_PTC_PUNJABI_GOLD","jtv1190"],"PeppersTV.in@SD":["Peppers.TV.in","PeppersTV.in","ts421","jtv796","6644","796"],"Pitaara.in@SD":["Pitaara.in","543026","LIVETV_LIVETVCHANNEL_PITAARA","jtv946","6576","946"],"PocketFilms.in":["Pocket.Films.in","RUNNTV_LIVECHANNEL_4","jtv3259","7097","3259"],"Pogo.in@SD":["Pogo.in","POGO.in","543393","ts239","LIVETV_LIVETVCHANNEL_POGO"],"PolimerTV.in@SD":["Polimer.TV.in","POLIMER.in","PolimerTV.in","543431","ts272","LIVETV_LIVETVCHANNEL_POLIMER_TV","jtv705","705"],"Pop.uk":["0-9-9z5910525"],"PublicMovies.in@SD":["Public.Movies.in","PUBLIC.MOVIES.in","PublicMovies.in","543203","ts661","LIVETV_LIVETVCHANNEL_PUBLIC_MOVIES","jtv1633","1633"],"PublicMusic.in@SD":["Public.Music.in","PUBLIC.MUSIC.in","PublicMusic.in","543355","ts424","LIVETV_LIVETVCHANNEL_PUBLIC_MUSIC","jtv773","773"],"PunjabiHits.in":["Punjabi.Hits.in","PunjabiHits.in","jtv2934","7004","2934"],"PunjabiShorts.in":["SWIFTTV_LIVECHANNEL_308","jtv3471","7128","3471"],"PuthuyugamTV.in@SD":["Puthu.Yugam.in","PUTHU.YUGAM.in","543133","LIVETV_LIVETVCHANNEL_PUTHU_YUGAM","jtv824","824"],"QelloConcertsbyStingray.ca@SD":["jtv3289","3289"],"RPlusGold.in@SD":["jtv3538","7171","3538"],"RajDigitalPlus.in@SD":["Raj.Digital.Plus.in","RAJ.DIGITAL.PLUS.in","RajDigitalPlus.in","543042","ts426","LIVETV_LIVETVCHANNEL_RAJ_DIGITAL_PLUS","jtv683","683"],"RajMusicTelugu.in@SD":["Raj.Music.Telugu.in","jtv737","737"],"RajMusixKannada.in@SD":["RAJ.MUSIX.KANNADA.in","RajMusixKannada.in","543078","ts427","LIVETV_LIVETVCHANNEL_RAJ_MUSIX_KANNADA"],"RajMusixMalayalam.in@SD":["RAJ.MUSIX.MALAYALAM.in","543404","ts541","LIVETV_LIVETVCHANNEL_RAJ_MUSIX_MALAYALAM"],"RajMusixTamil.in@SD":["RAJ.MUSIX.TAMIL.in","RAJMUSIXTAMIL.in","543499","LIVETV_LIVETVCHANNEL_RAJ_MUSIX_TAMIL"],"RajMusixTelugu.in@SD":["RAJ.MUSIX.TELUGU.in","RajMusixTelugu.in","543024","ts429","LIVETV_LIVETVCHANNEL_RAJ_MUSIX_TELUGU"],"RajTV.in@SD":["Raj.tv.in","Raj.TV.in","RAJ.TV.in","RajTV.in","543033","ts439","LIVETV_LIVETVCHANNEL_RAJ_TV","jtv707"],"Ramdhenu.in@SD":["Ramdhenu.in","RAMDHENU.in","543092","ts449","LIVETV_LIVETVCHANNEL_RAMDHENU","jtv639","639"],"RedBullTV.at@EUMENA":["Red.Bull.TV.in","jtv2779","2779"],"RojaMovies.in@SD":["ts1868","jtv3417","3417"],"RomedyNow.in@SD":["Romedy.Now.in","ROMEDY.NOW.in","RomedyNow.in","543123","ts174","LIVETV_LIVETVCHANNEL_ROMEDY_NOW","jtv478","jtv1401"],"RongeenTV.in@SD":["Rongeen.TV.in","RongeenTV.in","ts1132","jtv1667","1667"],"RupasiBangla.in@SD":["Ruposhi.Bangla.in","RUPASI.BANGLA.in","RuposhiBangla.in","RupasiBangla.in","ts3","LIVETV_LIVETVCHANNEL_RUPOSHI_BANGLA_TV"],"SafariTV.in@SD":["Safari.TV..in","SAFARI.TV.in","SafariTV.in","543117","ts436","LIVETV_LIVETVCHANNEL_SAFARI_TV","jtv1666","1666"],"SanaPlus.in@SD":["ts1284","jtv3359","3359"],"SanaTV.in@SD":["ts1285","jtv3201","7130","3201"],"SangeetBangla.in@SD":["Sangeet.Bangla.in","SANGEET.BANGLA.in","SangeetBangla.in","543268","ts215","LIVETV_LIVETVCHANNEL_SANGEET_BANGLA","jtv740","740"],"SangeetBhojpuri.in@SD":["Sangeet.Bhojpuri.in","SangeetBhojpuri.in","jtv741","741"],"SangeetMarathi.in@SD":["Sangeet.Marathi.in","SangeetMarathi.in","ts217","LIVETV_LIVETVCHANNEL_SANGEET_MARATHI","jtv735","735"],"ShemarooBollywood.us":["Shemaroo.Bollywood.in","jtv3075","3075"],"ShemarooJosh.in@SD":["ts1269","LIVETV_LIVETVCHANNEL_CHUMBAK_TV"],"ShemarooTV.in@SD":["Shemaroo.TV.in","ShemarooTV.in","543214","ts818","LIVETV_LIVETVCHANNEL_SHEMAROO_TV","jtv1961","1961"],"SidharthGold.in@SD":["Sidharth.GOLD.in","Sidharth.Gold.in","SidharthGOLD.in","10000000075992325","ts1170","LIVETV_LIVETVCHANNEL_SIDHARTH_GOLD","jtv1957","1957"],"SiriKannada.in@SD":["Siri.Kannada.in","jtv1634","1634"],"SiriKannadaAllTime.in":["SIRI.KANNADA-ALL.TIME.in","SIRIKANNADAAlltime.in","543254","ts940"],"SongdewTV.in@SD":["SongDew.TV.in","SONGDEW.in","543261","SongdewTV.in","jtv1411","598"],"Sonic.in@SD":["ts127","LIVETV_LIVETVCHANNEL_SONIC","Sonic.in"],"Sony.Aath.in":["Sony.Aath.in","SONY.AATH.in","SONYAATH.in","543401","SonyAath.in","ts34","LIVETV_LIVETVCHANNEL_SONY_8","jtv697"],"SonyBBCEarth.in@SD":["SONY.BBC.Earth.in","SONY.BBC.EARTH.in","543410","543416","SonyBBCEarth.in","ts158","ts460","LIVETV_LIVETVCHANNEL_SONY_BBC_EARTH_HD"],"SonyEntertainmentTelevision.in@SD":["Sony.Entertainment.Television.in","SonyEntertainmentTelevision.in"],"SonyMax.in@SD":["Sony.Max.in","SONY.MAX.in","543269","10000000033520000","ts132","ts80","LIVETV_LIVETVCHANNEL_SONY_MAX_HD","LIVETV_LIVETVCHANNEL_SONY_MAX"],"SonyMax2.in@SD":["Sony.MAX2.in","Sony.Max.2.in","SONY.MAX.2.in","543114","SonyMax2.in","ts120","LIVETV_LIVETVCHANNEL_SONY_MAX_2","jtv483"],"SonyPix.in":["SONY.PIX.in","543113","543337","SonyPix.in","ts558","ts32","LIVETV_LIVETVCHANNEL_SONY_PIX","LIVETV_LIVETVCHANNEL_SONY_PIX_HD"],"SonySAB.in@HD":["Sony.SAB.in","SONY.SAB.in","SONYSAB.in","543101","SonySAB.in","ts48","ts559","LIVETV_LIVETVCHANNEL_SONY_SAB_HD"],"SonySportsTen3.in":["Sony.Sports.Ten.3.HD.in","SONY.SPORTS.TEN.3.in","SonySportsTEN3.in","543206","543295","SonySportsTen3.in"],"SonySportsTen4.in":["Sony.Sports.Ten.4.HD.in","SonySportsTEN4.in"],"SonySportsTen5.in":["Sony.Sports.Ten.5.in","SONY.SPORTS.TEN.5.in","SONYSPORTSTEN5.in","543505","543047","SonySportsTen5.in","ts35","LIVETV_LIVETVCHANNEL_SONY_SPORTS_TEN_5"],"SonyYay.in@SD":["SONY.YAY!.in","Sony.yay.in","543317","SonyYay.in","ts45","LIVETV_LIVETVCHANNEL_SONY_YAY","Sony.YAY!.in","3507"],"Star.Jalsha.Movies.in":["Star.Jalsha.Movies.in","JALSHA.MOVIES.HD.in","JALSHA.MOVIES.in","543072","543369","JalshaMovies.in","ts537","LIVETV_LIVETVCHANNEL_JALSHA_MOVIES_HD"],"Star.Jalsha.in":["Star.Jalsha.in","STAR.JALSHA.in","STARJALSHA.in","543407","542998","StarJalsha.in","ts468","LIVETV_LIVETVCHANNEL_STAR_JALSHA"],"StarBharat.in":["Star.Bharat.in","STAR.BHARAT.in","STARBHARAT.in","543115","543501","StarBharat.in","ts244","LIVETV_LIVETVCHANNEL_STAR_BHARAT"],"StarGold.in@HD":["Star.Gold.in","STAR.GOLD.in","543292","543055","StarGold.in","ts632","LIVETV_LIVETVCHANNEL_STAR_GOLD_HD","LIVETV_LIVETVCHANNEL_STAR_GOLD"],"StarGoldSelect.in@SD":["Star.Gold.Select.in","STAR.GOLD.SELECT.in","StarGoldSelect.in","543216","543074","LIVETV_LIVETVCHANNEL_STAR_GOLD_SELECT_HD","LIVETV_LIVETVCHANNEL_STAR_GOLD_SELECT","jtv1119"],"StarGoldThrills.in@SD":["Star.Gold.Thrills.in","STAR.GOLD.THRILLS.in","543460","10000000075992763","LIVETV_LIVETVCHANNEL_STAR_GOLD_THRILLS","jtv3098","ts494","3098"],"StarMaa.in@SD":["STAR.MAA.in","STARMAA.in","543246","543459","StarMaa.in","ts956","jtv1138","Star.Maa.HD.in"],"StarMaaMovies.in@SD":["Star.Maa.Movies.in","STAR.MAA.MOVIES.in","543492","543235","ts957","LIVETV_LIVETVCHANNEL_STAR_MAA_MOVIES_HD"],"StarMovies.in@SD":["Star.Movies.in","STAR.MOVIES.in","543176","543187","StarMovies.in","LIVETV_LIVETVCHANNEL_STAR_MOVIES_HD","LIVETV_LIVETVCHANNEL_STAR_MOVIES","jtv1115"],"StarMoviesSelect.in@HD":["Star.Movies.Select.HD.in","STAR.MOVIES.SELECT.in","543313","543316","StarMoviesSelect.in","LIVETV_LIVETVCHANNEL_STAR_MOVIES_SELECT_HD","LIVETV_LIVETVCHANNEL_STAR_MOVIES_SELECT","jtv3276"],"StarPlus.in@SD":["Star.Plus.in","STAR.PLUS.in","STARPLUS.in","543093","543164","StarPlus.in","ts8","LIVETV_LIVETVCHANNEL_STAR_PLUS"],"StarPravah.in@SD":["Star.Pravah.in","STAR.PRAVAH.in","543054","StarPravah.in","ts469","LIVETV_LIVETVCHANNEL_STAR_PRAVAH","LIVETV_LIVETVCHANNEL_STAR_PRAVAH_HD","jtv336"],"StarSports1.in@HD":["Star.Sports.1.in","STAR.SPORTS.1.in","StarSports1.in","543006","543489","ts78","LIVETV_LIVETVCHANNEL_STAR_SPORTS_1","LIVETV_LIVETVCHANNEL_STAR_SPORTS_1_HD"],"StarSports1Hindi.in@HD":["STAR.SPORTS.1.HINDI.in","StarSports1Hindi.in","543275","543058","ts24","jtv1108","jtv362"],"StarSports3.in@SD":["STAR.SPORTS.3.in","StarSports3.in","543366","LIVETV_LIVETVCHANNEL_STAR_SPORTS_3","jtv1389","ts664"],"StarSportsSelect1.in@SD":["Star.Sports.Select.1.in","StarSportsSelect1.in","543120","543263","ts246","LIVETV_LIVETVCHANNEL_STAR_SPORTS_SELECT_1","LIVETV_LIVETVCHANNEL_STAR_SPORTS_SELECT_1_HD","jtv1123"],"StarSportsSelect2.in@SD":["Star.Sports.Select.2.in","STAR.SPORTS.SELECT.2.in","StarSportsSelect2.in","543061","543450","LIVETV_LIVETVCHANNEL_STAR_SPORTS_SELECT_2_HD","LIVETV_LIVETVCHANNEL_STAR_SPORTS_SELECT_2","jtv461"],"StarSuvarnaPlus.in@SD":["STAR.SUVARNA.PLUS.in","543423","ts540","LIVETV_LIVETVCHANNEL_STAR_SUVARNA_PLUS","Star.Suvarna.Plus.in"],"StarUtsavMovies.in@SD":["Star.Utsav.Movies.in","STAR.UTSAV.MOVIES.in","543124","StarUtsavMovies.in","LIVETV_LIVETVCHANNEL_STAR_UTSAV_MOVIES","jtv1136","1136","ts470"],"SteelbirdMusic.in@SD":["Steelbird.Music.in"],"StingrayDJAZZ.ca@SD":["jtv3290","3290"],"StingrayNaturescape.ca":["jtv3285","3285"],"StingrayTheSpa.ca":["jtv3323","3323"],"StudioOnePlus.in@SD":["Studio.One.in","jtv1274","1274"],"StudioYuva.in":["jtv1799","7107","1799"],"SubinTV.in@SD":["ts1385","jtv3360","3360"],"SunBangla.in@SD":["Sun.Bangla.in","SUN.BANGLA.in","SUNBANGLA.in","543322","SunBangla.in","LIVETV_LIVETVCHANNEL_SUN_BANGLA","jtv1669","1669"],"SunMusic.in@SD":["Sun.Music.HD.in","SUN.MUSIC.in","543232","543454","LIVETV_LIVETVCHANNEL_SUN_MUSIC","LIVETV_LIVETVCHANNEL_SUN_MUSIC_HD","jtv895","895"],"SuperHungama.in@SD":["Super.Hungama.in","SUPER.HUNGAMA.in","543103","LIVETV_LIVETVCHANNEL_SUPER_HUNGAMA","jtv1392","1392","ts587"],"SuriyaTV.in":["jtv3394","3394"],"TLC.in@HD":["TLC.HD.in","TLC.in","543386","543128","ts135","ts480","LIVETV_LIVETVCHANNEL_TLC","LIVETV_LIVETVCHANNEL_TLC_HD"],"TabbarHits.in":["Tabbar.Hits.in","10000000065580000","jtv2778","7005","2778"],"TarangMusic.in@SD":["TARANG.MUSIC.in","543280","TarangMusic.in","LIVETV_LIVETVCHANNEL_TARANG_MUSIC","jtv751","751"],"ThalaaTV.in":["6601"],"ThanthiOne.in":["Thanthi.One.in","THANTHI.ONE.in","jtv3059","3059"],"TheJungleBook.in":["SWIFTTV_LIVECHANNEL_79"],"TinyPop.uk":["0-9-9z5910526"],"TollyTV.in":["6613"],"Travelxp.in@SD":["Travelxp.HD.Hindi.in","Travelxp.in","jtv562","562"],"UBangla.in":["U.Bangla.in","jtv2184","ts1080","2184"],"UltimateTV.in@SD":["jtv3396","3396"],"VaanavilTV.in@SD":["Vaanavil.TV.in","jtv971","971"],"VanithaTV.in@SD":["Vanitha.in","ts1135","jtv775","227","775"],"VasanthTV.in@SD":["Vasanth.TV.in","VASANTH.TV.in","VasanthTV.in","543287","ts499","LIVETV_LIVETVCHANNEL_VASANTH_TV","jtv727","727"],"VendharTV.in@SD":["Vendhar.TV.in","VendharTV.in","ts659","jtv857","857"],"VijaySuper.in@SD":["VIJAY.SUPER.in","543204","543438","LIVETV_LIVETVCHANNEL_VIJAY_SUPER_HD","LIVETV_LIVETVCHANNEL_VIJAYSUPER","jtv1131","jtv3266","ts1176"],"VissaTV.in@SD":["Vissa.TV.in","VISSA.TV.in","VissaTV.in","543439","ts585","LIVETV_LIVETVCHANNEL_VISSA_TV","jtv734","734"],"WildEarth.za":["Wild.Earth.in","jtv2437","2437"],"ZBCartoon.in":["jtv3321","3321"],"Zee24Ghanta.in@SD":["Zee.24.Ghanta.in","Zee24Ghanta.in","554174","ts258","SWIFTTV_LIVECHANNEL_168","LIVETV_LIVETVCHANNEL_ZEE_24_GHANTA","jtv464","0-9-24ghantatv"],"ZeeAction.in":["ZEE.ACTION.in","543243","ZeeAction.in","jtv488","0-9-zeeaction","488"],"ZeeBangla.in@HD":["Zee.Bangla.in","ZEE.BANGLA.in","ZEEBANGLA.in","543504","404001","ZeeBangla.in","ts522","ts253"],"ZeeBanglaSonar.in@SD":["ts254","LIVETV_LIVETVCHANNEL_ZEE_BANGLA_CINEMA","jtv3476","0-9-zeebanglacinema","3476"],"ZeeBollywood.in@SD":["Zee.Bollywood.in","ZEE.Bollywood.in","ZeeBollywood.in","543294","ts175","LIVETV_LIVETVCHANNEL_ZEE_BOLLYWOOD","jtv487","0-9-zeeclassic"],"ZeeCinema.in@HD":["Zee.Cinema.in","ZEE.CINEMA.in","ZeeCinema.in","543084","543330","ts503","ts123","LIVETV_LIVETVCHANNEL_ZEE_CINEMA_HD"],"ZeeCinemalu.in@HD":["Zee.Cinemalu.HD.in","ZEE.CINEMALU.in","ZeeCinemalu.in","543172","543358","ts636","ts252","LIVETV_LIVETVCHANNEL_ZEE_CINEMALU"],"ZeeKannada.in@SD":["Zee.Kannada.in","ZEE.KANNADA.in","ZeeKannada.in","543097","543064","ts675","ts256","LIVETV_LIVETVCHANNEL_ZEE_KANNADA"],"ZeeTV.in@SD":["Zee.TV.in","ZEE.TV.in","ZeeTV.in","543105","543086","ts63","ts557","LIVETV_LIVETVCHANNEL_ZEE_TV_HD"],"ZeeTalkies.in@HD":["Zee.Talkies.in","ZEE.TALKIES.in","ZeeTalkies.in","543200","543068","ts249","ts515","LIVETV_LIVETVCHANNEL_ZEE_TALKIES_HD"],"ZeeTamil.in@SD":["Zee.Tamil.in","ZEE.TAMIL.in","ZeeTamil.in","543143","543165","ts257","ts608","LIVETV_LIVETVCHANNEL_ZEE_TAMIL_HD"],"Zing.in@SD":["ZING.in","Zing.in","543208","ts517","LIVETV_LIVETVCHANNEL_ZING","jtv585","0-9-zing","585"],"custom.aljazeera.english":["AL.Jazeera.in","ALJAZEERA.in","AlJazeera.in","543135","ts190","jtv494","494"],"custom.colors":["Colors.in","Colors.SD.in","Colors.HD.in","COLORS.in","COLORS.HD.in","543080","543247","ts543"],"custom.duck.tv":["jtv3537","3537"],"custom.ekamra.cinema":["Ekamra.Cinema.in"],"custom.ekamra.manoranjan":["Ekamra.Manoranjan.in","ts1207"],"custom.ekamra.musiq":["Ekamra.Musiq.in"],"custom.solntse":["&TV.HD.in","and.TV.in","andtv.in","AndTV.in","10000000028050000","ts578","ts40","LIVETV_LIVETVCHANNEL_SYMANDTV"],"custom.sonic.bangla":["Sonic.Bangla.in","jtv1345","1345"],"custom.sony.ten.1":["Sony.Ten.1.in","Sony.Ten.1.HD.in","jtv162","jtv514","514","162"],"custom.sony.ten.5":["Sony.Ten.5.HD.in","Sony.Ten.5.in","jtv155","jtv525","155","525"],"custom.sonyten2":["Sony.Ten.2.HD.in","jtv891","891"],"custom.starsports2":["Star.Sports.2.HD.in","STAR.SPORTS.2.in","STAR.SPORTS.2.HD.in","StarSports2.in","543210","543498","ts235","LIVETV_LIVETVCHANNEL_STAR_SPORTS_2"]};





















































































function json(data, status = 200) {
  return new Response(JSON.stringify(data), { status, headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store" } });
}
function parseAttrs(line) {
  const attrs = {}; let m; const re = /([\w-]+)="([^"]*)"/g;
  while ((m = re.exec(line))) attrs[m[1]] = m[2]; return attrs;
}
function stableId(value) {
  let h = 0x811c9dc5; for (let i=0;i<value.length;i++) { h ^= value.charCodeAt(i); h = Math.imul(h,0x01000193); }
  return (h >>> 0) & 0x7fffffff;
}
function parsePlaylist(text) {
  const lines=text.split(/\r?\n/); let categoryNames=[];
  const header=lines.find(x=>x.startsWith("#PLAYLIST-STUDIO-CATEGORIES:"));
  if(header) { try { categoryNames=JSON.parse(header.slice(header.indexOf(":")+1)); } catch {} }
  const entries=[];
  for(let i=0;i<lines.length;i++){
    if(!lines[i].startsWith("#EXTINF:")) continue;
    const ext=lines[i], comma=ext.lastIndexOf(","); if(comma<0 || i+1>=lines.length) continue;
    const a=parseAttrs(ext), name=ext.slice(comma+1).trim(), url=lines[i+1].trim();
    if(!name || !url || url.startsWith("#")) continue;
    const group=a["group-title"] || "Uncategorized", tvgId=a["tvg-id"] || "", tvgName=a["tvg-name"] || name, logo=a["tvg-logo"] || "";
    entries.push({ id:stableId(tvgId+"|"+name+"|"+group+"|"+url), name, tvgId, tvgName, logo, group, channelNo:a["tvg-chno"]||"", url });
    i++;
  }
  const groups=[]; for(const g of categoryNames) if(!groups.includes(g)) groups.push(g);
  for(const e of entries) if(!groups.includes(e.group)) groups.push(e.group);
  const categoryId=new Map(groups.map((g,i)=>[g,String(i+1)]));
  for(const e of entries) e.categoryId=categoryId.get(e.group)||"0";
  return {entries,groups};
}
async function getPlaylist(env){
  const cache=caches.default, key=new Request(CACHE_KEY), cached=await cache.match(key); if(cached) return cached.text();
  const r=await fetch(env.PLAYLIST_URL||DEFAULT_PLAYLIST_URL,{headers:{"user-agent":"BDIX-IPTV-Xtream-Gateway/1.0"}});
  if(!r.ok) throw new Error("Playlist fetch failed: "+r.status);
  const text=await r.text();
  await cache.put(key,new Response(text,{headers:{"content-type":"text/plain","cache-control":"public, max-age="+CACHE_TTL}}));
  return text;
}
function auth(url,env){return url.searchParams.get("username")===env.XTREAM_USERNAME && url.searchParams.get("password")===env.XTREAM_PASSWORD;}
function pathAuth(parts,env){return parts[1]===env.XTREAM_USERNAME && parts[2]===env.XTREAM_PASSWORD;}
function userInfo(request,env){
  const u=new URL(request.url);
  const host=u.hostname;
  return {user_info:{username:env.XTREAM_USERNAME,password:env.XTREAM_PASSWORD,message:"BDIX-IPTV Xtream Gateway",auth:1,status:"Active",exp_date:null,is_trial:"0",active_cons:"0",created_at:String(Math.floor(Date.now()/1000)),max_connections:"2",allowed_output_formats:["ts","m3u8"]},server_info:{url:host,port:"443",https_port:"443",server_protocol:"https",rtmp_port:"",timezone:env.TIMEZONE||"Asia/Dhaka",timestamp_now:Math.floor(Date.now()/1000),time_now:new Date().toLocaleString("sv-SE",{timeZone:env.TIMEZONE||"Asia/Dhaka"})}};
}

async function getEpg(env){
  const cache=caches.default, key=new Request(EPG_CACHE_KEY), cached=await cache.match(key);
  if(cached) return cached.text();

  // Prefer the repository's validated, playlist-aligned XMLTV publication.
  // This is the same epg.xml that the maintenance workflow validates before publish.
  try{
    const r=await fetch(EPG_PUBLIC_URL,{headers:{"user-agent":"BDIX-IPTV-Xtream-Gateway/1.0","accept":"application/xml,text/xml,*/*"}});
    if(r.ok){
      const xml=await r.text();
      if(xml.includes("<tv") && xml.includes("<programme ")){
        await cache.put(key,new Response(xml,{headers:{"content-type":"application/xml; charset=utf-8","cache-control":"public, max-age="+EPG_CACHE_TTL}}));
        return xml;
      }
    }
  }catch{}

  // Fallback to the public source feeds if the generated publication is unavailable.
  const xmls=[];
  for(const source of EPG_URLS){
    try{
      const r=await fetch(source,{headers:{"user-agent":"BDIX-IPTV-Xtream-Gateway/1.0","accept":"application/gzip, application/xml, text/xml, */*"}});
      if(!r.ok) continue;
      const bytes=await r.arrayBuffer();
      let xml;
      const contentEncoding=(r.headers.get("content-encoding")||"").toLowerCase();
      const isGzip=bytes.byteLength>=2 && new Uint8Array(bytes)[0]===0x1f && new Uint8Array(bytes)[1]===0x8b;
      if(contentEncoding.includes("gzip") && !isGzip){
        xml=new TextDecoder().decode(bytes);
      }else if(isGzip || source.endsWith(".gz")){
        try{
          xml=await new Response(new Blob([bytes]).stream().pipeThrough(new DecompressionStream("gzip"))).text();
        }catch{
          continue;
        }
      }else{
        xml=new TextDecoder().decode(bytes);
      }
      if(xml.includes("<tv") && xml.includes("<programme ")) xmls.push(xml);
    }catch{}
  }
  if(!xmls.length) throw new Error("All EPG sources failed");
  const merged=xmls.join("\n");
  await cache.put(key,new Response(merged,{headers:{"content-type":"application/xml; charset=utf-8","cache-control":"public, max-age="+EPG_CACHE_TTL}}));
  return merged;
}

function xmlUnescape(s){
  return String(s??"").replace(/&amp;/g,"&").replace(/&lt;/g,"<").replace(/&gt;/g,">").replace(/&quot;/g,'"').replace(/&apos;/g,"'");
}
function normalizeEpgName(s){
  return String(s??"").toLowerCase()
    .replace(/&amp;/g,"&")
    .replace(/\b(hd|sd|uhd|fhd|tv|channel)\b/g,"")
    .replace(/[^a-z0-9]+/g,"");
}
function epgNameAliases(s){
  const n=normalizeEpgName(s);
  if(!n) return [];
  const out=new Set([n]);
  const aliases={
    aakaashaath:"aakashaath",
    aakashath:"aakashaath",
    sonyaath:"sonyaath",
    zeeebangla:"zeebangla",
    zeebanglahd:"zeebangla",
    starjalshahd:"starjalsha",
    starjalsa:"starjalsha",
    colorsbanglahd:"colorsbangla",
    enter10bangla:"enter10bangla",
    goldminesmovie:"goldminesmovies",
    sonyentertainmenttv:"sonyentertainmenttelevision"
  };
  if(aliases[n]) out.add(aliases[n]);
  return [...out];
}
function parseXmltv(xml){
  const byId=new Map(), nameToIds=new Map();
  const add=(key,p)=>{if(!key)return; if(!byId.has(key))byId.set(key,[]); byId.get(key).push(p);};
  const cr=/<channel\b([^>]*)>([\s\S]*?)<\/channel>/g;
  let cm;
  while((cm=cr.exec(xml))){
    const a=parseAttrs(cm[1]), id=xmlUnescape(a.id||"");
    const names=[...cm[2].matchAll(/<display-name(?:\s[^>]*)?>([\s\S]*?)<\/display-name>/gi)].map(x=>xmlUnescape(x[1].replace(/<[^>]+>/g,"").trim())).filter(Boolean);
    if(id) for(const n of names) for(const k of epgNameAliases(n)){
      if(!nameToIds.has(k))nameToIds.set(k,[]);
      if(!nameToIds.get(k).includes(id)) nameToIds.get(k).push(id);
    }
  }
  const re=/<programme\b([^>]*)>([\s\S]*?)<\/programme>/g;
  let m;
  while((m=re.exec(xml))){
    const a=parseAttrs(m[1]), channel=xmlUnescape(a.channel||"");
    if(!channel) continue;
    const body=m[2];
    const tm=body.match(/<title(?:\s[^>]*)?>([\s\S]*?)<\/title>/i);
    const dm=body.match(/<desc(?:\s[^>]*)?>([\s\S]*?)<\/desc>/i);
    const p={start:a.start||"",stop:a.stop||"",title:xmlUnescape(tm?tm[1].replace(/<[^>]+>/g,""):""),desc:xmlUnescape(dm?dm[1].replace(/<[^>]+>/g,""):"")};
    add(channel,p);
    const base=channel.replace(/@[^.]+$/,"");
    if(base!==channel) add(base,p);
  }
  return {byId,nameToIds};
}
function epgKeyVariants(id,name){
  const v=new Set([id,name]);
  for(const x of [id,name,...(EPG_ID_MAP[id]||[])]){
    if(!x) continue;
    v.add(x.replace(/@[^.]+$/,""));
    if(!/@/.test(x) && /\.(bd|in|uk|us|au|pk|ae|lk|np|bt)$/.test(x)) v.add(x+"@SD");
  }
  for(const x of epgNameAliases(name)) v.add(x);
  return [...v].filter(Boolean);
}
function normalizeEpgId(s){
  return String(s??"").toLowerCase().replace(/@(?:sd|hd|uhd|fhd)$/i,"").replace(/[^a-z0-9]+/g,"");
}
function findEpgPrograms(epg,entry){
  const variants=epgKeyVariants(entry.tvgId,entry.name);
  for(const key of variants){
    const programs=epg.byId.get(key);
    if(programs?.length) return programs;
  }
  // EPGShare uses punctuation-heavy IDs such as Star.Jalsha.in and Zee.Bangla.in,
  // while the playlist often uses StarJalsha.in and ZeeBangla.in. Match those
  // equivalent IDs before falling back to display-name matching.
  const normalizedVariants=new Set(variants.map(normalizeEpgId).filter(Boolean));
  for(const [id,programs] of epg.byId){
    if(programs?.length && normalizedVariants.has(normalizeEpgId(id))) return programs;
  }
  for(const alias of epgNameAliases(entry.name)){
    const ids=epg.nameToIds.get(alias)||[];
    for(const id of ids){
      const programs=epg.byId.get(id);
      if(programs?.length) return programs;
    }
  }
  return [];
}
function toTimestamp(s){
  const m=/^(\d{4})(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})/.exec(String(s||""));
  if(!m) return 0;
  return Math.floor(Date.UTC(+m[1],+m[2]-1,+m[3],+m[4],+m[5],+m[6])/1000);
}
function epgListings(entry,programs){
  return programs.map((p,i)=>({
    id:String(stableId(entry.tvgId+"|"+p.start+"|"+p.stop+"|"+p.title+"|"+i)),
    epg_id:entry.tvgId||entry.name,
    title:p.title||"",
    lang:"en",
    start:String(p.start||""),
    end:String(p.stop||""),
    description:p.desc||"",
    channel_id:entry.tvgId||entry.name,
    start_timestamp:toTimestamp(p.start),
    stop_timestamp:toTimestamp(p.stop),
    now_playing:toTimestamp(p.start)<=Math.floor(Date.now()/1000) && toTimestamp(p.stop)>Math.floor(Date.now()/1000) ? 1 : 0,
    has_archive:0
  }));
}
function xmlEscape(s){
  return String(s??"").replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");
}
function epgXml(data,epg){
  const out=['<?xml version="1.0" encoding="UTF-8"?>','<tv generator-info-name="BDIX-IPTV Xtream Gateway">'];
  for(const e of data.entries){
    const id=e.tvgId||e.name;
    out.push('<channel id="'+xmlEscape(id)+'"><display-name>'+xmlEscape(e.name)+'</display-name>'+(e.logo?'<icon src="'+xmlEscape(e.logo)+'"/>':'')+'</channel>');
    for(const p of findEpgPrograms(epg,e)){
      if(!p.start || !p.stop) continue;
      out.push('<programme start="'+xmlEscape(p.start)+'" stop="'+xmlEscape(p.stop)+'" channel="'+xmlEscape(id)+'"><title>'+xmlEscape(p.title||"")+'</title>'+(p.desc?'<desc>'+xmlEscape(p.desc)+'</desc>':'')+'</programme>');
    }
  }
  out.push('</tv>');
  return out.join("");
}

function categories(data){return data.groups.map((name,i)=>({category_id:String(i+1),category_name:name,parent_id:0}));}
function streams(data,cat){
  const src=cat?data.entries.filter(e=>e.categoryId===String(cat)):data.entries;
  return src.map((e,i)=>({num:Number(e.channelNo)||i+1,name:e.name,stream_type:"live",stream_id:e.id,stream_icon:e.logo,epg_channel_id:(e.tvgId||e.name),added:"0",category_id:e.categoryId,custom_sid:"",tv_archive:0,direct_source:e.url,tv_archive_duration:0}));
}
function m3u(data,request,env){
  const u=new URL(request.url), ext=(u.searchParams.get("output")||"m3u8").toLowerCase()==="ts"?"ts":"m3u8", epgUrl=u.origin+"/xmltv-public.php", out=[`#EXTM3U url-tvg="${epgUrl}" x-tvg-url="${epgUrl}"`];
  for(const e of data.entries){
    const attrs=[`tvg-id="${e.tvgId}"`,`tvg-name="${e.tvgName}"`,`tvg-logo="${e.logo}"`,`group-title="${e.group}"`];
    if(e.channelNo) attrs.push(`tvg-chno="${e.channelNo}"`);
    out.push("#EXTINF:-1 "+attrs.join(" ")+","+e.name);
    out.push(u.origin+"/live/"+env.XTREAM_USERNAME+"/"+env.XTREAM_PASSWORD+"/"+e.id+"."+ext);
  }
  return new Response(out.join("\n")+"\\n",{headers:{"content-type":"audio/x-mpegurl; charset=utf-8","cache-control":"no-store"}});
}
function emptyEpg(){return new Response('<?xml version="1.0" encoding="UTF-8"?><tv generator-info-name="BDIX-IPTV Xtream Gateway"></tv>',{headers:{"content-type":"application/xml; charset=utf-8","cache-control":"no-store"}});}
export default {
 async fetch(request,env){
  try{
   if(!env.XTREAM_USERNAME||!env.XTREAM_PASSWORD) return json({error:"Xtream credentials are not configured."},500);
   const url=new URL(request.url), path=url.pathname;
   if(path==="/"||path==="/health") return json({ok:true,service:"BDIX-IPTV Xtream Gateway"});
   if(path==="/epg-health"){
    const epg=parseXmltv(await getEpg(env));
    const checks=[["StarJalsha.in","Star Jalsha"],["ZeeBangla.in","Zee Bangla"],["SonyAath.in","Sony AATH"]];
    const result={sources:EPG_URLS,channel_count:epg.byId.size,name_map_count:epg.nameToIds.size,checks:{}};
    for(const [id,name] of checks){
      const variants=epgKeyVariants(id,name);
      let matched=null,count=0;
      for(const k of variants){const p=epg.byId.get(k); if(p?.length){matched=k;count=p.length;break;}}
      const nk=normalizeEpgName(name);
      const nameIds=epg.nameToIds.get(nk)||[];
      let nameMatched=null,nameCount=0;
      for(const x of nameIds){const p=epg.byId.get(x); if(p?.length){nameMatched=x;nameCount=p.length;break;}}
      result.checks[id]={playlist_name:name,matched,count,nameIds:nameIds.slice(0,5),nameMatched,nameCount};
    }
    return json(result);
   }
   if(path==="/epg-audit"){
    const data=parsePlaylist(await getPlaylist(env)), epg=parseXmltv(await getEpg(env));
    const rows=data.entries.map(e=>{
      const programs=findEpgPrograms(epg,e);
      return {name:e.name,tvg_id:e.tvgId,group:e.group,programme_count:programs.length,matched:programs.length>0};
    });
    const matched=rows.filter(x=>x.matched), missing=rows.filter(x=>!x.matched);
    return json({
      sources:EPG_URLS,
      total:rows.length,
      matched:matched.length,
      missing:missing.length,
      by_group:[...new Set(rows.map(x=>x.group))].map(g=>{
        const a=rows.filter(x=>x.group===g);
        return {group:g,total:a.length,matched:a.filter(x=>x.matched).length,missing:a.filter(x=>!x.matched).length};
      }),
      missing_channels:missing.slice(0,300)
    });
   }
   if(path==="/player_api.php"){
    if(!auth(url,env)) return json({user_info:{auth:0,status:"Invalid credentials"}},401);
    const action=url.searchParams.get("action")||"", data=parsePlaylist(await getPlaylist(env));
    if(!action||action==="get_account_info") return json(userInfo(request,env));
    if(action==="get_live_categories") return json(categories(data));
    if(action==="get_live_streams") return json(streams(data,url.searchParams.get("category_id")));
    if(action==="get_short_epg"||action==="get_simple_data_table"){
      const streamId=Number(url.searchParams.get("stream_id")), entry=data.entries.find(e=>e.id===streamId);
      if(!entry) return json({epg_listings:[]});
      const epg=parseXmltv(await getEpg(env)), listings=epgListings(entry,findEpgPrograms(epg,entry));
      const limit=Number(url.searchParams.get("limit"))||4;
      return json({epg_listings:listings.slice(0,Math.max(1,Math.min(limit,100)))});
    }
    if(action==="get_all_epg") {
      const epg=parseXmltv(await getEpg(env)), all=[];
      for(const e of data.entries) all.push(...epgListings(e,findEpgPrograms(epg,e)));
      return json({epg_listings:all});
    }
    if(action==="get_vod_categories"||action==="get_series_categories"||action==="get_vod_streams"||action==="get_series") return json([]);
    return json({error:"Unsupported action"},400);
   }
   if(path==="/get.php"){if(!auth(url,env)) return new Response("Unauthorized",{status:401}); return m3u(parsePlaylist(await getPlaylist(env)),request,env);}
   if(path==="/xmltv-public.php"){
    const data=parsePlaylist(await getPlaylist(env)), epg=parseXmltv(await getEpg(env));
    return new Response(epgXml(data,epg),{headers:{"content-type":"application/xml; charset=utf-8","cache-control":"public, max-age=900"}});
   }
   if(path==="/xmltv.php"){
    if(!auth(url,env)) return new Response("Unauthorized",{status:401});
    const data=parsePlaylist(await getPlaylist(env)), epg=parseXmltv(await getEpg(env));
    return new Response(epgXml(data,epg),{headers:{"content-type":"application/xml; charset=utf-8","cache-control":"no-store"}});
   }
   if(path.startsWith("/live/")){
    const parts=path.split("/").filter(Boolean); if(!pathAuth(parts,env)) return new Response("Unauthorized",{status:401});
    const id=Number((parts[3]||"").split(".")[0]); if(!Number.isInteger(id)) return new Response("Bad stream ID",{status:400});
    const data=parsePlaylist(await getPlaylist(env)), stream=data.entries.find(e=>e.id===id);
    if(!stream) return new Response("Stream not found",{status:404});
    return Response.redirect(stream.url,302);
   }
   return new Response("Not found",{status:404});
  }catch(e){return json({error:String(e?.message||e)},500);}
 }
};
