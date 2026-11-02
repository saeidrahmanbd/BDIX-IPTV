const RAW_BASE = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main";
const ALLOWED = {
  "/main.m3u": "IPTV-Playlist.m3u",
  "/international.m3u": "International-Playlist.m3u"
};

const dashboard = `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>BDIX-IPTV Analytics</title><style>
:root{color-scheme:dark}*{box-sizing:border-box}body{margin:0;background:#0d1117;color:#e6edf3;font:15px system-ui,sans-serif}main{max-width:980px;margin:40px auto;padding:0 18px}h1{font-size:28px;margin:0 0 8px}.muted{color:#8b949e}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:14px;margin:24px 0}.card{background:#161b22;border:1px solid #30363d;border-radius:12px;padding:18px}.value{font-size:32px;font-weight:750;margin-top:8px}.section{margin-top:28px}table{width:100%;border-collapse:collapse;background:#161b22;border:1px solid #30363d;border-radius:10px;overflow:hidden}td,th{text-align:left;padding:12px;border-bottom:1px solid #30363d}th{color:#8b949e;font-weight:600}code{overflow-wrap:anywhere}a{color:#58a6ff}.pill{display:inline-block;padding:4px 9px;border:1px solid #30363d;border-radius:20px;color:#3fb950;font-size:12px}
</style></head><body><main><span class="pill">LIVE ANALYTICS API</span><h1>BDIX-IPTV Analytics</h1><p class="muted">Playlist request activity captured through the analytics gateway. This measures playlist fetches, not people watching channels.</p><div class="grid"><div class="card">Playlist requests · 14 days<div class="value" id="hits">—</div></div><div class="card">Unique clients · 14 days<div class="value" id="unique">—</div></div><div class="card">Main playlist requests<div class="value" id="main">—</div></div><div class="card">International requests<div class="value" id="intl">—</div></div></div><div class="section"><h2>Daily activity</h2><table><thead><tr><th>Date (UTC)</th><th>Playlist</th><th>Requests</th><th>Unique clients</th></tr></thead><tbody id="rows"><tr><td colspan="4">Loading…</td></tr></tbody></table></div><div class="section"><h2>Top countries</h2><table><thead><tr><th>Country code</th><th>Requests</th><th>Unique clients</th></tr></thead><tbody id="countries"><tr><td colspan="3">Loading…</td></tr></tbody></table></div><p class="muted section">Unique clients are privacy-preserving daily estimates based on a salted hash. IP addresses are never stored. Automated clients may still appear.</p><p class="muted">Refresh this page to update. Data retention: 90 days.</p></main><script>
fetch('/api/stats?days=14').then(r=>{if(!r.ok)throw Error('API '+r.status);return r.json()}).then(d=>{document.getElementById('hits').textContent=d.totals.requests.toLocaleString();document.getElementById('unique').textContent=d.totals.unique_clients.toLocaleString();document.getElementById('main').textContent=(d.totals.by_playlist.main||0).toLocaleString();document.getElementById('intl').textContent=(d.totals.by_playlist.international||0).toLocaleString();document.getElementById('rows').innerHTML=d.daily.map(x=>'<tr><td>'+x.day+'</td><td>'+x.playlist+'</td><td>'+Number(x.requests).toLocaleString()+'</td><td>'+Number(x.unique_clients).toLocaleString()+'</td></tr>').join('')||'<tr><td colspan="4">No traffic recorded yet.</td></tr>';document.getElementById('countries').innerHTML=d.countries.map(x=>'<tr><td>'+x.country+'</td><td>'+Number(x.requests).toLocaleString()+'</td><td>'+Number(x.unique_clients).toLocaleString()+'</td></tr>').join('')||'<tr><td colspan="3">No country data yet.</td></tr>'}).catch(e=>{document.getElementById('rows').innerHTML='<tr><td colspan="4">Analytics unavailable: '+e.message+'</td></tr>'});
</script></body></html>`;

async function clientHash(request, salt) {
  const ip = request.headers.get("CF-Connecting-IP") || "unknown";
  const ua = request.headers.get("User-Agent") || "unknown";
  const day = new Date().toISOString().slice(0, 10);
  const data = new TextEncoder().encode(salt + "|" + day + "|" + ip + "|" + ua);
  const digest = await crypto.subtle.digest("SHA-256", data);
  return [...new Uint8Array(digest)].map(b => b.toString(16).padStart(2, "0")).join("");
}

