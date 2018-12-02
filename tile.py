'''Tile Class for 2048 Game
CS108 Final Project
Created Fall 2018
@author: Duncan Van Keulen
'''

import random
from GUI import *

class Tile:
    '''Tile class for 2048 game'''

    def __init__(self, value=2):
        self._value = value
        self._color = '#BBBBBB'
        # FIXME: Make accessors/mutators for these variables
        self._x1 = 0
        self._y1 = 100
        self._x2 = 0
        self._y2 = 100
        self._center_x = 50
        self._center_y = 50
        self._occupied_tile = 0

    def render_tile(self, board):
        '''Renders tile to canvas'''

        # FIXME: Make it so this works with coords defined in GUI class
        # FIXME: Note: Might have to add list for center coords of each board square...
        # FIXME: Note: Make coords for square and center of square be set by which tile it's occupying
        board.create_rectangle(self._x1,self._y1, self._x2,self._y2, fill=self._color)
        board.create_text((self._center_x, self._center_y), text=str(self._value), font=('Roboto', 12))

    # Accessor functions
    def get_x(self):
        '''Accessor for x variable'''
        return self._x

    def get_y(self):
        '''Accessor for y variable'''
        return self._y

    def get_value(self):
        '''Accessor for value variable'''
        return self._value

    # Mutator functions
    def set_x(self, new_x):
        '''Mutator for x variable'''
        # FIXME: Make this animate
        self._x = new_x

    def set_y(self, new_y):
        '''Mutator for y variable'''
        # FIXME: Make this animate
        self._x = new_y

    def set_value(self, new_value):
        '''Mutator for value variable'''
        self._value = new_value

    def get_color(self):
        return self._color

    def set_color(self):
        '''Sets the color according go the value of tile
        Colors from https://www.materialpalette.com/'''
        print('setting color...')
        if self._value == 2:
            self._color = '#FFFFFF'
        elif self._value == 4:
            self._color = '#BDBDBD'
        elif self._value == 8:
            self._color = '#757575'
        elif self._value == 16:
            self._color = '#FFCDD2'
        elif self._value == 32:
            self._color = '#03A9F4'
        elif self._value == 64:
            self._color = '#FFF9800'
        elif self._value == 128:
            self._color = '#E91E63'
        elif self._value == 256:
            self._color = '#CDDC39'
        elif self._value == 512:
            self._color = '#E040FB'
        elif self._value == 1024:
            self._color = '#7C4DFF'
        elif self._value == 2048:
            print('value is 2048, setting color...')
            self._color = '#D32F2F'
