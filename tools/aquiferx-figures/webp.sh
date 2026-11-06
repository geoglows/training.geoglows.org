#!/usr/bin/env bash
# Convert raw/*.png to the WebP copies the pages use: at most 1800 px wide, quality 86.
set -euo pipefail
out=../../docs/static/images/aquiferx
mkdir -p "$out"
for f in raw/*.png; do
  w=$(sips -g pixelWidth "$f" | awk '/pixelWidth/{print $2}')
  resize=(-resize 0 0); [ "$w" -gt 1800 ] && resize=(-resize 1800 0)
  cwebp -quiet -q 86 "${resize[@]}" "$f" -o "$out/$(basename "${f%.png}").webp"
done
ls "$out"
