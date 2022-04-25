import socket
from Board import Board
from locations import *
from Previous_Boards import *
import main as main_offline
import Soldier_Classes
from Variables import *

IP = "127.0.0.1"
PORT = 32412
HEADER = 1024

TURNS = {0: W, 1: B}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))


def players_move(board: Board, con: socket.socket, turn: int, teams: dict):
    pass


def player_move(board: Board, king: Soldier_Classes.King, turn: int, location: Locations, p_boards: Previous):
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
           pass
        except (IndexError, TypeError, ValueError, AttributeError) as e:
            # Handles bad user input
            if type(e) is AttributeError:
                final_msg = f'\n{MOVEMENT_ERROR}'
            else:
                final_msg = f'\n{SYNTAX_ERROR}'
        finally:
            if valid:
                return mate, final_msg, turn


def start_server():
    server.listen()
    listening = True
    print(SERVER_START)
    while listening:
        # White connected
        con1, adr1 = server.accept()
        print(f"[*] - [NEW CONNECTION] {adr1} connected as White!")
        # Black connected
        con2, adr2 = server.accept()
        print(f"[*] - [NEW CONNECTION] {adr2} connected as Black!")
        if con1 and con2:
            listening = False
    return con1, con2


def main():
    playing_board = Board()
    team_locations = main_offline.initialize_locations(playing_board)
    p_boards = Previous(playing_board)
    con1, con2 = start_server()
    turn = 0
    teams = {con1: "White", con2: "Black"}
    turns = {0: con1, 1: con2}
    while True:
        msg = input("MSG: ")
        con1.send(msg.encode())
        con2.send(msg.encode())



if __name__ == '__main__':
    main()
