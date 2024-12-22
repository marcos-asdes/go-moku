from game.game_logic import is_winner

def make_move(state: dict, x: int, y: int) -> tuple[bool, str | None]:
    """
    Processa a jogada de um jogador.

    Parâmetros:
    state (dict) → Estado atual do jogo.
    x (int) → Coordenada x da jogada.
    y (int) → Coordenada y da jogada.

    Retorno:
    tuple[bool, str | None] → Um tuple indicando se a jogada foi válida e uma mensagem de erro, se houver.
    """
    x, y = x - 1, y - 1
    if state["board"][x][y] != ".":
        return False, "A célula já está ocupada."

    state["board"][x][y] = state["turn"]
    state["moves"] += 1

    if is_winner(state, x, y):
        state["winner"] = state["turn"]
    else:
        state["turn"] = "O" if state["turn"] == "X" else "X"

    return True, None