from pathlib import Path

# Safe preflight only: no files or playlist references are changed.
playlist = Path('NVisionBD-Playlist.m3u')
if not playlist.exists():
    raise SystemExit('NVisionBD-Playlist.m3u is missing')
text = playlist.read_text(encoding='utf-8', errors='replace')
count = sum(1 for p in Path('logos').glob('*.svg') if 'CHANNEL MARK' in p.read_text(encoding='utf-8', errors='ignore').upper())
print(f'Playlist readable; generic CHANNEL MARK SVG files found: {count}')
print('Preflight only. No logos downloaded or replaced.')
