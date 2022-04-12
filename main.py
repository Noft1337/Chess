from Board import Board
from Variables import *
import Piece_Class
import Soldier_Classes
# By Michael

TURNS = {0: "White", 1: "Black"}


def get_kings_cords(board: Board, team: str = "White" or "Black"):
    for i in range(8):
        for j in range(8):
             if type(board.board[i][j]) is Soldier_Classes.King:
                 if board.board[i][j].get_team() == team:
                    return [i, j]


def handle_input(move: list):
    """
    Just taking the user input and making it workable as a list index
    """
    move[0] = int(LETTERS.index(move[0].upper()))
    move[1] = 8 - (int(move[1]))
    return move


def player_move(board: Board):
    play = input("Move: ")
    try:
        play = play.split(" ")
        move_from = handle_input(list(play[0]))
        move_to = handle_input(list(play[2]))
        if not board.player_move(move_from, move_to):
            print(MOVEMENT_ERROR)
        else:
            # todo: we need to check if it's a check, if it is check also if its a mate.
            #  If neither then it might be a pat
            pass
    except IndexError or TypeError:
        # Handles bad user input
        print(SYNTAX_ERROR)


def main():
    playing_board = Board()
    w_king_cords = get_kings_cords(playing_board, TURNS[0])
    b_king_cords = get_kings_cords(playing_board, TURNS[1])
    turn = 0
    while True:
        print(playing_board)
        player_move(playing_board)
        turn += 1


if __name__ == '__main__':
    main()
