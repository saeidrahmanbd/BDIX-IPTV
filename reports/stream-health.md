# Stream Health

Last checked: **2026-09-29T16:43:28+00:00**

Non-destructive availability check of the current playlist.

## Summary

- Unique stream URLs checked: **0**
- Healthy: **0**
- Redirect/temporary: **0**
- Timeout: **0**
- HTTP error: **0**
- Invalid HLS: **0**
- Connection error: **0**
- Not Playing: **0**
- Repeated-failure candidates (>= 3 runs): **0**

## Policy

- A failed check never deletes a stream automatically.
- A stream needs 3 consecutive failed health runs before it is listed as an obsolete candidate.
- A later successful check resets the failure streak to zero.
- Valid redirects do not count as failures.
- Not Playing entries are excluded from active failure scoring.

## Primary / Backup Hierarchy

The hierarchy below is logical maintenance metadata; the playlist itself is not reordered or rewritten.
Primary is the currently preferred stream. Backup 1, Backup 2, etc. are ordered alternatives based on health and repeated-failure history.

See `reports/stream-priority.json` for the machine-readable hierarchy.

## Repeated-Failure Candidates

None.

## Detailed Results
