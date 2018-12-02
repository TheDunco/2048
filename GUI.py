'''GUI for 2048 Game
CS108 Final Project
Created Fall 2018
@author: Duncan Van Keulen
'''

from tkinter import *
from tile import *
from game import Twenty48

class GUI:

    def __init__(self, window):
        '''Constructor for GUI class'''

        # Set the board width and height variables
        BOARD_WIDTH = 400
        BOARD_HEIGHT = 400

        # Set the header width and height variables
        HEADER_WIDTH = BOARD_WIDTH
        HEADER_HEIGHT = BOARD_HEIGHT/2

        self._window = window
        self._window.bind('<Key>', self.key_event_handler)

        # Create the header
        header = Frame(self._window, bg='#FFFFFF', width=HEADER_WIDTH, height=HEADER_HEIGHT)
        header.grid(row=0, column=0, sticky=W+E)

        # Create the title object for the header
        title = Label(header, text='2048', font=('Roboto', 36), bg='#FFFFFF')
        title.grid(row=0, column=0, sticky=NW)

        # Create the new game button for the header
        new_game = Button(header, text='New Game', font=('Roboto', 16), bg='#FFFFFF', command=self.new_game)
        new_game.grid(row=1, column=0, sticky=NW)

        # Create the board
        self._board = Canvas(self._window, bg='#CCCCCC', width=BOARD_WIDTH, height=BOARD_HEIGHT)
        self._board.grid(row=1, column=0)

        BOARD_LINE_COLOR = '#222222'

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

        self._board_tile_coords = [
            [(0,0), (100,100)], [(100,0), (200,100)], [(200,0), (300, 100)], [(300,0), (400,100)],
            [(0,100), (100,200)], [(100,100), (200,200)], [(200,100), (300,200)], [(300,100), (400,200)],
            [(0,200), (100,300)], [(100,200), (200,300)], [(200,200), (300,300)], [(300,200), (400,300)],
            [(0,300), (100,400)], [(100,300), (200,400)], [(200,300), (300,400)], [(300,300), (400,400)]
        ]

        test_tile = Tile(2048)
        print(test_tile.get_color())
        print(test_tile.get_value())
        test_tile.set_color()
        print(test_tile.get_color())
        test_tile.render_tile(self._board)

    def key_event_handler(self, event):
        '''Handle the keyboard events of arrow keys and WASD'''

        if event.keysym == 'Right' or event.keysym == 'd':
            print('right')
            # self.move_tiles('right')
            # spawn_tiles()
        if event.keysym == 'Left' or event.keysym == 'a':
            print('left')
            # self.move_tiles('left')
            # spawn_tiles()
        if event.keysym == 'Up' or event.keysym == 'w':
            print('up')
            # self.move_tiles('up')
            # spawn_tiles()
        if event.keysym == 'Down' or event.keysym == 's':
            print('down')
            # self.move_tiles('down')
            # spawn_tiles()

    def new_game(self):
        # FIXME: Command for new game button
        print('New Game')

    def get_board(self):
        return self._board


if __name__ == '__main__':
    root = Tk()
    root.title('2048')
    app = GUI(root)
    root.mainloop()

