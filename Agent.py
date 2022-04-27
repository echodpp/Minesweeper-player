from Environment import *
from copy import deepcopy
import random
import queue
from itertools import combinations

class Agent(object):
    def __init__(self, env, num_of_mine):
        self.env = env
        self.score = 0
        self.kb = [[9 for col in range(self.env.dim)] for row in range(self.env.dim)]
        self.num_cell_left = self.env.dim * self.env.dim
        self.identified_hidden_cell = []
        self.num_of_mine = num_of_mine

    def inference(self):
        if self.num_cell_left > 0:
            if len(self.identified_hidden_cell):
                (x, y) = self.identified_hidden_cell.pop()
                mine_num = self.kb[x][y]
                reveal_mine_num = 0
                reveal_safe_num = 0
                hidden_num = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if (
                            0 <= x + i <= self.env.dim - 1
                            and 0 <= y + j <= self.env.dim - 1
                            and (i != 0 or j != 0)
                        ):
                            if self.kb[x + i][y + j] == -1:
                                reveal_mine_num += 1
                            elif self.kb[x + i][y + j] == 9:
                                hidden_num += 1
                            else:
                                reveal_safe_num += 1
                if mine_num - reveal_mine_num == hidden_num:
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if (
                                0 <= x + i <= self.env.dim - 1
                                and 0 <= y + j <= self.env.dim - 1
                                and self.kb[x + i][y + j] == 9
                            ):
                                self.kb[x + i][y + j] = -1
                                print(x + i, y + j)
                                self.env.mark_mine((x + i, y + j))
                                self.score += 1
                                self.num_cell_left -= 1

                elif (8 - mine_num) - reveal_safe_num == hidden_num:
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if (
                                0 <= x + i <= self.env.dim - 1
                                and 0 <= y + j <= self.env.dim - 1
                                and self.kb[x + i][y + j] == 9
                            ):
                                self.kb[x + i][y + j] = self.env.respond_query(
                                    x + i, y + j
                                )
                                self.identified_hidden_cell.append(
                                    deepcopy((x + i, y + j))
                                )
                                self.num_cell_left -= 1
            else:
                # Randomly pick x and y
                uncover_nodes_list = []
                for i in range(self.env.dim):
                    for j in range(self.env.dim):
                        if self.kb[i][j] == 9:
                            uncover_nodes_list.append((i, j))
                k = random.randint(0, len(uncover_nodes_list) - 1)
                (x, y) = uncover_nodes_list[k]
                if self.env.respond_query(x, y) is False:
                    self.kb[x][y] = -1
                else:
                    self.kb[x][y] = self.env.respond_query(x, y)
                    self.identified_hidden_cell.append(deepcopy((x, y)))
                self.num_cell_left -= 1

        return self.score

    def reset_agent(self, env):
        self.env = env
        self.score = 0
        self.kb = [[9 for col in range(self.env.dim)] for row in range(self.env.dim)]
