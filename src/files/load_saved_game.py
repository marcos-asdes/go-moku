from files import load_game_state, log_error
from utils.file_utils import ensure_directory_exists, extract_save_name

def load_saved_game(file_name: str) -> dict | None:
    """
    Carrega um jogo salvo.

    Parâmetros:
    file_name (str) → Nome do arquivo a ser carregado.

    Retorno:
    dict | None → Estado do jogo carregado ou None se houver erro.
    """
    try:
        # Garantir que a pasta 'saves' exista
        ensure_directory_exists('saves')

        state = load_game_state(f"saves/{file_name}")
        if not state:
            return None  # Se o estado não foi carregado corretamente, retornar None
        save_name = extract_save_name(file_name)
        state['save_name'] = save_name
        return state
    except Exception as e:
        print("Erro inesperado ao carregar o jogo salvo. Verifique o arquivo de log para mais detalhes.")
        log_error(f"Erro inesperado ao carregar o jogo salvo: {str(e)}")
        return