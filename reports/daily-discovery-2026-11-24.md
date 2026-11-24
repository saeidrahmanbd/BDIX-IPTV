# Daily IPTV Discovery Report — 2026-11-24

Generated: **2026-11-24 06:55:48 +06:00 (Asia/Dhaka)**  
Repository: [saeidrahmanbd/BDIX-IPTV](https://github.com/saeidrahmanbd/BDIX-IPTV)  
Snapshot checked: `main` at `b6fab9828700c8f5157197b2dd0cc0d48410e47c`

**Overall result: PARTIAL — both discovery workflows completed successfully, but the current playlists still have policy-compliance blockers.** No manual playlist edits were made during this audit.

## 1. IPTV-Playlist.m3u — Bangladesh and India

- Workflow: [IPTV New Channel Discovery run](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/45288773877) — **success**
- Run report: [reports/iptv-channel-discovery.md](https://github.com/saeidrahmanbd/BDIX-IPTV/blob/main/reports/iptv-channel-discovery.md)
- Discovery commit: [73cc72077a2f0c51d169e65b5f96e47026efea56](https://github.com/saeidrahmanbd/BDIX-IPTV/commit/73cc72077a2f0c51d169e65b5f96e47026efea56)
- Sources: Bangladesh and India iptv-org country feeds.
- Source candidates rejected/held: **863**.

### Candidate results

Four primary candidates and five backup candidates were staged for probing:

| Candidate | Result |
|---|---|
| ATN Music (360p) | Removed — HTTP 404 |
| Anmol TV (576p) | Removed — HTTP 404 |
| Captain (576p) | Removed — HTTP 404 |
| Win TV (576p) | Removed — HTTP 404 |
| DD Assam (576p) | Removed — HTTP 404 |
| DD Manipur (576p) | Removed — HTTP 404 |
| DD Nagaland (576p) | Removed — HTTP 404 |
| DD Tripura (576p) | Removed — HTTP 404 |
| Vanitha TV (576p) | Removed — HTTP 404 |

**Added today: 0 primary channels; 0 backup streams.** All nine newly discovered stream URLs failed with HTTP 404 and were removed. The existing queues remain present in the current playlist: 9 New Channels and 9 New Backups; those are not counted as today's additions.

Largest source rejection categories:
- Duplicate stream URL: 326
- Indian News: 304
- Indian non-Islamic Religious: 122
- Permanently banned candidates: 30
- Unsupported stream path: 20
- Indian Kids: 14
- Indian Business: 9
- Indian Education: 7
- Tokenized URL: 10

Other rejections included duplicate queued identities, prohibited Indian brands, and out-of-scope country records. Indian sports remained eligible.

## 2. International-Playlist.m3u

- Workflow: [International Channel Discovery run](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/45290229566) — **success**
- Run report: [reports/international-channel-discovery.md](https://github.com/saeidrahmanbd/BDIX-IPTV/blob/main/reports/international-channel-discovery.md)
- Discovery commit: [a532a36be431259551dbcba5c185cffa19666ced](https://github.com/saeidrahmanbd/BDIX-IPTV/commit/a532a36be431259551dbcba5c185cffa19666ced)
- Source: iptv-org category feed.
- Source records parsed: **12,152**
- Existing playlist records at scan: **3,314**
- New eligible source records after URL/policy filtering: **139**
- New primary candidates staged: **50**
- New backup candidates staged: **4**

### Verified additions retained

**New Channels — 3 verified primary channels**
- Aurora Media Films (720p)
- FMH Movies
- Kinosvidanie

**New Backups — 8 verified alternate streams**
- Cinema (Russia)
- Dom kino
- Dorama
- iFilm Persian
- Indiyskoye Kino
- KinoHit
- Muzyka Pervogo
- TRT Muzik

### Held candidates and probe results

- **Galaxy** — inconclusive probe (`URLError`); current URL host is `proxy-v.rctiplus.id`.
- **Galaxy Premium** — inconclusive probe (`URLError`); current URL host is `proxy-v.rctiplus.id`.

The workflow retained both in New Channels for manual review. They are **not verified live streams**, and the proxy-named host conflicts with the strict no-proxy rule. They remain a policy blocker and must not be counted as accepted additions.

Across 66 probed rows:
- Verified live media responses: **11**
- Verified new primary channels retained: **3**
- Verified alternate streams retained: **8**
- Inconclusive candidates retained: **2**
- Definitively dead or invalid candidates removed: **53**
- Adult channels added directly to Adult: **0**
- Fashion TV channels added directly to Fashion TV: **0**
- Country-group migrations: **0**

Existing Adult and Fashion TV groups remain intact (366 and 5 entries respectively). The five-primary-country threshold was respected; no new country group was created below threshold.

Major source rejection categories included non-Movie/Music categories (6,584), News (1,081), Religious (782), Kids (309), Sports (303), Documentary/Wildlife (195), unsafe/tokenized URLs (139), test/VOD/non-TV names (299), general entertainment (67), and TV series (24).

## 3. Current playlist snapshot and validation

The following checks were run against the current files on `main`, not copied from an older report.

| Check | IPTV-Playlist.m3u | International-Playlist.m3u |
|---|---:|---:|
| EXTINF entries | 1,350 | 3,315 |
| Malformed EXTINF/URL pairs | 0 | 0 |
| Duplicate stream URLs | 0 | 0 |
| Duplicate primary channel IDs | 0 | 0 |
| Relative `logos/...` logo paths | 411 | 8 |
| HTTP(S) `tvg-logo` references | 939 | 2,884 |
| Empty logo fields | 0 | 423 |

### Queue placement

- IPTV: New Channels (9) → New Backups (9) → Backup (410) → Review (206). Both queues are immediately before Backup.
- International: Review (630) → New Channels (5) → New Backups (8) → Backup (365). Both queues are immediately before Backup.

No duplicate stream URLs or duplicate primary channel IDs were found. There are same-name/different-ID review signals (8 in IPTV and 15 in International); these were not automatically merged because they may be distinct regional or feed variants.

### Outstanding policy blockers

1. **Logo URL/local-path policy is not satisfied playlist-wide.** The current files still contain 939 and 2,884 HTTP(S) logo references. The latest provenance manifest reports 0 officially verified logos; IPTV has 21 third-party-verified, 2 generated fallbacks and 1,327 needing review; International has 985 third-party-verified and 2,330 needing review. For today's 11 retained International candidates, only iFilm Persian, Indiyskoye Kino and KinoHit have third-party-verified provenance; the other eight logo assets are marked `needs_review`. The discovery validator's “no missing/non-local discovery logos” result is therefore not equivalent to an authenticity/provenance pass.
2. **International legacy content remains outside the requested genre scope.** Existing groups still include News (11), Documentary & Wildlife (129), Kids (149), Religious (30), Sports (183), and Indian Entertainment (175). The discovery workflow filtered new source candidates but did not broadly delete or reclassify existing entries, in order to preserve unrelated playlist content.
3. **Existing token-like stream URLs need review.** A conservative query-parameter scan found 12 International rows: CCTV-Storm Music, CCTV-Storm Theater, CCTV-The First Theater, Dorama, Kinoseriya, CCTV-Weapon & Technology, CCTV-Billiards, CCTV-Golf & Tennis, CCTV-Storm Football, EBC Foreign Movie, QTV-3, and FashionTV Secrets. FashionTV Secrets' match is an ad-macro parameter; the other 11 auth/token/key matches require review. These are existing rows, not today's verified additions.
4. **Two inconclusive proxy-hosted candidates remain in International New Channels:** Galaxy and Galaxy Premium. They should not be treated as verified additions under the no-proxy rule.

No unrelated channels were removed, reclassified, or rewritten by this audit.

## 4. Conclusion

- IPTV discovery: workflow passed; **no justified additions** because all nine probed candidates returned HTTP 404.
- International discovery: workflow passed; **3 verified new primaries and 8 verified backup streams** retained; 2 proxy-hosted/inconclusive candidates remain a policy exception.
- Structural checks and queue placement: passed.
- Full playlist policy compliance: **not passed** because of legacy genre rows, external logo URL/provenance issues, existing token-like URLs, and the two inconclusive proxy-hosted candidates.

The detailed stage reports above contain the full source rejection and stream-probe logs.
