'''2048 Game Class
CS108 Final Project
Created Fall 2018
@author: Duncan Van Keulen
'''

from random import randint
from GUI import *
from coords import *

# FIXME: Add high score, game over functionality


class Twenty48:

    def __init__(self, board, gui):

        # Create a list of the tile values
        self._vals = []
        self.init_vals_list()

        self._score = 0

        self._board = board

        self._gui = gui

        self._coords = Coords()

        self._merged = False

        self._colors = {
            2: '#FFE066',
            4: '#FFFFFF',
            8: '#757575',
            16: '#FFCDD2',
            32: '#03A9F4',
            64: '#003366',
            128: '#E91E63',
            256: '#CDDC39',
            512: '#E040FB',
            1024: '#7C4DFF',
            2048: '#D32F2F'
        }

    def init_vals_list(self):

        self._vals = [0, 0, 0, 0,
                      0, 0, 0, 0,
                      0, 0, 0, 0,
                      0, 0, 0, 0]

    def draw_tiles(self):
        for index in range(len(self._vals)):
            value = self._vals[index]
            if value != 0:
                color = self._colors[value]
                space = self._coords.get_space(index)

                self._board.create_rectangle(space['x1'], space['y1'], space['x2'], space['y2'], fill=color)
                self._board.create_text((space['cx'], space['cy']), text=str(value), font=('Roboto', 12))

    def spawn_tile(self, number):
        '''Spawns tiles with values 2 or 4 respective to percentages'''

        for i in range(number):

            # Choose whether the tile spawns as a 2 or 4 based on how many are spawning
            if number == 2:
                rand_percent = randint(0, 10)
            else:
                rand_percent = randint(0, 5)

            if rand_percent == 0 or rand_percent == 1:
                value = 4
            else:
                value = 2

            free_spaces = []

            for index in range(16):
                if self._vals[index] == 0:
                    # Create a list of the indices of free spaces
                    free_spaces.append(index)

            amount_free_spaces = len(free_spaces)
            rand_free_index = randint(0, amount_free_spaces-1)
            rand_index = free_spaces[rand_free_index]

            # Set the value of the random free index to a 2 or 4
            self._vals[rand_index] = value

    def _move(self, spaces, difference):

        board_state_copy = self._vals[:]

        # Move three times...
        for i in range(3):
            # For relevant indexes...
            for index in spaces:
                try:
                    # See if the new spot is empty and move there if it is
                    if self._vals[index + difference] == 0:
                        self._vals[index + difference] = self._vals[index]
                        self._vals[index] = 0
                        self._gui.refresh()
                    elif self._vals[index + difference] == self._vals[index]:
                        # Merge tiles
                        self._vals[index + difference] = self._vals[index] * 2
                        self._score += self._vals[index] * 2
                        self._vals[index] = 0
                        self._gui.refresh()

                except IndexError:
                    continue
        self._gui.set_score(self._score)

        if board_state_copy != self._vals:
            self.spawn_tile(1)
            self._gui.refresh()

        if self.game_over_check():
            print('Game 0ver!')
            self._gui.game_over()

    def move_tiles(self, direction):
        if direction == 'up':
            self._move(range(4, 16), (-4))

        if direction == 'down':
            self._move([12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0], 4)

        if direction == 'right':
            self._move([2, 1, 0, 6, 5, 4, 10, 9, 8, 14, 13, 12], 1) # [0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14], 1)

        if direction == 'left':
            self._move([1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15], (-1))

    def get_score(self):
        return self._score

    def set_score(self, new_score):
        self._score = new_score

    def game_over_check(self):
        '''Returns boolean of the game-over state'''

        # FIXME: This logic isn't always working, probably because index error...
        # FIXME: Either make it check each individual tile or think harder...

        if 0 not in self._vals:
            # Return false if a move can be made by moving up
            for index in [0, 1, 2, 3,
                          4, 5, 6, 7,
                          8, 9, 10, 11]:
                if self._vals[index] == self._vals[index + 4]:
                    return False

            # Return false if a move can be made by moving down
            for index in [4, 5, 6, 7,
                          8, 9, 10, 11,
                          12, 13, 14, 15]:
                if self._vals[index] == self._vals[index - 4]:
                    return False

            # Return false if a move can be made by moving right
            for index in [0, 1, 2,
                          4, 5, 6,
                          8, 9, 10,
                          12, 13, 14]:
                if self._vals[index] == self._vals[index + 1]:
                    return False

            # Return false if a move can be made by moving left
            for index in [1, 2, 3,
                          5, 6, 7,
                          9, 10, 11,
                          13, 14, 15]:
                if self._vals[index] == self._vals[index - 1]:
                    return False

            # If no moves can be made, the game is over
            return True





