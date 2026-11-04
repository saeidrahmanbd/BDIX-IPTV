# Contributing to BDIX-IPTV

Thanks for helping improve the project.

## Before changing playlists

- Preserve the `#PLAYLIST-STUDIO-CATEGORIES` registry and canonical category order.
- Do not remove an existing primary stream silently.
- Do not remove Backup or review-queue entries solely because an automated health check is inconclusive; remove only definitively dead/invalid streams or explicitly prohibited candidates.
- Keep `New Channels` and `New Backups` as manual-review queues. IPTV candidates must be BD/IN and follow the India exclusions; International BD/IN candidates follow the same rules, while all other countries must be Movie/Music only. Never auto-promote either review queue.
- Use local repository logos only in published playlists.
- Avoid duplicate stream URLs.
- Keep channel identity, country, language, group, and display-name metadata consistent.
- Treat signed, tokenized, session-specific, and rendition-only URLs as review items rather than proof of independent redundancy.

## Automation changes

When modifying a workflow or script:

1. Verify every referenced script or file exists.
2. Keep main-branch playlist writers on the shared `iptv-playlist-main-writer-v3` concurrency group.
3. Run the relevant tests and pre-publish gate.
4. Update documentation when policy or category behavior changes.
5. Do not commit credentials, API keys, private tokens, or session URLs.

## Pull requests

Describe the affected playlist, workflow, or report and explain any intentional metadata or stream changes. For generated reports, update the generating script rather than hand-editing a value that will immediately be regenerated.
