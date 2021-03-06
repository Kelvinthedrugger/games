# ooxx game in a 3*3 well

class well:
    def __init__(self):
        self.board = ['#' for _ in range(9)]
        self.eval = [[],[]]

    def play(self):
        loc1 = int(input("player 1: ")) - 1

        if loc1 < 0 or loc1 > 8:
            print("input should be within 1 to 9, try again\n")
            well.play(self)

        self.board[loc1] = 'O'
        self.eval[0].append(loc1)

        well.display(self)
        well.game_over(self)

        loc2 = int(input("player 2: ")) - 1

        if loc2 < 0 or loc2 > 8:
            print("input should be within 1 to 9, try again\n")
            well.play(self)

        self.board[loc2] = 'X'
        self.eval[1].append(loc2)

        well.display(self)
        well.game_over(self)

    def game_over(self):
        win_list = [[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]

        for ev in self.eval:
            ev.sort()
            for i in range(len(ev)-3+1):
                tmp = ev[i:i+3]
                if tmp in win_list:
                    print("game over, winner is player %d" % (self.eval.index(ev)+1))
                    exit(0)

    def dummy(self,loc=10):
        # to prevent override the filled position
        if loc in (self.eval[0] or self.eval[1]):
            print("do not override, pls try again")
        pass

    def display(self):
        for i in range(0,9,3):
            print(self.board[i:i+3])
        print("")

if __name__ == "__main__":
    game = well()
    while(1):
        game.play()

