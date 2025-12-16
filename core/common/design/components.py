import ttkbootstrap as tb
from ttkbootstrap.constants import *

from Design import Colors
from Padding import Padding
from Typography import Typography


class Components:
    @staticmethod
    def apply(style: tb.Style):
        # Notebook
        style.configure(
            "TNotebook",
            background=Colors.Bg_main,
            borderwidth=0
        )

        style.configure(
            "TNotebook.Tab",
            background="#2E2E2E",
            padding=Padding.Tab_padding,
            font=Typography.Font_tab,
            foreground=Colors.Subtext
        )

        style.map(
            "TNotebook.Tab",
            background=[("selected", Colors.Accent)],
            foreground=[("selected", "white")]
        )

        # Frame
        style.configure(
            "TFrame",
            background=Colors.Bg_card
        )

        # Label
        style.configure(
            "TLabel",
            background=Colors.Bg_card,
            font=Typography.Font_base,
            foreground=Colors.Text
        )

        # Button
        style.configure(
            "TButton",
            font=Typography.Font_bold,
            padding=Padding.Button_padding,
            borderwidth=0
        )

        style.map(
            "TButton",
            background=[("active", Colors.Accent_hover)],
            foreground=[("active", "white")]
        )

        # Accent Button
        style.configure(
            "Accent.TButton",
            background=Colors.Accent,
            foreground="white",
            relief="flat"
        )

        style.map(
            "Accent.TButton",
            background=[
                ("active", Colors.Accent_hover),
                ("pressed", Colors.Accent_pressed)
            ]
        )

        # Checkbutton
        style.configure(
            "Checklist.TCheckbutton",
            background=Colors.Bg_card,
            foreground=Colors.Text,
            font=Typography.Font_base,
            relief="flat"
        )
