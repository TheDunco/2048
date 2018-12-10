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

        # Set the high score to the score in the file
        self._high_score = IntVar()
        with open('high_score.txt', 'r') as hs:
            for line in hs:
                self._high_score.set(line)

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
        if self._score.get() > self._high_score.get():
            self._high_score.set(self._score.get())
            try:
                with open('high_score.txt', 'w') as hs:
                    hs.write(str(self._score.get()))
            except PermissionError:
                pass

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

        spacer = Label(self._header, text='                                     ', bg='#FFFFFF').grid(row=0, column=1)

        # Create the score display
        score_label = Label(self._header, text='Score: ', font=('Roboto', 16 ), bg='#FFFFFF')
        score_label.grid(column=2, row=0, sticky=W)

        score_var = Label(self._header, textvar=str(self._score), font=('Roboto', 16 ), bg='#FFFFFF')
        score_var.grid(column=3, row=0)

        high_score_label = Label(self._header, text='High Score: ', font=('Roboto', 16 ), bg='#FFFFFF')
        high_score_label.grid(column=2, row=1)

        high_score_var = Label(self._header, textvar=str(self._high_score), font=('Roboto', 16 ), bg='#FFFFFF')
        high_score_var.grid(column=3, row=1)

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

            elif event.keysym == 'q':
                self.game_over()

        except ValueError:
            pass

    def game_over(self):
        print('Game over')
        # self._board.delete(ALL)
        self._board.create_text((200, 150), text='Game Over!', font=('Roboto', 24))

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

