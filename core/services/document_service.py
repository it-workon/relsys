from pathlib import Path

from common.config import data, TEMPLATES_DIR, OUTPUT_DIR
from common.generator import generate_password
from common.utils import format_filename

from infra.document_infra import fill_template


def generate_document(user_name: str, process_num: str) -> str:
    if not user_name:
        raise ValueError("Nome inválido")

    password = generate_password(user_name)

    replacements = data.copy()
    replacements["{NAME}"] = user_name
    replacements["{PASSWD}"] = password
    replacements["{PROCESS}"] = process_num

    output_file = OUTPUT_DIR / f"{format_filename(user_name)}.docx"

    fill_template(
        template_path=Path(TEMPLATES_DIR), output_path=output_file, data=replacements
    )

    return str(output_file)
