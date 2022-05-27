class Grid:
  def __init__(self):
    self.board = [["_","_","_"], ["_","_","_"], ["_","_","_"]]
    self.steps = 0 # number of space that is not empty, aka, has been placed w/ o/x
    # record played step
    self.x, self.y = [], []

  def print(self):
    for row in self.board:
      for ele in row:
        print(ele, end=" ")
      print("")

  def lines(alp):
    # check if there's any line of "alp" in the board
    # if < minimun steps: it's definitely not ended yet: return 0
    if self.steps < 5: return 0

    return 0

  def check_result(self):
    # instead of loop thru the board every time
    #  just record the input history would be easier and faster ?
    if lines("x"):
        print("player 2 wins")
        return 1
    elif lines("o"):
        print("player 2 wins")
        return 0
    else:
        return -1



  # i need library to use the mouse ?
  def play(self):
    # "x": 120, "o": 111
    while input(""):
      self.check_result()
      pass

if __name__=="__main__":
  g = Grid()
  g.print()

