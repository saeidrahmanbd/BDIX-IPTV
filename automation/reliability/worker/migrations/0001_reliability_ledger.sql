-- Shadow-mode D1 migration for the BDIX-IPTV reliability ledger.
-- Apply only to the dedicated reliability database, never a production playlist store.
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS reliability_executions (
    execution_key TEXT PRIMARY KEY,
    workflow_id TEXT NOT NULL,
    business_date TEXT NOT NULL,
    registry_version TEXT NOT NULL,
    expected_at_utc TEXT NOT NULL,
    state TEXT NOT NULL CHECK (
        state IN ('EXPECTED','DISPATCHING','DISPATCHED','RUNNING','RETRY_WAIT',
                  'PUBLISHED','VERIFYING','VERIFIED','MANUAL_REVIEW','SUPERSEDED')
    ),
    dispatch_attempts INTEGER NOT NULL DEFAULT 0 CHECK (dispatch_attempts >= 0),
    github_run_id TEXT,
    github_run_attempt INTEGER,
    started_at_utc TEXT,
    completed_at_utc TEXT,
    publication_sha TEXT,
    verification_status TEXT NOT NULL DEFAULT 'PENDING' CHECK (
        verification_status IN ('PENDING','PASS','FAIL','NOT_APPLICABLE')
    ),
    next_retry_at_utc TEXT,
    last_error_code TEXT,
    last_error_summary TEXT,
    created_at_utc TEXT NOT NULL,
    updated_at_utc TEXT NOT NULL,
    UNIQUE (workflow_id, business_date)
);

CREATE TABLE IF NOT EXISTS reliability_attempts (
    workflow_id TEXT NOT NULL,
    business_date TEXT NOT NULL,
    attempt_number INTEGER NOT NULL CHECK (attempt_number >= 1),
    trigger_source TEXT NOT NULL CHECK (
        trigger_source IN ('cloudflare_cron','external_cron','manual','github_callback')
    ),
    dispatch_requested_at_utc TEXT NOT NULL,
    github_run_id TEXT,
    github_run_attempt INTEGER,
    run_status TEXT NOT NULL CHECK (
        run_status IN ('REQUESTED','QUEUED','IN_PROGRESS','COMPLETED','UNKNOWN')
    ),
    run_conclusion TEXT,
    critical_job_conclusion TEXT,
    publication_sha TEXT,
    verification_status TEXT NOT NULL DEFAULT 'PENDING' CHECK (
        verification_status IN ('PENDING','PASS','FAIL','NOT_APPLICABLE')
    ),
    error_code TEXT,
    error_summary TEXT,
    created_at_utc TEXT NOT NULL,
    updated_at_utc TEXT NOT NULL,
    PRIMARY KEY (workflow_id, business_date, attempt_number),
    FOREIGN KEY (workflow_id, business_date)
      REFERENCES reliability_executions(workflow_id, business_date)
);

CREATE TABLE IF NOT EXISTS reliability_events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    execution_key TEXT NOT NULL,
    event_type TEXT NOT NULL,
    event_source TEXT NOT NULL,
    event_at_utc TEXT NOT NULL,
    details_json TEXT NOT NULL DEFAULT '{}',
    FOREIGN KEY (execution_key) REFERENCES reliability_executions(execution_key)
);

CREATE INDEX IF NOT EXISTS idx_reliability_executions_due
  ON reliability_executions(state, expected_at_utc, next_retry_at_utc);
CREATE INDEX IF NOT EXISTS idx_reliability_attempts_run_id
  ON reliability_attempts(github_run_id);
CREATE INDEX IF NOT EXISTS idx_reliability_events_execution_time
  ON reliability_events(execution_key, event_at_utc);
