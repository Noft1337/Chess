# Board class
# A simple 10x10 board
# My idea is to make it like a triple array that is built like (10,10,Piece)
# King, Queen, Bishop, Rook, Knight, Pawn.
import Soldier_Types
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
        self.board[7][num_by_letter('a')] = Soldier_Types.Rook(team=W)
        self.board[7][num_by_letter('b')] = Soldier_Types.Knight(team=W)
        self.board[7][num_by_letter('c')] = Soldier_Types.Bishop(team=W)
        self.board[7][num_by_letter('d')] = Soldier_Types.Queen(team=W)
        self.board[7][num_by_letter('e')] = Soldier_Types.King(team=W)
        self.board[7][num_by_letter('f')] = Soldier_Types.Bishop(team=W)
        self.board[7][num_by_letter('g')] = Soldier_Types.Knight(team=W)
        self.board[7][num_by_letter('h')] = Soldier_Types.Rook(team=W)
        for i in range(8):
            self.board[6][i] = Soldier_Types.Pawn(team=W)

        self.board[0][num_by_letter('a')] = Soldier_Types.Rook(team=B)
        self.board[0][num_by_letter('b')] = Soldier_Types.Knight(team=B)
        self.board[0][num_by_letter('c')] = Soldier_Types.Bishop(team=B)
        self.board[0][num_by_letter('d')] = Soldier_Types.Queen(team=B)
        self.board[0][num_by_letter('e')] = Soldier_Types.King(team=B)
        self.board[0][num_by_letter('f')] = Soldier_Types.Bishop(team=B)
        self.board[0][num_by_letter('g')] = Soldier_Types.Knight(team=B)
        self.board[0][num_by_letter('h')] = Soldier_Types.Rook(team=B)
        for i in range(8):
            self.board[1][i] = Soldier_Types.Pawn(team=B)

    def check_king(self, x, y):
        """
        Checks if the cell contains a king, because we can't eat a king
        :params x , y: coordinates in the board
        :return: True/False
        """

    def is_cell_moveable(self, x1, y1, x2, y2):
        """
        Checks if the cell in board[x][y] could be moved to
        :param x1: the first index of the current cell
        :param y1: the second index of the current cell
        :param x2: the first index of the wished cell
        :param y2: the second index of the wished cell
        :return: True/False
        """
        # todo: check if the cell is either empty/'kingless'/not containing a piece of the playing team
        if self.board[x2][y2] != EMPTY_SYMBOL:
            if self.board[x1][y1].get_team() != self.board[x2][y2].get_team():
                return False
        return True

    def player_move(self, move_from: list[str], move_to: list[str]):
        """
        Handles the player's move and checking if it is valid
        :param move_from: current cell the piece is in
        :param move_to: where the player wants the piece to move
        :return: True if Valid, False if not
        """
        x_from = int(self.letters.index(move_from[0]))
        # I reverse X and Y (opposite than math) because when it accesses a list it goes to Y first and X last
        y_from = 8 - (int(move_from[1]))
        # doing this because it's reversed since it's a list
        x_to = int(self.letters.index(move_to[0]))
        y_to = 8 - (int(move_to[1]))
        # ^ These are coordinates in the list
        if self.is_cell_moveable(y_from, x_from, y_to, x_to):
            self.board[y_to][x_to] = self.board[y_from][x_from]
            self.board[y_from][x_from] = '-'
            return True
        return False

    def __str__(self):
        """
        Responsible for the moment this class gets printed
        :return: The playing board formatted
        """
        f = 9
        top_row = [f'{self.letters[i]} ' for i in range(8)]
        final = '  ' + ''.join(top_row).upper() + '\n'
        for b in self.board:
            f -= 1
            final += f'{f} '
            for c in b:
                final += f'{str(c)} '
            final += '\n'
        return final
