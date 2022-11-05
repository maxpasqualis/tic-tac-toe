import pytest
import numpy as np
from tictactoe.classes.board import Board, LENGTH, WIDTH

def test_board_initialization():
    b = Board().board

    assert str(type(b)) == "<class 'numpy.ndarray'>"
    assert len(b) == 3
    for i in range(3):
        assert list(b[i]) == [0, 0, 0]

# @pytest.mark.skip
def test_valid_move_is_true():
    b = Board()
    result = b.check_move_validity(1, 1)
    result2 = b.check_move_validity(0, 2)
    result3 = b.check_move_validity(2, 1)
    
    assert result
    assert result2
    assert result3

# @pytest.mark.skip
def test_valid_and_invalid_moves():
    b = Board()
    b.board = np.array([
        [1, 0, 0],
        [0, 0, 1],
        [0, 1, 0]])
    valid_move1 = b.check_move_validity(0, 1)
    valid_move2 = b.check_move_validity(2, 2)
    invalid_move1 = b.check_move_validity(0, 0)
    invalid_move2 = b.check_move_validity(1, 2)

    assert valid_move1
    assert valid_move2
    assert not invalid_move1
    assert not invalid_move2

@pytest.mark.skip
def test_move_puts_marker_in_empty_space():
    pass

@pytest.mark.skip
def test_invalid_move_returns_same_board():
    pass