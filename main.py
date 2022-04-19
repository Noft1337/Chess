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


def get_opposite_team(piece: Piece_Class.Piece):
    target_team = piece.get_team()
    if target_team == "Black":
        team = "White"
    else:
        team = "Black"
    return team


def get_tiles(board: Board, king: Soldier_Classes.King):
    k_x, k_y = list(king.get_cords())[::-1]
    final_tiles = []
    xs = [k_x - 1, k_x, k_x + 1]
    ys = [k_y - 1, k_y, k_y + 1]
    for x in xs:
        for y in ys:
            # make sure we don't get values outside our playing board
            if (0 < x < 8) and (0 < y < 8):
                if board.player_move([k_y, k_x], [y, x], test=True):
                    final_tiles.append([x, y])
    return final_tiles


def check_whole_board(board: Board, target_coords: list, opposite_team="White" or "Black"):
    """
    Checking each cell on the board if it's a Piece and if it's the opposing team of the king
    Then checking if it can reach the desired tile, meaning king can't escape there
    """
    for i in range(8):
        for j in range(8):
            if isinstance(board[[i, j]], Piece_Class.Piece):
                if board[[i, j]].get_team() == opposite_team:
                    if board.player_move([j, i], target_coords[::-1], test=True):
                        return True
    return False


def is_mate(board: Board, king: Soldier_Classes.King):
    # We first need to get all the tiles King can escape to.
    check = False
    king_escapes = get_tiles(board, king)
    opposite_team = get_opposite_team(king)
    for escape in king_escapes:
        # Now we check each escape if it can be checked by some Piece.
        # If it can be checked it means king could not escape there since it will be eaten
        check = check_whole_board(board, escape, opposite_team)
        if not check:
            return False
    if not check:
        return False
    return True


def handle_check(board: Board, king: Soldier_Classes.King):
    mate = is_mate(board, king)
    if mate:
        print(f"{board}\n{CHECKMATE % get_opposite_team(king)}")
    else:
        print(CHECK)
    return mate


def is_check(board: Board, coords: list, king: Soldier_Classes.King, other_coords=None):
    x, y = king.get_cords()
    if isinstance(board[coords[::-1]], Piece_Class.Piece):
        # return board.player_move(coords, [y, x])
        return board[coords[::-1]].movement(x, y)


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
    mate = False
    valid = False
    while not valid:
        try:
            play = input("Move: ")
            play = play.split(" ")
            move_from = handle_input(list(play[0]))
            if not check_correct_team_move(board, move_from, turn):
                print(TEAM_ERROR)
            else:
                if play[1] == "to":
                    play[1] = play[2]
                move_to = handle_input(list(play[1]))
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
                            board[move_to[::-1]].team = get_opposite_team(king)
                            mate = handle_check(board, king)
        except (ValueError, IndexError, AttributeError) as e:
            # Handles bad user input
            if type(e) is AttributeError:
                print(MOVEMENT_ERROR)
            else:
                print(SYNTAX_ERROR)
        finally:
            if valid:
                return mate


def main():
    playing_board = Board()
    turn = 0
    mate = False
    while not mate:
        print(playing_board)
        print(WHOS_PLAYING % TURNS[turn % 2])
        w_king_cords = get_kings_cords(playing_board, TURNS[0])
        b_king_cords = get_kings_cords(playing_board, TURNS[1])
        if TURNS[turn % 2] == "White":
            target_king = playing_board[b_king_cords]
        else:
            target_king = playing_board[w_king_cords]
        mate = player_move(playing_board, target_king, turn)
        turn += 1


if __name__ == '__main__':
    main()
