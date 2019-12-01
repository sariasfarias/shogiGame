from Pieces import *

class Board(object):

	def __init__(self):
		# Player 1
		self.L1_i=Lance(1, 0, 8)
		self.K1_i=Knight(1, 1, 8)
		self.SG1_i=Silver_General(1, 2, 8)
		self.GG1_i=Gold_General(1, 3, 8)
		self.K1= King(1, 8, 4)
		self.GG1_d=Gold_General(1, 5, 8)
		self.SG1_d= Silver_General(1, 6, 8)
		self.K1_d=Knight(1, 7, 8)
		self.L1_d=Lance(1, 8, 9)
		self.R1=Rook(1, 7, 7)
		self.B1=Bishop(1, 1, 7)
		self.P1_1=Pawn(1, 0, 6)
		self.P1_2=Pawn(1, 1, 6)
		self.P1_3=Pawn(1, 2, 6)
		self.P1_4=Pawn(1, 3, 6)
		self.P1_5=Pawn(1, 4, 6)
		self.P1_6=Pawn(1, 5, 6)
		self.P1_7=Pawn(1, 6, 6)
		self.P1_8=Pawn(1, 7, 6)
		self.P1_9=Pawn(1, 8, 6)

		# Player 2
		self.L2_i=Lance(2, 0, 0)
		self.K2_i=Knight(2, 1, 0)
		self.SG2_i=Silver_General(2, 2, 0)
		self.GG2_i=Gold_General(2, 3, 0)
		self.K2= King(2, 4, 0)
		self.GG2_d=Gold_General(2, 5, 0)
		self.SG2_d= Silver_General(2, 6, 0)
		self.K2_d=Knight(2, 7, 0)
		self.L2_d=Lance(2, 8, 0)
		self.R2=Rook(2, 1, 1)
		self.B2=Bishop(2, 7, 1)
		self.P2_1=Pawn(2, 0, 2)
		self.P2_2=Pawn(2, 1, 2)
		self.P2_3=Pawn(2, 2, 2)
		self.P2_4=Pawn(2, 3, 2)
		self.P2_5=Pawn(2, 4, 2)
		self.P2_6=Pawn(2, 5, 2)
		self.P2_7=Pawn(2, 6, 2)
		self.P2_8=Pawn(2, 7, 2)
		self.P2_9=Pawn(2, 8, 2)

		#Board
		self.board = [
			[self.L2_i, self.K2_i, self.SG2_i ,self.SG2_i ,self.K2 , self.GG2_d ,self.SG2_d,self.K2_d ,self.L2_d ],
			[None, self.R2, None, None, None, None, None,self.B2 , None], 
			[self.P2_1, self.P2_2,self.P2_3 ,self.P2_4 ,self.P2_5 ,self.P2_6 ,self.P2_7 ,self.P2_8 ,self.P2_9 ],
			[None] * 9,
			[None] * 9,
			[None] * 9,
			[self.P1_1,self.P1_2 ,self.P1_3 ,self.P1_4 ,self.P1_5 ,self.P1_6 ,self.P1_7 ,self.P1_8 ,self.P1_9 ],
			[None, self.B1, None, None, None, None, None, self.R1, None],
			[self.L1_i,self.K1_i , self.SG1_i, self.GG1_d, self.K1, self.GG1_i, self.SG1_d, self.K1_d, self.L1_d]
			]

		self.boardPrint = [
			[self.L2_i.id, self.K2_i.id, self.SG2_i.id ,self.SG2_i.id ,self.K2.id , self.GG2_d.id ,self.SG2_d.id,self.K2_d.id ,self.L2_d.id ],
			[None, self.R2.id, None, None, None, None, None,self.B2.id , None], 
			[self.P2_1.id, self.P2_2.id,self.P2_3.id ,self.P2_4.id ,self.P2_5.id ,self.P2_6.id ,self.P2_7.id ,self.P2_8.id ,self.P2_9.id ],
			[None] * 9,
			[None] * 9,
			[None] * 9,
			[self.P1_1.id,self.P1_2.id ,self.P1_3.id ,self.P1_4.id ,self.P1_5.id ,self.P1_6.id ,self.P1_7.id ,self.P1_8.id ,self.P1_9.id ],
			[None, self.B1.id, None, None, None, None, None, self.R1.id, None],
			[self.L1_i.id,self.K1_i.id , self.SG1_i.id, self.GG1_d.id, self.K1.id, self.GG1_i.id, self.SG1_d.id, self.K1_d.id, self.L1_d.id]
			]
		self.dim = 9
		self.alphabets = "abcdefghi"
		self.nro_alphabet=0

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
	
	def move(self, player,piece,a,b):
		if piece == "K":
			self.move_king(player, a, b)


	def move_king(self, player, a, b ):
		X=int(a)-1
		Y=self.alphabets.find(b)-1
		#king player 1
		self.boardPrint[X][Y]=self.boardPrint[self.K1.x][self.K1.y]
		self.boardPrint[self.K1.x][self.K1.y]=None

		self.K1.x=X
		self.K1.y=Y
		
		