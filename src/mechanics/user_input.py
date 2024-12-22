from files.file_operations import save_game
from files.logging import log_error
from interface.display import display_message
from mechanics.move_processing import make_move

def handle_user_input(state: dict, user_input: str) -> tuple[bool, dict]:
    """
    Processa a entrada do usuário.

    Parâmetros:
    state (dict) → Estado atual do jogo.
    user_input (str) → Entrada do usuário contendo a linha e a coluna.

    Retorno:
    tuple[bool, dict] → Um tuple contendo um booleano indicando se a jogada foi válida e o estado atualizado do jogo.
    """
    size = state['size']
    try:
        x, y = map(int, user_input.split())
        if not (1 <= x <= size and 1 <= y <= size):
            raise ValueError("Jogada fora dos limites.")
    except ValueError as e:
        display_message("Entrada inválida. Insira a linha e a coluna separadas por um espaço.")
        log_error(str(e))
        return False, state

    success, error = make_move(state, x, y)
    if not success:
        display_message(error)
        log_error(error)
        return False, state

    # Salvar automaticamente após cada jogada
    try:
        save_game(state, f"saves/{state['turn']}_{state['moves']}.save")
    except Exception as e:
        log_error(str(e))
        display_message("Erro ao salvar o jogo. Verifique o arquivo de log para mais detalhes.")
    
    return True, state