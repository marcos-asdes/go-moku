from files.log_error import log_error

def count_consecutive(state: dict, x: int, y: int, dx: int, dy: int, player: int) -> int:
    """
    Conta o número de peças consecutivas de um jogador em uma direção específica.

    Parâmetros:
    state (dict) → Estado atual do jogo.
    x (int) → Coordenada x da posição inicial.
    y (int) → Coordenada y da posição inicial.
    dx (int) → Direção x do movimento.
    dy (int) → Direção y do movimento.
    player (int) → Jogador (1 ou 2).

    Retorno:
    int → Número de peças consecutivas do jogador na direção especificada.
    """
    try:
        count = 0
        for step in range(1, 5):
            nx, ny = x + step * dx, y + step * dy
            if 0 <= nx < state['size'] and 0 <= ny < state['size'] and state['board'][nx][ny] == player:
                count += 1
            else:
                break
        return count
    except Exception as e:
        print("Erro ao contar peças consecutivas. Verifique o arquivo de log para mais detalhes.")
        log_error(f"Erro ao contar peças consecutivas: {str(e)}")
        return 0

def is_winner(state: dict, x: int, y: int) -> bool:
    """
    Verifica se a última jogada resultou em uma vitória.

    Parâmetros:
    state (dict) → Estado atual do jogo.
    x (int) → Coordenada x da última jogada.
    y (int) → Coordenada y da última jogada.

    Retorno:
    bool → True se a jogada resultou em uma vitória, False caso contrário.
    """
    try:
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        player = state["board"][x][y]

        for dx, dy in directions:
            count = 1
            count += count_consecutive(state, x, y, dx, dy, player)
            count += count_consecutive(state, x, y, -dx, -dy, player)

            if count >= 5:
                return True

        return False
    except Exception as e:
        print("Erro ao verificar vitória. Verifique o arquivo de log para mais detalhes.")
        log_error(f"Erro ao verificar vitória: {str(e)}")
        return False