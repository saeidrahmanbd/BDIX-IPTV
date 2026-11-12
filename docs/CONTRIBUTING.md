# Contributing to BDIX-IPTV

Thanks for helping improve the project.

## Before changing playlists

- Preserve the `#PLAYLIST-STUDIO-CATEGORIES` registry and canonical category order.
- For `IPTV-Playlist.m3u`, automation may repair metadata and authentic local logos, diagnose blocked/broken streams, improve EPG mappings and stage eligible discoveries in `New Channels` / `New Backups`. It must never delete/replace an existing stream, change an existing group assignment or channel number, reorder existing rows, or promote discovery/review rows.
- For `International-Playlist.m3u`, automation has full policy-based authority to add, filter, delete, move, migrate, deduplicate and reorganize channel rows, including backup reconciliation.
- Do not remove Backup or review-queue entries from the main IPTV playlist solely because an automated health check failed.
- Keep New Channels and New Backups populated by discovery workflows; apply each playlist's separate approval and promotion rules.
- Use local repository logos only in published playlists.
- Follow the regional discovery policy: Bangladesh allows all genres; India excludes News, all Religious (including Islamic), Educational, Business/Finance and Farming, and allows Kids and Sports; Pakistan excludes News, all Religious, Educational, Business/Finance, Farming, Kids and Sports; other countries in the International playlist allow Movies/Music only.
- Avoid duplicate stream URLs.
- Keep channel identity, country, language, group, and display-name metadata consistent.
- Treat signed, tokenized, session-specific, and rendition-only URLs as review items rather than proof of independent redundancy.

## Automation changes

See [Playlist Automation Policy](PLAYLIST-AUTOMATION-POLICY.md) for the mandatory per-playlist permission boundary.

When modifying a workflow or script:

1. Verify every referenced script or file exists.
2. Keep main-branch playlist writers on the shared `iptv-playlist-main-writer-v4` concurrency group.
3. Run the relevant tests and pre-publish gate.
4. Update documentation when policy or category behavior changes.
5. Do not commit credentials, API keys, private tokens, or session URLs.

## Pull requests

Describe the affected playlist, workflow, or report and explain any intentional metadata or stream changes. For generated reports, update the generating script rather than hand-editing a value that will immediately be regenerated.
