import sys
from files.file_operations import load_game, save_game
from mechanics.game_initialization import initialize_game
from interface.menus import show_pause_menu, show_file_menu

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