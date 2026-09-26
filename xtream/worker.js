const DEFAULT_PLAYLIST_URL = "https://raw.githubusercontent.com/saeidsujon-rahman/BDIX-IPTV/main/IPTV%20Playlist.m3u";
const CACHE_KEY = "https://bdix-iptv.internal/playlist";
const CACHE_TTL = 60;

function json(data, status = 200) {
  return new Response(JSON.stringify(data), { status, headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store" } });
}
function parseAttrs(line) {
  const attrs = {}; let m; const re = /([\\w-]+)="([^"]*)"/g;
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
  const origin=new URL(request.url).origin;
  return {user_info:{username:env.XTREAM_USERNAME,password:env.XTREAM_PASSWORD,message:"BDIX-IPTV Xtream Gateway",auth:1,status:"Active",exp_date:"0",is_trial:"0",active_cons:"0",created_at:String(Math.floor(Date.now()/1000)),max_connections:"2",allowed_output_formats:["ts","m3u8"]},server_info:{url:origin,port:"443",https_port:"443",server_protocol:"https",timezone:env.TIMEZONE||"Asia/Dhaka",timestamp_now:Math.floor(Date.now()/1000),time_now:new Date().toISOString()}};
}
function categories(data){return data.groups.map((name,i)=>({category_id:String(i+1),category_name:name,parent_id:0}));}
function streams(data,cat){
  const src=cat?data.entries.filter(e=>e.categoryId===String(cat)):data.entries;
  return src.map((e,i)=>({num:Number(e.channelNo)||i+1,name:e.name,stream_type:"live",stream_id:e.id,stream_icon:e.logo,epg_channel_id:e.tvgId,added:"0",category_id:e.categoryId,custom_sid:"",tv_archive:0,direct_source:e.url,tv_archive_duration:0}));
}
function m3u(data,request,env){
  const u=new URL(request.url), ext=(u.searchParams.get("output")||"m3u8").toLowerCase()==="ts"?"ts":"m3u8", out=["#EXTM3U"];
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
   if(path==="/player_api.php"){
    if(!auth(url,env)) return json({user_info:{auth:0,status:"Invalid credentials"}},401);
    const action=url.searchParams.get("action")||"", data=parsePlaylist(await getPlaylist(env));
    if(!action||action==="get_account_info") return json(userInfo(request,env));
    if(action==="get_live_categories") return json(categories(data));
    if(action==="get_live_streams") return json(streams(data,url.searchParams.get("category_id")));
    if(action==="get_short_epg"||action==="get_simple_data_table"||action==="get_all_epg") return json({epg_listings:[]});
    if(action==="get_vod_categories"||action==="get_series_categories"||action==="get_vod_streams"||action==="get_series") return json([]);
    return json({error:"Unsupported action"},400);
   }
   if(path==="/get.php"){if(!auth(url,env)) return new Response("Unauthorized",{status:401}); return m3u(parsePlaylist(await getPlaylist(env)),request,env);}
   if(path==="/xmltv.php"){if(!auth(url,env)) return new Response("Unauthorized",{status:401}); return emptyEpg();}
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