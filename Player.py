class Player():
    def __init__(self, player):
        self.player=player
        self.turn_num =0
        self.move_to="0a"
        self.piece="peon"

    def turn(self):
        print("* * *  PLAYER ",self.player,"  * * *")
        self.piece = input("          Choose your piece: ")
        self.move_to = input("          Now  Move: To ")

    def ingres_piece(self):
        print("* * *  INTRODUCE A PIECE ",self.player,"  * * *")
        self.piece = input("          Choose your piece: ")
        self.move_to = input("          Now  Move: To ")
        
