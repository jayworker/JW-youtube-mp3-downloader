# YouTube MP3 Downloader

[![Latest Release](https://img.shields.io/github/v/release/jayworker/JW-youtube-mp3-downloader?label=download&style=for-the-badge&color=f43f5e)](https://github.com/jayworker/JW-youtube-mp3-downloader/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/jayworker/JW-youtube-mp3-downloader/total?style=for-the-badge&color=8b5cf6)](https://github.com/jayworker/JW-youtube-mp3-downloader/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge)](LICENSE)

YouTube 링크를 붙여넣으면 MP3로 변환해 저장해주는 작은 데스크탑 앱입니다.
Python + Tkinter 기반의 가벼운 GUI이며, 다운로드/추출은 전적으로
[**yt-dlp**](https://github.com/yt-dlp/yt-dlp)와 [**FFmpeg**](https://ffmpeg.org/)에
의존합니다.

> **이 앱은 yt-dlp의 얇은 GUI 래퍼입니다.** 실제 다운로드 로직과 사이트 호환성은
> yt-dlp 프로젝트의 작품입니다. 모든 공로는 yt-dlp 메인테이너와 컨트리뷰터에게
> 있습니다.

---

## ⬇ 다운로드

### 🪟 Windows — [한 번에 다운로드 (최신 버전)](https://github.com/jayworker/JW-youtube-mp3-downloader/releases/latest/download/JW-YouTubeMP3Downloader-windows.zip)

1. 위 버튼으로 zip을 받습니다.
2. 압축을 풀고 폴더 안의 **`JW-YouTubeMP3Downloader.exe`**를 더블클릭합니다.
3. YouTube 링크 붙여넣기 → **MP3 다운로드** 버튼.

> 💡 처음 실행 시 "Windows의 PC 보호" 경고가 뜰 수 있습니다.
> 코드 서명을 하지 않은 빌드라서 그렇습니다. **추가 정보 → 실행**을 누르면 동작합니다.

### 🍎 macOS (Apple Silicon) — [한 번에 다운로드 (최신 버전)](https://github.com/jayworker/JW-youtube-mp3-downloader/releases/latest/download/JW-YouTubeMP3Downloader-macos.zip)

1. 위 버튼으로 zip을 받습니다.
2. 압축을 풀고 나오는 **`JW-YouTubeMP3Downloader.app`**을 `응용 프로그램`(Applications) 폴더로 드래그합니다.
3. 처음 실행할 땐 앱을 **마우스 우클릭 → 열기 → 열기**로 실행하세요.
   (Gatekeeper 경고를 우회하는 절차이며, 두 번째부턴 더블클릭으로 그냥 열립니다.)

> 💡 **Apple Silicon (M1/M2/M3/M4) 전용**입니다. Intel Mac은 소스에서 직접
> 실행해 주세요 (아래 [소스에서 직접 실행](#사용-방법--소스에서-직접-실행) 참고).
>
> 💡 Apple 개발자 인증(노터라이즈)을 받지 않은 빌드라 처음 한 번은
> "확인되지 않은 개발자" 경고가 나옵니다. 우클릭 → 열기로 통과시키면 끝.

---

다른 모든 릴리스(이전 버전 포함)는
[Releases 페이지](https://github.com/jayworker/JW-youtube-mp3-downloader/releases)에서 확인하세요.

---

## ⚠️ 사용 전 안내 (Disclaimer)

- 이 도구는 **개인 사용 / 학습 / 본인이 권리를 보유한 콘텐츠의 백업** 용도로만
  제공됩니다.
- YouTube 이용약관은 원칙적으로 콘텐츠 다운로드를 금지합니다
  (YouTube Premium의 오프라인 저장 기능 제외). 본 도구를 사용해 발생하는
  법적·계약상 책임은 전적으로 사용자에게 있습니다.
- 저작권이 있는 음원의 무단 다운로드·재배포는 거주 국가의 저작권법을
  위반할 수 있습니다. 사용 전 본인 관할법을 확인하세요.
- 본인이 만들지 않았거나 라이선스가 없는 음원을 상업적으로 사용·재배포하지
  마세요.

---

## 기능

- YouTube URL → MP3 변환 (단일 영상)
- 저장 경로 지정
- 진행 상황 / 활동 로그 표시
- 다크 테마 GUI
- FFmpeg를 내장하여 별도 설치 없이 동작 (배포 빌드 기준)

---

## 사용 방법 — 소스에서 직접 실행

### 사전 준비

- Python 3.10 이상
- Windows PowerShell (Windows 기준; macOS/Linux에서는 동등한 셸 명령을
  사용하세요)

### 1. 저장소 클론 및 의존성 설치

```powershell
git clone https://github.com/jayworker/JW-youtube-mp3-downloader.git
cd JW-youtube-mp3-downloader

python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. FFmpeg 준비

`vendor/` 폴더에 `ffmpeg.exe`와 `ffprobe.exe`가 필요합니다. 헬퍼 스크립트로
자동 다운로드할 수 있습니다 (Windows 기준):

```powershell
.\scripts\fetch_ffmpeg.ps1
```

이미 시스템에 FFmpeg가 설치되어 PATH에 잡혀 있다면 `vendor/`를 비워두어도
동작합니다.

### 3. 실행

```powershell
python app.py
```

---

## 빌드 (단일 실행 파일 만들기)

### Windows에서 로컬 빌드

```powershell
pip install -r requirements-dev.txt
.\build.ps1
```

`dist\JW-YouTubeMP3Downloader\` 폴더에 결과가 생성됩니다.

### macOS에서 로컬 빌드

```bash
pip install -r requirements-dev.txt
bash scripts/fetch_ffmpeg.sh
python -m PyInstaller --noconfirm JW-YouTubeMP3Downloader.spec
# → dist/JW-YouTubeMP3Downloader.app
```

### 클라우드 빌드 (권장)

본 저장소는 [GitHub Actions 워크플로](.github/workflows/release.yml)를 통해
Windows와 macOS 빌드를 **자동으로 생성**합니다.

- `git tag v1.0.0 && git push --tags` → 양쪽 빌드가 만들어져
  새 Release에 자동 첨부됩니다.
- 또는 Actions 탭에서 "Build & Release" 워크플로를 수동으로 실행하면
  workflow artifact로 결과물을 다운로드할 수 있습니다.

Mac이 없어도 macOS 빌드를 만들 수 있는 유일한 합법적·실용적 경로입니다.

---

## 프로젝트 구조

```
.
├── app.py                          # Tkinter GUI
├── downloader.py                   # yt-dlp 래퍼 (다운로드 핵심)
├── JW-YouTubeMP3Downloader.spec    # PyInstaller 빌드 스펙 (Windows/macOS 공용)
├── build.ps1                       # Windows 원샷 빌드 스크립트
├── scripts/
│   ├── fetch_ffmpeg.ps1            # Windows용 FFmpeg 자동 다운로드
│   └── fetch_ffmpeg.sh             # macOS용 FFmpeg 자동 다운로드
├── .github/workflows/
│   └── release.yml                 # CI: Windows + macOS 동시 빌드 + Release 업로드
├── vendor/                         # ffmpeg / ffprobe 바이너리 (gitignore)
├── requirements.txt
├── requirements-dev.txt
├── LICENSE                         # MIT (래퍼 코드)
└── NOTICE.md                       # 제3자 컴포넌트 라이선스
```

---

## 라이선스 / 크레딧

- 본 저장소의 **래퍼 코드**: MIT License — see [`LICENSE`](LICENSE)
- 다운로드 엔진: [yt-dlp](https://github.com/yt-dlp/yt-dlp)
  (Unlicense / public domain)
- 미디어 처리: [FFmpeg](https://ffmpeg.org/) (LGPL / GPL)

자세한 제3자 컴포넌트 표기는 [`NOTICE.md`](NOTICE.md)를 참고하세요.

---

## 기여

버그 리포트나 PR은 환영합니다. 다만 **다운로드 로직 자체의 버그**는 대부분
upstream인 [yt-dlp 이슈 트래커](https://github.com/yt-dlp/yt-dlp/issues)에서
다루는 것이 적절합니다 (YouTube 측 변경에 따른 호환성 등).

본 저장소는 GUI / 패키징 / 사용성 관련 이슈에 집중합니다.
