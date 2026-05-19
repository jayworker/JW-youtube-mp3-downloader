# Third-Party Notices

This project builds on top of the following open-source software.
The wrapper code in this repository is MIT-licensed (see `LICENSE`),
but the components below retain their own licenses.

---

## yt-dlp

- Source: https://github.com/yt-dlp/yt-dlp
- License: The Unlicense (public domain dedication)
- Role: Provides the entire YouTube extraction and download engine.
  This program is essentially a small GUI on top of `yt-dlp`.

All credit for the actual download functionality goes to the yt-dlp
maintainers and contributors.

---

## FFmpeg

- Source: https://ffmpeg.org/
- License: LGPL v2.1+ (some builds GPL v2+ depending on enabled components)
- Role: Used as an external binary (`ffmpeg.exe`, `ffprobe.exe`) for
  decoding YouTube audio streams and encoding them to MP3.

FFmpeg binaries are **not** included in this Git repository. They are
downloaded at build time by `scripts/fetch_ffmpeg.ps1` from
https://www.gyan.dev/ffmpeg/builds/ (a widely used Windows build host).

If you redistribute a packaged build that bundles FFmpeg, you are
responsible for complying with the relevant FFmpeg license terms,
including making the corresponding source available where required.

---

## Python standard library / Tk

The GUI uses Python's built-in `tkinter`, which is part of the standard
Python distribution and covered by the PSF license.
