from interface.display import display_message
from files.logging import log_error

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
        try:
            if action == 'salvar':
                return input("Digite o nome do novo arquivo (sem extensão): ") + ".save"
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