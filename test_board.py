import unittest
from board import BoardGame

class TestSequenceBoard(unittest.TestCase):
    def setUp(self):
        self.board = BoardGame()

    def test_move_up(self):
        position = self.board.move((2,4),"U")
        self.assertEqual((1,4), position)

    def test_move_down(self):
        position = self.board.move((2,4),"D")
        self.assertEqual((3,4), position)

    def test_move_left(self):
        position = self.board.move((2,4),"L")
        self.assertEqual((2,3), position)

    def test_move_right(self):
        position = self.board.move((2,4),"R")
        self.assertEqual((2,5), position)