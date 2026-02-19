import tkinter as tk
from tkinter import ttk, messagebox

from design import Design
from services.termination_service import register_termination


def tab_termination(app, container):
    frame = ttk.Frame(container, padding=Design.Padding.Xs)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Título
    ttk.Label(
        frame,
        text="Checklist de Desligamento",
        font=Design.Typography.Font_title,
        foreground=Design.Colors.Text,
    ).pack(pady=(0, Design.Padding.Xs))

    # CHECKBOXES
    checkbox_vars = {
        "ad": tk.BooleanVar(),
        "email": tk.BooleanVar(),
        "gi": tk.BooleanVar(),
        "vbd": tk.BooleanVar(),
        "teams": tk.BooleanVar(),
        "forticlient": tk.BooleanVar(),
        "papercut": tk.BooleanVar(),
    }

    checklist_frame = ttk.Frame(frame)
    checklist_frame.pack()

    col_left = ttk.Frame(checklist_frame)
    col_left.grid(row=0, column=0, padx=Design.Padding.Xs)

    col_right = ttk.Frame(checklist_frame)
    col_right.grid(row=0, column=1, padx=Design.Padding.Xs)

    def checkbox(parent, label, var):
        ttk.Checkbutton(
            parent,
            text=label,
            variable=var,
            style="Checklist.TCheckbutton",
        ).pack(anchor="w", pady=Design.Padding.Xs)

    checkbox(col_left, "AD", checkbox_vars["ad"])
    checkbox(col_left, "E-mail", checkbox_vars["email"])
    checkbox(col_left, "GI", checkbox_vars["gi"])
    checkbox(col_left, "VBD", checkbox_vars["vbd"])

    checkbox(col_right, "Teams", checkbox_vars["teams"])
    checkbox(col_right, "FortiClient", checkbox_vars["forticlient"])
    checkbox(col_right, "PaperCut", checkbox_vars["papercut"])

    # TEXT FIELDS
    fields_frame = ttk.Frame(frame)
    fields_frame.pack(pady=Design.Padding.Xs)

    def text_field(label):
        ttk.Label(fields_frame, text=label).pack(anchor="w", pady=(Design.Padding.Sm, Design.Padding.Xs))
        entry = ttk.Entry(fields_frame, width=45)
        entry.pack(ipady=Design.Padding.Sm)
        return entry

    employee_entry = text_field("Nome do colaborador:")
    backup_entry = text_field("Backup:")
    authorization_entry = text_field("Autorização:")
    date_entry = text_field("Data da demissão:")
    zeev_entry = text_field("Zeev:")
    term_entry = text_field("Termo (link):")

    def on_save():
        try:
            path = register_termination(
                employee_name=employee_entry.get().strip(),
                ad_disabled=checkbox_vars["ad"].get(),
                email_disabled=checkbox_vars["email"].get(),
                gi_disabled=checkbox_vars["gi"].get(),
                vbd_disabled=checkbox_vars["vbd"].get(),
                teams_disabled=checkbox_vars["teams"].get(),
                forticlient_disabled=checkbox_vars["forticlient"].get(),
                papercut_disabled=checkbox_vars["papercut"].get(),
                backup=backup_entry.get().strip(),
                authorization=authorization_entry.get().strip(),
                termination_date=date_entry.get().strip(),
                zeev=zeev_entry.get().strip(),
                termination_term=term_entry.get().strip(),
            )

            messagebox.showinfo(
                "Sucesso",
                f"Registro salvo com sucesso!\n\nArquivo:\n{path}",
            )
        except Exception as exc:
            messagebox.showerror("Erro ao salvar", str(exc))

    ttk.Button(
        frame,
        text="Salvar na Planilha",
        command=on_save,
        style="Accent.TButton",
    ).pack(pady=Design.Padding.Xs)

    ttk.Separator(frame).pack(fill="x", pady=Design.Padding.Xs)

    ttk.Label(
        frame,
        text="RelSyS © 2026",
        font=Design.Typography.Font_small_italic,
        foreground=Design.Colors.Subtext,
    ).pack()
