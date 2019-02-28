from functools import reduce
from minesweeper.text_game import TextGame
from minesweeper.board import Board

instructions = \
"""
moves are all of the form 'X i j' where i and j are rows and columns respectfully.
'X' must be one of the following commands:
  'C' is for checking or clicking on a square
  'F' is for flagging a mine
  'Q' is for marking a square you are not sure of
  'R' is for removing a flag or marking
"""

class Minesweeper(TextGame):
  def get_initial_input(self):
    n_str = self.get_input("input board size (integer greater than 0): ")
    assert n_str.isdigit(), "invalid input"
    print(instructions)
    self.n = int(n_str)
    self.board = Board(self.n)
    self.cmds = ['F', 'Q', 'C', 'R']

  def request_move(self):
    return self.get_input("input move: ")

  def execute_move(self, move):
    move = move.split(" ")
    cmd, i, j = move

    # convert coords to indices
    i = int(i)-1
    j = int(j)-1

    if cmd == 'F':
      self.board.flag(i, j)
    elif cmd == 'Q':
      self.board.question(i, j)
    elif cmd == 'C':
      self.board.check(i, j)
    elif cmd == 'R':
      self.board.remove_mark(i, j)

  def is_valid_move(self, move):
    move = move.split(" ")
    if len(move) != 3:
      print("invalid number of inputs")
      return False

    cmd, i, j = move
    if not i.isdigit() or not j.isdigit():
      print("coordinates must be positive integers")
      return False
    i = int(i)
    j = int(j)
    # Checks for supported command and valid indices
    return cmd in self.cmds and 0 < i and i <= self.n \
                            and 0 < j and j <= self.n

  """
  Returns True iff no mines have been checked and 
                   all non-mine squares have been checked
  """
  def won(self):
    if self.lost():
      return False
    for i in range(self.n):
      for j in range(self.n):
        if self.board.hidden_board[i][j] >= 0:
          c = self.board.visible_board[i][j]
          if not c.isdigit() and c != " ":
            return False
    return True

  """
  Returns True iff a mine has been checked
  """
  def lost(self):
    # Flattens board into 1D list to check if a mine was checked
    return "M" in reduce(lambda x, y: x+y, self.board.visible_board)

  def get_input(self, text):
    return input(text)

  def __str__(self):
    return str(self.board)
