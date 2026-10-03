const DEFAULT_PLAYLIST_URL = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u";
const CACHE_KEY = "https://bdix-iptv.internal/playlist";
const CACHE_TTL = 60;

const EPG_URLS = [
  // IN1 is the broad India guide. IN4 is a smaller complementary India guide
  // with additional regional/channel IDs. Keep the live set to these two to
  // avoid the memory pressure caused by the much larger ALL_SOURCES feed.
  "https://epgshare01.online/epgshare01/epg_ripper_IN1.xml.gz",
  "https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz",
  "https://iptv-epg.org/files/epg-in.xml",
  "https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz"
];
const EPG_CACHE_KEY = "https://bdix-iptv.internal/epg-xml-v10";
const EPG_CACHE_TTL = 900;
// Direct M3U EPG endpoint deployment trigger. v10: IN1 + complementary IN4.

// Cross-map playlist tvg-id variants to canonical EPG IDs used by public guides.
const EPG_ID_MAP = {"7SMusic.in@SD":["7S.MUSIC.in"],"7XMusic.in@SD":["7X.Music.in"],"9XJalwa.in":["9X.Jalwa.in","9XJalwa.in","407811"],"9XJhakaas.in@SD":["9x.Jhakaas.in","9X.JHAKAAS.in","543161"],"9XM.in@SD":["9XM.in","543367"],"9XTashan.in@SD":["9X.Tashan.in","9X.TASHAN.in","9XTashan.in","543036"],"AakaashAath.in@SD":["AakaashAath.in"],"AamarBangla.in":["Amar.Bangla.TV.in"],"AlankarTV.in@SD":["Alankar.TV.in","ALANKAR.in","543118"],"AllTimeMovies.in@SD":["ALL.Time.MOVIES.in","ALLTimeMOVIES.in"],"AmritaTV.in@SD":["Amrita.TV.in","AMRITA.in","AmritaTV.in","543102"],"AnandTV.in@SD":["Anand.TV.in"],"AndPictures.in@SD":["And.Pictures.in","and.PICTURES.in","AndPictures.in"],"AndTV.in@SD":["&TV.HD.in","and.TV.in","andtv.in"],"AndpriveHD.in":["And.Prive.HD.in","and.PRIVE.HD.in"],"AndxplorHD.in":["&Xplor.HD.in","and.xplorHD.in"],"AnimalPlanet.in@SD":["Animal.Planet.HD.in","ANIMAL.PLANET.in","AnimalPlanet.in","543099"],"AsianetMovies.in@SD":["Asianet.Movies.HD.in","ASIANET.MOVIES.in","AsianetMovies.in","543022","543281"],"B4UBhojpuri.in@SD":["B4U.Bhojpuri.in","B4UBhojpuri.in"],"B4UKadak.in@SD":["B4U.Kadak.in","B4U.KADAK.in","B4UKadak.in","543225"],"B4UMovies.in@India":["B4U.Movies.in","B4UMovies.in","543309"],"B4UMusic.in@India":["B4U.Music.in","B4U.MUSIC.in","B4UMusic.in","543038"],"BHI.Channel.in":["BHI.Channel.in"],"BSTV.pk@SD":["BSTV.in"],"BalleBalle.in@SD":["Balle.Balle.TV.in","BALLE.BALLE.in","543327"],"BhojpuriCinema.in@SD":["Bhojpuri.Cinema.in","BHOJPURI.CINEMA.in","BhojpuriCinema.in","543361"],"CartoonNetwork.uk":["Cartoon.Network.HD+.in","Cartoon.Network.in","CARTOON.NETWORK.in","CartoonNetwork+.in","CartoonNetwork.in","543449"],"Colors.Bangla.in":["Colors.Bangla.in","COLORS.BANGLA.in","COLORSBANGLA.in","543370","543469"],"ColorsBanglaCinema.in@SD":["Colors.Bangla.Cinema.in","COLORS.BANGLA.CINEMA.in","543218"],"ColorsCineplex.in@SD":["Colors.Cineplex.in","COLORS.CINEPLEX.in","543298"],"ColorsCineplexBollywood.in@SD":["Colors.Cineplex.Bollywood.in"],"ColorsCineplexSuperhits.in@SD":["Colors.Cineplex.Superhits.in","COLORS.CINEPLEX.SUPERHITS.in","543230"],"ColorsGujarati.in@SD":["Colors.Gujarati.in","COLORS.GUJARATI.in","543314"],"ColorsGujaratiCinema.in@SD":["Colors.Gujarati.Cinema.in","COLORS.GUJARATI.CINEMA.in","543362"],"ColorsKannada.in@SD":["Colors.Kannada.SD.in","Colors.Kannada.HD.in","COLORS.KANNADA.in","COLORSKANNADA.in","543329","543147"],"ColorsKannadaCinema.in@SD":["Colors.Kannada.Cinema.in"],"ColorsMarathi.in@SD":["Colors.Marathi.HD.in","Colors.Marathi.SD.in","COLORS.MARATHI.in","COLORSMARATHI.in","543065","543277"],"ColorsRishteyAmericas.in":["Colors.Rishtey.in","COLORS.RISHTEY.in","ColorsRishtey.in","543236"],"ColorsSuper.in":["Colors.Super.in","COLORS.SUPER.in","543284"],"ColorsTamil.in@SD":["Colors.Tamil.in","COLORSTAMIL.in","543334","543302"],"DDArunPrabha.in@SD":["DD.Arunprabha.in","DD.ARUN.PRABHA.in","543094"],"DDBangla.in@SD":["DD.Bangla.in","543434"],"DDBharati.in@SD":["DD.bharati.in"],"DDChandana.in@SD":["DD.Chandana.in","DDChandana.in","543175"],"DDGirnar.in@SD":["DD.Girnar.in","DD.GIRNAR.in","DDGirnar.in","543062"],"DDKashir.in@SD":["DD.Kashir.in","543500"],"DDMadhyaPradesh.in@SD":["DD.Madhya.Pradesh.in","DDMadhyaPradesh.in"],"DDMalayalam.in@SD":["DD.Malayalam.in","DD.MALAYALAM.in","DDMalayalam.in","543259"],"DDNational.in@SD":["DD.National.in","DDNational.in","543184"],"DDOdia.in@SD":["DD.ODIA.in","DDOdia.in","543028"],"DDPunjabi.in@SD":["DD.Punjabi.in","DD.PUNJABI.in","DDPunjabi.in","543437"],"DDSahyadri.in@SD":["DD.SAHYADRI.in","DDSahyadri.in","543462"],"DDSaptagiri.in@SD":["DD.Saptagiri.in","DDSaptagiri.in","543376"],"DDSports.in@SD":["DD.Sports.in","DDSports.in","543389"],"DDTamil.in@SD":["DD.TAMIL.in","DDTamil.in","543273"],"DDTripura.in@SD":["DDTripura.in@SD"],"DDUrdu.in@SD":["DD.urdu.in","DD.URDU.in","543021"],"Dangal2.in@SD":["Dangal.2.in","Dangal2.in","543069"],"DangalTV.in@SD":["Dangal.in","DANGAL.in","543037"],"DarshanaTV.in@SD":["DARSHANA.in","543481"],"DesiChannel.in":["Desi.Channel.in"],"DhoomMusic.in@SD":["Dhoom.Music.Bangla.in","DHOOM.MUSIC.in"],"DiscoveryChannel.in@SD":["Discovery.in","DISCOVERY.CHANNEL.in","543256"],"DiscoveryKids.au":["Discovery.Kids.in","DISCOVERY.KIDS.in","DiscoveryKids.in","543485"],"DisneyChannel.in@HD":["DISNEY.CHANNEL.in"],"E24.in":["E.24.in"],"ETVBalBharat.in@SD":["ETV.BAL.BHARAT.in","543412"],"ETVCinema.in":["ETV.Cinema.in","ETV.CINEMA.in","ETVCinema.in","543267"],"EkamraBharatOdia.in@SD":["Ekamra.Bharat.Odia.in"],"Enterr10Bangla.in@SD":["ENTER10.BANGLA.in","Enterr10Bangla.in","543030"],"ExpressNews.in@SD":["Express.News.in"],"FaktMarathi.in@SD":["Fakt.Marathi.in","FAKT.MARATHI.in","FaktMarathi.in","543453"],"FoodFood.in@SD":["Food.Food.in","FoodFood.in"],"Gangaur.in@SD":["Gangaur.in"],"Goldmines.in@SD":["Goldmines.in"],"GoldminesBollywood.in@SD":["Goldmines.Bollywood.in"],"GoldminesMovies.in@SD":["Goldmines.Movies.in"],"HMTV.in@SD":["HM.TV.in","HMTV.in"],"History.us":["HISTORY.CHANNEL.in","543138"],"HistoryTV18.in@SD":["History.TV18.SD.in","History.TV18.HD.in","HISTORY.TV18.HD.in","543336"],"Hungama.in@SD":["Hungama.in","HUNGAMA.in","543181"],"Insync.in":["Insync.in"],"InvestigationDiscovery.in@SD":["Investigation.Discovery.in","InvestigationDiscovery.in","543196"],"IsaiAruvi.in@SD":["ISAI.ARUVI.in","Isaiaruvi.in","543163"],"KairaliTV.in@SD":["Kairali.TV.in","KAIRALI.in","543357"],"KairaliWe.in@SD":["Kairali.WE.TV.in"],"KalaignarMurasu.in":["MURASU.in"],"KalaignarTV.in@SD":["Kalaignar.TV.in","KALAIGNAR.in","KalaignarTV.in","543395"],"KappaTV.in@SD":["Kappa.TV.in"],"KhushbooBangla.in@SD":["KhushbooBangla.in"],"MKSix.in":["MK.Six.in"],"MNX.in@SD":["MNX.in","543194"],"MONTVBangla.in":["Mon.TV.Bangla.in"],"MadhimugamTV.in":["Madhimugam.TV.in"],"MahaaMax.in":["Mahaa.Max.in"],"ManoranjanGrand.in@SD":["Manoranjan.Grand.in"],"Mastiii.in@SD":["Mastiii.in"],"MazhavilManorama.in@SD":["Mazhavil.Manorama.in","MAZHAVIL.MANORAMA.in","MAZHAVILMANORAMA.in","543130","543345"],"Mh1Music.in@SD":["mh1.(Music).in"],"MoviesNow.in@SD":["Movies.Now.in","MOVIES.NOW.in","MoviesNow.in","543174"],"MoviesNowPlus.in@SD":["MN+.HD.in","543209"],"MusicIndia.in@SD":["Music.India.in"],"NKTVBangla.bd":["NK.TV.Bangla.in"],"NTV.bd":["NTV.in","543153"],"NationalGeographic.in@SD":["National.Geographic.HD.in","NATIONAL.GEOGRAPHIC.in","543180","543108"],"NationalGeographicWild.in@SD":["Nat.Geo.Wild.HD.in","NAT.GEO.WILD.in","NAT.GEO.WILD.HD.in","NatGeoWild.in","543356","543052"],"Nazara.in@SD":["NAZARA.in"],"News24.bd":["News.24.in","NEWS.24.in","News24.in","543354"],"NickJr.in@SD":["Nick.Jr.in","NICK.JR.in","543502"],"Nickelodeon.in@SD":["Nick.HD+.in","Nick.in","NICK.in","NICK.HD+.in","543260","543090"],"OnePaschima.in@SD":["One.Paschima.in"],"Only.Music.in":["Only.Music.in"],"OscarMoviesBhojpuri.in@SD":["Oscar.Movies.Bhojpuri.in","OscarMoviesBhojpuri.in"],"PTCChakde.in@SD":["PTC.Chak.De.in","PTC.CHAK.DE.in","PTCChakDe.in","543198"],"PTCMusic.in@SD":["PTC.Music.in","PTCMusic.in","543071"],"PTCPunjabi.in@SD":["PTC.Punjabi.in","PTC.PUNJABI.in","PTCPunjabi.in","543360"],"PTCPunjabiGold.in@SD":["PTC.Punjabi.Gold..in","PTC.Punjabi.Gold.in","PTC.PUNJABI.GOLD.in","PTCPunjabiGold.in","543031"],"PeppersTV.in@SD":["Peppers.TV.in","PeppersTV.in"],"Pitaara.in@SD":["Pitaara.in","543026"],"PocketFilms.in":["Pocket.Films.in"],"Pogo.in@SD":["Pogo.in","POGO.in","543393"],"PolimerTV.in@SD":["Polimer.TV.in","POLIMER.in","PolimerTV.in","543431"],"PublicMovies.in@SD":["Public.Movies.in","PUBLIC.MOVIES.in","PublicMovies.in","543203"],"PublicMusic.in@SD":["Public.Music.in","PUBLIC.MUSIC.in","PublicMusic.in","543355"],"PunjabiHits.in":["Punjabi.Hits.in"],"PuthuyugamTV.in@SD":["Puthu.Yugam.in","PUTHU.YUGAM.in","543133"],"RSBharat.in@SD":["RS.Bharat.in"],"RajDigitalPlus.in@SD":["Raj.Digital.Plus.in","RAJ.DIGITAL.PLUS.in","RajDigitalPlus.in","543042"],"RajMusicTelugu.in@SD":["Raj.Music.Telugu.in"],"RajMusixKannada.in@SD":["RAJ.MUSIX.KANNADA.in","RajMusixKannada.in","543078"],"RajMusixMalayalam.in@SD":["RAJ.MUSIX.MALAYALAM.in","543404"],"RajMusixTamil.in@SD":["RAJ.MUSIX.TAMIL.in","RAJMUSIXTAMIL.in","543499"],"RajMusixTelugu.in@SD":["RAJ.MUSIX.TELUGU.in","RajMusixTelugu.in","543024"],"RajTV.in@SD":["Raj.tv.in","Raj.TV.in","RAJ.TV.in","RajTV.in","543033"],"Ramdhenu.in@SD":["Ramdhenu.in","RAMDHENU.in","543092"],"RedBullTV.at@EUMENA":["Red.Bull.TV.in"],"RomedyNow.in@SD":["Romedy.Now.in","ROMEDY.NOW.in","RomedyNow.in","543123"],"RongeenTV.in@SD":["Rongeen.TV.in","RongeenTV.in"],"RupashiBanglaTV.bd@SD":["Rupashi.Bangla.in"],"RupasiBangla.in@SD":["Ruposhi.Bangla.in","RUPASI.BANGLA.in","RuposhiBangla.in"],"SafariTV.in@SD":["Safari.TV..in","SAFARI.TV.in","SafariTV.in","543117"],"SangeetBangla.in@SD":["Sangeet.Bangla.in","SANGEET.BANGLA.in","SangeetBangla.in","543268"],"SangeetBhojpuri.in@SD":["Sangeet.Bhojpuri.in"],"SangeetMarathi.in@SD":["Sangeet.Marathi.in","SangeetMarathi.in"],"ShemarooBollywood.us":["Shemaroo.Bollywood.in"],"ShemarooTV.in@SD":["Shemaroo.TV.in","ShemarooTV.in","543214"],"SidharthGold.in@SD":["Sidharth.GOLD.in","Sidharth.Gold.in","SidharthGOLD.in"],"SiriKannada.in@SD":["Siri.Kannada.in"],"SiriKannadaAllTime.in":["SIRI.KANNADA-ALL.TIME.in","SIRIKANNADAAlltime.in","543254"],"SongdewTV.in@SD":["SongDew.TV.in","SONGDEW.in","543261"],"Sony.Aath.in":["Sony.Aath.in","SONY.AATH.in","SONYAATH.in","543401"],"SonyBBCEarth.in@SD":["SONY.BBC.Earth.in","SONY.BBC.EARTH.in","543410","543416"],"SonyEntertainmentTelevision.in@SD":["Sony.Entertainment.Television.in"],"SonyMax.in@SD":["Sony.Max.in","SONY.MAX.in","543269"],"SonyMax2.in@SD":["Sony.MAX2.in","Sony.Max.2.in","SONY.MAX.2.in","543114"],"SonyPix.in":["SONY.PIX.in","543113","543337"],"SonySAB.in@HD":["Sony.SAB.in","SONY.SAB.in","SONYSAB.in","543101"],"SonySportsTen3.in":["Sony.Sports.Ten.3.HD.in","SONY.SPORTS.TEN.3.in","SonySportsTEN3.in","543206","543295"],"SonySportsTen4.in":["Sony.Sports.Ten.4.HD.in","SonySportsTEN4.in"],"SonySportsTen5.in":["Sony.Sports.Ten.5.in","SONY.SPORTS.TEN.5.in","SONYSPORTSTEN5.in","543505","543047"],"SonyYay.in@SD":["SONY.YAY!.in","Sony.yay.in","543317"],"Star.Jalsha.Movies.in":["Star.Jalsha.Movies.in","JALSHA.MOVIES.HD.in","JALSHA.MOVIES.in","543072","543369"],"Star.Jalsha.in":["Star.Jalsha.in","STAR.JALSHA.in","STARJALSHA.in","543407","542998"],"StarBharat.in":["Star.Bharat.in","STAR.BHARAT.in","STARBHARAT.in","543115","543501"],"StarGold.in@HD":["Star.Gold.in","STAR.GOLD.in","543292","543055"],"StarGold2.in@SD":["Star.Gold.2.in","543348"],"StarGoldSelect.in@SD":["Star.Gold.Select.in","STAR.GOLD.SELECT.in","StarGoldSelect.in","543216","543074"],"StarGoldThrills.in@SD":["Star.Gold.Thrills.in","STAR.GOLD.THRILLS.in","543460"],"StarMaa.in@SD":["STAR.MAA.in","STARMAA.in","543246","543459"],"StarMaaMovies.in@SD":["Star.Maa.Movies.in","STAR.MAA.MOVIES.in","543492","543235"],"StarMaaMusic.in@SD":["STAR.MAA.MUSIC.in","543192"],"StarMovies.in@SD":["Star.Movies.in","STAR.MOVIES.in","543176","543187"],"StarMoviesSelect.in@HD":["Star.Movies.Select.HD.in","STAR.MOVIES.SELECT.in","543313","543316"],"StarPlus.in@SD":["Star.Plus.in","STAR.PLUS.in","STARPLUS.in","543093","543164"],"StarPravah.in@SD":["Star.Pravah.in","STAR.PRAVAH.in","543054"],"StarSports1.in@HD":["Star.Sports.1.in","STAR.SPORTS.1.in","StarSports1.in","543006","543489"],"StarSports1Hindi.in@HD":["STAR.SPORTS.1.HINDI.in","StarSports1Hindi.in","543275","543058"],"StarSports3.in@SD":["STAR.SPORTS.3.in","StarSports3.in","543366"],"StarSportsSelect1.in@SD":["Star.Sports.Select.1.in","StarSportsSelect1.in","543120","543263"],"StarSportsSelect2.in@SD":["Star.Sports.Select.2.in","STAR.SPORTS.SELECT.2.in","StarSportsSelect2.in","543061","543450"],"StarSuvarnaPlus.in@SD":["STAR.SUVARNA.PLUS.in","543423"],"StarUtsavMovies.in@SD":["Star.Utsav.Movies.in","STAR.UTSAV.MOVIES.in","543124"],"SteelbirdMusic.in@SD":["Steelbird.Music.in"],"StudioOnePlus.in@SD":["Studio.One.in"],"SunBangla.in@SD":["Sun.Bangla.in","SUN.BANGLA.in","SUNBANGLA.in","543322"],"SunMusic.in@SD":["Sun.Music.HD.in","SUN.MUSIC.in","543232","543454"],"SuperHungama.in@SD":["Super.Hungama.in","SUPER.HUNGAMA.in","543103"],"TLC.in@HD":["TLC.HD.in","TLC.in","543386","543128"],"TabbarHits.in":["Tabbar.Hits.in"],"TarangMusic.in@SD":["TARANG.MUSIC.in","543280"],"ThanthiOne.in":["Thanthi.One.in","THANTHI.ONE.in"],"Travelxp.in@SD":["Travelxp.HD.Hindi.in","Travelxp.in"],"UBangla.in":["U.Bangla.in"],"VaanavilTV.in@SD":["Vaanavil.TV.in"],"VanithaTV.in@SD":["Vanitha.in"],"VasanthTV.in@SD":["Vasanth.TV.in","VASANTH.TV.in","VasanthTV.in","543287"],"VendharTV.in@SD":["Vendhar.TV.in","VendharTV.in"],"VijaySuper.in@SD":["VIJAY.SUPER.in","543204","543438"],"VissaTV.in@SD":["Vissa.TV.in","VISSA.TV.in","VissaTV.in","543439"],"WahPunjabi.in@SD":["Wah.Punjabi.in"],"WildEarth.za":["Wild.Earth.in"],"YRFMusic.in@SD":["YRF.Music.in"],"Zee24Ghanta.in@SD":["Zee.24.Ghanta.in","Zee24Ghanta.in","554174"],"ZeeAction.in":["ZEE.ACTION.in","543243"],"ZeeBangla.in@HD":["Zee.Bangla.in","ZEE.BANGLA.in","ZEEBANGLA.in","543504","404001"],"ZeeBollywood.in@SD":["Zee.Bollywood.in","ZEE.Bollywood.in","ZeeBollywood.in","543294"],"ZeeCinema.in@HD":["Zee.Cinema.in","ZEE.CINEMA.in","ZeeCinema.in","543084","543330"],"ZeeCinemalu.in@HD":["Zee.Cinemalu.HD.in","ZEE.CINEMALU.in","ZeeCinemalu.in","543172","543358"],"ZeeKannada.in@SD":["Zee.Kannada.in","ZEE.KANNADA.in","ZeeKannada.in","543097","543064"],"ZeeTV.in@SD":["Zee.TV.in","ZEE.TV.in","ZeeTV.in","543105","543086"],"ZeeTalkies.in@HD":["Zee.Talkies.in","ZEE.TALKIES.in","ZeeTalkies.in","543200","543068"],"ZeeTamil.in@SD":["Zee.Tamil.in","ZEE.TAMIL.in","ZeeTamil.in","543143","543165"],"Zing.in@SD":["ZING.in","Zing.in","543208"],"custom.aljazeera.english":["AL.Jazeera.in","ALJAZEERA.in","AlJazeera.in","543135"],"custom.colors":["Colors.in","Colors.SD.in","Colors.HD.in","COLORS.in","COLORS.HD.in","543080","543247"],"custom.ekamra.cinema":["Ekamra.Cinema.in"],"custom.ekamra.manoranjan":["Ekamra.Manoranjan.in"],"custom.ekamra.musiq":["Ekamra.Musiq.in"],"custom.solntse":["&TV.HD.in"],"custom.sonic.bangla":["Sonic.Bangla.in"],"custom.sony.ten.1":["Sony.Ten.1.in","Sony.Ten.1.HD.in"],"custom.sony.ten.5":["Sony.Ten.5.HD.in","Sony.Ten.5.in"],"custom.sonyten2":["Sony.Ten.2.HD.in"],"custom.starsports2":["Star.Sports.2.HD.in","STAR.SPORTS.2.in","STAR.SPORTS.2.HD.in","StarSports2.in","543210","543498"]};


























































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
  const xmls=[];
  for(const source of EPG_URLS){
    try{
      const r=await fetch(source,{headers:{"user-agent":"BDIX-IPTV-Xtream-Gateway/1.0","accept":"application/gzip, application/xml, text/xml, */*"}});
      if(!r.ok) continue;
      const bytes=await r.arrayBuffer();
      const encoding=(r.headers.get("content-encoding")||"").toLowerCase();
      let xml;
      if(encoding.includes("gzip")) {
        xml=new TextDecoder().decode(bytes);
      } else if(source.endsWith(".gz")) {
        try {
          xml=await new Response(new Blob([bytes]).stream().pipeThrough(new DecompressionStream("gzip"))).text();
        } catch {
          xml=new TextDecoder().decode(bytes);
        }
      } else {
        xml=new TextDecoder().decode(bytes);
      }
      if(xml.includes("<tv") && xml.includes("<programme")) xmls.push(xml);
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
