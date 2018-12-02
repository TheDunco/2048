'''2048 Game
CS108 Final Project
Created Fall 2018
@author: Duncan Van Keulen
'''

from tile import *
from random import randint


class Twenty48:

    def __init__(self):

        self._score = 0
        self._occupied_tiles = [False, False, False, False,
                                False, False, False, False,
                                False, False, False, False,
                                False, False, False, False]

        self._active_tiles = []

    def spawn_tiles(self):
        '''Spawns tiles with values 2 or 3'''

        spawn_values = [2,4]
        choose_random = randint(0,1)
        value = spawn_values[choose_random]
        for i in range(2):
            tile = Tile(value)
            self.active_tiles.append(tile)

    def move_tiles(self, direction):
        if direction == 'up':
            for tile in self._occupied_tiles:
                pass

    def draw_tiles(self):
        '''Render the tiles'''
        for tile in self._active_tiles:
            tile.render(board)

    def game_over(self):
        '''Returns boolean of the game-over state'''
        for element in self._occupied_tiles:
            if not element:
                return False


if __name__ == '__main__':
    game = Twenty48()



