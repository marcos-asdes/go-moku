import sys
from files.file_operations import load_game, save_game
from game.game_initialization import initialize_game
from interface.menus import show_credits, show_file_menu, show_game_rules, show_main_menu, show_pause_menu
from game.game_history import show_game_history
from interface.display import display_message
from utils.file_utils import ensure_directory_exists

def handle_pause_menu(state: dict) -> dict | None:
    """
    Gerencia o menu de pausa.

    Parâmetros:
    state (dict) → Estado atual do jogo.

    Retorno:
    dict | None → Novo estado do jogo após a ação do menu de pausa ou None se for para voltar ao menu principal.
    """
    while True:
        pause_action = show_pause_menu()
        if pause_action == '1':  # Iniciar novo jogo
            return initialize_game(state['size'])
        elif pause_action == '2':  # Carregar partida
            file = show_file_menu('carregar')
            if file:
                return load_game(f"saves/{file}")
        elif pause_action == '3':  # Salvar partida
            file = show_file_menu('salvar')
            if file:
                save_game(state, f"saves/{file}")
        elif pause_action == '4':  # Voltar ao jogo
            return state
        elif pause_action == '5':  # Voltar ao menu principal
            return None
        elif pause_action == '6':  # Sair
            sys.exit()

def start_new_game() -> bool:
    """
    Inicia um novo jogo.

    Retorno:
    bool → True se o jogo terminar normalmente, False se o jogador optar por voltar ao menu principal.
    """
    from game.game_flow import play_game
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
    from game.game_flow import play_game
    # Garantir que a pasta 'saves' exista
    ensure_directory_exists('saves')

    file = show_file_menu('carregar')
    if file:
        state = load_game(f"saves/{file}")
        if not play_game(state):
            return False
    return True

def render_main_menu() -> None:
    """
    Renderiza o menu principal e executa a ação correspondente.

    Retorno:
    None
    """
    while True:
        choice = show_main_menu()
        if choice == '1':  # Iniciar jogo
            if not start_new_game():
                continue
        elif choice == '2':  # Carregar jogo
            if not load_and_play_game():
                continue
        elif choice == '3':  # Histórico de partidas
            show_game_history()
        elif choice == '4':  # Configurações
            display_message("\nConfigurações: Ainda a implementar...")
        elif choice == '5':  # Ver regras
            show_game_rules()
        elif choice == '6':  # Créditos
            show_credits()
        elif choice == '7':  # Sair
            sys.exit()