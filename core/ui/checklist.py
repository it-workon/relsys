# checklist_tab.py
import tkinter as tk
from tkinter import ttk


class ChecklistTab:
    def __init__(self, colors):
        self.colors = colors
        self.check_vars = []

    def build(self, container):
        frame = ttk.Frame(container, padding=40, style="TFrame")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        itens_software = [
            "Criar o Suporte / Dar ADM ao suporte", "Logar no suporte", "Colocar WIFI",
            "Colocar no domínio e o nome", "Entrar na minha conta",
            "Baixar Chrome", "Baixar AnyDesk", "Baixar FortClient", "Baixar WINRAR",
            "Baixar Office", "Baixar Gi", "Baixar Java", "Baixar Adobe",
            "Baixar o BitDefender", "Baixar o PaperCut"
        ]

        itens_config = [
            "Ativar Suporte", "Email / Assinatura", "Teams",
            "GI", "Fortclient", "PaperCut", "Impressora",
            "Conferir Dowloads", "Imprimir Bem Vindo"
        ]

        duas_colunas = ttk.Frame(frame, style="TFrame")
        duas_colunas.pack(pady=20)

        # =============================
        #       COLUNA 1 - SOFTWARE
        # =============================
        col1 = ttk.Frame(duas_colunas, style="TFrame")
        col1.grid(row=0, column=0, padx=30, sticky="nw")

        ttk.Label(
            col1,
            text="Primeiros Passos",
            style="TLabel",
            font=("Times New Roman", 12, "bold"),
            foreground=self.colors["subtext_color"]
        ).pack(anchor="w", pady=(0, 10))

        for item in itens_software:
            var = tk.BooleanVar()
            chk = ttk.Checkbutton(
                col1,
                text=item,
                variable=var,
                style="Checklist.TCheckbutton"
            )
            chk.pack(anchor="w")
            self.check_vars.append(var)

        # =============================
        #       COLUNA 2 - CONFIG
        # =============================
        col2 = ttk.Frame(duas_colunas, style="TFrame")
        col2.grid(row=0, column=1, padx=30, sticky="nw")

        ttk.Label(
            col2,
            text="Configurar",
            style="TLabel",
            font=("Times New Roman", 12, "bold"),
            foreground=self.colors["subtext_color"]
        ).pack(anchor="w", pady=(0, 10))

        for item in itens_config:
            var = tk.BooleanVar()
            chk = ttk.Checkbutton(
                col2,
                text=item,
                variable=var,
                style="Checklist.TCheckbutton"
            )
            chk.pack(anchor="w")
            self.check_vars.append(var)

        ttk.Button(
            frame,
            text="Limpar Checklist",
            style="Accent.TButton",
            command=self.clear_checklist
        ).pack(pady=15)

        ttk.Separator(frame, orient="horizontal").pack(fill="x", pady=15)

        ttk.Label(
            frame,
            text="RelSyS © 2025",
            style="TLabel",
            font=("Times New Roman", 9, "italic"),
            foreground=self.colors["subtext_color"]
        ).pack()

    def clear_checklist(self):
        for var in self.check_vars:
            var.set(False)
