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
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    player = state["board"][x][y]

    for dx, dy in directions:
        count = 1

        for step in range(1, 5):
            nx, ny = x + step * dx, y + step * dy
            if 0 <= nx < state['size'] and 0 <= ny < state['size'] and state['board'][nx][ny] == player:
                count += 1
            else:
                break

        for step in range(1, 5):
            nx, ny = x - step * dx, y - step * dy
            if 0 <= nx < state['size'] and 0 <= ny < state['size'] and state['board'][nx][ny] == player:
                count += 1
            else:
                break

        if count >= 5:
            return True

    return False