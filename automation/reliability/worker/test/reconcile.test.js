import test from "node:test";
import assert from "node:assert/strict";
import {dhakaDate,addCalendarDays,expectedUtc,evaluateWorkflowDay,recoveryPlan,canDispatchSameDay} from "../src/index.js";
test("Dhaka local date is stable across UTC midnight",()=>{
  assert.equal(dhakaDate(new Date("2026-11-15T18:30:00Z")),"2026-11-16");
});
test("calendar date addition crosses year boundaries",()=>{
  assert.equal(addCalendarDays("2026-12-31",1),"2027-01-01");
});
test("Bangladesh local schedule converts to UTC",()=>{
  assert.equal(expectedUtc("2026-11-16","05:00"),"2026-11-15T23:00:00.000Z");
});
const base={id:"epg_refresh",expected_local_time:"06:10",required_job_id:"refresh",
  replay_policy:"publish_only_after_last_known_good_validation"};
test("only workflow and required-job success is verified",()=>{
  const run={id:1,event:"schedule",created_at:"2026-11-16T00:10:00Z",status:"completed",conclusion:"success"};
  const result=evaluateWorkflowDay(base,"2026-11-16",[run],{"1":[{name:"refresh",conclusion:"success"}]},
    new Date("2026-11-16T02:00:00Z"));
  assert.equal(result.state,"VERIFIED"); assert.equal(result.verification_status,"PASS");
});
test("skipped critical job is not counted as success",()=>{
  const run={id:2,event:"schedule",created_at:"2026-11-16T00:10:00Z",status:"completed",conclusion:"success"};
  const result=evaluateWorkflowDay(base,"2026-11-16",[run],{"2":[{name:"refresh",conclusion:"skipped"}]},
    new Date("2026-11-16T02:00:00Z"));
  assert.equal(result.state,"MANUAL_REVIEW"); assert.equal(result.last_error_code,"required_job_skipped");
});
test("in-progress workflow is monitored",()=>{
  const run={id:3,event:"workflow_run",created_at:"2026-11-16T00:10:00Z",status:"in_progress"};
  assert.equal(evaluateWorkflowDay(base,"2026-11-16",[run],{},new Date("2026-11-16T02:00:00Z")).state,"RUNNING");
});
test("new channel discovery misses require manual review",()=>{
  const r=recoveryPlan({...base,replay_policy:"manual_review_for_missed_business_date"});
  assert.equal(r.state,"MANUAL_REVIEW"); assert.equal(r.recovery_recommendation,"manual_review");
});
test("stream health is never automatically backfilled",()=>{
  const r=recoveryPlan({...base,replay_policy:"never_backfill_health_failures; missed_day_resets_streak"});
  assert.equal(r.state,"MANUAL_REVIEW"); assert.equal(r.recovery_recommendation,"never_backfill");
});
test("safe replay remains a candidate until active mode",()=>{
  const w={...base,replay_policy:"safe_latest_state_reconciliation"};
  assert.equal(recoveryPlan(w).state,"RETRY_WAIT");
  assert.equal(canDispatchSameDay({MODE:"shadow"},w,"2026-11-16",new Date("2026-11-16T04:00:00Z")),false);
});
test("active replay is limited to eligible workflows on today's Dhaka date",()=>{
  const safe={...base,replay_policy:"safe_latest_state_reconciliation"};
  const manual={...base,replay_policy:"manual_review_for_missed_business_date"};
  const now=new Date("2026-11-16T04:00:00Z");
  assert.equal(canDispatchSameDay({MODE:"active"},safe,"2026-11-16",now),true);
  assert.equal(canDispatchSameDay({MODE:"active"},safe,"2026-11-15",now),false);
  assert.equal(canDispatchSameDay({MODE:"active"},manual,"2026-11-16",now),false);
});
test("run events are assigned by Bangladesh business date",()=>{
  const run={id:10,event:"schedule",created_at:"2026-11-15T23:00:00Z",status:"completed",conclusion:"success"};
  const r=evaluateWorkflowDay({...base,expected_local_time:"05:00"},"2026-11-16",[run],
    {"10":[{name:"refresh",conclusion:"success"}]},new Date("2026-11-16T00:30:00Z"));
  assert.equal(r.state,"VERIFIED");
});

test("policy-aware discovery may catch up only when no workflow run exists",()=>{
  const w={...base,replay_policy:"policy_aware_reconciliation"};
  assert.equal(recoveryPlan(w,"workflow_run_not_found").state,"RETRY_WAIT");
  assert.equal(recoveryPlan(w,"workflow_failed").state,"MANUAL_REVIEW");
  assert.equal(recoveryPlan(w,"required_job_skipped").state,"MANUAL_REVIEW");
});
test("EPG catch-up candidate must pass the existing last-known-good gate",()=>{
  const w={...base,replay_policy:"publish_only_after_last_known_good_validation"};
  assert.equal(recoveryPlan(w,"workflow_run_not_found").state,"RETRY_WAIT");
  assert.equal(recoveryPlan(w,"workflow_failed").state,"MANUAL_REVIEW");
});

test("newer skipped run blocks retry despite an older failed run",()=>{
  const older={id:20,event:"schedule",created_at:"2026-11-16T00:10:00Z",status:"completed",conclusion:"failure"};
  const newer={id:21,event:"workflow_dispatch",created_at:"2026-11-16T00:20:00Z",status:"completed",conclusion:"success"};
  const r=evaluateWorkflowDay({...base,replay_policy:"safe_latest_state_reconciliation"},"2026-11-16",
    [older,newer],{"21":[{name:"refresh",conclusion:"skipped"}]},new Date("2026-11-16T02:00:00Z"));
  assert.equal(r.state,"MANUAL_REVIEW");
  assert.equal(r.last_error_code,"required_job_skipped");
  assert.equal(r.run.id,21);
});
test("newer failed run cannot be masked by an older successful run",()=>{
  const older={id:22,event:"schedule",created_at:"2026-11-16T00:10:00Z",status:"completed",conclusion:"success"};
  const newer={id:23,event:"workflow_dispatch",created_at:"2026-11-16T00:20:00Z",status:"completed",conclusion:"failure"};
  const r=evaluateWorkflowDay(base,"2026-11-16",[older,newer],
    {"22":[{name:"refresh",conclusion:"success"}]},new Date("2026-11-16T02:00:00Z"));
  assert.equal(r.state,"MANUAL_REVIEW");
  assert.equal(r.last_error_code,"workflow_failed");
  assert.equal(r.run.id,23);
});
