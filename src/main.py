import argparse
import os

from files.load_game_state import load_game_state
from interface.main_menu import main_menu
from interface.game_history import show_game_history
from interface.menus import show_credits, show_game_rules
from mechanics.game_flow import play_game
from mechanics.initialize_new_game import initialize_new_game
from utils.file_utils import ensure_directory_exists, extract_save_name

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

    # Inicia um novo jogo se o argumento new_game for passado
    if args.new_game:
        state = initialize_new_game()
        if state:
            play_game(state)
        return

    # Carrega um jogo salvo se o argumento load_game for passado
    if args.load_game:
        ensure_directory_exists('saves')
        file_path = f"saves/{args.load_game}.save"
        if not os.path.exists(file_path):
            print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
            return
        state = load_game_state(file_path)
        if state:
            state['save_name'] = extract_save_name(args.load_game)
            play_game(state)
        return

    # Mostra o histórico do jogo se o argumento show_history for passado
    if args.show_history:
        show_game_history()
        return

    # Mostra as regras do jogo se o argumento show_rules for passado
    if args.show_rules:
        show_game_rules()
        return

    # Mostra os créditos do jogo se o argumento show_credits for passado
    if args.show_credits:
        show_credits()
        return

    # Exibe o menu principal se nenhum argumento for passado
    main_menu()

if __name__ == "__main__":
    main()