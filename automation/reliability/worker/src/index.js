const TIME_ZONE = "Asia/Dhaka";
const LOOKAHEAD_DAYS = 2;

function dateParts(date) {
  const parts = new Intl.DateTimeFormat("en-CA", {
    timeZone: TIME_ZONE, year: "numeric", month: "2-digit", day: "2-digit"
  }).formatToParts(date);
  return Object.fromEntries(parts.filter(p => p.type !== "literal").map(p => [p.type, p.value]));
}

export function dhakaDate(date = new Date()) {
  const p = dateParts(date);
  return `${p.year}-${p.month}-${p.day}`;
}

export function addCalendarDays(isoDate, amount) {
  const [y, m, d] = isoDate.split("-").map(Number);
  const next = new Date(Date.UTC(y, m - 1, d + amount));
  return next.toISOString().slice(0, 10);
}

export function expectedUtc(date, localTime) {
  const [y, m, d] = date.split("-").map(Number);
  const [hour, minute] = localTime.split(":").map(Number);
  // Asia/Dhaka is UTC+06:00; it has no daylight-saving transition.
  return new Date(Date.UTC(y, m - 1, d, hour - 6, minute)).toISOString();
}

function executionKey(workflowId, businessDate) {
  return `${workflowId}:${businessDate}`;
}

async function ensureObligation(db, workflow, businessDate, nowIso, registryVersion) {
  const key = executionKey(workflow.id, businessDate);
  const inserted = await db.prepare(`
    INSERT OR IGNORE INTO reliability_executions (
      execution_key, workflow_id, business_date, registry_version,
      expected_at_utc, state, created_at_utc, updated_at_utc
    ) VALUES (?, ?, ?, ?, ?, 'EXPECTED', ?, ?)
  `).bind(key, workflow.id, businessDate, registryVersion,
    expectedUtc(businessDate, workflow.expected_local_time), nowIso, nowIso).run();

  if (inserted.meta?.changes > 0) {
    await db.prepare(`
      INSERT INTO reliability_events (
        execution_key, event_type, event_source, event_at_utc, details_json
      ) VALUES (?, 'OBLIGATION_CREATED', 'shadow_reconciler', ?, ?)
    `).bind(key, nowIso, JSON.stringify({
      workflow_id: workflow.id, business_date: businessDate,
      mode: "shadow", registry_version: registryVersion
    })).run();
  }
  return inserted.meta?.changes > 0;
}

export async function reconcile(env, now = new Date()) {
  if (!env.RELIABILITY_DB) throw new Error("RELIABILITY_DB binding is required");
  if (!env.REGISTRY_JSON) throw new Error("REGISTRY_JSON binding is required");
  const registry = typeof env.REGISTRY_JSON === "string"
    ? JSON.parse(env.REGISTRY_JSON) : env.REGISTRY_JSON;
  if (!Array.isArray(registry.workflows) || !registry.registry_version) {
    throw new Error("Invalid reliability registry");
  }

  const nowIso = now.toISOString();
  const today = dhakaDate(now);
  let created = 0;
  let examined = 0;
  for (let offset = 0; offset <= LOOKAHEAD_DAYS; offset += 1) {
    const businessDate = addCalendarDays(today, offset);
    for (const workflow of registry.workflows) {
      examined += 1;
      if (await ensureObligation(env.RELIABILITY_DB, workflow, businessDate,
        nowIso, registry.registry_version)) created += 1;
    }
  }

  // Shadow mode deliberately does not dispatch GitHub workflows or alter production.
  if (env.HEALTHCHECKS_PING_URL) {
    const response = await fetch(env.HEALTHCHECKS_PING_URL, { method: "GET" });
    if (!response.ok) throw new Error(`Healthchecks heartbeat failed: HTTP ${response.status}`);
  }
  return { mode: "shadow", business_date: today, examined, created, dispatched: 0 };
}

function constantTimeEqual(a, b) {
  const left = new TextEncoder().encode(a);
  const right = new TextEncoder().encode(b);
  let diff = left.length ^ right.length;
  const n = Math.max(left.length, right.length);
  for (let i = 0; i < n; i += 1) diff |= (left[i] || 0) ^ (right[i] || 0);
  return diff === 0;
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (request.method === "GET" && url.pathname === "/healthz") {
      return Response.json({ ok: true, mode: "shadow" });
    }
    if (request.method !== "POST" || url.pathname !== "/reconcile") {
      return new Response("Not found", { status: 404 });
    }
    if (!env.RECONCILE_BEARER_TOKEN) {
      return new Response("Reconciliation endpoint is not configured", { status: 503 });
    }
    const authorization = request.headers.get("Authorization") || "";
    const supplied = authorization.startsWith("Bearer ") ? authorization.slice(7) : "";
    if (!constantTimeEqual(supplied, env.RECONCILE_BEARER_TOKEN)) {
      return new Response("Unauthorized", { status: 401 });
    }
    try {
      const result = await reconcile(env);
      return Response.json(result);
    } catch (error) {
      return Response.json({ error: "reconciliation_failed", message: String(error.message || error) }, { status: 503 });
    }
  },

  async scheduled(_controller, env, ctx) {
    ctx.waitUntil(reconcile(env));
  }
};
