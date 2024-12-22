import os
from utils.file_utils import ensure_directory_exists

def handle_auto_save_file(custom_save_name: str) -> tuple[bool, str | None]:
    """
    Lida com a lógica de verificação e sobrescrita do arquivo de autosave para o arg auto_save_file.

    Parâmetros:
    custom_save_name (str) → Nome personalizado do arquivo de save.

    Retorno:
    tuple[bool, str | None] → (True, nome do arquivo) se a operação continuar, (False, None) se for cancelada.
    """
    ensure_directory_exists('saves')
    auto_save_path = f"saves/{custom_save_name}.save"
    if os.path.exists(auto_save_path):
        confirm = input(f"O arquivo '{auto_save_path}' já existe. Deseja sobrescrevê-lo? (s/n): ").strip().lower()
        if confirm != 's':
            print("Operação cancelada.")
            return False, None
    return True, auto_save_path