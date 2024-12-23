import pytest
from unittest.mock import patch
from src.files.auto_save_game import auto_save_game

@patch('src.files.auto_save_game.save_game_state')
@patch('src.files.auto_save_game.log_error')
def test_auto_save_game_with_save_name(mock_log_error, mock_save_game_state):
    state = {
        'moves': 10,
        'save_name': 'test_game'
    }
    auto_save_game(state)
    mock_save_game_state.assert_called_once_with(state, 'saves/test_game-automatic_save-turn_10.save')
    mock_log_error.assert_not_called()

@patch('src.files.auto_save_game.save_game_state')
@patch('src.files.auto_save_game.log_error')
def test_auto_save_game_without_save_name(mock_log_error, mock_save_game_state):
    state = {
        'moves': 5
    }
    auto_save_game(state)
    mock_save_game_state.assert_called_once_with(state, 'saves/automatic_save-turn_5.save')
    mock_log_error.assert_not_called()

@patch('src.files.auto_save_game.save_game_state', side_effect=Exception('Test Exception'))
@patch('src.files.auto_save_game.log_error')
def test_auto_save_game_exception(mock_log_error, mock_save_game_state):
    state = {
        'moves': 3
    }
    auto_save_game(state)
    mock_save_game_state.assert_called_once()
    mock_log_error.assert_called_once_with('Erro ao salvar o jogo: Test Exception')

if __name__ == "__main__":
    pytest.main()