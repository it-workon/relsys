import tkinter as tk
from tkinter import ttk, messagebox
from generator import generate_password
from document import generate_document
from pathlib import Path
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("RelSyS - Emissor de Relatórios")
        self.geometry("640x480")
        self.configure(bg="#1E1E1E")
        self.resizable(False, False)

        style = ttk.Style(self)
        style.theme_use("clam")

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
            font=("Times New Roman", 10, "bold"),
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

        notebook = ttk.Notebook(self)
        notebook.pack(expand=True, fill="both", padx=25, pady=25)

        tab_documents = ttk.Frame(notebook)
        notebook.add(tab_documents, text="Gerar Relatório")
        self.tab_create_docs(tab_documents)
        tab_sheets = ttk.Frame(notebook)
        notebook.add(tab_sheets, text="Configuração Máquina")
        self.tab_config_note(tab_sheets)

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
        name_entry = ttk.Entry(
            frame,
            width=35,
            font=("Times New Roman", 10)
        )
        name_entry.pack(ipady=6)

        ttk.Label(frame, text="Número do processo (formato: XXXXXX)").pack(pady=(20, 5))
        process_entry = ttk.Entry(
            frame,
            width=35,
            font=("Times New Roman", 10)
        )
        process_entry.pack(ipady=6)

        ttk.Button(
            frame,
            text="Gerar Relatório",
            command=lambda: self.on_generate_document(
                name_entry.get(),
                process_num=process_entry.get()
            ),
            style="Accent.TButton"
        ).pack(pady=30)

        ttk.Separator(frame, orient="horizontal").pack(fill="x", pady=15)
        ttk.Label(
            frame,
            text="RelSyS © 2025",
            font=("Times New Roman", 9, "italic"),
            foreground=self.subtext_color
        ).pack()

    def on_generate_document(self, user_name: str, process_num: str):
        try:
            user_name = user_name.strip()
            passwd = generate_password(user_name)
            path = generate_document(user_name, passwd, process_num)
            messagebox.showinfo(
                "Sucesso",
                f"Relatório gerado com sucesso!\n\nCaminho:\n{path}"
            )
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def tab_config_note(self, container):
        frame = ttk.Frame(container, padding=40)
        frame.place(relx=0.5, rely=0.5, anchor="center")


        ttk.Separator(frame, orient="horizontal").pack(fill="x", pady=15)
        ttk.Label(
            frame,
            text="RelSyS © 2025",
            font=("Times New Roman", 9, "italic"),
            foreground=self.subtext_color
        ).pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()
