import unittest
from minesweeper.board import Board

class TestBoard(unittest.TestCase):
	def setUp(self):
		self.board = Board(4)
		self.board.hidden_board = [[0, 0, 0, 0], \
		                           [1, 1, 1, 0], \
		                           [1, -1, 2, 1], \
		                           [1, 2, -1, 1]]

	def test_generate_board(self):
		self.assertEqual(len(self.board.visible_board), 4)

	def test_neighbors(self):
		self.assertEqual(self.board._neighbors(0, 3),
			               [(0, 2), (1, 2), (1, 3)])

	def test_check(self):
		self.board.check(0, 1)
		self.assertEqual(self.board.visible_board, \
			               [[' ', ' ', ' ', ' '], \
			                ['1', '1', '1', ' '], \
			                ['#', '#', '2', '1'], \
			                ['#', '#', '#', '#']])

	def test_flag(self):
		self.board.flag(3, 1)
		self.assertEqual(self.board.visible_board, \
			               [['#', '#', '#', '#'], \
			                ['#', '#', '#', '#'], \
			                ['#', '#', '#', '#'], \
			                ['#', 'F', '#', '#']])
		self.board.remove_mark(3, 1)
		self.assertEqual(self.board.visible_board, \
			               [['#', '#', '#', '#'], \
			                ['#', '#', '#', '#'], \
			                ['#', '#', '#', '#'], \
			                ['#', '#', '#', '#']])

if __name__ == '__main__':
	unittest.main()
