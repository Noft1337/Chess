import socket
import main
from Variables import *

HEADER = 2048
TEAM_SET = False
TEAM_PLAYING = "Playing team: %s"
OPPOSITE_TEAM = {"White": "Black", "Black": "White"}
CHECK_MATE = "Checkmate!"


def handle_input():
    user_input = ""
    valid = False
    while not valid:
        user_input = input(OPENING_MSG)
        if user_input != '1' and user_input != '2':
            print(f"{Colors.RED}Invalid pick.{Colors.END}")
        else:
            valid = True
    return user_input


def validate_ip(ip: str):
    try:
        segments = ip.split('.')
        if len(segments) != 4:
            return False
        for segment in segments:
            if not (0 <= int(segment) < 255):
                return False
        return True
    except ValueError:
        return False


def validate_port(port: str):
    try:
        if not (1024 < int(port) <= 65535):
            return False
        return True
    except ValueError:
        return False


def connection_input():
    ip = ''
    port = 0
    valid = False
    while not valid:
        ip = input(ENTER_IP)
        valid = validate_ip(ip)
        if not valid:
            print(IP_ERROR)
    valid = False
    while not valid:
        port = input(ENTER_PORT)
        valid = validate_port(port)
        if not valid:
            print(PORT_ERROR)
    return ip, int(port)


def set_team(msg: str):
    if "White" in msg:
        team = "White"
    else:
        team = "Black"
    TEAM_SET = True
    return team


def validate_response(resp: str, team: str):
    return TEAM_PLAYING % OPPOSITE_TEAM[team] in resp


def send_move(s: socket.socket, team: str):
    valid = False
    while not valid:
        move = input("Move: ")
        s.send(move.encode())
        resp = s.recv(HEADER).decode()
        print(resp)
        valid = validate_response(resp, team)


def check_if_mate(msg: str):
    return CHECK_MATE in msg


def handle_msg(msg: str, team: str, s: socket.socket):
    print(msg)
    if TEAM_PLAYING % team in msg:
        send_move(s, team)
    return check_if_mate(msg)


def client_main():
    online = handle_input()
    team = ""
    if online == '1':
        main.main()
    else:
        ip, port = connection_input()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        print(f"Connected to {ip}:{port} successfully!")
        mate = False
        while not mate:
            msg = s.recv(HEADER).decode()
            if msg:
                if not TEAM_SET:
                    team = set_team(msg)
                mate = handle_msg(msg, team, s)


if __name__ == '__main__':
    client_main()
