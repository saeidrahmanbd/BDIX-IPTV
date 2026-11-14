# BDIX-IPTV Existing Automation — Simplified Architecture

Status: approved operating direction; implementation is incremental and remains subject to pull-request checks.

## Decision

Continue repairing and simplifying the existing production automation. Do not perform an Automation V2 cutover or replace the repository's production orchestration with a second system.

The repository should have six clearly bounded responsibilities:
1. Playlist management and validation.
2. Local logo management.
3. EPG mapping, source management, generation and freshness.
4. New-channel and alternate-stream discovery.
5. International playlist stream-health management.
6. Shared reliability, publication safety, recovery and reporting.

A responsibility may use more than one workflow when its schedule, permissions or failure isolation requires it. Avoid duplicate jobs, duplicate writers and competing sources of truth rather than forcing everything into one large workflow.

## Playlist authority and mutation boundaries

### IPTV-Playlist.m3u — owner-curated

The owner retains structural control. Routine automation may:
- Normalize display names and correct evidence-backed metadata.
- Maintain authentic local logo references and EPG identity mappings.
- Validate stream URL integrity, duplicate identities, metadata and publication safety.
- Discover eligible Bangladesh and India candidates into the existing manual review queues.
- Produce reports and recommendations for owner review.

Routine automation must preserve every pre-existing row's relative order, group assignment, stream URL and channel number. It must not automatically sort, regroup, renumber, promote, demote, remove or replace an existing row. New discoveries may only be appended to the established manual queues under the existing discovery policy.

The former one-time owner-requested IPTV migration was revoked on 2026-11-14. Its workflow branch and queue-promotion scripts are retired. The revoked marker remains only as an audit record; production maintenance does not read it.

### International-Playlist.m3u — automation-managed

Automation may maintain metadata, local logos, EPG mappings, country/category groups and ordering. It owns stream-health checks, failure history, Review recovery and retirement under the established three-consecutive-Bangladesh-calendar-day rule. Inconclusive, authentication, rate-limit, geo-block and runner-wide connectivity failures are not definitive failures.

A country-specific group requires at least five unique primary channel identities, except the established fixed groups. The International automation must never apply its reorganization or removal authority to IPTV-Playlist.m3u.

## Six responsibility areas

### 1. Playlist management
- Keep playlist syntax, metadata, identity and URL checks consistent.
- Apply the correct mutation boundary for each playlist.
- Preserve established group names and review-queue visibility rules.
- Keep tvg-id, channel-id, channel numbering and EPG IDs consistent where evidence supports it.
- Publish only after preservation, integrity and regression gates pass.

### 2. Logo management
- Published playlist logo references must resolve to authentic repository-local assets.
- Convert supported source formats to optimized PNG where appropriate; retain vector originals only when required by the asset pipeline.
- Associate assets with verified channel identity and provenance.
- Search approved external sources for missing assets, then download, validate and localize them.
- Treat HTTP 403, rate limits and unavailable sources as source failures; never substitute unrelated artwork or fabricate a logo.
- Delete assets only after proving that no playlist, manifest, dashboard, documentation or runtime references them and a recoverable backup exists.

### 3. EPG management
- Maintain one authoritative mapping/source registry.
- Evaluate source rights, reliability, freshness and region coverage.
- Map channel identities using verified aliases.
- Audit schedule coverage, stale feeds, timezone offsets, duplicate programmes and malformed XMLTV.
- Generate and publish only validated XMLTV; retain last-known-good output when a candidate fails.

### 4. Channel discovery
- Discover worthwhile channels for both playlists under their distinct rules.
- Validate candidate stream reachability and identity; check duplicates and country/genre eligibility.
- Keep unverified or incomplete candidates in the established review queues.
- Never promote an IPTV candidate into an owner-curated primary group automatically.
- Never treat an HTTP block or transient probe failure as proof that a channel should be removed.

