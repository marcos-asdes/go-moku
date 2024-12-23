from files.auto_save_game import auto_save_game
from mechanics.game_logic import is_winner
from files.log_error import log_error

def process_user_move(state: dict, user_input: str) -> tuple[bool, dict]:
    """
    Processa a jogada do usuário.

    Parâmetros:
    state (dict) → Estado atual do jogo.
    user_input (str) → Entrada do usuário contendo a linha e a coluna.

    Retorno:
    tuple[bool, dict] → Um tuple contendo um booleano indicando se a jogada foi válida e o estado atualizado do jogo.
    """
    size = state['size']
    try:
        x, y = map(int, user_input.split())
        if not (1 <= x <= size and 1 <= y <= size):
            raise ValueError("Jogada fora dos limites.")
    except ValueError as e:
        print("Entrada inválida. Insira a linha e a coluna separadas por um espaço.")
        log_error(f"Erro ao processar jogada: {str(e)}")
        return False, state

    success, error = execute_move(state, x, y)
    if not success:
        print(error)
        log_error(f"Erro ao processar jogada: {str(error)}")
        return False, state

    # Salvar automaticamente após cada jogada
    auto_save_game(state)
    
    return True, state

def execute_move(state: dict, x: int, y: int) -> tuple[bool, str | None]:
    """
    Executa a jogada de um jogador.

    Parâmetros:
    state (dict) → Estado atual do jogo.
    x (int) → Coordenada x da jogada.
    y (int) → Coordenada y da jogada.

    Retorno:
    tuple[bool, str | None] → Um tuple indicando se a jogada foi válida e uma mensagem de erro, se houver.
    """
    try:
        x, y = x - 1, y - 1
        if state["board"][x][y] != ".":
            return False, f"A célula {x+1} {y+1} já está ocupada."

        state["board"][x][y] = state["turn"]
        state["moves"] += 1

        if is_winner(state, x, y):
            state["winner"] = state["turn"]
        else:
            state["turn"] = "O" if state["turn"] == "X" else "X"

        return True, None
    except Exception as e:
        log_error(f"Erro ao processar jogada: {str(e)}")
        return False, "Ocorreu um erro ao processar a jogada. Verifique o arquivo de log para mais detalhes."