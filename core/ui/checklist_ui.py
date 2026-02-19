import tkinter as tk
from tkinter import ttk

from design import Design


def tab_checklist(app, container):
    frame = ttk.Frame(container, padding=Design.Padding.Xs)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    checklist_vars: list[tk.BooleanVar] = []

    software_items = [
        "Criar o Suporte / Dar ADM ao suporte",
        "Logar no suporte",
        "Colocar WIFI",
        "Colocar no domínio e o nome",
        "Entrar na minha conta",
        "Baixar Chrome",
        "Baixar AnyDesk",
        "Baixar FortClient",
        "Baixar WINRAR",
        "Baixar Office",
        "Baixar Gi",
        "Baixar Java",
        "Baixar Adobe",
        "Baixar o BitDefender",
        "Baixar o PaperCut",
    ]

    config_items = [
        "Ativar Suporte",
        "Email / Assinatura",
        "Teams",
        "GI",
        "Fortclient",
        "PaperCut",
        "Impressora",
        "Conferir Dowloads",
        "Imprimir Bem Vindo",
        "Planilhar Máquina",
    ]

    # Título
    ttk.Label(
        frame,
        text="Checklist de Preparação",
        font=Design.Typography.Font_title,
        foreground=Design.Colors.Text,
    ).pack(pady=(0, Design.Padding.Md))

    columns_container = ttk.Frame(frame)
    columns_container.pack(pady=Design.Padding.Sm)

    def build_column(parent, title, items):
        column = ttk.Frame(parent)
        column.pack(side="left", padx=Design.Padding.Xs, anchor="n")

        ttk.Label(
            column,
            text=title,
            font=Design.Typography.Font_bold,
            foreground=Design.Colors.Subtext,
        ).pack(anchor="w", pady=(0, Design.Padding.Sm))

        for item in items:
            var = tk.BooleanVar()
            ttk.Checkbutton(
                column,
                text=item,
                variable=var,
                style="Checklist.TCheckbutton",
            ).pack(anchor="w", pady=Design.Padding.Xs)
            checklist_vars.append(var)

    build_column(columns_container, "Primeiros Passos", software_items)
    build_column(columns_container, "Configurar", config_items)

    def clear_checklist():
        for var in checklist_vars:
            var.set(False)

    ttk.Button(
        frame,
        text="Limpar Checklist",
        command=clear_checklist,
        style="Accent.TButton",
    ).pack(pady=Design.Padding.Xs)

    ttk.Separator(frame).pack(fill="x", pady=Design.Padding.Md)

    ttk.Label(
        frame,
        text="RelSyS © 2026",
        font=Design.Typography.Font_small_italic,
        foreground=Design.Colors.Subtext,
    ).pack()
