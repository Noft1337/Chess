from Piece_Class import *


class King(Piece):
    def __init__(self, team):
        self.name = "King"
        super().__init__(name=self.name, team=team)


class Queen(Piece):
    def __init__(self, team):
        self.name = "Queen"
        super().__init__(name=self.name, team=team)


class Bishop(Piece):
    def __init__(self, team):
        self.name = "Bishop"
        super().__init__(name=self.name, team=team)


class Rook(Piece):
    def __init__(self, team):
        self.name = "Rook"
        super().__init__(name=self.name, team=team)


class Knight(Piece):
    def __init__(self, team):
        self.name = "Knight"
        super().__init__(name=self.name, team=team)


class Pawn(Piece):
    def __init__(self, team):
        self.name = "Pawn"
        super().__init__(name=self.name, team=team)