### 5. Stream health
- Run automated stream-health lifecycle management only for International-Playlist.m3u.
- Keep IPTV-Playlist.m3u stream-health review manual, as requested by the owner.
- Persist consecutive Bangladesh-date failure history and recovery evidence.
- Stop publication on batch-wide connectivity anomalies.

### 6. Shared reliability and governance
- Use one serialized main-branch writer queue for all mutating workflows.
- Use explicit playlist targets in scripts; avoid ambiguous all-playlist mutation defaults.
- Back up before structural changes; support rollback to the last known-good state.
- Make runs idempotent and safe to retry.
- Deduplicate schedules and completion hooks without suppressing legitimate recovery runs.
- Publish concise reports with inputs, outputs, counts, warnings, blockers and artifact freshness.
- Keep regression tests for owner protection, International-only authority, URLs, grouping thresholds, logo authenticity, EPG quality and recovery.

## Workflow and code simplification rules

1. Keep the existing production workflows until a dependency and runtime audit proves a replacement is safe.
2. Consolidate overlapping triggers and repeated validation steps where doing so does not weaken failure isolation, permissions or safety gates.
3. Every workflow must have a named responsibility, an owner, an input/output contract, an explicit write scope and a recovery path.
4. Retire a workflow only after confirming no schedule, workflow_run hook, manual procedure, external badge, dashboard, script or user process depends on it.
5. Retire a script only after repository-wide reference search, workflow tracing, test tracing and runtime/import tracing.
6. Keep tests that protect production data and owner intent. Consolidate duplicate tests only after preserving their coverage.
7. Keep current operational documentation and policy. Archive obsolete V2 design documents only after checking that no active procedure links to them.
8. Do not bulk-delete logo files, reports, scripts, workflows or folders as a cleanup shortcut.
9. Keep generated reports that are public operational outputs; expire stale transient diagnostics only through an explicit retention policy.
10. Do not change production playlists as part of architecture-only work.

## Current workflow inventory and disposition

The current repository has 25 workflow files:

- Eight Automation V2 workflows are retained as diagnostic/CI evidence; they are not the production architecture.
- Seventeen existing production, maintenance, deployment, discovery, EPG, logo, health, reporting and validation workflows remain in place.
- The two logo workflows have overlapping IPTV coverage but different scopes: the isolated logo-localization workflow targets IPTV-Playlist.m3u, while the scheduled playlist-logo workflow handles both playlists. They must be compared for source-catalog and output parity before consolidation.
- IPTV and International discovery have separate schedules and policy scopes; keep those separate.
- The two EPG source-probe workflows are source-research utilities, not substitutes for the EPG publication pipeline.
- Deployment, SEO, IndexNow and test workflows are supporting services, not playlist-maintenance engines.

The scheduled Automation V2 Candidate Bundle and Automation V2 Missed-Run Recovery triggers are paused. Manual dispatch remains available for explicit diagnostics. Branch CI and legacy regression workflows remain available to validate changes. No V2 production cutover is authorized.

## Automation V2 disposition

Automation V2 development and cutover are frozen. Existing V2 contracts, reports and migration evidence are retained as audit/reference material while the existing production system is repaired. No V2 workflow may become a second production writer or silently take over scheduling.

## Acceptance criteria

The simplified system is accepted only when:
- IPTV maintenance passes while preserving all existing IPTV row order, groups, URLs and channel numbers.
- International health and reorganization pass without touching IPTV structural data.
- EPG generation, mapping audit and freshness checks pass.
- Logo references resolve locally and missing/blocked sources are reported honestly.
- Discovery respects both playlist policies and review queues.
- All main-branch writers serialize correctly and retry/recovery behavior is verified.
- The scheduled workflows run at their intended Bangladesh times without duplicate or missing runs.
- Reports and dashboards describe the actual published state.

A green test suite alone is not production acceptance; post-merge scheduled runs and published outputs must also be checked.