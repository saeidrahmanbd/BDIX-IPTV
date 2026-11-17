import { createGitHubClient, verifyGitHubAppAccess } from "./github-app.js";

const TIME_ZONE = "Asia/Dhaka";
const LOOKBACK_DAYS = 3;
const LOOKAHEAD_DAYS = 2;
const SCAN_INTERVAL_MS = 5 * 60 * 1000;
const FAILURE_GRACE_MS = 15 * 60 * 1000;
const TERMINAL = new Set(["VERIFIED", "MANUAL_REVIEW", "SUPERSEDED"]);

function dateParts(date) {
  const parts = new Intl.DateTimeFormat("en-CA", {
    timeZone: TIME_ZONE, year: "numeric", month: "2-digit", day: "2-digit"
  }).formatToParts(date);
  return Object.fromEntries(parts.filter(p => p.type !== "literal").map(p => [p.type, p.value]));
}
export function dhakaDate(date = new Date()) {
  const p = dateParts(date);
  return p.year + "-" + p.month + "-" + p.day;
}
export function addCalendarDays(date, amount) {
  const [y, m, d] = date.split("-").map(Number);
  return new Date(Date.UTC(y, m - 1, d + amount)).toISOString().slice(0, 10);
}
export function expectedUtc(date, localTime) {
  const [y, m, d] = date.split("-").map(Number);
  const [hour, minute] = localTime.split(":").map(Number);
  return new Date(Date.UTC(y, m - 1, d, hour - 6, minute)).toISOString();
}
function keyFor(workflowId, date) { return workflowId + ":" + date; }

export function recoveryPlan(workflow, reason) {
  const policy = workflow.replay_policy || "manual_review";
  let recommendation = "manual_review";
  if (policy === "safe_latest_state_reconciliation") recommendation = "safe_latest_state_reconciliation";
  else if (policy === "policy_aware_reconciliation") recommendation = "policy_evaluation_required";
  else if (policy === "publish_only_after_last_known_good_validation") recommendation = "last_known_good_validation_required";
  else if (policy.startsWith("never_backfill")) recommendation = "never_backfill";
  return {
    state: recommendation === "safe_latest_state_reconciliation" ? "RETRY_WAIT" : "MANUAL_REVIEW",
    verification_status: "PENDING",
    last_error_code: reason || "workflow_run_not_found",
    last_error_summary: "No successful required job was confirmed. Recovery recommendation: " + recommendation + ".",
    recovery_recommendation: recommendation
  };
}

const VALID_EVENTS = new Set(["schedule", "workflow_dispatch", "workflow_run", "push"]);
export function evaluateWorkflowDay(workflow, date, runs, jobsByRun, now = new Date()) {
  const sameDay = (runs || []).filter(run => VALID_EVENTS.has(run.event) && run.created_at &&
    dhakaDate(new Date(run.created_at)) === date)
    .sort((a, b) => Date.parse(b.created_at) - Date.parse(a.created_at));
  let active = null, failed = null, skipped = null;
  for (const run of sameDay) {
    if (run.status !== "completed") { if (!active) active = run; continue; }
    if (run.conclusion !== "success") { if (!failed) failed = {run, job:null}; continue; }
    const jobs = jobsByRun[String(run.id)] || [];
    const job = jobs.find(item => item.name === workflow.required_job_id);
    if (job && job.conclusion === "success") {
      return {state:"VERIFIED",verification_status:"PASS",run,job,
        recovery_recommendation:"none",last_error_code:null,last_error_summary:null};
    }
    if (!skipped) skipped = {run,job};
  }
  if (active) return {state:"RUNNING",verification_status:"PENDING",run:active,
    job:null,recovery_recommendation:"monitor",last_error_code:null,last_error_summary:null};
  const dueAt = Date.parse(expectedUtc(date, workflow.expected_local_time)) + FAILURE_GRACE_MS;
  if (Date.parse(now) < dueAt) return {state:"EXPECTED",verification_status:"PENDING",run:null,job:null,
    recovery_recommendation:"wait_for_schedule",last_error_code:null,last_error_summary:null};
  const result = recoveryPlan(workflow, failed ? "workflow_failed" : skipped ? "required_job_skipped" : "workflow_run_not_found");
  return {...result,run:failed ? failed.run : skipped ? skipped.run : null,
    job:failed ? failed.job : skipped ? skipped.job : null};
}

