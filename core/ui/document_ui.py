from tkinter import ttk, messagebox

from design import Design
from services.document_service import generate_document


def tab_create_docs(app, container):
    frame = ttk.Frame(container, padding=Design.Padding.Xl)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    ttk.Label(
        frame,
        text="Gerador de Relatórios",
        font=Design.Typography.Font_title,
        foreground=Design.Colors.Text,
    ).pack(pady=(0, Design.Padding.Lg))

    ttk.Label(
        frame,
        text="Nome (formato: nome.sobrenome)",
    ).pack(pady=(Design.Padding.Sm, Design.Padding.Xs))

    name_entry = ttk.Entry(frame, width=35)
    name_entry.pack(ipady=Design.Padding.Sm)

    ttk.Label(
        frame,
        text="Número do processo (formato: XXXXXX)",
    ).pack(pady=(Design.Padding.Lg, Design.Padding.Xs))

    process_entry = ttk.Entry(frame, width=35)
    process_entry.pack(ipady=Design.Padding.Sm)

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

    ttk.Button(
        frame,
        text="Gerar Relatório",
        command=on_generate_document,
        style="Accent.TButton",
    ).pack(pady=Design.Padding.Xl)

    ttk.Separator(frame).pack(fill="x", pady=Design.Padding.Lg)

    ttk.Label(
        frame,
        text="RelSyS © 2025",
        font=Design.Typography.Font_small_italic,
        foreground=Design.Colors.Subtext,
    ).pack()
