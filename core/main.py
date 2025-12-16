import ttkbootstrap as tb
from tkinter import ttk
from ttkbootstrap.constants import *
from style import apply_styles

from core.tabs.document import tab_create_docs
from core.tabs.checklist import ChecklistTab
from core.tabs.plan import tab_plan_note
from core.tabs.termination import tab_termination
from common import Design

class App(tb.Window):
    def __init__(self):
        super().__init__(themename="darkly")
        self.title("RelSyS - Emissor de Relatórios")
        self.geometry("820x620")
        self.configure(bg=Design.Colors.Bg_main)
        self.resizable(False, False)

        # apply styles from style.py
        self.colors = apply_styles(self)

        notebook = ttk.Notebook(self)
        notebook.pack(expand=True, fill="both", padx=25, pady=25)

        # generate document tab
        tab_documents = ttk.Frame(notebook)
        notebook.add(tab_documents, text="Gerar Relatório")
        tab_create_docs(self, tab_documents)

        # checklist tab
        tab_sheets = ttk.Frame(notebook)
        notebook.add(tab_sheets, text="Checklist Máquina")
        ChecklistTab(self, tab_sheets)

        # plan sheets tab
        tab_plan = ttk.Frame(notebook)
        notebook.add(tab_plan, text="Planilhar Máquina")
        tab_plan_note(self, tab_plan)

        # Termination tab
        tab_termination = ttk.Frame(notebook)
        notebook.add(tab_termination, text="Desligamento")
        tab_termination(self, tab_termination)


if __name__ == "__main__":
    app = App()
    app.mainloop()
