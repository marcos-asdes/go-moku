from files.log_error import log_error
from files.save_game_state import save_game_state

def auto_save_game(state: dict) -> None:
    """
    Salva automaticamente o estado do jogo.

    Parâmetros:
    state (dict) → Estado atual do jogo.
    """
    try:
        moves = state['moves']
        save_name = state.get('save_name')
        if save_name:
            auto_save_filename = f"saves/{save_name}-automatic_save-turn_{moves}.save"
        else:
            auto_save_filename = f"saves/automatic_save-turn_{moves}.save"
        save_game_state(state, auto_save_filename)
    except Exception as e:
        log_error(f"Erro ao salvar o jogo: {str(e)}")
        print("Erro ao salvar o jogo. Verifique o arquivo de log para mais detalhes.")