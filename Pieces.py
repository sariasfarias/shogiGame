class Piece(object):

	def __init__(self, player, x, y, promoted=False, cp = True):
		self.x = x
		self.y = y
		self.player = player
		self.promoted = promoted
		self.can_promote = cp

class King(Piece):

	def __init__(self, player, x, y, promoted=False):
		super(King, self).__init__(player, x, y, promoted, False)
		self.name = "King"
		self.id = "K"

class Gold_General(Piece):

	def __init__(self, player, x, y, promoted=False):
		super(Gold_General, self).__init__(player, x, y, promoted, False)
		self.name = "Gold General"
		self.id = "G"

class Silver_General(Piece):

	def __init__(self, player, x, y, promoted=False):
		super(Silver_General, self).__init__(player, x, y, promoted)
		if promoted is True:
			self.name = "Promoted Silver General"
			self.id = "+S"
		else:
			self.name = "Silver General"
			self.id = "S"

class Rook(Piece):

	def __init__(self, player, x, y, promoted=False):
		super(Rook, self).__init__(player, x, y, promoted)
		if promoted is True:
			self.name = "Promoted Rook"
			self.id = "+R"
		else:
			self.name = "Rook"
			self.id = "R"

class Bishop(Piece):

	def __init__(self, player, x, y, promoted=False):
		super(Bishop, self).__init__(player, x, y, promoted)
		if promoted is True:
			self.name = "Promoted Bishop"
			self.id = "+B"
		else:
			self.name = "Bishop"
			self.id = "B"

class Knight(Piece):

	def __init__(self, player, x, y, promoted=False):
		super(Knight, self).__init__(player, x, y, promoted)
		if promoted is True:
			self.name = "Promoted Knight"
			self.id = "+N"
		else:
			self.name = "Knight"
			self.id= "N"

class Lance(Piece):

	def __init__(self, player, x, y, promoted=False):
		super(Lance, self).__init__(player, x, y, promoted)
		if promoted is True:
			self.name = "Promoted Lance"
			self.id = "+L"
		else:
			self.name = "Lance"
			self.id = "L"

class Pawn(Piece):

	def __init__(self, player, x, y, promoted=False):
		super(Pawn, self).__init__(player, x, y, promoted)
		if promoted is True:
			self.name = "Promoted Pawn"
			self.id = "+P"
		else:
			self.name = "Pawn"
			self.id = "P"                  