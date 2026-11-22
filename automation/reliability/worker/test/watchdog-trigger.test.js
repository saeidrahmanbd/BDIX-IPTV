import test from "node:test";
import assert from "node:assert/strict";
import { DatabaseSync } from "node:sqlite";
import worker from "../src/index.js";
import {
  CHECKPOINTS, WATCHDOG_WORKFLOW_FILE, dueCheckpoint, runWatchdogTrigger, triggerMode, isRetryableFailure,
  resetSchemaCacheForTests, recentWatchdogTriggers, MAX_CHECKPOINT_DISPATCHES_PER_DAY, MAX_MANUAL_DISPATCHES_PER_DAY
} from "../src/watchdog-trigger.js";

// A D1-shaped wrapper over real SQLite so the claim/retry SQL is genuinely executed.
function fakeD1() {
  const sqlite = new DatabaseSync(":memory:");
  return {
    sqlite,
    prepare(sql) {
      return { bind(...args) {
        return {
          async run() { const r = sqlite.prepare(sql).run(...args); return { meta: { changes: Number(r.changes) } }; },
          async first() { return sqlite.prepare(sql).get(...args) || null; },
          async all() { return { results: sqlite.prepare(sql).all(...args) }; }
        };
      }, async run() { const r = sqlite.prepare(sql).run(); return { meta: { changes: Number(r.changes) } }; } };
    }
  };
}
function setup(opts = {}) {
  resetSchemaCacheForTests();
  const db = fakeD1();
  const calls = { dispatch: [], list: 0, clients: 0 };
  const state = { runs: opts.runs || [], dispatchError: opts.dispatchError || null };
  const deps = { async createClient() {
    calls.clients++;
    return {
      async listWorkflowRuns(file) { calls.list++; assert.equal(file, WATCHDOG_WORKFLOW_FILE); return state.runs; },
      async dispatchWorkflow(file, ref) {
        calls.dispatch.push([file, ref]);
        if (state.dispatchError) throw new Error(state.dispatchError);
        return { accepted: true };
      }
    };
  } };
  const env = { RELIABILITY_DB: db, WATCHDOG_TRIGGER_MODE: opts.mode || "active" };
  return { db, calls, state, deps, env };
}
const at = (iso) => new Date(iso);                        // 05:25 Dhaka == 23:25Z the day before
const T0525 = "2026-11-21T23:25:00Z";                     // 2026-11-22 05:25 Dhaka
const rows = (db) => db.sqlite.prepare("SELECT trigger_key,source,state,attempts,retryable FROM watchdog_triggers ORDER BY trigger_key").all();

