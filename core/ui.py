import tkinter as tk
from tkinter import ttk, messagebox
from passwd_gen import generate_password

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("RelSyS - Emissor de Relatórios")
        self.geometry("700x480")
        
        notebook = ttk.Notebook(self)
        notebook.pack(expand=True, fill="both")
        
        tab_documents = ttk.Frame(notebook)
        notebook.add(tab_documents, text="Gerar Senha")
        self.tab_create_docs(tab_documents)
        
        
    def tab_create_docs(self, container):
        ttk.Label(container, text="Nome (formato nome.sobrenome):").pack(pady=10)
        entrada_nome = ttk.Entry(container, width=30)
        entrada_nome.pack()
        
        def generate():
            nome = entrada_nome.get().strip()
            try:
                senha = generate_password(nome)
                messagebox.showinfo("Senha Gerada", f"Senha: {senha}")
            except ValueError as e:
                messagebox.showerror("Erro", str(e))

        ttk.Button(container, text="Gerar Senha", command=generate).pack(pady=15)
        
if __name__ == "__main__":
    app = App()
    app.mainloop()