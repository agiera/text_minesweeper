import unittest
from unittest.mock import patch
from minesweeper.minesweeper import Minesweeper

class TestBoard(unittest.TestCase):
	@patch('minesweeper.minesweeper.Minesweeper.get_input',
		   return_value="4")
	def setUp(self, input):
		self.game = Minesweeper()
		self.game.get_initial_input()
		self.game.board.hidden_board = [[0, 0, 0, 0], \
			                            [1, 1, 1, 0], \
			                            [1, -1, 2, 1], \
			                            [1, 2, -1, 1]]

	def test_won(self):
		self.assertFalse(self.game.won())
		self.game.play_move("C 1 1")
		self.game.play_move("C 2 1")
		self.game.play_move("C 2 2")
		self.game.play_move("C 2 3")
		self.game.play_move("C 3 1")
		self.game.play_move("C 3 3")
		self.game.play_move("C 3 4")
		self.game.play_move("C 4 1")
		self.game.play_move("C 4 2")
		self.game.play_move("C 4 4")
		self.assertTrue(self.game.won())

	def test_lost(self):
		self.assertFalse(self.game.lost())
		self.game.play_move("C 4 3")
		self.assertTrue(self.game.lost())

if __name__ == '__main__':
	unittest.main()
