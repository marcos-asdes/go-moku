from utils import get_timestamp

def log_error(error_message: str, filename: str = "gomoku_errors.log") -> None:
    """
    Registra erros em um arquivo.

    Parâmetros:
    error_message (str) → Mensagem de erro a ser registrada.
    filename (str) → Nome do arquivo onde o erro será registrado.

    Retorno:
    None
    """
    timestamp = get_timestamp()
    with open(filename, "a") as file:
        file.write(f"{timestamp}: {error_message}\n")

def log_history(state: dict) -> None:
    """
    Registra o histórico de uma partida no arquivo history.txt.

    Parâmetros:
    state (dict) → Estado atual do jogo.

    Retorno:
    None
    """
    timestamp = get_timestamp()
    with open('saves/history.txt', 'a') as file:
        if state['winner']:
            file.write(f"{timestamp} - Vencedor: {state['winner']} - Movimentos: {state['moves']}\n")
        else:
            file.write(f"{timestamp} - Empate - Movimentos: {state['moves']}\n")