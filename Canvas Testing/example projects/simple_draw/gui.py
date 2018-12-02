'''
The SimpleDraw interface...

Created Summer, 2015

@author: kvlinden
'''
from tkinter import *
from figure import *


class SimpleDraw:
    '''
    This class provides the GUI for the SimpleDraw figure editor.
    '''
    
    def __init__(self, window):
        ''' Create the GUI and the list of figures '''
        
        # The main drawing canvas
        self.canvas = Canvas(window, width=400, height=300, background='white')
        self.canvas.pack()
        self.canvas.bind('<Button-1>', self.process_mouse_press)
        self.canvas.bind('<B1-Motion>', self.process_mouse_motion)
        self.canvas.bind('<ButtonRelease-1>', self.process_mouse_release)
        
        # The list of model objects, which starts empty
        self.figures = []
        
        # The figure mode panel
        figure_frame = Frame(window)
        figure_frame.pack(anchor=W)
        FIGURES = [('Line', 'line'), ('Rectangle', 'rectangle'), ('Ellipse', 'ellipse'), ('Squiggle', 'squiggle')]
        self.figure_variable = StringVar()
        self.figure_variable.set('line')
        for t, v in FIGURES:
            b = Radiobutton(figure_frame, text=t, value=v, variable=self.figure_variable)
            b.pack(side=LEFT)

        # The color mode panel
        color_frame = Frame(window)
        color_frame.pack(anchor=W)
        COLORS = [('Black', 'Black'), ('Red', 'Red'), ('Green', 'Green'), ('Blue', 'Blue')]
        self.color_variable = StringVar()
        self.color_variable.set('Black')
        for t, v in COLORS:
            b = Radiobutton(color_frame, text=t, value=v, variable=self.color_variable)
            b.pack(side=LEFT)

        # The fill mode panel
        fill_frame = Frame(window)
        fill_frame.pack(anchor=W)
        FILL_VALUES = [('UnFilled', False), ('Filled', True)]
        self.fill_variable = BooleanVar()
        self.fill_variable.set(False)
        for t, v in FILL_VALUES:
            b = Radiobutton(fill_frame, text=t, value=v, variable=self.fill_variable)
            b.pack(side=LEFT)
        
    def process_mouse_press(self, event):
        ''' Start a new figure where the user presses the mouse based on the mode settings '''
        self.x = event.x
        self.y = event.y
        self.temporary_figure = self.create_figure(event, self.fill_variable.get(), self.color_variable.get())
        self.temporary_figure.render(self.canvas)

    def process_mouse_motion(self, event):
        ''' Display a temporary version of the figure and erase the previous temporary version '''
        if self.figure_variable.get() == 'squiggle':
            # Squiggles are special in that they don't have temporary versions.
            self.temporary_figure.add_point((event.x, event.y))
            self.temporary_figure.render(self.canvas)
        else:
            # Erase the previous version by redrawing it in white.
            self.temporary_figure.set_color('White')
            self.temporary_figure.render(self.canvas)
            self.temporary_figure = self.create_figure(event, self.fill_variable.get(), self.color_variable.get())
            self.temporary_figure.render(self.canvas)

    def process_mouse_release(self, event):
        ''' Create and save the final version of the figure '''
        if self.figure_variable.get() == 'squiggle':
            self.temporary_figure.add_point((event.x, event.y))
            self.figures.append(self.temporary_figure)
        else:
            self.figures.append(self.create_figure(event, self.fill_variable.get(), self.color_variable.get()))
        self.draw_figures()
        
    def create_figure(self, event, filled, color):
        ''' 
        Create a figure, temporary or permanent, based on the given mode settings
        The calls to the constructors for closed figures must convert upper-left and lower-right
        points into upper-left point and dimensions for the constructors.
        '''
        if self.figure_variable.get() == 'line':
            return Line((self.x, self.y), (event.x, event.y), color=color)
        elif self.figure_variable.get() == 'rectangle':
            return Rectangle((self.x, self.y), (event.x-self.x, event.y-self.y), filled=filled, color=color)
        elif self.figure_variable.get() == 'ellipse':
            return Ellipse((self.x, self.y), (event.x-self.x, event.y-self.y), filled=filled, color=color)
        elif self.figure_variable.get() == 'squiggle':
            return Squiggle((self.x, self.y), color=color)
    
    def draw_figures(self):
        ''' Redraw all the stored figures '''
        self.canvas.delete(ALL);
        for figure in self.figures:
            figure.render(self.canvas)

        
if __name__ == '__main__':
    root = Tk()
    root.title('SimpleDraw')
    app = SimpleDraw(root)
    root.mainloop()
