from Pieces import *

class Board(object):

	def __init__(self):
		self.board = [
			[Lance(2, 0, 0), Knight(2, 1, 0), Silver_General(2, 2, 0), Gold_General(2, 3, 0), King(2, 4, 0), Gold_General(2, 5, 0), Silver_General(2, 6, 0), Knight(2, 7, 0), Lance(2, 8, 0)],
			[None, Rook(2, 1, 1), None, None, None, None, None, Bishop(2, 7, 1), None], 
			[Pawn(2, 0, 2), Pawn(2, 1, 2), Pawn(2, 2, 2), Pawn(2, 3, 2), Pawn(2, 4, 2), Pawn(2, 5, 2), Pawn(2, 6, 2), Pawn(2, 7, 2), Pawn(2, 8, 2)],
			[None] * 9,
			[None] * 9,
			[None] * 9,
			[Pawn(1, 0, 6), Pawn(1, 1, 6), Pawn(1, 2, 6), Pawn(1, 3, 6), Pawn(1, 4, 6), Pawn(1, 5, 6), Pawn(1, 6, 6), Pawn(1, 7, 6), Pawn(1, 8, 6)],
			[None, Bishop(1, 1, 7), None, None, None, None, None, Rook(1, 7, 7), None],
			[Lance(1, 0, 8), Knight(1, 1, 8), Silver_General(1, 2, 8), Gold_General(1, 3, 8), King(1, 4, 8), Gold_General(1, 5, 8), Silver_General(1, 6, 8), Knight(1, 7, 8), Lance(1, 8, 8)]
			]

		self.boardPrint = [
			[Lance(2, 0, 0).id, Knight(2, 1, 0).id, Silver_General(2, 2, 0).id, Gold_General(2, 3, 0).id, King(2, 4, 0).id, Gold_General(2, 5, 0).id, Silver_General(2, 6, 0).id, Knight(2, 7, 0).id, Lance(2, 8, 0).id],
			[None, Rook(2, 1, 1).id, None, None, None, None, None, Bishop(2, 7, 1).id, None], 
			[Pawn(2, 0, 2).id, Pawn(2, 1, 2).id, Pawn(2, 2, 2).id, Pawn(2, 3, 2).id, Pawn(2, 4, 2).id, Pawn(2, 5, 2).id, Pawn(2, 6, 2).id, Pawn(2, 7, 2).id, Pawn(2, 8, 2).id],
			[None] * 9,
			[None] * 9,
			[None] * 9,
			[Pawn(1, 0, 6).id, Pawn(1, 1, 6).id, Pawn(1, 2, 6).id, Pawn(1, 3, 6).id, Pawn(1, 4, 6).id, Pawn(1, 5, 6).id, Pawn(1, 6, 6).id, Pawn(1, 7, 6).id, Pawn(1, 8, 6).id],
			[None, Bishop(1, 1, 7).id, None, None, None, None, None, Rook(1, 7, 7).id, None],
			[Lance(1, 0, 8).id, Knight(1, 1, 8).id, Silver_General(1, 2, 8).id, Gold_General(1, 3, 8).id, King(1, 4, 8).id, Gold_General(1, 5, 8).id, Silver_General(1, 6, 8).id, Knight(1, 7, 8).id, Lance(1, 8, 8).id]
			]
		self.dim = 9

	def print(self):
		
		alphabets = "abcdefghi"
		print("        ", end=' ')
		print("  ", end=' ')
		for i in range(1, 10):
			print(" " + str(alphabets[i-1]) + " ", end=' ')
		print("\n         ", end=' ')
		print("----" * 9)
		for x in range(0, 9):
			print("        ", end=' ')
			print( str(x+1) +"|" , end=' ')
			for y in range(0, 9):
				if self.boardPrint[x][y]== None:
					self.boardPrint[x][y]="."
				if ("*" in self.boardPrint[x][y]):
					print(self.boardPrint[x][y] + " ", end=' ')
				else:
					print(" " + self.boardPrint[x][y] + " ", end=' ')
			
			print("\n")