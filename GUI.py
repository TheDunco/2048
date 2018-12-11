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

# FIXME: Implement help/how to play menu
# FIXME: Add color schemes
# FIXME: Merging issues


class GUI:
    '''
    GUI Class for 2048 game.
    Receives a tkinter object
    Handles drawing and refreshing the screen as well as menus
    '''

    def __init__(self, window):
        '''Constructor for GUI class'''

        # Initialize the score wrapper variable
        self._score = IntVar()

        # Set the high score to the score in the file
        self._high_score = IntVar()
        with open('high_score.txt', 'r') as hs:
            for line in hs:
                self._high_score.set(line)

        # Set up general window and key bindings
        self._window = window
        self._window.bind('<Key>', self.key_event_handler)
        self._window.protocol('WM_DELETE_WINDOW', self.safe_exit)

        # Create the header
        self._header = Frame(self._window, bg='#FFFFFF', width=HEADER_WIDTH, height=HEADER_HEIGHT)

        # Create the board canvas
        self._board = Canvas(self._window, bg='#EEEEEE', width=BOARD_WIDTH, height=BOARD_HEIGHT)

        # Initially draw the header and board
        self.draw_board()
        self.draw_header()

        # Create a game object and pass it the instance of the GUI object
        self._game = Twenty48(self._board, self)

        # Set the color scheme of the game
        self._game.set_color_scheme('red')

        # Start a new game
        self.new_game()

    def refresh(self):
        '''Refresh the screen'''

        # Clear the board and all tiles
        self._board.delete(ALL)
        # Redraw the board
        self.draw_board()
        # Redraw tiles in current state
        self._game.draw_tiles()
        # Updtate the board
        self._board.update()

        # High score updating
        if self._score.get() > self._high_score.get():
            self._high_score.set(self._score.get())
            try:
                with open('high_score.txt', 'w') as hs:
                    hs.write(str(self._score.get()))
            except PermissionError:
                pass

    def draw_header(self):
        '''Draw the header with new game and scores'''

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

        spacer = Label(self._header, text='                             ', bg='#FFFFFF').grid(row=0, column=1)

        # Create the score display label
        score_label = Label(self._header, text='Score: ', font=('Roboto', 16 ), bg='#FFFFFF')
        score_label.grid(column=2, row=0, sticky=W)

        # Create the score display variable
        score_var = Label(self._header, textvar=str(self._score), font=('Roboto', 16 ), bg='#FFFFFF')
        score_var.grid(column=3, row=0)

        # Create the high score display label
        high_score_label = Label(self._header, text='High Score: ', font=('Roboto', 16 ), bg='#FFFFFF')
        high_score_label.grid(column=2, row=1)

        # Create the high score display variable
        high_score_var = Label(self._header, textvar=str(self._high_score), font=('Roboto', 16), bg='#FFFFFF')
        high_score_var.grid(column=3, row=1)

    def draw_board(self):
        '''Draw the play board'''

        # Grid (pack) the board initialized in the constructor
        self._board.grid(row=2, column=0)

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

    def game_win(self):
        '''Draw the winner label'''
        win = Label(self._window, text='Congratulations! You win!', bg="#FFFFFF", font=('Roboto', 24, 'bold'))
        win.grid(row=1, column=0)

    def draw_help_screen(self):
        '''Draw the "how to play" tip'''

        # Create the instructional help label below the board
        help_label = Label(self._window,
                           text='Use arrow keys or WASD to move tiles.\nLike tiles merge. Get 2048 tile to win.',
                           font=('Roboto', 16))
        help_label.grid(row=3, column=0, columnspan=1)

        help_label2 = Label(self._window,
                           text='"Q": End game | "P": Reset high score\n"T": Playful scheme | "Y": Red scheme\n"U": Blue scheme',
                           font=('Roboto', 16))
        help_label2.grid(row=4, column=0, columnspan=1)

    def key_event_handler(self, event):
        '''Handle the keyboard events of arrow keys and WASD'''

        try:
            # Movement key bindings...
            if event.keysym == 'Up' or event.keysym == 'w':
                self._game.move_tiles('up')

            elif event.keysym == 'Down' or event.keysym == 's':
                self._game.move_tiles('down')

            elif event.keysym == 'Right' or event.keysym == 'd':
                self._game.move_tiles('right')

            elif event.keysym == 'Left' or event.keysym == 'a':
                self._game.move_tiles('left')

            # Quit keybinding
            elif event.keysym == 'q':
                self.game_over()
                self._board.update()
                self.safe_exit()

            # Help screen keybinding
            elif event.keysym == 'h':
                self.draw_help_screen()

            # Keybinding for resetting the high score
            elif event.keysym == 'p':
                print('Resetting high score')
                with open('high_score.txt', 'w') as file:
                    file.write('0')
                self.safe_exit()

            # Keybinding for setting color scheme to playful
            elif event.keysym == 't':
                self._game.set_color_scheme('playful')

            # Keybinding for for setting color scheme to warm
            elif event.keysym == 'y':
                self._game.set_color_scheme('red')

            elif event.keysym == 'u':
                self._game.set_color_scheme('blue')

        except ValueError:
            pass

    def game_over(self):
        '''Displays if the game is over'''

        # Create game over label
        self._board.create_text((200, 140), text='Game Over!', font=('Roboto', 36, 'bold', 'underline'))
        # FIXME: Make an entry field appear for username of high score if score was beat...

    def set_score(self, score):
        '''Mutator for the score wrapper variable'''
        self._score.set(score)

    def safe_exit(self):
        '''Destroy the window and exit python'''

        self._window.destroy()
        exit()

    def new_game(self):
        '''Start a new game'''

        # Clear the board
        self._board.delete(ALL)

        # Set the score to 0
        self._game.set_score(0)
        self._score.set(0)

        # Redraw the board
        self.draw_board()

        # Initialize the tile values list and spawn 2 tiles
        self._game.init_vals_list()
        self._game.spawn_tile(2)

        # Draw the tiles
        self._game.draw_tiles()

    def get_board(self):
        '''Accessor for the board frame'''
        return self._board


if __name__ == '__main__':
    # Initialize a Tkinter object and run the mainloop
    root = Tk()
    root.title('2048')
    app = GUI(root)
    root.mainloop()
