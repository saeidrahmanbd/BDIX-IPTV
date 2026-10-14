const PLAYLIST_URL = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u";
const EPG_URL = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/epg/epg.xml";
const INACTIVE = new Set(["Test", "Not Playing", "New Backup", "New Channels"]);

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store" }
  });
}
function xml(data, status = 200) {
  return new Response(data, {
    status,
    headers: { "content-type": "application/xml; charset=utf-8", "cache-control": "no-store" }
  });
}
function text(data, status = 200, type = "text/plain; charset=utf-8") {
  return new Response(data, {
    status,
    headers: { "content-type": type, "cache-control": "no-store" }
  });
}
function attrs(line) {
  const out = {};
  const re = /([A-Za-z0-9_-]+)="([^"]*)"/g;
  let m;
  while ((m = re.exec(line))) out[m[1]] = m[2];
  return out;
}
function stableId(s) {
  let h = 2166136261;
  for (const c of `${s.tvgId}|${s.url}`) {
    h ^= c.charCodeAt(0);
    h = Math.imul(h, 16777619);
  }
  return (Math.abs(h >>> 0) % 899999999) + 100000000;
}
function parseM3U(data) {
  const out = [];
  let cur = null;
  for (const raw of data.split(/\r?\n/)) {
    const line = raw.trim();
    if (line.startsWith("#EXTINF:")) {
      const a = attrs(line);
      const i = line.indexOf(",");
      cur = {
        tvgId: (a["tvg-id"] || "").trim(),
        name: (a["tvg-name"] || (i >= 0 ? line.slice(i + 1) : "")).trim(),
        logo: (a["tvg-logo"] || "").trim(),
        group: (a["group-title"] || "Uncategorized").trim(),
        chno: (a["tvg-chno"] || "").trim()
      };
    } else if (cur && /^https?:\/\//i.test(line)) {
      if (!INACTIVE.has(cur.group)) {
        const s = { ...cur, url: line };
        s.id = stableId(s);
        out.push(s);
      }
      cur = null;
    }
  }
  return out;
}
async function playlist(env) {
  const source = env.PLAYLIST_URL || PLAYLIST_URL;
  const r = await fetch(source, { headers: { "User-Agent": "BDIX-IPTV-Xtream/6.1" } });
  if (!r.ok) throw Error(`Playlist HTTP ${r.status}`);
  const streams = parseM3U(await r.text());
  if (!streams.length) throw Error("Playlist contains no active streams");
  return streams;
}
function auth(url, env) {
  const expectedUser = String(env.XTREAM_USERNAME || "").trim();
  const expectedPass = String(env.XTREAM_PASSWORD || "");
  return Boolean(expectedUser && expectedPass) &&
    (url.searchParams.get("username") || "").trim() === expectedUser &&
    (url.searchParams.get("password") || "") === expectedPass;
}
function userInfo(url, authenticated) {
  return {
    username: url.searchParams.get("username") || "",
    message: "",
    auth: authenticated ? 1 : 0,
    status: authenticated ? "Active" : "Disabled",
    exp_date: null,
    is_trial: "0",
    active_cons: "0",
    created_at: String(Math.floor(Date.now() / 1000)),
    max_connections: "10",
    allowed_output_formats: ["m3u8", "ts"]
  };
}
function serverInfo(url) {
  const now = new Date();
  const parts = Object.fromEntries(new Intl.DateTimeFormat("en-GB", {
    timeZone: "Asia/Dhaka",
    year: "numeric", month: "2-digit", day: "2-digit",
    hour: "2-digit", minute: "2-digit", second: "2-digit",
    hourCycle: "h23"
  }).formatToParts(now).map(part => [part.type, part.value]));
  return {
    url: url.hostname,
    port: "443",
    https_port: "443",
    server_protocol: "https",
    protocol: "https",
    rtmp_port: "",
    timezone: "Asia/Dhaka",
    timestamp_now: Math.floor(now.getTime() / 1000),
    time_now: `${parts.year}-${parts.month}-${parts.day} ${parts.hour}:${parts.minute}:${parts.second}`
  };
}
function categories(streams) {
  return [...new Set(streams.map(s => s.group))]
    .map((name, i) => ({ category_id: String(i + 1), category_name: name, parent_id: 0 }));
}
function payload(s, origin) {
  return {
    num: Number(s.chno) || 0,
    name: s.name,
    stream_type: "live",
    stream_id: s.id,
    stream_icon: s.logo,
    epg_channel_id: s.tvgId,
    category_id: String(s.categoryId),
    tv_archive: 0,
    direct_source: s.url,
    stream_url: `${origin}/live/{username}/{password}/${s.id}.ts`,
    tvg_id: s.tvgId,
    tvg_name: s.name
  };
}
function wantsAllCategories(categoryId) {
  if (categoryId == null) return true;
  const v = String(categoryId).trim().toLowerCase();
  return v === "" || v === "0" || v === "-1" || v === "all" || v === "all_categories";
}

