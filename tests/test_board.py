import pytest
import numpy as np
from tictactoe.classes.board import Board

def test_board_reset_creates_array_of_zeros():
    # Arrange, Act
    b = Board.reset_board()
    # Assert
    assert isinstance(b, np.ndarray)
    assert len(b) == 3
    for i in range(3):
        assert list(b[i]) == [0, 0, 0]