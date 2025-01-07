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
            # Exibe o menu principal e obtém a escolha do usuário
            choice = show_main_menu()
            
            # Dicionário de ações associadas a cada escolha do menu
            actions = {
                '1': lambda: play_game(initialize_new_game()),  # Iniciar um novo jogo
                '2': lambda: load_and_play_game(),  # Carregar um jogo salvo
                '3': show_game_history,  # Mostrar histórico de partidas
                '4': lambda: print("\nConfigurações: Ainda a implementar..."),  # Mostrar configurações (ainda não implementado)
                '5': show_game_rules,  # Mostrar regras do jogo
                '6': show_credits,  # Mostrar créditos do jogo
                '7': sys.exit  # Sair do jogo
            }
            
            # Obtém a ação correspondente à escolha do usuário
            action = actions.get(choice)
            
            # Se a ação existir
            if action:
                # Executa a ação e verifica seu retorno
                if not action():
                    # Se a ação retornar False, continua para a próxima iteração do loop
                    continue
            else:
                # Se a escolha do usuário não for válida, exibe uma mensagem de erro
                print("Opção inválida. Tente novamente.")
    except Exception as e:
        print("Erro ao executar o menu principal. Verifique o arquivo de log para mais detalhes.")
        log_error(f"Erro ao executar o menu principal: {str(e)}")

def load_and_play_game() -> bool:
    """
    Carrega um jogo salvo e inicia o jogo.

    Retorno:
    bool → True se o jogo foi carregado e iniciado corretamente, False se o usuário optar por voltar ao menu principal.
    """
    file = show_file_menu('carregar')
    if file is None:
        return False  # Voltar ao menu principal se '0' for selecionado
    state = load_saved_game(file)
    if state:
        play_game(state)
        return True
    return False  # Voltar ao menu principal se ocorrer um erro