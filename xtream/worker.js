// BDIX-IPTV Xtream gateway — IPTV at /, BDIX at /bdix.
// Backup is retained; Test/New Channels/New Backup/Not Playing are excluded.
const DEFAULT_PLAYLIST_URL = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u";
const DEFAULT_BDIX_PLAYLIST_URL = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/BDIX-Playlist.m3u";
const EPG_PUBLIC_URL = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/epg/epg.xml";
const CACHE_TTL = 60;
const INACTIVE_GROUPS = new Set(["Test", "Not Playing", "New Backup", "New Channels"]);

// scripts/sync_epg_worker_map.py replaces this object during maintenance.
// The gateway falls back to the playlist tvg-id when no explicit mapping exists.
const EPG_ID_MAP = {};

function json(data, status = 200) {
  return new Response(JSON.stringify(data), { status, headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store" } });
}
function xml(data, status = 200) {
  return new Response(data, { status, headers: { "content-type": "application/xml; charset=utf-8", "cache-control": "no-store" } });
}
function text(data, status = 200, type = "text/plain; charset=utf-8") {
  return new Response(data, { status, headers: { "content-type": type, "cache-control": "no-store" } });
}
function attrs(line) {
  const out = {};
  const re = /([A-Za-z0-9_-]+)="([^"]*)"/g;
  let m; while ((m = re.exec(line))) out[m[1]] = m[2];
  return out;
}
function parsePlaylist(textData) {
  const rows = []; let current = null; let streamId = 1;
  for (const raw of textData.split(/\r?\n/)) {
    const line = raw.trim();
    if (line.startsWith("#EXTINF:")) {
      const a = attrs(line); const comma = line.indexOf(",");
      current = { tvgId: (a["tvg-id"] || "").trim(), tvgName: (a["tvg-name"] || (comma >= 0 ? line.slice(comma + 1).trim() : "")).trim(), logo: (a["tvg-logo"] || "").trim(), group: (a["group-title"] || "Uncategorized").trim(), chno: (a["tvg-chno"] || "").trim(), country: (a["tvg-country"] || "").trim() };
    } else if (current && /^https?:\/\//i.test(line)) {
      if (current.tvgId && !INACTIVE_GROUPS.has(current.group)) rows.push({ ...current, url: line, id: streamId++ });
      current = null;
    }
  }
  return rows;
}
function categoryList(streams) {
  return [...new Set(streams.map(x => x.group).filter(Boolean))].map((name, i) => ({ category_id: String(i + 1), category_name: name, parent_id: 0 }));
}
function withCategoryIds(streams, categories) {
  const ids = new Map(categories.map(x => [x.category_name, x.category_id]));
  return streams.map(s => ({ ...s, categoryId: ids.get(s.group) || "1" }));
}
function mappedEpgId(tvgId) {
  const ids = EPG_ID_MAP[tvgId];
  return Array.isArray(ids) && ids.length ? ids[0] : tvgId;
}
function authOk(url, env) {
  const expectedU = env.XTREAM_USERNAME, expectedP = env.XTREAM_PASSWORD;
  if (!expectedU || !expectedP) return true;
  return url.searchParams.get("username") === expectedU && url.searchParams.get("password") === expectedP;
}
function basePath(pathname) { return pathname === "/bdix" || pathname.startsWith("/bdix/") ? "/bdix" : ""; }
function envPlaylistUrl(env, base) { return base === "/bdix" ? (env.BDIX_PLAYLIST_URL || DEFAULT_BDIX_PLAYLIST_URL) : (env.PLAYLIST_URL || DEFAULT_PLAYLIST_URL); }
async function cachedFetch(url, ttl = CACHE_TTL) {
  const req = new Request(url, { method: "GET", headers: { "User-Agent": "BDIX-IPTV-Xtream/5.0" } });
  const cache = caches.default; const cached = await cache.match(req); if (cached) return cached;
  const response = await fetch(req); if (!response.ok) return response;
  const copy = new Response(response.body, response); copy.headers.set("cache-control", `public, max-age=${ttl}`); await cache.put(req, copy.clone()); return copy;
}
async function getStreams(env, base) {
  const response = await cachedFetch(envPlaylistUrl(env, base), 60); if (!response.ok) throw new Error(`playlist HTTP ${response.status}`);
  return parsePlaylist(await response.text());
}
function streamPayload(s, base, origin) {
  return { num: Number(s.chno) || s.id, name: s.tvgName, stream_type: "live", stream_id: s.id, stream_icon: s.logo, epg_channel_id: mappedEpgId(s.tvgId), category_id: s.categoryId, tv_archive: 0, direct_source: s.url, stream_url: `${origin}${base}/live/{username}/{password}/${s.id}.ts`, tvg_id: s.tvgId, tvg_name: s.tvgName };
}
function programmeRows(xmlText, channelId, limit = 10) {
  const escaped = channelId.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  const re = new RegExp(`<programme\\b[^>]*\\bchannel=["']${escaped}["'][^>]*>([\\s\\S]*?)</programme>`, "gi");
  const out = []; let m;
  while ((m = re.exec(xmlText)) && out.length < limit) {
    const full = m[0]; const get = tag => { const x = full.match(new RegExp(`<${tag}[^>]*>([\\s\\S]*?)</${tag}>`, "i")); return x ? x[1].replace(/<!\[CDATA\[|\]\]>/g, "").replace(/<[^>]+>/g, "").trim() : ""; };
    const start = (full.match(/\bstart=["']([^"']+)["']/i) || [])[1] || ""; const stop = (full.match(/\bstop=["']([^"']+)["']/i) || [])[1] || "";
    out.push({ id: String(out.length + 1), start, stop, title: get("title"), description: get("desc") });
  }
  return out;
}
async function getEpgXml() {
  const response = await cachedFetch(EPG_PUBLIC_URL, 300); if (!response.ok) throw new Error(`EPG HTTP ${response.status}`); return response.text();
}
function makeM3U(streams, base, origin, username, password) {
  const lines = ["#EXTM3U", `#PLAYLIST:BDIX-IPTV Xtream ${base || "/"}`];
  for (const s of streams) lines.push(`#EXTINF:-1 tvg-id="${s.tvgId}" tvg-name="${s.tvgName.replace(/"/g, "&quot;")}" tvg-logo="${s.logo}" group-title="${s.group}" tvg-chno="${s.chno}"`, `${origin}${base}/live/${encodeURIComponent(username)}/${encodeURIComponent(password)}/${s.id}.ts`);
  return lines.join("\n") + "\n";
}
async function handlePlayerApi(url, env, base, origin) {
  const action = (url.searchParams.get("action") || "").toLowerCase();
  const raw = await getStreams(env, base); const categories = categoryList(raw); const streams = withCategoryIds(raw, categories);
  const username = url.searchParams.get("username") || "", password = url.searchParams.get("password") || "";
  if (!action) return json({ user_info: { username, auth: 1, status: "Active", exp_date: "", is_trial: "0", active_cons: "0", created_at: "", max_connections: "10", allowed_output_formats: ["m3u8", "ts"] }, server_info: { url: origin, port: "443", https_port: "443", protocol: "https", timezone: env.TIMEZONE || "Asia/Dhaka", timestamp_now: Math.floor(Date.now() / 1000) } });
  if (action === "get_live_categories") return json(categories);
  if (action === "get_live_streams") {
    const category = url.searchParams.get("category_id");
    const selected = category ? streams.filter(s => s.categoryId === category) : streams;
    return json(selected.map(s => streamPayload(s, base, origin)));
  }
  if (action === "get_short_epg" || action === "get_simple_data_table") {
    const stream = streams.find(s => s.id === Number(url.searchParams.get("stream_id")));
    if (!stream) return json({ epg_listings: [] });
    const rows = programmeRows(await getEpgXml(), mappedEpgId(stream.tvgId), action === "get_short_epg" ? Number(url.searchParams.get("limit") || 10) : 50);
    if (action === "get_simple_data_table") return json(rows);
    return json({ epg_listings: rows.map(p => ({ id: p.id, epg_id: mappedEpgId(stream.tvgId), title: btoa(unescape(encodeURIComponent(p.title))), description: btoa(unescape(encodeURIComponent(p.description))), start: p.start, end: p.stop, start_timestamp: p.start, stop_timestamp: p.stop })) });
  }
  if (action === "get_live_info") return json([]);
  return json([]);
}
export default {
  async fetch(request, env) {
    const url = new URL(request.url); const base = basePath(url.pathname); const path = base ? url.pathname.slice(base.length) || "/" : url.pathname; const origin = url.origin;
    if (path === "/health" || path === "/epg-health") {
      try { const xmlText = await getEpgXml(); return json({ ok: true, epg_url: EPG_PUBLIC_URL, bytes: xmlText.length, channels: (xmlText.match(/<channel\b/g) || []).length, programmes: (xmlText.match(/<programme\b/g) || []).length, timestamp: new Date().toISOString() }); } catch (e) { return json({ ok: false, error: String(e) }, 502); }
    }
    if (path === "/xmltv-public.php") { try { return xml(await getEpgXml()); } catch (e) { return text(String(e), 502); } }
    if (path === "/xmltv.php") { if (!authOk(url, env)) return json({ user_info: { auth: 0, status: "Disabled" } }, 401); try { return xml(await getEpgXml()); } catch (e) { return text(String(e), 502); } }
    if (path === "/get.php") {
      if (!authOk(url, env)) return text("Unauthorized", 401);
      try { const raw = await getStreams(env, base); const streams = withCategoryIds(raw, categoryList(raw)); return text(makeM3U(streams, base, origin, url.searchParams.get("username") || "", url.searchParams.get("password") || ""), 200, "audio/x-mpegurl; charset=utf-8"); } catch (e) { return text(String(e), 502); }
    }
    if (path === "/player_api.php") { if (!authOk(url, env)) return json({ user_info: { auth: 0, status: "Disabled" } }, 401); try { return await handlePlayerApi(url, env, base, origin); } catch (e) { return json({ error: String(e) }, 502); } }
    const live = path.match(/^\/live\/([^/]+)\/([^/]+)\/(\d+)(?:\.(?:ts|m3u8))?$/i);
    if (live) {
      if (!authOk(url, env)) return text("Unauthorized", 401);
      try { const stream = (await getStreams(env, base)).find(s => s.id === Number(live[3])); if (!stream) return text("Stream not found", 404); return fetch(stream.url, { headers: { "User-Agent": "BDIX-IPTV-Xtream/5.0" } }); } catch (e) { return text(String(e), 502); }
    }
    return json({ ok: true, service: "BDIX-IPTV Xtream", base, endpoints: ["player_api.php", "get.php", "xmltv.php", "xmltv-public.php", "live/<username>/<password>/<stream_id>.ts"] });
  }
};
