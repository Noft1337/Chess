from Board import Board


class Previous(object):

    def __init__(self, board: Board):
        self.boards = [board]
        self.turn = 0

    def add_board(self, board: Board):
        self.boards.append(board)
        self.turn += 1

    def roll_back(self, how_many: int):
        rolled_board = self.boards[-how_many]
        self.boards = self.boards[::-(how_many + 1)]
        return rolled_board

