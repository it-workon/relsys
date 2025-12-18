import ttkbootstrap as tb
from tkinter import ttk
from ttkbootstrap.constants import *

from style import apply_styles
from design import Design

from ui.document_ui import tab_create_docs
# from tabs.checklist import ChecklistTab
# from tabs.plan import tab_plan_note
# from tabs.termination import tab_termination


class App(tb.Window):
    def __init__(self):
        super().__init__(themename="darkly")

        self.title("RelSyS - Emissor de Relatórios")
        self.geometry("820x620")
        self.configure(bg=Design.Colors.Bg_main)
        self.resizable(False, False)

        self.colors = apply_styles(self)

        notebook = ttk.Notebook(self)
        notebook.pack(expand=True, fill="both", padx=25, pady=25)

        # Document tab
        tab_documents = ttk.Frame(notebook)
        notebook.add(tab_documents, text="Gerar Relatório")
        tab_create_docs(self, tab_documents)

        # Checklist tab
        # tab_sheets = ttk.Frame(notebook)
        # notebook.add(tab_sheets, text="Checklist Máquina")
        # ChecklistTab(self, tab_sheets)

        # Plan tab
        # tab_plan = ttk.Frame(notebook)
        # notebook.add(tab_plan, text="Planilhar Máquina")
        # tab_plan_note(self, tab_plan)

        # Termination tab
        # tab_term = ttk.Frame(notebook)
        # notebook.add(tab_term, text="Desligamento")
        # tab_termination(self, tab_term)


if __name__ == "__main__":
    app = App()
    app.mainloop()
