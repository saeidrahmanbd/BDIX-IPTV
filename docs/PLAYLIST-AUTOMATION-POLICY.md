# Playlist Automation Policy

This policy is mandatory for every scheduled workflow, maintenance script, discovery job, repair utility and future automation change.

## IPTV-Playlist.m3u — owner-curated, manually reviewed by the owner

Daily automation may:
- Correct channel names, IDs, country/language metadata and other metadata when supported by reliable evidence.
- Replace invalid/external logo references only with verified authentic repository-local assets.
- Improve EPG identity mappings and report schedule gaps; the dedicated EPG workflow owns XMLTV generation/publication.
- Discover eligible new Bangladesh/India channels and alternate streams into the manual `New Channels` / `New Backups` queues.
- Keep streamable new candidates in those queues when country/language/name metadata or an authentic local logo is unresolved. These are warning-only manual-review items and must not stop discovery or block other valid candidates. Never invent metadata or use a placeholder logo.
- Diagnose broken, blocked, restricted, fragile and inconclusive endpoints. Use reliable evidence to correct metadata or queue a discovered alternate in `New Backups`; stream access failures never authorize URL replacement.
- Keep every existing row's `group-title`, `tvg-chno`, category position and relative row order unchanged. New discoveries may be appended only to the manual `New Channels` / `New Backups` queues.

Automation must never:
- Delete an existing stream row or replace/change its stream URL.
- Automatically retire a channel after stream-probe failures. The owner manually reviews stream health.
- Promote, demote or migrate entries from `Backup`, `Review`, `New Channels` or `New Backups`; these remain owner-controlled queues.
- Alter `Adult` entries or guess country/genre metadata when evidence is ambiguous.
- Treat an HTTP block, regional restriction, transient outage or inconclusive probe as authorization to remove a channel.

The main-playlist publication gate verifies that every pre-existing stream URL occurrence remains present. Routine automation may repair metadata and authentic local-logo references only. It must preserve existing row order, group assignments, channel numbers and stream URLs. It must not promote, demote, migrate, renumber, regroup or reassemble existing IPTV rows. New discoveries remain in the manual `New Channels` / `New Backups` queues for owner review.

The former one-time owner-requested migration authorization was revoked on 2026-11-14 and its automatic workflow path has been retired. The revoked marker remains in the repository as an audit record; it is not read by production automation. Any future structural exception requires a new, explicit owner decision and a separately reviewed change; the retired queue-promotion mechanism must not be reactivated.

`Review` is reserved for channels that do not stream at the time of checking and are retained for future rechecks. It is not a general-purpose holding category for policy-excluded, missing-logo, or uncertain metadata cases.

## International-Playlist.m3u — automation-controlled

Daily automation must:
- Maintain channel metadata, authentic local logos, EPG mappings and correct country/genre grouping.
- Probe all streams and maintain consecutive Bangladesh-calendar-day failure history.
- Move a first-day definitive failure to `Review`; remove a stream only after three consecutive definitive failed days. A missed day restarts the streak; an inconclusive/authentication/rate-limit/geo-block result is not a definitive failure and cannot authorize deletion.
- Re-test `Review` entries. When a row is confirmed working and still satisfies the country/genre policy, migrate it to its correct primary group; if the channel identity already has a primary stream, place the working alternate in `Backup`. Keep invalid or policy-ineligible entries in `Review`.
- Create a dedicated country group only when there are at least five unique primary channel identities for that country. Backup/alternate streams and Review rows do not count. Bangladesh and India retain their established fixed groups; Pakistan and all other country-specific groups follow the five-identity threshold.
- Reorganize and deduplicate the International playlist under the established regional policy, preserving protected Adult and discovery queues.

A stream URL must not be deleted because of a single failure, an inconclusive probe, or a runner-wide connectivity incident. The batch safety gate must stop publication when the probe results indicate a global network/reachability anomaly.

## Shared engineering requirements

- Every mutating script must identify its target playlist explicitly; avoid ambiguous all-playlist mutation defaults.
- International reorganization and health/removal authority must never be applied to the owner-curated IPTV playlist.
- Public XMLTV generation/publication remains in `.github/workflows/epg-refresh.yml`, with freshness, quality and last-known-good publication guards.
- Logo repair must use authentic, validated local assets; never invent or substitute unrelated artwork.
- All playlist writers must use the common serialized writer queue.
- Regression tests must cover URL preservation, protected queues, grouping thresholds, Review recovery, three-day retirement and regional policy.
