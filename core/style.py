import ttkbootstrap as tb
from ttkbootstrap.constants import *


def apply_styles(window):
    style = tb.Style()

    # color palette
    accent_color = "#5B7FFF"
    bg_main = "#1E1E1E"
    bg_card = "#2A2A2A"
    text_color = "#E0E0E0"
    subtext_color = "#B0B0B0"

    # notebook
    style.configure("TNotebook", background=bg_main, borderwidth=0)
    style.configure(
        "TNotebook.Tab",
        background="#2E2E2E",
        padding=[18, 10],
        font=("Arial", 10, "bold"),
        foreground=subtext_color,
    )
    style.map(
        "TNotebook.Tab",
        background=[("selected", accent_color)],
        foreground=[("selected", "white")],
    )

    # frames
    style.configure("TFrame", background=bg_card)

    # labels
    style.configure(
        "TLabel",
        background=bg_card,
        font=("Times New Roman", 10),
        foreground=text_color,
    )

    # buttons
    style.configure(
        "TButton", font=("Times New Roman", 10, "bold"), padding=10, borderwidth=0
    )
    style.map(
        "TButton", background=[("active", "#4866E1")], foreground=[("active", "white")]
    )

    # accent button
    style.configure(
        "Accent.TButton", background=accent_color, foreground="white", relief="flat"
    )
    style.map(
        "Accent.TButton", background=[("active", "#4866E1"), ("pressed", "#384FC1")]
    )

    # checkboxes
    style.configure(
        "Checklist.TCheckbutton",
        background=bg_card,
        foreground=text_color,
        font=("Times New Roman", 10),
        relief="flat",
    )

    # return colors to be reutilized
    return {
        "accent_color": accent_color,
        "bg_main": bg_main,
        "bg_card": bg_card,
        "text_color": text_color,
        "subtext_color": subtext_color,
    }
