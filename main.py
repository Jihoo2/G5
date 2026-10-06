"""실행: python main.py"""
import tkinter as tk

from src.ui.main_window import LabelingApp
from src.ui.theme import setup_theme


def main():
    root = tk.Tk()
    setup_theme(root)
    root.app = LabelingApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
