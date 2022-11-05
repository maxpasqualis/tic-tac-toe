import numpy as np

LENGTH = 3
WIDTH = 3

class Board:
    def __init__(self):
        # creates the working board instance
        self.board = np.zeros((LENGTH,WIDTH), dtype=int)

    def check_move_validity(self, x, y):
        # helper function - checks if the specified move can be made
        pass

    def make_move(self, x, y, player):
        # takes in xy coords of desired marker position and a Player instance
        # if valid move, outputs new board with player's marker in specified position
        pass
