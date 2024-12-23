from files.logging import log_error, log_history
from interface.display import display_message, print_board
from interface.pause_menu import handle_pause_menu
from mechanics.ai import ai_move
from mechanics.user_input import handle_user_input

def play_game(state: dict, custom_save_name: str = None) -> bool:
    """
    Executa o loop principal do jogo.

    Parâmetros:
    state (dict) → Estado atual do jogo.
    custom_save_name (str) → Nome personalizado do arquivo de save, se houver.

    Retorno:
    bool → True se o jogo terminar normalmente, False se o jogador optar por voltar ao menu principal.
    """
    size = state['size']
    while state["winner"] is None and state["moves"] < size * size:
        try:
            display_message("\n")
            print_board(state)
            current_player_name = state['player1_name'] if state['turn'] == 'X' else state['player2_name']
            display_message(f"Turno de {current_player_name} - peça {state['turn']}.")
            display_message("Pressione 'P' para pausar ou insira sua jogada (linha e coluna):")

            if state['mode'] == '1' and state['turn'] == 'O':  # Modo um jogador e turno da IA
                x, y = ai_move(state)
                display_message(f"IA jogou em: {x} {y}")
                valid_move, state = handle_user_input(state, f"{x} {y}", custom_save_name)
            else:
                user_input = input("> ").strip()
                if user_input.lower() == 'p':  # Caso o jogador pressione 'P'
                    new_state, new_custom_save_name = handle_pause_menu(state, custom_save_name)
                    if new_state is None:
                        return False  # Voltar ao menu principal
                    state = new_state
                    custom_save_name = new_custom_save_name
                    continue

                valid_move, state = handle_user_input(state, user_input, custom_save_name)
                if not valid_move:
                    continue
        except Exception as e:
            log_error(str(e))
            display_message("Ocorreu um erro durante o jogo. Verifique o arquivo de log para mais detalhes.")
            return False
    
    print_board(state)
    if state["winner"]:
        winner_name = state['player1_name'] if state['winner'] == 'X' else state['player2_name']
        display_message(f"{winner_name} venceu!")
    else:
        display_message("Isso é um empate!")

    # Registrar o histórico da partida
    log_history(state)
    return True