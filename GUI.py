'''GUI for 2048 Game
CS108 Final Project
Created Fall 2018
@author: Duncan Van Keulen
'''

from tkinter import *
from coords import *
from tile import *
from game import *

# Set the board width and height variables
BOARD_WIDTH = 400
BOARD_HEIGHT = 400

BOARD_LINE_COLOR = '#222222'

# Set the header width and height variables
HEADER_WIDTH = 400
HEADER_HEIGHT = 200


class GUI:

    def __init__(self, window):
        '''Constructor for GUI class'''

        self._terminated = False

        self._window = window
        self._window.bind('<Key>', self.key_event_handler)

        # Create the board canvas
        self._board = Canvas(self._window, bg='#CCCCCC', width=BOARD_WIDTH, height=BOARD_HEIGHT)

        # Create the header
        header = Frame(self._window, bg='#FFFFFF', width=HEADER_WIDTH, height=HEADER_HEIGHT)
        header.grid(row=0, column=0, sticky=W+E)

        # Create the title object for the header
        title = Label(header, text='2048', font=('Roboto', 36), bg='#FFFFFF')
        title.grid(row=0, column=0, sticky=NW)

        # Create the new game button for the header
        new_game = Button(header, text='New Game', font=('Roboto', 16), bg='#FFFFFF', command=self.new_game)
        new_game.grid(row=1, column=0, sticky=NW)

        self.draw_board()

        self._game = Twenty48()

        self.go()

        # Early test code
        # test_tile = Tile(2048)
        # print(test_tile.get_color())
        # print(test_tile.get_value())
        # test_tile.set_color()
        # print(test_tile.get_color())
        # test_tile.render_tile(self._board)
        # test_tile.set_position_coords(SPACE1)
        # self._board.delete(ALL)
        # self.draw_board()
        # test_tile.render_tile(self._board)

    def go(self):
        while not self._terminated:
            self._game.spawn_tile()
            for tile in self._game.get_tiles_list():
                tile.set_color()
                self._board.delete(ALL)
                self.draw_board()
                tile.render_tile(self._board)
            self._board.after(10)
            self._board.update()
            break

    def draw_board(self):

        self._board.grid(row=1, column=0)

        # FIXME: Put in for loops
        # Create vertical board lines
        self._board.create_line(2, 0, 2, BOARD_HEIGHT, fill=BOARD_LINE_COLOR)
        self._board.create_line(BOARD_HEIGHT, 0, BOARD_HEIGHT, BOARD_HEIGHT, fill=BOARD_LINE_COLOR)
        self._board.create_line(100, 0, 100, BOARD_HEIGHT, fill=BOARD_LINE_COLOR)
        self._board.create_line(200, 0, 200, BOARD_HEIGHT, fill=BOARD_LINE_COLOR)
        self._board.create_line(300, 0, 300, BOARD_HEIGHT, fill=BOARD_LINE_COLOR)

        # Create horizontal board lines
        self._board.create_line(0, 2, BOARD_WIDTH, 2, fill=BOARD_LINE_COLOR)
        self._board.create_line(0, BOARD_HEIGHT, BOARD_WIDTH, BOARD_HEIGHT, fill=BOARD_LINE_COLOR)
        self._board.create_line(0, 100, BOARD_WIDTH, 100, fill=BOARD_LINE_COLOR)
        self._board.create_line(0, 200, BOARD_WIDTH, 200, fill=BOARD_LINE_COLOR)
        self._board.create_line(0, 300, BOARD_WIDTH, 300, fill=BOARD_LINE_COLOR)

    def key_event_handler(self, event):
        '''Handle the keyboard events of arrow keys and WASD'''

        if event.keysym == 'Right' or event.keysym == 'd':
            print('right')
            # self.move_tiles('right')

        if event.keysym == 'Left' or event.keysym == 'a':
            print('left')
            # self.move_tiles('left')

        if event.keysym == 'Up' or event.keysym == 'w':
            print('up')
            # self.move_tiles('up')

        if event.keysym == 'Down' or event.keysym == 's':
            print('down')
            # self.move_tiles('down')

    def new_game(self):
        # FIXME: Command for new game button
        self._game.spawn_tile()
        self._board.after(10)
        self._board.update()
        self.go()

    def get_board(self):
        return self._board


if __name__ == '__main__':
    root = Tk()
    root.title('2048')
    app = GUI(root)
    root.mainloop()

