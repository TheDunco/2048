'''GUI for 2048 Game
CS108 Final Project
Created Fall 2018
@author: Duncan Van Keulen
'''

from tkinter import *
from coords import *
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

        # FIXME: Display score!!!
        self._score = IntVar()

        self._window = window
        self._window.bind('<Key>', self.key_event_handler)
        self._window.protocol('WM_DELETE_WINDOW', self.safe_exit)

        # Create the header
        self._header = Frame(self._window, bg='#FFFFFF', width=HEADER_WIDTH, height=HEADER_HEIGHT)

        # Create the board canvas
        self._board = Canvas(self._window, bg='#EEEEEE', width=BOARD_WIDTH, height=BOARD_HEIGHT)

        self.draw_board()
        self.draw_header()

        self._game = Twenty48(self._board, self)

        self.new_game()

    def refresh(self):
        self._board.delete(ALL)
        self.draw_board()
        self._game.draw_tiles()
        self._board.update()

    def draw_header(self):

        # Destory all the widgets in the header frame
        for widget in self._header.winfo_children():
            widget.destroy()

        self._header.grid(row=0, column=0, sticky=W + E)

        # Create the title object for the header
        title = Label(self._header, text='2048', font=('Roboto', 36), bg='#FFFFFF')
        title.grid(row=0, column=0, sticky=NW)

        # Create the new game button for the header
        new_game = Button(self._header, text='New Game', font=('Roboto', 16), bg='#FFFFFF', command=self.new_game)
        new_game.grid(row=1, column=0, sticky=NW)

        # Create the score display
        score_label = Label(self._header, text='Score: ', font=('Roboto', 16 ), bg='#FFFFFF').grid(column=1, row=0)
        score_var = Label(self._header, textvar=str(self._score), font=('Roboto', 16 ), bg='#FFFFFF').grid(column=2, row=0)

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
        try:
            if event.keysym == 'Up' or event.keysym == 'w':
                self._game.move_tiles('up')

            elif event.keysym == 'Down' or event.keysym == 's':
                self._game.move_tiles('down')

            elif event.keysym == 'Right' or event.keysym == 'd':
                self._game.move_tiles('right')

            elif event.keysym == 'Left' or event.keysym == 'a':
                self._game.move_tiles('left')

        except ValueError:
            pass

    def set_score(self, score):
        self._score.set(score)

    def safe_exit(self):
        '''Turn off the event loop before closing the GUI'''

        self._terminated = True
        self._window.destroy()

    def new_game(self):
        '''Start a new game'''
        self._board.delete(ALL)
        self._game.set_score(0)
        self._score.set(0)
        self.draw_board()
        self._game.init_vals_list()
        self._game.spawn_tile(2)
        self._game.draw_tiles()

    def get_board(self):
        return self._board

if __name__ == '__main__':
    root = Tk()
    root.title('2048')
    app = GUI(root)
    root.mainloop()

