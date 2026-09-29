#!/bin/sh
set -eu
mkdir -p /hls
for item in channel9 duronto-tv jtv-classic sony-max-2-us star-gold-thrills zee-action ary-music big-magic zee-anmol star-movies tlc sonic-bangla astro-cricbuzz fox-cricket-501 sony-sports-ten-3 star-sports-sl-2 ten-sports-hd ekattor-tv independent-tv mohona-tv star-jalsha travelxp-bangla; do
  url=$(printenv "SOURCE_$item" || true)
  [ -n "$url" ] || { echo "Missing SOURCE_$item" >&2; continue; }
  (
    mkdir -p "/hls/$item"
    while :; do
      ffmpeg -hide_banner -loglevel warning         -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 10         -user_agent "Mozilla/5.0" -i "$url"         -map 0:v:0? -map 0:a:0? -c copy         -f hls -hls_time 4 -hls_list_size 6         -hls_flags delete_segments+independent_segments+temp_file         -hls_delete_threshold 2         -hls_segment_filename "/hls/$item/seg_%06d.ts"         "/hls/$item/index.m3u8" || true
      sleep 3
    done
  ) &
done
wait
