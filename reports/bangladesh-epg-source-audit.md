# Bangladesh EPG Source Audit

Checked: **2026-10-11**
Scope: public XMLTV feeds and channel-ID catalogues for the Bangladesh-group channels in IPTV-Playlist.m3u, BDIX-Playlist.m3u, and NVisionBD-Playlist.m3u.

## Result

**No reliable Bangladesh-domestic XMLTV feed was verified in the public sources checked.** I found no current source whose XMLTV channel IDs and programme data could safely be mapped to the local `.bd` identities. Therefore, this audit does not add mappings, alter playlist IDs, or synthesize programme data.

This is a negative finding for the sources checked, not proof that no private or broadcaster-internal feed exists.

## Source checks

| Source | Result | Decision |
|---|---|---|
| [epg.pw XMLTV guide catalogue](https://epg.pw/xmltv.html?lang=en) | The published country-feed list includes a range of country feeds (including India) but no Bangladesh feed. | No Bangladesh feed to add. |
| [epgshare01 directory](https://epgshare01.online/epgshare01/) and its [source-ID readme](https://epgshare01.online/epgshare01/0_READ_ME_FIRST_AS_I_CONTAIN_VERY_HELPFUL_INFO.html) | The directory publishes per-source `.xml.gz` files and matching `.txt` channel-ID lists. No dedicated `epg_ripper_BD1`/Bangladesh feed was found. The combined catalogue did not contain exact native IDs such as `ATNBangla.bd`, `ChannelI.bd`, `NTV.bd`, `JamunaTV.bd`, or `SomoyNewsTV.bd`. | Do not map native Bangladesh IDs from Indian or diaspora lookalikes. The all-sources archive is very large and is not a safe substitute for an exact source. |
| [iptv-org/epg source catalogue](https://github.com/iptv-org/epg/tree/master/sites) and [guide status list](https://github.com/iptv-org/epg/blob/master/GUIDES.md) | No live public Bangladesh-local guide was verified. Some stale source configuration mentions Canadian service variants; the matching CA1 listing endpoint currently returns 404. | Treat CA1 entries as leads only, not an active feed. |

## Exact IDs found in a currently listed diaspora feed

The current [epgshare01 ASIANTELEVISION1 ID list](https://epgshare01.online/epgshare01/epg_ripper_ASIANTELEVISION1.txt) is dated `202610110538` and lists these exact XMLTV channel IDs:

| XMLTV channel ID | Catalogue label/context | Possible playlist counterpart | Status |
|---|---|---|---|
| `ATN.Bangla.ca` | ATN Bangla, Canada service/feed | `ATNBangla.bd` | **Unverified equivalent** — do not map automatically. |
| `Channel.I.Bangla.ca` | Channel I Bangla, Canada service/feed | `ChannelI.bd` | **Unverified equivalent** — do not map automatically. |
| `ATN.Colors.Bangla.ca` | ATN Colors Bangla | None; this is not the native Bangladesh ATN Bangla service | **Exclude**. |

The same-name Canadian services may have different schedules, regional inserts, or time alignment. An ID's presence in a catalogue proves only that the source identifies a channel; it does **not** prove that its programmes and start times match the Bangladesh-local stream. The feed's ID catalogue was checked, but its programme rows were not independently compared against a broadcaster-published Bangladesh schedule. These two candidates are therefore not counted as verified mappings.

### Stale CA1 leads (not accepted)

The [iptv-org/epg CA1 channel configuration](https://github.com/iptv-org/epg/blob/master/sites/epgshare01.online/epgshare01.online_CA1.channels.xml) contains scraper-specific identifiers:
- `CA1#Channel.i.(Bangladesh).ca`
- `CA1#ATN.-.Bangla.ca`
- `CA1#NTV.Bangla.ca`

These are source/site identifiers, not verified native `.bd` IDs; the corresponding `epg_ripper_CA1.txt` endpoint returned 404 during this check. They are excluded from eligible sources until a live feed and current programme data can be verified.

The active UK1 list also includes `IQRA.BANGLA.uk`, but that is a UK service ID and is not a substitute for schedules for Bangladesh-local channels.

## Playlist channel identities to preserve

The three playlists already use native/custom identities such as `ATNBangla.bd`, `ATNNews.bd`, `BanglaVision.bd`, `BTVNational.bd`, `Channel24.bd`, `ChannelI.bd`, `DBCNews.bd`, `DeeptoTV.bd`, `EkattorTV.bd`, `JamunaTV.bd`, `MaasrangaTV.bd`, `NTV.bd`, `News24.bd`, `RTV.bd`, `SATV.bd`, and `SomoyNewsTV.bd`. These playlist IDs should remain unchanged unless a verified source supplies programme data for the exact same channel/service.

## Acceptance rules for future discoveries

A feed can be promoted to the production source list only after all of the following are demonstrated:

1. The source URL responds with valid XMLTV and contains real `<programme>` rows, not only channel declarations.
2. The exact source channel ID is present in the XMLTV `<channel id>` set and has current/future programmes.
3. Several programme titles and start/end times match an official broadcaster schedule or a trusted local schedule for the same Bangladesh service.
4. The time zone and any regional/time-shift version are accounted for.
5. The match is added as a narrow, explicit mapping; no fuzzy-name or India-channel fallback is used.

Until then, native Bangladesh channel guide coverage should remain reported as missing rather than being filled with guessed or mismatched programmes.
