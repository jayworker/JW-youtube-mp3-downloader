#requires -Version 5.1
<#
    fetch_ffmpeg.ps1
    Downloads a Windows FFmpeg "essentials" build from gyan.dev and extracts
    ffmpeg.exe / ffprobe.exe into the vendor/ directory.

    FFmpeg is LGPL/GPL licensed — see NOTICE.md. This script only fetches it;
    it does not redistribute it. If you ship a built artifact that bundles
    these binaries, comply with the relevant FFmpeg license terms.
#>

$ErrorActionPreference = 'Stop'

$repoRoot  = Split-Path -Parent $PSScriptRoot
$vendorDir = Join-Path $repoRoot 'vendor'
$tmpDir    = Join-Path $env:TEMP ("ffmpeg_fetch_" + [Guid]::NewGuid().ToString('N'))
$zipPath   = Join-Path $tmpDir 'ffmpeg.zip'
$url       = 'https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip'

New-Item -ItemType Directory -Force -Path $vendorDir | Out-Null
New-Item -ItemType Directory -Force -Path $tmpDir    | Out-Null

Write-Host "Downloading FFmpeg from $url ..." -ForegroundColor Cyan
Invoke-WebRequest -Uri $url -OutFile $zipPath -UseBasicParsing

Write-Host "Extracting ..." -ForegroundColor Cyan
Expand-Archive -Path $zipPath -DestinationPath $tmpDir -Force

$ffmpeg  = Get-ChildItem -Path $tmpDir -Recurse -Filter 'ffmpeg.exe'  | Select-Object -First 1
$ffprobe = Get-ChildItem -Path $tmpDir -Recurse -Filter 'ffprobe.exe' | Select-Object -First 1

if (-not $ffmpeg -or -not $ffprobe) {
    throw "ffmpeg.exe or ffprobe.exe not found inside the downloaded archive."
}

Copy-Item $ffmpeg.FullName  (Join-Path $vendorDir 'ffmpeg.exe')  -Force
Copy-Item $ffprobe.FullName (Join-Path $vendorDir 'ffprobe.exe') -Force

Remove-Item $tmpDir -Recurse -Force

Write-Host "Done. vendor/ffmpeg.exe and vendor/ffprobe.exe are ready." -ForegroundColor Green
