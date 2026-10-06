"""JPG 이미지를 화면 비율에 맞춰 표시하는 캔버스."""
import tkinter as tk
from PIL import Image, ImageTk
from configs import settings as C
from src.ui.theme import FONTS


class ImageCanvas(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master, bg=C.COLOR_CANVAS)
        self.image = None
        self._tk_img = None
        self._resize_job = None
        self.canvas = tk.Canvas(self, bg=C.COLOR_CANVAS, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<Configure>", self._on_resize)
        self.zoom_lbl = tk.Label(self, text="-", bg="#111827", fg="white",
                                 font=FONTS["bold"], padx=8, pady=3)
        self.zoom_lbl.place(relx=1.0, rely=1.0, x=-12, y=-12, anchor="se")

    def set_image(self, image):
        self.image = image
        self._render()

    def _on_resize(self, event):
        if self._resize_job is not None:
            self.after_cancel(self._resize_job)
        self._resize_job = self.after(60, self._render)

    def _render(self):
        if self._resize_job is not None:
            self.after_cancel(self._resize_job)
            self._resize_job = None
        width, height = self.canvas.winfo_width(), self.canvas.winfo_height()
        if width <= 1 or height <= 1:
            return
        self.canvas.delete("all")
        if self.image is None:
            self.canvas.create_text(width / 2, height / 2,
                text="폴더 열기(Ctrl+O)로 이미지 폴더를 선택하세요",
                fill="#9CA3AF", font=FONTS["bold"])
            return
        self.scale = min(width / self.image.width, height / self.image.height)
        size = (max(1, int(self.image.width * self.scale)),
                max(1, int(self.image.height * self.scale)))
        resized = self.image.resize(size, Image.Resampling.LANCZOS)
        self._tk_img = ImageTk.PhotoImage(resized, master=self.canvas)
        self.ox, self.oy = (width - size[0]) / 2, (height - size[1]) / 2
        self.canvas.create_image(self.ox, self.oy, image=self._tk_img, anchor="nw")
        self.zoom_lbl.configure(text=f"{self.scale * 100:.1f}%")
