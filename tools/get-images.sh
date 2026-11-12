#!/bin/bash
# Downloads the Lab's images from Squarespace into static/images/legacy.
# Run from the site folder:  bash tools/get-images.sh
# Must be run BEFORE the Squarespace subscription is cancelled.
cd "$(dirname "$0")/.." || exit 1
mkdir -p static/images/legacy
ok=0; fail=0
tail -n +2 tools/images.csv | tr -d '\r' | while IFS=, read -r url path; do
  [ -s "$path" ] && continue
  if curl -fsSL --retry 2 -o "$path" "$url"; then ok=$((ok+1)); else echo "FAILED: $url"; rm -f "$path"; fi
done
echo "Done. $(ls static/images/legacy | wc -l) images in static/images/legacy (expected $(($(wc -l < tools/images.csv)-1)))."
