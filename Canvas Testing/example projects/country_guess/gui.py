'''
The GUI view for the country guess game

Created Summer, 2015

@author: kvlinden
'''
from tkinter import *

from game import Game


class App:
    
    def __init__(self, window):
        # Add nicer font.
        
        self._game = Game('countries.txt')
        
        main_frame = Frame(window)
        main_frame.pack(padx=10, pady=10)
        label_font = ('Helvetica')        
        
        logo = PhotoImage(file='images/who.gif')
        image_label = Label(main_frame, image=logo)
        image_label.image = logo
        image_label.pack()

        self._hint_variable = StringVar()
        self._hint_variable.set('Try to guess a country. {0}'.format(self._game.get_hint()))
        hint_label = Label(main_frame, textvariable=self._hint_variable, font=label_font)
        hint_label.pack(anchor=W)
                
        input_frame = Frame(main_frame)
        input_frame.pack(anchor=W, fill=X)
        self._entry_variable = StringVar()
        entry_field = Entry(input_frame, textvariable=self._entry_variable, font=label_font)
        entry_field.bind('<Return>', self.guess)
        entry_field.pack(side=LEFT, padx=5)
        guess_button = Button(input_frame, text='Guess', command=self.guess, font=label_font)
        guess_button.pack(side=LEFT, padx=5)
        giveup_button = Button(input_frame, text='Give Up', command=self.give_up, font=label_font)
        giveup_button.pack(side=LEFT, padx=5)
        quit_button = Button(input_frame, text='Quit', command=main_frame.quit, font=label_font)
        quit_button.pack(side=RIGHT)
    
    def guess(self, event=None):
        if self._game.check_answer(self._entry_variable.get()):
            self._game.reset()
            self._hint_variable.set('Good! Try another. {0}'.format(self._game.get_hint()))
        else:
            self._hint_variable.set('Nope... Try again. {0}'.format(self._game.get_hint()))
        self._entry_variable.set('')
            
    def give_up(self):
        answer = self._game.get_answer()
        self._game.reset()
        hint = self._game.get_hint() 
        self._hint_variable.set('The answer was {0}. Try another. {1}'.format(answer, hint))
        self._entry_variable.set('')
        

if __name__ == '__main__':
    root = Tk()
    root.title('Country Guess')
    app = App(root)
    root.mainloop()
