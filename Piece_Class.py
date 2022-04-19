# Class of piece (soldier)
# Responsible for the position of a piece and if it was eaten or not
# Might not use it
from Variables import *


class Piece(object):
    def __init__(self, team: str, name: str, x: int, y: int):
        self._team = team
        self.x = x
        self.y = y
        if team.lower() == "white":
            self.name = "W_" + name.capitalize()[0]
            self.symbol = W_SYMBOLS[name]
        else:
            self.name = "B_" + name.capitalize()[0]
            self.symbol = B_SYMBOLS[name]

    def get_team(self):
        return self._team

    def get_symbol(self):
        return self.symbol

    def get_cords(self):
        return self.x, self.y

    def get_name(self):
        return self.name

    def __repr__(self):
        return self.symbol

    def __str__(self):
        return self.symbol
