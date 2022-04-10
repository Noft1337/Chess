# Board class
# A simple 10x10 board
# My idea is to make it like a triple array that is built like (10,10,Piece)
# King, Queen, Bishop, Rook, Knight, Pawn
import Piece
import Soldier_Types

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
        self.board = [['-' for i in range(8)] for i in range(8)]

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
        return True

    def player_move(self, move_from: list[str], move_to: list[str]):
        """
        Handles the player's move and checking if it is valid
        :param move_from: current cell the piece is in
        :param move_to: where the player wants the piece to move
        :return: True if Valid, False if not
        """
        a_from = int(self.letters.index(move_from[0]))
        b_from = int(move_from[1])
        a_to = int(self.letters.index(move_to[0]))
        b_to = int(move_to[1])
        # ^ These are coordinates in the list
        if self.is_cell_moveable(a_from, b_from, a_to, b_to):
            self.board[a_to][b_to] = self.board[a_from][b_from]
            self.board[a_from][b_from] = '-'
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
