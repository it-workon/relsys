from tkinter import ttk, messagebox

from design import Design
from services.document_service import generate_document


def tab_create_docs(app, container):
    frame = ttk.Frame(container, padding=Design.Padding.Lg)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Title
    ttk.Label(
        frame,
        text="Gerador de Relatórios",
        font=Design.Typography.Font_bold,  # ↓ antes: Font_title
        foreground=Design.Colors.Text,
    ).pack(pady=(0, Design.Padding.Md))

    # Name
    ttk.Label(
        frame,
        text="Nome (formato: nome.sobrenome)",
    ).pack(pady=(Design.Padding.Xs, Design.Padding.Xs))

    name_entry = ttk.Entry(frame, width=32)
    name_entry.pack(ipady=Design.Padding.Xs)

    # Process
    ttk.Label(
        frame,
        text="Número do processo (formato: XXXXXX)",
    ).pack(pady=(Design.Padding.Md, Design.Padding.Xs))

    process_entry = ttk.Entry(frame, width=32)
    process_entry.pack(ipady=Design.Padding.Xs)

    def on_generate_document():
        try:
            path = generate_document(
                user_name=name_entry.get().strip(),
                process_num=process_entry.get().strip(),
            )

            messagebox.showinfo(
                "Sucesso",
                f"Relatório gerado com sucesso!\n\nCaminho:\n{path}",
            )
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    # Button
    ttk.Button(
        frame,
        text="Gerar Relatório",
        command=on_generate_document,
        style="Accent.TButton",
    ).pack(pady=Design.Padding.Lg)

    ttk.Separator(frame).pack(fill="x", pady=Design.Padding.Md)

    ttk.Label(
        frame,
        text="RelSyS © 2026",
        font=Design.Typography.Font_small_italic,
        foreground=Design.Colors.Subtext,
    ).pack()
