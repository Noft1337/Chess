import socket
import main
from Variables import *


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


def client_main():
    online = handle_input()
    if online == '1':
        main.main()
    else:
        ip, port = connection_input()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        while True:
            msg = s.recv(1024)
            if msg:
                print(msg)


if __name__ == '__main__':
    client_main()