export default {
  async fetch(request, env) {
    const u = new URL(request.url);
    const p = u.pathname;
    const origin = u.origin;

    if (p === "/health") {
      try {
        const streams = await playlist(env);
        return json({ ok: true, playlist: env.PLAYLIST_URL || PLAYLIST_URL, streams: streams.length });
      } catch (e) {
        return json({ ok: false, error: String(e) }, 502);
      }
    }

    if (p === "/epg-health") {
      try {
        const r = await fetch(EPG_URL);
        const body = await r.text();
        return json({
          ok: r.ok,
          bytes: body.length,
          channels: (body.match(/<channel\b/g) || []).length,
          programmes: (body.match(/<programme\b/g) || []).length
        });
      } catch (e) {
        return json({ ok: false, error: String(e) }, 502);
      }
    }

    if (p === "/xmltv.php") {
      if (!auth(u, env)) return json({ user_info: userInfo(u, false) }, 401);
      const r = await fetch(EPG_URL);
      return xml(await r.text(), r.status);
    }

    if (p === "/player_api.php") {
      const info = { user_info: userInfo(u, auth(u, env)), server_info: serverInfo(u) };
      if (!auth(u, env)) return json(info);
      try {
        const streams = await playlist(env);
        const c = categories(streams);
        const categoryByName = new Map(c.map(x => [x.category_name, x.category_id]));
        streams.forEach(s => { s.categoryId = categoryByName.get(s.group) || "0"; });
        const action = (u.searchParams.get("action") || "").toLowerCase();

        if (action === "get_live_categories") return json(c);
        if (action === "get_live_streams") {
          const categoryId = u.searchParams.get("category_id");
          return json(streams
            .filter(s => wantsAllCategories(categoryId) || String(s.categoryId) === String(categoryId))
            .map(s => payload(s, origin)));
        }
        return json(info);
      } catch (e) {
        return json({ error: String(e) }, 502);
      }
    }

    if (p === "/get.php") {
      if (!auth(u, env)) return text("Unauthorized", 401);
      try {
        const streams = await playlist(env);
        const lines = ["#EXTM3U"];
        for (const s of streams) {
          lines.push(
            `#EXTINF:-1 tvg-id="${s.tvgId}" tvg-name="${s.name.replaceAll('"', "&quot;")}" tvg-logo="${s.logo}" group-title="${s.group}" tvg-chno="${s.chno}",${s.name}`,
            `${origin}/live/${encodeURIComponent(env.XTREAM_USERNAME)}/${encodeURIComponent(env.XTREAM_PASSWORD)}/${s.id}.ts`
          );
        }
        return text(lines.join("\n") + "\n", 200, "audio/x-mpegurl; charset=utf-8");
      } catch (e) {
        return text(String(e), 502);
      }
    }

    const m = p.match(/^\/live\/([^/]+)\/([^/]+)\/(\d+)\.(?:ts|m3u8)$/i);
    if (m) {
      const streamRequest = new URL(request.url);
      streamRequest.searchParams.set("username", decodeURIComponent(m[1]));
      streamRequest.searchParams.set("password", decodeURIComponent(m[2]));
      if (!auth(streamRequest, env)) return text("Unauthorized", 401);
      try {
        const s = (await playlist(env)).find(x => x.id === Number(m[3]));
        if (!s) return text("Stream not found", 404);
        return fetch(s.url, { headers: { "User-Agent": "BDIX-IPTV-Xtream/6.1" } });
      } catch (e) {
        return text(String(e), 502);
      }
    }

    return json({
      ok: true,
      service: "BDIX-IPTV Xtream Main",
      endpoints: ["player_api.php", "get.php", "xmltv.php", "live/<username>/<password>/<stream_id>.ts"]
    });
  }
};