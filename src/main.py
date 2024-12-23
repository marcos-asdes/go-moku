import argparse
from files.load_game_state import load_game_state
from interface.main_menu import main_menu
from mechanics.initialize_new_game import initialize_new_game
from utils.file_utils import ensure_directory_exists, extract_save_name
from mechanics.game_flow import play_game

def parse_arguments() -> argparse.Namespace:
    """
    Analisa os argumentos da linha de comando.

    Retorno:
    argparse.Namespace: Os argumentos analisados.
    """
    parser = argparse.ArgumentParser(description="Jogo Go-moku")
    parser.add_argument('--new-game', action='store_true', help="Iniciar um novo jogo imediatamente")
    parser.add_argument('--load-game', type=str, help="Carregar um jogo a partir de um arquivo especificado")
    parser.add_argument('--show-history', action='store_true', help="Mostrar histórico de partidas")
    parser.add_argument('--show-rules', action='store_true', help="Mostrar regras do jogo")
    parser.add_argument('--show-credits', action='store_true', help="Mostrar créditos do jogo")
    return parser.parse_args()

def main() -> None:
    """
    Função principal que executa o menu inicial e o loop do jogo.

    Retorno:
    None
    """
    args = parse_arguments()

    if args.new_game:
        initialize_new_game()
        return

    if args.load_game:
        ensure_directory_exists('saves')
        state = load_game_state(f"saves/{args.load_game}")
        if state:
            state['save_name'] = extract_save_name(args.load_game)
            play_game(state)
        return

    if args.show_history:
        from interface.game_history import show_game_history
        show_game_history()
        return

    if args.show_rules:
        from interface.menus import show_game_rules
        show_game_rules()
        return

    if args.show_credits:
        from interface.menus import show_credits
        show_credits()
        return

    main_menu()

if __name__ == "__main__":
    main()