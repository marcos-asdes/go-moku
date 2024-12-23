from files.log_error import log_error
from files.log_history import log_history
from interface.print_board import print_board
from interface.pause_menu import handle_pause_menu
from mechanics.ai import ai_move
from mechanics.move_processing import process_user_move

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
            display_turn(state)
            if state['mode'] == '1' and state['turn'] == 'O':  # Modo um jogador e turno da IA
                if not process_ai_move(state):
                    continue
            else:
                if not process_player_move(state):
                    continue
        except Exception as e:
            log_error(f"Erro na execução do jogo: {str(e)}")
            print("Ocorreu um erro durante o jogo. Verifique o arquivo de log para mais detalhes.")
            return False
    
    handle_game_end(state)
    return True

def display_turn(state: dict) -> None:
    """
    Exibe o turno atual do jogo.

    Parâmetros:
    state (dict) → Estado atual do jogo.

    Retorno:
    None
    """
    try:
        print("\n")
        print_board(state)
        current_player_name = state['player1_name'] if state['turn'] == 'X' else state['player2_name']
        print(f"Turno de {current_player_name} - peça {state['turn']}.")
        print("Pressione 'P' para pausar ou insira sua jogada (linha e coluna):")
    except Exception as e:
        print("Erro ao exibir o turno. Verifique o arquivo de log para mais detalhes.")
        log_error(f"Erro ao exibir o turno: {str(e)}")

def process_ai_move(state: dict) -> bool:
    """
    Processa a jogada da IA.

    Parâmetros:
    state (dict) → Estado atual do jogo.

    Retorno:
    bool → True se a jogada foi processada corretamente, False caso contrário.
    """
    try:
        x, y = ai_move(state)
        print(f"IA jogou em: {x} {y}")
        valid_move, state = process_user_move(state, f"{x} {y}")
        return valid_move
    except Exception as e:
        print("Erro ao processar a jogada da IA. Verifique o arquivo de log para mais detalhes.")
        log_error(f"Erro ao processar a jogada da IA: {str(e)}")
        return False

def process_player_move(state: dict) -> bool:
    """
    Processa a jogada do jogador.

    Parâmetros:
    state (dict) → Estado atual do jogo.

    Retorno:
    bool → True se a jogada foi processada corretamente, False caso contrário.
    """
    try:
        user_input = input("> ").strip()
        if user_input.lower() == 'p':  # Caso o jogador pressione 'P'
            new_state, new_save_name = handle_pause_menu(state)
            if new_state is None:
                return False  # Voltar ao menu principal
            state.update(new_state)
            state['save_name'] = new_save_name
            return True

        valid_move, state = process_user_move(state, user_input)
        return valid_move
    except Exception as e:
        print("Erro ao processar a jogada do jogador. Verifique o arquivo de log para mais detalhes.")
        log_error(f"Erro ao processar a jogada do jogador: {str(e)}")
        return False

def handle_game_end(state: dict) -> None:
    """
    Lida com o fim do jogo, exibindo a mensagem apropriada e registrando o histórico.

    Parâmetros:
    state (dict) → Estado atual do jogo.

    Retorno:
    None
    """
    try:
        print_board(state)
        if state["winner"]:
            if state['mode'] == '1' and state['winner'] == 'O':
                winner_name = "IA"
            else:
                winner_name = state['player1_name'] if state['winner'] == 'X' else state['player2_name']
            print(f"{winner_name} venceu!")
        else:
            print("Isso é um empate!")

        # Registrar o histórico da partida
        log_history(state)
    except Exception as e:
        print("Erro ao lidar com o fim do jogo. Verifique o arquivo de log para mais detalhes.")
        log_error(f"Erro ao lidar com o fim do jogo: {str(e)}")