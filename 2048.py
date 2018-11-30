'''2048 Game
CS108 Final Project
Created Fall 2018
@author: Duncan Van Keulen
'''

from GUI import *
from tile import *
from tkinter import *


class Twenty48:

    def __init__(self):
        self._occupied_tiles = [False, False, False, False,
                                False, False, False, False,
                                False, False, False, False,
                                False, False, False, False]
        root = Tk()
        root.title('2048')
        app = GUI(root)
        root.mainloop()


if __name__ == '__main__':
    game = Twenty48()
    

