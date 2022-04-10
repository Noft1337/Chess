# Board class
# A simple 10x10 board
# My idea is to make it like a triple array that is built like (10,10,Piece)

class Board(object):
    def __init__(self):
        self.gematria = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}
        self.board = [['-' for i in range(10)] for i in range(10)]

    def __str__(self):
        f = 0
        print(f'{self.gematria[i]} ' for i in range(8))
        for b in self.board:
            f += 1
            print(f, ' '.join(b))