test("checkpoints are Bangladesh local times, and UTC midnight does not shift the date", () => {
  assert.deepEqual(dueCheckpoint(at(T0525)), { key: "2026-11-22T05:25", date: "2026-11-22", time: "05:25" });
  assert.equal(dueCheckpoint(at("2026-11-21T23:24:59Z")), null);            // 05:24:59
  assert.equal(dueCheckpoint(at("2026-11-21T18:00:00Z")), null);            // 00:00 Dhaka
});
test("a checkpoint stays claimable for its grace window then expires", () => {
  assert.equal(dueCheckpoint(at("2026-11-21T23:44:00Z")).time, "05:35");   // 05:44 -> latest due is 05:35
  assert.equal(dueCheckpoint(at("2026-11-21T23:44:00Z")).key, "2026-11-22T05:35");
  assert.equal(dueCheckpoint(at("2026-11-22T00:11:00Z")).time, "06:00");    // 06:11 is still inside 06:00's grace
  assert.equal(dueCheckpoint(at("2026-11-22T01:12:00Z")), null);            // 07:12: 06:50 expired, 07:30 not yet
});
test("every checkpoint is unique, sorted and inside the Bangladesh morning-to-noon recovery window", () => {
  assert.deepEqual([...CHECKPOINTS].sort(), CHECKPOINTS);
  assert.equal(new Set(CHECKPOINTS).size, CHECKPOINTS.length);
  assert.ok(CHECKPOINTS[0] >= "05:20" && CHECKPOINTS.at(-1) <= "13:00");
});
test("mode defaults to off and rejects unknown values", () => {
  assert.equal(triggerMode({}), "off");
  assert.equal(triggerMode({ WATCHDOG_TRIGGER_MODE: "ACTIVE" }), "active");
  assert.equal(triggerMode({ WATCHDOG_TRIGGER_MODE: "yes" }), "off");
});
test("off mode never touches D1 or GitHub", async () => {
  const s = setup({ mode: "off" });
  assert.equal((await runWatchdogTrigger(s.env, s.deps, { now: at(T0525) })).action, "disabled");
  assert.equal(s.calls.clients, 0);
});
test("outside a checkpoint nothing happens and no GitHub call is made", async () => {
  const s = setup();
  assert.equal((await runWatchdogTrigger(s.env, s.deps, { now: at("2026-11-22T02:00:00Z") })).action, "none");
  assert.equal(s.calls.clients, 0);
});
test("each checkpoint dispatches the watchdog exactly once even if the cron fires every minute", async () => {
  const s = setup();
  const results = [];
  for (const minute of ["25", "26", "27", "28"]) results.push((await runWatchdogTrigger(s.env, s.deps, { now: at("2026-11-21T23:" + minute + ":10Z") })).action);
  assert.deepEqual(results, ["dispatched", "already_handled", "already_handled", "already_handled"]);
  assert.deepEqual(s.calls.dispatch, [[WATCHDOG_WORKFLOW_FILE, "main"]]);
});
test("concurrent isolates cannot both claim one checkpoint", async () => {
  const s = setup();
  const both = await Promise.all([
    runWatchdogTrigger(s.env, s.deps, { now: at(T0525) }), runWatchdogTrigger(s.env, s.deps, { now: at(T0525) })]);
  assert.deepEqual(both.map(r => r.action).sort(), ["already_handled", "dispatched"]);
  assert.equal(s.calls.dispatch.length, 1);
});
test("a later checkpoint dispatches again", async () => {
  const s = setup();
  await runWatchdogTrigger(s.env, s.deps, { now: at(T0525) });
  const second = await runWatchdogTrigger(s.env, s.deps, { now: at("2026-11-21T23:35:30Z") });
  assert.equal(second.action, "dispatched");
  assert.equal(s.calls.dispatch.length, 2);
});
test("only the watchdog is ever dispatched, never a playlist, EPG or Xtream workflow", async () => {
  const s = setup();
  for (const t of ["23:25", "23:35", "23:50"]) await runWatchdogTrigger(s.env, s.deps, { now: at("2026-11-21T" + t + ":05Z") });
  assert.ok(s.calls.dispatch.length >= 3);
  for (const [file, ref] of s.calls.dispatch) { assert.equal(file, "discovery-schedule-watchdog.yml"); assert.equal(ref, "main"); }
});
test("an active watchdog run suppresses the dispatch and consumes that checkpoint", async () => {
  const s = setup({ runs: [{ id: 1, status: "in_progress", created_at: "2026-11-22T00:00:00Z" }] });
  assert.equal((await runWatchdogTrigger(s.env, s.deps, { now: at(T0525) })).action, "skipped_active");
  assert.equal(s.calls.dispatch.length, 0);
  assert.equal((await runWatchdogTrigger(s.env, s.deps, { now: at("2026-11-21T23:26:00Z") })).action, "already_handled");
});
test("a watchdog run that just succeeded suppresses a checkpoint dispatch", async () => {
  const s = setup({ runs: [{ id: 2, status: "completed", conclusion: "success", created_at: "2026-11-21T23:22:00Z" }] });
  assert.equal((await runWatchdogTrigger(s.env, s.deps, { now: at(T0525) })).action, "skipped_recent");
  assert.equal(s.calls.dispatch.length, 0);
});
test("an old or failed watchdog run does not suppress dispatch", async () => {
  const old = setup({ runs: [{ id: 3, status: "completed", conclusion: "success", created_at: "2026-11-21T22:00:00Z" }] });
  assert.equal((await runWatchdogTrigger(old.env, old.deps, { now: at(T0525) })).action, "dispatched");
  const failed = setup({ runs: [{ id: 4, status: "completed", conclusion: "failure", created_at: "2026-11-21T23:24:00Z" }] });
  assert.equal((await runWatchdogTrigger(failed.env, failed.deps, { now: at(T0525) })).action, "dispatched");
});
test("transient failures retry on later minutes up to the attempt cap", async () => {
  const s = setup({ dispatchError: "GitHub workflow dispatch failed (HTTP 503)" });
  const actions = [];
  for (const m of ["25", "26", "27", "28", "29"]) actions.push((await runWatchdogTrigger(s.env, s.deps, { now: at("2026-11-21T23:" + m + ":10Z") })).action);
  assert.deepEqual(actions, ["failed", "failed", "failed", "already_handled", "already_handled"]);
  assert.equal(s.calls.dispatch.length, 3);
  assert.equal(rows(s.db)[0].attempts, 3);
});
test("a transient failure that later succeeds stops retrying", async () => {
  const s = setup({ dispatchError: "GitHub workflow dispatch failed (HTTP 502)" });
  await runWatchdogTrigger(s.env, s.deps, { now: at(T0525) });
  s.state.dispatchError = null;
  assert.equal((await runWatchdogTrigger(s.env, s.deps, { now: at("2026-11-21T23:26:10Z") })).action, "dispatched");
  assert.equal((await runWatchdogTrigger(s.env, s.deps, { now: at("2026-11-21T23:27:10Z") })).action, "already_handled");
  assert.equal(rows(s.db)[0].state, "DISPATCHED");
});
test("permission and configuration failures are not retried blindly", async () => {
  for (const status of [401, 403, 404, 422]) {
    const s = setup({ dispatchError: "GitHub workflow dispatch failed (HTTP " + status + ")" });
    assert.equal((await runWatchdogTrigger(s.env, s.deps, { now: at(T0525) })).action, "failed");
    assert.equal((await runWatchdogTrigger(s.env, s.deps, { now: at("2026-11-21T23:26:10Z") })).action, "already_handled");
    assert.equal(s.calls.dispatch.length, 1);
    assert.equal(rows(s.db)[0].retryable, 0);
  }
  assert.equal(isRetryableFailure(new Error("fetch failed")), true);
  assert.equal(isRetryableFailure(new Error("GitHub API request failed (HTTP 429)")), true);
});
test("a claim abandoned by a crashed isolate is re-claimed only after the stuck window", async () => {
  const s = setup();
  await runWatchdogTrigger(s.env, s.deps, { now: at(T0525) });
  s.db.sqlite.prepare("UPDATE watchdog_triggers SET state='DISPATCHING', updated_at_utc=?").run("2026-11-21T23:25:00.000Z");
  assert.equal((await runWatchdogTrigger(s.env, s.deps, { now: at("2026-11-21T23:26:00Z") })).action, "already_handled");
  assert.equal((await runWatchdogTrigger(s.env, s.deps, { now: at("2026-11-21T23:29:00Z") })).action, "dispatched");
});
test("the daily checkpoint dispatch cap is enforced", async () => {
  const s = setup();
  await s.db.prepare("CREATE TABLE IF NOT EXISTS watchdog_triggers (trigger_key TEXT PRIMARY KEY,business_date TEXT NOT NULL,source TEXT NOT NULL CHECK (source IN ('checkpoint','manual')),state TEXT NOT NULL CHECK (state IN ('DISPATCHING','DISPATCHED','FAILED','SKIPPED_ACTIVE','SKIPPED_RECENT','SKIPPED_LIMIT','DRY_RUN')),attempts INTEGER NOT NULL DEFAULT 0,retryable INTEGER NOT NULL DEFAULT 0,error_summary TEXT,created_at_utc TEXT NOT NULL,updated_at_utc TEXT NOT NULL)").run();
  for (let i = 0; i < MAX_CHECKPOINT_DISPATCHES_PER_DAY; i++)
    s.db.sqlite.prepare("INSERT INTO watchdog_triggers VALUES (?,?,?,?,?,?,?,?,?)").run("2026-11-22T00:0" + (i % 10) + "-x" + i, "2026-11-22", "checkpoint", "DISPATCHED", 1, 0, null, "t", "t");
  assert.equal((await runWatchdogTrigger(s.env, s.deps, { now: at(T0525) })).action, "skipped_limit");
  assert.equal(s.calls.dispatch.length, 0);
});
test("dry_run mode records the decision but never reaches GitHub", async () => {
  const s = setup({ mode: "dry_run" });
  assert.equal((await runWatchdogTrigger(s.env, s.deps, { now: at(T0525) })).action, "dry_run");
  assert.equal(s.calls.clients, 0);
  assert.equal(rows(s.db)[0].state, "DRY_RUN");
});
test("manual recovery dispatches at any time, bypassing checkpoints", async () => {
  const s = setup();
  const result = await runWatchdogTrigger(s.env, s.deps, { now: at("2026-11-22T03:17:00Z"), source: "manual" });
  assert.equal(result.action, "dispatched");
  assert.equal(rows(s.db)[0].source, "manual");
});
test("manual recovery honours dry_run, an active watchdog and its own daily cap", async () => {
  const s = setup();
  assert.equal((await runWatchdogTrigger(s.env, s.deps, { now: at("2026-11-22T03:17:00Z"), source: "manual", dryRun: true })).action, "dry_run");
  assert.equal(s.calls.dispatch.length, 0);
  const busy = setup({ runs: [{ id: 9, status: "queued", created_at: "2026-11-22T03:00:00Z" }] });
  assert.equal((await runWatchdogTrigger(busy.env, busy.deps, { now: at("2026-11-22T03:17:00Z"), source: "manual" })).action, "skipped_active");
  const capped = setup();
  const results = [];
  for (let i = 0; i < MAX_MANUAL_DISPATCHES_PER_DAY + 2; i++)
    results.push((await runWatchdogTrigger(capped.env, capped.deps, { now: at("2026-11-22T03:" + String(10 + i).padStart(2, "0") + ":00Z"), source: "manual" })).action);
  assert.equal(results.filter(a => a === "dispatched").length, MAX_MANUAL_DISPATCHES_PER_DAY);
  assert.equal(results.at(-1), "skipped_limit");
});
test("manual dispatches do not consume the checkpoint budget", async () => {
  const s = setup();
  await runWatchdogTrigger(s.env, s.deps, { now: at("2026-11-22T03:17:00Z"), source: "manual" });
  assert.equal((await runWatchdogTrigger(s.env, s.deps, { now: at(T0525) })).action, "dispatched");
});
test("recent triggers can be listed without exposing anything sensitive", async () => {
  const s = setup();
  await runWatchdogTrigger(s.env, s.deps, { now: at(T0525) });
  const list = await recentWatchdogTriggers(s.env);
  assert.equal(list.length, 1);
  assert.deepEqual(Object.keys(list[0]).sort(), ["attempts","business_date","error_summary","retryable","source","state","trigger_key","updated_at_utc"]);
});

