import tkinter as tk
from tkinter import ttk, messagebox
from generator import generate_password
from document import generate_document
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("RelSyS - Emissor de Relatórios")
        self.geometry("640x480")
        
        notebook = ttk.Notebook(self)
        notebook.pack(expand=True, fill="both")
        
        tab_documents = ttk.Frame(notebook)
        notebook.add(tab_documents, text="Gerar Relatório")
        self.tab_create_docs(tab_documents)
        
        
    def tab_create_docs(self, container):
        ttk.Label(container, text="Nome (formato nome.sobrenome)").pack(pady=10)
        name_entry = ttk.Entry(container, width=30)
        name_entry.pack()
        
        ttk.Label(container, text="Número do processo (formato: XXXXXX)").pack(pady=10)
        process_entry = ttk.Entry(container, width=30)
        process_entry.pack()
        
        ttk.Button(container, text="Gerar Relatório", command=lambda: self.on_generate_document(name_entry.get(), process_num=process_entry.get())).pack(pady=15)
    
      
    def on_generate_document(self, user_name: str, process_num: str):
        """Fluxo principal — valida, gera senha e documento."""
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
if __name__ == "__main__":
    app = App()
    app.mainloop()