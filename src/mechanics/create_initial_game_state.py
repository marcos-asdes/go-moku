def create_initial_game_state(size: int, mode: str, player1_name: str, player2_name: str = None) -> dict:
    """
    Cria o estado inicial do jogo.

    Parâmetros:
    size (int) → Tamanho do tabuleiro.
    mode (str) → Modo de jogo ('1' para um jogador, '2' para dois jogadores).
    player1_name (str) → Nome do jogador 1.
    player2_name (str) → Nome do jogador 2 (opcional).

    Retorno:
    dict → Estado inicial do jogo.
    """
    return {
        "size": size,
        "board": [["." for _ in range(size)] for _ in range(size)],
        "turn": "X",
        "winner": None,
        "moves": 0,
        "mode": mode,
        "player1_name": player1_name,
        "player2_name": player2_name,
        "save_name": None 
    }