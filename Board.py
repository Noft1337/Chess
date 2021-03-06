# Board class
# A simple 10x10 board
# My idea is to make it like a triple array that is built like (10,10,Piece)
# King, Queen, Bishop, Rook, Knight, Pawn.
import Piece_Class
import Soldier_Classes
# I import variables again because it couldn't find FINAL_MSG as is, I needed to refer to it as Variables.FINAL_MSG
import Variables
from Variables import *


def num_by_letter(letter: str):
    pass
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
        self.last_moved = (0, 0)
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

        self.pawns_moved = []

    def get_board(self):
        return self.board, self.w_king_coords, self.b_king_coords, self.pawns_moved, self.last_moved

    def retrue_first(self, pawn: Soldier_Classes.Pawn):
        """
        when we roll back if the last moved piece was a Pawn and, it was its first move we need to set Pawn.first to True
        """
        if self.board[self.last_moved[0]][self.last_moved[1]] == pawn:
            pawn.first = True

    def integrate_pawns(self, new_pawns: list):
        """
        when we roll back the board if pawns are getting moved back to its initial position
        we need to set Pawn.moved to False
        """
        different_pawns = list(set(self.pawns_moved) - set(new_pawns))
        for pawn in different_pawns:
            self.retrue_first(pawn)
            pawn.moved = False
        return new_pawns

    def set_board(self, set_to: tuple):
        self.board = set_to[0]
        self.w_king_coords = set_to[1]
        self.b_king_coords = set_to[2]
        self.last_moved = set_to[4]
        old_pawns_moved = self.integrate_pawns(set_to[3])
        self.pawns_moved = old_pawns_moved

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

    def clear_bishop(self, x1, y1, x2, y2):
        """
        makes sure that the bishop's way is clear until its target
        """
        if abs(x1 - x2) == 1 and abs(y1 - y2) == 1:
            # if we are moving only 1 tile we don't need to check if the way is clear.
            return True
        while x1 != x2 - 1:
            if x1 == x2 + 1:
                return True
            if x1 > x2:
                x1 -= 1
            else:
                x1 += 1
            if y1 > y2:
                y1 -= 1
            else:
                y1 += 1
            if self.board[x1][y1] != EMPTY_SYMBOL:
                return False
        return True

    def iterate_rook(self, v1, v2, z, opposite=False):
        iteration = 0
        while v1 != v2 - 1:
            if v1 == v2 + 1:
                return True
            iteration += 1
            if v1 > v2:
                v1 -= 1
            else:
                v1 += 1
            if not opposite:
                if self.board[v1][z] != EMPTY_SYMBOL:
                    return False
            else:
                if self.board[z][v1] != EMPTY_SYMBOL:
                    return False
        return True

    def clear_rook(self, x1, y1, x2, y2):
        """
        makes sure that the rook's way is clear until its target
        """
        if (y1 == y2 and abs(x1 - x2) == 1) or (x1 == x2 and abs(y1 - y2) == 1):
            # if we are moving only 1 tile we don't need to check if the way is clear.
            return True
        iteration = 0
        if y1 == y2:
            return self.iterate_rook(x1, x2, y1)
        elif x1 == x2:
            return self.iterate_rook(y1, y2, x1, opposite=True)
        else:
            return False

    def clear_way(self, x1, y1, x2, y2):
        if isinstance(self.board[x1][y1], Soldier_Classes.Rook):
            if self.clear_rook(x1, y1, x2, y2):
                return True
            return False
        elif isinstance(self.board[x1][y1], Soldier_Classes.Bishop):
            if self.clear_bishop(x1, y1, x2, y2):
                return True
            return False
        elif isinstance(self.board[x1][y1], Soldier_Classes.Queen):
            if self.clear_rook(x1, y1, x2, y2) or self.clear_bishop(x1, y1, x2, y2):
                return True
            return False
        return True

    def threatened(self, x, y, team, p=True):
        # this function is the same as main.check_whole_board(), but I couldn't import it due to circular import.
        for i in range(8):
            for j in range(8):
                if isinstance(self.board[i][j], Piece_Class.Piece):
                    if self.board[i][j].get_team() != team:
                        if self.board[i][j].movement(i, j, x, y) and self.clear_way(i, j, x, y):
                            if p:
                                Variables.FINAL_MSG += f"{Colors.GREEN} \
                                      {self.board[i][j]} ({letter_by_num(j)}{8 - i}) Threatens King in \
                                      {letter_by_num(9 - y)}{8 - x}! \
                                      {Colors.END}"
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

    def add_to_pawns(self, x, y):
        if isinstance(self.board[x][y], Soldier_Classes.Pawn):
            self.pawns_moved.append(self.board[x][y])

    def eat(self, y_from, x_from, y_to, x_to):
        self.add_to_pawns(y_from, x_from)
        self.board[y_to][x_to] = self.board[y_from][x_from]
        self.board[y_from][x_from] = EMPTY_SYMBOL
        self.update_last_moved(y_to, x_to)

    def check_castling_threats(self, y_from, x_from, y_to, x_to, team):
        """
        When Castling we can't move it if it's going to be threatened or if it is already checked,
        this function is here to cover these conditions
        """
        if abs(x_from - x_to) == 2 and y_from == y_to:
            if self.threatened(y_to, x_to, team, p=False):
                # Check if it is going to be threatened
                Variables.FINAL_MSG += THREAT_CASTLE % (letter_by_num(y_to) + str(8 - x_to))
                return True
            elif self.threatened(y_from, x_from, team, p=False):
                # Check if it is checked
                Variables.FINAL_MSG += CHECKED_CASTLE
                return True
        return True

    def team_castling(self, y_from, x_from, y_to, x_to, team):
        if team == "White":
            y = 7
        else:
            y = 0
        # Check that the king is in its position
        if y_from == y and x_from == 4:
            if x_from < x_to:
                # Handle King's side
                x = 7
            else:
                # Queen's side
                x = 0
            # Check that rook is in its position
            if isinstance(self.board[y][x], Soldier_Classes.Rook):
                # Make sure nothing is in the way
                if self.clear_way(y, x, y, 5) or self.clear_way(y, x, y, 3):
                    # Do the actual Castling
                    # Move King
                    self.eat(y_from, x_from, y_to, x_to)
                    # Move Rook
                    self.eat(y, x, y, abs(x - 2))
                    return True
        return False

    def is_castling(self, y_from, x_from, y_to, x_to):
        # we can castle only from king's original position as far as I know
        if isinstance(self.board[y_from][x_from], Soldier_Classes.King):
            team = self.board[y_from][x_from].get_team()
            # Make sure the movement is all right
            if self.check_castling_threats(y_from, x_from, y_to, x_to, team):
                if self.team_castling(y_from, x_from, y_to, x_to, team):
                    return True
        return False

    def is_en_passant(self, y_from, x_from, y_to, x_to):
        if isinstance(self.board[y_from][x_from], Soldier_Classes.Pawn) and \
                isinstance(self.board[y_from][x_to], Soldier_Classes.Pawn):
            if self.board[y_from][x_to].get_team() != self.board[y_from][x_from].get_team():
                if self.board[y_from][x_to].first:
                    self.board[y_to][x_to] = self.board[y_from][x_from]
                    self.board[y_from][x_to] = EMPTY_SYMBOL
                    return True
        return False

    def is_pawn_passing(self, y_from, x_from, y_to, x_to):
        if isinstance(self.board[y_from][x_from], Soldier_Classes.Pawn) and \
                isinstance(self.board[y_to][x_to], Soldier_Classes.Pawn):
            if self.board[y_from][x_from].movement(x_from, y_from, x_to, y_to, catch=True):
                return True
        return False

    def update_last_moved(self, x, y):
        if isinstance(self.board[self.last_moved[0]][self.last_moved[1]], Soldier_Classes.Pawn):
            self.board[self.last_moved[0]][self.last_moved[1]].first = False
        self.last_moved = (x, y)

    def player_move(self, move_from: list, move_to: list, test_move=False):
        """
        Handles the player's move and checking if it is valid
        :param move_from: current cell the piece is in
        :param move_to: where the player wants the piece to move
        :param test_move: if we want to check if it's a valid move we need to check it with this function but without
        actually moving pieces
        :return: True if Valid, False if not
        """
        # Defining the coordinates of the cells
        if move_from == move_to:
            return False
        x_from = move_from[0]
        y_from = move_from[1]
        x_to = move_to[0]
        y_to = move_to[1]
        if test_move:
            pass
        # Check that we can move to the cell
        if self.is_cell_moveable(y_from, x_from, y_to, x_to):
            # Check that the move is according to the piece movement method
            if self.board[y_from][x_from].movement(x_from, y_from, x_to, y_to):
                # Checking the way is clear
                if self.clear_way(y_from, x_from, y_to, x_to):
                    if isinstance(self.board[y_from][x_from], Soldier_Classes.King):
                        if not test_move:
                            if self.threatened(y_to, x_to, self.board[y_from][x_from].get_team()):
                                return False
                    else:
                        if self.is_king_left_threatened(y_from, x_from):
                            return False
                    if not test_move:
                        self.eat(y_from, x_from, y_to, x_to)
                        if isinstance(self.board[y_to][x_to], Soldier_Classes.King):
                            self.update_kings(y_to, x_to)
                    return True
            else:
                if self.is_pawn_passing(y_from, x_from, y_to, x_to):
                    self.eat(y_from, x_from, y_to, x_to)
                    return True
                elif self.is_en_passant(y_from, x_from, y_to, x_to):
                    self.eat(y_from, x_from, y_to, x_to)
                    return True
                elif self.is_castling(y_from, x_from, y_to, x_to):
                    return True
        return False

    def __getitem__(self, item: list):
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
