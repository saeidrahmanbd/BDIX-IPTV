CREATE TABLE IF NOT EXISTS hits (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ts TEXT NOT NULL,
  day TEXT NOT NULL,
  playlist TEXT NOT NULL CHECK (playlist IN ('main','international')),
  client_hash TEXT NOT NULL,
  country TEXT NOT NULL DEFAULT 'XX'
);
CREATE INDEX IF NOT EXISTS idx_hits_ts ON hits(ts);
CREATE INDEX IF NOT EXISTS idx_hits_day_playlist ON hits(day, playlist);
CREATE INDEX IF NOT EXISTS idx_hits_client_day ON hits(day, client_hash);
