import unittest
from Board import *

class TestBoardPrint(unittest.TestCase):

    def test_board_print(self):
        board=Board()
        
        self.assertIsNotNone(board.print() )   