import Piece_Class
from Board import Board
from Variables import *
import Soldier_Classes
# By Michael

TURNS = {0: "White", 1: "Black"}


def check_correct_team_move(board: Board, cell: list[int, int], turn: int):
    return board[[cell[1], cell[0]]].get_team() == TURNS[turn % 2]


def get_kings_cords(board: Board, team: str = "White" or "Black"):
    for i in range(8):
        for j in range(8):
             if type(board.board[i][j]) is Soldier_Classes.King:
                 if board.board[i][j].get_team() == team:
                    return [i, j]


def is_check(board: Board, coords: list, king: Soldier_Classes.King):
    try:
        x, y = king.get_cords()
    except AttributeError:
        print("Attribute Errored")
    if isinstance(board.board[coords[0]][coords[1]], Piece_Class.Piece):
        return board.board[coords[0]][coords[1]].movement(x, y)


def handle_input(move: list):
    """
    Just taking the user input and making it workable as a list index
    :returns A list with the values in it, False if it fails because of input
    """
    move[0] = int(LETTERS.index(move[0].upper()))
    move[1] = 8 - (int(move[1]))
    return move


def player_move(board: Board, king: Soldier_Classes.King, turn: int):
    """
    handles all of the functions that happen when a player move is being made,
    checking that the move is valid
    checking that the piece that is trying to be moved belongs to the playing team
    checking if a check, mate or a pat is true after the move
    :param board: The playing board
    :param king: the opposing team's king piece
    :param turn: what turn we're on
    """
    valid = False
    while not valid:
        try:
            play = input("Move: ")
            play = play.split(" ")
            move_from = handle_input(list(play[0]))
            if not check_correct_team_move(board, move_from, turn):
                print(TEAM_ERROR)
            else:
                move_to = handle_input(list(play[2]))
                if not move_to or not move_from:
                    # meaning that the function handle_input() got bad input so, we need to
                    print(SYNTAX_ERROR)
                else:
                    if not board.player_move(move_from, move_to):
                        print(MOVEMENT_ERROR)
                    else:
                        valid = True
                        # todo: we need to check if it's a check, if it is check also if its a mate.
                        #  If neither then it might be a pat
                        # Since we moved the piece to the target tile,
                        # we need to check if the other king is withing the Piece's reach
                        if is_check(board, move_to, king):
                            print("Check!")
        except (TypeError, ValueError, IndexError, AttributeError) as e:
            # Handles bad user input
            if type(e) is AttributeError:
                print(MOVEMENT_ERROR)
            else:
                print(SYNTAX_ERROR)


def main():
    playing_board = Board()
    turn = 0
    while True:
        print(playing_board)
        print(WHOS_PLAYING.format(TURNS[turn % 2]))
        w_king_cords = get_kings_cords(playing_board, TURNS[0])
        b_king_cords = get_kings_cords(playing_board, TURNS[1])
        if TURNS[turn % 2] == "White":
            target_king = playing_board[b_king_cords]
        else:
            target_king = playing_board[w_king_cords]
        player_move(playing_board, target_king, turn)
        turn += 1


if __name__ == '__main__':
    main()
