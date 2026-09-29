const DEFAULT_PLAYLIST_URL = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u";
const CACHE_KEY = "https://bdix-iptv.internal/playlist";
const CACHE_TTL = 60;

const EPG_URLS = [
  // Keep the request path memory-safe. IN1 is the broad India guide;
  // additional large guides are handled by the offline coverage workflow.
  "https://epgshare01.online/epgshare01/epg_ripper_IN1.xml.gz"
];
const EPG_CACHE_KEY = "https://bdix-iptv.internal/epg-xml-v9";
const EPG_CACHE_TTL = 900;
// Direct M3U EPG endpoint deployment trigger. v9: memory-safe India guide.

// Cross-map playlist tvg-id variants to canonical EPG IDs used by public guides.
const EPG_ID_MAP = {
  "AakaashAath.in":["AakaashAath.in@SD","Aakash.Aath.in"],
  "AlankarTV.in":["AlankarTV.in@SD"],
  "DDTripura.in":["DDTripura.in@SD"],
  "KhushbooBangla.in":["KhushbooBangla.in@SD"],
  "RupasiBangla.in":["RupasiBangla.in@SD","RUPASI.BANGLA.in"],
  "ZBCinema.in":["ZeeBanglaCinema.in@SD","ZeeBanglaSonar.in@SD","ZEE.BANGLA.CINEMA.in"],
  "zeebanglacinema.in":["ZeeBanglaCinema.in@SD","ZeeBanglaSonar.in@SD","ZEE.BANGLA.CINEMA.in"],
  "AndTV.in":["AndTV.in@SD","&TV.HD.in"],
  "OscarMoviesBhojpuri.in@SD":["OscarMoviesBhojpuri.in@SD","Oscar.Movies.Bhojpuri.in","Oscar.Movies.Bhojpuri.Tv.in2"],
  "Goldmines.in":["Goldmines.in@SD","Goldmines.in"],
  "GoldminesAction.in":["GoldminesAction.in@SD"],
  "GoldminesBollywood.in":["GoldminesBollywood.in@SD","Goldmines.Bollywood.in","Goldmines.Bollywood.Today.in2"],
  "GoldminesMovies.in":["GoldminesMovies.in@SD","Goldmines.Movies.in","Goldmines.Movies.Today.For.Dd.Free.Dish.Users.in2","Goldmines.Movie.Today.in2"],
  "AnjanTV.in@SD":["AnjanTV.in@SD","Anjan.TV.in"],
  "B4UBhojpuri.in@SD":["B4UBhojpuri.in@SD","B4U.Bhojpuri.in","B4u.Bhojpuri.in2"],
  "MHOneDilSe.in":["MHOneDilSe.in@SD","MH1.Dil.Se.in","Mh1.Dil.Se.Tv.Channel.Today.in2"],
  "MTV.in@SD":["MTV.in@SD","MTV.in"],
  "KalaignarMurasu.in":["KalaignarMurasu.in","MURASU.in"],
  "ShemarooJosh.in":["ShemarooJosh.in@SD","Shemaroo.Josh.Today.in2"],
  "DisneyChannel.in":["DisneyChannel.in@HD","Disney.in"],
  "StarJalsha.in":["StarJalsha.in@SD","StarJalsha.in@HD"],
  "ZeeBangla.in":["ZeeBangla.in@SD","ZeeBangla.in@HD"],
  "ColorsBangla.in":["ColorsBangla.in@SD","ColorsBangla.in@HD"],
  "SonyAath.in":["SonyAath.in@SD"],
  "DDAssam.in":["DDAssam.in@SD"],
  "DDGoa.in":["DDGoa.in@SD"],
  "DDHaryana.in":["DDHaryana.in@SD"],
  "DDHimachalPradesh.in":["DDHimachalPradesh.in@SD"],
  "DDJharkhand.in":["DDJharkhand.in@SD"],
  "DDManipur.in":["DDManipur.in@SD"],
  "DDMeghalaya.in":["DDMeghalaya.in@SD"],
  "DDNagaland.in":["DDNagaland.in@SD"],
  "MHOneMovies.in":["MHOneMovies.in@SD"],
  "ETVMusic.in":["ETVMusic.in@SD"],
  "SonySAB.in":["SonySAB.in@SD"],
  "local.bb3c3114fb20":["ColorsBangla.in@HD"],
  "local.285a6aa870f3":["JalshaMovies.in@HD"],
  "local.zee-24-ghanta":["Zee24Ghanta.in@SD"],
  "local.072484feec7":["ZeeBangla.in@HD"],
  "local.5f40adcebbde":["Colors.in@SD","Colors.in@HD"],
  "local.history-tv18":["HistoryTV18.in@SD","HistoryTV18.in@HD"],
  "CartoonNetwork.uk":["CartoonNetwork.in@SD"],
  "CartoonNetworkHDPlus.in":["CartoonNetwork.in@SD"],
  "DiscoveryKids.au":["DiscoveryKids.in@SD"],
  "local.enter-10-bangla":["Enterr10Bangla.in@SD"],
  "local.gold-mines-movie":["GoldminesMovies.in@SD"],
  "SonyEntertainmentTelevision":["SonyEntertainmentTelevision.in@SD","SonyEntertainmentTelevision.in@HD"]
};

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
function findEpgPrograms(epg,entry){
  for(const key of epgKeyVariants(entry.tvgId,entry.name)){
    const programs=epg.byId.get(key);
    if(programs?.length) return programs;
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