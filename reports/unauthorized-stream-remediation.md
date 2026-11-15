# Unauthorized Third-Party Stream Credential Remediation

**Status:** Prepared for review; not merged  
**Scope:** Public IPTV playlist and generated audit reports  
**Policy:** Stream URLs found publicly are not treated as permission to redistribute them.

## Findings

The current `IPTV-Playlist.m3u` contained eight distinct entries with opaque third-party tokenized playback URLs. The affected channel identities were:

- Madani TV
- Deepto TV
- 9X Jalwa
- Dangal
- Independent TV
- Manoranjan TV
- Shemaroo TV
- The Q

Copies of these credential-bearing URLs were also present in:
- `reports/iptv-playlist-audit.md`
- `reports/iptv-fragile-streams.md`

## Actions in this change

1. Removed the eight affected stream entries from the public IPTV playlist. No unrelated playlist entries, channel IDs, groups, numbering, logos, or other stream URLs were intentionally changed.
2. Redacted the credential-bearing URL values from the two reports while retaining their surrounding audit context.
3. Preserved the affected channel names in this remediation record so they can be matched to authorized replacement sources later.

## Deliberately not changed

- The two International playlist entries using a generic `token=onlinetv` query value were not treated as the same opaque credentials. Their authorization and redistribution status still need independent verification.
- No provider credentials were tested, renewed, rotated, or reused.
- No unrelated stream URLs were changed.

## Required follow-up

1. Review the repository's full Git history and any cached public artifacts for historical copies. This pull request only cleans the current branch state; it does **not** erase old commits or forks.
2. If historical credentials remain exposed, decide on a coordinated history rewrite. This is a disruptive repository operation and should be performed separately with a backup and contributor notice.
3. Do not restore any affected channel stream until a source grants explicit redistribution permission or a clearly authorized replacement is found.
4. Add a publication gate that rejects newly introduced opaque credential-bearing URLs while allowing reviewed public parameters that are not credentials.
5. Re-run playlist audit, maintenance, EPG, and publication workflows after merge.

## Verification boundary

This remediation removes the currently identified opaque tokenized stream URLs and their copies in the two reports. It does not certify the legal status of every other playlist stream or historical commit.
