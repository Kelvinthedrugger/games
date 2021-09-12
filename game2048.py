# implement game 2048 without pygame library
# stable version @ ~/rand-things/pythings/game2048.py

import random
# use queue to move() more efficiently
# combine with dict{} to locate the values


class Game:
    def __init__(self):
        self.score = 0
        self.merge = 0  # indicator of merge occurance
        # 0: continue, 1: lose
        self.game_state = 0
        # faster
        self.board = [[0 for _ in range(4)] for _ in range(4)]
        # # below test on of the edge cases
        # # checker() failed
        self.board = [[i+1+j for i in range(4)] for j in range(0, 16, 4)]
        self.board[-1][-1] = 0
        self.board[-2][-1] = 2

    def produce(self):
        self.row = random.randint(0, 3)
        self.col = random.randint(0, 3)
        print(self.row, self.col)
        # check if it's empty
        if self.board[self.row][self.col] != 0:
            Game.checker(self)
            # edge cases
            print(self.game_state)
            if self.game_state == 1:
                return
            Game.produce(self)
        # produce
        self.board[self.row][self.col] = 2

    def leftmove(self):
        def left(self):
            for arr in self.board:
                for i in range(4):
                    if arr[i] == 0:
                        # store the location of leftmost 0
                        loc = i
                        for j in range(i, 4):
                            if arr[j] != 0:
                                # swap
                                arr[loc] = arr[j]
                                arr[j] = 0
                                break

        def merge_left(self):
            for arr in self.board:
                for i in range(4):
                    for j in range(i+1, 4):
                        if arr[i] > 0 and arr[i] == arr[j]:
                            print("merge occurred\n", self.board.index(arr), i)
                            arr[i] *= 2
                            arr[j] = 0
                            self.merge += arr[i]
                            break
        merge_left(self)
        left(self)

    def upmove(self):
        def up(self):
            for col in range(4):
                for row in range(4):
                    if self.board[row][col] == 0:
                        loc = row
                        for k in range(row, 4):
                            if self.board[k][col] != 0:
                                self.board[loc][col] = self.board[k][col]
                                self.board[k][col] = 0
                                break

        def merge_up(self):
            for col in range(4):
                for row in range(4):
                    for target in range(row+1, 4):
                        if self.board[target][col] > 0 and self.board[target][col] == self.board[row][col]:
                            print("merge occurred\n", target, col)
                            self.board[row][col] *= 2
                            self.board[target][col] = 0
                            self.merge = self.board[row][col]
                            break

        merge_up(self)
        up(self)

    def downmove(self):
        def down(self):
            for col in range(4):
                for row in range(3, -1, -1):
                    if self.board[row][col] == 0:
                        loc = row
                        for k in range(row, -1, -1):
                            if self.board[k][col] != 0:
                                self.board[loc][col] = self.board[k][col]
                                self.board[k][col] = 0
                                break

        def merge_down(self):
            for col in range(4):
                for row in range(3, -1, -1):
                    for target in range(row-1, -1, -1):
                        if self.board[target][col] > 0 and self.board[target][col] == self.board[row][col]:
                            print("merge occurred\n", target, col)
                            self.board[row][col] *= 2
                            self.board[target][col] = 0
                            self.merge = self.board[row][col]
                            break

        merge_down(self)
        down(self)

    def rightmove(self):
        def right(self):
            for arr in self.board:
                for i in range(3, -1, -1):
                    if arr[i] == 0:
                        # store the location of rightmost 0
                        loc = i
                        for j in range(i, -1, -1):
                            if arr[j] != 0:
                                # swap
                                arr[loc] = arr[j]
                                arr[j] = 0
                                break

        def merge_right(self):
            for arr in self.board:
                for i in range(3, -1, -1):
                    for j in range(i-1, -1, -1):
                        if arr[i] > 0 and arr[i] == arr[j]:
                            print("merge occurred\n", self.board.index(arr), i)
                            arr[i] *= 2
                            arr[j] = 0
                            self.merge += arr[i]
                            break
        merge_right(self)
        right(self)

    def score_count(self):
        # calculate the current score
        self.score += self.merge
        print("current score", self.score, end="\n\n")
        self.merge = 0

    def move_constraint(self):
        """should be finished after checker() is done ..."""
        pass

    def checker(self):
        # step1: check if the board is full: worked!
        for arr in self.board:
            for ele in arr:
                if ele == 0:
                    return
        # step 2: check numbers that can be merged
        # horizontal
        for arr in self.board:
            for j in range(3):
                if arr[j] == arr[j+1]:
                    return
        # vertical
        for col in range(4):
            for row in range(3, 0, -1):
                if self.board[row][col] == self.board[row-1][col]:
                    return
        # after checked all the cases
        self.game_state = 1

    def display(self):
        for board in self.board:
            print(board)
        print("")


"""transpose might still works
, which would saved lines
, and produced more steps to calculate
"""
"""buggy when perform edge case in __init__()"""
if __name__ == "__main__":
    """
    constrained move not done (tricky)
    checker() is weird
    """
    # reproduce
    random.seed(1237)
    game = Game()
    while(1):
        game.produce()
        game.display()
        instruction = input("which direction to move: ")
        if (instruction).upper() == "S":
            game.downmove()
        elif instruction.upper() == "W":
            game.upmove()
        elif instruction.upper() == "A":
            game.leftmove()
        elif instruction.upper() == "D":
            game.rightmove()
        else:
            print("Invalid input, pls try again")
        game.score_count()
        game.display()
        game.checker()
        if game.game_state == 1:
            print("Lost")
            break