// --- HTTP surface ---------------------------------------------------------
const req = (path, headers = {}, method = "POST") => new Request("https://worker.example" + path, { method, headers });
test("watchdog endpoints are bearer-protected and fail closed when no token is configured", async () => {
  const s = setup();
  for (const path of ["/watchdog-dispatch", "/watchdog-status"]) {
    assert.equal((await worker.fetch(req(path), { ...s.env })).status, 503);
    assert.equal((await worker.fetch(req(path), { ...s.env, RECONCILE_BEARER_TOKEN: "right" })).status, 401);
    assert.equal((await worker.fetch(req(path, { Authorization: "Bearer wrong" }), { ...s.env, RECONCILE_BEARER_TOKEN: "right" })).status, 401);
  }
  assert.equal(s.calls.clients, 0);
});
test("watchdog endpoints reject GET and healthz reports the trigger mode only", async () => {
  const s = setup();
  assert.equal((await worker.fetch(req("/watchdog-dispatch", {}, "GET"), s.env)).status, 404);
  const health = await (await worker.fetch(req("/healthz", {}, "GET"), s.env)).json();
  assert.deepEqual(health, { ok: true, mode: "shadow", watchdog_trigger: "active" });
});
test("manual dispatch endpoint never leaks credentials when GitHub auth fails", async () => {
  const s = setup();
  const env = { ...s.env, RECONCILE_BEARER_TOKEN: "bearer-secret-value", GITHUB_APP_ID: "1", GITHUB_INSTALLATION_ID: "2",
    GITHUB_APP_PRIVATE_KEY: "-----BEGIN RSA PRIVATE KEY-----\nSECRETKEYBODY!!\n-----END RSA PRIVATE KEY-----" };
  const response = await worker.fetch(req("/watchdog-dispatch", { Authorization: "Bearer bearer-secret-value" }), env);
  const text = await response.text();
  assert.equal(response.status, 503);
  assert.ok(!text.includes("bearer-secret-value"));
  assert.ok(!text.includes("SECRETKEYBODY"));
  assert.ok(!text.includes("ghs_"));
  const stored = JSON.stringify(rows(s.db)) + JSON.stringify(s.db.sqlite.prepare("SELECT error_summary FROM watchdog_triggers").all());
  assert.ok(!stored.includes("SECRETKEYBODY") && !stored.includes("bearer-secret-value"));
});
test("manual dry run through the endpoint records without needing GitHub credentials", async () => {
  const s = setup();
  const env = { ...s.env, RECONCILE_BEARER_TOKEN: "right" };
  const response = await worker.fetch(req("/watchdog-dispatch?dry_run=1", { Authorization: "Bearer right" }), env);
  assert.equal(response.status, 200);
  assert.equal((await response.json()).action, "dry_run");
  const status = await (await worker.fetch(req("/watchdog-status", { Authorization: "Bearer right" }), env)).json();
  assert.equal(status.recent[0].state, "DRY_RUN");
});
test("scheduled handler survives total failure of both jobs and still resolves", async () => {
  const s = setup();
  let pending;
  await worker.scheduled({}, { ...s.env }, { waitUntil: p => { pending = p; } });
  const settled = await pending;
  assert.equal(settled.length, 2);
  assert.ok(settled.every(r => r.status === "fulfilled" || r.status === "rejected"));
});
