// Independent external trigger for the GitHub "Discovery Schedule Watchdog".
//
// GitHub `schedule` events for this repository are delayed by hours (and sometimes
// dropped), and the watchdog's own checkpoints are schedule events too. This module
// lets the Worker's one-minute Cloudflare cron fire the watchdog through
// `workflow_dispatch` at fixed Bangladesh-time checkpoints instead.
//
// The Worker deliberately does NOT decide what is missing and never dispatches the
// playlist/EPG/Xtream workflows itself. The watchdog keeps all of that: Bangladesh
// calendar-date checks, required-job verification, per-workflow dispatch limits and
// the writer concurrency lock. Dispatching the watchdog is idempotent, so a
// duplicate or retried trigger can never create duplicate writer runs.

export const WATCHDOG_WORKFLOW_FILE = "discovery-schedule-watchdog.yml";
export const TIME_ZONE = "Asia/Dhaka";

// Bangladesh-local checkpoints. Each one sits just after a recovery threshold in
// scripts/discovery_schedule_guard.py (discovery 05:20/05:30, logo 05:45, stream
// health 05:55, maintenance 06:10, EPG and Xtream 06:45); the later ones retry
// failures and cover a late start.
export const CHECKPOINTS = ["05:25", "05:35", "05:50", "06:00", "06:15", "06:50", "07:30", "09:00", "12:00"];
export const CHECKPOINT_GRACE_MINUTES = 20;      // a checkpoint may still fire this long after its time
export const RECENT_SUCCESS_MINUTES = 5;         // skip if a watchdog run just succeeded
export const STUCK_CLAIM_MINUTES = 3;            // re-claim a trigger whose isolate died mid-dispatch
export const MAX_ATTEMPTS_PER_TRIGGER = 3;
export const MAX_CHECKPOINT_DISPATCHES_PER_DAY = 12;
export const MAX_MANUAL_DISPATCHES_PER_DAY = 10;
export const MODES = new Set(["off", "dry_run", "active"]);

const ACTIVE_STATUSES = new Set(["queued", "in_progress", "waiting", "pending", "requested"]);

export function triggerMode(env) {
  const mode = String((env && env.WATCHDOG_TRIGGER_MODE) || "off").toLowerCase();
  return MODES.has(mode) ? mode : "off";
}

function dhakaParts(date) {
  const parts = new Intl.DateTimeFormat("en-CA", {
    timeZone: TIME_ZONE, year: "numeric", month: "2-digit", day: "2-digit",
    hour: "2-digit", minute: "2-digit", hourCycle: "h23"
  }).formatToParts(date);
  return Object.fromEntries(parts.filter(p => p.type !== "literal").map(p => [p.type, p.value]));
}
export function dhakaDateOf(date = new Date()) {
  const p = dhakaParts(date);
  return p.year + "-" + p.month + "-" + p.day;
}
function minutesOf(hhmm) {
  const [h, m] = hhmm.split(":").map(Number);
  return h * 60 + m;
}
function shiftDate(date, days) {
  const [y, m, d] = date.split("-").map(Number);
  return new Date(Date.UTC(y, m - 1, d + days)).toISOString().slice(0, 10);
}

// The latest checkpoint at or before `now` (Bangladesh time) that is still inside
// its grace window, or null. Pure function: no I/O.
export function dueCheckpoint(now = new Date(), checkpoints = CHECKPOINTS, graceMinutes = CHECKPOINT_GRACE_MINUTES) {
  const p = dhakaParts(now);
  const date = p.year + "-" + p.month + "-" + p.day;
  const current = Number(p.hour) * 60 + Number(p.minute);
  let best = null;
  for (const time of checkpoints) {
    const at = minutesOf(time);
    if (at <= current && current - at < graceMinutes && (best === null || at > minutesOf(best))) best = time;
  }
  return best === null ? null : { key: date + "T" + best, date, time: best };
}

const SCHEMA = [
  "CREATE TABLE IF NOT EXISTS watchdog_triggers (" +
    "trigger_key TEXT PRIMARY KEY," +
    "business_date TEXT NOT NULL," +
    "source TEXT NOT NULL CHECK (source IN ('checkpoint','manual'))," +
    "state TEXT NOT NULL CHECK (state IN ('DISPATCHING','DISPATCHED','FAILED','SKIPPED_ACTIVE'," +
      "'SKIPPED_RECENT','SKIPPED_LIMIT','DRY_RUN'))," +
    "attempts INTEGER NOT NULL DEFAULT 0," +
    "retryable INTEGER NOT NULL DEFAULT 0," +
    "error_summary TEXT," +
    "created_at_utc TEXT NOT NULL," +
    "updated_at_utc TEXT NOT NULL)",
  "CREATE INDEX IF NOT EXISTS idx_watchdog_triggers_day ON watchdog_triggers (business_date, source, state)"
];
let schemaReady = new WeakSet();
export async function ensureWatchdogSchema(db) {
  if (schemaReady.has(db)) return;
  for (const sql of SCHEMA) await db.prepare(sql).run();
  schemaReady.add(db);
}
export function resetSchemaCacheForTests() { schemaReady = new WeakSet(); }

function sanitize(error) {
  return String((error && error.message) || error || "unknown error").replace(/\s+/g, " ").slice(0, 240);
}
// A dispatch is worth retrying only for transient failures (rate limit, 5xx, network).
export function isRetryableFailure(error) {
  const match = /HTTP (\d{3})/.exec(sanitize(error));
  if (!match) return true;
  const status = Number(match[1]);
  return status === 429 || status >= 500;
}

