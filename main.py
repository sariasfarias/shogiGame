from Board import *
from Player import *

class main():
    board= Board()
    
   # board.print()
    player1= Player(1)
    player2= Player(2)

    
    while 1:
        board.valid= False
        while board.valid== False:
            board.valid= True
            board.print()
            a=0
            for i in board.p1Piece:
                a=a+i
            if(a>0):
                print("* * *  PLAYER ",player1.player,"  * * *")
                choose = input("          Do you want to introduce a piece? y/n ")
            else:
                choose="n"
            if choose=="y":
                player1.ingres_piece()
                try:
                    if (player1.move_to[0] not in "123456789"):
                        board.valid= False
                        print ("          INVALID number OPTION \n")
                    elif (player1.move_to[1] not in board.alphabets):
                        board.valid= False
                        print ("          INVALID letter OPTION \n")
                except (NameError, IndexError):
                    board.valid= False
                    print ("          INVALID OPTION \n")
                if board.valid == True:
                    board.introduce_piece(player1.player, player1.piece, player1.move_to[0], player1.move_to[1])
            elif choose=="n":
                player1.turn()
                try:
                    if (player1.move_to[0] not in "123456789"):
                        board.valid= False
                        print ("          INVALID number OPTION \n")
                    elif (player1.move_to[1] not in board.alphabets):
                        board.valid= False
                        print ("          INVALID letter OPTION \n")
                except (NameError, IndexError):
                    board.valid= False
                    print ("          INVALID OPTION \n")
                if board.valid == True:
                    board.move(player1.player, player1.piece, player1.move_to[0], player1.move_to[1])
            else:
                board.valid= False
                print ("          INVALID OPTION \n")
            
        player1.turn_num += 1

        board.valid= False
        while board.valid== False:
            board.valid= True
            board.print()
            a=0
            for a in board.p2Piece:
                a=+a
            
            if(a>0):
                print("* * *  PLAYER ",player2.player,"  * * *")
                choose = input("          Do you want to introduce a piece? y/n ")
            else:
                choose="n"
                
            if choose=="y":
                player2.ingres_piece()
                try:
                    if (player2.move_to[0] not in "123456789"):
                        board.valid= False
                        print ("          INVALID number OPTION \n")
                    elif (player2.move_to[1] not in board.alphabets):
                        board.valid= False
                        print ("          INVALID letter OPTION \n")
                except (NameError, IndexError):
                    board.valid= False
                    print ("          INVALID OPTION \n")
                if board.valid == True:
                    board.move(player2.player, player2.piece, player2.move_to[0], player2.move_to[1])
            elif choose=="n":
                player2.turn()
                try:
                    if (player2.move_to[0] not in "123456789"):
                        board.valid= False
                        print ("          INVALID number OPTION \n")
                    elif (player2.move_to[1] not in board.alphabets):
                        board.valid= False
                        print ("          INVALID letter OPTION \n")
                except (NameError, IndexError):
                    board.valid= False
                    print ("          INVALID OPTION \n")
                if board.valid == True:
                    board.move(player2.player, player2.piece, player2.move_to[0], player2.move_to[1])
            else:
                board.valid= False
                print ("          INVALID OPTION ")
        player2.turn_num += 1



        
        
