from Board import Board
from Variables import *


class Previous(object):

    def __init__(self, board: Board):
        self.boards = [self.set_board_by_running(board.get_board())]
        self.turn = 0

    @staticmethod
    def set_board_by_running(to_append):
        """
        We need to manually set our lists to be equal to all the values we get from board
        Because, if we save it as is, as long as it inherits from Board class it will automatically update
        If that makes any sense
        :param to_append: board, w_king_coords, b_king_coords, pawns_moved, last_moved
        :return: manually set lists inside a tuple
        """
        final_board = [[EMPTY_SYMBOL for i in range(8)] for i in range(8)]
        board = to_append[0]
        for i in range(8):
            for j in range(8):
                final_board[i][j] = board[i][j]
        pawns_moved = []
        for i in range(len(to_append[3])):
            pawns_moved.append(to_append[3][i])
        w_king = (to_append[1][0], to_append[1][1])
        b_king = (to_append[2][0], to_append[2][1])
        last_moved = (to_append[4][0], to_append[4][1])
        return final_board, w_king, b_king, pawns_moved, last_moved

    def add_board(self, board: Board):
        to_append = self.set_board_by_running(board.get_board())
        self.boards.append(to_append)
        self.turn += 1

    def roll_back(self, how_many: int, board: Board):
        rolled_board = self.boards[-how_many - 1]
        self.boards = self.boards[::-(how_many + 1)]
        board.set_board(rolled_board)
        self.turn -= how_many
        return board, self.turn

