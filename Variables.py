# Errors
RULES_LINK = u"https://en.wikipedia.org/wiki/Rules_of_chess#Movement"
SYNTAX_ERROR = "Invalid input.\n\t" \
               "Valid Input: <Cell> to <Cell> (e.g A4 to A5)"
MOVEMENT_ERROR = "Illegal move."
POSITION_ERROR = "The cell you'd like to move from is not manned by a piece of yours."
TEAM_ERROR = "You can't move this piece"

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
WHOS_PLAYING = "Playing team: {}"
