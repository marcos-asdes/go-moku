import os
from interface import display_message
from utils import ensure_directory_exists

def show_game_history() -> None:
    """
    Exibe o histórico de partidas.

    Retorno:
    None
    """
    # Garantir que a pasta 'saves' exista
    ensure_directory_exists('saves')

    # Garantir que o arquivo 'history.txt' exista
    if not os.path.exists('saves/history.txt'):
        with open('saves/history.txt', 'w') as file:
            file.write("")

    with open('saves/history.txt', 'r') as file:
        history = file.readlines()

    if not history:
        display_message("\nHistórico de partidas: Nenhuma partida finalizada")
    else:
        display_message("\nHistórico de partidas:")
        for line in history:
            display_message(line.strip())