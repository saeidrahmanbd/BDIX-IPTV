// Deployment pipeline: code and required secrets are deployed as one version.
const DEFAULT_PLAYLIST_URL = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u";
const DEFAULT_BDIX_PLAYLIST_URL = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/BDIX-Playlist.m3u";
const CACHE_KEY = "https://bdix-iptv.internal/playlist-v5-backup-stream-filter";
const CACHE_TTL = 60;

const EPG_PUBLIC_URL = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/epg/epg.xml";
const EPG_URLS = [
  // IN1 is the broad India guide. IN4 is a smaller complementary India guide
  // with additional regional/channel IDs. Keep the live set to these two to
  // avoid the memory pressure caused by the much larger ALL_SOURCES feed.
  "https://epgshare01.online/epgshare01/epg_ripper_IN1.xml.gz",
  "https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz",
  "https://iptv-epg.org/files/epg-in.xml"
];
const EPG_CACHE_KEY = "https://bdix-iptv.internal/epg-xml-v12";
const EPG_CACHE_TTL = 900;
// Direct M3U EPG endpoint deployment trigger. v10: IN1 + complementary IN4.

// Cross-map playlist tvg-id variants to canonical EPG IDs used by public guides.
const EPG_ID_MAP = {"7SMusic.in@SD":["7S.MUSIC.in","LIVETV_LIVETVCHANNEL_7S_MUSIC"],"7XMusic.in@SD":["7X.Music.in","ts1019","jtv1871","1871"],"9XJalwa.in":["9X.Jalwa.in","9XJalwa.in","407811","LIVETV_LIVETVCHANNEL_9X_JALWA","jtv440","440"],"9XJhakaas.in@SD":["9x.Jhakaas.in","9X.JHAKAAS.in","543161","90012","jtv441","441"],"9XM.in@SD":["9XM.in","543367","77447","ts139","LIVETV_LIVETVCHANNEL_9XM","jtv587","587"],"9XTashan.in@SD":["9X.Tashan.in","9X.TASHAN.in","9XTashan.in","543036","142504","LIVETV_LIVETVCHANNEL_9X_TASHAN","jtv732","732"],"AakaashAath.in@SD":["AakaashAath.in"],"AamarBangla.in":["Amar.Bangla.TV.in"],"AaryaaTV.in":["jtv3395","3395"],"AlJazeera.qa@English":["AL.Jazeera.in","ALJAZEERA.in","AlJazeera.in","543135","ts190","jtv494","494"],"AlankarTV.in@SD":["Alankar.TV.in","ALANKAR.in","543118","142630","LIVETV_LIVETVCHANNEL_ALANKAR","jtv686","686"],"AmritaTV.in@SD":["Amrita.TV.in","AMRITA.in","AmritaTV.in","543102","142632","ts178","jtv723","723"],"AnandTV.in@SD":["Anand.TV.in","jtv3294","3294"],"AndPictures.in@SD":["And.Pictures.in","and.PICTURES.in","AndPictures.in","142638","142637","ts267","ts148","LIVETV_LIVETVCHANNEL_SYMANDPICTURES"],"AndTV.in@SD":["&TV.HD.in","and.TV.in","andtv.in","142640","142641","ts578","ts40","LIVETV_LIVETVCHANNEL_SYMANDTV"],"AndpriveHD.in":["And.Prive.HD.in","and.PRIVE.HD.in"],"AndxplorHD.in":["&Xplor.HD.in","and.xplorHD.in","LIVETV_LIVETVCHANNEL_SYMANDXPLOR_HD","And.Xplor.HD.in","And.XplorHD.in"],"AnimalPlanet.in@SD":["Animal.Planet.HD.in","ANIMAL.PLANET.in","AnimalPlanet.in","543099","158140","157574","ts130","ts287"],"AnjanTV.in@SD":["Anjan.TV.in","AnjanTV.in","ts180","jtv919","919"],"B4UKadak.in@SD":["B4U.Kadak.in","B4U.KADAK.in","B4UKadak.in","543225","142695","ts730","LIVETV_LIVETVCHANNEL_B4U_KADAK","jtv1295"],"B4UMovies.in@India":["B4U.Movies.in","B4UMovies.in","543309","140063","ts7","LIVETV_LIVETVCHANNEL_B4U_MOVIES","jtv182","182"],"B4UMusic.in@India":["B4U.Music.in","B4U.MUSIC.in","B4UMusic.in","543038","158141","ts9","LIVETV_LIVETVCHANNEL_B4U_MUSIC","jtv183"],"BBCNews.uk":["158142","ts188","LIVETV_LIVETVCHANNEL_BBC_NEWS"],"BHI.Channel.in":["BHI.Channel.in"],"BSTV.pk@SD":["BSTV.in","jtv2765","2765"],"BalleBalle.in@SD":["Balle.Balle.TV.in","BALLE.BALLE.in","543327","142697","jtv1453","6437","1453"],"BangBangTV":["6590"],"BhojpuriCinema.in@SD":["Bhojpuri.Cinema.in","BHOJPURI.CINEMA.in","BhojpuriCinema.in","543361","142713","LIVETV_LIVETVCHANNEL_BHOJPURI_CINEMA","jtv486","486"],"CartoonNetwork.uk":["Cartoon.Network.HD+.in","Cartoon.Network.in","CARTOON.NETWORK.in","CartoonNetwork+.in","CartoonNetwork.in","543449","157576","ts238"],"Chithiram.in@SD":["142738","ts1166"],"Colors.Bangla.in":["Colors.Bangla.in"],"Colors.in":["Colors.in","COLORS.in","543080","543247","158144","158149","ts543","ts52"],"ColorsBanglaCinema.in@SD":["Colors.Bangla.Cinema.in"],"ColorsCineplex.in@SD":["Colors.Cineplex.in","Colors.Cineplex.HD.in","COLORS.CINEPLEX.in","543298","158147","158146","ts61","ts53"],"ColorsCineplexBollywood.in@SD":["Colors.Cineplex.Bollywood.in","142749","ts1000","LIVETV_LIVETVCHANNEL_COLORS_CINEPLEX_BOLLYWOOD","jtv1763","1763"],"ColorsCineplexSuperhits.in@SD":["Colors.Cineplex.Superhits.in","COLORS.CINEPLEX.SUPERHITS.in","543230","142750","LIVETV_LIVETVCHANNEL_COLORS_CINEPLEX_SUPERHITS","ts1025"],"ColorsGujarati.in@SD":["Colors.Gujarati.in","COLORS.GUJARATI.in","543314","158148","ts107","LIVETV_LIVETVCHANNEL_COLORS_GUJARATI","jtv196","196"],"ColorsKannada.in@SD":["Colors.Kannada.SD.in","Colors.Kannada.HD.in","COLORS.KANNADA.in","COLORSKANNADA.in","543329","543147","157579","158235"],"ColorsKannadaCinema.in@SD":["Colors.Kannada.Cinema.in","142752","ts667","LIVETV_LIVETVCHANNEL_COLORS_KANNADA_CINEMA","jtv1632","1632"],"ColorsMarathi.in@SD":["Colors.Marathi.HD.in","Colors.Marathi.SD.in","COLORS.MARATHI.in","COLORSMARATHI.in","543065","543277","157580","158237"],"ColorsRishteyAmericas.in":["Colors.Rishtey.in","COLORS.RISHTEY.in","ColorsRishtey.in","543236","158239","ts438","LIVETV_LIVETVCHANNEL_COLORS_RISHTEY","jtv279"],"ColorsSuper.in":["Colors.Super.in","COLORS.SUPER.in","543284","158240","ts533","LIVETV_LIVETVCHANNEL_COLORS_SUPER","jtv785","785"],"ColorsTamil.in@SD":["Colors.Tamil.in","COLORSTAMIL.in","543334","543302","158241","157682","ts674","ts418"],"CricketGold.au@SD":["6995"],"DDArunPrabha.in@SD":["DD.Arunprabha.in","DD.ARUN.PRABHA.in","543094","142776","ts758","LIVETV_LIVETVCHANNEL_DD_ARUNPRABHA","jtv1328","1328"],"DDAssam.in@SD":["142777","LIVETV_LIVETVCHANNEL_DD_NORTH_EAST"],"DDBangla.in@SD":["DD.Bangla.in"],"DDBharati.in@SD":["DD.bharati.in","142779","ts316","LIVETV_LIVETVCHANNEL_DD_BHARATI","jtv580","580"],"DDBihar.in@SD":["DD.Bihar.in","DD.BIHAR.in","543478","142780","ts317","LIVETV_LIVETVCHANNEL_DD_BIHAR","jtv539","539"],"DDChandana.in@SD":["DD.Chandana.in","DDChandana.in","543175","142781","ts321","LIVETV_LIVETVCHANNEL_DD_CHANDANA"],"DDChhattisgarh.in@SD":["154889","ts1216"],"DDGirnar.in@SD":["DD.Girnar.in","DD.GIRNAR.in","DDGirnar.in","543062","142782","209534","ts323","LIVETV_LIVETVCHANNEL_DD_GIRNAR"],"DDGoa.in@SD":["142783","ts1215"],"DDHaryana.in@SD":["142784","ts1212"],"DDHimachalPradesh.in@SD":["142785","ts1217","LIVETV_LIVETVCHANNEL_DD_SHIMLA"],"DDIndia.in@SD":["DD.India.in","DD.INDIA.in","DDIndia.in","543088","158251","154545","ts324","ts1219"],"DDJharkhand.in@SD":["142787","ts1188"],"DDKashir.in@SD":["DD.Kashir.in","543500","142788","ts325","LIVETV_LIVETVCHANNEL_DD_KASHIR","jtv716","716"],"DDKisan.in@SD":["DD.Kisan.in","DDKisan.in","543191","209326","142789","ts326","LIVETV_LIVETVCHANNEL_DD_KISAN","jtv583"],"DDMadhyaPradesh.in@SD":["DD.Madhya.Pradesh.in","DDMadhyaPradesh.in","142790","ts330","LIVETV_LIVETVCHANNEL_DD_MP","jtv536","536"],"DDMalayalam.in@SD":["DD.Malayalam.in","DD.MALAYALAM.in","DDMalayalam.in","543259","142791","ts328","LIVETV_LIVETVCHANNEL_DD_MALAYALAM","jtv699"],"DDManipur.in@SD":["142792","ts329","LIVETV_LIVETVCHANNEL_DD_IMPHAL"],"DDMeghalaya.in@SD":["142793","ts991","LIVETV_LIVETVCHANNEL_DD_SHILLONG"],"DDNagaland.in@SD":["142795","ts1214"],"DDNational.in@SD":["DD.National.in","DDNational.in","543184","158252","158253","ts191","ts1218","LIVETV_LIVETVCHANNEL_DD_NATIONAL"],"DDOdia.in@SD":["DD.ODIA.in","DDOdia.in","543028","ts333","LIVETV_LIVETVCHANNEL_DD_ORIYA"],"DDPunjabi.in@SD":["DD.Punjabi.in","DD.PUNJABI.in","DDPunjabi.in","543437","142800","ts335","LIVETV_LIVETVCHANNEL_DD_PUNJABI","jtv715"],"DDRajasthan.in@SD":["DD.RAJASTHAN.in","DDRajasthan.in","543060","142801","ts332","LIVETV_LIVETVCHANNEL_DD_RAJASTHAN"],"DDSahyadri.in@SD":["DD.SAHYADRI.in","DDSahyadri.in","543462","142803","209541","ts336","LIVETV_LIVETVCHANNEL_DD_SAHYADRI"],"DDSaptagiri.in@SD":["DD.Saptagiri.in","DDSaptagiri.in","543376","142804","ts337","LIVETV_LIVETVCHANNEL_DD_SAPTAGIRI","jtv706","706"],"DDSports.in@SD":["DD.Sports.in","DDSports.in","543389","158312","158255","ts1191","ts223","LIVETV_LIVETVCHANNEL_DD_SPORTS"],"DDTamil.in@SD":["DD.TAMIL.in","DDTamil.in","543273","142797","209540","ts334","LIVETV_LIVETVCHANNEL_DD_TAMIL","jtv726"],"DDTripura.in@SD":["142806","ts1210","LIVETV_LIVETVCHANNEL_DD_TRIPURA"],"DDUrdu.in@SD":["DD.urdu.in","DD.URDU.in","543021","142808","ts338","LIVETV_LIVETVCHANNEL_DD_URDU","jtv712","712"],"DDUttarPradesh.in@SD":["DD.Uttar.Pradesh.in","ts339","LIVETV_LIVETVCHANNEL_DD_UP","jtv540","540"],"DDUttarakhand.in@SD":["ts1213"],"DDYadagiri.in@SD":["DD.YADAGIRI.in","DDYadagiri.in","543493","142810","ts548","LIVETV_LIVETVCHANNEL_DD_YADAGIRI","jtv1516","1516"],"Dangal2.in@SD":["Dangal.2.in","Dangal2.in","543069","142772","LIVETV_LIVETVCHANNEL_DANGAL_2"],"DangalTV.in@SD":["Dangal.in","DANGAL.in","543037","142771","LIVETV_LIVETVCHANNEL_DANGAL","jtv701","701"],"DarshanaTV.in@SD":["DARSHANA.in","543481","142774"],"DesiChannel.in":["Desi.Channel.in","jtv906","906"],"DhoolTV.in@SD":["jtv3610"],"DhoomMusic.in@SD":["Dhoom.Music.Bangla.in"],"DiscoveryChannel.in@SD":["Discovery.in","DISCOVERY.CHANNEL.in","543256","100869","ts219","LIVETV_LIVETVCHANNEL_DISCOVERY_CHANNEL"],"DiscoveryKids.au":["Discovery.Kids.in","DISCOVERY.KIDS.in","DiscoveryKids.in","543485","159011","ts119","LIVETV_LIVETVCHANNEL_DISCOVERY_KIDS"],"DisneyChannel.in@HD":["DISNEY.CHANNEL.in"],"DocuBayTV.in":["jtv3402","3402"],"E24.in":["E.24.in","LIVETV_LIVETVCHANNEL_E24","591"],"ETVBalBharat.in@SD":["ETV.BAL.BHARAT.in","543412","143025","LIVETV_LIVETVCHANNEL_ETV_BAL_BHARAT"],"ETVBeats.in@HD":["3559"],"ETVCinema.in":["ETV.Cinema.in","ETV.CINEMA.in","ETVCinema.in","543267","143026","LIVETV_LIVETVCHANNEL_ETV_CINEMA","jtv1665","jtv252"],"ETVComedy.in":["jtv3561","3561"],"ETVJosh.in":["jtv3560","3560"],"ETVMusic.in":["143023","ts358","LIVETV_LIVETVCHANNEL_ETV_ABHIRUCHI","jtv3559","565"],"EkamraBharatOdia.in@SD":["Ekamra.Bharat.Odia.in","ts1196"],"Enterr10Bangla.in@SD":["ENTER10.BANGLA.in"],"EpicBharat.in@SD":["ts1184","SWIFTTV_LIVECHANNEL_86","jtv3383","3383"],"EpicBhojpuri.in@SD":["157803","ts830","LIVETV_LIVETVCHANNEL_FILAMCHI_BHOJPURI","jtv3384","3384"],"EpicMusic.in@SD":["159097","ts733","LIVETV_LIVETVCHANNEL_SHOWBOX"],"FaktMarathi.in@SD":["Fakt.Marathi.in","FAKT.MARATHI.in","FaktMarathi.in","543453","143038","LIVETV_LIVETVCHANNEL_FAKT_MARATHI","jtv738","738"],"FoodFood.in@SD":["Food.Food.in","FoodFood.in","ts117","jtv561","561"],"GREATmovies.uk":["0-9-9z5910243"],"Goldmines.in@SD":["Goldmines.in","143087","ts823","LIVETV_LIVETVCHANNEL_GOLDMINES"],"GoldminesBollywood.in@SD":["Goldmines.Bollywood.in","143089","LIVETV_LIVETVCHANNEL_GOLDMINES_BOLLYWOOD"],"GoldminesMovies.in@SD":["Goldmines.Movies.in","142881","ts1499"],"HiDost.in@SD":["Hi.Dost!.in","jtv1232","1232"],"HistoryTV18.in@SD":["History.TV18.SD.in","History.TV18.HD.in","HISTORY.TV18.HD.in","543336","143132","143133","LIVETV_LIVETVCHANNEL_HISTORY_TV18","LIVETV_LIVETVCHANNEL_HISTORY_TV18_HD"],"Hungama.in@SD":["Hungama.in","HUNGAMA.in","543181","143150","LIVETV_LIVETVCHANNEL_HUNGAMA","jtv1391","1391"],"INWILD.nl":["jtv3389","3389"],"InTravel.in@HD":["jtv3392","3392"],"Insync.in":["Insync.in","jtv1286","6633","1286"],"InvestigationDiscovery.in@SD":["Investigation.Discovery.in","InvestigationDiscovery.in","543196","157811","ts633","ts1276","LIVETV_LIVETVCHANNEL_INVESTIGATION_DISCOVERY_HD","LIVETV_LIVETVCHANNEL_INVESTIGATION_DISCOVERY"],"IsaiAruvi.in@SD":["ISAI.ARUVI.in","Isaiaruvi.in","543163","143212","ts647","LIVETV_LIVETVCHANNEL_ISAI_ARUVI"],"JeevanTV.in@SD":["Jeevan.TV.in","JeevanTV.in","ts372","jtv842","842"],"Jonack.in@SD":["Jonack.in","143238","LIVETV_LIVETVCHANNEL_JONACK","jtv765","765"],"KairaliTV.in@SD":["Kairali.TV.in","KAIRALI.in","543357","143247","ts25","LIVETV_LIVETVCHANNEL_KAIRALI_TV","jtv710","710"],"KairaliWe.in@SD":["Kairali.WE.TV.in","143248","LIVETV_LIVETVCHANNEL_KAIRALI_WE","jtv731","731"],"KalaignarMurasu.in":["MURASU.in"],"KalaignarTV.in@SD":["Kalaignar.TV.in","KALAIGNAR.in","KalaignarTV.in","543395","143249","ts200","LIVETV_LIVETVCHANNEL_KALAIGNAR_TV","jtv1209"],"KappaTV.in@ALT1":["jtv786","786"],"KhushbooBangla.in@SD":["KhushbooBangla.in"],"KiteVicters.in@SD":["KITE.VICTERS.in","jtv1429","1429"],"LoLTV.in":["6609"],"MHOneDilSe.in@SD":["143536"],"MKSix.in":["MK.Six.in","jtv1647","1647"],"MNX.in@SD":["MNX.in","543194","143549","147570","ts234","ts599","LIVETV_LIVETVCHANNEL_MNX","LIVETV_LIVETVCHANNEL_MNX_HD"],"MONTVBangla.in":["Mon.TV.Bangla.in"],"MTVIndia.in@SD":["jtv248","248"],"MadhimugamTV.in":["Madhimugam.TV.in","jtv843","843"],"MahaaMax.in":["Mahaa.Max.in","LIVETV_LIVETVCHANNEL_MAHAA_MAX","jtv3143","7052","3143"],"ManoranjanGrand.in@SD":["Manoranjan.Grand.in","143302"],"ManoranjanMovies.in@SD":["143303"],"ManoranjanPrime.in@SD":["154892"],"ManoranjanTV.in@SD":["ManoranjanTV.in","143304","ts731","LIVETV_LIVETVCHANNEL_MANORANJAN_TV"],"Mastiii.in@SD":["Mastiii.in","143308"],"MazhavilManorama.in@SD":["Mazhavil.Manorama.in","MAZHAVIL.MANORAMA.in","MAZHAVILMANORAMA.in","543130","543345","143310","147769","ts395"],"Mh1Music.in@SD":["mh1.(Music).in","jtv742","742"],"MoviesNow.in@SD":["Movies.Now.in","MOVIES.NOW.in","MoviesNow.in","543174","143554","147571","ts562","ts173"],"MoviesNowPlus.in@SD":["MN+.HD.in","543209","143548","ts210","LIVETV_LIVETVCHANNEL_MNSYMPLUS","jtv477","477"],"MusicIndia.in@SD":["Music.India.in","143563","jtv250","250"],"NHBollyFlix.in":["RUNNTV_LIVECHANNEL_40","jtv3336","3336"],"NHBollyGold.in":["RUNNTV_LIVECHANNEL_39","jtv3338","3338"],"NHBollyRaga.in":["RUNNTV_LIVECHANNEL_41","jtv3343","3343"],"NationalGeographic.in@SD":["National.Geographic.HD.in","NATIONAL.GEOGRAPHIC.in","543180","543108","143574","143573","LIVETV_LIVETVCHANNEL_NATIONAL_GEOGRAPHIC_CHANNEL","LIVETV_LIVETVCHANNEL_NATIONAL_GEOGRAPHIC_CHANNEL_HD"],"NationalGeographicWild.in@SD":["Nat.Geo.Wild.HD.in","NAT.GEO.WILD.in","NAT.GEO.WILD.HD.in","NatGeoWild.in","543356","543052","143571","143572"],"NickJr.in@SD":["Nick.Jr.in","NICK.JR.in","543502","ts118"],"Nickelodeon.in@SD":["Nick.HD+.in","Nick.in","NICK.in","NICK.HD+.in","543260","543090","143625","159121"],"OdishaTV.in@SD":["OdishaTV.in"],"OnePaschima.in@SD":["One.Paschima.in"],"Only.Music.in":["Only.Music.in","jtv903","903"],"OscarMoviesBhojpuri.in@SD":["Oscar.Movies.Bhojpuri.in","OscarMoviesBhojpuri.in","143638","ts431"],"PTCChakde.in@SD":["PTC.Chak.De.in","PTC.CHAK.DE.in","PTCChakDe.in","543198","143681","ts92","LIVETV_LIVETVCHANNEL_PTC_CHAKDE","jtv1172"],"PTCMusic.in@SD":["PTC.Music.in","PTCMusic.in","543071","143682","ts922","LIVETV_LIVETVCHANNEL_PTC_MUSIC","jtv1189","1189"],"PTCPunjabi.in@SD":["PTC.Punjabi.in","PTC.PUNJABI.in","PTCPunjabi.in","543360","159123","ts122","LIVETV_LIVETVCHANNEL_PTC_PUNJABI","jtv1171"],"PTCPunjabiGold.in@SD":["PTC.Punjabi.Gold..in","PTC.Punjabi.Gold.in","PTC.PUNJABI.GOLD.in","PTCPunjabiGold.in","543031","143684","ts794","LIVETV_LIVETVCHANNEL_PTC_PUNJABI_GOLD"],"PearTV.in@SD":["PearTV.in","LIVETV_LIVETVCHANNEL_PEARS_TV"],"PeppersTV.in@SD":["Peppers.TV.in","PeppersTV.in","ts421","jtv796","6644","796"],"Pitaara.in@SD":["Pitaara.in","543026","143650","LIVETV_LIVETVCHANNEL_PITAARA","jtv946","6576","946"],"PocketFilms.in":["Pocket.Films.in","RUNNTV_LIVECHANNEL_4","jtv3259","7097","3259"],"Pogo.in@SD":["Pogo.in","POGO.in","543393","143663","ts239","LIVETV_LIVETVCHANNEL_POGO"],"PolimerTV.in@SD":["Polimer.TV.in","POLIMER.in","PolimerTV.in","543431","143665","ts272","LIVETV_LIVETVCHANNEL_POLIMER_TV","jtv705"],"Pop.uk":["0-9-9z5910525"],"PrarthanaTV.in@SD":["Prarthana.TV.in"],"PublicMovies.in@SD":["Public.Movies.in","PUBLIC.MOVIES.in","PublicMovies.in","543203","143686","ts661","LIVETV_LIVETVCHANNEL_PUBLIC_MOVIES","jtv1633"],"PublicMusic.in@SD":["Public.Music.in","PUBLIC.MUSIC.in","PublicMusic.in","543355","143687","ts424","LIVETV_LIVETVCHANNEL_PUBLIC_MUSIC","jtv773"],"PunjabiHits.in":["Punjabi.Hits.in","jtv2934","7004","2934"],"PunjabiShorts.in":["SWIFTTV_LIVECHANNEL_308","jtv3471","7128","3471"],"PuthuyugamTV.in@SD":["Puthu.Yugam.in","PUTHU.YUGAM.in","543133","143693","LIVETV_LIVETVCHANNEL_PUTHU_YUGAM","jtv824","824"],"QelloConcertsbyStingray.ca@SD":["jtv3289","3289"],"RPlusGold.in@SD":["jtv3538"],"RajDigitalPlus.in@SD":["Raj.Digital.Plus.in","RAJ.DIGITAL.PLUS.in","RajDigitalPlus.in","543042","143704","ts426","LIVETV_LIVETVCHANNEL_RAJ_DIGITAL_PLUS","jtv683"],"RajMusicTelugu.in@SD":["Raj.Music.Telugu.in","jtv737","737"],"RajMusixKannada.in@SD":["RAJ.MUSIX.KANNADA.in","RajMusixKannada.in","543078","143705","ts427","LIVETV_LIVETVCHANNEL_RAJ_MUSIX_KANNADA"],"RajMusixMalayalam.in@SD":["RAJ.MUSIX.MALAYALAM.in","543404","143706","ts541","LIVETV_LIVETVCHANNEL_RAJ_MUSIX_MALAYALAM"],"RajMusixTamil.in@SD":["RAJ.MUSIX.TAMIL.in","RAJMUSIXTAMIL.in","543499","143707","LIVETV_LIVETVCHANNEL_RAJ_MUSIX_TAMIL"],"RajMusixTelugu.in@SD":["RAJ.MUSIX.TELUGU.in","RajMusixTelugu.in","543024","143708","ts429","LIVETV_LIVETVCHANNEL_RAJ_MUSIX_TELUGU"],"RajTV.in@SD":["Raj.tv.in","Raj.TV.in","RAJ.TV.in","RajTV.in","543033","143715","ts439","LIVETV_LIVETVCHANNEL_RAJ_TV"],"Ramdhenu.in@SD":["Ramdhenu.in","RAMDHENU.in","543092","143717","ts449","LIVETV_LIVETVCHANNEL_RAMDHENU","jtv639","639"],"Rang.in@SD":["Rang.in","RANG.in","543368","143718","ts101","LIVETV_LIVETVCHANNEL_RANG","jtv623","623"],"RedBullTV.at@EUMENA":["Red.Bull.TV.in","jtv2779","2779"],"Rengoni.in@SD":["Rengoni.in","RENGONI.in","543249","181417","143722","ts214","LIVETV_LIVETVCHANNEL_RENGONI_TV","jtv635"],"RojaMovies.in@SD":["ts1868","jtv3417","3417"],"RojaTV.in":["ts1867","jtv3409","3409"],"RomedyNow.in@SD":["Romedy.Now.in","ROMEDY.NOW.in","RomedyNow.in","543123","143729","ts174","LIVETV_LIVETVCHANNEL_ROMEDY_NOW","jtv478"],"RongeenTV.in@SD":["Rongeen.TV.in"],"RupasiBangla.in@SD":["Ruposhi.Bangla.in"],"SafariTV.in@SD":["Safari.TV..in","SAFARI.TV.in","SafariTV.in","543117","143739","ts436","LIVETV_LIVETVCHANNEL_SAFARI_TV","jtv1666"],"SagaMusic.in":["Saga.Music.in","jtv2750","2750"],"SanaPlus.in@SD":["ts1284","jtv3359","3359"],"SanaTV.in@SD":["ts1285","jtv3201","7130","3201"],"SangeetBangla.in@SD":["Sangeet.Bangla.in"],"SangeetBhojpuri.in@SD":["Sangeet.Bhojpuri.in","143757","jtv741","741"],"SangeetMarathi.in@SD":["Sangeet.Marathi.in","SangeetMarathi.in","ts217","LIVETV_LIVETVCHANNEL_SANGEET_MARATHI","jtv735","735"],"ShemarooBollywood.us":["Shemaroo.Bollywood.in","jtv3075","3075"],"ShemarooJosh.in@SD":["158861","ts1269","LIVETV_LIVETVCHANNEL_CHUMBAK_TV"],"ShemarooMarathiBana.in@SD":["Shemaroo.MarathiBana.in","Shemaroo.Marathibana.in","ShemarooMarathiBana.in","543104","143777","ts800","LIVETV_LIVETVCHANNEL_SHEMAROO_MARATHIBANA","jtv1452"],"ShemarooTV.in@SD":["Shemaroo.TV.in","ShemarooTV.in","543214","143778","ts818","LIVETV_LIVETVCHANNEL_SHEMAROO_TV","jtv1961","1961"],"SidharthGold.in@SD":["Sidharth.GOLD.in","Sidharth.Gold.in","SidharthGOLD.in","143786","ts1170","LIVETV_LIVETVCHANNEL_SIDHARTH_GOLD","jtv1957","1957"],"SiriKannada.in@SD":["Siri.Kannada.in","143790","jtv1634","1634"],"SiriKannadaAllTime.in":["SIRI.KANNADA-ALL.TIME.in","SIRIKANNADAAlltime.in","543254","ts940"],"SirippoliTV.in@SD":["143791","ts611","LIVETV_LIVETVCHANNEL_SIRIPPOLI"],"SongdewTV.in@SD":["SongDew.TV.in","SONGDEW.in","543261","142920","jtv1411","598"],"Sonic.in@SD":["159124","ts127","LIVETV_LIVETVCHANNEL_SONIC","Sonic.in"],"Sony.Aath.in":["Sony.Aath.in"],"SonyBBCEarth.in@SD":["SONY.BBC.Earth.in","SONY.BBC.EARTH.in","543416","543410","143800","143799","ts158","ts460"],"SonyMax.in@SD":["Sony.Max.in","SONY.MAX.in","543269","157590","159098","ts132","ts80","LIVETV_LIVETVCHANNEL_SONY_MAX_HD"],"SonyMax2.in@SD":["Sony.MAX2.in","Sony.Max.2.in","SONY.MAX.2.in","543114","143801","ts120","LIVETV_LIVETVCHANNEL_SONY_MAX_2","jtv483"],"SonyPal.in@SD":["Sony.Pal.in","SONY.PAL.in","SonyPal.in","543324","157973","ts554","LIVETV_LIVETVCHANNEL_SONY_PAL","jtv474"],"SonyPix.in":["SONY.PIX.in","543113","543337","143803","143802","ts558","ts32","LIVETV_LIVETVCHANNEL_SONY_PIX"],"SonySAB.in@HD":["Sony.SAB.in","SONY.SAB.in","SONYSAB.in","543101","159099","159125","ts48","ts559"],"SonySportsTen1.in":["Sony.Sports.Ten.1.in","SONY.SPORTS.TEN.1.in","SonySportsTEN1.in","jtv162","jtv514","514","162"],"SonySportsTen2.in":["Sony.Sports.Ten.2.in","SONY.SPORTS.TEN.2.in","SonySportsTEN2.in","jtv891","891"],"SonySportsTen3.in":["Sony.Sports.Ten.3.HD.in","SONY.SPORTS.TEN.3.in","SonySportsTEN3.in","543206","543295"],"SonySportsTen4.in":["Sony.Sports.Ten.4.HD.in","SonySportsTEN4.in"],"SonySportsTen5.in":["Sony.Sports.Ten.5.in","SONY.SPORTS.TEN.5.in","SONYSPORTSTEN5.in","543505","543047","159129","157593","ts35"],"SonyWah.in@SD":["Sony.Wah.in","SONY.WAH.in","543352","157974","ts56","LIVETV_LIVETVCHANNEL_SONY_WAH","jtv1393","1393"],"SonyYay.in@SD":["SONY.YAY!.in","Sony.yay.in","543317","159100","ts45","LIVETV_LIVETVCHANNEL_SONY_YAY","Sony.YAY!.in","3507"],"Spondon.in@SD":["Spondon.in","143806","jtv2435","2435"],"Star.Jalsha.Movies.in":["Star.Jalsha.Movies.in"],"Star.Jalsha.in":["Star.Jalsha.in"],"StarBharat.in":["Star.Bharat.in","STAR.BHARAT.in","STARBHARAT.in","543115","543501","159130","159101","ts244"],"StarGold.in@HD":["Star.Gold.in","STAR.GOLD.in","543055","143815","159131","ts632","LIVETV_LIVETVCHANNEL_STAR_GOLD_HD","LIVETV_LIVETVCHANNEL_STAR_GOLD"],"StarGoldSelect.in@SD":["Star.Gold.Select.in","STAR.GOLD.SELECT.in","StarGoldSelect.in","543216","543074","143817","143816","LIVETV_LIVETVCHANNEL_STAR_GOLD_SELECT_HD"],"StarGoldThrills.in@SD":["Star.Gold.Thrills.in","STAR.GOLD.THRILLS.in","543460","158822","LIVETV_LIVETVCHANNEL_STAR_GOLD_THRILLS","jtv3098","3098"],"StarMaa.in@SD":["STAR.MAA.in","STARMAA.in","543246","543459","179620","143821","ts956","jtv1138"],"StarMaaMovies.in@SD":["Star.Maa.Movies.in","STAR.MAA.MOVIES.in","543492","543235","143826","143825","ts957","LIVETV_LIVETVCHANNEL_STAR_MAA_MOVIES_HD"],"StarMoviesSelect.in@HD":["Star.Movies.Select.HD.in","STAR.MOVIES.SELECT.in","543313","543316","143830","158863","LIVETV_LIVETVCHANNEL_STAR_MOVIES_SELECT_HD","LIVETV_LIVETVCHANNEL_STAR_MOVIES_SELECT"],"StarPlus.in@SD":["Star.Plus.in","STAR.PLUS.in","STARPLUS.in","543093","543164","143832","143831","ts8"],"StarPravah.in@HD":["Star.Pravah.in","STAR.PRAVAH.in","543054","143834","143833","ts469","LIVETV_LIVETVCHANNEL_STAR_PRAVAH","LIVETV_LIVETVCHANNEL_STAR_PRAVAH_HD"],"StarSports1.in@HD":["Star.Sports.1.in","STAR.SPORTS.1.in","StarSports1.in","543006","543489","143837","143835","ts78"],"StarSports1Hindi.in@HD":["STAR.SPORTS.1.HINDI.in","StarSports1Hindi.in","543275","543058","143839","143838","ts24","jtv1108"],"StarSports3.in@SD":["STAR.SPORTS.3.in","StarSports3.in","543366","143846","LIVETV_LIVETVCHANNEL_STAR_SPORTS_3","jtv1389"],"StarSportsSelect1.in@SD":["Star.Sports.Select.1.in","StarSportsSelect1.in","543120","543263","143848","143849","ts246","LIVETV_LIVETVCHANNEL_STAR_SPORTS_SELECT_1"],"StarSportsSelect2.in@SD":["Star.Sports.Select.2.in","STAR.SPORTS.SELECT.2.in","StarSportsSelect2.in","543061","543450","143850","143851","LIVETV_LIVETVCHANNEL_STAR_SPORTS_SELECT_2_HD"],"StarSuvarnaPlus.in@SD":["STAR.SUVARNA.PLUS.in","543423","143854","ts540","LIVETV_LIVETVCHANNEL_STAR_SUVARNA_PLUS","Star.Suvarna.Plus.in"],"SteelbirdMusic.in@SD":["Steelbird.Music.in"],"StingrayDJAZZ.ca@SD":["jtv3290","3290"],"StingrayNaturescape.ca":["jtv3285","3285"],"StingrayTheSpa.ca":["jtv3323","3323"],"StudioOnePlus.in@SD":["Studio.One.in","jtv1274","1274"],"StudioYuva.in":["jtv1799","7107","1799"],"SubinTV.in@SD":["ts1385","jtv3360","3360"],"SunMusic.in@SD":["Sun.Music.HD.in","SUN.MUSIC.in","543232","543454","145427","143876","LIVETV_LIVETVCHANNEL_SUN_MUSIC","LIVETV_LIVETVCHANNEL_SUN_MUSIC_HD"],"SuperHungama.in@SD":["Super.Hungama.in","SUPER.HUNGAMA.in","543103","143883","LIVETV_LIVETVCHANNEL_SUPER_HUNGAMA","jtv1392","1392"],"SuriyaTV.in":["jtv3394","3394"],"SuriyanTV.in@SD":["ts1384"],"TLC.in@HD":["TLC.HD.in","TLC.in","543386","543128","123500","158023","ts135","ts480"],"TabbarHits.in":["Tabbar.Hits.in","143292","jtv2778","7005","2778"],"TamilanTV.in":["jtv2958","2958"],"TarangMusic.in@SD":["TARANG.MUSIC.in","543280","143926","LIVETV_LIVETVCHANNEL_TARANG_MUSIC","jtv751","751"],"TeluguOne.in@HD":["teluguone.tv.in","jtv3594","7132","3594"],"ThalaaTV.in":["6601"],"ThanthiOne.in":["Thanthi.One.in","THANTHI.ONE.in","jtv3059","3059"],"TheJungleBook.in":["SWIFTTV_LIVECHANNEL_79"],"TinyPop.uk":["0-9-9z5910526"],"TollyTV.in":["6613"],"Travelxp.in@SD":["Travelxp.HD.Hindi.in","Travelxp.in","jtv562","562"],"UBangla.in":["U.Bangla.in"],"UltimateTV.in@SD":["jtv3396","3396"],"VaanavilTV.in@SD":["Vaanavil.TV.in","jtv971","971"],"VanithaTV.in@SD":["Vanitha.in","ts1135","jtv775","227","775"],"VasanthTV.in@SD":["Vasanth.TV.in","VASANTH.TV.in","VasanthTV.in","543287","144068","ts499","LIVETV_LIVETVCHANNEL_VASANTH_TV","jtv727"],"VendharTV.in@SD":["Vendhar.TV.in","VendharTV.in","ts659","jtv857","857"],"VissaTV.in@SD":["Vissa.TV.in","VISSA.TV.in","VissaTV.in","543439","144081","ts585","LIVETV_LIVETVCHANNEL_VISSA_TV","jtv734"],"WildEarth.za":["Wild.Earth.in","jtv2437","2437"],"YRFMusic.in":["YRF.Music.in","jtv2753","2753"],"ZBMusic.in@HD":["jtv3319"],"Zee24Ghanta.in@SD":["Zee.24.Ghanta.in"],"ZeeAction.in":["ZEE.ACTION.in","543243","jtv488","0-9-zeeaction","488"],"ZeeBangla.in@HD":["Zee.Bangla.in"],"ZeeBanglaSonar.in@SD":["144437"],"ZeeBollywood.in@SD":["Zee.Bollywood.in","ZEE.Bollywood.in","ZeeBollywood.in","543294","144438","ts175","LIVETV_LIVETVCHANNEL_ZEE_BOLLYWOOD","jtv487"],"ZeeCinema.in@HD":["Zee.Cinema.in","ZEE.CINEMA.in","ZeeCinema.in","543084","543330","144443","159104","ts503"],"ZeeKannada.in@SD":["Zee.Kannada.in","ZEE.KANNADA.in","ZeeKannada.in","543097","543064","144452","144451","ts675"],"ZeeTV.in@SD":["Zee.TV.in","ZEE.TV.in","ZeeTV.in","543105","543086","144478","144479","ts63"],"ZeeTalkies.in@HD":["Zee.Talkies.in","ZEE.TALKIES.in","ZeeTalkies.in","543200","543068","144469","144468","ts249"],"ZeeTamil.in@SD":["Zee.Tamil.in","ZEE.TAMIL.in","ZeeTamil.in","543143","543165","144471","144470","ts257"],"Zing.in@SD":["ZING.in","Zing.in","543208","144484","142988","ts517","LIVETV_LIVETVCHANNEL_ZING","jtv585"],"custom.asianet":["Asianet.in","ASIANET.HD.in","ASIANET.in","543306","543223","142668","142673","ts292"],"custom.colors.infinity":["Colors.Infinity.SD.in","Colors.Infinity.HD.in","Colors.Infinity.in","COLORS.INFINITY.HD.in","COLORS.INFINITY..in","ColorsInfinity.in","543156","543190"],"custom.discovery.science":["Discovery.Science.in","DiscoveryScience.in","543364","159107","ts113","LIVETV_LIVETVCHANNEL_DISCOVERY_SCIENCE"],"custom.discovery.turbo":["Discovery.Turbo.in","DiscoveryTurbo.in","543148","159108","ts228","LIVETV_LIVETVCHANNEL_DISCOVERY_TURBO","jtv541","541"],"custom.duck.tv":["jtv3537","3537"],"custom.ekamra.cinema":["Ekamra.Cinema.in"],"custom.ekamra.manoranjan":["Ekamra.Manoranjan.in","ts1207"],"custom.ekamra.musiq":["Ekamra.Musiq.in"],"custom.enter10.bangla":["ENTER10.BANGLA.in","543030"],"custom.history.tv":["HISTORY.CHANNEL.in","543138"],"custom.kolkatatv":["Kolkata.TV.in"],"custom.mtv":["MTV.HD.in","MTV.in","543480","159093","143558","ts103","ts406","LIVETV_LIVETVCHANNEL_MTV"],"custom.solntse":["&TV.HD.in","and.TV.in","andtv.in","142640","142641","ts578","ts40","LIVETV_LIVETVCHANNEL_SYMANDTV"],"custom.sonic.bangla":["Sonic.Bangla.in","jtv1345","1345"],"custom.sony.ten.5":["Sony.Ten.5.HD.in","Sony.Ten.5.in","jtv155","jtv525","155","525"],"custom.star.vijay":["Star.Vijay.HD.in","144079","144075","ts496","LIVETV_LIVETVCHANNEL_VIJAY_HD","LIVETV_LIVETVCHANNEL_STAR_VIJAY","jtv1130","jtv368"],"custom.starsports2":["Star.Sports.2.HD.in","STAR.SPORTS.2.in","STAR.SPORTS.2.HD.in","StarSports2.in","543210","543498","143844","143845"],"custom.taratv":["Tara.TV.in"],"new.zee.anmol":["Zee.Anmol.in","ZEE.ANMOL.in","543429"],"new.zee.cafe":["Zee.Cafe.HD.in","ZEE.CAFE.HD.in","ZEE.CAFE.in","543151","543237","jtv1319","jtv1364","1319"],"staging.assam.talks":["Assam.Talks.in","142683","ts1484","LIVETV_LIVETVCHANNEL_ASSAM_TALKS","jtv675","675"],"staging.dhinchaak":["ALL.Time.MOVIES.in","ALLTimeMOVIES.in","160750","ts1321","RUNNTV_LIVECHANNEL_128"]};




























































































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
function normalizeGroup(value){return String(value??"").normalize("NFKC").replace(/[\u00A0\u2000-\u200B\u202F\u205F\u3000]/g," ").replace(/\s+/g," ").trim();}
function groupKey(value){return normalizeGroup(value).toLocaleLowerCase();}
function parsePlaylist(text, includeBackup = false) {
  const lines=text.split(/\r?\n/); let categoryNames=[];
  const header=lines.find(x=>x.startsWith("#PLAYLIST-STUDIO-CATEGORIES:"));
  if(header) { try { categoryNames=JSON.parse(header.slice(header.indexOf(":")+1)); } catch {} }
  const entries=[];
  for(let i=0;i<lines.length;i++){
    if(!lines[i].startsWith("#EXTINF:")) continue;
    const ext=lines[i], comma=ext.lastIndexOf(","); if(comma<0 || i+1>=lines.length) continue;
    const a=parseAttrs(ext), name=ext.slice(comma+1).trim(), url=lines[i+1].trim();
    if(!name || !url || url.startsWith("#")) continue;
    const rawGroup=normalizeGroup(a["group-title"] || "Uncategorized"); const group=rawGroup || "Uncategorized"; if([...(includeBackup ? [] : ["backup"]), "new channels", "new backup", "not playing", "test"].includes(groupKey(group))) continue; const tvgId=a["tvg-id"] || "", tvgName=a["tvg-name"] || name, logo=a["tvg-logo"] || "";
    entries.push({ id:stableId(tvgId+"|"+name+"|"+group+"|"+url), name, tvgId, tvgName, logo, group, channelNo:a["tvg-chno"]||"", url });
    i++;
  }
  const groups=[];
  for(const g of categoryNames){ const clean=normalizeGroup(g); if(clean && ![...(includeBackup ? [] : ["backup"]), "new channels", "new backup", "not playing","test"].includes(groupKey(clean)) && !groups.some(x=>groupKey(x)===groupKey(clean))) groups.push(clean); }
  for(const e of entries){ const match=groups.find(g=>groupKey(g)===groupKey(e.group)); if(match) e.group=match; else if(e.group && ![...(includeBackup ? [] : ["backup"]), "new channels", "new backup", "not playing","test"].includes(groupKey(e.group))) groups.push(e.group); }
  const categoryId=new Map(groups.map((g,i)=>[groupKey(g),String(i+1)]));
  for(const e of entries) e.categoryId=categoryId.get(groupKey(e.group))||"0";
  return {entries,groups};
}
async function getPlaylist(playlistEnv){
  const cache=caches.default, key=new Request(CACHE_KEY + "|" + (playlistEnv.PLAYLIST_URL||DEFAULT_PLAYLIST_URL)), cached=await cache.match(key); if(cached) return cached.text();
  const r=await fetch(playlistEnv.PLAYLIST_URL||DEFAULT_PLAYLIST_URL,{headers:{"user-agent":"BDIX-IPTV-Xtream-Gateway/1.0"}});
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
  // XMLTV timestamps may carry an explicit timezone offset, e.g.
  // "20261005124600 +0530". Parse that offset instead of treating the
  // clock fields as UTC; Xtream now_playing/start_timestamp otherwise drift
  // by the timezone amount and can highlight an old programme as current.
  const m=/^(\d{4})(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})(?:\s*([+-])(\d{2})(\d{2}))?/.exec(String(s||"").trim());
  if(!m) return 0;
  const base=Date.UTC(+m[1],+m[2]-1,+m[3],+m[4],+m[5],+m[6]);
  if(!m[7]) return Math.floor(base/1000);
  const offsetMinutes=(+m[8]*60)+(+m[9]);
  const offsetMs=offsetMinutes*60*1000*(m[7]==="+"?1:-1);
  return Math.floor((base-offsetMs)/1000);
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

