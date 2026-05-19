#!/usr/bin/env bash
# fetch_ffmpeg.sh
# Downloads static FFmpeg builds for macOS from evermeet.cx and extracts
# the ffmpeg / ffprobe binaries into vendor/.
#
# FFmpeg is LGPL/GPL licensed — see NOTICE.md. This script only fetches it;
# it does not redistribute it. If you ship a built artifact that bundles
# these binaries, comply with the relevant FFmpeg license terms.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
VENDOR_DIR="$REPO_ROOT/vendor"
TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT

mkdir -p "$VENDOR_DIR"

echo "Downloading FFmpeg (macOS) from evermeet.cx ..."
curl -fL -o "$TMP_DIR/ffmpeg.zip"  "https://evermeet.cx/ffmpeg/getrelease/ffmpeg/zip"
curl -fL -o "$TMP_DIR/ffprobe.zip" "https://evermeet.cx/ffmpeg/getrelease/ffprobe/zip"

echo "Extracting ..."
unzip -q "$TMP_DIR/ffmpeg.zip"  -d "$TMP_DIR"
unzip -q "$TMP_DIR/ffprobe.zip" -d "$TMP_DIR"

cp "$TMP_DIR/ffmpeg"  "$VENDOR_DIR/ffmpeg"
cp "$TMP_DIR/ffprobe" "$VENDOR_DIR/ffprobe"
chmod +x "$VENDOR_DIR/ffmpeg" "$VENDOR_DIR/ffprobe"

echo "Done. $VENDOR_DIR/ffmpeg and $VENDOR_DIR/ffprobe are ready."
