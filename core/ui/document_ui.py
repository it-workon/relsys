from tkinter import ttk, messagebox

from services.document_service import generate_document


def tab_create_docs(app, container):
    frame = ttk.Frame(container, padding=40)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    ttk.Label(
        frame,
        text="Gerador de Relatórios",
        font=("Times New Roman", 16, "bold"),
        foreground="#F5F5F5"
    ).pack(pady=(0, 25))

    ttk.Label(frame, text="Nome (formato: nome.sobrenome)").pack(pady=(10, 5))
    name_entry = ttk.Entry(frame, width=35, font=("Times New Roman", 10))
    name_entry.pack(ipady=6)

    ttk.Label(frame, text="Número do processo (formato: XXXXXX)").pack(pady=(20, 5))
    process_entry = ttk.Entry(frame, width=35, font=("Times New Roman", 10))
    process_entry.pack(ipady=6)

    def on_generate_document():
        try:
            path = generate_document(
                user_name=name_entry.get().strip(),
                process_num=process_entry.get().strip()
            )

            messagebox.showinfo(
                "Sucesso",
                f"Relatório gerado com sucesso!\n\nCaminho:\n{path}"
            )
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    ttk.Button(
        frame,
        text="Gerar Relatório",
        command=on_generate_document,
        style="Accent.TButton"
    ).pack(pady=30)

    ttk.Separator(frame, orient="horizontal").pack(fill="x", pady=15)

    ttk.Label(
        frame,
        text="RelSyS © 2025",
        font=("Times New Roman", 9, "italic"),
        foreground=app.colors["subtext_color"]
    ).pack()