function categories(data){const seen=new Set(),out=[];for(const name of data.groups){const clean=normalizeGroup(name),key=groupKey(clean);if(!key||seen.has(key))continue;seen.add(key);out.push({category_id:String(out.length+1),category_name:clean,parent_id:0});}return out;}
function streams(data,cat){
  let src=data.entries;
  if(cat){
    const requested=String(cat);
    const requestedIndex=Number(requested);
    const requestedGroup=(Number.isInteger(requestedIndex)&&requestedIndex>0)?data.groups[requestedIndex-1]:"";
    src=data.entries.filter(e =>
      e.categoryId===requested ||
      (requestedGroup && groupKey(e.group)===groupKey(requestedGroup))
    );
  }
  return src.map((e,i)=>({
    num:Number(e.channelNo)||i+1,
    name:e.name,
    stream_type:"live",
    stream_id:e.id,
    stream_icon:e.logo,
    epg_channel_id:(e.tvgId||e.name),
    added:"0",
    category_id:e.categoryId,
    custom_sid:"",
    tv_archive:0,
    direct_source:e.url,
    tv_archive_duration:0
  }));
}
function m3u(data,request,env){
  const u=new URL(request.url), base=u.pathname==="/bdix"||u.pathname.startsWith("/bdix/")?"/bdix":"", ext=(u.searchParams.get("output")||"m3u8").toLowerCase()==="ts"?"ts":"m3u8", epgUrl=u.origin+base+"/xmltv-public.php", out=[`#EXTM3U url-tvg="${epgUrl}" x-tvg-url="${epgUrl}"`];
  for(const e of data.entries){
    const attrs=[`tvg-id="${e.tvgId}"`,`tvg-name="${e.tvgName}"`,`tvg-logo="${e.logo}"`,`channel-id="${e.tvgId||e.name}#${e.id}"`,`group-title="${e.group}"`];
    if(e.channelNo) attrs.push(`tvg-chno="${e.channelNo}"`);
    out.push("#EXTINF:-1 "+attrs.join(" ")+","+e.name);
    out.push(u.origin+base+"/live/"+env.XTREAM_USERNAME+"/"+env.XTREAM_PASSWORD+"/"+e.id+"."+ext);
  }
  return new Response(out.join("\n")+"\n",{headers:{"content-type":"audio/x-mpegurl; charset=utf-8","cache-control":"no-store"}});
}
function emptyEpg(){return new Response('<?xml version="1.0" encoding="UTF-8"?><tv generator-info-name="BDIX-IPTV Xtream Gateway"></tv>',{headers:{"content-type":"application/xml; charset=utf-8","cache-control":"no-store"}});}
export default {
 async fetch(request,env){
  try{
   if(!env.XTREAM_USERNAME||!env.XTREAM_PASSWORD) return json({error:"Xtream credentials are not configured."},500);
   const url=new URL(request.url), rawPath=url.pathname, isBdix=rawPath==="/bdix"||rawPath.startsWith("/bdix/"), path=isBdix?(rawPath.slice(5)||"/"):rawPath;
   const playlistEnv=isBdix?{...env,PLAYLIST_URL:env.BDIX_PLAYLIST_URL||DEFAULT_BDIX_PLAYLIST_URL}:env;
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
    const data=parsePlaylist(await getPlaylist(playlistEnv), !isBdix), epg=parseXmltv(await getEpg(env));
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
    const action=url.searchParams.get("action")||"", data=parsePlaylist(await getPlaylist(playlistEnv), !isBdix);
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
   if(path==="/get.php"){if(!auth(url,env)) return new Response("Unauthorized",{status:401}); return m3u(parsePlaylist(await getPlaylist(playlistEnv), !isBdix),request,env);}
   if(path==="/xmltv-public.php"){
    const data=parsePlaylist(await getPlaylist(playlistEnv), !isBdix), epg=parseXmltv(await getEpg(env));
    return new Response(epgXml(data,epg),{headers:{"content-type":"application/xml; charset=utf-8","cache-control":"public, max-age=900"}});
   }
   if(path==="/xmltv.php"){
    if(!auth(url,env)) return new Response("Unauthorized",{status:401});
    const data=parsePlaylist(await getPlaylist(playlistEnv), !isBdix), epg=parseXmltv(await getEpg(env));
    return new Response(epgXml(data,epg),{headers:{"content-type":"application/xml; charset=utf-8","cache-control":"no-store"}});
   }
   if(path.startsWith("/live/")){
    const parts=path.split("/").filter(Boolean); if(!pathAuth(parts,env)) return new Response("Unauthorized",{status:401});
    const id=Number((parts[3]||"").split(".")[0]); if(!Number.isInteger(id)) return new Response("Bad stream ID",{status:400});
    const data=parsePlaylist(await getPlaylist(playlistEnv), !isBdix), stream=data.entries.find(e=>e.id===id);
    if(!stream) return new Response("Stream not found",{status:404});
    return Response.redirect(stream.url,302);
   }
   return new Response("Not found",{status:404});
  }catch(e){return json({error:String(e?.message||e)},500);}
 }
};
