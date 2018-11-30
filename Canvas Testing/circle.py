'''
Expanding circles - base code ...

Created on Nov 17, 2014
Updated Summer, 2015

@author smn4
@author kvlinden
'''

from tkinter import *
from random import randint


def get_random_color():
    ''' Generate random color intensities for red, green & blue and convert them to hex. '''
    return '#{:02X}{:02X}{:02X}'.format(randint(0, 255), randint(0, 255), randint(0, 255))


class CircleAnimation:
        
    def __init__(self, window):
        self._window = window
        self._window.protocol('WM_DELETE_WINDOW', self.safe_exit)    
        
        WIDTH = 250
        HEIGHT = WIDTH
        canvas = Canvas(self._window,
                        background='white',
                        width=WIDTH,
                        height=HEIGHT)
        canvas.pack()

        radius = 50
        color = get_random_color()
        self._terminated = False
        while not self._terminated:
            canvas.create_oval((WIDTH / 2) - radius, (HEIGHT / 2) - radius, (WIDTH / 2) + radius, (HEIGHT / 2) + radius,
                               fill=color)

            color = get_random_color()

            radius += 1
            canvas.after(40)
            canvas.update()

        # canvas.create_oval((WIDTH/2)-radius, (HEIGHT/2)-radius, (WIDTH/2)+radius, (HEIGHT/2)+radius)
        #
        # canvas.create_line(20,20, 200,200, fill='blue')
        #
        # canvas.create_rectangle(10,10, 50,50, fill=get_random_color())

    def safe_exit(self):
        ''' Terminate the animation before shutting down the GUI window. '''
        self._terminated = True
        self._window.destroy()
        
        
if __name__ == '__main__':
    root = Tk()
    root.title('Those crazy circles...')    
    app = CircleAnimation(root)
    root.mainloop()
