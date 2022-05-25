class Grid:
  def __init__(self):
    self.board = [["_","_","_"], ["_","_","_"], ["_","_","_"]]

  def print(self):
    for row in self.board:
      for ele in row:
        print(ele, end=" ")
      print("")


  def check_result(self):
    # instead of loop thru the board every time
    #  just record the input history would be easier and faster ?
    pass



  # i need library to use the mouse ?
  def play(self):
    # "x": 120, "o": 111
    while input(""):
      self.check_result()
      pass

if __name__=="__main__":
  g = Grid()
  g.print()

