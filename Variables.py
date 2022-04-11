# Errors
RULES_LINK = u"https://en.wikipedia.org/wiki/Rules_of_chess#Movement"
SYNTAX_ERROR = "Invalid input.\n\t" \
               "Valid Input: <Cell> to <Cell> (e.g A4 to A5)"
MOVEMENT_ERROR = "The piece in {from} cannot move to {to} as it does not follow its skill set\n\t" \
                 "If you'd like to know what each piece is capable of please visit: %s" % RULES_LINK
POSITION_ERROR = "The cell you'd like to move from is not manned by a piece of yours."

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
