
import random
from itertools import permutations as P

class sudoku:

    def __init__(self):
        combinations = list(P(list(range(1,10))))
        assert len(combinations) == 362880
        # a block: [[1,2,3],[4,5,6],[7,8,9]]
        blocks = []
        for i in range(9):
            idx = random.randint(1,len(combinations))
            block = combinations[idx]
            block = [block[i:i+3] for i in range(0,9,3)]
            blocks.append(block)
        
        # add checker here

        self.blocks = blocks

    def checker(self):
        # locate the 'collisions'
        # re-permute the 'collisions'

        pass

    def display(self):
        # 0,0,0; 0,1,0; 0,2,0
        # 0,0,1; 0,1,1; 0,2,1
        # 0,0,2; 0,1,2; 0,2,2
        print("")
        for B in range(9):
            for ele in range(3):
                for row in range(3):
                    print(" ", self.blocks[B][row][ele],end="")
                print("",end=" ")
            print("")

            if B%3 == 2:
                print("")

class sudo2:
    # apply alternative method here
    """
    to be fixed:
    assigning the same block for different number
    """

    def __init__(self):
        board = [[0]*9 for _ in range(9)]
        board = [board[i:i+3] for i in range(0,9,3)]
        # fill the number
        for num in range(1,3):
            col_idx = [[0,1,2] for _ in range(3)]
            print("num %d" % num)
            for i in range(3):
                row_idx = [0,1,2] # for row checking
                for j in range(3):
                    idx = random.randint(0,8)
                    print("block %d" % (j+3*i+1))
                    if j > 0:
                        idx = sudo2.row_check(self,idx,row_idx)
                    
                    if i > 0:
                        # think how to integrate col with row check
                        idx = sudo2.col_check(self,idx,col_idx[j],row_idx)

                    if num > 1:
                        # apply number collision check
                        # idx = num_check()
                        # not done: 'not in list' error
                        idx = sudo2.num_check(self,idx,row_idx,col_idx,board[i][j],i,j)

                    board[i][j][idx] = num
                    print("mod of idx %d" % (idx//3))
                    a = row_idx.pop(row_idx.index(idx//3))
                    col_idx[j].pop(col_idx[j].index(idx % 3))
                    print("checker %d" % a)
                    print("left idx", row_idx)
                    print("%d,%d" % (i,j))
                    print("")

        self.board = board

    def row_check(self,idx,row_list):
        # change the index (reset) if collision has occurred
        while(not (idx//3 in row_list)):
            idx = random.randint(0,8)
            print("row reset idx %d" % idx)
        return idx

    def col_check(self,idx,col_list,row_list):
        # notice when do we apply col_check
        while(not (idx % 3 in col_list and idx // 3 in row_list)):
            idx = random.randint(0,8)
            print("col reset idx %d" % idx)
        return idx


    def num_check(self,idx,row_list,col_list,arr,i,j):
        if j == 0:
            if i == 0:
                while(arr[idx] != 0):
                    idx = random.randint(0,8)
                    print("num reset idx %d" % idx)
                return idx
            while(not(idx // 3 in row_list) and arr[idx] != 0):
                idx = random.randint(0,8)
                print("num reset idx %d" % idx)
            return idx

        while(not(idx // 3 in row_list and idx % 3 in col_list) and arr[idx] != 0):
            idx = random.randint(0,8)
            print("num reset idx %d" % idx)
        return idx


    def display(self):
        print("")
        for board in self.board:
            for row in range(0,9,3):
                for Row in range(3):
                    print(" ",board[Row][row:row+3],end="")
                print("")
            print("")

        # 3,3,9 
        print(" board shape: %d, %d, %d" % (len(self.board),len(self.board[0]),len(self.board[0][0])))
"""
method 3.x per se
    # maybe implement a random pick function would be much easier
    # e.g.
    # F: the picking function
    # a = F[(1,2,3]); a = 1 or 2 or 3
    # [1,2,3].pop([1,2,3].index(a))
"""
# method 3
# succeed but can be fixed
class sudo3:

    def __init__(self):
        board = [[0]*9 for _ in range(9)]
        board = [board[i:i+3] for i in range(0,9,3)]
        position = [list(range(9)) for _ in range(9)]

        # fill
        for num in range(1,6):
            col_list = [[0,1,2] for _ in range(3)]
            print("num: %d" % num)
            for i in range(3):
                row_list = [0,1,2]
                for j in range(3):
                    idx = random.randint(0,8)
                    # re-select, very loopy
                    while idx not in position[3*i+j]:
                        idx = random.randint(0,8)
                    if j > 0:
                        # row check
                        while(idx//3 not in row_list):
                            idx = random.randint(0,8)
                    if i > 0:
                        # col check
                        while(not (idx//3 in row_list and idx % 3 in col_list[j])):
                            idx = random.randint(0,8)
                    if num > 1:
                        # num check
                        while(not (idx//3 in row_list and idx % 3 in col_list[j]) or board[i][j][idx] != 0):
                            idx = random.randint(0,8)

                    board[i][j][idx] = num
                    a = position[3*i+j].pop(position[3*i+j].index(idx))
                    print("popped %d" % a)
                    row_list.pop(row_list.index(idx//3))
                    col_list[j].pop(col_list[j].index(idx%3))
        
        self.board = board

    def display(self):
        print("")
        for board in self.board:
            for row in range(0,9,3):
                for Row in range(3):
                    print(" ",board[Row][row:row+3],end="")
                print("")
            print("")

        # 3,3,9 
        print(" board shape: %d, %d, %d" % (len(self.board),len(self.board[0]),len(self.board[0][0])))


# method 3.1
# slightly better than method 3
"""
problem: random pick might result to dead end
potential sol'n: implement a fixer that begins to act @ block 1
for test: close the game when it reaches a dead end
"""
class sudo4:
    def __init__(self):
        board = [[0]*9 for _ in range(9)]
        board = [board[i:i+3] for i in range(0,9,3)]
        pos = [list(range(9)) for _ in range(9)]
        
        for num in range(1,6):
            start = time()
            print("num %d"%num)
            col_list = [[0,1,2] for _ in range(3)]
            for i in range(3):
                row_list = [0,1,2] 
                for j in range(3):
                    # somehow buggy: stuck in idx loop
                    idx = sudo4.func(self,pos[3*i+j])
                    if j > 0:
                        print("row check")
                        while(not(idx//3 in row_list)):
                            idx = sudo4.func(self,pos[3*i+j])
                    if i > 0:
                        print("col check")
                        # dead end ?
                        while(not(idx//3 in row_list and idx%3 in col_list[j])):
                            idx = sudo4.func(self,pos[3*i+j])
                            if time() - start > 5:
                                print("reset required")
                                self.board = board
                                return 
                    
                    print("block: %d, index: %d\n" % (3*i+j+1,idx))
                    board[i][j][idx] = num
                    pos[3*i+j].pop(pos[3*i+j].index(idx))
                    row_list.pop(row_list.index(idx//3))
                    col_list[j].pop(col_list[j].index(idx%3))
        
        self.board = board

    def func(self,arr):
        ele = arr[R(0,len(arr)-1)]
        return ele
        arr.pop(arr.index(idx))
        return arr,idx

    def display(self):
        print("")
        for board in self.board:
            for row in range(0,9,3):
                for Row in range(3):
                    print(" ",board[Row][row:row+3],end="")
                print("")
            print("")

        # 3,3,9 
        print(" board shape: %d, %d, %d" % (len(self.board),len(self.board[0]),len(self.board[0][0])))

# method 3.1 + collector implementation
class sudo5:
    def __init__(self):
        board = [[0]*9 for _ in range(9)]
        board = [board[i:i+3] for i in range(0,9,3)]
        pos = [list(range(9)) for _ in range(9)]
        #for num in range(1,6):
        num = 0
        while num < 4:
            num += 1
            start = time()
            print("\n***num %d***\n"%num)
            idc = sudo5.fill(self,num,pos,board,start)
            if idc:
                num -= 1
                sudo5.debug_display(self,board)

        self.board = board

    def fill(self,num,pos,board,start):
        clt = [] # num collector
        col_list = [[0,1,2] for _ in range(3)]
        for i in range(3):
            row_list = [0,1,2] 
            for j in range(3):
                idx = sudo5.func(self,pos[3*i+j])
                if j > 0:
                    while(not(idx//3 in row_list)):
                        idx = sudo5.func(self,pos[3*i+j])
                        if time() - start > 5:
                            print("\n reset required! due to row\n")
                            for coor in clt:
                                i,j = clt.index(coor)//3, clt.index(coor)%3
                                board[i][j][coor] = 0 # restore the value
                                pos[3*i+j].append(coor)
                            return 1 # restart the round

                if i > 0:
                    while(not(idx//3 in row_list and idx%3 in col_list[j])):
                        idx = sudo5.func(self,pos[3*i+j])
                        if time() - start > 5:
                            print("\n reset required! due to col\n")
                            for coor in clt:
                                i,j = clt.index(coor)//3, clt.index(coor)%3
                                board[i][j][coor] = 0 # restore the value
                                pos[3*i+j].append(coor)
                            return 1 # restart the round
                 
                print("block %d\n"%(3*i+j+1))
                board[i][j][idx] = num
                # collect the positions each round
                clt.append(pos[3*i+j].pop(pos[3*i+j].index(idx)))
                row_list.pop(row_list.index(idx//3))
                col_list[j].pop(col_list[j].index(idx%3))

    def func(self,arr):
        ele = arr[R(0,len(arr)-1)]
        return ele

    def debug_display(self,board):
        print("")
        for ele in board:
            for row in range(0,9,3):
                for Row in range(3):
                    print(" ",ele[Row][row:row+3],end="")
                print("")
            print("")
 
    def display(self):
        print("")
        for board in self.board:
            for row in range(0,9,3):
                for Row in range(3):
                    print(" ",board[Row][row:row+3],end="")
                print("")
            print("")
        # 3,3,9 
        print(" board shape: %d, %d, %d" % (len(self.board),len(self.board[0]),len(self.board[0][0])))


from random import randint as R
from time import time # use timer as debugger
if __name__ == "__main__":
    #g4 = sudo4()
    #g4.display()
    g5 = sudo5()
    g5.display()
