# Class of piece (soldier)
# Responsible for the position of a piece and if it was eaten or not
# Might not use it

class Piece(object):
    def __init__(self, team):
        self.team = team
        if team.lower() == "black":
            self.name = "B_king"
            self.symbol = "♔"
        else:
            self.name = "W_King"
            self.symbol = "♚"

    def get_team(self):
        return self.team

    def get_symbol(self):
        return self.symbol

    def get_name(self):
        return self.name

    def __repr__(self):
        return self.symbol

    def __str__(self):
        return self.symbol
