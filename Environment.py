import re
from tkinter import E
import numpy as np
import random


class Environment(object):
    def __init__(self, d: int, n: int) -> None:
        self.dim = d
        self.mine_num = n
        self.board = [[0 for col in range(d)] for row in range(d)]
        self.hidden_board = [[0 for col in range(d)] for row in range(d)]

        self.ini_board_mine()

    def ini_board_mine(self) -> None:
        for i in range(self.mine_num):
            c = random.randint(0, self.dim - 1)
            r = random.randint(0, self.dim - 1)
            while self.board[c][r] == -1:
                c = random.randint(0, self.dim - 1)
                r = random.randint(0, self.dim - 1)
            self.board[c][r] = -1
            for j in range(-1, 2):
                for k in range(-1, 2):
                    if (
                        0 <= c + j <= self.dim - 1
                        and 0 <= r + k <= self.dim - 1
                        and self.board[c + j][r + k] != -1
                    ):
                        self.board[c + j][r + k] += 1
        for i in range(self.dim):
            print(self.board[i])

    def new_game(self) -> None:
        self.board = [[0 for col in range(self.dim)] for row in range(self.dim)]
        self.hidden_board = [[0 for col in range(self.dim)] for row in range(self.dim)]
        self.ini_board_mine()

    def update_clear_mark(self) -> None:
        for i in range(self.dim):
            for j in range(self.dim):
                if self.hidden_board[i][j] == 2:
                    self.hidden_board[i][j] = 1

    def uncover(self, node: tuple) -> bool:
        (x, y) = node
        self.hidden_board[x][y] = 1

    def mark_mine(self, mine_node: tuple) -> bool:
        (x, y) = mine_node
        self.hidden_board[x][y] = -1

    def respond_query(self, i: int, j: int) -> int:
        if self.board[i][j] == -1:
            self.uncover((i, j))
            return False
        self.uncover((i, j))

        return self.board[i][j]
