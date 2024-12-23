from files.file_operations import load_game
from interface.menus import show_file_menu
from mechanics.game_flow import play_game
from mechanics.game_initialization import initialize_game
from utils.constants import BOARD_SIZE
from utils.file_utils import ensure_directory_exists, extract_save_name

def start_new_game(mode: str, player1_name: str, player2_name: str = None) -> bool:
    """
    Inicia um novo jogo com o modo e nomes dos jogadores fornecidos.

    Parâmetros:
    mode (str) → Modo de jogo ('1' para um jogador, '2' para dois jogadores).
    player1_name (str) → Nome do jogador 1.
    player2_name (str) → Nome do jogador 2 (opcional).

    Retorno:
    bool → True se o jogo iniciar corretamente, False caso contrário.
    """
    size = 15  # Tamanho padrão do tabuleiro
    state = initialize_game(size, mode, player1_name, player2_name)
    return play_game(state)

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
        custom_save_name = extract_save_name(file)
        if not play_game(state, custom_save_name):
            return False
    return True