'''2048 Game Class
CS108 Final Project
Created Fall 2018
@author: Duncan Van Keulen
'''

from random import randint
from GUI import *
from coords import *


class Twenty48:
    '''
    Main game mechanics for 2048 game
    Handles movement, merging, colors, drawing tiles, and game states
    '''

    def __init__(self, gui):

        # Create a list of the tile values
        self._vals = []
        self.init_vals_list()

        self._score = 0

        # Initialize the instance variables of the board and GUI from the GUI class
        self._gui = gui

        # Make a coords object
        self._coords = Coords()

        self._colors = {}

    def set_color_scheme(self, scheme):
        '''Set the correct dictionary of colors according to the scheme'''

        if scheme == 'playful':
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
                2048: '#D32F2F',
                4096: '#303030',
                8192: '#00FF33'
            }

        if scheme == 'red':
            '''Color scheme made from https://www.december.com/html/spec/color1.html'''
            self._colors = {
                2: '#CDC9C9',
                4: '#8B8989',
                8: '#8B6969',
                16: '#BC8F8F',
                32: '#C67171',
                64: '#CD5555',
                128: '#8E2323',
                256: '#800000',
                512: '#CC3232',
                1024: '#660000',
                2048: '#FF0000',
                4096: '#330000',
                8192: '#FFFAFA'
            }

        if scheme == 'blue':
            '''Color scheme made from https://www.december.com/html/spec/color1.html'''
            self._colors = {
                2: '#E0EEEE',
                4: '#AABBFF',
                8: '#79CDCD',
                16: '#55A7C3',
                32: '#00B2EE',
                64: '#0099CC',
                128: '#00688B',
                256: '#003F87',
                512: '#1874CD',
                1024: '#40509F',
                2048: '#0000FF',
                4096: '#162252',
                8192: '#380474'
            }

    def init_vals_list(self):
        '''Initialize the values of all of the spaces to be 0'''
        self._vals = [0, 0, 0, 0,
                      0, 0, 0, 0,
                      0, 0, 0, 0,
                      0, 0, 0, 0]

        # # Color scheme testing
        # self._vals = [2, 4, 8, 16,
        #               32, 64, 128, 256,
        #               1024, 2048, 4096, 8192,
        #               0, 0, 0, 0]

    def draw_tiles(self):
        '''Draw the tiles on the gui'''

        if 2048 in self._vals:
            self._gui.game_win()

        # For each index in the list of tile values
        for index in range(len(self._vals)):
            value = self._vals[index]
            if value != 0:
                # Change the tile color
                color = self._colors[value]
                # Set the correct space dictionary for the tile's position
                space = self._coords.get_space(index)

                # Create the the tile
                self._gui.get_board().create_rectangle(space['x1'], space['y1'], space['x2'], space['y2'], fill=color)
                # Create the text for the value of the tile
                self._gui.get_board().create_text((space['cx'], space['cy']), text=str(value), font=('Roboto', 12))

    def spawn_tile(self, number=1):
        '''Spawns tiles with values 2 or 4'''

        #
        for i in range(number):
            # Choose whether the tile spawns as a 2 or 4 based on how many are spawning
            # If there are 2 tiles spawning, the chances of a 4 are increased
            if number == 2:

                # 1/5 chance of spawning a 4
                rand_percent = randint(0, 5)
            else:
                # 1/8 chance of spawning a 4
                rand_percent = randint(0, 8)

            if rand_percent == 5:
                value = 4
            else:
                value = 2

            free_spaces = []

            # Create a list of the indices of free spaces
            for index in range(16):
                if self._vals[index] == 0:
                    free_spaces.append(index)

            # How many free spaces there are
            amount_free_spaces = len(free_spaces)
            # A random index for the free_spaces list
            rand_free_index = randint(0, amount_free_spaces-1)
            # A random index for spawning a new tile
            rand_index = free_spaces[rand_free_index]

            # Set the value of the random free index to previously decided value
            self._vals[rand_index] = value

    def _move(self, spaces, difference):
        '''Move the tiles based on a list of which tiles and the difference between them (direction)'''

        board_state_copy = self._vals[:]

        # Move three times...
        for i in range(3):
            # For relevant indexes...
            for index in spaces:
                try:
                    # Check if the new spot is empty and move there if it is
                    if self._vals[index + difference] == 0:
                        self._vals[index + difference] = self._vals[index]
                        self._vals[index] = 0
                        self._gui.refresh()

                    # If the value of the new space is the same as the old, merge them
                    elif self._vals[index + difference] == self._vals[index]:
                        self._vals[index + difference] = self._vals[index] * 2
                        self._score += self._vals[index] * 2
                        self._vals[index] = 0
                        self._gui.refresh()

                except IndexError:
                    continue

        # Set the score on the GUI
        self._gui.set_score(self._score)

        # Check to see if anything changed and spawn a new tile if it did
        if board_state_copy != self._vals:
            self.spawn_tile(1)
            self._gui.refresh()

        # Check to see if the game is over
        if self.game_over_check():
            self._gui.game_over()

    def move_tiles(self, direction):
        '''Call the move method for moving the values the specified direction'''

        # Move tiles 4-16 up
        if direction == 'up':
            self._move(range(4, 16), (-4))

        # Move tiles that can down
        if direction == 'down':
            self._move([12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0], 4)

        # Move the tiles that can right
        if direction == 'right':
            self._move([2, 1, 0, 6, 5, 4, 10, 9, 8, 14, 13, 12], 1) # [0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14], 1)

        # Move the tiles that can left
        if direction == 'left':
            self._move([1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15], (-1))

    def get_score(self):
        '''Accessor for the socre instance variable'''
        return self._score

    def set_score(self, new_score):
        '''Mutator for the score instance variable'''
        self._score = new_score

    def game_over_check(self):
        '''Returns boolean of the game-over state'''

        # If there are no more empty spaces (all spaces are filled)
        if 0 not in self._vals:
            # Return false if a move can be made by moving up
            for index in [4, 5, 6, 7,
                          8, 9, 10, 11,
                          12, 13, 14, 15]:
                # If an above tile is the same value, the game is not over
                if self._vals[index] == self._vals[index - 4]:
                    return False

            # Return False if a move can be made by moving down
            for index in [0, 1, 2, 3,
                          4, 5, 6, 7,
                          8, 9, 10, 11]:
                # If an above tile is the same value, the game is not over
                if self._vals[index] == self._vals[index + 4]:
                    return False

            # Return false if a move can be made by moving right
            for index in [0, 1, 2,
                          4, 5, 6,
                          8, 9, 10,
                          12, 13, 14]:
                # If an adjacent tile to the right is the same value, the game is not over
                if self._vals[index] == self._vals[index + 1]:
                    return False

            # Return false if a move can be made by moving left
            for index in [1, 2, 3,
                          5, 6, 7,
                          9, 10, 11,
                          13, 14, 15]:
                # If an adjacent tile to the right is the same value, the game is not over
                if self._vals[index] == self._vals[index - 1]:
                    return False

            # If no moves can be made, the game is over
            return True
