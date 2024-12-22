from mechanics.game_logic import count_consecutive, is_winner

def ai_move(state: dict) -> tuple[int, int]:
    """
    Decide o próximo movimento da IA.

    Parâmetros:
    state (dict) → Estado atual do jogo.

    Retorno:
    tuple[int, int] → Coordenadas (x, y) do próximo movimento da IA.
    """
    size = state['size']
    board = state['board']
    player = state['turn']
    opponent = 'X' if player == 'O' else 'O'

    best_score = -1
    best_move = (-1, -1)

    for x in range(size):
        for y in range(size):
            if board[x][y] == '.':
                # Avaliar movimento para o jogador
                board[x][y] = player
                if is_winner(state, x, y):
                    board[x][y] = '.'  # Reverter a jogada
                    return x + 1, y + 1
                player_score = evaluate_move(state, x, y, player)
                board[x][y] = '.'

                # Avaliar movimento para o oponente
                board[x][y] = opponent
                if is_winner(state, x, y):
                    board[x][y] = '.'  # Reverter a jogada
                    return x + 1, y + 1
                opponent_score = evaluate_move(state, x, y, opponent)
                board[x][y] = '.'

                # Escolher o movimento com a melhor pontuação
                total_score = player_score + opponent_score
                if total_score > best_score:
                    best_score = total_score
                    best_move = (x + 1, y + 1)

    # Verificar se a célula escolhida está ocupada
    if best_move != (-1, -1) and board[best_move[0] - 1][best_move[1] - 1] == '.':
        return best_move

    # Fazer um movimento aleatório se não houver melhor
    for x in range(size):
        for y in range(size):
            if board[x][y] == '.':
                return x + 1, y + 1

    return 1, 1  # Movimento padrão se não houver melhor

def evaluate_move(state: dict, x: int, y: int, player: str) -> int:
    """
    Avalia a qualidade de um movimento.

    Parâmetros:
    state (dict) → Estado atual do jogo.
    x (int) → Coordenada x do movimento.
    y (int) → Coordenada y do movimento.
    player (str) → Jogador ('X' ou 'O').

    Retorno:
    int → Pontuação do movimento.
    """
    score = 0
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    
    for dx, dy in directions:
        count = 1
        count += count_consecutive(state, x, y, dx, dy, player)
        count += count_consecutive(state, x, y, -dx, -dy, player)
        score += count ** 2  # Aumentar a pontuação exponencialmente para movimentos melhores

    return score