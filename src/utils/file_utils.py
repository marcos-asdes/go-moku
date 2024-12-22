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

def extract_save_name(file_name: str) -> str:
    """
    Extrai o nome personalizado do arquivo de save a partir do nome do arquivo.

    Parâmetros:
    file_name (str) → Nome do arquivo.

    Retorno:
    str → Nome personalizado do arquivo de save.
    """
    return file_name.split('.')[0]