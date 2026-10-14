// BDIX-IPTV Xtream gateway — IPTV at /, BDIX at /bdix.
const DEFAULT_PLAYLIST_URL = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u";
const DEFAULT_BDIX_PLAYLIST_URL = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/BDIX-Playlist.m3u";
const EPG_PUBLIC_URL = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/epg/epg.xml";
const CACHE_TTL = 60;
const INACTIVE_GROUPS = new Set(["Test", "Not Playing", "New Backup", "New Channels"]);
const EPG_ID_MAP = {};

function json(data,status=200){return new Response(JSON.stringify(data),{status,headers:{"content-type":"application/json; charset=utf-8","cache-control":"no-store"}})}
function xml(data,status=200){return new Response(data,{status,headers:{"content-type":"application/xml; charset=utf-8","cache-control":"no-store"}})}
function text(data,status=200,type="text/plain; charset=utf-8"){return new Response(data,{status,headers:{"content-type":type,"cache-control":"no-store"}})}
function attrs(line){const out={};const re=/([A-Za-z0-9_-]+)="([^"]*)"/g;let m;while((m=re.exec(line)))out[m[1]]=m[2];return out}
function parsePlaylist(textData){const rows=[];let current=null;let streamId=1;for(const raw of textData.split(/\r?\n/)){const line=raw.trim();if(line.startsWith("#EXTINF:")){const a=attrs(line);const comma=line.indexOf(",");current={tvgId:(a["tvg-id"]||"").trim(),tvgName:(a["tvg-name"]||(comma>=0?line.slice(comma+1).trim():"")).trim(),logo:(a["tvg-logo"]||"").trim(),group:(a["group-title"]||"Uncategorized").trim(),chno:(a["tvg-chno"]||"").trim()}}else if(current&&/^https?:\/\//i.test(line)){if(current.tvgId&&!INACTIVE_GROUPS.has(current.group))rows.push({...current,url:line,id:streamId++});current=null}}return rows}
function categoryList(streams){return[...new Set(streams.map(x=>x.group).filter(Boolean))].map((name,i)=>({category_id:String(i+1),category_name:name,parent_id:0}))}
function withCategoryIds(streams,categories){const ids=new Map(categories.map(x=>[x.category_name,x.category_id]));return streams.map(s=>({...s,categoryId:ids.get(s.group)||"1"}))}
function mappedEpgId(tvgId){const ids=EPG_ID_MAP[tvgId];return Array.isArray(ids)&&ids.length?ids[0]:tvgId}
function authOk(url,env){
  const suppliedU=(url.searchParams.get("username")||"").trim();
  const suppliedP=url.searchParams.get("password")||"";
  const secretU=String(env.XTREAM_USERNAME||"").trim();
  const secretP=String(env.XTREAM_PASSWORD||"");
  const configuredU=String(env.XTREAM_LOGIN_USERNAME||"").trim();
  const configuredP=String(env.XTREAM_LOGIN_PASSWORD||"");
  const expectedU=secretU||configuredU;
  const expectedP=secretP||configuredP;
  return Boolean(expectedU&&expectedP&&suppliedU===expectedU&&suppliedP===expectedP);
}
function basePath(pathname){return pathname==="/bdix"||pathname.startsWith("/bdix/")?"/bdix":""}
function envPlaylistUrl(env,base){return base==="/bdix"?(env.BDIX_PLAYLIST_URL||DEFAULT_BDIX_PLAYLIST_URL):(env.PLAYLIST_URL||DEFAULT_PLAYLIST_URL)}
async function cachedFetch(url,ttl=CACHE_TTL){const req=new Request(url,{method:"GET",headers:{"User-Agent":"BDIX-IPTV-Xtream/5.0"}});const cache=caches.default;const cached=await cache.match(req);if(cached)return cached;const response=await fetch(req);if(!response.ok)return response;const copy=new Response(response.body,response);copy.headers.set("cache-control",`public,max-age=${ttl}`);await cache.put(req,copy.clone());return copy}
async function getStreams(env,base){const response=await cachedFetch(envPlaylistUrl(env,base),60);if(!response.ok)throw new Error(`playlist HTTP ${response.status}`);const streams=parsePlaylist(await response.text());if(!streams.length)throw new Error(`playlist parsed 0 active streams from ${envPlaylistUrl(env,base)}`);return streams}
function streamPayload(s,base,origin){return{num:Number(s.chno)||s.id,name:s.tvgName,stream_type:"live",stream_id:s.id,stream_icon:s.logo,epg_channel_id:mappedEpgId(s.tvgId),category_id:s.categoryId,tv_archive:0,direct_source:s.url,stream_url:`${origin}${base}/live/{username}/{password}/${s.id}.ts`,tvg_id:s.tvgId,tvg_name:s.tvgName}}
async function getEpgXml(){const response=await cachedFetch(EPG_PUBLIC_URL,300);if(!response.ok)throw new Error(`EPG HTTP ${response.status}`);return response.text()}
function makeM3U(streams,base,origin,username,password){const lines=["#EXTM3U",`#PLAYLIST:BDIX-IPTV Xtream ${base||"/"}`];for(const s of streams)lines.push(`#EXTINF:-1 tvg-id="${s.tvgId}" tvg-name="${s.tvgName.replace(/"/g,"&quot;")}" tvg-logo="${s.logo}" group-title="${s.group}" tvg-chno="${s.chno}"`,`${origin}${base}/live/${encodeURIComponent(username)}/${encodeURIComponent(password)}/${s.id}.ts`);return lines.join("\n")+"\n"}
async function handlePlayerApi(url,env,base,origin){const action=(url.searchParams.get("action")||"").toLowerCase();const raw=await getStreams(env,base),categories=categoryList(raw),streams=withCategoryIds(raw,categories);const username=url.searchParams.get("username")||"";if(!action)return json({user_info:{username,auth:1,status:"Active",exp_date:"",is_trial:"0",active_cons:"0",created_at:"",max_connections:"10",allowed_output_formats:["m3u8","ts"]},server_info:{url:origin,port:"443",https_port:"443",protocol:"https",timezone:env.TIMEZONE||"Asia/Dhaka",timestamp_now:Math.floor(Date.now()/1000)}});if(action==="get_live_categories")return json(categories);if(action==="get_live_streams"){const category=url.searchParams.get("category_id");const selected=category?streams.filter(s=>s.categoryId===category):streams;return json(selected.map(s=>streamPayload(s,base,origin)))}if(action==="get_short_epg"||action==="get_simple_data_table")return json({epg_listings:[]});return json([])}
export default{async fetch(request,env){const url=new URL(request.url),base=basePath(url.pathname),path=base?url.pathname.slice(base.length)||"/":url.pathname,origin=url.origin;
if(path==="/health"){try{const streams=await getStreams(env,base);return json({ok:true,base,playlist_url:envPlaylistUrl(env,base),streams:streams.length,timestamp:new Date().toISOString()})}catch(e){return json({ok:false,base,error:String(e)},502)}}
if(path==="/epg-health"){try{const xmlText=await getEpgXml();return json({ok:true,bytes:xmlText.length,channels:(xmlText.match(/<channel\b/g)||[]).length,programmes:(xmlText.match(/<programme\b/g)||[]).length})}catch(e){return json({ok:false,error:String(e)},502)}}
if(path==="/xmltv-public.php"){try{return xml(await getEpgXml())}catch(e){return text(String(e),502)}}
if(path==="/xmltv.php"){if(!authOk(url,env))return json({user_info:{auth:0,status:"Disabled"}},401);try{return xml(await getEpgXml())}catch(e){return text(String(e),502)}}
if(path==="/get.php"){if(!authOk(url,env))return text("Unauthorized",401);try{const raw=await getStreams(env,base),streams=withCategoryIds(raw,categoryList(raw));return text(makeM3U(streams,base,origin,url.searchParams.get("username")||"",url.searchParams.get("password")||""),200,"audio/x-mpegurl; charset=utf-8")}catch(e){return text(String(e),502)}}
if(path==="/player_api.php"){if(!authOk(url,env))return json({user_info:{auth:0,status:"Disabled"}},401);try{return await handlePlayerApi(url,env,base,origin)}catch(e){return json({error:String(e)},502)}}
const live=path.match(/^\/live\/([^/]+)\/([^/]+)\/(\d+)(?:\.(?:ts|m3u8))?$/i);if(live){if(!authOk(url,env))return text("Unauthorized",401);try{const stream=(await getStreams(env,base)).find(s=>s.id===Number(live[3]));if(!stream)return text("Stream not found",404);return fetch(stream.url,{headers:{"User-Agent":"BDIX-IPTV-Xtream/5.0"}})}catch(e){return text(String(e),502)}}
return json({ok:true,service:"BDIX-IPTV Xtream",base,endpoints:["player_api.php","get.php","xmltv.php","xmltv-public.php","live/<username>/<password>/<stream_id>.ts"]})}}
