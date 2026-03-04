import tkinter as tk
from tkinter import ttk

from design import Design


def tab_checklist(app, container):
    # Frame principal travado no centro da tela
    main_frame = ttk.Frame(container, padding=Design.Padding.Md)
    main_frame.place(relx=0.5, rely=0.5, anchor="center", width=600, height=600)

    ttk.Label(
        main_frame,
        text="Checklist de Máquina",
        font=Design.Typography.Font_title,
        foreground=Design.Colors.Text,
    ).pack(pady=(0, Design.Padding.Lg))

    # BOTÕES DE NAVEGAÇÃO
    nav_frame = ttk.Frame(main_frame)
    nav_frame.pack(pady=(0, Design.Padding.Lg))

    # CONTAINER DO CHECKLIST
    list_container = ttk.Frame(main_frame)
    list_container.pack(fill="both", expand=True)

    checklists = {
        "Verificação": [
            "Verificar Avarias externas",
            "Testar Teclado",
            "Testar Câmera",
            "Testar Brilho da Tela",
            "Testar Microfone",
            "Testar se conecta a internet",
            "Testar se Carrega / Mantém carga"
        ],
        "Configuração Básica": [
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
            "Baixar o BitDefender"
        ],
        "Usuário": [
            "Ativar Suporte",
            "Email / Assinatura",
            "Teams",
            "GI",
            "Fortclient",
            "Baixar PaperCut",
            "Configurar Impressora",
            "Planilhar Máquina",
            "Imprimir Bem Vindo"
        ]
    }

    def update_list(category):
        for widget in list_container.winfo_children():
            widget.destroy()

        ttk.Label(
            list_container,
            text=f"Etapa: {category}",
            font=Design.Typography.Font_bold,
            foreground=Design.Colors.Subtext,
        ).pack(anchor="n", pady=(10, 20))

        items_inner_frame = ttk.Frame(list_container)
        items_inner_frame.pack(anchor="n")

        for item in checklists[category]:
            var = tk.BooleanVar()
            ttk.Checkbutton(
                items_inner_frame,
                text=item,
                variable=var,
                style="Checklist.TCheckbutton",
            ).pack(anchor="w", pady=Design.Padding.Xs)

    for cat in checklists.keys():
        ttk.Button(
            nav_frame,
            text=cat,
            command=lambda c=cat: update_list(c),
            style="Accent.TButton",
        ).pack(side="left", padx=Design.Padding.Xs)

    footer_frame = ttk.Frame(main_frame)
    footer_frame.pack(side="bottom", fill="x", pady=(Design.Padding.Md, 0))
    
    ttk.Separator(footer_frame).pack(fill="x", pady=Design.Padding.Sm)
    ttk.Label(
        footer_frame,
        text="RelSyS © 2026",
        font=Design.Typography.Font_small_italic,
        foreground=Design.Colors.Subtext,
    ).pack()

    update_list("Verificação")