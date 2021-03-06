# level 1: 9*9; 10
# level 2: 16*16; 40 
# level 3: 30*16; 99

import random

class mining:
    """
    requires 2 boards:
    one for display: d_board
    the other for numbers: n_board
    and a function to display two boards partially at the same time
    """
    def __init__(self,level=1):
        self.level = level
        if self.level == 1:
            """board for display"""
            self.d_board = [['*']*9 for _ in range(9)]

    def bomb(self):
        # bomb location
        if self.level == 1:
            rows = [random.randint(1,9) for _ in range(10)]
            cols = [random.randint(1,9) for _ in range(10)]

        # check if there are same bomb locations existed
        def checker(array):
            for i in range(len(array)):
                for j in range(i,len(array)):
                    if array[i] == array[j]:
                        return 1,i # tuple
            return 0

        while not checker(rows)[0]*checker(cols)[0]:
            if checker(rows)[0]:
                if checker(cols)[0]:
                    # reassign the ele in cols that's not the same
                    cols[checker(cols)[1]] = random.randint(0,10)

        # bomb location after checking
        self.location = [(row,col) for row,col in zip(rows,cols)]

        # calculate the numbers around the bombs
        # , then pop the 1st and last element of each row
        if self.level == 1:
            # augmented 
            self.n_board = [[0] * 11 for _ in range(11)]

        # fill the board with bomb
        for loc in self.location:
            self.n_board[loc[0]][loc[1]] = '#'

        # no need to grid search again
        for loc in self.location:
            i, j = loc[0], loc[1]
            for k in range(-1,2):
                for m in range(-1,2):
                    if self.n_board[i+k][j+m] != '#':
                        self.n_board[i+k][j+m] += 1

        # pop the augmented elements
        self.n_board.pop(0)
        self.n_board.pop()
        for row in self.n_board:
            row.pop(0)
            row.pop()
 
    def play(self):
        print("bomb location: ")
        x = int(input("row:"))
        y = int(input("col:"))
        self.x = x
        self.y = y
        mining.display_number(self)
        for bombs in self.location:
            if (x,y) == bombs:
                print("you lose")
                exit(0)
    

    def display(self):
        """display the board for players"""
        print("")
        for arr in self.d_board:
            for ele in arr:
                print(" ", ele,end="  ")
            print("\n")

    def display_number(self):
        print("")
        for arr in self.n_board:
            for ele in arr:
                print(" ", ele,end="  ")
            print("\n")

if __name__ == "__main__":

    random.seed(1337)
    game = mining()
    game.bomb()
    game.display()
    for _ in range(2):
        game.play()
        game.display()

    game.display_number()