async function ensureObligation(db, workflow, date, nowIso, version) {
  const key = keyFor(workflow.id, date);
  const sql = "INSERT OR IGNORE INTO reliability_executions " +
    "(execution_key,workflow_id,business_date,registry_version,expected_at_utc,state,created_at_utc,updated_at_utc) " +
    "VALUES (?,?,?,?,?,'EXPECTED',?,?)";
  const result = await db.prepare(sql).bind(key,workflow.id,date,version,
    expectedUtc(date,workflow.expected_local_time),nowIso,nowIso).run();
  if (result.meta && result.meta.changes > 0) {
    await db.prepare("INSERT INTO reliability_events (execution_key,event_type,event_source,event_at_utc,details_json) " +
      "VALUES (?,'OBLIGATION_CREATED','shadow_reconciler',?,?)")
      .bind(key,nowIso,JSON.stringify({workflow_id:workflow.id,business_date:date,registry_version:version})).run();
  }
  return !!(result.meta && result.meta.changes > 0);
}
async function event(db, key, type, nowIso, details) {
  await db.prepare("INSERT INTO reliability_events (execution_key,event_type,event_source,event_at_utc,details_json) " +
    "VALUES (?,?,'shadow_reconciler',?,?)")
    .bind(key,type,nowIso,JSON.stringify(details || {})).run();
}
async function lastScan(db,key) {
  return db.prepare("SELECT event_at_utc FROM reliability_events WHERE execution_key=? AND event_type='HISTORY_SCAN' " +
    "ORDER BY event_id DESC LIMIT 1").bind(key).first();
}
async function recordRun(db,key,run,job,nowIso) {
  const found = await db.prepare("SELECT event_id FROM reliability_events WHERE execution_key=? " +
    "AND event_type='GITHUB_RUN_OBSERVED' AND json_extract(details_json,'$.run_id')=? LIMIT 1")
    .bind(key,String(run.id)).first();
  if (!found) await event(db,key,"GITHUB_RUN_OBSERVED",nowIso,{
    run_id:String(run.id),run_attempt:run.run_attempt || 1,event:run.event,status:run.status,
    conclusion:run.conclusion || null,required_job:job ? job.name : null,
    required_job_conclusion:job ? job.conclusion : null,html_url:run.html_url || null
  });
}
async function saveEvaluation(db,row,result,nowIso) {
  const run = result.run, job = result.job;
  await db.prepare("UPDATE reliability_executions SET state=?,github_run_id=?,github_run_attempt=?," +
    "started_at_utc=?,completed_at_utc=?,verification_status=?,last_error_code=?,last_error_summary=?,updated_at_utc=? " +
    "WHERE execution_key=?")
    .bind(result.state,run ? String(run.id) : null,run ? (run.run_attempt || 1) : null,
      run ? (run.run_started_at || run.created_at || null) : null,
      run && run.status === "completed" ? (run.updated_at || null) : null,
      result.verification_status,result.last_error_code,result.last_error_summary,nowIso,row.execution_key).run();
  if (run) await recordRun(db,row.execution_key,run,job,nowIso);
  await event(db,row.execution_key,"HISTORY_EVALUATED",nowIso,{
    state:result.state,recovery_recommendation:result.recovery_recommendation,
    run_id:run ? String(run.id) : null,required_job:job ? job.name : null,
    required_job_conclusion:job ? job.conclusion : null
  });
}

