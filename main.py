import socket
import Piece_Class
from Board import Board
from locations import *
from Previous_Boards import Previous
import Soldier_Classes

TURNS = {0: W, 1: B}


def check_correct_team_move(board: Board, cell: list, turn: int):
    return board[cell[::-1]].get_team() == TURNS[turn % 2]


def get_kings_cords(board: Board, team: str = W or B):
    return board.get_king_coords(team)


def get_opposite_team(piece: Piece_Class.Piece):
    target_team = piece.get_team()
    if target_team == B:
        team = W
    else:
        team = B
    return team


def get_tiles(board: Board, king: Soldier_Classes.King):
    k_x, k_y = list(board.get_king_coords(king.get_team()))[::-1]
    final_tiles = []
    xs = [k_x - 1, k_x, k_x + 1]
    ys = [k_y - 1, k_y, k_y + 1]
    for x in xs:
        for y in ys:
            # make sure we don't get values outside our playing board
            if (0 <= x < 8) and (0 <= y < 8):
                if board.player_move([k_x, k_y], [x, y], test_move=True):
                    final_tiles.append([x, y])
    return final_tiles


def check_whole_board(board: Board, target_coords: list, opposite_team, loc: Locations):
    """
    Checking each cell on the board if it's a Piece and if it's the opposing team of the king
    Then checking if it can reach the desired tile, meaning king can't escape there
    """
    x = target_coords[0]
    y = target_coords[1]
    pieces = loc.get_team_locations(opposite_team)
    for piece in pieces:
        if board.player_move(piece[::-1], [x, y], test_move=True):
            print("piece: {}\ncords:{}\nto: {}\nreach: {}".format(board[piece], piece, (y, x), board[piece].movement(piece[0], piece[1], y, x)))
            loc.add_to_maters(piece)
            return True
    return False


def is_mate(board: Board, king: Soldier_Classes.King, loc: Locations):
    # We first need to get all the tiles King can escape to.
    check = False
    king_escapes = get_tiles(board, king)
    opposite_team = get_opposite_team(king)
    # Since we don't want past mate checks' pieces to be in the list twe need to reset it each time
    if king_escapes:
        loc.reset_maters()
    for escape in king_escapes:
        # Now we check each escape if it can be checked by some Piece.
        # If it can be checked it means king could not escape there since it will be eaten
        check = check_whole_board(board, escape, opposite_team, loc)
        if not check:
            return False
    return True


def handle_check(board: Board, king: Soldier_Classes.King, loc: Locations):
    mate = is_mate(board, king, loc)
    return mate


def can_check(board: Board, coords: list, x, y):
    if board[coords[::-1]].movement(coords[1], coords[0], x, y):
        if board.clear_way(coords[1], coords[0], x, y):
            return True
    return False


def is_check(board: Board, coords: list, king: Soldier_Classes.King):
    x, y = board.get_king_coords(king.get_team())
    # return board.player_move(coords, [x, y], test_move=True)
    # For some reason I could not use it as it returns True Falsely for some reason, so I did it manually
    if can_check(board, coords, x, y):
        return True
    return False


def handle_input(move: list):
    """
    Just taking the user input and making it workable as a list index
    :returns A list with the values in it, False if it fails because of input
    """
    move[0] = int(LETTERS.index(move[0].upper()))
    move[1] = 8 - (int(move[1]))
    return move


def get_all_pieces(board: Board, team: str):
    pieces = []
    for i in range(8):
        for j in range(8):
            if isinstance(board[[i, j]], Piece_Class.Piece):
                if board[[i, j]].get_team() == team:
                    pieces.append([i, j])
    return pieces


def update_location(board: Board, loc: Locations, t_from, t_to: list, team):
    """
    We need to update the location class each time a move is being made,
    If we are 'eating' a Piece we need to remove it from the list
    """
    opp_team = get_opposite_team(board[t_to])
    if loc.find_location(t_to, opp_team):
        # delete an opponent piece from its list
        loc.remove_location(t_to, opp_team)
    # Then we just update it
    loc.update_location(t_from, t_to, team)


def check_valid_moves(board: Board, loc: Locations, our_team: str):
    """
    Checks if the opponent team can move any  piece that could change the current situation
    """
    opponent_pieces = loc.get_opposite_team_locations(our_team)
    our_maters = loc.get_maters()
    # These are the opponent's targets
    if not our_maters:
        return True
    for mater in our_maters:
        for piece in opponent_pieces:
            if board.player_move(piece[::-1], mater[::-1], test_move=True):
                return True
    return False


def is_stalemate(board: Board, king: Soldier_Classes.King, loc: Locations):
    """
    checking if a stalemate happened, how?
     - checking if the target king is surrounded
     - checking if the other team has any moves that could change this option
    :param board: playing board
    :param king: the opposite team's king
    :param loc: The teams' pieces locations
    :return: True/False
    """
    our_team = get_opposite_team(king)
    # Checking if the king is being surrounded
    if is_mate(board, king, loc):
        if not check_valid_moves(board, loc, our_team):
            return True
    return False


