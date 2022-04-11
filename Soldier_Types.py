# All the soldier types that are in the game
# Maybe there's a better way to do this

class King:
    def __init__(self, team):
        self.team = team
        if team.lower() == "black":
            self.name = "B_king"
            self.symbol = "♔"
        else:
            self.name = "W_King"
            self.symbol = "♚"

    def get_symbol(self):
        return self.symbol

    def get_name(self):
        return self.name

    def get_team(self):
        return self.team

    def __repr__(self):
        return self.symbol

    def __str__(self):
        return self.symbol


class Queen:
    def __init__(self, team):
        self.team = team
        if team.lower() == "black":
            self.name = "B_Queen"
            self.symbol = "♕"
        else:
            self.name = "W_Queen"
            self.symbol = "♛"

    def get_symbol(self):
        return self.symbol

    def get_name(self):
        return self.name

    def get_team(self):
        return self.team

    def __repr__(self):
        return self.symbol

    def __str__(self):
        return self.symbol


class Rook:
    def __init__(self, team):
        self.team = team
        if team.lower() == "black":
            self.name = "B_Rook"
            self.symbol = "♖"
        else:
            self.name = "W_Rook"
            self.symbol = "♜"

    def get_symbol(self):
        return self.symbol

    def get_name(self):
        return self.name

    def get_team(self):
        return self.team

    def __repr__(self):
        return self.symbol

    def __str__(self):
        return self.symbol


class Bishop:
    def __init__(self, team):
        self.team = team
        if team.lower() == "black":
            self.name = "B_Bishop"
            self.symbol = "♗"
        else:
            self.name = "W_Bishop"
            self.symbol = "♝"

    def get_symbol(self):
        return self.symbol

    def get_name(self):
        return self.name

    def get_team(self):
        return self.team

    def __repr__(self):
        return self.symbol

    def __str__(self):
        return self.symbol


class Knight:
    def __init__(self, team):
        self.team = team
        if team.lower() == "black":
            self.name = "B_Knight"
            self.symbol = "♘"
        else:
            self.name = "W_Knight"
            self.symbol = "♞"

    def get_symbol(self):
        return self.symbol

    def get_name(self):
        return self.name

    def get_team(self):
        return self.team

    def __repr__(self):
        return self.symbol

    def __str__(self):
        return self.symbol


class Pawn:
    def __init__(self, team):
        self.team = team
        if team.lower() == "black":
            self.name = "B_Pawn"
            self.symbol = "♙"
        else:
            self.name = "W_Pawn"
            self.symbol = "♟"

    def get_symbol(self):
        return self.symbol

    def get_name(self):
        return self.name

    def get_team(self):
        return self.team

    def __repr__(self):
        return self.symbol

    def __str__(self):
        return self.symbol
