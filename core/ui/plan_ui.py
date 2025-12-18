from tkinter import ttk, messagebox
from services.plan_service import register_machine_plan


def tab_plan(app, container):
    frame = ttk.Frame(container, padding=40)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    ttk.Label(
        frame,
        text="Plano de Máquina",
        font=("Times New Roman", 16, "bold"),
        foreground=app.colors["text_color"],
    ).pack(pady=(0, 25))

    fields = [
        ("Nome do Computador", "computer_name"),
        ("Nome de Usuário", "username"),
        ("Colaborador", "employee_name"),
        ("Departamento", "department"),
        ("Patrimônio", "asset_tag"),
        ("Locadora", "leasing_company"),
        ("Modelo", "model"),
        ("Office", "office_version"),
    ]

    entries = {}

    for label_text, key in fields:
        ttk.Label(frame, text=label_text).pack(anchor="w", pady=(10, 2))
        entry = ttk.Entry(frame, width=40)
        entry.pack(ipady=5)
        entries[key] = entry

    def on_save_plan():
        try:
            path = register_machine_plan(
                **{key: entry.get().strip() for key, entry in entries.items()}
            )
            messagebox.showinfo(
                "Sucesso",
                f"Plano registrado com sucesso!\n\nCaminho:\n{path}",
            )
        except Exception as exc:
            messagebox.showerror("Erro", str(exc))

    ttk.Button(
        frame,
        text="Registrar Plano",
        command=on_save_plan,
        style="Accent.TButton",
    ).pack(pady=25)
