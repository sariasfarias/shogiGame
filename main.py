from Board import *
from Player import *

class main():
    board= Board()
    
    board.print()
    player1= Player(1)
    player2= Player(2)


    player1.turn()
    board.move(player1.player, player1.piece, player1.move_to[0], player1.move_to[1])
    board.print()