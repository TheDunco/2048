'''2048 Game
CS108 Final Project
Created Fall 2018
@author: Duncan Van Keulen
'''

from GUI import *
from tile import *
from tkinter import *
from random import randint


class Twenty48:

    def __init__(self):
        self._occupied_tiles = [False, False, False, False,
                                False, False, False, False,
                                False, False, False, False,
                                False, False, False, False]
        self._active_tiles = []

        root = Tk()
        root.title('2048')
        app = GUI(root)
        root.mainloop()

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


if __name__ == '__main__':
    game = Twenty48()


