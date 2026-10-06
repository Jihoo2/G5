"""폰트·ttk 스타일 설정. setup_theme() 호출 후 FONTS 사용."""
import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk

from configs import settings as C

FONTS: dict = {}


def _pick(root, candidates):
    families = set(tkfont.families(root))
    for fam in candidates:
        if fam in families:
            return fam
    return candidates[-1]


def setup_theme(root: tk.Tk) -> dict:
    fam = _pick(root, C.FONT_CANDIDATES)
    mono = _pick(root, C.MONO_CANDIDATES)
    for name in ("TkDefaultFont", "TkTextFont", "TkMenuFont", "TkHeadingFont", "TkTooltipFont"):
        try:
            tkfont.nametofont(name).configure(family=fam, size=10)
        except tk.TclError:
            pass

    FONTS.update(
        base=(fam, 10), bold=(fam, 10, "bold"), title=(fam, 11, "bold"),
        big=(fam, 16, "bold"), small=(fam, 9), tag=(fam, 9, "bold"), mono=(mono, 9),
    )
    root.configure(bg=C.COLOR_BG)

    s = ttk.Style(root)
    try:
        s.theme_use("clam")
    except tk.TclError:
        pass
    s.configure(".", font=FONTS["base"], background=C.COLOR_PANEL, foreground=C.COLOR_TEXT)
    s.configure("TFrame", background=C.COLOR_PANEL)

    s.configure("Tool.TButton", padding=(10, 5), background="#F7F9FC", bordercolor=C.COLOR_BORDER)
    s.map("Tool.TButton", background=[("active", "#E6EEFB")])
    s.configure("ToolActive.TButton", padding=(10, 5), background=C.COLOR_ACCENT,
                foreground="white", bordercolor=C.COLOR_ACCENT)
    s.map("ToolActive.TButton", background=[("active", C.COLOR_ACCENT_DARK)],
          foreground=[("active", "white")])

    s.configure("Accent.TButton", padding=(14, 7), background=C.COLOR_ACCENT,
                foreground="white", font=FONTS["bold"])
    s.map("Accent.TButton", background=[("active", C.COLOR_ACCENT_DARK)])

    s.configure("Small.TButton", padding=(8, 3), font=FONTS["small"], background="#F7F9FC")
    s.configure("SmallActive.TButton", padding=(8, 3), font=FONTS["small"],
                background=C.COLOR_ACCENT, foreground="white")
    s.map("SmallActive.TButton", background=[("active", C.COLOR_ACCENT_DARK)],
          foreground=[("active", "white")])

    s.configure("Treeview", rowheight=22, font=FONTS["small"],
                background="white", fieldbackground="white")
    s.configure("Treeview.Heading", font=FONTS["small"], background="#F3F5F9")
    s.map("Treeview", background=[("selected", C.COLOR_ACCENT)],
          foreground=[("selected", "white")])

    s.configure("TRadiobutton", background=C.COLOR_PANEL, font=FONTS["base"])
    s.configure("TEntry", padding=3)
    s.configure("TCombobox", padding=3)
    s.configure("Done.Horizontal.TProgressbar", troughcolor="#E5E7EB",
                background=C.COLOR_SUCCESS, bordercolor="#E5E7EB",
                lightcolor=C.COLOR_SUCCESS, darkcolor=C.COLOR_SUCCESS)
    return FONTS
