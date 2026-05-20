# JW-YouTube MP3 Downloader

[![Latest Release](https://img.shields.io/github/v/release/jayworker/JW-youtube-mp3-downloader?label=download&style=for-the-badge&color=f43f5e)](https://github.com/jayworker/JW-youtube-mp3-downloader/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/jayworker/JW-youtube-mp3-downloader/total?style=for-the-badge&color=8b5cf6)](https://github.com/jayworker/JW-youtube-mp3-downloader/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge)](LICENSE)

**링크를 붙여넣고 버튼만 누르면 MP3로 저장되는 데스크탑 앱.**
설치도 필요 없고, 따로 깔 것도 없습니다. zip 받아서 풀고 실행하면 끝.

> 📢 **이름은 "YouTube MP3 Downloader"지만, YouTube뿐 아니라 Instagram · TikTok 등 yt-dlp가 지원하는 사이트의 음원도 동일하게 MP3로 다운로드할 수 있어요.**

---

## 📦 최신 정식 빌드

> 모든 빌드는 [GitHub Actions](https://github.com/jayworker/JW-youtube-mp3-downloader/actions/workflows/release.yml)에서
> 본 저장소의 소스코드를 그대로 컴파일한 결과물입니다. 누구나 소스부터 빌드 로그까지 확인할 수 있어요.

<div align="center">

<table>
<tr>
<td width="50%" align="center" valign="top">

#### 🪟 &nbsp; Windows (64-bit)

<a href="https://github.com/jayworker/JW-youtube-mp3-downloader/releases/latest/download/JW-YouTubeMP3Downloader-windows.zip">
<img src="https://img.shields.io/badge/Download_for_Windows-0078D4?style=for-the-badge&logo=windows&logoColor=white&labelColor=0078D4" alt="Download for Windows" height="44">
</a>

![Version](https://img.shields.io/github/v/release/jayworker/JW-youtube-mp3-downloader?label=version&color=0078D4)
![Size](https://img.shields.io/badge/size-~96_MB-lightgrey)

압축을 풀고 **`JW-YouTubeMP3Downloader.exe`** 더블클릭

</td>
<td width="50%" align="center" valign="top">

#### 🍎 &nbsp; macOS (Apple Silicon)

<a href="https://github.com/jayworker/JW-youtube-mp3-downloader/releases/latest/download/JW-YouTubeMP3Downloader-macos.zip">
<img src="https://img.shields.io/badge/Download_for_macOS-000000?style=for-the-badge&logo=apple&logoColor=white&labelColor=000000" alt="Download for macOS" height="44">
</a>

![Version](https://img.shields.io/github/v/release/jayworker/JW-youtube-mp3-downloader?label=version&color=555555)
![Size](https://img.shields.io/badge/size-~74_MB-lightgrey)

압축을 풀고 **`JW-YouTubeMP3Downloader.app`** 실행

</td>
</tr>
</table>

[**전체 릴리스 목록 →**](https://github.com/jayworker/JW-youtube-mp3-downloader/releases) &nbsp;·&nbsp;
[**소스 코드 →**](https://github.com/jayworker/JW-youtube-mp3-downloader) &nbsp;·&nbsp;
[**빌드 워크플로 →**](https://github.com/jayworker/JW-youtube-mp3-downloader/blob/main/.github/workflows/release.yml)

</div>

### 사용법 (둘 다 동일)

1. 앱 실행
2. 링크 붙여넣기 (YouTube · Instagram · TikTok 등)
3. **MP3 다운로드** 버튼 → 끝.

---

## 💬 문의 / 버그 신고

문제가 생기거나 궁금한 게 있으면 아래에서 알려주세요. 양식만 채우시면 됩니다 (GitHub 계정 필요 · 무료).

| 종류 | 어디로 | 용도 |
|---|---|---|
| 🐛 **버그 신고** | [Issues — Bug report](https://github.com/jayworker/JW-youtube-mp3-downloader/issues/new?template=bug_report.yml) | 앱이 안 되거나 이상하게 동작할 때 |
| 💡 **기능 제안** | [Issues — Feature request](https://github.com/jayworker/JW-youtube-mp3-downloader/issues/new?template=feature_request.yml) | "이런 기능 있으면 좋겠다" |
| 💬 **사용법·일반 질문** | [Discussions](https://github.com/jayworker/JW-youtube-mp3-downloader/discussions) | "어떻게 쓰는지 모르겠어요", 잡담 |

📋 같은 문제를 다른 분이 이미 올렸을 수도 있어요 →
[기존 이슈 검색](https://github.com/jayworker/JW-youtube-mp3-downloader/issues?q=is%3Aissue) ·
[기존 Discussions 검색](https://github.com/jayworker/JW-youtube-mp3-downloader/discussions)

> **여기까지가 일반 사용자가 알아야 할 전부입니다.** 아래는 개발자/고급 사용자용입니다.

---

<details>
<summary>⚠️ 처음 실행 시 보안 경고가 뜬다면 (펼쳐보기)</summary>

코드 서명이 없는 빌드라 OS가 처음 보는 프로그램이라 경고를 띄웁니다. 한 번만 통과시키면 다음부터는 그냥 열려요.

**Windows** — "Windows의 PC 보호" 창이 뜨면 → **추가 정보** → **실행**.

**macOS** — "확인되지 않은 개발자" 경고가 뜨면 → 앱 아이콘을 **마우스 우클릭(또는 Ctrl+클릭) → 열기 → 열기**. 두 번째부턴 더블클릭으로 그냥 열립니다.

> macOS 빌드는 Apple Silicon(M1/M2/M3/M4) 전용입니다. Intel Mac은 아래 "소스에서 직접 실행"을 참고하세요.

</details>

<details>
<summary>⚠️ 사용 전 꼭 읽어주세요 (저작권/약관 안내)</summary>

- 이 도구는 **개인 사용 / 학습 / 본인이 권리를 보유한 콘텐츠 백업** 용도로만 제공됩니다.
- YouTube 이용약관은 원칙적으로 콘텐츠 다운로드를 금지합니다 (YouTube Premium 오프라인 저장 기능 제외).
- 저작권이 있는 음원의 무단 다운로드/재배포는 거주국 저작권법에 위반될 수 있습니다.
- 본 도구를 사용해 발생하는 법적·계약상 책임은 **전적으로 사용자에게 있습니다.**

</details>

---

## 크레딧

이 앱은 [**yt-dlp**](https://github.com/yt-dlp/yt-dlp)의 얇은 GUI 래퍼입니다.
실제 다운로드 로직과 사이트 호환성은 yt-dlp 프로젝트의 작품이며, 모든 공로는
yt-dlp 메인테이너와 컨트리뷰터에게 있습니다. 음원 변환은 [**FFmpeg**](https://ffmpeg.org/)을 사용합니다.

자세한 제3자 컴포넌트 표기는 [`NOTICE.md`](NOTICE.md), 본 저장소의 래퍼 코드는 [MIT 라이선스](LICENSE)입니다.

---

<details>
<summary>🛠 개발자용 — 소스에서 직접 실행 / 빌드 (펼쳐보기)</summary>

### 사전 준비
- Python 3.10 이상

### 소스에서 실행

```powershell
git clone https://github.com/jayworker/JW-youtube-mp3-downloader.git
cd JW-youtube-mp3-downloader

python -m venv .venv
.\.venv\Scripts\Activate.ps1     # Windows
# source .venv/bin/activate      # macOS / Linux
pip install -r requirements.txt

# FFmpeg 자동 다운로드
.\scripts\fetch_ffmpeg.ps1       # Windows
# bash scripts/fetch_ffmpeg.sh   # macOS

python app.py
```

시스템에 FFmpeg가 PATH로 잡혀 있다면 fetch 단계는 생략 가능합니다.

### 단일 실행 파일 빌드

```powershell
pip install -r requirements-dev.txt
.\build.ps1                      # Windows → dist\JW-YouTubeMP3Downloader\
# python -m PyInstaller --noconfirm JW-YouTubeMP3Downloader.spec   # macOS → dist/JW-YouTubeMP3Downloader.app
```

### 클라우드 빌드 (권장)

`git tag v1.x.x && git push --tags` → [GitHub Actions](.github/workflows/release.yml)가
Windows + macOS 빌드를 만들고 새 Release에 자동 첨부합니다.

### 프로젝트 구조

```
.
├── app.py                          # Tkinter GUI
├── downloader.py                   # yt-dlp 래퍼
├── JW-YouTubeMP3Downloader.spec    # PyInstaller 빌드 스펙 (Win/Mac 공용)
├── build.ps1                       # Windows 원샷 빌드
├── scripts/
│   ├── fetch_ffmpeg.ps1            # Windows용 FFmpeg 다운로드
│   └── fetch_ffmpeg.sh             # macOS용 FFmpeg 다운로드
├── .github/workflows/
│   └── release.yml                 # CI: Win + Mac 빌드 + Release 업로드
├── vendor/                         # FFmpeg 바이너리 (gitignore)
├── requirements.txt
├── requirements-dev.txt
├── LICENSE                         # MIT (래퍼 코드)
└── NOTICE.md                       # 제3자 컴포넌트 라이선스
```

### 기여

다운로드 **엔진**의 버그(YouTube 호환성 등)는 [yt-dlp 이슈 트래커](https://github.com/yt-dlp/yt-dlp/issues)에 올려주세요.
본 저장소는 GUI / 패키징 / 사용성 관련 이슈에 집중합니다.

</details>
