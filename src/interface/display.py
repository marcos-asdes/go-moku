def print_board(state: dict) -> None:
    """
    Imprime o estado atual do tabuleiro com o alinhamento adequado.

    Parâmetros:
    state (dict) → Estado atual do jogo.

    Retorno:
    None
    """
    size = state['size']
    # Imprime os cabeçalhos das colunas com o alinhamento adequado
    col_headers = "   " + " ".join([f"{i+1:2}" for i in range(size)])
    display_message(col_headers)
    
    # Imprime cada linha com o índice da linha
    for i, row in enumerate(state['board']):
        row_str = f"{i+1:2}  " + "  ".join(row)
        display_message(row_str)

def display_message(message: str) -> None:
    """
    Exibe uma mensagem para o usuário.

    Parâmetros:
    message (str) → Mensagem a ser exibida.

    Retorno:
    None
    """
    print(message)