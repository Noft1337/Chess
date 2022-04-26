import socket
from Board import Board
from locations import *
from Previous_Boards import *
import main as main_offline
import Soldier_Classes
from Variables import *

IP = "127.0.0.1"
PORT = 32412
HEADER = 2048

TURNS = {0: W, 1: B}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))


def send_all_connections(msg: str, *args: socket.socket):
    for arg in args:
        arg.send(msg.encode())


def start_server(msg: str):
    con1 = con2 = ''
    server.listen()
    listening = True
    print(SERVER_START)
    while listening:
        # White connected
        con1, adr1 = server.accept()
        print(f"[*] - [NEW CONNECTION] {adr1} connected as White!")
        con1.send("Welcome White!, waiting for Black to join.".encode())
        # Black connected
        con2, adr2 = server.accept()
        con2.send("Welcome Black! starting game!".encode())
        con1.send("Black joined! starting game!".encode())
        print(f"[*] - [NEW CONNECTION] {adr2} connected as Black!")
        if con1 and con2:
            send_all_connections(msg, con1, con2)
            listening = False

    return con1, con2


def get_input(turn: int, turns: dict[int: socket.socket]):
    u_input = turns[turn % 2].recv(HEADER).decode()
    print(f"{TURNS[turn % 2]}'s move: {u_input}")
    return u_input


def handle_user_input(board: Board, king: Soldier_Classes.King, turn: int, locs: Locations, p_b: Previous, turns: dict):
    """
    Handles the user input to make sure that in the end it's valid
    """
    mate = False
    add_to_msg = ''
    valid = False
    while not valid:
        player_input = get_input(turn, turns)
        mate, add_to_msg, turn = main_offline.player_move(board, king, turn, locs, p_b, player_input)
        if Colors.RED in add_to_msg:
            turns[turn % 2].send(add_to_msg.encode())
        else:
            valid = True
    return mate, add_to_msg, turn


def main():
    turn = 0
    playing_board = Board()
    team_locations = main_offline.initialize_locations(playing_board)
    p_boards = Previous(playing_board)
    to_send = main_offline.reset_msg(playing_board, TURNS[turn % 2])
    con1, con2 = start_server(to_send)
    turns = {0: con1, 1: con2}
    mate = False
    while not mate:
        king = main_offline.get_target_king(playing_board, turn)
        mate, add_to_msg, turn = handle_user_input(playing_board, king, turn, team_locations, p_boards, turns)
        turn += 1
        to_send = main_offline.finalize_msg(playing_board, turn, add_to_msg)
        print(to_send)
        send_all_connections(to_send, con1, con2)


if __name__ == '__main__':
    main()