function json(data, status=200) {
  return new Response(JSON.stringify(data), {status, headers: {"content-type":"application/json; charset=utf-8","cache-control":"no-store","access-control-allow-origin":"*"}});
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (request.method !== "GET" && request.method !== "HEAD") return new Response("Method not allowed", {status:405});
    if (url.pathname === "/" || url.pathname === "/dashboard") {
      return new Response(dashboard, {headers: {"content-type":"text/html; charset=utf-8","cache-control":"no-store"}});
    }
    if (url.pathname === "/health") return json({ok:true,service:"bdix-iptv-analytics"});
    if (url.pathname === "/api/stats") {
      const days = Math.min(90, Math.max(1, Number(url.searchParams.get("days") || 14)));
      const since = new Date(Date.now() - days * 86400000).toISOString();
      const [totals, daily] = await Promise.all([
        env.ANALYTICS_DB.prepare("SELECT COUNT(*) requests, COUNT(DISTINCT client_hash || ':' || day) unique_clients FROM hits WHERE ts >= ?").bind(since).first(),
        env.ANALYTICS_DB.prepare("SELECT day, playlist, COUNT(*) requests, COUNT(DISTINCT client_hash) unique_clients FROM hits WHERE ts >= ? GROUP BY day, playlist ORDER BY day DESC, playlist").bind(since).all()
      ]);
      const [byPlaylist, byCountry] = await Promise.all([
        env.ANALYTICS_DB.prepare("SELECT playlist, COUNT(*) requests FROM hits WHERE ts >= ? GROUP BY playlist").bind(since).all(),
        env.ANALYTICS_DB.prepare("SELECT country, COUNT(*) requests, COUNT(DISTINCT client_hash || ':' || day) unique_clients FROM hits WHERE ts >= ? GROUP BY country ORDER BY requests DESC LIMIT 20").bind(since).all()
      ]);
      const map = Object.fromEntries((byPlaylist.results || []).map(x => [x.playlist, x.requests]));
      return json({period_days:days, totals:{requests:totals?.requests||0,unique_clients:totals?.unique_clients||0,by_playlist:map},countries:byCountry.results||[],daily:daily.results||[]});
    }
    const filename = ALLOWED[url.pathname];
    if (!filename) return new Response("Not found", {status:404});
    const upstream = await fetch(RAW_BASE + "/" + filename, {headers: {"accept":"*/*"}});
    if (!upstream.ok) return new Response("Upstream playlist unavailable", {status:502});
    const body = request.method === "HEAD" ? null : await upstream.arrayBuffer();
    const playlist = url.pathname === "/main.m3u" ? "main" : "international";
    const ip = request.headers.get("CF-Connecting-IP");
    const ua = request.headers.get("User-Agent") || "";
    // Exclude obvious crawlers from the primary usage figures; keep real player clients.
    const bot = /bot|crawler|spider|slurp|preview|monitor|uptime|github-actions/i.test(ua);
    if (!bot && ip && env.ANALYTICS_SALT) {
      const day = new Date().toISOString().slice(0,10);
      const hash = await clientHash(request, env.ANALYTICS_SALT);
      await env.ANALYTICS_DB.prepare("INSERT INTO hits (ts, day, playlist, client_hash, country) VALUES (?, ?, ?, ?, ?)")
        .bind(new Date().toISOString(), day, playlist, hash, request.cf?.country || "XX").run();
    }
    const headers = new Headers(upstream.headers);
    headers.set("content-type","application/vnd.apple.mpegurl; charset=utf-8");
    headers.set("cache-control","no-store, no-cache, must-revalidate");
    headers.set("access-control-allow-origin","*");
    headers.delete("content-length");
    return new Response(body, {status:200,headers});
  },
  async scheduled(controller, env, ctx) {
    ctx.waitUntil(env.ANALYTICS_DB.prepare("DELETE FROM hits WHERE ts < ?").bind(new Date(Date.now()-90*86400000).toISOString()).run());
  }
};
