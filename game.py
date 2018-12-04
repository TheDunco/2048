'''2048 Game Class
CS108 Final Project
Created Fall 2018
@author: Duncan Van Keulen
'''

from tile import *
from random import randint
from GUI import *
from coords import *

# FIXME: Add safe exit method
# FIXME: Color does not change in space 0


class Twenty48:

    def __init__(self):

        self._score = 0
        self._occupied_tiles = [False, False, False, False,
                                False, False, False, False,
                                False, False, False, False,
                                False, False, False, False]

        self._active_tiles = []

        self._coords = Coords()

    def spawn_tile(self):
        '''Spawns tiles with values 2 or 4 respective to percentages'''

        # Choose whether the tile spawns as a 2 (90%) or 4 (10%)
        rand_percent = randint(0,10)
        if rand_percent == 0 or rand_percent == 1:
            value = 4
        else:
            value = 2

        tile = Tile(value)
        tile.set_position_coords(self._coords.get_space(randint(0, 15)))
        tile.set_color()
        self._active_tiles.append(tile)

    def get_tiles_list(self):
        return self._active_tiles

    def move_tiles(self, direction):
        if direction == 'up':
            for tile in self._occupied_tiles:
                pass

    def draw_tiles(self):
        '''Render the tiles'''
        for tile in self._active_tiles:
            tile.render(self._board)

    def game_over(self):
        '''Returns boolean of the game-over state'''
        # FIXME: Create dynamic accessor and mutator for SPACE occupied 'oc' slice and use that...
        # FIXME: Will have to create an accessor for SPACES list
        for element in self._occupied_tiles:
            if not element:
                return False


if __name__ == '__main__':
    game = Twenty48()



