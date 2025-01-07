import sys
from files.log_error import log_error
from interface.file_menu import show_file_menu
from mechanics.initialize_new_game import initialize_new_game
from files.load_game_state import load_game_state
from files.save_game_state import save_game_state
from interface.menus import show_pause_menu
from utils.file_utils import extract_save_name
from mechanics.create_initial_game_state import create_initial_game_state

def handle_pause_menu(state: dict) -> tuple[dict | None, str | None]:
    """
    Lida com a lógica do menu de pausa.

    Parâmetros:
    state (dict) → Estado atual do jogo.

    Retorno:
    tuple[dict | None, str | None] → Novo estado do jogo e nome do arquivo salvo, se aplicável.
    """
    while True:
        option = show_pause_menu()
        result = handle_option(option, state)
        if option == '5':  # Voltar ao menu principal
            return None, None
        if result is not None:
            return result

def handle_option(option: str, state: dict) -> tuple[dict | None, str | None] | None:
    """
    Lida com a opção selecionada no menu de pausa.

    Parâmetros:
    option (str) → Opção selecionada pelo usuário.
    state (dict) → Estado atual do jogo.

    Retorno:
    tuple[dict | None, str | None] | None → Novo estado do jogo e nome do arquivo salvo, 
                                            ou None se o usuário optar por sair ou voltar ao menu principal.
    """
    if option == '1':
        return create_initial_game_state(state['size'], state['mode'], state['player1_name'], state['player2_name']), None  # Iniciar um novo jogo
    elif option == '2':
        return load_game_state_action()  # Carregar um jogo salvo
    elif option == '3':
        return save_game_state_action(state)  # Salvar o estado atual do jogo
    elif option == '4':
        return state, state['save_name']  # Voltar ao jogo
    elif option == '5':
        return None, None  # Voltar ao menu principal
    elif option == '6':
        sys.exit()  # Sair do jogo
    else:
        print("Opção inválida. Tente novamente.") 
        return None  # Retornar None para continuar no menu de pausa

def load_game_state_action() -> tuple[dict | None, str | None] | None:
    """
    Lida com a ação de carregar o estado do jogo a partir de um arquivo.

    Retorno:
    tuple[dict | None, str | None] | None → Novo estado do jogo e nome do arquivo salvo, 
                                            ou None se o usuário optar por voltar.
    """
    file = show_file_menu('carregar') # Exibe o menu de arquivos para carregar
    if file and file != '0': # Verifica se um arquivo foi selecionado e não é '0'
        new_state = load_game_state(f"saves/{file}") # Carrega o estado do jogo a partir do arquivo selecionado
        if new_state: # Verifica se o estado do jogo foi carregado com sucesso
            return new_state, extract_save_name(file)
    return None  # Voltar ao menu de pausa se '0' for selecionado

def save_game_state_action(state: dict) -> tuple[dict, str] | None:
    """
    Lida com a ação de salvar o estado do jogo em um arquivo.

    Parâmetros:
    state (dict) → Estado atual do jogo.

    Retorno:
    tuple[dict, str] → Estado do jogo atualizado e nome do arquivo salvo.
    """
    file = show_file_menu('salvar') # Exibe o menu de arquivos para salvar
    if file: # Verifica se um arquivo foi selecionado e não é '0'
        save_game_state(state, f"saves/{file}") # Salva o estado do jogo no arquivo selecionado
        state['save_name'] = extract_save_name(file) # Atualiza o nome do arquivo salvo no estado do jogo
        return state, state['save_name'] # Retorna o estado do jogo atualizado e o nome do arquivo salvo
    return None  # Voltar ao menu de pausa se '0' for selecionado
