import ttkbootstrap as tb
from tkinter import ttk
from ttkbootstrap.constants import *

from design import Design
from design.apply import apply_design

from ui.document_ui import tab_create_docs
from ui.checklist_ui import tab_checklist
from ui.plan_ui import tab_plan
from ui.termination_ui import tab_termination


class App(tb.Window):
    def __init__(self):
        super().__init__(themename="darkly")

        self.title("RelSyS - Emissor de Relatórios")
        self.geometry("1168x940")
        self.configure(bg=Design.Colors.Bg_main)
        self.resizable(False, False)

        apply_design()

        notebook = ttk.Notebook(self)
        notebook.pack(expand=True, fill="both", padx=25, pady=25)

        # Document tab
        tab_documents_frame = ttk.Frame(notebook)
        notebook.add(tab_documents_frame, text="Gerar Relatório")
        tab_create_docs(self, tab_documents_frame)

        # Checklist tab
        tab_checklist_frame = ttk.Frame(notebook)
        notebook.add(tab_checklist_frame, text="Checklist")
        tab_checklist(self, tab_checklist_frame)

        # Plan tab
        tab_plan_frame = ttk.Frame(notebook)
        notebook.add(tab_plan_frame, text="Planilhar Máquina")
        tab_plan(self, tab_plan_frame)

        # Termination tab
        tab_term_frame = ttk.Frame(notebook)
        notebook.add(tab_term_frame, text="Desligamento")
        tab_termination(self, tab_term_frame)


if __name__ == "__main__":
    app = App()
    app.mainloop()
