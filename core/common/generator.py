import re
from common.state import global_passwd


def validate_format(user_name: str) -> bool:
    std = r"^[A-Za-zÀ-ÖØ-öø-ÿ]+\.[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    return bool(re.match(std, user_name))


def generate_password(user_name) -> str:

    if not validate_format(user_name):
        raise ValueError("Formato inválido! \nUse o formato: 'nome.sobrenome'")

    parts = user_name.split(".")
    first = parts[0][0].upper()
    first += parts[0][1]
    second = parts[1][0].capitalize()

    passwd = f"{first}{second}@work2025"

    return passwd
