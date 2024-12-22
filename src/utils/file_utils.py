import os

def ensure_directory_exists(directory: str) -> None:
    """
    Garante que o diretório especificado exista. Se não existir, ele será criado.

    Parâmetros:
    directory (str) → Caminho do diretório a ser verificado/criado.

    Retorno:
    None
    """
    os.makedirs(directory, exist_ok=True)