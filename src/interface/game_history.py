import os
from utils.constants import HISTORY_FILE_PATH
from utils.file_utils import ensure_directory_exists
from files.log_error import log_error

def show_game_history() -> None:
    """
    Exibe o histórico de partidas.

    Retorno:
    None
    """
    try:
        # Garantir que a pasta 'saves' exista
        ensure_directory_exists('saves')

        # Garantir que o arquivo 'history.txt' exista
        if not os.path.exists(HISTORY_FILE_PATH):
            with open(HISTORY_FILE_PATH, 'w') as file:
                file.write("")

        with open(HISTORY_FILE_PATH, 'r') as file:
            history = file.readlines()

        if not history:
            print("\nHistórico de partidas: Nenhuma partida finalizada")
        else:
            print("\nHistórico de partidas:")
            for line in history:
                print(line.strip())
    except Exception as e:
        print("Erro ao exibir o histórico de partidas. Verifique o arquivo de log para mais detalhes.")
        log_error(f"Erro ao exibir o histórico de partidas: {str(e)}")