# This file is meant to store all the locations of each team's pieces
# so we don't have to run over the board over and over again to find the team's pieces
from Variables import *


class Locations(object):

    def __init__(self, black_coords: list, white_coords: list):
        self.black = black_coords
        self.white = white_coords

    def update_location(self, old: list, new: list, team):
        if team == W:
            i = self.white.index(old)
            self.white[i] = new
        else:
            i = self.black.index(old)
            self.black[i] = new

    def get_team_locations(self, team):
        if team == W:
            return self.white
        else:
            return self.black


if __name__ == '__main__':
    pass