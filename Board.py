from Pieces import *
from colorama import init, Fore, Back, Style
import sys
import numpy as np

class Board(object):

	def __init__(self):
		# Player 1
		self.L1_i=Lance(1, 8, 0)
		self.K1_i=Knight(1, 8, 1)
		self.SG1_i=Silver_General(1, 8, 2)
		self.GG1_i=Gold_General(1, 8, 3)
		self.K1= King(1, 8, 4)
		self.GG1_d=Gold_General(1, 8, 5)
		self.SG1_d= Silver_General(1, 8, 6)
		self.K1_d=Knight(1, 8, 7)
		self.L1_d=Lance(1, 8, 8)
		self.R1=Rook(1, 7, 7)
		self.B1=Bishop(1, 7, 1)
		self.P1_1=Pawn(1, 6, 0)
		self.P1_2=Pawn(1, 6, 1)
		self.P1_3=Pawn(1, 6, 2)
		self.P1_4=Pawn(1, 6, 3)
		self.P1_5=Pawn(1, 6, 4)
		self.P1_6=Pawn(1, 6, 5)
		self.P1_7=Pawn(1, 6, 6)
		self.P1_8=Pawn(1, 6, 7)
		self.P1_9=Pawn(1, 6, 8)

		# Player 2
		self.L2_i=Lance(2, 0, 0)
		self.K2_i=Knight(2, 0, 1)
		self.SG2_i=Silver_General(2, 0, 2)
		self.GG2_i=Gold_General(2, 0, 3)
		self.K2= King(2, 0, 4)
		self.GG2_d=Gold_General(2, 0, 5)
		self.SG2_d= Silver_General(2, 0, 6)
		self.K2_d=Knight(2, 0, 7)
		self.L2_d=Lance(2, 0, 8)
		self.R2=Rook(2, 1, 1)
		self.B2=Bishop(2, 1, 7)
		self.P2_1=Pawn(2, 2, 0)
		self.P2_2=Pawn(2, 2, 1)
		self.P2_3=Pawn(2, 2, 2)
		self.P2_4=Pawn(2, 2, 3)
		self.P2_5=Pawn(2, 2, 4)
		self.P2_6=Pawn(2, 2, 5)
		self.P2_7=Pawn(2, 2, 6)
		self.P2_8=Pawn(2, 2, 7)
		self.P2_9=Pawn(2, 2, 8)
		#Board
		self.board = [
			[self.L2_i, self.K2_i, self.SG2_i ,self.GG2_i ,self.K2 , self.GG2_d ,self.SG2_d,self.K2_d ,self.L2_d ],
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
			[self.L2_i.id+"i", self.K2_i.id+"i", self.SG2_i.id+"i" ,self.GG2_i.id+"i" ,self.K2.id+" " , self.GG2_d.id+"d" ,self.SG2_d.id+"d",self.K2_d.id+"d" ,self.L2_d.id +"d"],
			[None, self.R2.id+" ", None, None, None, None, None,self.B2.id+" " , None], 
			[self.P2_1.id+"1", self.P2_2.id+"2",self.P2_3.id+"3" ,self.P2_4.id+"4" ,self.P2_5.id+"5" ,self.P2_6.id+"6" ,self.P2_7.id+"7" ,self.P2_8.id+"8" ,self.P2_9.id+"9" ],
			[None] * 9,
			[None] * 9,
			[None] * 9,
			[self.P1_1.id+"1",self.P1_2.id+"2" ,self.P1_3.id +"3",self.P1_4.id+"4" ,self.P1_5.id+"5" ,self.P1_6.id+"6" ,self.P1_7.id+"7" ,self.P1_8.id+"8" ,self.P1_9.id+"9" ],
			[None, self.B1.id+" ", None, None, None, None, None, self.R1.id+" ", None],
			[self.L1_i.id+"i",self.K1_i.id+"i" , self.SG1_i.id+"i", self.GG1_d.id+"i", self.K1.id+" ", self.GG1_i.id+"d", self.SG1_d.id+"d", self.K1_d.id+"d", self.L1_d.id+"d"]
			]
		self.dim = 9
		self.alphabets = "abcdefghi"
		self.nro_alphabet=0
		self.valid= True
		self.p1Piece = [0, 0, 0, 0, 0, 0, 0]
		self.p2Piece = [0, 0, 0, 0, 0, 0, 0]
		self.GetPiece = ["Rr", "Bb", "Gg", "Ss", "Nn", "Ll", "Pp"]
		self.Recovery_pieces=[]

	def invalidmove(self):
		print("\n" * 13)
		print("                 Invalid Move! ", end=' ')
		print("\n" * 9)

	def invaliddrope(self):
		print("\n" * 13)
		print("                 Invalid  Drop! ", end=' ')
		print("\n" * 9)
	
	def invalid_piece(self):
		print("\n" * 13)
		print("                 Invalid  Piece! ", end=' ')
		print("\n" * 9)

	def out_of_range(self):
		print("\n" * 13)
		print("                 OUT OF RANGE!!! ", end=' ')
		print("\n" * 9)

	def print(self):
		
		alphabets = "abcdefghi"
		print("        ", end=' ')
		print("  ", end=' ')
		for i in range(1, 10):
			print(" "+ str(alphabets[i-1]) + "  ", end=' ')
		print("\n         ", end=' ')
		print("-----" * 9)
		for x in range(0, 9):
			print("        ", end=' ')
			print( str(x+1) +"|" , end=' ')
			for y in range(0, 9):
				pl=0
				if self.boardPrint[x][y]== None:
					self.boardPrint[x][y]=". "
				elif self.boardPrint[x][y]!= ". ":
					pl=self.board[x][y].player

				if (self.boardPrint[x][y].__contains__("+")):
					if(pl==1 and self.boardPrint[x][y]!= ". "):
						print(Fore.CYAN  + self.boardPrint[x][y] + " "+Fore.RESET, end=' ')
					elif pl==2 and self.boardPrint[x][y]!= ". ":
						print(Fore.YELLOW +self.boardPrint[x][y] + " "+Fore.RESET, end=' ')
					else:
						print(self.boardPrint[x][y] + " ", end=' ')
				else:
					if(pl==1 and self.boardPrint[x][y]!= ". "):
						print(Fore.CYAN  +  " "+self.boardPrint[x][y] + " "+Fore.RESET, end=' ')
					elif pl==2 and self.boardPrint[x][y]!= ". ":
						print(Fore.YELLOW + " "+ self.boardPrint[x][y] + " "+Fore.RESET, end=' ')
					else:
						print( " "+self.boardPrint[x][y] + " ", end=' ')

			print("\n")
		print("\n")
		print("          P1:", end=' ')
		for a in range(0, 7):
			print(self.GetPiece[a][0] + "*" + str(self.p1Piece[a]) + " ", end=' ')
		print("")

		print("          P2:", end=' ')
		for a in range(0, 7):
			print(self.GetPiece[a][0] + "*" + str(self.p2Piece[a]) + " ", end=' ')
		print("")
		print("\n")
	
	def drope(self, player,  a , b , first):
		print("voy a dropear")
		if player==1:
			if self.board[a][b] != None:
				if first:#pieza recien ingresada
					if self.board[a][b].player==1:
						self.invaliddrope()
						self.valid=False
					elif self.board[a][b].player==2:
						if self.boardPrint[a][b].__contains__("R"):
							self.invaliddrope()
							self.valid= False
						elif self.boardPrint[a][b].__contains__("B"):
							self.invaliddrope()
							self.valid= False
						elif self.boardPrint[a][b].__contains__("G"):
							self.invaliddrope()
							self.valid= False
						elif self.boardPrint[a][b].__contains__("S"):
							self.invaliddrope()
							self.valid= False
						elif self.boardPrint[a][b].__contains__("N"):
							self.invaliddrope()
							self.valid= False
						elif self.boardPrint[a][b].__contains__("L"):
							self.invaliddrope()
							self.valid= False
						elif self.boardPrint[a][b].__contains__("P"):
							self.invaliddrope()
							self.valid= False
					else:
						self.valid=True
				else: 	
					if self.board[a][b].player==1:
						self.invaliddrope()
						self.valid= False
					elif self.board[a][b].player==2:
						if self.boardPrint[a][b].__contains__("R"):
							self.p1Piece[0]=+1
						elif self.boardPrint[a][b].__contains__("B"):
							self.p1Piece[1]=+1
						elif self.boardPrint[a][b].__contains__("G"):
							self.p1Piece[2]=+1
						elif self.boardPrint[a][b].__contains__("S"):
							self.p1Piece[3]=+1
						elif self.boardPrint[a][b].__contains__("N"):
							self.p1Piece[4]=+1
						elif self.boardPrint[a][b].__contains__("L"):
							self.p1Piece[5]=+1
						elif self.boardPrint[a][b].__contains__("P"):
							self.p1Piece[6]=+1
			else:
				self.valid=True		
		if player==2:
			if self.board[a][b] != None:
				if first:
					if self.board[a][b].player==2  :
						self.invaliddrope()
						self.valid= False
					elif self.board[a][b].player==1:
						if self.boardPrint[a][b].__contains__("R"):
							self.invaliddrope()
							self.valid= False
						elif self.boardPrint[a][b].__contains__("B") :
							self.invaliddrope()
							self.valid= False
						elif self.boardPrint[a][b].__contains__("G") :
							self.invaliddrope()
							self.valid= False
						elif self.boardPrint[a][b].__contains__("S") :
							self.invaliddrope()
							self.valid= False
						elif self.boardPrint[a][b].__contains__("N") :
							self.invaliddrope()
							self.valid= False
						elif self.boardPrint[a][b].__contains__("L") :
							self.invaliddrope()
							self.valid= False
						elif self.boardPrint[a][b].__contains__("P"):
							self.invaliddrope()
							self.valid= False
					else:
						self.valid=True	
				else:
					if self.board[a][b].player==2  :
						self.invaliddrope()
						self.valid= False
					elif self.board[a][b].player==1:
						if self.boardPrint[a][b].__contains__("R"):
							self.p2Piece[0]=+1
						elif self.boardPrint[a][b].__contains__("B") :
							self.p2Piece[1]=+1
						elif self.boardPrint[a][b].__contains__("G") :
							self.p2Piece[2]=+1
						elif self.boardPrint[a][b].__contains__("S") :
							self.p2Piece[3]=+1
						elif self.boardPrint[a][b].__contains__("N") :
							self.p2Piece[4]=+1
						elif self.boardPrint[a][b].__contains__("L") :
							self.p2Piece[5]=+1
						elif self.boardPrint[a][b].__contains__("P"):
							self.p2Piece[6]=+1
			else:
				self.valid=True				
				
	def move(self, player,piece, a, b):		
		Y=self.alphabets.find(b)
		X=int(a)-1
		
		if self.valid==True:
			if piece == "k":
				self.move_king(player, X, Y)
			elif piece.__contains__("n"):
				self.move_knight(player, X, Y, piece)
			elif piece.__contains__("g"):
				self.move_gold_general(player, X, Y, piece)
			elif piece.__contains__("s"):
				self.move_silver_general(player, X, Y, piece)
			elif piece.__contains__("l"):
				self.move_lance(player, X, Y, piece)
			elif piece.__contains__("b"):
				self.move_bishop(player, X, Y, piece)
			elif piece.__contains__("r"):
				self.move_rook(player, X, Y, piece)
			elif piece.__contains__("p"):
				self.move_pawn(player, X, Y, piece)
			else:
				self.invalid_piece()
				self.valid= False
			
	def move_king(self, player, a, b ):
		aux=0
		if player==1:
			p=[self.K1]
			if (a-p[aux].x)>1 or (b-p[aux].y)>1:
				self.out_of_range()
				self.valid= False
			if self.valid:
				self.drope(player, a, b,False)
				self.valid_move( player, a, b, p, aux, False)
		if player==2:
			p=[self.K2]
			if (a-p[aux].x)>1 or (b-p[aux].y)>1:
				self.out_of_range()
				self.valid= False
			if self.valid:
				self.drope(player, a, b,False)
				self.valid_move( player, a, b, p, aux, False)
	
	def move_gold_general(self, player, a, b, piece ):
		if piece[1]=="i":
			aux=0
		elif piece[1]=="d":
			aux=1
		
		if player==1:
			if piece[0] in "12":
				p=self.add_piece(piece)
			else:
				p=[self.GG1_i,self.GG1_d]
			if (b == p[aux].y-1 and a == p[aux].x-1) or (b == p[aux].y+1  and a == p[aux].x-1) :
				self.invalidmove()
				self.valid= False
			elif (abs(a-p[aux].x))>1 or (abs(b-p[aux].y))>1:
				self.out_of_range()
				self.valid= False

			if self.valid:
				self.drope(player, a, b,False)
				self.valid_move( player, a, b, p, aux, False)
				#check
				self.check(player, a+1, b+1)
				self.check(player, a+1, b-1)
				self.check(player, a+1, b)
				self.check(player, a, b-1)
				self.check(player, a, b+1)
				self.check(player, a-1, b)
		if player==2:
			if piece[0] in "12":
				p=self.add_piece(piece)
			else:
				p=[self.GG2_i,self.GG2_d]
			if (b == p[aux].y+1 and a == p[aux].x+1) or (b == p[aux].y-1  and a == p[aux].x+1) :
				self.invalidmove()
				self.valid= False
			elif  (abs(a-p[aux].x))>1 or (abs(b-p[aux].y))>1:
				self.out_of_range()
				self.valid= False

			if self.valid:
				self.drope(player, a, b,False)
				self.valid_move( player, a, b, p, aux, False)
				#check
				self.check(player, a+1, b+1)
				self.check(player, a+1, b-1)
				self.check(player, a+1, b)
				self.check(player, a, b-1)
				self.check(player, a, b+1)
				self.check(player, a-1, b)

	def move_silver_general(self, player, a, b, piece ):
		aux=0
		if player==1:
			if piece[0] in "12":
				p=self.add_piece(piece)
			else:
				if piece[1]=="i":
					aux=0
				elif piece[1]=="d":
					aux=1			
				p=[self.SG1_i,self.SG1_d]
			if p[aux].promoted:
				self.move_gold_general_promoted(player, a, b, piece, p[aux].x, p[aux].y)
			else:			
				if (b == p[aux].y-1 and a == p[aux].x) or (b == p[aux].y+1  and a == p[aux].x) or (b == p[aux].y  and a == p[aux].x-1) :
					self.invalidmove()
					self.valid= False
				elif (a-p[aux].x)>1 or (b-p[aux].y)>1:
					self.out_of_range()
					self.valid= False
				if self.valid:
					self.drope(player, a, b, False)
					self.valid_move( player, a, b, p, aux, False)
					#check
					self.check(player, a+1, b+1)
					self.check(player, a+1, b-1)
					self.check(player, a+1, b)
					self.check(player, a-1, b-1)
					self.check(player, a-1, b+1)
			#promocion de ficha
			self.promoted( player, a, b, p, aux)
		if player==2:
			if piece[0] in "12":
				p=self.add_piece(piece)
			else:
				if piece[1]=="i":
					aux=0
				elif piece[1]=="d":
					aux=1			
				p=[self.SG2_i,self.SG2_d]

			if p[aux].promoted:
				self.move_gold_general_promoted(player, a, b, piece, p[aux].x, p[aux].y)
			else:
				if (b == p[aux].y-1 and a == p[aux].x) or (b == p[aux].y+1  and a == p[aux].x) or (b == p[aux].y  and a == p[aux].x+1) :
					self.invalidmove()
					self.valid= False
				elif (a-p[aux].x)>1 or (b-p[aux].y)>1:
					self.out_of_range()
					self.valid= False
				if self.valid:	
					self.drope(player, a, b, False)
					self.valid_move( player, a, b, p, aux, False)
					#check
					self.check(player, a+1, b+1)
					self.check(player, a+1, b-1)
					self.check(player, a+1, b)
					self.check(player, a-1, b-1)
					self.check(player, a-1, b+1)
			#promocion de ficha
			self.promoted( player, a, b, p, aux)

	def move_knight(self, player, a, b, piece ):
		aux=0
		if player==1:
			if piece[0] in "12":
				p=self.add_piece(piece)
			else:
				if piece[1]=="i":
					aux=0
				elif piece[1]=="d":
					aux=1			
				p=[self.K1_i,self.K1_d]
			if p[aux].promoted:
				self.move_gold_general_promoted(player, a, b, piece, p[aux].x, p[aux].y)
			else:	
				if (b != p[aux].y-1 and a != p[aux].x-2) or (b != p[aux].y+1  and a != p[aux].x-2) :
					self.invalidmove()
					self.valid= False
				if self.valid:
					self.drope(player, a, b, False)
					self.valid_move( player, a, b, p, aux, False)
					#check
					self.check(player, a+2, b+1)
					self.check(player, a+2, b-1)
			#promocion de ficha
			self.promoted( player, a, b, p, aux)
	
		if player==2:
			if piece[0] in "12":
				p=self.add_piece(piece)
			else:
				if piece[1]=="i":
					aux=0
				elif piece[1]=="d":
					aux=1			
				p=[self.K2_i,self.K2_d]	
			if p[aux].promoted:
				self.move_gold_general_promoted(player, a, b, piece, p[aux].x, p[aux].y)
			else:
				if (b != p[aux].y-1 and a != p[aux].x+2) or (b != p[aux].y+1  and a != p[aux].x-2) :
					self.invalidmove()
					self.valid= False
				if self.valid:
					self.drope(player, a, b, False)
					self.valid_move( player, a, b, p, aux, False)
					#check
					self.check(player, a+2, b+1)
					self.check(player, a+2, b-1)
			#promocion de ficha
			self.promoted( player, a, b, p, aux)

	def move_lance(self, player, a, b, piece ):
		aux=0
		if player==1:
			if piece[0] in "12":
				p=self.add_piece(piece)
			else:
				if piece[1]=="i":
					aux=0
				elif piece[1]=="d":
					aux=1
				p=[self.L1_i,self.L1_d]
			if p[aux].promoted:
				self.move_gold_general_promoted(player, a, b, piece, p[aux].x, p[aux].y)
			else:
				if (b !=p[aux].y and a>p[aux].x) :
					self.invalidmove()
					self.valid= False
				elif (abs(b-p[aux].y))>1 and (abs(a-p[aux].x))<1:
					self.out_of_range()
					self.valid= False
				if self.valid:
					self.drope(player, a, b, False)
					self.valid_move( player, a, b, p, aux, False)
					#check
					for i in range(9-a):
						if self.check(player, i , b):
							break
			#promocion de ficha
			self.promoted( player, a, b, p, aux)
		if player==2:
			if piece[0] in "12":
				p=self.add_piece(piece)
			else:
				if piece[1]=="i":
					aux=0
				elif piece[1]=="d":
					aux=1			
				p=[self.L2_i,self.L2_d]
			if p[aux].promoted:
				self.move_gold_general_promoted(player, a, b, piece, p[aux].x, p[aux].y)
			else:
				if (b != p[aux].y and a<p[aux].x):
					self.invalidmove()
					self.valid= False
				elif (abs(b-p[aux].y))>1 and (abs(a-p[aux].x))<1:
					self.out_of_range()
					self.valid= False
				if self.valid:
					self.drope(player, a, b, False)
					self.valid_move( player, a, b, p, aux, False)
					#check
					for i in range(9):
						if self.check(player, i , b):
							break
			#promocion de ficha
			self.promoted( player, a, b, p, aux)
	
	def move_bishop(self, player, a, b, piece ):
		aux=0	
		if player==1:
			if piece[0] in "12":
				p=self.add_piece(piece)
			else:
				p=[self.B1]
			if p[aux].promoted:
				if (abs(p[aux].y-b)!= abs(p[aux].x-a) and ( p[aux].y!=b and p[aux].x==a and a!=1)) :
					self.invalidmove()
					self.valid= False
				
				if self.valid:
					self.drope(player, a, b, False)
					self.valid_move( player, a, b, p, aux, False)
					#check
					self.check(player, a, b+1)
					self.check(player, a, b-1)
					self.check(player, a-1, b)
					self.check(player, a+1, b)
					np_matrix=np.array(self.boardPrint)
					if(b>4):
						diag1=np_matrix.diagonal(8-a)
						diag2=np.fliplr(np_matrix).diagonal(a+b)
					elif(b<4):
						diag1=np_matrix.diagonal(b-a)
						diag2=np.fliplr(np_matrix).diagonal(8-a+b)
					else:
						diag1=np_matrix.diagonal()
						diag2=np.fliplr(np_matrix).diagonal()
					
					for i in diag1:
						if i != None:
							if i.__contains__("K"):
								print (Fore.RED+"          Player 1 has placed Player 2's King in Check! "+Fore.RESET)
								break
					for i in diag2:
						if i != None:
							if i.__contains__("K"):
								print (Fore.RED+"          Player 1 has placed Player 2's King in Check! "+Fore.RESET)
								break	
			else:
				if (abs(p[aux].y-b)!= abs(p[aux].x-a)) :
					self.invalidmove()
					self.valid= False
				if self.valid:
					self.drope(player, a, b, False)
					self.valid_move( player, a, b, p, aux, False)
					#check
					np_matrix=np.array(self.boardPrint)
					if(b>4):
						diag1=np_matrix.diagonal(8-a)
						diag2=np.fliplr(np_matrix).diagonal(a+b)
					elif(b<4):
						diag1=np_matrix.diagonal(b-a)
						diag2=np.fliplr(np_matrix).diagonal(8-a+b)
					else:
						diag1=np_matrix.diagonal()
						diag2=np.fliplr(np_matrix).diagonal()
					for i in diag1:
						if i != None:
							if i.__contains__("K2"):
								print (Fore.RED+"          Player 1 has placed Player 2's King in Check! "+Fore.RESET)
								break
					for i in diag2:
						if i != None:
							if i.__contains__("K2"):
								print (Fore.RED+"          Player 1 has placed Player 2's King in Check! "+Fore.RESET)
								break	


					self.check(player, a, i)
			#promocion de ficha
			self.promoted( player, a, b, p, aux)
	
		if player==2:
			if piece[0] in "12":
				p=self.add_piece(piece)
			else:
				p=[self.B2]
			if p[aux].promoted:
				if (abs(p[aux].y-b)!= abs(p[aux].x-a) and ( p[aux].y!=b and p[aux].x==a and abs(p[aux].x-a)!=1)) :
					self.invalidmove()
					self.valid= False
				if self.valid:
					self.drope(player, a, b, False)
					self.valid_move( player, a, b, p, aux, False)
					#check
					self.check(player, a, b+1)
					self.check(player, a, b-1)
					self.check(player, a-1, b)
					self.check(player, a+1, b)
					np_matrix=np.array(self.boardPrint)
					if(b>4):
						diag1=np_matrix.diagonal(8-a)
						diag2=np.fliplr(np_matrix).diagonal(a+b)
					elif(b<4):
						diag1=np_matrix.diagonal(b-a)
						diag2=np.fliplr(np_matrix).diagonal(8-a+b)
					else:
						diag1=np_matrix.diagonal()
						diag2=np.fliplr(np_matrix).diagonal()
					for i in diag1:
						if i != None:
							if i.__contains__("K2"):
								print (Fore.RED+"          Player 2 has placed Player 1's King in Check! "+Fore.RESET)
								break
					for i in diag2:
						if i != None:
							if i.__contains__("K2"):
								print (Fore.RED+"          Player 2 has placed Player 1's King in Check! "+Fore.RESET)
								break	
			else:
				if (abs(p[aux].y-b)!= abs(p[aux].x-a)) :
					self.invalidmove()
					self.valid= False
				if self.valid:
					self.drope(player, a, b, False)
					self.valid_move( player, a, b, p, aux, False)
					#check
					np_matrix=np.array(self.boardPrint)
					if(b>4):
						diag1=np_matrix.diagonal(8-a)
						diag2=np.fliplr(np_matrix).diagonal(a+b)
					elif(b<4):
						diag1=np_matrix.diagonal(b-a)
						diag2=np.fliplr(np_matrix).diagonal(8-a+b)
					else:
						diag1=np_matrix.diagonal()
						diag2=np.fliplr(np_matrix).diagonal()
					for i in diag1:
						if i != None:
							if i.__contains__("K2"):
								print (Fore.RED+"          Player 2 has placed Player 1's King in Check! "+Fore.RESET)
								break
					for i in diag2:
						if i != None:
							if i.__contains__("K2"):
								print (Fore.RED+"          Player 2 has placed Player 1's King in Check! "+Fore.RESET)
								break	
			#promocion de ficha
			self.promoted( player, a, b, p, aux)

	def move_rook(self, player, a, b, piece):
		aux=0
		if player==1:
			if piece[0] in "12":
				p=self.add_piece(piece)
			else:
				p=[self.R1]
			if p[aux].promoted:
				if ((b != p[aux].y and a != p[aux].x) and (abs(p[aux].y-b) != abs(p[aux].x-a) and abs(p[aux].x-a)!=1 ) ) :
					self.invalidmove()
					self.valid= False
				if self.valid:
					self.drope(player, a, b,False)
					self.valid_move( player, a, b, p, aux, False)
					#check
					self.check(player, a+1, b+1)
					self.check(player, a+1, b-1)
					self.check(player, a-1, b+1)
					self.check(player, a-1, b-1)
					for i in range(a,-1):
						self.check(player, a, i)
					for i in range(a,9):
						self.check(player, a, i)
					for i in range(b,-1):
						self.check(player, i , b)
					for i in range(b,9):
						self.check(player, i , b)
			else:
				if (b != p[aux].y and a != p[aux].x) :
					self.invalidmove()
					self.valid= False
				
				if self.valid:
					self.drope(player, a, b,False)
					self.valid_move( player, a, b, p, aux, False)
					#check
					for i in range(a,-1):
						self.check(player, a, i)
					for i in range(a,9):
						self.check(player, a, i)
					for i in range(b,-1):
						self.check(player, i , b)
					for i in range(b,9):
						self.check(player, i , b)
			#promocion de ficha
			self.promoted( player, a, b, p, aux)	
		if player==2:
			if piece[0] in "12":
				p=self.add_piece(piece)
			else:
				p=[self.R2]
			if p[aux].promoted:
				if (abs(p[aux].y-b)!= abs(p[aux].x-a) and ( p[aux].y!=b and p[aux].x==a and a!=1)) :
					self.invalidmove()
					self.valid= False
				
				if self.valid:
					self.drope(player, a, b,False)
					self.valid_move( player, a, b, p, aux, False)
					#check
					self.check(player, a+1, b+1)
					self.check(player, a+1, b-1)
					self.check(player, a-1, b+1)
					self.check(player, a-1, b-1)
					#check
					for i in range(a,-1):
						self.check(player, a, i)
					for i in range(a,9):
						self.check(player, a, i)
					for i in range(b,-1):
						self.check(player, i , b)
					for i in range(b,9):
						self.check(player, i , b)
			else:
				if (b != p[aux].y and a != p[aux].x) :
					self.invalidmove()
					self.valid= False

				if self.valid:
					self.drope(player, a, b,False)
					self.valid_move( player, a, b, p, aux, False)
					#check
					for i in range(a,-1):
						self.check(player, a, i)
					for i in range(a,9):
						self.check(player, a, i)
					for i in range(b,-1):
						self.check(player, i , b)
					for i in range(b,9):
						self.check(player, i , b)
			#promocion de ficha
			self.promoted( player, a, b, p, aux)

	def move_pawn(self, player, a, b, piece ):
		aux=0
		if player==1:
			if piece[0] in "123456789":
				aux=int (piece[0])-1
				p=self.add_piece(piece)
			else:
				aux=int (piece[1])-1
				p=[self.P1_1,self.P1_2,self.P1_3,self.P1_4,self.P1_5,self.P1_6,self.P1_7,self.P1_8,self.P1_9]
			if p[aux].promoted:
				self.move_gold_general_promoted(player, a, b, piece, p[aux].x, p[aux].y)
			else:
				if (b != p[aux].y or a != p[aux].x-1) :
					self.invalidmove()
					self.valid= False
				if self.valid:
					self.drope(player, a, b,False)	
					self.valid_move(player, a, b, p, aux, False)
			#promocion de ficha
			self.promoted( player, a, b, p, aux)
			#check
			self.check(player, a+1 , b)			
		if player==2:
			if piece[0] in "123456789":
				aux=int (piece[0])-1
				p=self.add_piece(piece)
			else:
				aux=int (piece[1])-1
				p=[self.P2_1,self.P2_2,self.P2_3,self.P2_4,self.P2_5,self.P2_6,self.P2_7,self.P2_8,self.P2_9]
			if p[aux].promoted:
				self.move_gold_general_promoted(player, a, b, piece, p[aux].x, p[aux].y)
			else:
				if (b != p[aux].y or a != p[aux].x+1) :
					self.invalidmove()
					self.valid= False
				if self.valid:
					self.drope(player, a, b,False)
					self.valid_move( player, a, b, p, aux, False)
			#promocion de ficha
			self.promoted( player, a, b, p, aux)
			#check
			self.check(player, a+1 , b)	

	def valid_move(self, player, a, b, p, aux, first):
		if first==False:

			king_piece=self.boardPrint[a][b]

			self.boardPrint[a][b]=self.boardPrint[p[aux].x][p[aux].y]
			self.boardPrint[p[aux].x][p[aux].y]=None
			self.board[a][b]=self.board[p[aux].x][p[aux].y]
			self.board[p[aux].x][p[aux].y]=None
			p[aux].x=a
			p[aux].y=b
			if(king_piece.__contains__("K")):
				print("\n")
				print("\n")
				print (Fore.GREEN+"          Player",player," has won! "+Fore.RESET)
				sys.exit()	
		else:
			self.boardPrint[a][b]=p[aux].id
			self.board[a][b]=p[aux]
	
	def check(self, player, a, b):
		if player==1:
			if self.boardPrint[a][b]!= ". ":
				if self.boardPrint[a][b]=="K" :
					print (Fore.RED+"          Player 1 has placed Player 2's King in Check! "+Fore.RESET)
					return True
		else:
			if self.boardPrint[a][b]!= ". ":
				if self.boardPrint[a][b]=="K":
					print(Fore.RED+"          Player 2 has placed Player 1's King in Check!"+Fore.RESET)
					return True
	
	def promoted(self, player, a, b, p, aux):	
		if p[aux].promoted==False:
			if player==1:
				if p[aux].x <3:
					p[aux].promoted = True						
			elif player==2:
				if p[aux].x >5:
					p[aux].promoted = True
			if 	p[aux].promoted == True:
				p[aux].id="+"+p[aux].id
				side=self.boardPrint[p[aux].x][p[aux].y][1:]
				if side.__contains__("i"):
					side="i"
				elif side.__contains__("d"):
					side="d"
				else:
					side=""	
				self.boardPrint[p[aux].x][p[aux].y]=self.board[p[aux].x][p[aux].y].id+side	
	
	def move_gold_general_promoted(self, player, a, b, piece,x,y ):
			aux=0
			if player==1:
				p=[self.board[x][y]]
				if (b == p[aux].y-1 and a == p[aux].x-1) or (b == p[aux].y+1  and a == p[aux].x-1):
					self.invalidmove()
					self.valid= False
				elif (abs(a-p[aux].x))>1 or (abs(b-p[aux].y))>1:
					self.out_of_range()
					self.valid= False
				
				if self.valid:
					self.drope(player, a, b,False)
					self.valid_move( player, a, b, p, aux, False)
					#check
					self.check(player, a+1, b+1)
					self.check(player, a+1, b-1)
					self.check(player, a+1, b)
					self.check(player, a, b-1)
					self.check(player, a, b+1)
					self.check(player, a-1, b)
				
			if player==2:
				p=[self.board[x][y]]
				if (b == p[aux].y+1 and a == p[aux].x+1) or (b == p[aux].y-1  and a == p[aux].x+1) :
					self.invalidmove()
					self.valid= False
				elif  (abs(a-p[aux].x))>1 or (abs(b-p[aux].y))>1:
					self.out_of_range()
					self.valid= False

				if self.valid:
					self.drope(player, a, b,False)
					self.valid_move( player, a, b, p, aux, False)
					#check
					self.check(player, a+1, b+1)
					self.check(player, a+1, b-1)
					self.check(player, a+1, b)
					self.check(player, a, b-1)
					self.check(player, a, b+1)
					self.check(player, a-1, b)		

	def add_piece(self, piece):
		pos=0
		for item in self.Recovery_pieces:
			if item.id == piece.upper():
				break
			pos=+1
		
		return [self.Recovery_pieces[pos]]

	def introduce_piece(self, player, piece, a, b):
		j=self.alphabets.find(b)
		i=int(a)-1
		aux=0
		print(piece)
		cant=0
		if self.valid==True:
			
			if piece.__contains__("r"):#torre
				self.p1Piece[0]=self.p1Piece[0]-1
				p=[Rook(player, i, j)]
				#id
				cant = p[aux].id.count("R")
			elif piece.__contains__("b"):
				self.p1Piece[1]=self.p1Piece[1]-1
				p=[Bishop(player, i, j)]
				#id
				cant = p[aux].id.count("B")
			elif piece.__contains__("g"):
				self.p1Piece[2]=self.p1Piece[2]-1
				p=[Gold_General(player, i, j)]
				#id
				cant = p[aux].id.count("G")
			elif piece.__contains__("s"):
				self.p1Piece[3]=self.p1Piece[3]-1
				p=[Silver_General(player, i, j)]
				#id
				cant = p[aux].id.count("S")
			elif piece.__contains__("n"):
				self.p1Piece[4]=self.p1Piece[4]-1
				p=[Knight(player, i, j)]
				#id
				cant = p[aux].id.count("N")
			elif piece.__contains__("l"):
				self.p1Piece[5]=self.p1Piece[5]-1
				p=[Lance(player, i, j)]
				#id
				cant = p[aux].id.count("L")
			elif piece.__contains__("p"):
				self.p1Piece[6]=self.p1Piece[6]-1
				p=[Pawn(player, i, j)]
				#id
				cant = p[aux].id.count("P")
			else:
				self.invalid_piece()
				self.valid= False	
			
			if self.valid==True:
				#cosas comunes
				p[aux].id=str(cant)+p[aux].id
				#insertar en la lista
				self.Recovery_pieces.append(p[aux])
				#que no se coma ninguna pieza
				self.drope(player, i, j, True)
				#insertarlo
				if self.valid:
					self.valid_move( player, i, j, p, aux, True)		
