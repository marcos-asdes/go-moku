import sys
from files.log_error import log_error
from interface.file_menu import show_file_menu
from mechanics.create_initial_game_state import create_initial_game_state
from files.load_game_state import load_game_state
from files.save_game_state import save_game_state
from interface.menus import show_pause_menu
from utils.file_utils import extract_save_name

def handle_pause_menu(state: dict) -> tuple[dict | None, str | None]:
    """
    Gerencia o menu de pausa.

    Parâmetros:
    state (dict) → Estado atual do jogo.

    Retorno:
    tuple[dict | None, str | None] → Novo estado do jogo após a ação do menu de pausa ou None se for para voltar ao menu principal.
    """
    try:
        while True:
            pause_action = show_pause_menu()
            actions = {
                '1': lambda: (create_initial_game_state(state['size'], state['mode'], state['player1_name'], state['player2_name']), None),
                '2': lambda: load_game_state_action(state),
                '3': lambda: save_game_state_action(state),
                '4': lambda: (state, state['save_name']),
                '5': lambda: (None, None),
                '6': sys.exit
            }
            action = actions.get(pause_action)
            if action:
                return action()
            else:
                print("Opção inválida. Tente novamente.")
    except Exception as e:
        print("Erro ao gerenciar o menu de pausa. Verifique o arquivo de log para mais detalhes.")
        log_error(f"Erro ao gerenciar o menu de pausa: {str(e)}")
        return None, None

def load_game_state_action(state: dict) -> tuple[dict, str]:
    file = show_file_menu('carregar')
    if file:
        return load_game_state(f"saves/{file}"), extract_save_name(file)
    return state, state['save_name']

def save_game_state_action(state: dict) -> tuple[dict, str]:
    file = show_file_menu('salvar')
    if file:
        save_game_state(state, f"saves/{file}")
        state['save_name'] = extract_save_name(file)
    return state, state['save_name']