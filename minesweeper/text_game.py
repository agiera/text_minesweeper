"""
Abstract class for a text based game
"""
class TextGame:
  """
  Requests initial information from user and initializes game
  """
  def get_initial_input(self):
    raise NotImplementedError

  """
  Initializes game and starts main loop
  """
  def run(self):
    self.get_initial_input()

    print(self)
    while not self.is_over():
      print()
      move = self.request_move()

      if not self.play_move(move):
        print("invalid move")
        print()
        continue

      print()
      print(self)

    print()
    if self.won():
      print("You Won!!!!")
    else:
      print("Game Over!")

  """
  Plays move if legal
  Returns True if move is valid else False
  """
  def play_move(self, move):
    if self.is_valid_move(move):
      self.execute_move(move)
      return True
    else:
      return False

  """
  Requests move from user and returns the result
  """
  def request_move(self):
    raise NotImplementedError

  """
  Returns True iff the move is legal
  """
  def is_valid_move(self, move):
    raise NotImplementedError

  """
  Executes a move assuming that it is legal
  """
  def execute_move(self, move):
    raise NotImplementedError

  """
  Returns True iff the game is won
  """
  def won(self):
    raise NotImplementedError

  """
  Returns True iff the game is lost
  """
  def lost(self):
    raise NotImplementedError

  """
  Returns True iff the player has won or lost
  """
  def is_over(self):
    return self.won() or self.lost()

  """
  Used to show the player the state of the game
  """
  def __str__(self):
    raise NotImplementedError
