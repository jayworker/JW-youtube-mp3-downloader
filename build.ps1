#requires -Version 5.1
<#
    build.ps1
    One-shot build script: ensures FFmpeg is present in vendor/, then runs
    PyInstaller against YouTubeMP3Downloader.spec.

    Output: dist/JW-YouTubeMP3Downloader/
#>

$ErrorActionPreference = 'Stop'
$repoRoot = $PSScriptRoot

$ffmpeg = Join-Path $repoRoot 'vendor\ffmpeg.exe'
if (-not (Test-Path $ffmpeg)) {
    Write-Host "FFmpeg not found in vendor/. Fetching ..." -ForegroundColor Yellow
    & (Join-Path $repoRoot 'scripts\fetch_ffmpeg.ps1')
}

Write-Host "Running PyInstaller ..." -ForegroundColor Cyan
& python -m PyInstaller --noconfirm (Join-Path $repoRoot 'JW-YouTubeMP3Downloader.spec')

Write-Host "Done. Built artifact: dist\JW-YouTubeMP3Downloader\" -ForegroundColor Green
