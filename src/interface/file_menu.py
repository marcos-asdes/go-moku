from interface.display import display_message
from files.logging import log_error

def get_filename(files: list[str]) -> str | None:
    """
    Obtém o nome do arquivo para salvar, garantindo que o usuário confirme a sobrescrita se o arquivo já existir.

    Parâmetros:
    files (list[str]) → Lista de arquivos disponíveis.

    Retorno:
    str | None → Nome do arquivo escolhido ou None se o usuário optar por voltar.
    """
    filename = input("Digite o nome do novo arquivo (sem extensão): ") + ".save"
    if filename in files:
        confirm = input(f"O arquivo '{filename}' já existe. Deseja sobrescrevê-lo? (s/n): ").strip().lower()
        if confirm == 's':
            return filename
        else:
            display_message("Operação cancelada. Voltando ao menu de arquivos.")
            return None
    return filename

def get_choice(files: list[str]) -> str | None:
    """
    Obtém a escolha do usuário para carregar um arquivo existente.

    Parâmetros:
    files (list[str]) → Lista de arquivos disponíveis.

    Retorno:
    str | None → Nome do arquivo escolhido ou None se o usuário optar por voltar.
    """
    try:
        choice = int(input("Escolha um arquivo ou 0 para voltar: "))
        if choice == 0:
            return None
        if 1 <= choice <= len(files):
            return files[choice - 1]
        else:
            display_message("Escolha inválida. Por favor, escolha um número válido.")
    except ValueError as e:
        display_message("Entrada inválida. Por favor, insira um número válido.")
        log_error(str(e))
    return None

def handle_file_menu(action: str, files: list[str]) -> str | None:
    """
    Lida com a lógica do menu para salvar ou carregar jogos a partir de arquivos.

    Parâmetros:
    action (str) → Ação a ser realizada ('salvar' ou 'carregar').
    files (list[str]) → Lista de arquivos disponíveis.

    Retorno:
    str | None → Nome do arquivo escolhido ou None se o usuário optar por voltar.
    """
    while True:
        if action == 'salvar':
            filename = get_filename(files)
            if filename:
                return filename
        else:
            choice = get_choice(files)
            if choice:
                return choice