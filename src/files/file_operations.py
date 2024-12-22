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
    # Garantir que a pasta 'saves' exista
    ensure_directory_exists('saves')
    with open(filename, "w") as file:
        file.write(f"size:{state['size']}\n")
        file.write(f"turn:{state['turn']}\n")
        file.write(f"winner:{state['winner']}\n")
        file.write(f"moves:{state['moves']}\n")
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
        board = [list(line.strip()) for line in lines[4:]]
        return {
            "size": size,
            "board": board,
            "turn": turn,
            "winner": winner,
            "moves": moves
        }