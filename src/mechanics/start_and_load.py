from files.file_operations import load_game
from interface.menus import show_file_menu
from mechanics.game_flow import play_game
from mechanics.game_initialization import initialize_game
from utils.file_utils import ensure_directory_exists

def start_new_game() -> bool:
    """
    Inicia um novo jogo.

    Retorno:
    bool → True se o jogo terminar normalmente, False se o jogador optar por voltar ao menu principal.
    """
    state = initialize_game(15)
    if not play_game(state):
        return False
    return True

def load_and_play_game() -> bool:
    """
    Carrega um jogo salvo e inicia o jogo.

    Retorno:
    bool → True se o jogo terminar normalmente, False se o jogador optar por voltar ao menu principal.
    """
    # Garantir que a pasta 'saves' exista
    ensure_directory_exists('saves')

    file = show_file_menu('carregar')
    if file:
        state = load_game(f"saves/{file}")
        if not play_game(state):
            return False
    return True