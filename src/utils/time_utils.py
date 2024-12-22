import time

def get_timestamp() -> str:
    """
    Retorna o timestamp atual no formato 'YYYY-MM-DD HH:MM:SS'.

    Retorno:
    str → Timestamp atual.
    """
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())