from files.log_error import log_error
from mechanics.game_flow import play_game
from mechanics.create_initial_game_state import create_initial_game_state
from utils.constants import BOARD_SIZE

def initialize_new_game() -> bool:
    """
    Inicializa um novo jogo com o modo e nomes dos jogadores fornecidos.

    Retorno:
    bool → True se o jogo iniciar corretamente, False caso contrário.
    """
    try:
        mode = input("Selecione o modo de jogo (1: Um jogador, 2: Dois jogadores): ").strip()
        if mode == '1' or mode == '2':
            player1_name = input("Digite o nome do jogador 1: ").strip()
            player2_name = None
            if mode == '2':
                player2_name = input("Digite o nome do jogador 2: ").strip()
            state = create_initial_game_state(BOARD_SIZE, mode, player1_name, player2_name)
            return play_game(state)
        else:
            log_error(f"Erro ao processar entrada: {str(mode)}")
            print("Opção inválida. Tente novamente.")
            return False
    except Exception as e:
        log_error(f"Erro ao iniciar o jogo: {str(e)}")
        print("Ocorreu um erro ao iniciar o jogo. Verifique o arquivo de log para mais detalhes.")
        return False