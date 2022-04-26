from colors import *

# Messages
OPENING_MSG = "Welcome to my Chess game!\n" \
              "How to play:\n\t" \
              "Movement: <From: Tile> <To: Tile>\n\t" \
              "Rolling back: You can roll the board back by typing !<How many turns back>\n\n" \
              "Please choose:\n" \
              "1. Play alone, you vs you\n" \
              "2. Play multiplayer\n" \
              "I choose: "
ENTER_IP = "Please enter the server's IP address: "
ENTER_PORT = "Please enter the port to connect to: "

# Teams
W = 'White'
B = 'Black'

# Final msg to be printed
FINAL_MSG = ''

# Checks
CHECK = f"{Colors.GREEN}Check!{Colors.END}"
CHECKMATE = f"{Colors.CYAN}Checkmate!\n %s Won!{Colors.END}"
STALEMATE = f"{Colors.BLUE}Stalemate situation has been reached!\n\tTie!{Colors.UNDERLINE}"


# Errors
CHECKED_CASTLE = f"{Colors.GREEN}Can't Castle when you're Checked!{Colors.END}"
THREAT_CASTLE = f"{Colors.GREEN}Can't castle into: %s{Colors.END}"
RULES_LINK = u"https://en.wikipedia.org/wiki/Rules_of_chess#Movement"
SYNTAX_ERROR = f"{Colors.RED}Invalid input.\n\t" \
               f"Valid Input: <Cell> <Cell> (e.g A4 A5){Colors.END}"
MOVEMENT_ERROR = f"{Colors.RED}Illegal move.{Colors.END}"
POSITION_ERROR = f"{Colors.RED}The cell you'd like to move from is not manned by a piece of yours.{Colors.END}"
TEAM_ERROR = f"{Colors.RED}You can't move this piece{Colors.END}"
BLOCKED_WAY = f"{Colors.RED}The way is blocked{Colors.END}"
THREAT_ERROR = f"{Colors.GREEN}{Colors.BOLD}The King cannot be moved into a threat!{Colors.END}"
UTILIZATION_ERROR = f"{Colors.RED}This function has not been fully utilized yet. Sorry!{Colors.END}"
IP_ERROR = f"{Colors.RED}Invalid IP.{Colors.END}"
PORT_ERROR = f"{Colors.RED}Invalid PORT.{Colors.END}"

# Server messages
SERVER_START = f"{Colors.BLUE}[*] - [SYSTEM] Server is starting...{Colors.END}"
OPONNENT_LEFT = "Your opponent left.\nYou win!"

# Symbols and Icons
EMPTY_SYMBOL = '_'

W_SYMBOLS = {
    "King": "♚",
    "Queen": "♛",
    "Bishop": "♝",
    "Rook": "♜",
    "Knight": "♞",
    "Pawn": "♟"
}

B_SYMBOLS = {
    "King": "♔",
    "Queen": "♕",
    "Bishop": "♗",
    "Rook": "♖",
    "Knight": "♘",
    "Pawn": "♙"
}


# lists

LETTERS = list('ABCDEFGH')

# misc
WHOS_PLAYING = f"{Colors.YELLOW}Playing team: %s{Colors.END}"
