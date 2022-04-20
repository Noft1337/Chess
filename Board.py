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

def letter_by_num(num: int):
    letters = list('ABCDEFGH')
    return letters[num - 1]


class Board(object):
    def __init__(self):
        """
        Initializes a blank playing board with all the pieces in place
        """
        self.board = [[EMPTY_SYMBOL for i in range(8)] for i in range(8)]

        # I believe there's a prettier way to do this but couldn't think of one...
        # Sets the white side of the board
        self.board[7][num_by_letter('a')] = Soldier_Classes.Rook(team=W)
        self.board[7][num_by_letter('b')] = Soldier_Classes.Knight(team=W)
        self.board[7][num_by_letter('c')] = Soldier_Classes.Bishop(team=W)
        self.board[7][num_by_letter('d')] = Soldier_Classes.Queen(team=W)
        self.board[7][num_by_letter('e')] = Soldier_Classes.King(team=W)
        self.board[7][num_by_letter('f')] = Soldier_Classes.Bishop(team=W)
        self.board[7][num_by_letter('g')] = Soldier_Classes.Knight(team=W)
        self.board[7][num_by_letter('h')] = Soldier_Classes.Rook(team=W)
        for i in range(8):
            self.board[6][i] = Soldier_Classes.Pawn(team=W)
        # Sets the black side of the board
        self.board[0][num_by_letter('a')] = Soldier_Classes.Rook(team=B)
        self.board[0][num_by_letter('b')] = Soldier_Classes.Knight(team=B)
        self.board[0][num_by_letter('c')] = Soldier_Classes.Bishop(team=B)
        self.board[0][num_by_letter('d')] = Soldier_Classes.Queen(team=B)
        self.board[0][num_by_letter('e')] = Soldier_Classes.King(team=B)
        self.board[0][num_by_letter('f')] = Soldier_Classes.Bishop(team=B)
        self.board[0][num_by_letter('g')] = Soldier_Classes.Knight(team=B)
        self.board[0][num_by_letter('h')] = Soldier_Classes.Rook(team=B)
        for i in range(8):
            self.board[1][i] = Soldier_Classes.Pawn(team=B)

        self.w_king_coords = (7, 4)
        self.b_king_coords = (0, 4)

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
        if isinstance(self.board[x1][y1], Piece_Class.Piece) is True:
            # A player can't eat its own Piece or a King
            try:
                if self.board[x1][y1].get_team() == self.board[x2][y2].get_team() or self.check_king(x2, y2):
                    return False
            except (AttributeError, IndexError):
                # we might get this since there might not be a piece in the target cell
                # so, it will try to call get_team() on a str
                # in that case we know that the cell is empty so, we just need to verify it's not a king
                if self.check_king(x2, y2):
                    return False
            return True
        return False

    def get_king_coords(self, team=W or B):
        if team == W:
            return self.w_king_coords
        else:
            return self.b_king_coords

    def update_kings(self, x, y):
        if self.board[x][y].get_team() == B:
            self.b_king_coords = (x, y)
        else:
            self.w_king_coords = (x, y)

    def clear_bishop(self, x1, y1, x2, y2, test=False):
        while x1 != x2:
            if x1 > x2:
                x1 -= 1
            else:
                x1 += 1
            if y1 > y2:
                y1 -= 1
            else:
                y1 += 1
            if self.board[x1][y1] != EMPTY_SYMBOL:
                if not test:
                    print(BLOCKED_WAY)
                return False
        return False

    def clear_rook(self, x1, y1, x2, y2, test=False):
        if x1 != x2:
            while x1 != x2:
                if x1 > x2:
                    x1 -= 1
                else:
                    x1 += 1
                if self.board[x1][y1] != EMPTY_SYMBOL:
                    if not test:
                        print(BLOCKED_WAY)
                    return False
        else:
            while y1 != y2:
                if y1 > y2:
                    y1 -= 1
                else:
                    y1 += 1
                if self.board[x1][y1] != EMPTY_SYMBOL:
                    if not test:
                        print(BLOCKED_WAY)
                    return False
            pass

    def clear_way(self, x1, y1, x2, y2, test=False):
        if isinstance(self.board[x1][y1], Soldier_Classes.Rook):
            if self.clear_rook(x1, y1, x2, y2, test):
                return True
            return False
        elif isinstance(self.board[x1][y1], Soldier_Classes.Bishop):
            if self.clear_bishop(x1, y1, x2, y2, test):
                return True
            return False
        elif isinstance(self.board[x1][y1], Soldier_Classes.Bishop):
            if self.clear_bishop(x1, y1, x2, y2, test) or self.clear_rook(x1, y1, x2, y2, test):
                return True
            return False
        return True

    def threatened(self, x, y, team):
        # this function is the same as main.check_whole_board(), but I couldn't import it due to circular import.
        for i in range(8):
            for j in range(8):
                if isinstance(self.board[i][j], Piece_Class.Piece):
                    if self.board[i][j].get_team() != team:
                        if self.board[i][j].movement(i, j, x, y) and self.clear_way(i, j, x, y):
                            print(f"{Colors.GREEN}"
                                  f"{self.board[i][j]} ({letter_by_num(j)}{8 - i}) Threatens King in "
                                  f"{letter_by_num(9 - y)}{8 - x}!"
                                  f"{Colors.END}")
                            return True
        return False

    def is_king_left_threatened(self, x_from, y_from):
        piece = self.board[x_from][y_from]
        team = self.board[x_from][y_from].get_team()
        self.board[x_from][y_from] = EMPTY_SYMBOL
        if team == B:
            k_x, k_y = self.b_king_coords
        else:
            k_x, k_y = self.w_king_coords
        try:
            if self.threatened(k_x, k_y, team):
                return True
            return False
        finally:
            # In the end we want the piece back to its position.
            self.board[x_from][y_from] = piece

    def player_move(self, move_from: list[int, int], move_to: list[int, int], test_move=False):
        """
        Handles the player's move and checking if it is valid
        :param move_from: current cell the piece is in
        :param move_to: where the player wants the piece to move
        :param test_move: if we want to check if it's a checkmate, we need to see where e king can be moved without
        actually moving it
        :return: True if Valid, False if not
        """
        # Defining the coordinates of the cells
        x_from = move_from[0]
        y_from = move_from[1]
        x_to = move_to[0]
        y_to = move_to[1]
        # Check that we can move to the cell
        if self.is_cell_moveable(y_from, x_from, y_to, x_to):
            # Check that the move is according to the piece movement method
            if self.board[y_from][x_from].movement(x_from, y_from, x_to, y_to):
                # Checking the way is clear
                if self.clear_way(y_from, x_from, y_to, x_to, test_move):
                    if isinstance(self.board[y_from][x_from], Soldier_Classes.King):
                        if not test_move:
                            if self.threatened(y_to, x_to, self.board[y_from][x_from].get_team()):
                                return False
                    else:
                        if self.is_king_left_threatened(y_from, x_from):
                            return False
                    if not test_move:
                        if isinstance(self.board[y_from][x_from], Soldier_Classes.Pawn) and \
                                not self.board[y_from][x_from].moved:
                            self.board[y_from][x_from].moved = True
                        self.board[y_to][x_to] = self.board[y_from][x_from]
                        self.board[y_from][x_from] = EMPTY_SYMBOL
                        if isinstance(self.board[y_to][x_to], Soldier_Classes.King):
                            self.update_kings(y_to, x_to)
                    return True
            else:
                # todo: check for special moves, since they do not satisfy the piece's movement condition
                pass
        return False

    def __getitem__(self, item: list[int]):
        return self.board[item[0]][item[1]]

    def __str__(self):
        """
        Responsible for the moment this class gets printed
        :return: The playing board formatted
        """
        f = 9
        letters_row = [f'{LETTERS[i]} ' for i in range(8)]
        final = '\t' + '\t'.join(letters_row).upper() + '\n'
        for b in self.board:
            f -= 1
            final += f'{f}\t'
            for c in b:
                final += f'{str(c)}\t'
            final += f'{f}'
            final += '\n'
        final += '\t' + '\t'.join(letters_row).upper()
        return final
