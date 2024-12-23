from utils.file_utils import ensure_directory_exists

def save_game_state(state: dict, filename: str = "gomoku_save.txt") -> None:
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
        file.write(f"save_name:{state['save_name']}\n") 
        for row in state['board']:
            file.write("".join(row) + "\n")

