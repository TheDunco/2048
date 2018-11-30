'''Tile Class for 2048 Game
CS108 Final Project
Created Fall 2018
@author: Duncan Van Keulen
'''

import random

class Tile:
    '''Tile class for 2048 game'''

    def __init__(self, value):
        self._value = value
        self._color = '#BBBBBB'
        self._x = 0
        self._y = 0

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
