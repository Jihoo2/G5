"""이미지 목록의 빈 화면 배치."""
import tkinter as tk
from tkinter import ttk
from configs import settings as C
from src.ui.theme import FONTS


class ThumbnailStrip(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master, bg=C.COLOR_PANEL)
        self.prev_btn = ttk.Button(self, text="‹", width=2, style="Small.TButton",
                                   state="disabled")
        self.prev_btn.pack(side="left", fill="y")
        self.next_btn = ttk.Button(self, text="›", width=2, style="Small.TButton",
                                   state="disabled")
        self.next_btn.pack(side="right", fill="y")
        self.canvas = tk.Canvas(self, height=C.THUMB_H + 30, bg=C.COLOR_PANEL,
                                highlightthickness=0)
        self.canvas.pack(side="left", fill="x", expand=True, padx=4)
        self.canvas.create_text(12, (C.THUMB_H + 30) / 2, anchor="w",
                                text="이미지가 없습니다", fill=C.COLOR_MUTED,
                                font=FONTS["small"])
