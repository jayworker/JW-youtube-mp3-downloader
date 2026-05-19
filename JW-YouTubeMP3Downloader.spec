# -*- mode: python ; coding: utf-8 -*-
import sys
from PyInstaller.utils.hooks import collect_submodules

is_mac = sys.platform == 'darwin'
is_win = sys.platform == 'win32'

hiddenimports = collect_submodules('yt_dlp')

if is_win:
    datas = [('vendor/ffmpeg.exe', 'vendor'), ('vendor/ffprobe.exe', 'vendor')]
elif is_mac:
    datas = [('vendor/ffmpeg', 'vendor'), ('vendor/ffprobe', 'vendor')]
else:
    datas = []


a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='JW-YouTubeMP3Downloader',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='JW-YouTubeMP3Downloader',
)

if is_mac:
    app = BUNDLE(
        coll,
        name='JW-YouTubeMP3Downloader.app',
        icon=None,
        bundle_identifier='com.jayworker.jw-youtubemp3downloader',
        info_plist={
            'NSHighResolutionCapable': True,
            'CFBundleShortVersionString': '1.0.0',
            'LSMinimumSystemVersion': '11.0',
        },
    )