export function canDispatchSameDay(env, workflow, businessDate, now = new Date()) {
  if (env.MODE !== "active" || businessDate !== dhakaDate(now)) return false;
  return ["safe_latest_state_reconciliation","policy_aware_reconciliation",
    "publish_only_after_last_known_good_validation"].includes(workflow.replay_policy);
}
async function dispatchOnce(env,db,github,row,workflow,nowIso) {
  if (!canDispatchSameDay(env,workflow,row.business_date,new Date(nowIso))) return false;
  const changed = await db.prepare("UPDATE reliability_executions SET state='DISPATCHING'," +
    "dispatch_attempts=dispatch_attempts+1,updated_at_utc=? " +
    "WHERE execution_key=? AND state IN ('EXPECTED','RETRY_WAIT') AND dispatch_attempts=0")
    .bind(nowIso,row.execution_key).run();
  if (!changed.meta || changed.meta.changes !== 1) return false;
  await db.prepare("INSERT OR IGNORE INTO reliability_attempts " +
    "(workflow_id,business_date,attempt_number,trigger_source,dispatch_requested_at_utc,run_status," +
    "verification_status,created_at_utc,updated_at_utc) " +
    "VALUES (?,?,1,'cloudflare_cron',?,'REQUESTED','PENDING',?,?)")
    .bind(workflow.id,row.business_date,nowIso,nowIso,nowIso).run();
  try {
    const result = await github.dispatchWorkflow(workflow.workflow_file,"main");
    await db.prepare("UPDATE reliability_executions SET state='DISPATCHED',updated_at_utc=? " +
      "WHERE execution_key=? AND state='DISPATCHING'").bind(nowIso,row.execution_key).run();
    await event(db,row.execution_key,"WORKFLOW_DISPATCH_ACCEPTED",nowIso,result);
    return true;
  } catch (error) {
    const summary = String(error.message || error).slice(0,240);
    await db.prepare("UPDATE reliability_executions SET state='MANUAL_REVIEW',last_error_code='dispatch_failed'," +
      "last_error_summary=?,updated_at_utc=? WHERE execution_key=?")
      .bind(summary,nowIso,row.execution_key).run();
    await db.prepare("UPDATE reliability_attempts SET run_status='UNKNOWN',error_code='dispatch_failed'," +
      "error_summary=?,updated_at_utc=? WHERE workflow_id=? AND business_date=? AND attempt_number=1")
      .bind(summary,nowIso,workflow.id,row.business_date).run();
    await event(db,row.execution_key,"WORKFLOW_DISPATCH_FAILED",nowIso,{error:summary});
    return false;
  }
}

