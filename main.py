from Board import Board
from Variables import *
import Piece_Class
import Soldier_Classes
# By Michael


def player_move(board: Board):
    play = input("Move: ")
    try:
        play = play.split(" ")
        move_from = list(play[0])
        move_to = list(play[2])
        if not board.player_move(move_from, move_to):
            print(MOVEMENT_ERROR)
    except IndexError or TypeError:
        # Handles bad user input
        print(SYNTAX_ERROR)


def main():
    playing_board = Board()
    while True:
        print(playing_board)
        player_move(playing_board)


if __name__ == '__main__':
    main()
