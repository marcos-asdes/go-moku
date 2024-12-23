from files.log_error import log_error

def print_board(state: dict) -> None:
    """
    Imprime o estado atual do tabuleiro com o alinhamento adequado.

    Parâmetros:
    state (dict) → Estado atual do jogo.

    Retorno:
    None
    """
    try:
        size = state['size']
        # Imprime os cabeçalhos das colunas com o alinhamento adequado
        col_headers = "   " + " ".join([f"{i+1:2}" for i in range(size)])
        print(col_headers)
        
        # Imprime cada linha com o índice da linha
        for i, row in enumerate(state['board']):
            row_str = f"{i+1:2}  " + "  ".join(row)
            print(row_str)
    except Exception as e:
        print("Erro ao imprimir o tabuleiro. Verifique o arquivo de log para mais detalhes.")
        log_error(f"Erro ao imprimir o tabuleiro: {str(e)}")