from utils.time_utils import get_timestamp
from utils.constants import HISTORY_FILE_PATH

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
    mode = "1 jogador" if state['mode'] == '1' else "2 jogadores"
    player1_name = state['player1_name']
    player2_name = "IA" if state['mode'] == '1' else state['player2_name']
    
    with open(HISTORY_FILE_PATH, 'a') as file:
        if state['winner']:
            winner_name = state['player1_name'] if state['winner'] == 'X' else state['player2_name']
            file.write(f"{timestamp} - Modo: {mode} - {player1_name} x {player2_name} - Vencedor: {winner_name} - Movimentos: {state['moves']}\n")
        else:
            file.write(f"{timestamp} - Modo: {mode} - {player1_name} x {player2_name} - Empate - Movimentos: {state['moves']}\n")