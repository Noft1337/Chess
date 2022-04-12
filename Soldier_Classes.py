from Piece_Class import *


class King(Piece):
    def __init__(self, team, x, y):
        self.name = "King"
        super().__init__(name=self.name, team=team, x=x, y=y)

    def movement(self, new_x, new_y):
        # King can move 1 tile in any direction so the absolute delta of either x or y or both must be 1
        if abs(self.x - new_x) == 1 or abs(self.y - new_y) == 1:
            self.x = new_x
            self.y = new_y
            return True
        return False


class Queen(Piece):
    def __init__(self, team, x, y):
        self.name = "Queen"
        super().__init__(name=self.name, team=team, x=x, y=y)

    def movement(self, new_x, new_y):
        # Queen can either move like a Bishop or a Rook so, it has to satisfy either condition
        # This is the Rook's condition
        if self.x == new_x or self.y == new_y:
            # Check that the piece has moved
            if self.x != new_x or self.y != new_y:
                self.x = new_x
                self.y = new_y
                return True
        else:
            # if the Rook's movement is not satisfied we check the Bishop's movement
            if abs((new_x - self.x) / (new_y - self.y)) == 1:
                self.x = new_x
                self.y = new_y
                return True
        return False


class Bishop(Piece):
    def __init__(self, team, x, y):
        self.name = "Bishop"
        super().__init__(name=self.name, team=team, x=x, y=y)

    def movement(self, new_x, new_y):
        # Bishop moves like a function with the formula of y = mx where m = 1
        # so, we can use the formula m = y2 - y1 / x2 - x1
        try:
            if abs((new_x - self.x) / (new_y - self.y)) == 1:
                self.x = new_x
                self.y = new_y
                return True
        except ZeroDivisionError:
            pass
        return False


class Rook(Piece):
    def __init__(self, team, x, y):
        self.name = "Rook"
        super().__init__(name=self.name, team=team, x=x, y=y)

    def movement(self, new_x, new_y):
        # it can only move horizontally or vertically so either x or y have to stay the same
        if self.x == new_x or self.y == new_y:
            # Check that the piece has moved
            if self.x != new_x or self.y != new_y:
                self.x = new_x
                self.y = new_y
                return True
        return False


class Knight(Piece):
    def __init__(self, team, x, y):
        self.name = "Knight"
        super().__init__(name=self.name, team=team, x=x, y=y)

    def movement(self, new_x, new_y):
        # Knight can move 1 x tile and 2 y tiles at a time to all directions
        if abs(self.x - new_x) == 1 and abs(self.y - new_y) == 2:
            self.x = new_x
            self.y = new_y
            return True
        return False


class Pawn(Piece):
    def __init__(self, team, x, y):
        self.name = "Pawn"
        super().__init__(name=self.name, team=team, x=x, y=y)

    def movement(self, new_x, new_y):
        # Pawn can move only in the y-axis in steps of 1 or 2
        if abs(self.y - new_y) == 1 or abs(self.y - new_y) == 2:
            self.y = new_y
            return True
        return False
