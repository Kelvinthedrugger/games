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

    def display_both(self):
        """
        the way to display when playing
        prop 1: replace the elements in d_board once input is given
                : use x,y and grid_size to deal with edge cases
        do self.level == 1 first
        """
        # use loop: self.d_board[k] = self.n_board[k]
        # normal cases
        """
        x = [4,5,6]
        y = [6,5,4]
        self.x, self.y = x.pop(), y.pop()"""
        for i in range(-1,2):
            for j in range(-1,2):
                if (i+self.x,j+self.y) not in self.location:
                    self.d_board[i+self.x][j+self.y] = self.n_board[i+self.x][i+self.y]
        return

        # edge cases
        # 4 edge cases
        if self.x < 2:
            if self.y < 3:
                pass
            elif self.y > 6 and self.y < 8:
                pass
        if self.x > 6 and self.x < 8:
            if self.y < 3:
                pass
            elif self.y > 6 and self.y < 8:
                pass
        pass
    def play_debug(self):
        mining.bomb(self)
        mining.display_both(self)
        print("bomb location: ")
        self.x, self.y = 5,5
        #mining.display_both(self)
        for bombs in self.location:
            if (self.x,self.y) == bombs:
                print("you lose")
                return
 
    def play(self):
        mining.bomb(self)
        # mining.display_both(self)
        print("bomb location: ")
        x = int(input("row:"))
        y = int(input("col:"))
        self.x = x
        self.y = y
        #mining.display_both(self)
        for bombs in self.location:
            if (x,y) == bombs:
                print("you lose")
        #        return
        # for display the number


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
    game.display_number()
    for _ in range(10):
#        game.play()
        game.play_debug()
        game.display()
#        game.display_number()

