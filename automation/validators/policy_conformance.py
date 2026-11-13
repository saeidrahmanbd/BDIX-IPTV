"""Dependency-free structural checks for the V2 machine-readable policy."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
POLICY_PATH = ROOT / "automation" / "policy" / "policy.json"

def validate_policy(policy):
    errors = []
    if policy.get("timezone") != "Asia/Dhaka":
        errors.append("timezone must be Asia/Dhaka")
    playlists = policy.get("playlists", {})
    iptv = playlists.get("IPTV-Playlist.m3u", {})
    intl = playlists.get("International-Playlist.m3u", {})
    if iptv.get("owner") != "owner_curated":
        errors.append("IPTV playlist must remain owner-curated")
    protected = iptv.get("existing_rows", {})
    for field in ("stream_urls", "group_title", "channel_number", "relative_order"):
        if protected.get(field) != "immutable":
            errors.append(f"IPTV existing {field} must be immutable")
    if protected.get("deletion") != "forbidden" or protected.get("url_replacement") != "forbidden":
        errors.append("IPTV deletion and URL replacement must be forbidden")
    if intl.get("owner") != "automation_controlled":
        errors.append("International playlist must remain automation-controlled")
    failure = intl.get("failure_policy", {})
    if failure.get("consecutive_definitive_failed_days_before_removal") != 3:
        errors.append("International removal threshold must be three consecutive days")
    if failure.get("first_definitive_failed_day_group") != "Review":
        errors.append("First definitive failure must move to Review")
    if intl.get("country_groups", {}).get("minimum_unique_primary_identities") != 5:
        errors.append("Country groups require five unique primary identities")
    shared = policy.get("shared", {})
    if shared.get("candidate_outputs_only_until_all_gates_pass") is not True:
        errors.append("Candidate-only publication gate must be enabled")
    if shared.get("new_channels_and_new_backups_xtream_visible") is not False:
        errors.append("Discovery queues must be hidden from Xtream")
    return errors

def main():
    policy = json.loads(POLICY_PATH.read_text(encoding="utf-8"))
    errors = validate_policy(policy)
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    print("Automation V2 policy: PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
