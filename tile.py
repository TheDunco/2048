'''Tile Class for 2048 Game
CS108 Final Project
Created Fall 2018
@author: Duncan Van Keulen
'''

# from GUI import *
from coords import *


class Tile:
    '''Tile class for 2048 game'''

    def __init__(self, value=2):
        '''Constructor for instance variables of tile'''
        self._value = value
        self._color = '#BBBBBB'
        self._x1 = 0
        self._y1 = 0
        self._x2 = 100
        self._y2 = 100
        self._center_x = 50
        self._center_y = 50
        self._occupied_tile_id = 0

    def render_tile(self, board):
        '''Renders tile to canvas'''

        board.create_rectangle(self._x1,self._y1, self._x2,self._y2, fill=self._color)
        board.create_text((self._center_x, self._center_y), text=str(self._value), font=('Roboto', 12))

    # Accessor functions
    def get_value(self):
        '''Accessor for value variable'''
        return self._value

    def get_color(self):
        '''Accessor for the color variable'''
        return self._color

    # Mutator functions
    def set_value(self, new_value):
        '''Mutator for value variable'''
        self._value = new_value

    def set_position_coords(self, space):
        '''Update all of the position coordinates to the tile space coordinates'''

        self._x1 = space['x1']
        self._y1 = space['y1']
        self._x2 = space['x2']
        self._y2 = space['y2']
        self._center_x = space['cx']
        self._center_y = space['cy']
        self._occupied_tile_id = space['id']

    def set_color(self):
        '''Sets the color according go the value of tile
        Colors from https://www.materialpalette.com/'''

        colors = {
            2: '#FFFFFF',
            4: '#BDBDBD',
            8: '#757575',
            16: '#FFCDD2',
            32: '#03A9F4',
            64: '#FFF980',
            128: '#E91E63',
            256: '#CDDC39',
            512: '#E040FB',
            1024: '#7C4DFF',
            2048: '#D32F2F'
        }

        self._color = colors[self._value]

