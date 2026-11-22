-- External watchdog trigger ledger (one row per Bangladesh-time checkpoint or manual request).
-- Apply only to the dedicated reliability database, never a production playlist store.
-- The Worker also creates this table on demand (IF NOT EXISTS), so applying this
-- migration is optional but keeps `wrangler d1 migrations` history complete.
CREATE TABLE IF NOT EXISTS watchdog_triggers (
    trigger_key TEXT PRIMARY KEY,
    business_date TEXT NOT NULL,
    source TEXT NOT NULL CHECK (source IN ('checkpoint','manual')),
    state TEXT NOT NULL CHECK (
        state IN ('DISPATCHING','DISPATCHED','FAILED','SKIPPED_ACTIVE',
                  'SKIPPED_RECENT','SKIPPED_LIMIT','DRY_RUN')
    ),
    attempts INTEGER NOT NULL DEFAULT 0,
    retryable INTEGER NOT NULL DEFAULT 0,
    error_summary TEXT,
    created_at_utc TEXT NOT NULL,
    updated_at_utc TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_watchdog_triggers_day
    ON watchdog_triggers (business_date, source, state);