export async function reconcile(env, now = new Date()) {
  const db = env.RELIABILITY_DB;
  if (!db) throw new Error("RELIABILITY_DB binding is required");
  if (!env.REGISTRY_JSON) throw new Error("REGISTRY_JSON binding is required");
  const registry = typeof env.REGISTRY_JSON === "string" ? JSON.parse(env.REGISTRY_JSON) : env.REGISTRY_JSON;
  if (!Array.isArray(registry.workflows) || !registry.registry_version) throw new Error("Invalid reliability registry");
  const nowIso = now.toISOString(), today = dhakaDate(now);
  let obligationsCreated = 0;
  for (let offset=-LOOKBACK_DAYS; offset<=LOOKAHEAD_DAYS; offset++) {
    const date = addCalendarDays(today,offset);
    for (const workflow of registry.workflows) {
      if (await ensureObligation(db,workflow,date,nowIso,registry.registry_version)) obligationsCreated++;
    }
  }
  const low = addCalendarDays(today,-LOOKBACK_DAYS), high = addCalendarDays(today,LOOKAHEAD_DAYS);
  const selected = await db.prepare("SELECT * FROM reliability_executions WHERE business_date>=? AND business_date<=? " +
    "ORDER BY business_date,workflow_id").bind(low,high).all();
  const rows = selected.results || [];
  const github = await createGitHubClient(env);
  let workflowsScanned=0,runsObserved=0,verified=0,running=0,needsReview=0,dispatched=0;
  for (const workflow of registry.workflows) {
    const workRows = rows.filter(row => row.workflow_id === workflow.id);
    const dueRows = workRows.filter(row => Date.parse(row.expected_at_utc)+FAILURE_GRACE_MS <= Date.parse(nowIso) &&
      !TERMINAL.has(row.state));
    if (!dueRows.length) continue;
    const todayKey = keyFor(workflow.id,today);
    const previous = await lastScan(db,todayKey);
    if (previous && Date.parse(nowIso)-Date.parse(previous.event_at_utc)<SCAN_INTERVAL_MS) continue;
    const from = addCalendarDays(today,-LOOKBACK_DAYS-1), to = addCalendarDays(today,LOOKAHEAD_DAYS);
    const runs = await github.listWorkflowRuns(workflow.workflow_file,from,to);
    await event(db,todayKey,"HISTORY_SCAN",nowIso,{workflow_id:workflow.id,from_date:from,to_date:to,runs_returned:runs.length});
    workflowsScanned++;
    for (const row of dueRows) {
      const dayRuns = runs.filter(run => run.created_at && dhakaDate(new Date(run.created_at)) === row.business_date);
      const jobs = {};
      for (const run of dayRuns.slice(0,12)) {
        if (run.status === "completed" && run.conclusion === "success") {
          jobs[String(run.id)] = await github.listWorkflowJobs(run.id);
        }
      }
      let result = evaluateWorkflowDay(workflow,row.business_date,dayRuns,jobs,now);
      if (row.business_date !== today && result.state === "RETRY_WAIT") {
        result = {...result,state:"MANUAL_REVIEW",recovery_recommendation:"historical_replay_not_supported",
          last_error_summary:"Past Bangladesh business dates cannot be replayed safely by the current workflow inputs."};
      }
      await saveEvaluation(db,row,result,nowIso);
      runsObserved += dayRuns.length;
      if (result.state === "VERIFIED") verified++;
      else if (result.state === "RUNNING") running++;
      else if (result.state === "MANUAL_REVIEW" || result.state === "RETRY_WAIT") needsReview++;
      if (dayRuns.length === 0 && row.business_date === today &&
          await dispatchOnce(env,db,github,row,workflow,nowIso)) dispatched++;
    }
  }
  return {ok:true,mode:env.MODE === "active" ? "active" : "shadow",business_date:today,
    obligations_created:obligationsCreated,workflows_scanned:workflowsScanned,runs_observed:runsObserved,
    verified,running,needs_review:needsReview,dispatched};
}

function constantTimeEqual(a,b) {
  const left=new TextEncoder().encode(a), right=new TextEncoder().encode(b);
  let diff=left.length ^ right.length;
  for (let i=0;i<Math.max(left.length,right.length);i++) diff |= (left[i] || 0) ^ (right[i] || 0);
  return diff === 0;
}
function authorized(request,env) {
  if (!env.RECONCILE_BEARER_TOKEN) return false;
  const header=request.headers.get("Authorization") || "";
  return constantTimeEqual(header.startsWith("Bearer ") ? header.slice(7) : "",env.RECONCILE_BEARER_TOKEN);
}
export default {
  async fetch(request,env) {
    const url=new URL(request.url);
    if (request.method === "GET" && url.pathname === "/healthz")
      return Response.json({ok:true,mode:env.MODE === "active" ? "active" : "shadow"});
    if (request.method !== "POST" || !["/reconcile","/github-check"].includes(url.pathname))
      return new Response("Not found",{status:404});
    if (!env.RECONCILE_BEARER_TOKEN) return new Response("Protected endpoint is not configured",{status:503});
    if (!authorized(request,env)) return new Response("Unauthorized",{status:401});
    try {
      if (url.pathname === "/github-check") {
        const result=await verifyGitHubAppAccess(env);
        return Response.json({...result,mode:env.MODE === "active" ? "active" : "shadow",dispatched:0});
      }
      return Response.json(await reconcile(env));
    } catch (error) {
      return Response.json({error:url.pathname === "/github-check" ? "github_authentication_failed" : "reconciliation_failed",
        message:String(error.message || error).slice(0,240)},{status:503});
    }
  },
  async scheduled(_controller,env,ctx) { ctx.waitUntil(reconcile(env)); }
};
