# International Playlist Organization Audit

- Entries before: 3303
- Entries after: 3303
- Channel names normalized: 11
- Malformed HTTP options moved into VLC directives: 0
- Invalid/external logo references removed: 2919
- Exact duplicate URLs omitted: 0
- Additional same-channel streams moved to Backup: 0
- Original Backup/Backups and protected queue rows examined: 1480
- Matching alternate streams retained in Backup: 371
- True orphan Backup rows evaluated: 4
- Eligible orphan Backup rows promoted to primary: 3
- Clearly identified Adult orphans restored to Adult: 0
- Ineligible/unclassified orphan Backup rows retained: 1
- Genre groups (News, Sports, Kids, Religious, Documentary & Wildlife, Fashion TV and Adult) take precedence over country groups for every country; country groups contain only eligible non-genre Movies/Music/region-specific channels.
- Outside the dedicated genre groups, countries other than Bangladesh, India and Pakistan use Movies/Music-only country groups.
- Every country except Bangladesh and India, including Pakistan, requires five unique primary channel identities before a dedicated country group is used.
- Eligible orphan Backup rows without a matching primary identity are migrated to their country/genre primary group; matching alternates remain in Backup. Unclassifiable orphans are retained for manual review.
- Adult rows are preserved in Adult; clearly identified Adult orphans are restored to Adult rather than filtered by foreign genre rules.
- New Channels and New Backups remain manual-review queues; candidates are never automatically promoted.
- Retained stream URLs are preserved; playback/availability was not tested.

## Removal summary


## Protected Backup/Review/Not Playing entries preserved (policy would have removed them)

- test/VOD/non-TV name: 1

## Category counts

- Bangladesh: 47
- Indian Bangla: 32
- Indian Movies: 76
- Indian Music: 59
- Indian Entertainment: 169
- Pakistani: 19
- Argentina: 14
- Brazil: 15
- Bulgaria: 21
- Canada: 31
- Chile: 11
- China: 9
- Colombia: 8
- Costa Rica: 9
- Czech Republic: 22
- DO: 11
- Estonia: 6
- France: 45
- Germany: 72
- Greece: 8
- Hungary: 15
- Iran: 13
- Italy: 25
- Lebanon: 6
- Mexico: 17
- Netherlands: 17
- North Macedonia: 5
- Panama: 5
- Paraguay: 5
- Peru: 8
- Poland: 24
- Romania: 28
- Russia: 76
- Saudi Arabia: 9
- Singapore: 5
- Spain: 18
- Sweden: 49
- Turkey: 15
- Ukraine: 28
- United Kingdom: 21
- United States: 239
- Uzbekistan: 5
- Vietnam: 6
- International: 101
- News: 12
- Kids: 13
- Religious: 3
- Sports: 8
- Adult: 366
- Review: 1105
- Backup: 372
