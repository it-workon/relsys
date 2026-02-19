import ttkbootstrap as tb
from ttkbootstrap.constants import *

from . import Design

class Components:
    @staticmethod
    def apply(style: tb.Style):
        # Notebook
        style.configure("TNotebook", background=Design.Colors.Bg_main, borderwidth=0)

        style.configure(
            "TNotebook.Tab",
            background="#2E2E2E",
            padding=Design.Padding.Tab_padding,
            font=Design.Typography.Font_tab,
            foreground=Design.Colors.Subtext,
        )

        style.map(
            "TNotebook.Tab",
            background=[("selected", Design.Colors.Accent)],
            foreground=[("selected", "white")],
        )

        # Frame
        style.configure("TFrame", background=Design.Colors.Bg_card)

        # Label
        style.configure(
            "TLabel",
            background=Design.Colors.Bg_card,
            font=Design.Typography.Font_base,
            foreground=Design.Colors.Text,
        )

        # Button
        style.configure(
            "TButton",
            font=Design.Typography.Font_bold,
            padding=Design.Padding.Button_padding,
            borderwidth=0,
        )

        style.map(
            "TButton",
            background=[("active", Design.Colors.Accent_hover)],
            foreground=[("active", "white")],
        )

        # Accent Button
        style.configure(
            "Accent.TButton",
            background=Design.Colors.Accent,
            foreground="white",
            relief="flat",
        )

        style.map(
            "Accent.TButton",
            background=[
                ("active", Design.Colors.Accent_hover),
                ("pressed", Design.Colors.Accent_pressed),
            ],
        )

        # Checkbutton
        style.configure(
            "Checklist.TCheckbutton",
            background=Design.Colors.Bg_card,
            foreground=Design.Colors.Text,
            font=Design.Typography.Font_base,
            relief="flat",
        )

    @staticmethod
    def title(parent, text):
        return tb.Label(
            parent,
            text=text,
            font=Design.Typography.Font_title,
            foreground=Design.Colors.Text,
        )

    @staticmethod
    def label(parent, text):
        return tb.Label(parent, text=text, style="TLabel")

    @staticmethod
    def entry(parent, width=40):
        return tb.Entry(parent, width=width)

    @staticmethod
    def labeled_entry(parent, label_text, width=40):
        label = Components.label(parent, label_text)
        label.pack(anchor="w", pady=(10, 2))

        entry = Components.entry(parent, width)
        entry.pack(ipady=5)

        return entry

    @staticmethod
    def accent_button(parent, text, command):
        return tb.Button(
            parent,
            text=text,
            command=command,
            style="Accent.TButton",
        )

    @staticmethod
    def footer(parent, text, color):
        return tb.Label(
            parent,
            text=text,
            font=Design.Typography.Font_small_italic,
            foreground=color,
        )
