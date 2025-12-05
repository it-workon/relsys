import tkinter as tk 
import ttkbootstrap as tb
from tkinter import ttk, messagebox
from ttkbootstrap.constants import *
from generator import generate_password
from document import generate_document
from desligamento import salvar_registro
from plan_note import salvar_plan_note
from ExternoEmail import salvar_email_externo
from pathlib import Path

class App(tb.Window):
    def __init__(self):
        super().__init__(themename="darkly")
        self.title("RelSyS - Emissor de Relatórios")
        self.geometry("820x620")
        self.configure(bg="#1E1E1E")
        self.resizable(False, False)

        style = tb.Style()

        self.accent_color = "#5B7FFF"
        self.bg_main = "#1E1E1E"
        self.bg_card = "#2A2A2A"
        self.text_color = "#E0E0E0"
        self.subtext_color = "#B0B0B0"

        style.configure("TNotebook", background=self.bg_main, borderwidth=0)
        style.configure(
            "TNotebook.Tab",
            background="#2E2E2E",
            padding=[18, 10],
            font=("Arial", 10, "bold"),
            foreground=self.subtext_color
        )
        style.map(
            "TNotebook.Tab",
            background=[("selected", self.accent_color)],
            foreground=[("selected", "white")]
        )

        style.configure("TFrame", background=self.bg_card)
        style.configure(
            "TLabel",
            background=self.bg_card,
            font=("Times New Roman", 10),
            foreground=self.text_color
        )
        style.configure(
            "TButton",
            font=("Times New Roman", 10, "bold"),
            padding=10,
            borderwidth=0
        )
        style.map(
            "TButton",
            background=[("active", "#4866E1")],
            foreground=[("active", "white")]
        )

        style.configure(
            "Accent.TButton",
            background=self.accent_color,
            foreground="white",
            relief="flat"
        )
        style.map(
            "Accent.TButton",
            background=[("active", "#4866E1"), ("pressed", "#384FC1")]
        )

        style.configure(
            "Checklist.TCheckbutton",
            background=self.bg_card,
            foreground=self.text_color,
            font=("Times New Roman", 10),
            relief="flat"
        )

        notebook = ttk.Notebook(self)
        notebook.pack(expand=True, fill="both", padx=25, pady=25)

        tab_documents = ttk.Frame(notebook)
        notebook.add(tab_documents, text="Gerar Relatório")
        self.tab_create_docs(tab_documents)

        tab_sheets = ttk.Frame(notebook)
        notebook.add(tab_sheets, text="Checklist Máquina")
        self.tab_config_note(tab_sheets)

        tab_plan = ttk.Frame(notebook)
        notebook.add(tab_plan, text="Planilhar Máquina")
        self.tab_plan_note(tab_plan)

        tab_termination = ttk.Frame(notebook)
        notebook.add(tab_termination, text="Desligamento")
        self.tab_termination(tab_termination)

        tab_externo_email = ttk.Frame(notebook)
        notebook.add(tab_externo_email, text="E-mail Externo")
        self.tab_externo_email(tab_externo_email)



    def tab_externo_email(self, container):
        frame = ttk.Frame(container, padding=40)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(
            frame,
            text="Cadastro — E-mail de Colaborador Externo",
            font=("Times New Roman", 16, "bold"),
            foreground=self.text_color
        ).pack(pady=(0, 20))

        campos_frame = ttk.Frame(frame)
        campos_frame.pack(pady=20)

        def campo(texto):
            ttk.Label(campos_frame, text=texto).pack(anchor="w")
            e = ttk.Entry(campos_frame, width=45)
            e.pack(pady=3)
            return e

        self.nome_ext_entry = campo("Nome Completo:")
        self.cliente_ext_entry = campo("Cliente:")
        self.cc_ext_entry = campo("Centro de Custo:")
        self.desc_ext_entry = campo("Descrição (opcional):")

        ttk.Button(
            frame,
            text="Salvar E-mail Externo",
            style="Accent.TButton",
            command=self.on_save_externo_email
        ).pack(pady=20)

        ttk.Separator(frame, orient="horizontal").pack(fill="x", pady=15)
        ttk.Label(
            frame,
            text="RelSyS © 2025",
            font=("Times New Roman", 9, "italic"),
            foreground=self.subtext_color
        ).pack()

    def on_save_externo_email(self):
        try:
            path = salvar_email_externo(
                self.nome_ext_entry.get(),
                self.cliente_ext_entry.get(),
                self.cc_ext_entry.get(),
                self.desc_ext_entry.get()
            )

            messagebox.showinfo(
                "Sucesso",
                f"E-mail externo salvo com sucesso!\n\nArquivo:\n{path}"
            )

        except Exception as e:
            messagebox.showerror("Erro ao salvar", str(e))



    def tab_create_docs(self, container):
        frame = ttk.Frame(container, padding=40)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(
            frame,
            text="Gerador de Relatórios",
            font=("Times New Roman", 16, "bold"),
            foreground="#F5F5F5"
        ).pack(pady=(0, 25))

        ttk.Label(frame, text="Nome (formato: nome.sobrenome)").pack(pady=(10, 5))
        name_entry = ttk.Entry(frame, width=35)
        name_entry.pack(ipady=6)

        ttk.Label(frame, text="Número do processo").pack(pady=(20, 5))
        process_entry = ttk.Entry(frame, width=35)
        process_entry.pack(ipady=6)

        ttk.Button(
            frame,
            text="Gerar Relatório",
            command=lambda: self.on_generate_document(name_entry.get(), process_num=process_entry.get()),
            style="Accent.TButton"
        ).pack(pady=30)

        ttk.Separator(frame, orient="horizontal").pack(fill="x", pady=15)
        ttk.Label(frame, text="RelSyS © 2025", font=("Times New Roman", 9, "italic")).pack()

    def on_generate_document(self, user_name: str, process_num: str):
        try:
            passwd = generate_password(user_name.strip())
            path = generate_document(user_name.strip(), passwd, process_num)
            messagebox.showinfo("Sucesso", f"Gerado!\n{path}")
        except Exception as e:
            messagebox.showerror("Erro", str(e))



    def tab_config_note(self, container):
        frame = ttk.Frame(container, padding=40)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        self.check_vars = []

        itens_software = [
            "Criar o Suporte / Dar ADM ao suporte", "Logar no suporte", "Colocar WIFI",
            "Colocar no domínio e o nome", "Entrar na minha conta",
            "Baixar Chrome", "Baixar AnyDesk", "Baixar FortClient", "Baixar WINRAR",
            "Baixar Office", "Baixar Gi", "Baixar Java", "Baixar Adobe",
            "Baixar o BitDefender", "Baixar o PaperCut"
        ]

        itens_config = [
            "Ativar Suporte", "Email / Assinatura", "Teams",
            "GI", "Fortclient", "PaperCut", "Impressora", "Conferir Dowloads", "Imprimir Bem Vindo"
        ]

        duas_colunas = ttk.Frame(frame)
        duas_colunas.pack(pady=20)

        col1 = ttk.Frame(duas_colunas)
        col1.grid(row=0, column=0, padx=30)

        ttk.Label(col1, text="Primeiros Passos", font=("Times New Roman", 12, "bold")).pack(anchor="w", pady=(0, 10))
        for item in itens_software:
            var = tk.BooleanVar()
            ttk.Checkbutton(col1, text=item, variable=var, style="Checklist.TCheckbutton").pack(anchor="w")
            self.check_vars.append(var)

        col2 = ttk.Frame(duas_colunas)
        col2.grid(row=0, column=1, padx=30)

        ttk.Label(col2, text="Configurar", font=("Times New Roman", 12, "bold")).pack(anchor="w", pady=(0, 10))
        for item in itens_config:
            var = tk.BooleanVar()
            ttk.Checkbutton(col2, text=item, variable=var, style="Checklist.TCheckbutton").pack(anchor="w")
            self.check_vars.append(var)

        ttk.Button(frame, text="Limpar Checklist", command=self.limpar_checklist).pack()

        ttk.Separator(frame, orient="horizontal").pack(fill="x", pady=15)
        ttk.Label(frame, text="RelSyS © 2025", font=("Times New Roman", 9, "italic")).pack()

    def limpar_checklist(self):
        for var in self.check_vars:
            var.set(False)



    def tab_plan_note(self, container):
        frame = ttk.Frame(container, padding=40)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(frame, text="Planilhar Máquina", font=("Times New Roman", 16, "bold")).pack(pady=(0, 20))

        campos_frame = ttk.Frame(frame)
        campos_frame.pack(pady=20)

        def campo(nome):
            ttk.Label(campos_frame, text=nome).pack(anchor="w")
            e = ttk.Entry(campos_frame, width=45)
            e.pack(pady=3)
            return e

        self.pc_nome_entry = campo("Nome do computador:")
        self.user_nome_entry = campo("Nome de usuário:")
        self.colab_entry_plan = campo("Colaborador:")
        self.dep_entry = campo("Departamento:")
        self.patrimonio_entry = campo("Patrimônio:")
        self.locadora_entry = campo("Locadora:")
        self.modelo_entry = campo("Modelo:")
        self.office_entry = campo("Office:")

        ttk.Button(
            frame,
            text="Salvar na Planilha",
            style="Accent.TButton",
            command=self.on_save_plan_note
        ).pack(pady=20)

        ttk.Separator(frame, orient="horizontal").pack(fill="x", pady=15)
        ttk.Label(frame, text="RelSyS © 2025", font=("Times New Roman", 9, "italic")).pack()

    def on_save_plan_note(self):
        try:
            path = salvar_plan_note(
                self.pc_nome_entry.get(),
                self.user_nome_entry.get(),
                self.colab_entry_plan.get(),
                self.dep_entry.get(),
                self.patrimonio_entry.get(),
                self.locadora_entry.get(),
                self.modelo_entry.get(),
                self.office_entry.get()
            )
            messagebox.showinfo("Sucesso", f"Registro salvo!\n{path}")
        except Exception as e:
            messagebox.showerror("Erro", str(e))



    def tab_termination(self, container):
        frame = ttk.Frame(container, padding=40)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(frame, text="Checklist de Desligamento", font=("Times New Roman", 16, "bold")).pack(pady=(0, 20))

        checks_frame = ttk.Frame(frame)
        checks_frame.pack()

        self.ad_var = tk.BooleanVar()
        self.email_var = tk.BooleanVar()
        self.gi_var = tk.BooleanVar()
        self.vbd_var = tk.BooleanVar()
        self.teams_var = tk.BooleanVar()
        self.forti_var = tk.BooleanVar()
        self.papercut_var = tk.BooleanVar()

        col1 = ttk.Frame(checks_frame)
        col1.grid(row=0, column=0, padx=25)

        col2 = ttk.Frame(checks_frame)
        col2.grid(row=0, column=1, padx=25)

        ttk.Checkbutton(col1, text="AD", variable=self.ad_var, style="Checklist.TCheckbutton").pack(anchor="w")
        ttk.Checkbutton(col1, text="E-mail", variable=self.email_var, style="Checklist.TCheckbutton").pack(anchor="w")
        ttk.Checkbutton(col1, text="GI", variable=self.gi_var, style="Checklist.TCheckbutton").pack(anchor="w")
        ttk.Checkbutton(col1, text="VBD", variable=self.vbd_var, style="Checklist.TCheckbutton").pack(anchor="w")

        ttk.Checkbutton(col2, text="Teams", variable=self.teams_var, style="Checklist.TCheckbutton").pack(anchor="w")
        ttk.Checkbutton(col2, text="FortiClient", variable=self.forti_var, style="Checklist.TCheckbutton").pack(anchor="w")
        ttk.Checkbutton(col2, text="PaperCut", variable=self.papercut_var, style="Checklist.TCheckbutton").pack(anchor="w")

        campos_frame = ttk.Frame(frame)
        campos_frame.pack(pady=20)

        def campo(nome):
            ttk.Label(campos_frame, text=nome).pack(anchor="w")
            e = ttk.Entry(campos_frame, width=45)
            e.pack(pady=3)
            return e

        self.colab_entry = campo("Nome do colaborador:")
        self.backup_entry = campo("Backup:")
        self.aut_entry = campo("Autorização:")
        self.data_entry = campo("Data da demissão:")
        self.zeev_entry = campo("Zeev:")
        self.termo_entry = campo("Termo (link):")

        ttk.Button(
            frame,
            text="Salvar na Planilha",
            style="Accent.TButton",
            command=self.on_save_termination
        ).pack(pady=20)

        ttk.Separator(frame, orient="horizontal").pack(fill="x", pady=15)
        ttk.Label(frame, text="RelSyS © 2025", font=("Times New Roman", 9, "italic")).pack()

    def on_save_termination(self):
        try:
            path = salvar_registro(
                self.colab_entry.get(),
                self.ad_var.get(),
                self.email_var.get(),
                self.gi_var.get(),
                self.vbd_var.get(),
                self.teams_var.get(),
                self.forti_var.get(),
                self.papercut_var.get(),
                self.backup_entry.get(),
                self.aut_entry.get(),
                self.data_entry.get(),
                self.zeev_entry.get(),
                self.termo_entry.get()
            )
            messagebox.showinfo("Sucesso", f"Registro salvo!\n{path}")
        except Exception as e:
            messagebox.showerror("Erro ao salvar", str(e))


if __name__ == "__main__":
    app = App()
    app.mainloop()
