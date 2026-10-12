#!/usr/bin/env bash
# Baut das Carport-Reel: Szene 2 als Zeitlupe (2.17s -> 3.5s), Overlay-Grafiken, Instagram-Export.
# Usage: build.sh <source.mp4> <overlay_frames_dir> <work_dir> <out.mp4>
set -euo pipefail
SRC=$1 OV=$2 WORK=$3 OUT=$4

ffmpeg -v error -y -i "$SRC" -vf "trim=start_frame=48:end_frame=100,setpts=(PTS-STARTPTS)*87/52,minterpolate=fps=24:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1,trim=end_frame=84,setpts=PTS-STARTPTS" \
  -c:v libx264 -crf 12 -preset fast -an "$WORK/s2_slow.mp4"

ffmpeg -v error -y -i "$SRC" -i "$WORK/s2_slow.mp4" -framerate 24 -i "$OV/o_%04d.png" -filter_complex "\
[0:v]setsar=1,format=yuv420p,split[v0][v1];[v0]trim=start_frame=0:end_frame=48,setpts=PTS-STARTPTS[va];[1:v]setsar=1,format=yuv420p,setpts=PTS-STARTPTS[vs];[v1]trim=start_frame=100,setpts=PTS-STARTPTS[vb];[va][vs][vb]concat=n=3:v=1:a=0[b];\
[b][2:v]overlay=0:0:format=auto,format=yuv420p[v];\
[0:a]asplit=3[a0][a1][a2];[a0]atrim=0:2,asetpts=PTS-STARTPTS,afade=t=out:st=1.97:d=0.03[aa];[a1]atrim=2:4.166667,asetpts=PTS-STARTPTS,atempo=52/84,afade=t=in:d=0.03,afade=t=out:st=3.47:d=0.03[as];[a2]atrim=start=4.166667,asetpts=PTS-STARTPTS,afade=t=in:d=0.03[ab];[aa][as][ab]concat=n=3:v=0:a=1,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[a]" \
  -map "[v]" -map "[a]" -c:v libx264 -profile:v high -level 4.2 -preset slow -crf 17 -maxrate 14M -bufsize 28M -pix_fmt yuv420p -r 24 -g 48 \
  -c:a aac -b:a 192k -ar 48000 -ac 2 -movflags +faststart -t 11.375 -color_primaries bt709 -color_trc bt709 -colorspace bt709 "$OUT"
