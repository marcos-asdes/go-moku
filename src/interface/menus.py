def show_main_menu() -> str:
    """
    Mostra o menu principal e retorna a opção escolhida.

    Retorno:
    str → Opção escolhida pelo usuário.
    """
    print("\nMenu principal:")
    print("1. Iniciar jogo")
    print("2. Carregar jogo")
    print("3. Histórico de partidas")
    print("4. Configurações")
    print("5. Ver regras")
    print("6. Créditos")
    print("7. Sair")
    return input("Escolha uma opção: ")

def show_pause_menu() -> str:
    """
    Mostra o menu de pausa e retorna a opção escolhida.

    Retorno:
    str → Opção escolhida pelo usuário.
    """
    print("\nMenu de pausa:")
    print("1. Iniciar novo jogo")
    print("2. Carregar partida")
    print("3. Salvar partida")
    print("4. Voltar ao jogo")
    print("5. Voltar ao menu principal")
    print("6. Sair")
    return input("Escolha uma opção: ")

def show_game_rules() -> None:
    """
    Mostra as regras do jogo.

    Retorno:
    None
    """
    print("\nRegras do Jogo:")
    print("1. O objetivo é alinhar 5 peças em linha (horizontal, vertical ou diagonal).")
    print("2. O jogo termina quando um jogador alinha 5 peças ou o tabuleiro está cheio.")

def show_credits() -> None:
    """
    Mostra informações sobre o autor e o jogo.

    Retorno:
    None
    """
    print("\nCréditos:")
    print("Autor: Marcos Antonio")
    print("LinkedIn: https://www.linkedin.com/in/marcos-asdes/")
    print("Versão: 2.0")
    print("Futuras melhorias: Implementar interface gráfica.")