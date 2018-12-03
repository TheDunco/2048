'''2048 Game Class
CS108 Final Project
Created Fall 2018
@author: Duncan Van Keulen
'''

from tile import *
from random import randint
from GUI import *
from coords import *


class Twenty48:

    def __init__(self):

        self._score = 0
        self._occupied_tiles = [False, False, False, False,
                                False, False, False, False,
                                False, False, False, False,
                                False, False, False, False]

        self._active_tiles = []

    def spawn_tile(self):
        '''Spawns tiles with values 2 or 3'''

        rand_percent = randint(0,10)
        if rand_percent == 0 or rand_percent == 1:
            value = 4
        else:
            value = 2

        tile = Tile(value)
        # tile.set_position_coords(SPACES[randint(0, 15)])
        tile.set_position_coords(SPACE15)
        # FIXME: Problems with SPACE0, 4, 5, 6, 7 | 8, 9, 10, 11, 12, 13, 14, 15
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
        for element in self._occupied_tiles:
            if not element:
                return False


if __name__ == '__main__':
    game = Twenty48()



