import tkinter as tk
from tkinter import ttk


def tab_checklist(app, container):
    frame = ttk.Frame(container, padding=40)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    checklist_vars = []

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
    ]

    ttk.Label(
        frame,
        text="Checklist de Preparação",
        font=("Times New Roman", 16, "bold"),
        foreground=app.colors["text_color"],
    ).pack(pady=(0, 25))

    columns_container = ttk.Frame(frame)
    columns_container.pack(pady=20)

    def build_column(parent, title, items):
        column = ttk.Frame(parent)
        column.pack(side="left", padx=30, anchor="n")

        ttk.Label(
            column,
            text=title,
            font=("Times New Roman", 12, "bold"),
            foreground=app.colors["subtext_color"],
        ).pack(anchor="w", pady=(0, 10))

        for item in items:
            var = tk.BooleanVar()
            ttk.Checkbutton(
                column,
                text=item,
                variable=var,
                style="Checklist.TCheckbutton",
            ).pack(anchor="w")
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
    ).pack(pady=20)

    ttk.Separator(frame, orient="horizontal").pack(fill="x", pady=15)

    ttk.Label(
        frame,
        text="RelSyS © 2025",
        font=("Times New Roman", 9, "italic"),
        foreground=app.colors["subtext_color"],
    ).pack()
