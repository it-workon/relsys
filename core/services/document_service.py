from pathlib import Path

from common.config import data, TEMPLATES_DIR, OUTPUT_DIR
from common.generator import generate_password
from common.utils import format_filename

from infra.document_infra import fill_template


def generate_document(user_name: str, process_num: str, systems: list) -> str:
    if not user_name:
        raise ValueError("Nome inválido")

    password = generate_password(user_name)

    replacements = {
        "{NAME}": user_name,
        "{PASS}": password,
        "{PROCESS_NUMBER}": process_num,
        "{DOMAIN_ORG}": "workongroup.com.br",
        "{ASSET}": "XXX-123456"
    }

    todos_sistemas = ["Windows", "Email", "Ginfor", "Teams", "VBD", "FortClient"]

    for sistema in todos_sistemas:
        key_login = f"{{LOGIN_{sistema.upper()}}}"
        key_pass = f"{{PASS_{sistema.upper()}}}"
        
        if sistema in systems:
            replacements[key_login] = data.get(f"login_{sistema.lower()}", user_name)
            replacements[key_pass] = data.get(f"pass_{sistema.lower()}", password)
        else:
            replacements[key_login] = "Acesso não criado!"
            replacements[key_pass] = "Acesso não criado!"

    output_file = OUTPUT_DIR / f"{format_filename(user_name)}.docx"

    fill_template(
        template_path=Path(TEMPLATES_DIR), 
        output_path=output_file, 
        data=replacements
    )

    return str(output_file)