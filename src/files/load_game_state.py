def load_game_state(filename: str = "gomoku_save.txt") -> dict:
    """
    Carrega o estado do jogo a partir de um arquivo.

    Parâmetros:
    filename (str) → Nome do arquivo de onde o estado do jogo será carregado.

    Retorno:
    dict → Estado do jogo carregado do arquivo.
    """
    with open(filename, "r") as file:
        lines = file.readlines()
        size = int(lines[0].split(":")[1].strip())
        turn = lines[1].split(":")[1].strip()
        winner = lines[2].split(":")[1].strip()
        winner = None if winner == "None" else winner
        moves = int(lines[3].split(":")[1].strip())
        mode = lines[4].split(":")[1].strip()
        player1_name = lines[5].split(":")[1].strip()
        player2_name = lines[6].split(":")[1].strip()
        save_name = lines[7].split(":")[1].strip()
        save_name = None if save_name == "None" else save_name
        board = [list(line.strip()) for line in lines[8:]]
        return {
            "size": size,
            "turn": turn,
            "winner": winner,
            "moves": moves,
            "mode": mode,
            "player1_name": player1_name,
            "player2_name": player2_name,
            "save_name": save_name,
            "board": board
        }