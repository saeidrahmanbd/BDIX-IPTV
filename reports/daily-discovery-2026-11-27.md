# Daily IPTV Discovery Report — 2026-11-27

Generated: **2026-11-27 06:56:08 +06:00 (Asia/Dhaka)**

Repository: [saeidrahmanbd/BDIX-IPTV](https://github.com/saeidrahmanbd/BDIX-IPTV)

Final playlist snapshot after targeted repair: **225a65307ba59061c77dc3fc2eb46d20c0c632d9**

**Overall status: PARTIAL.** Both discovery workflows' actual `discover` jobs completed successfully, both final discovery validations passed, and both stage commits were published. Today's scheduled events were absent; the repository watchdog recovered the discovery workflows through workflow_dispatch. The EPG recovery dispatched by the watchdog failed its configuration test. Existing playlist-policy and logo-provenance blockers remain.

This report was generated from the 27 November 2026 workflow runs, current stage reports, current playlist blobs and a fresh post-discovery validation. It does not reuse an earlier daily report.

## 1. Schedule audit and recovery

The repository's Actions run history was independently queried for `event=schedule` over the 27 November Bangladesh-date window:

- UTC window checked: **2026-11-26T18:00:00Z to 2026-11-27T00:56:08Z**
- Scheduled workflow runs found: **0**

The current workflow files still define these Bangladesh-local production times:

| Workflow | Configured schedule |
|---|---:|
| IPTV New Channel Discovery | 05:07 |
| International Channel Discovery | 05:17 |
| Playlist Logo Repair and Localization | 05:27 |
| International Stream Health | 05:37 |
| IPTV Playlist Update | 05:47 |
| Refresh IPTV EPG | 06:07 |
| Daily Xtream Health Check | 06:30 |

The Discovery Schedule Watchdog also has independent checkpoints at 05:15, 05:30, 05:45, 06:00, 06:15, 06:30, 06:45, 06:55 and later in the morning. No schedule-triggered run was recorded in the checked Bangladesh-date window. **This is a missing schedule-event finding; it does not prove the cron definitions are wrong, and cron delivery is not considered fixed.**

### Manual recovery evidence

| Bangladesh time | Watchdog / production run | Result |
|---|---|---|
| 05:25:35 | [Watchdog #45910871598](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/45910871598) | Dispatched IPTV discovery attempt 1/2 |
| 05:26:11 | [IPTV discovery #45910930837](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/45910930837) | Success |
| 05:35:34 | [Watchdog #45911851251](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/45911851251) | Dispatched International discovery attempt 1/2 |
| 05:36:04 | [International discovery #45911899168](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/45911899168) | Success |
| 05:50:34 | [Watchdog #45913283185](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/45913283185) | Recovery check |
| 05:51:05 | [Logo localization #45913332303](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/45913332303) | Success |
| 06:00:35 | [Watchdog #45914199389](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/45914199389) | Recovery check |
| 06:01:05 | [International stream health #45914255778](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/45914255778) | Success |
| 06:15:34 | [Watchdog #45915681551](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/45915681551) | Recovery check |
| 06:16:07 | [IPTV maintenance #45915734468](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/45915734468) | Success |
| 06:50:34 | [Watchdog #45919098926](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/45919098926) | Success; evaluated actual required jobs |
| 06:51:10 | [EPG refresh #45919156698](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/45919156698) | Failed in refresh job |
| 06:51:14 | [Xtream health #45919162329](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/45919162329) | Success |

The 06:50 watchdog log confirmed that the required IPTV discovery, International discovery, logo-localization, stream-health and maintenance jobs already had successful runs for Bangladesh date 2026-11-27. It did not launch duplicate discovery writers. It dispatched EPG recovery attempt 1/2 and Xtream health attempt 1/2.

At the final audit, the latest 100 main-branch runs contained no active or queued workflow. The watchdog's EPG dispatch failed after its daily guard passed. The connected GitHub action interface did not expose a second workflow_dispatch operation, so no individual writer was launched to bypass the watchdog's retry and lock protections.

**Schedule conclusion:** manual recovery successfully completed both discovery stages, but the scheduled events were absent. Do not report cron delivery as repaired.

## 2. IPTV-Playlist.m3u — Bangladesh and India

- Workflow: [IPTV New Channel Discovery #45910930837](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/45910930837)
- Required jobs: `daily_guard` **success**; `discover` **success**
- The discovery policy, country-metadata, stream-identity, validator, daily-guard, workflow-isolation and report-freshness test steps all passed.
- Fresh stage report: [reports/iptv-channel-discovery.md](https://github.com/saeidrahmanbd/BDIX-IPTV/blob/main/reports/iptv-channel-discovery.md)
- Discovery commit: [0696dee82f63a4fcaa091b222cbb33d58517753f](https://github.com/saeidrahmanbd/BDIX-IPTV/commit/0696dee82f63a4fcaa091b222cbb33d58517753f)

### Discovery and probe results

| Metric | Result |
|---|---:|
| New primary candidates staged | 31 |
| New alternative candidates staged | 21 |
| Source candidates rejected/held | 824 |
| New entries and queued streams probed | 52 |
| Live-media responses | 21 |
| Verified new primary entries retained | 0 |
| Verified alternative streams retained | 0 |
| Inconclusive candidates retained for manual review | 10 |
| Unverified backup streams moved to Review during probe | 9 |
| Definitively dead candidates removed | 12 |
| Duplicate newly discovered stream entries removed | 0 |

**No justified verified primary-group or New Backup additions were made by this IPTV probe.** The workflow retained candidates for owner review rather than treating an HTTP response or incomplete evidence as proof of a legitimate, playable channel.

The stage's final validation was **PASS** at 05:27:34 Bangladesh time:

- 40 manual-review candidates retained
- 0 new malformed EXTINF/URL pairs
- 0 new duplicate stream URL occurrences
- 10 retained candidates lacked an authentic local logo; no placeholder was used
- 2 candidates had country metadata requiring manual review
- 0 prohibited Indian rows remained in New Channels/New Backups
- 0 new backup identity/duplicate-primary issues

### Rejection reasons

| Reason | Count |
|---|---:|
| Indian news | 303 |
| Duplicate stream URL | 286 |
| Indian religious category | 122 |
| Permanently banned | 32 |
| Unsupported stream path | 19 |
| Indian kids | 13 |
| Known prohibited Indian brand/category | 12 |
| Tokenized URL | 10 |
| Indian business | 9 |
| Indian education | 7 |
| Proxy/worker host | 3 |
| Duplicate queued identity | 1 |
| Indian knowledge | 2 |
| Country metadata outside Bangladesh/India | 4 |
| Other prohibited/retired candidates | 1 |

Policy caveat: the 122 religious rejections are reported under a broad Indian religious category. The current rule excludes **non-Islamic** religious channels but permits Islamic religious channels. The source rejection report does not distinguish those subcategories, so this filter needs a category-level audit to avoid over-rejecting eligible Islamic channels.

### Current IPTV queue and playlist snapshot

The subsequent maintenance run completed successfully. The current playlist has:

| Group | Entries |
|---|---:|
| Bangladesh | 67 |
| Indian Bangla | 35 |
| Indian Movies | 66 |
| Indian Music | 59 |
| Indian Entertainment | 162 |
| Pakistani | 16 |
| International | 81 |
| Documentary & Wildlife | 55 |
| Kids | 36 |
| Religious | 27 |
| Sports | 104 |
| Review | 1 |
| New Channels | 25 |
| New Backups | 15 |
| Backup | 434 |
| **Total** | **1,183** |

Current New Channels include Madani Channel Bangla, News 21 Bangla TV, Rupashi Bangla TV, AMN TV, Cine Jomjomat, Epic TV Digital, History TV18 HD, Mango Mobile TV, NDTV Good Times, Sooriyan TV, Travelxp HD, WeatherSpy, Zee Cine Classic, Zee Comedy Nation, Zee Dil Se, Zee Horror Nights, Zee South Flix, Zee Tamil HD, Zee Telugu HD and other held candidates.

Current New Backups include ATN Bangla, DBC News, Duronto TV, Ekhon TV, Gazi TV, Maasranga TV, RTV, 9X Jhakaas, 9X Tashan, B4U Bhojpuri, B4U Kadak, B4U Movies, DD Uttar Pradesh, Dhoom Music and INWILD.

The current queue inventory includes manual-review rows accumulated in the playlist; it is not a claim that all 40 rows were newly verified today. The existing Pakistani, International, Documentary & Wildlife, Kids and Religious groups remain legacy scope blockers. They were preserved rather than broadly deleted or reclassified.

## 3. International-Playlist.m3u

- Workflow: [International Channel Discovery #45911899168](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/45911899168)
- Required jobs: `daily_guard` **success**; `discover` **success**
- The strict Movies/Music policy, retired-endpoint, stream-validator, five-channel/protected-group tests, script compilation, attribution, stream-probe and final playlist-validation steps completed successfully.
- Fresh stage report: [reports/international-channel-discovery.md](https://github.com/saeidrahmanbd/BDIX-IPTV/blob/main/reports/international-channel-discovery.md)
- Discovery commit: [4e4a0ba9ba3022eb47883d55dbe918e59af6e03c](https://github.com/saeidrahmanbd/BDIX-IPTV/commit/4e4a0ba9ba3022eb47883d55dbe918e59af6e03c)

### Discovery and probe results

| Metric | Result |
|---|---:|
| Source records parsed | 12,164 |
| Existing playlist records at scan | 3,318 |
| Exact source URLs already present | 2,182 |
| New eligible source records | 152 |
| New primary candidates staged | 50 |
| New backup candidates staged | 8 |
| Adult primary channels discovered directly into Adult | 0 |
| Fashion TV channels discovered directly into Fashion TV | 0 |
| Entries and existing queue streams probed | 72 |
| Live-media responses | 14 |
| Verified new primary entries retained in New Channels | 4 |
| Verified alternative streams retained in New Backups | 10 |
| Inconclusive candidates retained for manual review | 9 |
| Unverified backup streams moved to Review | 2 |
| Definitively dead candidates removed | 47 |
| Duplicate newly discovered stream entries removed | 0 |

The final discovery validation was **PASS** at 05:37:13 Bangladesh time:

- 3,329 entries parsed at the discovery-run snapshot
- 0 malformed EXTINF/URL pairs
- 0 duplicate stream URLs
- Review → New Channels → New Backups → Backup ordering passed
- 4 discovery rows had no authentic local logo and were left without a logo
- 0 non-local discovery logo references
- 0 geography/content-policy issues reported by the stage validator
- Existing non-discovery entries were not removed by stream validation

No new Adult or Fashion TV primary channel was found. Existing groups remain: Adult **366** entries and Fashion TV **5** entries.

### Inconclusive and rejected candidates

The nine inconclusive primary candidates recorded by the probe were:

- BRIDGE Dance — HTTP 403
- BRIDGE Jazz — HTTP 403
- BRIDGE Rap — HTTP 403 / geo-blocked
- Galaxy — URLError
- Galaxy Premium — URLError
- Hollywood Ukraine — URLError
- Komsan TV — URLError
- Prokino — URLError
- Viasat Kino (Ukraine) — URLError

These are held for manual review, not counted as verified playable channels. The probe also removed numerous dead endpoints, including 4 Fun TV, 7 RadioVisione, AMC (United States), AMC Latin America, Cinevault 80s, Film & Arts, multiple Rakuten TV endpoints and Summer of Movies. TVS Film Noir Network returned HTML/error content rather than a TV stream and was removed.

The two unverified backup streams moved to Review were M1 (Ukraine) and Viasat Kino Action. The final current New Backups queue contains 10 entries: Cinema (Russia), Dom kino, Dorama, Epic Music, iFilm Persian, Indiyskoye Kino, KinoHit, Muzyka Pervogo, Rotana Cinema KSA and TRT Muzik.

### Rejection reasons

| Reason | Count |
|---|---:|
| Source category not Movies or Music | 6,600 |
| News | 1,082 |
| Religious | 780 |
| Kids | 315 |
| Sports | 305 |
| Test/VOD/non-TV name | 300 |
| Documentary & Wildlife | 189 |
| Unsafe/tokenized URL | 141 |
| General entertainment | 69 |
| TV series | 24 |
| Permanently banned | 10 |
| Known prohibited Indian brand/category | 12 |
| Other specific/ambiguous categories | 4 |

### Current International playlist snapshot

- Total entries: **3,315**
- New Channels: **11**
- New Backups: **10**
- Adult: **366**
- Fashion TV: **5**
- Review: **925**
- Backup: **293**

The current queue order is Review → New Channels → New Backups → Backup.

The workflow report's five-primary-identity threshold still exempts Bangladesh and India, while the current instruction requires the threshold for every country. No new country group was created today, but the configuration exception remains a blocker.

Legacy out-of-scope groups remain in the existing International playlist: Indian Entertainment 157, News 11, Documentary & Wildlife 129, Kids 149, Religious 31 and Sports 177. They were preserved rather than broadly deleted or reclassified.

## 4. Targeted IPTV playlist repair after discovery

The independent current-file audit found that IPTV-Playlist.m3u still had 749 raw GitHub logo URLs and the queue groups were in the wrong order:

- Before repair: Backup → New Channels → New Backups → Review
- Required order: Review → New Channels → New Backups → Backup

A targeted repair was committed:

[225a65307ba59061c77dc3fc2eb46d20c0c632d9 — Use local IPTV logos and restore discovery queue order](https://github.com/saeidrahmanbd/BDIX-IPTV/commit/225a65307ba59061c77dc3fc2eb46d20c0c632d9)

The commit changed **IPTV-Playlist.m3u only**:

- Converted 749 raw repository logo URLs to relative logos/ paths.
- Verified all 749 referenced logo files exist in the repository tree.
- Left zero external tvg-logo URLs and zero missing referenced logo files.
- Reordered only the final queue groups to Review → New Channels → New Backups → Backup.
- Preserved all 1,183 entries, stream URLs, group assignments and channel identities; no channel was added or removed by this repair.

## 5. Final independent playlist validation

Validation was rerun against the current main-branch files after the targeted repair.

| Check | IPTV-Playlist.m3u | International-Playlist.m3u |
|---|---:|---:|
| EXTINF entries | 1,183 | 3,315 |
| Malformed EXTINF/URL pairs | 0 | 0 |
| Duplicate stream URLs | 0 | 0 |
| Duplicate primary identity groups | 0 | 0 |
| Relative logos/ references | 1,183 | 2,915 |
| External tvg-logo references | 0 | 0 |
| Blank logo fields | 0 | 400 |
| Referenced local logo files missing | 0 | 0 |
| Queue order | Pass | Pass |

International's 400 blank logo fields were left blank rather than filled with invented or placeholder artwork.

### Logo authenticity limitation

The latest available logo provenance report was generated at 06:18:50 Bangladesh time, before the IPTV path-only repair. It recorded 0 officially verified logos, 1,003 third-party-verified assets, 2 generated fallback assets and 3,493 assets needing provenance review across the two playlists. The path-only repair did not change image bytes, but the provenance report must be regenerated against the new IPTV playlist fingerprint. Therefore, **local-path validation passed, but full broadcaster-logo authenticity is not yet certified**. The two generated fallback assets and the large needs-review inventory remain blockers.

## 6. EPG recovery failure and remaining blockers

The 06:50:34 watchdog run found no successful required EPG job for Bangladesh date 2026-11-27 and dispatched recovery attempt **1/2**. The EPG workflow's daily_guard passed, but its actual `refresh` job failed.

Exact failing test:

`test_epg_config.VerifiedAliasTests.test_verified_international_ids_exist_in_playlist`

The test expected **tvg-id="RakutenTVFamilyMovies.es"** in the current International playlist, but that ID was not present. XMLTV regeneration/publication therefore did not complete in this recovery run.

The Xtream health recovery completed successfully. No active or queued writer remained at the final audit. No individual EPG writer was manually launched after the failure; the watchdog's bounded retry and shared-writer protections were not bypassed.

Remaining blockers:

1. GitHub recorded no schedule-triggered workflow runs for the checked Bangladesh date, despite valid cron definitions. Manual recovery completed discovery, but cron delivery remains unverified.
2. EPG recovery attempt 1/2 failed because the verified International EPG alias references a missing playlist tvg-id.
3. International's country-group threshold code still exempts Bangladesh and India from the five-identity minimum.
4. IPTV's 122 broad Indian religious rejections do not distinguish Islamic from non-Islamic channels.
5. Existing out-of-scope legacy groups remain in both playlists because broad deletion/reclassification was not authorized.
6. Logo paths now pass local-file checks, but the latest provenance inventory still contains generated fallback and needs-review assets and must be regenerated after the IPTV change.

## 7. Final result

- **IPTV discovery:** actual discover job succeeded; final validation passed; 31 primary and 21 backup candidates were staged, but no verified primary or alternative stream was retained after probing. Forty candidates remain in manual-review queues.
- **International discovery:** actual discover job succeeded; final validation passed; 4 verified primary entries and 10 verified alternative streams were retained. Nine inconclusive primary candidates remain held. No new Adult or Fashion TV channels were found.
- **Targeted repair:** IPTV external logo URLs were converted to verified local paths and queue order was corrected in a single-file commit.
- **Schedule reliability:** schedule events were absent; watchdog workflow_dispatch recovery ran successfully for discovery. Cron delivery is not considered fixed.
- **Overall:** **PARTIAL**, because the EPG recovery failed and the existing country-threshold, legacy-content and logo-authenticity blockers remain.

Stage reports and run logs are linked above. No playlist was replaced with a partial list, and no broad channel deletion or reclassification was performed.
