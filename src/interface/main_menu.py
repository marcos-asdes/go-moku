import sys
from interface.menus import show_credits, show_game_rules, show_main_menu
from interface.game_history import show_game_history
from interface.file_menu import show_file_menu
from mechanics.initialize_new_game import initialize_new_game
from files.log_error import log_error
from files.load_saved_game import load_saved_game
from mechanics.game_flow import play_game

def main_menu() -> None:
    """
    Renderiza o menu principal e executa a ação correspondente.

    Retorno:
    None
    """
    try:
        while True:
            choice = show_main_menu()
            actions = {
                '1': initialize_new_game,
                '2': lambda: play_game(load_saved_game(show_file_menu('carregar'))),
                '3': show_game_history,
                '4': lambda: print("\nConfigurações: Ainda a implementar..."),
                '5': show_game_rules,
                '6': show_credits,
                '7': sys.exit
            }
            action = actions.get(choice)
            if action:
                if not action():
                    continue
            else:
                print("Opção inválida. Tente novamente.")
    except Exception as e:
        print("Erro ao executar o menu principal. Verifique o arquivo de log para mais detalhes.")
        log_error(f"Erro ao executar o menu principal: {str(e)}")