"""이미지 목록의 첫 이미지 미리보기."""
import tkinter as tk
from PIL import Image, ImageTk
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

    def show_first(self, image, name, count):
        preview = image.copy()
        preview.thumbnail((C.THUMB_W, C.THUMB_H), Image.Resampling.LANCZOS)
        self._photo = ImageTk.PhotoImage(preview, master=self.canvas)
        self.canvas.delete("all")
        self.canvas.create_image(12 + C.THUMB_W / 2, 6 + C.THUMB_H / 2,
                                 image=self._photo)
        self.canvas.create_text(12, C.THUMB_H + 12, anchor="w", text=name,
                                 font=FONTS["small"], fill=C.COLOR_TEXT)
        self.canvas.create_text(C.THUMB_W + 30, 40, anchor="w",
                                 text=f"총 {count}장 · 첫 이미지 표시",
                                 font=FONTS["small"], fill=C.COLOR_MUTED)
