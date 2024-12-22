import os
from interface.display import display_message
from interface.file_menu import handle_file_menu

def show_main_menu() -> str:
    """
    Mostra o menu principal e retorna a opção escolhida.

    Retorno:
    str → Opção escolhida pelo usuário.
    """
    display_message("\nMenu principal:")
    display_message("1. Iniciar jogo")
    display_message("2. Carregar jogo")
    display_message("3. Histórico de partidas")
    display_message("4. Configurações")
    display_message("5. Ver regras")
    display_message("6. Créditos")
    display_message("7. Sair")
    return input("Escolha uma opção: ")

def show_pause_menu() -> str:
    """
    Mostra o menu de pausa e retorna a opção escolhida.

    Retorno:
    str → Opção escolhida pelo usuário.
    """
    display_message("\nMenu de pausa:")
    display_message("1. Iniciar novo jogo")
    display_message("2. Carregar partida")
    display_message("3. Salvar partida")
    display_message("4. Voltar ao jogo")
    display_message("5. Voltar ao menu principal")
    display_message("6. Sair")
    return input("Escolha uma opção: ")

def show_file_menu(action: str) -> str | None:
    """
    Mostra o menu para salvar ou carregar jogos a partir de arquivos.

    Parâmetros:
    action (str) → Ação a ser realizada ('salvar' ou 'carregar').

    Retorno:
    str | None → Nome do arquivo escolhido ou None se o usuário optar por voltar.
    """
    files = [f for f in os.listdir('saves') if f.endswith('.save')]
    display_message(f"\nMenu de arquivos para {action}:")
    display_message("Arquivos existentes:")
    for i, file in enumerate(files, 1):
        display_message(f"{i}. {file}")
    display_message("0. Voltar")
    return handle_file_menu(action, files)

def show_game_rules() -> None:
    """
    Mostra as regras do jogo.

    Retorno:
    None
    """
    display_message("\nRegras do Jogo:")
    display_message("1. O objetivo é alinhar 5 peças em linha (horizontal, vertical ou diagonal).")
    display_message("2. O jogo termina quando um jogador alinha 5 peças ou o tabuleiro está cheio.")

def show_credits() -> None:
    """
    Mostra informações sobre o autor e o jogo.

    Retorno:
    None
    """
    display_message("\nCréditos:")
    display_message("Autor: Marcos Antonio")
    display_message("LinkedIn: https://www.linkedin.com/in/marcos-asdes/")
    display_message("Versão: 1.0")
    display_message("Futuras melhorias: IA para jogar contra o computador.")