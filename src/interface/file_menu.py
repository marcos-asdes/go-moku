import os
from files.log_error import log_error

def get_filename(files: list[str]) -> str | None:
    """
    Obtém o nome do arquivo para salvar, garantindo que o usuário confirme a sobrescrita se o arquivo já existir.

    Parâmetros:
    files (list[str]) → Lista de arquivos disponíveis.

    Retorno:
    str | None → Nome do arquivo escolhido ou None se o usuário optar por voltar.
    """
    try:
        filename = input("Digite o nome do novo arquivo (sem extensão): ") + ".save"
        if filename in files:
            confirm = input(f"O arquivo '{filename}' já existe. Deseja sobrescrevê-lo? (s/n): ").strip().lower()
            if confirm == 's':
                return filename
            else:
                print("Operação cancelada. Voltando ao menu de arquivos.")
                return None
        return filename
    except Exception as e:
        print("Erro ao obter o nome do arquivo. Verifique o arquivo de log para mais detalhes.")
        log_error(f"Erro ao obter o nome do arquivo: {str(e)}")
        return None

def get_choice(files: list[str]) -> str | None:
    """
    Obtém a escolha do usuário para carregar um arquivo existente.

    Parâmetros:
    files (list[str]) → Lista de arquivos disponíveis.

    Retorno:
    str | None → Nome do arquivo escolhido ou None se o usuário optar por voltar.
    """
    while True:
        try:
            choice = int(input("Escolha um arquivo ou 0 para voltar: "))
            if choice == 0:
                return None
            if 1 <= choice <= len(files):
                return files[choice - 1]
            else:
                print("Escolha inválida. Por favor, escolha um número válido.")
        except ValueError as e:
            print("Entrada inválida. Por favor, insira um número válido.")
            log_error(f"Entrada inválida durante a seleção de arquivo: {str(e)}")

def handle_file_menu(action: str, files: list[str]) -> str | None:
    """
    Lida com a lógica do menu para salvar ou carregar jogos a partir de arquivos.

    Parâmetros:
    action (str) → Ação a ser realizada ('salvar' ou 'carregar').
    files (list[str]) → Lista de arquivos disponíveis.

    Retorno:
    str | None → Nome do arquivo escolhido ou None se o usuário optar por voltar.
    """
    try:
        while True:
            if action == 'salvar':
                filename = get_filename(files)
                if filename:
                    return filename
            else:
                choice = get_choice(files)
                if choice is not None:
                    return choice
                else:
                    return None
    except Exception as e:
        print("Erro ao lidar com o menu de arquivos. Verifique o arquivo de log para mais detalhes.")
        log_error(f"Erro ao lidar com o menu de arquivos: {str(e)}")
        return None
    
def show_file_menu(action: str) -> str | None:
    """
    Mostra o menu para salvar ou carregar jogos a partir de arquivos.

    Parâmetros:
    action (str) → Ação a ser realizada ('salvar' ou 'carregar').

    Retorno:
    str | None → Nome do arquivo escolhido ou None se o usuário optar por voltar.
    """
    try:
        files = [f for f in os.listdir('saves') if f.endswith('.save')]
        print(f"\nMenu de arquivos para {action}:")
        print("Arquivos existentes:")
        for i, file in enumerate(files, 1):
            print(f"{i}. {file}")
        print("0. Voltar")
        return handle_file_menu(action, files)
    except Exception as e:
        print("Erro ao mostrar o menu de arquivos. Verifique o arquivo de log para mais detalhes.")
        log_error(f"Erro ao mostrar o menu de arquivos: {str(e)}")
        return None