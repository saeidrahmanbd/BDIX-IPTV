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

### Explicit owner-approved manual exception — 2026-11-26

The owner explicitly authorized a one-time migration of five already-retained Backup entries in PR #391:
- `CartoonNetwork.in@SD`, `Pogo.in@SD`, and `SonyYay.in@SD` -> `Kids`.
- `custom.discoverybangla` -> `Documentary & Wildlife`.
- `MatribhumiTV.bd` -> `Bangladesh`.

This is a narrowly scoped manual curation exception, not a discovery-policy change. The Indian Kids discovery exclusion remains active for all other Indian Kids candidates. Discovery must continue rejecting those candidates unless the owner gives a new explicit approval. The three named Indian Kids rows must not be used as precedent to automatically admit further Indian Kids channels.

### Explicit owner-directed removals and discovery exclusions — 2026-11-26

The owner explicitly instructed removal of these two India-origin candidates from the maintained IPTV playlist because they do not fit the permitted Indian channel categories:
- `MetroTV.in@SD` — Metro TV (India), Telugu news; classified as Indian News.
- `AyushNextCommunicationNetwork.in@SD` — Ayush Next Communication Network; classified as Indian Knowledge/health-information content.

Both rows were removed from `New Channels`. Their exact identities are now explicit Indian discovery exclusions, so future scheduled discovery must reject them rather than re-adding them. This is a narrow owner-directed exception to the normal protected-queue/no-delete rule, not a general authorization to delete other queue entries.

Disney Channel India (`DisneyChannel.in@HD`) was already present in the primary `Kids` group; no additional promotion was needed. Its separate alternate stream remains in `Backup`.


### Owner clarification: Indian groups are programme-based, not origin-based — 2026-11-26

The owner clarified that broadcaster headquarters, incorporation, uplink or country of origin do not determine eligibility for the four Indian groups. Classification is based on the actual channel programming and the four group definitions:
- Indian Bangla: Bengali-language programming.
- Indian Movies: movie programming, any language or region.
- Indian Music: music programming, any language or region.
- Indian Entertainment: entertainment programming, any language or region.

Do not reject a channel solely because its metadata country is PK, CA, US, AE or another country. Do not classify a channel as Indian solely because its metadata country is IN. Inspect the actual channel programming and classify by content genre. News-only channels do not qualify for these four groups.

Owner-directed corrections:
- Jalwa TV (`JalwaTV.pk@SD`) belongs in `Pakistani`: it is a Pakistani music channel, not an Indian music channel. Preserve its PK/Urdu metadata.
- Wayanad Vision Movies belongs in Indian Movies.
- Movies Now, Sony Movies, and Star Movies belong in International per the owner's explicit instruction; rename `Star Movies (India) HD` to `Star Movies`.
- MBC Bollywood is an Arabic-language service for this playlist's classification; move it to International and rename it `MBC`. Preserve its channel ID and EPG identity.
- KCM India remains in Indian Entertainment because its programming comprises English-language dramas, movies and factual entertainment; its non-Indian operator/origin alone is not grounds for exclusion.
- Nepal 1 (`Nepal1.in@SD`) is prohibited non-Bangladeshi news content; remove it from every playlist group and permanently block its identity from rediscovery.

- Non-Bangladeshi news channels are prohibited from every playlist, including `International`, `Backup` and `Review`, except the four owner-approved International news exceptions: Al Jazeera (`AlJazeera.qa`), BBC World (`custom.bbcworld`), CNN (`CNN.us`) and DW News (`DWNews.de`). Keep these four in `International`; their exact identities are exempt from automatic foreign-news exclusion. Bangladeshi news channels remain allowed.
- The classification is based on the actual programme genre/content, not the broadcaster's headquarters, distribution market, uplink, or country metadata. For example, a Pakistani music channel is not an Indian Music channel merely because it broadcasts music.
- Recheck corrections: Alankar TV -> Indian Entertainment (Jatra/drama-led Odia entertainment); Tabbar Hits -> Indian Music (Punjabi music channel); Mahua Play -> Indian Movies (Bhojpuri movie service); TamilVision-TV -> Indian Entertainment (mixed Tamil-language entertainment, not a dedicated movie channel); NTC TV language metadata -> `tam`.
- Jaihind TV (`JaihindTV.in@SD`) is non-Bangladeshi news and remains permanently excluded from the playlist and automatic rediscovery. Al Jazeera, BBC World, CNN and DW News are explicit owner-approved exceptions and must remain in `International`.

The main-playlist publication gate verifies that every pre-existing stream URL occurrence remains present. Routine automation may repair metadata and authentic local-logo references only. It must preserve existing row order, group assignments, channel numbers and stream URLs. It must not promote, demote, migrate, renumber, regroup or reassemble existing IPTV rows. New discoveries remain in the manual `New Channels` / `New Backups` queues for owner review.

The former one-time owner-requested migration authorization was revoked on 2026-11-14 and its automatic workflow path has been retired. The revoked marker remains in the repository as an audit record; it is not read by production automation. Any future structural exception requires a new, explicit owner decision and a separately reviewed change; the retired queue-promotion mechanism must not be reactivated.

`Review` is reserved for channels that do not stream at the time of checking and are retained for future rechecks. It is not a general-purpose holding category for policy-excluded, missing-logo, or uncertain metadata cases.

## International-Playlist.m3u — automation-controlled

Daily automation must:
- Maintain channel metadata, authentic local logos, EPG mappings and correct country/genre grouping.
- Probe all streams and maintain consecutive Bangladesh-calendar-day failure history.
- Move a first-day definitive failure to `Review`; remove a stream only after three consecutive definitive failed days. A missed day restarts the streak; an inconclusive/authentication/rate-limit/geo-block result is not a definitive failure and cannot authorize deletion.
- Re-test `Review` entries. When a row is confirmed working and still satisfies the country/genre policy, migrate it to its correct primary group; if the channel identity already has a primary stream, place the working alternate in `Backup`. Remove policy-ineligible channels from all playlist groups immediately; `Review` is only for channels temporarily unavailable pending stream rechecks.
- Create a dedicated country group only when there are at least five unique primary channel identities for that country. Backup/alternate streams and Review rows do not count. Bangladesh and India retain their established fixed groups; Pakistan and all other country-specific groups follow the five-identity threshold.
- Discover only dedicated Movies/Music channels worldwide, including Bangladesh, India and Pakistan; preserve existing Fashion TV entries as a legacy exception.
- Discovery must not broadly reclassify, reorder or delete unrelated existing entries. Commit only validated, targeted queue additions and their fresh report.

A stream URL must not be deleted because of a single failure, an inconclusive probe, or a runner-wide connectivity incident. The batch safety gate must stop publication when the probe results indicate a global network/reachability anomaly.

## Shared engineering requirements

- Every mutating script must identify its target playlist explicitly; avoid ambiguous all-playlist mutation defaults.
- International reorganization and health/removal authority must never be applied to the owner-curated IPTV playlist.
- Public XMLTV generation/publication remains in `.github/workflows/epg-refresh.yml`, with freshness, quality and last-known-good publication guards.
- Logo repair must use authentic, validated local assets; never invent or substitute unrelated artwork.
- All playlist writers must use the common serialized writer queue.
- Regression tests must cover URL preservation, protected queues, grouping thresholds, Review recovery, three-day retirement and regional policy.
