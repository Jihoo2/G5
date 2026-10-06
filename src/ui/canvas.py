import tkinter as tk
from configs import settings as C
from src.ui.theme import FONTS


class ImageCanvas(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master, bg=C.COLOR_CANVAS)
        self.canvas = tk.Canvas(self, bg=C.COLOR_CANVAS, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.hint = self.canvas.create_text(
            0, 0, text="폴더 열기(Ctrl+O)로 이미지 폴더를 선택하세요",
            fill="#9CA3AF", font=FONTS["bold"],
        )
        self.canvas.bind("<Configure>", self._position_hint)
        self.zoom_lbl = tk.Label(self, text="-", bg="#111827", fg="white",
                                 font=FONTS["bold"], padx=8, pady=3)
        self.zoom_lbl.place(relx=1.0, rely=1.0, x=-12, y=-12, anchor="se")

    def _position_hint(self, event):
        self.canvas.coords(self.hint, event.width / 2, event.height / 2)
