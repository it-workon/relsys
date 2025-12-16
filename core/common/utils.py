import os
def format_filename(user_name: str, directory: str = ".") -> str:
    
    parts = user_name.split(".")
    if len(parts) != 2:
        raise ValueError("Formato inválido. Use nome.sobrenome")

    formatted = f"{parts[0].capitalize()} {parts[1].capitalize()}"
    file_name = f"Boas Vindas - {formatted}"
    return os.path.join(directory, file_name)

