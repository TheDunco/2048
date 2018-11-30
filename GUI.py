'''GUI for 2048 Game
CS108 Final Project
Created Fall 2018
@author: Duncan Van Keulen
'''

from tkinter import *

class GUI:

    def __init__(self, window):
        '''Constructor for GUI class'''

        BOARD_WIDTH = 1000
        BOARD_HEIGHT = 1000

        HEADER_WIDTH = BOARD_WIDTH
        HEADER_WIDTH = BOARD_HEIGHT/2

        self._window = window
        self._window.bind('<Key>', self.key_event_handler)

    def key_event_handler(self, event):
        '''Handle the keyboard events of arrow keys and WASD'''

        if event.keysym == 'Right' or event.keysym == 'd':
            pass
            # self.move_tiles('right')
        if event.keysym == 'Left' or event.keysym == 'a':
            pass
            # self.move_tiles('left')
        if event.keysym == 'Up' or event.keysym == 'w':
            pass
            # self.move_tiles('up')
        if event.keysym == 'Down' or event.keysym == 's':
            pass
            # self.move_tiles('down')




if __name__ == '__main__':
    root = Tk()
    root.title('2048')
    app = GUI(root)
    root.mainloop()
