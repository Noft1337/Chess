# Board class
# A simple 10x10 board
# My idea is to make it like a triple array that is built like (10,10,Piece)
# King, Queen, Bishop, Rook, Knight, Pawn.
import Piece_Class
import Soldier_Classes
from Variables import *

W = 'White'
B = 'Black'


def num_by_letter(letter: str):
    letters = list('ABCDEFGH')
    return letters.index(letter.upper())


class Board(object):
    def __init__(self):
        """
        Initializes a blank playing board
        """
        self.letters = list('ABCDEFGH')
        self.board = [[EMPTY_SYMBOL for i in range(8)] for i in range(8)]

        # Sets the white side of the board
        self.board[7][num_by_letter('a')] = Soldier_Classes.Rook(team=W, y=7, x=num_by_letter('a'))
        self.board[7][num_by_letter('b')] = Soldier_Classes.Knight(team=W, y=7, x=num_by_letter('b'))
        self.board[7][num_by_letter('c')] = Soldier_Classes.Bishop(team=W, y=7, x=num_by_letter('c'))
        self.board[7][num_by_letter('d')] = Soldier_Classes.Queen(team=W, y=7, x=num_by_letter('d'))
        self.board[7][num_by_letter('e')] = Soldier_Classes.King(team=W, y=7, x=num_by_letter('e'))
        self.board[7][num_by_letter('f')] = Soldier_Classes.Bishop(team=W, y=7, x=num_by_letter('f'))
        self.board[7][num_by_letter('g')] = Soldier_Classes.Knight(team=W, y=7, x=num_by_letter('g'))
        self.board[7][num_by_letter('h')] = Soldier_Classes.Rook(team=W, y=7, x=num_by_letter('h'))
        for i in range(8):
            self.board[6][i] = Soldier_Classes.Pawn(team=W, y=6, x=i)
        # Sets the black side of the board
        self.board[0][num_by_letter('a')] = Soldier_Classes.Rook(team=B, y=0, x=num_by_letter('a'))
        self.board[0][num_by_letter('b')] = Soldier_Classes.Knight(team=B, y=0, x=num_by_letter('b'))
        self.board[0][num_by_letter('c')] = Soldier_Classes.Bishop(team=B, y=0, x=num_by_letter('c'))
        self.board[0][num_by_letter('d')] = Soldier_Classes.Queen(team=B, y=0, x=num_by_letter('d'))
        self.board[0][num_by_letter('e')] = Soldier_Classes.King(team=B, y=0, x=num_by_letter('e'))
        self.board[0][num_by_letter('f')] = Soldier_Classes.Bishop(team=B, y=0, x=num_by_letter('f'))
        self.board[0][num_by_letter('g')] = Soldier_Classes.Knight(team=B, y=0, x=num_by_letter('g'))
        self.board[0][num_by_letter('h')] = Soldier_Classes.Rook(team=B, y=0, x=num_by_letter('h'))
        for i in range(8):
            self.board[1][i] = Soldier_Classes.Pawn(team=B, y=1, x=i)

    def check_king(self, x, y):
        """
        Checks if the cell contains a king, because we can't eat a king
        :params x , y: coordinates in the board
        :return: True/False
        """
        return isinstance(self.board[x][y], Soldier_Classes.King)

    def is_cell_moveable(self, x1, y1, x2, y2):
        """
        Checks if the cell in board[x][y] could be moved to
        :param x1: the first index of the current cell
        :param y1: the second index of the current cell
        :param x2: the first index of the wished cell
        :param y2: the second index of the wished cell
        :return: True/False
        """
        # Make sure a cell contains a Chess Piece
        if isinstance(self.board[x1][y1], Piece_Class.Piece):
            # A player can't eat its own Piece or a King
            try:
                if self.board[x1][y1].get_team() == self.board[x2][y2].get_team() or self.check_king(x2, y2):
                    return False
            except AttributeError:
                # we might get this since there might not be a piece in the target cell
                # so, it will try to call get_team() on a str
                # in that case we know that the cell is empty so, we just need to verify it's not a king
                if self.check_king(x2, y2):
                    return False
            return True
        return False

    def player_move(self, move_from: list[str], move_to: list[str]):
        """
        Handles the player's move and checking if it is valid
        :param move_from: current cell the piece is in
        :param move_to: where the player wants the piece to move
        :return: True if Valid, False if not
        """
        # Defining the coordinates of the cells
        x_from = int(self.letters.index(move_from[0].upper()))
        # I'm reversing X and Y (opposite than math) because when it accesses a list it goes to Y first and X last
        y_from = 8 - (int(move_from[1]))
        # doing this because it's reversed since it's a list
        x_to = int(self.letters.index(move_to[0].upper()))
        y_to = 8 - (int(move_to[1]))
        # Check that we can move to the cell
        if self.is_cell_moveable(y_from, x_from, y_to, x_to):
            # Check that the move is according to the piece movement method
            if self.board[y_from][x_from].movement(x_to, y_to):
                self.board[y_to][x_to] = self.board[y_from][x_from]
                self.board[y_from][x_from] = EMPTY_SYMBOL
                return True
        return False

    def __str__(self):
        """
        Responsible for the moment this class gets printed
        :return: The playing board formatted
        """
        f = 9
        letters_row = [f'{self.letters[i]} ' for i in range(8)]
        final = '  ' + ''.join(letters_row).upper() + '\n'
        for b in self.board:
            f -= 1
            final += f'{f} '
            for c in b:
                final += f'{str(c)} '
            final += '\n'
        final += '  ' + ''.join(letters_row).upper()
        return final