def handle_backwards_input(user_input: str, turn: int):
    """
    get the relevant part from the user's input when it wants to go backwards
    :param user_input: the user input
    :param turn: we take turn as an argument because how many turns to go back can't be higher than it
    :return: int, the number of turns it wants to go back
    """
    how_many = int(user_input[1::])
    if how_many > turn + 1:
        # Raising AttributeError in order to get the movement Error
        raise AttributeError
    return how_many


def move_backwards(board: Board, user_input: str, turn: int, p_boards: Previous):
    """
    Move the game a few steps backwards
    """
    how_many = handle_backwards_input(user_input, turn)
    board = p_boards.roll_back(how_many)
    # I return turn too because when we roll the playing board back we want that the team that has been playing
    # when the board was in this form will be the same. I decrease it by 1 too because it gets increased
    # soon as player_move exits
    return board, turn - (how_many + 1)


def player_move(board: Board, king: Soldier_Classes.King, turn: int, location: Locations, p_boards: Previous, player_input=''):
    """
    handles all the functions that happen when a player move is being made,
    checking that the move is valid
    checking that the piece that is trying to be moved belongs to the playing team
    checking if a check, mate or a pat is true after the move
    :param board: The playing board
    :param king: the opposing team's king piece
    :param location: The location of each team's Pieces on the playing board
    :param turn: what turn we're on
    :param p_boards: The boards of previous turns
    """
    final_msg = ''
    mate = False
    valid = False
    while not valid:
        try:
            if final_msg:
                if player_input:
                    return False, final_msg, turn
                print(final_msg)
            if player_input:
                play = player_input
            else:
                play = input("Move: ")
            if play.startswith("!"):
                valid = True
                board, turn = move_backwards(board, play, turn, p_boards)
                location = initialize_locations(board)
                continue
            play = play.split(" ")
            move_from = handle_input(list(play[0]))
            if not check_correct_team_move(board, move_from, turn):
                final_msg = TEAM_ERROR
            else:
                if play[1] == "to":
                    play[1] = play[2]
                move_to = handle_input(list(play[1]))
                if not move_to or not move_from:
                    # meaning that the function handle_input() got bad input so, we need to
                    final_msg = SYNTAX_ERROR
                else:
                    if not board.player_move(move_from, move_to):
                        final_msg = MOVEMENT_ERROR
                    else:
                        valid = True
                        update_location(board, location, move_from[::-1], move_to[::-1], TURNS[turn % 2])
                        final_msg = ''
                        # Since we moved the piece to the target tile,
                        # we need to check if the other king is withing the Piece's reach
                        if is_check(board, move_to, king):
                            mate = handle_check(board, king, location)
                            final_msg = f'\n{CHECK}' if not mate else f'\n{CHECKMATE % get_opposite_team(king)}'
                        else:
                            # Stalemate is not fully initialized yet
                            if is_stalemate(board, king, location):
                                mate = True
                                final_msg = "\n{}".format(STALEMATE)
        except (IndexError, TypeError, ValueError, AttributeError) as e:
            # Handles bad user input
            if type(e) is AttributeError:
                final_msg = f'\n{MOVEMENT_ERROR}'
            else:
                final_msg = f'\n{SYNTAX_ERROR}'
        finally:
            if valid:
                return mate, final_msg, turn


def reset_msg(board: Board, team: str):
    """
    we want the message that we print to the console to be reset each turn
    """
    msg = '%s\n%s' % (str(board), WHOS_PLAYING % team)
    return msg


def initialize_locations(board: Board):
    black = get_all_pieces(board, B)
    white = get_all_pieces(board, W)
    ls = Locations(black, white)
    return ls


def get_target_king(playing_board: Board, turn: int) -> Soldier_Classes.King:
    w_king_cords = get_kings_cords(playing_board, TURNS[0])
    b_king_cords = get_kings_cords(playing_board, TURNS[1])
    if TURNS[turn % 2] == "White":
        target_king = playing_board[b_king_cords]
    else:
        target_king = playing_board[w_king_cords]
    return target_king


def finalize_msg(playing_board: Board, turn: int, add_to_msg: str):
    final = reset_msg(playing_board, TURNS[turn % 2])
    final += '%s' % add_to_msg
    return final


def main():
    """
    main function of the Chess game when it's not multiplayer
    """
    playing_board = Board()
    team_locations = initialize_locations(playing_board)
    p_boards = Previous(playing_board)
    turn = 0
    mate = False
    print(reset_msg(playing_board, TURNS[turn % 2]))
    while not mate:
        target_king = get_target_king(playing_board, turn)
        mate, add_to_msg, turn = player_move(playing_board, target_king, turn, team_locations, p_boards)
        p_boards.add_board(playing_board)
        turn += 1
        final = finalize_msg(playing_board, turn, add_to_msg)
        add_to_msg = ''
        print(final)


if __name__ == '__main__':
    main()
