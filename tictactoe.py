class Grid:
  def __init__(self):
    self.board = [["_","_","_"], ["_","_","_"], ["_","_","_"]]

  def print(self):
    for row in self.board:
      for ele in row:
        print(ele, end=" ")
      print("")

  def lines(alp):
    # check if there's any line of "alp" in the board
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

