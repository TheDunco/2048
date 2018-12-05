'''2048 Game Class
CS108 Final Project
Created Fall 2018
@author: Duncan Van Keulen
'''

from tile import *
from random import randint
from GUI import *
from coords import *

# FIXME: Make sure that it doesn't spawn a new tile when nothing moves: move the go() calls to the GUI maybe
# FIXME: Add game over functionality
# FIXME: ADD SCORE


class Twenty48:

    def __init__(self):

        # self.gui = gui

        self._active_tiles = []
        self.init_active_tiles_list()

        self._free_spaces = []

        self._coords = Coords()

        self._row0 = [0, 1, 2,  3]
        self._row1 = [4, 5, 6, 7]
        self._row2 = [8, 9, 10, 11]
        self._row3 = [12, 13, 14, 15]

        self._column0 = [0, 4, 8, 12]
        self._column1 = [1, 5, 9, 13]
        self._column2 = [2, 6, 10, 14]
        self._column3 = [3, 7, 11, 15]

    def init_active_tiles_list(self):
        self._active_tiles = [Blank(), Blank(), Blank(), Blank(),
                              Blank(), Blank(), Blank(), Blank(),
                              Blank(), Blank(), Blank(), Blank(),
                              Blank(), Blank(), Blank(), Blank()]

        self._free_spaces = [0, 1, 2, 3,
                             4, 5, 6, 7,
                             8, 9, 10, 11,
                             12, 13, 14, 15]

    def spawn_tile(self, number):
        '''Spawns tiles with values 2 or 4 respective to percentages'''

        # Choose whether the tile is a 2 or 4
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

            # Create a Tile object with the specified value
            tile = Tile(value)

            rand_free_range = randint(0, len(self._free_spaces)-1)
            rand_space = self._free_spaces[rand_free_range]

            print(rand_space)

            # FIXME so that tiles can't spawn on top of existing ones
            if type(self._active_tiles[rand_space]) == Blank:
                # Update the tile coordinates if the new space is a blank
                tile.set_position_coords(self._coords.get_space(rand_space))

                # Remove the new tile space from the free spaces list
                self._free_spaces.remove(rand_space)

                # Set the color and append the tile to the active_tiles instance list
                tile.set_color()
                self._active_tiles[tile.get_occupied_space_id()] = tile

    def get_tiles_list(self):
        '''Return the list of active tiles'''
        return self._active_tiles

    def merge(self, index1, index2):
        '''Merge tile1 @ index1 into tile 2 @ index2'''

        tile1 = self._active_tiles[index1]
        tile2 = self._active_tiles[index2]

        # Only merge the tiles if they have the same value
        if tile1.get_value() == tile2.get_value():
            # Double the value of the tile
            val = tile2.get_value()
            val *=2
            tile2.set_value(val)

            # Set space of tile 1 to blank
            self._active_tiles[index1] = Blank()
            self._free_spaces.append(index1)

            # Update the merged tile
            self._active_tiles[index2] = tile2
            # self._free_spaces.remove(index2)

    def row1_up(self):
        '''Move row 1 up to row 0'''
        for index in self._row1:
            # Find all of the tiles in the row
            if type(self._active_tiles[index]) == Tile:
                # Make sure that the space to move to is blank
                if type(self._active_tiles[index - 4]) == Blank:
                    # Get the tile to be moved from the active_tiles_list
                    tile = self._active_tiles[index]
                    # Set the position of the tile to the new space
                    tile.set_position_coords(self._coords.get_space((index - 4)))
                    self._active_tiles[index - 4] = tile
                    self._active_tiles[index] = Blank()
                    # Add new tile space and remove old tile space from free_spaces
                    self._free_spaces.remove((index - 4))
                    self._free_spaces.append(index)
                else:
                    self.merge(index, index - 4)

    def row2_up(self):
        '''Move row2 up to row 1'''
        for index in self._row2:
            # Find all of the tiles in the row
            if type(self._active_tiles[index]) == Tile:
                # Make sure that the space to move to is blank
                if type(self._active_tiles[index - 4]) == Blank:
                    # Get the tile to be moved from the active_tiles_list
                    tile = self._active_tiles[index]
                    # Set the position of the tile to the new space
                    tile.set_position_coords(self._coords.get_space((index - 4)))
                    self._active_tiles[index - 4] = tile
                    self._active_tiles[index] = Blank()
                    # Add new tile space and remove old tile space from free_spaces
                    self._free_spaces.remove((index - 4))
                    self._free_spaces.append(index)
                else:
                    self.merge(index, index - 4)

    def row3_up(self):
        '''Move row 3 up to row 2'''
        for index in self._row3:
            # Find all of the tiles in the row
            if type(self._active_tiles[index]) == Tile:
                # Make sure that the space to move to is blank
                if type(self._active_tiles[index - 4]) == Blank:
                    # Get the tile to be moved from the active_tiles_list
                    tile = self._active_tiles[index]
                    # Set the position of the tile to the new space
                    tile.set_position_coords(self._coords.get_space((index - 4)))
                    self._active_tiles[index - 4] = tile
                    self._active_tiles[index] = Blank()
                    # Add new tile space and remove old tile space from free_spaces
                    self._free_spaces.remove((index - 4))
                    self._free_spaces.append(index)
                else:
                    self.merge(index, index - 4)

    def row0_down(self):
        '''Move row 0 down to row 1'''
        for index in self._row0:
            # Find all of the tiles in the row
            if type(self._active_tiles[index]) == Tile:
                # Make sure that the space to move to is blank
                if type(self._active_tiles[index + 4]) == Blank:
                    # Get the tile to be moved from the active_tiles_list
                    tile = self._active_tiles[index]
                    # Set the position of the tile to the new space
                    tile.set_position_coords(self._coords.get_space((index + 4)))
                    self._active_tiles[index + 4] = tile
                    self._active_tiles[index] = Blank()
                    # Add new tile space and remove old tile space from free_spaces
                    self._free_spaces.remove((index + 4))
                    self._free_spaces.append(index)
                else:
                    self.merge(index, index + 4)

    def row1_down(self):
        '''Move row1 down to row 2'''
        for index in self._row1:
            # Find all of the tiles in the row
            if type(self._active_tiles[index]) == Tile:
                # Make sure that the space to move to is blank
                if type(self._active_tiles[index + 4]) == Blank:
                    # Get the tile to be moved from the active_tiles_list
                    tile = self._active_tiles[index]
                    # Set the position of the tile to the new space
                    tile.set_position_coords(self._coords.get_space((index + 4)))
                    self._active_tiles[index + 4] = tile
                    self._active_tiles[index] = Blank()
                    # Add new tile space and remove old tile space from free_spaces
                    self._free_spaces.remove((index + 4))
                    self._free_spaces.append(index)
                else:
                    self.merge(index, index + 4)

    def row2_down(self):
        '''Move row 2 down to row 3'''
        for index in self._row2:
            # Find all of the tiles in the row
            if type(self._active_tiles[index]) == Tile:
                # Make sure that the space to move to is blank
                if type(self._active_tiles[index + 4]) == Blank:
                    # Get the tile to be moved from the active_tiles_list
                    tile = self._active_tiles[index]
                    # Set the position of the tile to the new space
                    tile.set_position_coords(self._coords.get_space((index + 4)))
                    self._active_tiles[index + 4] = tile
                    self._active_tiles[index] = Blank()
                    # Add new tile space and remove old tile space from free_spaces
                    self._free_spaces.remove((index + 4))
                    self._free_spaces.append(index)
                else:
                    self.merge(index, index + 4)

    def column0_right(self):
        '''Move column0 to column1'''
        for index in self._column0:
            # Find all of the tiles in the row
            if type(self._active_tiles[index]) == Tile:
                # Make sure that the space to move to is blank
                if type(self._active_tiles[index + 1]) == Blank:
                    # Get the tile to be moved from the active_tiles_list
                    tile = self._active_tiles[index]
                    # Set the position of the tile to the new space
                    tile.set_position_coords(self._coords.get_space((index + 1)))
                    self._active_tiles[index + 1] = tile
                    self._active_tiles[index] = Blank()
                    # Add new tile space and remove old tile space from free_spaces
                    self._free_spaces.remove((index + 1))
                    self._free_spaces.append(index)
                else:
                    self.merge(index, index + 1)

    def column1_right(self):
        '''Move column1 to column2'''
        for index in self._column1:
            # Find all of the tiles in the row
            if type(self._active_tiles[index]) == Tile:
                # Make sure that the space to move to is blank
                if type(self._active_tiles[index + 1]) == Blank:
                    # Get the tile to be moved from the active_tiles_list
                    tile = self._active_tiles[index]
                    # Set the position of the tile to the new space
                    tile.set_position_coords(self._coords.get_space((index + 1)))
                    self._active_tiles[index + 1] = tile
                    self._active_tiles[index] = Blank()
                    # Add new tile space and remove old tile space from free_spaces
                    self._free_spaces.remove((index + 1))
                    self._free_spaces.append(index)
                else:
                    self.merge(index, index + 1)

    def column2_right(self):
        '''Move column2 to column3'''
        for index in self._column2:
            # Find all of the tiles in the row
            if type(self._active_tiles[index]) == Tile:
                # Make sure that the space to move to is blank
                if type(self._active_tiles[index + 1]) == Blank:
                    # Get the tile to be moved from the active_tiles_list
                    tile = self._active_tiles[index]
                    # Set the position of the tile to the new space
                    tile.set_position_coords(self._coords.get_space((index + 1)))
                    self._active_tiles[index + 1] = tile
                    self._active_tiles[index] = Blank()
                    # Add new tile space and remove old tile space from free_spaces
                    self._free_spaces.remove((index + 1))
                    self._free_spaces.append(index)
                else:
                    self.merge(index, index + 1)

    def column1_left(self):
        '''Move column1 to column0'''
        for index in self._column1:
            # Find all of the tiles in the row
            if type(self._active_tiles[index]) == Tile:
                # Make sure that the space to move to is blank
                if type(self._active_tiles[index - 1]) == Blank:
                    # Get the tile to be moved from the active_tiles_list
                    tile = self._active_tiles[index]
                    # Set the position of the tile to the new space
                    tile.set_position_coords(self._coords.get_space((index - 1)))
                    self._active_tiles[index - 1] = tile
                    self._active_tiles[index] = Blank()
                    # Add new tile space and remove old tile space from free_spaces
                    self._free_spaces.remove((index - 1))
                    self._free_spaces.append(index)
                else:
                    self.merge(index, index - 1)

    def column2_left(self):
        '''Move column2 to column1'''
        for index in self._column2:
            # Find all of the tiles in the row
            if type(self._active_tiles[index]) == Tile:
                # Make sure that the space to move to is blank
                if type(self._active_tiles[index - 1]) == Blank:
                    # Get the tile to be moved from the active_tiles_list
                    tile = self._active_tiles[index]
                    # Set the position of the tile to the new space
                    tile.set_position_coords(self._coords.get_space((index - 1)))
                    self._active_tiles[index - 1] = tile
                    self._active_tiles[index] = Blank()
                    # Add new tile space and remove old tile space from free_spaces
                    self._free_spaces.remove((index - 1))
                    self._free_spaces.append(index)
                else:
                    self.merge(index, index - 1)

    def column3_left(self):
        '''Move column3 to column2'''
        for index in self._column3:
            # Find all of the tiles in the row
            if type(self._active_tiles[index]) == Tile:
                # Make sure that the space to move to is blank
                if type(self._active_tiles[index - 1]) == Blank:
                    # Get the tile to be moved from the active_tiles_list
                    tile = self._active_tiles[index]
                    # Set the position of the tile to the new space
                    tile.set_position_coords(self._coords.get_space((index - 1)))
                    self._active_tiles[index - 1] = tile
                    self._active_tiles[index] = Blank()
                    # Add new tile space and remove old tile space from free_spaces
                    self._free_spaces.remove((index - 1))
                    self._free_spaces.append(index)
                else:
                    self.merge(index, index - 1)

    def move_tiles(self, direction):
        if direction == 'up':
            print(self._free_spaces)
            self.row1_up()
            self.row2_up()
            self.row1_up()
            self.row3_up()
            self.row2_up()
            self.row1_up()

        if direction == 'down':
            print(self._free_spaces)
            self.row2_down()
            self.row1_down()
            self.row2_down()
            self.row0_down()
            self.row1_down()
            self.row2_down()

        if direction == 'right':
            print(self._free_spaces)
            self.column2_right()
            self.column1_right()
            self.column2_right()
            self.column0_right()
            self.column1_right()
            self.column2_right()

        if direction == 'left':
            print(self._free_spaces)
            self.column1_left()
            self.column2_left()
            self.column1_left()
            self.column3_left()
            self.column2_left()
            self.column1_left()

        if self.game_over_check():
            print('Game Over')

    def game_over_check(self):
        '''Returns boolean of the game-over state'''
        # FIXME: Create dynamic accessor and mutator for SPACE occupied 'oc' slice and use that...
        # FIXME: Will have to create an accessor for SPACES list
        for element in self._active_tiles:
            if type(element) == Blank:
                return False
        return True


if __name__ == '__main__':
    # root = Tk()
    # root.title('2048')
    # app = GUI(root)
    # root.mainloop()
    game = Twenty48()


