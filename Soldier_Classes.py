from Piece_Class import *


class King(Piece):
    def __init__(self, team):
        self.name = "King"
        super().__init__(name=self.name, team=team)

    @staticmethod
    def movement(x, y, new_x, new_y):
        # King can move 1 tile in any direction so the absolute delta of either x or y or both must be 1
        if abs(x - new_x) == 1 or abs(y - new_y) == 1:
            return True
        return False


class Queen(Piece):
    def __init__(self, team,):
        self.name = "Queen"
        super().__init__(name=self.name, team=team)

    @staticmethod
    def movement(x, y, new_x, new_y):
        # Queen can either move like a Bishop or a Rook so, it has to satisfy either condition
        # This is the Rook's condition
        if x == new_x or y == new_y:
            # Check that the piece has moved
            if x != new_x or y != new_y:
                return True
        else:
            # if the Rook's movement is not satisfied we  board: Board,check the Bishop's movement
            if abs((new_x - x) / (new_y - y)) == 1:
                return True
        return False


class Bishop(Piece):
    def __init__(self, team,):
        self.name = "Bishop"
        super().__init__(name=self.name, team=team)

    @staticmethod
    def movement(x, y, new_x, new_y):
        # Bishop moves like a function with the formula of y = mx where m = 1
        # so, we can use the formula m = y2 - y1 / x2 - x1
        try:
            if abs((new_x - x) / (new_y - y)) == 1:
                return True
        except ZeroDivisionError:
            pass
        return False


class Rook(Piece):
    def __init__(self, team):
        self.name = "Rook"
        super().__init__(name=self.name, team=team)

    @staticmethod
    def movement(x, y, new_x, new_y):
        # it can only move horizontally or vertically so either x or y have to stay the same
        if x == new_x or y == new_y:
            # Check that the piece has moved
            if x != new_x or y != new_y:
                return True
        return False


class Knight(Piece):
    def __init__(self, team):
        self.name = "Knight"
        super().__init__(name=self.name, team=team)

    @staticmethod
    def movement(x, y, new_x, new_y):
        # Knight can move 1 x tile and 2 y tiles at a time to all directions
        if abs(x - new_x) == 1 and abs(y - new_y) == 2:
            return True
        return False


class Pawn(Piece):
    def __init__(self, team):
        self.name = "Pawn"
        # Moved indexes if the Pawn moved already. Because only on its first move it can move 2 tiles a time
        self.moved = False
        super().__init__(name=self.name, team=team)

    def movement(self, x, y, new_x, new_y, ):
        # Pawn can move only in the y-axis in steps of 1 or 2
        if (abs(y - new_y) == 1 or (not self.moved and abs(y - new_y) == 2)) and x == new_x:
            return True
        return False
