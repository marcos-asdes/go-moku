from files.log_error import log_error
from mechanics.create_initial_game_state import create_initial_game_state
from utils.constants import BOARD_SIZE

def initialize_new_game() -> dict | None:
    """
    Inicializa um novo jogo com o modo e nomes dos jogadores fornecidos.

    Retorno:
    dict → Estado inicial do jogo se o jogo iniciar corretamente, None caso contrário.
    """
    try:
        while True:
            mode = input("Selecione o modo de jogo (1: Um jogador, 2: Dois jogadores): ").strip()
            if mode not in ['1', '2']:
                print("Opção inválida. Tente novamente.")
                continue

            player1_name = input("Digite o nome do jogador 1: ").strip()
            player2_name = input("Digite o nome do jogador 2: ").strip() if mode == '2' else None
            state = create_initial_game_state(BOARD_SIZE, mode, player1_name, player2_name)
            return state
    except Exception as e:
        log_error(f"Erro ao iniciar o jogo: {str(e)}")
        print("Ocorreu um erro ao iniciar o jogo. Verifique o arquivo de log para mais detalhes.")
        return None