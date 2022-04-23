# This file is meant to store all the locations of each team's pieces
# so we don't have to run over the board over and over again to find the team's pieces
from Variables import *


class Locations(object):

    def __init__(self, black_coords: list, white_coords: list):
        self.black = black_coords
        self.white = white_coords
        # This is a list that includes only pieces that are surrounding the king in the same turn
        self.maters = []

    def update_location(self, old: list, new: list, team):
        if team == W:
            i = self.white.index(old)
            self.white[i] = new
        else:
            i = self.black.index(old)
            self.black[i] = new

    def remove_location(self, loc: list, team):
        if team == W:
            self.white.remove(loc)
        else:
            self.black.remove(loc)

    def find_location(self, loc: list, team):
        try:
            if team == W:
                if self.white.index(loc):
                    return True
            else:
                if self.black.index(loc):
                    return True
            return False
        except ValueError:
            # If it's not in the list index() raises ValueError
            return False

    def get_team_locations(self, team):
        if team == W:
            return self.white
        else:
            return self.black

    def get_opposite_team_locations(self, team):
        if team == B:
            return self.white
        else:
            return self.black

    def get_maters(self):
        return self.maters

    def add_to_maters(self, coords: list):
        self.maters.append(coords)

    def reset_maters(self):
        self.maters = []
