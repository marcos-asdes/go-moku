from utils.file_utils import ensure_directory_exists

def save_game(state: dict, filename: str = "gomoku_save.txt") -> None:
    """
    Salva o estado do jogo em um arquivo.

    Parâmetros:
    state (dict) → Estado atual do jogo.
    filename (str) → Nome do arquivo onde o estado do jogo será salvo.

    Retorno:
    None
    """
    ensure_directory_exists('saves')
    with open(filename, "w") as file:
        file.write(f"size:{state['size']}\n")
        file.write(f"turn:{state['turn']}\n")
        file.write(f"winner:{state['winner']}\n")
        file.write(f"moves:{state['moves']}\n")
        file.write(f"mode:{state['mode']}\n")
        file.write(f"player1_name:{state['player1_name']}\n")
        file.write(f"player2_name:{state['player2_name']}\n")
        for row in state['board']:
            file.write("".join(row) + "\n")

def load_game(filename: str = "gomoku_save.txt") -> dict:
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
        board = [list(line.strip()) for line in lines[7:]]
        return {
            "size": size,
            "board": board,
            "turn": turn,
            "winner": winner,
            "moves": moves,
            "mode": mode,
            "player1_name": player1_name,
            "player2_name": player2_name
        }