from utils.time_utils import get_timestamp

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