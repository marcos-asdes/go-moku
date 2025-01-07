# Go-moku

Projeto de jogo Go-moku em Python para a disciplina de Algoritmos Computacionais da UERJ.

Este jogo não possui interface gráfica e é jogado pelo console do terminal.

## Descrição

Go-moku é um jogo de tabuleiro tradicional onde dois jogadores se alternam colocando peças em um tabuleiro com o objetivo de alinhar cinco peças consecutivas na horizontal, vertical ou diagonal.

## Estrutura do Projeto

```plaintext
.
├── LICENSE
├── README.md
├── saves/
│   ├── history.txt
│   └── ...
└── src/
    ├── files/
    │   ├── auto_save_game.py
    │   ├── load_game_state.py
    │   ├── load_saved_game.py
    │   ├── log_error.py
    │   ├── log_history.py
    │   ├── save_game_state.py
    │   └── __init__.py
    ├── interface/
    │   ├── game_history.py
    │   ├── main_menu.py
    │   ├── menus.py
    │   ├── pause_menu.py
    │   ├── file_menu.py
    │   ├── print_board.py
    │   └── __init__.py
    ├── mechanics/
    │   ├── ai.py
    │   ├── create_initial_game_state.py
    │   ├── game_flow.py
    │   ├── game_logic.py
    │   ├── initialize_new_game.py
    │   ├── move_processing.py
    │   └── __init__.py
    ├── utils/
    │   ├── constants.py
    │   ├── file_utils.py
    │   ├── time_utils.py
    │   └── __init__.py
    └── main.py

```

## Funcionalidades

- **Modo de Jogo**: Um jogador contra IA ou dois jogadores.
- **Salvar e Carregar**: Salva automaticamente o estado do jogo e permite carregar jogos salvos.
- **Histórico de Partidas**: Exibe o histórico de partidas jogadas.
- **Menu de Pausa**: Permite pausar o jogo e acessar opções como salvar, carregar e voltar ao menu principal.

## Instalação

Clone o repositório:

```sh
git clone https://github.com/marcos-asdes/go-moku.git
cd go-moku
```

## Uso

Para iniciar o jogo, execute:

```sh
python src/main.py
```

### Comandos argparse

O jogo suporta os seguintes comandos via linha de comando:

- **Iniciar um novo jogo**:

  ```sh
  python src/main.py --new-game
  ```

- **Carregar um jogo salvo**:

  ```sh
  python src/main.py --load-game <nome_do_jogo>
  ```

- **Mostrar histórico de partidas**:

  ```sh
  python src/main.py --show-history
  ```

- **Mostrar regras do jogo**:

  ```sh
  python src/main.py --show-rules
  ```

- **Mostrar créditos do jogo**:
  ```sh
  python src/main.py --show-credits
  ```

## Estrutura do Código

### Arquivos Principais

- `main.py`: Ponto de entrada do jogo.
- `game_flow.py`: Contém a lógica principal do jogo.
- `create_initial_game_state`: Contém o dicionário (estado) que rege o jogo.
- `main_menu.py`: Implementa o menu principal do jogo.
- `move_processing.py`: Contém a lógica de processamento de movimentos.
- `ai.py`: Contém a lógica de processamento de jogo da IA.
- `save_game_state.py`: Funções para salvar o estado do jogo.
- `load_game_state.py`: Funções para carregar o estado do jogo.

### Utilitários

- `constants.py`: Constantes usadas no jogo.
- `file_utils.py`: Funções auxiliares para manipulação de arquivos.
- `time_utils.py`: Funções auxiliares para manipulação de tempo.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [`LICENSE`](LICENSE) para mais detalhes.

## Autor

Marcos Antonio Silva do Espirito Santo

- [LinkedIn](https://www.linkedin.com/in/marcos-asdes/)
