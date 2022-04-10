from Board import Board
from Variables import *
import Piece
import Soldier_Types


def player_move(board: Board):
    play = input("Move: ")
    try:
        play = play.split(" ")
        move_from = list(play[0])
        to = list(play[2])
    except IndexError or TypeError:
        # Handles bad user input
        print(SYNTAX_ERROR)


def main():
    playing_board = Board()
    print(playing_board)
    player_move(playing_board)


if __name__ == '__main__':
    main()
