"""공용 위젯: 토글 스위치, 툴팁, 카드 패널, 스크롤 프레임."""
import tkinter as tk
from tkinter import ttk

from configs import settings as C
from src.ui.theme import FONTS


class ToggleSwitch(tk.Canvas):
    """BooleanVar와 연결되는 ON/OFF 스위치"""

    def __init__(self, master, variable: tk.BooleanVar, command=None,
                 width=44, height=22, bg=C.COLOR_PANEL):
        super().__init__(master, width=width, height=height, bg=bg,
                         highlightthickness=0, cursor="hand2")
        self.var = variable
        self.command = command
        self._sw_width, self._sw_height = width, height
        self.var.trace_add("write", lambda *_: self._draw())
        self._draw()

    def _draw(self):
        self.delete("all")
        w, h = self._sw_width, self._sw_height
        on = bool(self.var.get())
        color = C.COLOR_ACCENT if on else "#C5CBD3"
        self.create_oval(0, 0, h, h, fill=color, outline=color)
        self.create_oval(w - h, 0, w, h, fill=color, outline=color)
        self.create_rectangle(h / 2, 0, w - h / 2, h, fill=color, outline=color)
        x = w - h + 3 if on else 3
        self.create_oval(x, 3, x + h - 6, h - 3, fill="white", outline="white")



class Tooltip:
    def __init__(self, widget, text: str, delay: int = 450):
        self.widget, self.text, self.delay = widget, text, delay
        self._after = None
        self.tip = None
        widget.bind("<Enter>", self._schedule, add="+")
        widget.bind("<Leave>", self._hide, add="+")
        widget.bind("<ButtonPress>", self._hide, add="+")

    def _schedule(self, _e=None):
        self._cancel()
        self._after = self.widget.after(self.delay, self._show)

    def _cancel(self):
        if self._after:
            self.widget.after_cancel(self._after)
            self._after = None

    def _show(self):
        if self.tip or not self.text:
            return
        x = self.widget.winfo_rootx() + 10
        y = self.widget.winfo_rooty() + self.widget.winfo_height() + 6
        self.tip = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        tk.Label(tw, text=self.text, justify="left", bg="#1F2937", fg="white",
                 font=FONTS["small"], padx=8, pady=5).pack()

    def _hide(self, _e=None):
        self._cancel()
        if self.tip:
            self.tip.destroy()
            self.tip = None


def make_card(parent, title: str) -> tk.Frame:
    """파란 세로 바 + 제목이 있는 흰색 패널. .head / .title_lbl / .body 속성 제공"""
    outer = tk.Frame(parent, bg=C.COLOR_PANEL,
                     highlightbackground=C.COLOR_BORDER, highlightthickness=1)
    head = tk.Frame(outer, bg=C.COLOR_PANEL)
    head.pack(fill="x", padx=8, pady=(6, 4))
    tk.Frame(head, bg=C.COLOR_ACCENT, width=4, height=16).pack(side="left", padx=(0, 6))
    title_lbl = tk.Label(head, text=title, bg=C.COLOR_PANEL, fg=C.COLOR_ACCENT,
                         font=FONTS["title"])
    title_lbl.pack(side="left")
    body = tk.Frame(outer, bg=C.COLOR_PANEL)
    body.pack(fill="both", expand=True, padx=8, pady=(0, 8))
    outer.head, outer.title_lbl, outer.body = head, title_lbl, body
    return outer


class ScrollableFrame(tk.Frame):
    """세로로 내용이 넘칠 때만 스크롤바가 나타나는 프레임. 자식은 .inner 에 배치"""

    def __init__(self, master, bg=C.COLOR_BG):
        super().__init__(master, bg=bg)
        self.canvas = tk.Canvas(self, bg=bg, highlightthickness=0, bd=0)
        self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.inner = tk.Frame(self.canvas, bg=bg)
        self.canvas.create_window(0, 0, window=self.inner, anchor="nw")
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.inner.bind("<Configure>", self._update)
        self.canvas.bind("<Configure>", self._update)

    def _update(self, _e=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"),
                              width=self.inner.winfo_reqwidth())
        need = self.inner.winfo_reqheight() > self.canvas.winfo_height() > 1
        if need and not self.vsb.winfo_ismapped():
            self.vsb.pack(side="right", fill="y", before=self.canvas)
        elif not need and self.vsb.winfo_ismapped():
            self.vsb.pack_forget()
            self.canvas.yview_moveto(0)
