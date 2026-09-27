"""Fail closed before publication; retain the last working guide on failures."""
import argparse
import gzip
import json
import re
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAYLIST = ROOT / 'IPTV-Playlist.m3u'


def mappings():
    root = ET.parse(ROOT / 'epg/channels.xml').getroot()
    channels = list(root.findall('channel'))
    ids = [c.attrib['xmltv_id'] for c in channels]
    assert channels and len(ids) == len(set(ids)), 'Missing or duplicate channel mappings'
    playlist_ids = set(re.findall(r'tvg-id="([^"]+)"', PLAYLIST.read_text(encoding='utf-8-sig')))
    assert set(ids) <= playlist_ids, 'A mapped ID does not exist in the playlist'
    return channels, set(ids)


def check_policy():
    channels, _ = mappings()
    policy = json.loads((ROOT / 'epg/source-policy.json').read_text())
    assert all(policy.get(k) is True for k in (
        'approved_for_automated_access', 'approved_for_public_redistribution', 'feed_mapping_verified'
    )), 'EPG is inactive: source permissions and regional feed mappings must be established first'
    assert policy.get('permission_evidence', '').strip(), 'Record the source permission evidence'
    assert {c.attrib['site'] for c in channels} <= set(policy['sites']), 'Unapproved guide source'
    print('Source policy and mappings passed')


def validate_guide(path):
    _, wanted = mappings()
    data = Path(path).read_bytes()
    assert len(data) < 32 * 1024 * 1024, 'Pilot guide unexpectedly large'
    assert b'<!DOCTYPE' not in data.upper() and b'<!ENTITY' not in data.upper(), 'Unexpected XML declarations'
    root = ET.fromstring(data)
    assert root.tag == 'tv', 'Not XMLTV'
    available = [c.attrib.get('id') for c in root.findall('channel')]
    assert len(available) == len(set(available)) and wanted <= set(available), 'Missing or duplicate channel IDs'
    future = set()
    now = datetime.now(timezone.utc)
    programmes = root.findall('programme')
    for programme in programmes:
        cid = programme.attrib.get('channel')
        assert cid in available, 'Programme references an unknown channel'
        start = datetime.strptime(programme.attrib['start'], '%Y%m%d%H%M%S %z')
        stop = datetime.strptime(programme.attrib['stop'], '%Y%m%d%H%M%S %z')
        assert stop > start and programme.findtext('title', '').strip(), 'Invalid programme'
        if stop > now and cid in wanted:
            future.add(cid)
    assert wanted <= future, 'Empty/stale/partial guide: keep previous published guide'
    print(f'Validated {len(wanted)} mapped channels and {len(programmes)} programmes')
    return data


def publish(path, repository):
    check_policy()
    data = validate_guide(path)
    target = ROOT / 'epg.xml.gz'
    temp = target.with_suffix('.tmp')
    temp.write_bytes(gzip.compress(data, mtime=0))
    temp.replace(target)
    text = PLAYLIST.read_text(encoding='utf-8-sig')
    lines = text.splitlines(keepends=True)
    assert lines and lines[0].startswith('#EXTM3U'), 'Missing M3U header'
    header = re.sub(r'\s+(?:url-tvg|x-tvg-url)="[^"]*"', '', lines[0].strip())
    lines[0] = header + f' url-tvg="https://raw.githubusercontent.com/{repository}/main/epg.xml.gz"\n'
    PLAYLIST.write_text('\ufeff' + ''.join(lines), encoding='utf-8')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['mappings', 'policy', 'validate', 'publish'])
    parser.add_argument('--guide')
    parser.add_argument('--repository', default='saeidrahmanbd/BDIX-IPTV')
    args = parser.parse_args()
    if args.mode == 'mappings':
        print('Mapped IDs:', ', '.join(sorted(mappings()[1])))
    elif args.mode == 'policy':
        check_policy()
    elif args.mode == 'validate':
        validate_guide(args.guide)
    else:
        publish(args.guide, args.repository)
