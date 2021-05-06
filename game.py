import random

import pandas as pd
import copy

black, white = [46/250, 64/250, 87/250,1], [246/250, 216/250, 174/250,1]

class Game:

    def __init__(self):
        self.new_game_data()

    def new_game_data(self, *args):
        # rand = random.randint(0,11)
        rand = random.randint(3,11) # for easy ones
        # rand = 11
        data = self.get_start_df(rand)
        self.start_df = pd.DataFrame(data=data)

        data = self.get_solved_df(rand)
        self.solved_df = pd.DataFrame(data=data)

        self.game_df = copy.deepcopy(self.start_df)

    def add_Button(self, i, j, button):
        value = self.game_df[i][j]
        if value > 0:
            button.text = str(value)
            button.disabled = True
        button.board_pos = (i,j)
        button.solved_value = self.solved_df[i][j]

    def get_cube_xy(self, i = None, j = None, n = None):
        x, y = 0, 0
        if not (i is None and j is None):
            if i >= 6:
                x = 6
            elif i >= 3:
                x = 3
            if j >= 6:
                y = 6
            elif j >= 3:
                y = 3
            return x, y
        elif not n is None:
            list = [ [0,0],[1,0],[2,0],[0,1],[1,1],[2,1],[0,2],[1,2],[2,2], #topleft cube
                     [3,0],[4,0],[5,0],[3,1],[4,1],[5,1],[3,2],[4,2],[5,2],
                     [6,0],[7,0],[8,0],[6,1],[7,1],[8,1],[6,2],[7,2],[8,2], #topright cube
                     [0,3],[1,3],[2,3],[0,4],[1,4],[2,4],[0,5],[1,5],[2,5],
                     [3,3],[4,3],[5,3],[3,4],[4,4],[5,4],[3,5],[4,5],[5,5], #middle cube
                     [6,3],[7,3],[8,3],[6,4],[7,4],[8,4],[6,5],[7,5],[8,5],
                     [0,6],[1,6],[2,6],[0,7],[1,7],[2,7],[0,8],[1,8],[2,8], #bottomleft cube
                     [3,6],[4,6],[5,6],[3,7],[4,7],[5,7],[3,8],[4,8],[5,8],
                     [6,6],[7,6],[8,6],[6,7],[7,7],[8,7],[6,8],[7,8],[8,8], #bottomright cube
                     ]
            return list[n][0], list[n][1]
        return None

    def solve(self, i = 0,j = 0):
        if i < 9:
            if j < 0:
                return self.solve(i-1, 8)
            elif j < 9:
                if self.solved_df[i][j] == 0:
                    for value in range(1,10):
                        x, y = self.get_cube_xy(i, j)
                        flag = True
                        for a in range(x, x + 3):
                            for b in range(y, y + 3):
                                if self.solved_df[a][b] == value:
                                    flag = False
                        # first condition for colunm
                        # second condition for row/line
                        if list(self.solved_df[i]).count(value) == 0 and \
                                list(self.solved_df.iloc[j]).count(value) == 0 and \
                                flag:

                            self.solved_df[i][j] = value
                            recurse = self.solve(i, j+1)
                            if not recurse is None:
                                return recurse
                            self.solved_df[i][j] = 0
                    else:
                        return None
                return self.solve(i, j+1)
            return self.solve(i+1, 0)
        return self.solved_df

    def get_start_df(self, num):
        data = [
                    # hard
                    [[7,0,6,0,0,0,0,8,0],
                     [0,0,2,1,0,0,0,0,6],
                     [0,0,0,0,0,0,0,0,7],
                     [0,9,0,0,0,0,3,5,0],
                     [8,0,0,5,0,0,0,0,0],
                     [0,1,0,0,2,0,0,0,0],
                     [0,0,0,2,7,6,0,0,0],
                     [0,0,0,0,0,1,8,0,9],
                     [0,0,0,0,0,8,4,0,0]],
                    # medium
                    [[5,0,3,0,0,7,0,6,0],
                     [1,9,0,0,2,0,0,4,0],
                     [0,0,0,4,0,0,0,0,8],
                     [6,0,0,0,3,0,8,0,0],
                     [0,7,0,5,0,2,0,3,0],
                     [0,2,4,0,1,0,0,0,9],
                     [7,0,0,0,0,9,0,0,0],
                     [0,3,0,0,8,0,0,7,6],
                     [0,5,0,1,0,0,2,0,0]],

                    [[0,0,5,1,0,0,0,7,0],
                     [7,3,4,0,0,8,0,0,1],
                     [0,0,9,7,0,0,0,3,5],
                     [0,2,6,8,0,1,0,4,0],
                     [0,0,0,0,0,0,6,2,0],
                     [4,0,3,0,5,6,1,9,0],
                     [0,6,0,4,2,7,3,1,0],
                     [0,0,0,0,0,3,0,5,0],
                     [3,4,0,9,1,0,0,8,0]],
                    # easy
                    [[3,0,9,0,0,0,4,0,1],
                     [0,0,0,9,0,2,0,7,0],
                     [0,0,2,4,1,7,5,0,0],
                     [0,2,4,0,0,0,1,6,0],
                     [0,0,0,2,0,4,0,0,8],
                     [0,8,5,0,0,0,2,3,0],
                     [0,0,3,6,8,1,7,0,0],
                     [0,0,0,7,0,5,0,0,0],
                     [2,0,7,0,0,0,6,0,5]],

                    [[0,0,8,9,2,0,3,0,0],
                     [9,4,0,0,5,0,0,2,0],
                     [6,0,2,0,0,0,8,0,0],
                     [0,0,0,0,0,8,9,0,3],
                     [5,1,0,3,4,0,6,8,0],
                     [3,8,6,1,0,7,0,0,4],
                     [0,3,0,0,8,0,0,0,0],
                     [8,9,5,0,3,4,0,6,0],
                     [0,0,7,2,0,0,5,3,0]],

                    [[0,0,0,0,0,0,9,8,4],
                     [4,0,0,8,0,0,2,5,0],
                     [0,8,0,0,4,9,0,0,3],
                     [9,0,6,1,5,7,8,0,2],
                     [0,0,0,0,0,0,0,4,0],
                     [0,0,0,0,8,0,1,9,6],
                     [0,3,4,9,2,8,5,6,0],
                     [6,0,2,0,1,5,3,7,0],
                     [0,0,5,0,6,0,0,0,0]],

                    [[0,4,6,1,5,0,0,0,2],
                     [0,0,0,0,0,0,0,7,5],
                     [5,7,0,2,0,0,0,1,6],
                     [3,0,0,6,7,2,8,0,0],
                     [4,0,9,8,3,0,5,2,0],
                     [2,0,0,5,4,0,1,0,0],
                     [0,0,2,0,1,5,0,0,0],
                     [8,1,0,7,6,0,0,4,0],
                     [0,0,4,0,2,0,6,0,0]],

                    [[0,0,0,5,6,0,0,1,9],
                     [9,0,0,0,0,0,6,3,0],
                     [0,0,8,0,0,3,0,0,0],
                     [0,0,9,8,3,0,4,0,0],
                     [5,0,4,7,0,6,0,0,0],
                     [6,0,0,0,0,0,0,0,1],
                     [2,3,0,6,0,9,1,4,8],
                     [8,7,0,0,0,0,0,0,5],
                     [4,9,0,2,8,5,7,6,0]],

                    [[0,0,5,0,0,0,2,1,0],
                     [1,9,6,2,8,4,7,5,3],
                     [0,3,0,1,5,0,4,0,6],
                     [3,0,8,0,0,5,0,0,0],
                     [4,0,0,0,6,3,0,0,0],
                     [5,0,1,9,2,0,3,7,4],
                     [0,0,0,0,0,2,5,0,0],
                     [0,5,0,0,3,0,6,0,0],
                     [0,1,3,0,4,0,0,0,0]],

                    [[0,0,0,0,9,0,0,5,0],
                     [0,8,5,4,0,0,0,0,0],
                     [4,0,6,0,0,0,1,0,8],
                     [0,7,0,0,4,0,9,0,5],
                     [0,0,0,1,7,0,3,8,0],
                     [6,0,0,8,0,0,0,0,0],
                     [1,0,0,9,0,3,0,0,0],
                     [9,6,7,2,0,5,8,4,0],
                     [0,3,8,7,0,4,2,1,9]],

                    [[8,1,7,0,0,0,0,4,5],
                     [0,0,0,0,5,1,7,0,6],
                     [2,6,5,0,0,3,0,0,1],
                     [4,7,0,5,6,8,0,0,0],
                     [9,5,1,0,0,0,0,8,0],
                     [0,3,0,0,9,0,2,0,0],
                     [0,4,0,2,0,0,0,0,0],
                     [0,0,0,0,0,5,0,7,9],
                     [5,8,9,7,3,0,1,6,0]],

                    [[0,9,0,0,0,7,5,2,0],
                     [0,0,6,8,0,0,0,0,0],
                     [0,0,0,3,0,9,1,0,8],
                     [2,8,0,7,0,0,0,0,0],
                     [6,0,7,0,0,0,3,8,0],
                     [0,0,0,0,0,5,0,0,2],
                     [0,0,3,5,1,0,0,0,0],
                     [8,1,0,9,7,0,4,5,3],
                     [9,6,5,4,2,0,8,0,7]]
                ]
        return data[num]

    def get_solved_df(self, num):
        data = [
                    # hard
                    [[7, 3, 6, 4, 9, 2, 1, 8, 5], [4, 5, 2, 1, 8, 7, 9, 3, 6], [1, 8, 9, 6, 3, 5, 2, 4, 7], [2, 9, 7, 8, 6, 4, 3, 5, 1], [8, 6, 3, 5, 1, 9, 7, 2, 4], [5, 1, 4, 7, 2, 3, 6, 9, 8], [9, 4, 8, 2, 7, 6, 5, 1, 3], [6, 2, 5, 3, 4, 1, 8, 7, 9], [3, 7, 1, 9, 5, 8, 4, 6, 2]],

                    # medium
                    [[5, 4, 3, 8, 9, 7, 1, 6, 2], [1, 9, 8, 3, 2, 6, 7, 4, 5], [2, 6, 7, 4, 5, 1, 3, 9, 8], [6, 1, 5, 9, 3, 4, 8, 2, 7], [8, 7, 9, 5, 6, 2, 4, 3, 1], [3, 2, 4, 7, 1, 8, 6, 5, 9], [7, 8, 2, 6, 4, 9, 5, 1, 3], [4, 3, 1, 2, 8, 5, 9, 7, 6], [9, 5, 6, 1, 7, 3, 2, 8, 4]],

                    [[6, 8, 5, 1, 3, 2, 9, 7, 4], [7, 3, 4, 5, 9, 8, 2, 6, 1], [2, 1, 9, 7, 6, 4, 8, 3, 5], [9, 2, 6, 8, 7, 1, 5, 4, 3], [8, 5, 1, 3, 4, 9, 6, 2, 7], [4, 7, 3, 2, 5, 6, 1, 9, 8], [5, 6, 8, 4, 2, 7, 3, 1, 9], [1, 9, 7, 6, 8, 3, 4, 5, 2], [3, 4, 2, 9, 1, 5, 7, 8, 6]],
                    # easy
                    [[3, 7, 9, 5, 6, 8, 4, 2, 1], [4, 5, 1, 9, 3, 2, 8, 7, 6], [8, 6, 2, 4, 1, 7, 5, 9, 3], [9, 2, 4, 8, 5, 3, 1, 6, 7], [1, 3, 6, 2, 7, 4, 9, 5, 8], [7, 8, 5, 1, 9, 6, 2, 3, 4], [5, 9, 3, 6, 8, 1, 7, 4, 2], [6, 4, 8, 7, 2, 5, 3, 1, 9], [2, 1, 7, 3, 4, 9, 6, 8, 5]],

                    [[1, 7, 8, 9, 2, 6, 3, 4, 5], [9, 4, 3, 8, 5, 1, 7, 2, 6], [6, 5, 2, 4, 7, 3, 8, 9, 1], [7, 2, 4, 5, 6, 8, 9, 1, 3], [5, 1, 9, 3, 4, 2, 6, 8, 7], [3, 8, 6, 1, 9, 7, 2, 5, 4], [2, 3, 1, 6, 8, 5, 4, 7, 9], [8, 9, 5, 7, 3, 4, 1, 6, 2], [4, 6, 7, 2, 1, 9, 5, 3, 8]],

                    [[3, 5, 1, 6, 7, 2, 9, 8, 4], [4, 6, 9, 8, 3, 1, 2, 5, 7], [2, 8, 7, 5, 4, 9, 6, 1, 3], [9, 4, 6, 1, 5, 7, 8, 3, 2], [1, 2, 8, 3, 9, 6, 7, 4, 5], [5, 7, 3, 2, 8, 4, 1, 9, 6], [7, 3, 4, 9, 2, 8, 5, 6, 1], [6, 9, 2, 4, 1, 5, 3, 7, 8], [8, 1, 5, 7, 6, 3, 4, 2, 9]],

                    [[9, 4, 6, 1, 5, 7, 3, 8, 2], [1, 2, 8, 3, 9, 6, 4, 7, 5], [5, 7, 3, 2, 8, 4, 9, 1, 6], [3, 5, 1, 6, 7, 2, 8, 9, 4], [4, 6, 9, 8, 3, 1, 5, 2, 7], [2, 8, 7, 5, 4, 9, 1, 6, 3], [6, 9, 2, 4, 1, 5, 7, 3, 8], [8, 1, 5, 7, 6, 3, 2, 4, 9], [7, 3, 4, 9, 2, 8, 6, 5, 1]],

                    [[3, 4, 2, 5, 6, 7, 8, 1, 9], [9, 5, 7, 1, 2, 8, 6, 3, 4], [1, 6, 8, 9, 4, 3, 5, 2, 7], [7, 2, 9, 8, 3, 1, 4, 5, 6], [5, 1, 4, 7, 9, 6, 3, 8, 2], [6, 8, 3, 4, 5, 2, 9, 7, 1], [2, 3, 5, 6, 7, 9, 1, 4, 8], [8, 7, 6, 3, 1, 4, 2, 9, 5], [4, 9, 1, 2, 8, 5, 7, 6, 3]],

                    [[7, 4, 5, 3, 9, 6, 2, 1, 8], [1, 9, 6, 2, 8, 4, 7, 5, 3], [8, 3, 2, 1, 5, 7, 4, 9, 6], [3, 7, 8, 4, 1, 5, 9, 6, 2], [4, 2, 9, 7, 6, 3, 1, 8, 5], [5, 6, 1, 9, 2, 8, 3, 7, 4], [9, 8, 4, 6, 7, 2, 5, 3, 1], [2, 5, 7, 8, 3, 1, 6, 4, 9], [6, 1, 3, 5, 4, 9, 8, 2, 7]],

                    [[3, 1, 2, 6, 9, 8, 4, 5, 7], [7, 8, 5, 4, 3, 1, 6, 9, 2], [4, 9, 6, 5, 2, 7, 1, 3, 8], [8, 7, 1, 3, 4, 2, 9, 6, 5], [2, 5, 9, 1, 7, 6, 3, 8, 4], [6, 4, 3, 8, 5, 9, 7, 2, 1], [1, 2, 4, 9, 8, 3, 5, 7, 6], [9, 6, 7, 2, 1, 5, 8, 4, 3], [5, 3, 8, 7, 6, 4, 2, 1, 9]],

                    [[8, 1, 7, 9, 2, 6, 3, 4, 5], [3, 9, 4, 8, 5, 1, 7, 2, 6], [2, 6, 5, 4, 7, 3, 8, 9, 1], [4, 7, 2, 5, 6, 8, 9, 1, 3], [9, 5, 1, 3, 4, 2, 6, 8, 7], [6, 3, 8, 1, 9, 7, 2, 5, 4], [7, 4, 6, 2, 1, 9, 5, 3, 8], [1, 2, 3, 6, 8, 5, 4, 7, 9], [5, 8, 9, 7, 3, 4, 1, 6, 2]],

                    [[3, 9, 8, 1, 4, 7, 5, 2, 6], [1, 7, 6, 8, 5, 2, 9, 3, 4], [5, 2, 4, 3, 6, 9, 1, 7, 8], [2, 8, 9, 7, 3, 1, 6, 4, 5], [6, 5, 7, 2, 9, 4, 3, 8, 1], [4, 3, 1, 6, 8, 5, 7, 9, 2], [7, 4, 3, 5, 1, 8, 2, 6, 9], [8, 1, 2, 9, 7, 6, 4, 5, 3], [9, 6, 5, 4, 2, 3, 8, 1, 7]],
                ]
        return data[num]


# Game()
