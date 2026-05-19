"""YouTube audio downloader core (yt-dlp wrapper, converts to mp3 with bundled ffmpeg)."""
from __future__ import annotations

import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Optional

import yt_dlp


def _bundle_dir() -> Path:
    # When packaged by PyInstaller in --onefile mode, resources are unpacked to sys._MEIPASS.
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS)
    return Path(__file__).resolve().parent


def ffmpeg_location() -> Optional[str]:
    """Return the directory containing the bundled ffmpeg binary, or None if missing."""
    binary = "ffmpeg.exe" if sys.platform == "win32" else "ffmpeg"
    candidate = _bundle_dir() / "vendor" / binary
    if candidate.exists():
        return str(candidate.parent)
    return None


@dataclass
class DownloadResult:
    title: str
    filepath: str


def download(
    url: str,
    output_dir: str | os.PathLike[str] = "downloads",
    audio_quality: str = "0",
    progress_hook: Optional[Callable[[dict], None]] = None,
) -> DownloadResult:
    out_dir = Path(output_dir).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    ydl_opts: dict = {
        "format": "bestaudio/best",
        "outtmpl": str(out_dir / "%(title)s.%(ext)s"),
        "quiet": True,
        "no_warnings": True,
        "noplaylist": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": audio_quality,
            }
        ],
    }

    ff = ffmpeg_location()
    if ff:
        ydl_opts["ffmpeg_location"] = ff

    if progress_hook is not None:
        ydl_opts["progress_hooks"] = [progress_hook]

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        title = info.get("title", "audio")
        final_path = out_dir / f"{title}.mp3"

    return DownloadResult(title=title, filepath=str(final_path))