async function claim(db, key, date, source, nowIso) {
  const insert = await db.prepare(
    "INSERT OR IGNORE INTO watchdog_triggers " +
    "(trigger_key,business_date,source,state,attempts,retryable,created_at_utc,updated_at_utc) " +
    "VALUES (?,?,?,'DISPATCHING',1,0,?,?)").bind(key, date, source, nowIso, nowIso).run();
  if (insert.meta && insert.meta.changes === 1) return true;
  // Already seen. Re-claim only a transient failure, or a claim abandoned by a crashed isolate.
  const stuckBefore = new Date(Date.parse(nowIso) - STUCK_CLAIM_MINUTES * 60000).toISOString();
  const retry = await db.prepare(
    "UPDATE watchdog_triggers SET state='DISPATCHING',attempts=attempts+1,updated_at_utc=? " +
    "WHERE trigger_key=? AND attempts<? AND " +
    "((state='FAILED' AND retryable=1) OR (state='DISPATCHING' AND updated_at_utc<?))")
    .bind(nowIso, key, MAX_ATTEMPTS_PER_TRIGGER, stuckBefore).run();
  return !!(retry.meta && retry.meta.changes === 1);
}
async function finish(db, key, state, nowIso, details = {}) {
  await db.prepare("UPDATE watchdog_triggers SET state=?,retryable=?,error_summary=?,updated_at_utc=? WHERE trigger_key=?")
    .bind(state, details.retryable ? 1 : 0, details.error || null, nowIso, key).run();
}
async function dispatchedToday(db, date, source) {
  const row = await db.prepare(
    "SELECT COUNT(*) AS n FROM watchdog_triggers WHERE business_date=? AND source=? AND state='DISPATCHED'")
    .bind(date, source).first();
  return Number((row && row.n) || 0);
}

// Run one trigger decision. `deps.createClient(env)` returns the GitHub client from
// github-app.js; it is injectable so tests never touch the network.
export async function runWatchdogTrigger(env, deps, options = {}) {
  const now = options.now || new Date();
  const nowIso = now.toISOString();
  const source = options.source === "manual" ? "manual" : "checkpoint";
  const mode = triggerMode(env);
  if (mode === "off") return { action: "disabled", mode };

  let key, date;
  if (source === "manual") {
    date = dhakaDateOf(now);
    key = "manual:" + nowIso;
  } else {
    const checkpoint = dueCheckpoint(now);
    if (!checkpoint) return { action: "none", mode };
    ({ key, date } = checkpoint);
  }
  const dryRun = mode === "dry_run" || options.dryRun === true;

  const db = env.RELIABILITY_DB;
  if (!db) throw new Error("RELIABILITY_DB binding is required");
  await ensureWatchdogSchema(db);

  if (!(await claim(db, key, date, source, nowIso))) return { action: "already_handled", key, mode };

  try {
    const limit = source === "manual" ? MAX_MANUAL_DISPATCHES_PER_DAY : MAX_CHECKPOINT_DISPATCHES_PER_DAY;
    if ((await dispatchedToday(db, date, source)) >= limit) {
      await finish(db, key, "SKIPPED_LIMIT", nowIso, { error: "daily " + source + " dispatch limit reached" });
      return { action: "skipped_limit", key, mode };
    }
    if (dryRun) {
      await finish(db, key, "DRY_RUN", nowIso);
      return { action: "dry_run", key, mode: dryRun ? "dry_run" : mode };
    }

    const github = await deps.createClient(env);
    const from = shiftDate(date, -1), to = shiftDate(date, 1);
    const runs = await github.listWorkflowRuns(WATCHDOG_WORKFLOW_FILE, from, to);
    if (runs.some(run => ACTIVE_STATUSES.has(String(run.status || "").toLowerCase()))) {
      await finish(db, key, "SKIPPED_ACTIVE", nowIso);
      return { action: "skipped_active", key, mode };
    }
    if (source === "checkpoint") {
      const recent = runs.some(run => String(run.conclusion || "") === "success" &&
        Date.parse(run.created_at || 0) > Date.parse(nowIso) - RECENT_SUCCESS_MINUTES * 60000);
      if (recent) {
        await finish(db, key, "SKIPPED_RECENT", nowIso);
        return { action: "skipped_recent", key, mode };
      }
    }
    await github.dispatchWorkflow(WATCHDOG_WORKFLOW_FILE, "main");
    await finish(db, key, "DISPATCHED", nowIso);
    return { action: "dispatched", key, mode, workflow_file: WATCHDOG_WORKFLOW_FILE };
  } catch (error) {
    await finish(db, key, "FAILED", nowIso, { error: sanitize(error), retryable: isRetryableFailure(error) });
    return { action: "failed", key, mode, error: sanitize(error), retryable: isRetryableFailure(error) };
  }
}

export async function recentWatchdogTriggers(env, limit = 20) {
  const db = env.RELIABILITY_DB;
  if (!db) throw new Error("RELIABILITY_DB binding is required");
  await ensureWatchdogSchema(db);
  const rows = await db.prepare(
    "SELECT trigger_key,business_date,source,state,attempts,retryable,error_summary,updated_at_utc " +
    "FROM watchdog_triggers ORDER BY updated_at_utc DESC LIMIT ?").bind(Math.min(Math.max(limit, 1), 50)).all();
  return rows.results || [];
}
