import sys
from interface.menus import show_credits, show_game_rules, show_main_menu
from interface.game_history import show_game_history
from interface.display import display_message
from mechanics.start_and_load import load_and_play_game, start_new_game

def render_main_menu() -> None:
    """
    Renderiza o menu principal e executa a ação correspondente.

    Retorno:
    None
    """
    while True:
        choice = show_main_menu()
        if choice == '1':  # Iniciar jogo
            if not start_new_game():
                continue
        elif choice == '2':  # Carregar jogo
            if not load_and_play_game():
                continue
        elif choice == '3':  # Histórico de partidas
            show_game_history()
        elif choice == '4':  # Configurações
            display_message("\nConfigurações: Ainda a implementar...")
        elif choice == '5':  # Ver regras
            show_game_rules()
        elif choice == '6':  # Créditos
            show_credits()
        elif choice == '7':  # Sair
            sys.exit()