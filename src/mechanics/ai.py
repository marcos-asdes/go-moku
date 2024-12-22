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

    best_move = get_best_move(state, size, board, player, opponent)
    if best_move != (-1, -1) and board[best_move[0] - 1][best_move[1] - 1] == '.':
        return best_move

    return get_random_move(size, board)

def get_best_move(state: dict, size: int, board: list, player: str, opponent: str) -> tuple[int, int]:
    """
    Encontra o melhor movimento possível para o jogador atual.

    Parâmetros:
    state (dict) → Estado atual do jogo.
    size (int) → Tamanho do tabuleiro.
    board (list) → Representação do tabuleiro do jogo.
    player (str) → Jogador atual ('X' ou 'O').
    opponent (str) → Oponente do jogador atual ('X' ou 'O').

    Retorno:
    tuple[int, int] → Coordenadas (x, y) do melhor movimento encontrado.
    """
    best_score = -1
    best_move = (-1, -1)

    for x in range(size):
        for y in range(size):
            if board[x][y] == '.':
                player_score, opponent_score = evaluate_all_moves(state, x, y, player, opponent)
                total_score = player_score + opponent_score
                if total_score > best_score:
                    best_score = total_score
                    best_move = (x + 1, y + 1)
    return best_move

def evaluate_all_moves(state: dict, x: int, y: int, player: str, opponent: str) -> tuple[int, int]:
    """
    Avalia os movimentos para o jogador atual e o oponente.

    Parâmetros:
    state (dict) → Estado atual do jogo.
    x (int) → Coordenada x do movimento.
    y (int) → Coordenada y do movimento.
    player (str) → Jogador atual ('X' ou 'O').
    opponent (str) → Oponente do jogador atual ('X' ou 'O').

    Retorno:
    tuple[int, int] → Pontuações dos movimentos para o jogador atual e o oponente.
    """
    player_score = evaluate_single_move(state, x, y, player)
    opponent_score = evaluate_single_move(state, x, y, opponent)
    return player_score, opponent_score

def evaluate_single_move(state: dict, x: int, y: int, player: str) -> float:
    """
    Avalia um único movimento para o jogador atual.

    Parâmetros:
    state (dict) → Estado atual do jogo.
    x (int) → Coordenada x do movimento.
    y (int) → Coordenada y do movimento.
    player (str) → Jogador atual ('X' ou 'O').

    Retorno:
    float → Pontuação do movimento. Retorna float('inf') se o movimento resultar em vitória.
    """
    board = state['board']
    board[x][y] = player
    if is_winner(state, x, y):
        board[x][y] = '.'
        return float('inf')
    score = calculate_move_score(state, x, y, player)
    board[x][y] = '.'
    return score

def get_random_move(size: int, board: list) -> tuple[int, int]:
    """
    Encontra um movimento aleatório no tabuleiro.

    Parâmetros:
    size (int) → Tamanho do tabuleiro.
    board (list) → Representação do tabuleiro do jogo.

    Retorno:
    tuple[int, int] → Coordenadas (x, y) de um movimento aleatório encontrado.
    """
    for x in range(size):
        for y in range(size):
            if board[x][y] == '.':
                return x + 1, y + 1
    return 1, 1

def calculate_move_score(state: dict, x: int, y: int, player: str) -> int:
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