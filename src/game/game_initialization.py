def initialize_game(size: int) -> dict:
    """
    Inicializa o estado do jogo.

    Parâmetros:
    size (int) → Tamanho do tabuleiro.

    Retorno:
    dict → Estado inicial do jogo.
    """
    return {
        "size": size,
        "board": [["." for _ in range(size)] for _ in range(size)],
        "turn": "X",
        "winner": None,
        "moves": 0
    }