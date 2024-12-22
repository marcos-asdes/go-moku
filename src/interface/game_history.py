import os
from interface.display import display_message
from utils.file_utils import ensure_directory_exists
from utils.constants import HISTORY_FILE_PATH

def show_game_history() -> None:
    """
    Exibe o histórico de partidas.

    Retorno:
    None
    """
    # Garantir que a pasta 'saves' exista
    ensure_directory_exists('saves')

    # Garantir que o arquivo 'history.txt' exista
    if not os.path.exists(HISTORY_FILE_PATH):
        with open(HISTORY_FILE_PATH, 'w') as file:
            file.write("")

    with open(HISTORY_FILE_PATH, 'r') as file:
        history = file.readlines()

    if not history:
        display_message("\nHistórico de partidas: Nenhuma partida finalizada")
    else:
        display_message("\nHistórico de partidas:")
        for line in history:
            display_message(line.strip())