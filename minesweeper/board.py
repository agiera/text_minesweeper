import random
import copy

class Board:
  def __init__(self, n):
    self.n = n
    self.visible_board = [["#" for i in range(n)] for i in range(n)]
    self.hidden_board = self._generate_board(n)

  def flag(self, i, j):
    if self.visible_board[i][j] == "#":
      self.visible_board[i][j] = "F"

  def question(self, i, j):
    if self.visible_board[i][j] == "#":
      self.visible_board[i][j] = "?"

  def remove_mark(self, i, j):
    if self.visible_board[i][j] == "F" or self.visible_board[i][j] == "?":
      self.visible_board[i][j] = "#"

  def check(self, i, j):
    # ? and F should not be clickable
    if self.visible_board[i][j] == "F" or self.visible_board[i][j] == "?":
      return

    # case user clicks on a mine
    if self.hidden_board[i][j] == -1:
      self.visible_board[i][j] = "M"
    elif self.hidden_board[i][j] == 0:
      if self.visible_board[i][j] != " ":
        self.visible_board[i][j] = " "
        for x, y in self._neighbors(i, j):
          self.check(x, y)
    else:
      self.visible_board[i][j] = str(self.hidden_board[i][j])

  def _generate_board(self, n):
    p = 0.1
    # place mines randomly
    # each square has a 0.1 prob of being a mine
    mines = [[int(random.random() < p) for _ in range(n)] for _ in range(n)]

    # calculates hidden board from mines
    board = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
      for j in range(n):
        if mines[i][j] == 1:
          board[i][j] = -1
        else:
          neighbors = self._neighbors(i, j)
          # calculate number of neighbors that are mines
          board[i][j] = sum([mines[x][y] for (x, y) in neighbors])
    return board

  def _neighbors(self, i, j):
    n = self.n
    # candidates for valid neighbors of i j
    neighbors = [(i+d1, j+d2) for d1 in [-1, 0, 1] for d2 in [-1, 0, 1]]
    # remove itself
    neighbors.remove((i, j))
    # remove neighbors with invalid indices
    in_bounds = lambda coords: 0 <= coords[0] and coords[0] < n and 0 <= coords[1] and coords[1] < n
    neighbors = list(filter(in_bounds, neighbors))
    return neighbors

  def __str__(self):
    display = copy.deepcopy(self.visible_board)
    for i in range(self.n):
      display[i].insert(0, "|")
      display[i].insert(0, str(i+1))
    col_labels = [str(i+1) for i in range(self.n)]
    col_labels.insert(0, " ")
    col_labels.insert(0, " ")
    # insert label border
    display.insert(0, ["=" for i in range(self.n+2)])
    # insert labels
    display.insert(0, col_labels)
    board_str = "\n".join(["".join(l) for l in display])
    return board_str
