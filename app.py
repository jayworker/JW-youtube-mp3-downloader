"""Tkinter GUI for the YouTube -> MP3 downloader (modern dark theme)."""
from __future__ import annotations

import queue
import threading
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, font as tkfont, messagebox, ttk

from downloader import download


DEFAULT_OUTPUT = str(Path.home() / "Downloads" / "YouTubeMP3")

# Palette
BG          = "#16161f"
SURFACE     = "#1f1f2e"
SURFACE_2   = "#262638"
BORDER      = "#2f2f44"
TEXT        = "#e6e6ee"
TEXT_MUTED  = "#8a8aa3"
ACCENT      = "#f43f5e"
ACCENT_HOV  = "#fb5470"
ACCENT_DOWN = "#d63a55"
SUCCESS     = "#34d399"
ERROR       = "#fb7185"
INFO        = "#7dd3fc"


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("YouTube MP3 Downloader")
        self.geometry("680x560")
        self.minsize(600, 480)
        self.configure(bg=BG)

        self._msg_q: queue.Queue[tuple[str, str]] = queue.Queue()
        self._worker: threading.Thread | None = None

        self._setup_fonts()
        self._setup_styles()
        self._build_ui()
        self.after(100, self._poll_queue)

    # ----- styling ---------------------------------------------------------
    def _setup_fonts(self) -> None:
        family = "Segoe UI"
        self.f_title  = tkfont.Font(family=family, size=18, weight="bold")
        self.f_sub    = tkfont.Font(family=family, size=10)
        self.f_label  = tkfont.Font(family=family, size=10, weight="bold")
        self.f_body   = tkfont.Font(family=family, size=10)
        self.f_button = tkfont.Font(family=family, size=11, weight="bold")
        self.f_log    = tkfont.Font(family="Consolas", size=9)

    def _setup_styles(self) -> None:
        s = ttk.Style(self)
        s.theme_use("clam")

        s.configure("TFrame", background=BG)
        s.configure("Card.TFrame", background=SURFACE)

        s.configure("Title.TLabel",   background=BG, foreground=TEXT,       font=self.f_title)
        s.configure("Sub.TLabel",     background=BG, foreground=TEXT_MUTED, font=self.f_sub)
        s.configure("Section.TLabel", background=BG, foreground=TEXT_MUTED, font=self.f_label)

        s.configure(
            "Modern.TEntry",
            fieldbackground=SURFACE,
            background=SURFACE,
            foreground=TEXT,
            bordercolor=BORDER,
            lightcolor=BORDER,
            darkcolor=BORDER,
            insertcolor=TEXT,
            padding=8,
        )
        s.map(
            "Modern.TEntry",
            bordercolor=[("focus", ACCENT)],
            lightcolor=[("focus", ACCENT)],
            darkcolor=[("focus", ACCENT)],
        )

        s.configure(
            "Accent.TButton",
            background=ACCENT,
            foreground="#ffffff",
            font=self.f_button,
            padding=(18, 10),
            borderwidth=0,
            focusthickness=0,
        )
        s.map(
            "Accent.TButton",
            background=[("pressed", ACCENT_DOWN), ("active", ACCENT_HOV), ("disabled", BORDER)],
            foreground=[("disabled", TEXT_MUTED)],
        )

        s.configure(
            "Ghost.TButton",
            background=SURFACE_2,
            foreground=TEXT,
            font=self.f_body,
            padding=(12, 8),
            borderwidth=0,
            focusthickness=0,
        )
        s.map("Ghost.TButton", background=[("active", BORDER)])

        s.configure(
            "Accent.Horizontal.TProgressbar",
            background=ACCENT,
            troughcolor=SURFACE_2,
            bordercolor=SURFACE_2,
            lightcolor=ACCENT,
            darkcolor=ACCENT,
        )

    # ----- layout ----------------------------------------------------------
    def _build_ui(self) -> None:
        root = ttk.Frame(self, style="TFrame")
        root.pack(fill="both", expand=True, padx=24, pady=20)

        # Header
        header = ttk.Frame(root, style="TFrame")
        header.pack(fill="x", pady=(0, 18))
        ttk.Label(header, text="YouTube MP3 Downloader", style="Title.TLabel").pack(anchor="w")
        ttk.Label(
            header,
            text="링크를 붙여넣고 버튼을 누르세요. 자동으로 MP3로 변환됩니다.",
            style="Sub.TLabel",
        ).pack(anchor="w", pady=(2, 0))

        # URL
        ttk.Label(root, text="YOUTUBE URL", style="Section.TLabel").pack(anchor="w")
        self.url_var = tk.StringVar()
        url_entry = ttk.Entry(root, textvariable=self.url_var, style="Modern.TEntry", font=self.f_body)
        url_entry.pack(fill="x", pady=(4, 14), ipady=2)
        url_entry.focus_set()

        # Output dir
        ttk.Label(root, text="저장 위치", style="Section.TLabel").pack(anchor="w")
        row = ttk.Frame(root, style="TFrame")
        row.pack(fill="x", pady=(4, 16))
        self.dir_var = tk.StringVar(value=DEFAULT_OUTPUT)
        ttk.Entry(row, textvariable=self.dir_var, style="Modern.TEntry", font=self.f_body).pack(
            side="left", fill="x", expand=True, ipady=2
        )
        ttk.Button(row, text="폴더 선택", command=self._choose_dir, style="Ghost.TButton").pack(
            side="left", padx=(8, 0)
        )

        # Action row
        action = ttk.Frame(root, style="TFrame")
        action.pack(fill="x", pady=(2, 18))
        self.btn = ttk.Button(action, text="MP3 다운로드", command=self._start, style="Accent.TButton")
        self.btn.pack(side="left")
        self.progress = ttk.Progressbar(
            action, mode="indeterminate", style="Accent.Horizontal.TProgressbar", length=200
        )
        self.progress.pack(side="left", fill="x", expand=True, padx=(14, 0), ipady=2)

        # Log card
        ttk.Label(root, text="활동 로그", style="Section.TLabel").pack(anchor="w")
        log_wrap = tk.Frame(root, bg=BORDER, highlightthickness=0, bd=0)
        log_wrap.pack(fill="both", expand=True, pady=(4, 0))
        inner = tk.Frame(log_wrap, bg=SURFACE, bd=0)
        inner.pack(fill="both", expand=True, padx=1, pady=1)

        self.log = tk.Text(
            inner,
            wrap="word",
            bg=SURFACE,
            fg=TEXT,
            insertbackground=TEXT,
            relief="flat",
            bd=0,
            padx=12,
            pady=10,
            font=self.f_log,
            state="disabled",
        )
        self.log.pack(fill="both", expand=True)

        self.log.tag_configure("info",    foreground=INFO)
        self.log.tag_configure("ok",      foreground=SUCCESS)
        self.log.tag_configure("err",     foreground=ERROR)
        self.log.tag_configure("muted",   foreground=TEXT_MUTED)

        self._log("대기 중…  YouTube 링크를 입력해 시작하세요.", tag="muted")

        # Attribution footer
        footer = ttk.Frame(root, style="TFrame")
        footer.pack(fill="x", pady=(10, 0))
        ttk.Label(
            footer,
            text="Powered by yt-dlp · FFmpeg  ·  개인 사용 목적으로만 사용하세요.",
            style="Sub.TLabel",
        ).pack(anchor="w")

    # ----- behavior --------------------------------------------------------
    def _choose_dir(self) -> None:
        d = filedialog.askdirectory(initialdir=self.dir_var.get() or str(Path.home()))
        if d:
            self.dir_var.set(d)

    def _log(self, line: str, tag: str | None = None) -> None:
        self.log.configure(state="normal")
        if tag:
            self.log.insert("end", line.rstrip() + "\n", tag)
        else:
            self.log.insert("end", line.rstrip() + "\n")
        self.log.see("end")
        self.log.configure(state="disabled")

    def _start(self) -> None:
        url = self.url_var.get().strip()
        out = self.dir_var.get().strip() or DEFAULT_OUTPUT
        if not url:
            messagebox.showwarning("URL 필요", "YouTube 링크를 입력해 주세요.")
            return
        if self._worker and self._worker.is_alive():
            return

        self.btn.configure(state="disabled")
        self.progress.start(12)
        self._log(f"▶  시작: {url}", tag="info")
        self._worker = threading.Thread(target=self._run, args=(url, out), daemon=True)
        self._worker.start()

    def _run(self, url: str, out: str) -> None:
        def hook(d: dict) -> None:
            status = d.get("status")
            if status == "downloading":
                pct = d.get("_percent_str", "").strip()
                speed = d.get("_speed_str", "").strip()
                if pct:
                    self._msg_q.put(("muted", f"   다운로드 중…  {pct}  ({speed})"))
            elif status == "finished":
                self._msg_q.put(("info", "   다운로드 완료 → MP3 변환 중…"))

        try:
            result = download(url, output_dir=out, progress_hook=hook)
            self._msg_q.put(("ok", f"✓  저장 완료: {result.filepath}"))
            self._msg_q.put(("done", "ok"))
        except Exception as e:
            self._msg_q.put(("err", f"✗  실패: {e}"))
            self._msg_q.put(("done", "err"))

    def _poll_queue(self) -> None:
        try:
            while True:
                kind, payload = self._msg_q.get_nowait()
                if kind == "done":
                    self.progress.stop()
                    self.btn.configure(state="normal")
                else:
                    self._log(payload, tag=kind)
        except queue.Empty:
            pass
        self.after(100, self._poll_queue)


if __name__ == "__main__":
    App().mainloop()
