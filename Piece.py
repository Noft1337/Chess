# Class of piece (soldier)
# Responsible for the position of a piece and if it was eaten or not

class Piece(object):
    def __init__(self, team, name):
        self.name = name
        self.team = team
        self.is_king = self.name == "King"
