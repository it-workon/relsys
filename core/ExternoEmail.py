from openpyxl import load_workbook
from tkinter import messagebox

def salvar_email_externo(nome, cliente, centro_custo, descricao):

    caminho = r"Z:\NEW TECNOLOGIA\1 Documentação\2 Inventário\4 Emails\E-mails colaboradores externos - LOCAWEB.xlsx"

    # TENTA ABRIR A PLANILHA
    try:
        wb = load_workbook(caminho)
    except Exception as e:
        messagebox.showerror("Erro ao abrir planilha", f"Detalhes do erro:\n{e}")
        return  # <-- ESTAVA NO LUGAR ERRADO

    # TENTA CARREGAR A ABA
    try:
        ws = wb["BASE - LOCAWEB"]
    except Exception as e:
        messagebox.showerror(
            "Erro ao acessar aba",
            f"Aba 'BASE - LOCAWEB' não encontrada.\nDetalhes: {e}"
        )
        return  # <-- ESTAVA NO LUGAR ERRADO

    # CAMPOS OBRIGATÓRIOS
    if nome.strip() == "" or cliente.strip() == "" or centro_custo.strip() == "":
        messagebox.showwarning(
            "Campos faltando",
            "Nome, Cliente e Centro de Custo são obrigatórios."
        )
        return

    # FORMATAÇÕES
    nome_completo = nome.upper().strip()

    partes = nome.strip().split()
    primeiro = partes[0].lower()
    ultimo = partes[-1].lower()

    email = f"{primeiro}.{ultimo}@workontrademkt.com.br"
    usuario = f"{primeiro}.{ultimo}"
    status = "ATIVO"

    # PRÓXIMA LINHA DISPONÍVEL
    ultima = ws.max_row + 1

    # ESCREVE NA PLANILHA
    ws[f"A{ultima}"] = nome_completo
    ws[f"B{ultima}"] = cliente
    ws[f"C{ultima}"] = centro_custo
    ws[f"D{ultima}"] = descricao
    ws[f"E{ultima}"] = email
    ws[f"F{ultima}"] = status
    ws[f"G{ultima}"] = usuario

    # SALVA
    try:
        wb.save(caminho)
    except Exception as e:
        messagebox.showerror("Erro ao salvar", f"Detalhes do erro:\n{e}")
        return

    # SUCESSO
    messagebox.showinfo(
        "Sucesso!",
        f"Cadastro salvo com sucesso!\nE-mail gerado:\n{email}"
    )
