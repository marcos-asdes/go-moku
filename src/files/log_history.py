from files.log_error import log_error
from utils.constants import HISTORY_FILE_PATH
from utils.time_utils import get_timestamp

def log_history(state: dict) -> None:
    """
    Registra o histórico de uma partida no arquivo history.txt.

    Parâmetros:
    state (dict) → Estado atual do jogo.

    Retorno:
    None
    """
    try:
        timestamp = get_timestamp()
        mode = "1 jogador" if state['mode'] == '1' else "2 jogadores"
        player1_name = state['player1_name']
        player2_name = "IA" if state['mode'] == '1' else state['player2_name']
        
        with open(HISTORY_FILE_PATH, 'a') as file:
            if state['winner']:
                if state['mode'] == '1' and state['winner'] == 'O':
                    winner_name = "IA"
                else:
                    winner_name = state['player1_name'] if state['winner'] == 'X' else state['player2_name']
                file.write(f"{timestamp} - Modo: {mode} - {player1_name} x {player2_name} - Vencedor: {winner_name} - Movimentos: {state['moves']}\n")
            else:
                file.write(f"{timestamp} - Modo: {mode} - {player1_name} x {player2_name} - Empate - Movimentos: {state['moves']}\n")
    except Exception as e:
        print("Erro ao registrar o histórico da partida. Verifique o arquivo de log para mais detalhes.")
        log_error(f"Erro ao registrar o histórico da partida: {str(e)}")