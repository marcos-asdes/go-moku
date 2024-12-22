import sys
from files.file_operations import load_game, save_game
from mechanics.game_initialization import initialize_game
from interface.menus import show_pause_menu, show_file_menu
from utils.file_utils import extract_save_name

def handle_pause_menu(state: dict, custom_save_name: str = None) -> tuple[dict | None, str | None]:
    """
    Gerencia o menu de pausa.

    Parâmetros:
    state (dict) → Estado atual do jogo.
    custom_save_name (str) → Nome personalizado do arquivo de save, se houver.

    Retorno:
    tuple[dict | None, str | None] → Novo estado do jogo após a ação do menu de pausa ou None se for para voltar ao menu principal, e o nome personalizado do arquivo de save.
    """
    while True:
        pause_action = show_pause_menu()
        if pause_action == '1':  # Iniciar novo jogo
            return initialize_game(state['size']), None  # Reset custom_save_name to None
        elif pause_action == '2':  # Carregar partida
            file = show_file_menu('carregar')
            if file:
                return load_game(f"saves/{file}"), extract_save_name(file)
        elif pause_action == '3':  # Salvar partida
            file = show_file_menu('salvar')
            if file:
                save_game(state, f"saves/{file}")
                custom_save_name = extract_save_name(file)  # Atualizar auto save com o novo nome do arquivo de save
        elif pause_action == '4':  # Voltar ao jogo
            return state, custom_save_name
        elif pause_action == '5':  # Voltar ao menu principal
            return None, None
        elif pause_action == '6':  # Sair
            sys.exit()