from files.logging import log_history, log_error
from interface.display import display_message, print_board
from mechanics.user_input import handle_user_input
from game.menu_management import handle_pause_menu

def play_game(state: dict) -> bool:
    """
    Executa o loop principal do jogo.

    Parâmetros:
    state (dict) → Estado atual do jogo.

    Retorno:
    bool → True se o jogo terminar normalmente, False se o jogador optar por voltar ao menu principal.
    """
    size = state['size']
    while state["winner"] is None and state["moves"] < size * size:
        try:
            display_message("\n")
            print_board(state)
            display_message(f"Turno de {state['turn']}.")
            display_message("Pressione 'P' para pausar ou insira sua jogada (linha e coluna):")

            user_input = input("> ").strip()

            if user_input.lower() == 'p':  # Caso o jogador pressione 'P'
                new_state = handle_pause_menu(state)
                if new_state is None:
                    return False  # Voltar ao menu principal
                state = new_state
                continue

            valid_move, state = handle_user_input(state, user_input)
            if not valid_move:
                continue
        except Exception as e:
            log_error(str(e))
            display_message("Ocorreu um erro durante o jogo. Verifique o arquivo de log para mais detalhes.")
            return False
    
    print_board(state)
    if state["winner"]:
        display_message(f"Jogador {state['winner']} venceu!")
    else:
        display_message("Isso é um empate!")

    # Registrar o histórico da partida
    log_history(state)
    return True