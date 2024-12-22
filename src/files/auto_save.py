from files.file_operations import save_game
from files.logging import log_error
from interface.display import display_message

def auto_save_game(state: dict, custom_save_name: str = None) -> None:
    """
    Salva automaticamente o estado do jogo.

    Parâmetros:
    state (dict) → Estado atual do jogo.
    custom_save_name (str) → Nome personalizado do arquivo de save, se houver.
    """
    try:
        moves = state['moves']
        if custom_save_name:
            auto_save_filename = f"saves/{custom_save_name}-automatic_save-turn_{moves}.save"
        else:
            auto_save_filename = f"saves/automatic_save-turn_{moves}.save"
        save_game(state, auto_save_filename)
    except Exception as e:
        log_error(str(e))
        display_message("Erro ao salvar o jogo. Verifique o arquivo de log para mais detalhes.")