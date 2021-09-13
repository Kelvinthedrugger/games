# ooxx game in a 3*3 well

class well:
    def __init__(self):
        self.board = ['#' for _ in range(9)]
        self.eval = [[],[]]

    def play(self):
        loc1 = int(input("player 1: "))
        if loc1 < 0 or loc1 > 8:
            print("input should be within 0 to 9, try again\n")
            play(self)
        self.board[loc1] = 'O'
        self.eval[0].append(loc1)

        well.display(self)

        loc2 = int(input("player 2: "))
        if loc2 < 0 or loc2 > 8:
            print("input should be within 0 to 9, try again\n")
            play(self)
        self.board[loc2] = 'X'
        self.eval[1].append(loc2)

        well.display(self)

    def game_over(self):
        # not done
        self.eval[0].sort()
        self.eval[1].sort()
        sum1 = sum(self.eval[0])
        evalu1 = [(sum1 - ele) for ele in self.eval[0]]
        sum2 = sum(self.eval[1])
        evalu2 = [(sum2 - ele) for ele in self.eval[1]]

    def display(self):
        for i in range(0,9,3):
            print(self.board[i:i+3])
        print("")

if __name__ == "__main__":
    game = well()
    while(1):
        game.play()
