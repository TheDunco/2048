'''
Expanding circles...

Created on Nov 17, 2014
Updated Summer, 2015

@author: smn4
@author kvlinden, ds33
'''
from tkinter import *
from random import randint

def get_random_color():
    '''Generate random color intensities for red, green & blue and convert them to hex.'''
    return '#{:02X}{:02X}{:02X}'.format(randint(0,255), randint(0,255), randint(0,255))

class CircleAnimation:
        
    def __init__(self, window):
        self._window = window
        self._window.protocol('WM_DELETE_WINDOW', self.safe_exit)
        self._window.bind("<Button-1>", self.process_mouse_event)
        self._window.bind("<Key>", self.process_key_event)  
        
        SCREEN_WIDTH = 250
        self._x = self._y = SCREEN_WIDTH / 2
        self._radius = 0
        self._dx = 1
        self._color = get_random_color()
        self._rate = 10  # wait time between frames

        canvas = Canvas(self._window, bg='white', width=SCREEN_WIDTH, height=SCREEN_WIDTH)
        canvas.pack()
        
        # Run the animation.
        self._terminated = False
        while not self._terminated:
            canvas.delete(ALL)
            canvas.create_oval(self._x - self._radius,
                               self._y - self._radius, 
                               self._x + self._radius, 
                               self._y + self._radius, 
                               fill=self._color)
            if (self._radius < 0 or self._radius > SCREEN_WIDTH / 2):
                self._dx *= -1
            self._radius += self._dx    
            canvas.after(self._rate)
            canvas.update()
            
    def process_mouse_event(self, event):
        '''Restart the expanding circle at the point of the mouse click'''
#         print('Clicked at', event.x, event.y)        
        self._x = event.x
        self._y = event.y
        self._radius = 0
        self._color = get_random_color()
    
    def process_key_event(self, event):
        '''Move the expanding circle's center based on the arrow keys.
           Also, change color using the 'c' key.
        '''
        # print('keysym?', event.keysym)
        if event.keysym == 'Right':
            self._x += 5
        elif event.keysym == 'Left':
            self._x -= 5
        elif event.keysym == 'Up':
            self._y -= 5
        elif event.keysym == 'Down':
            self._y += 5
        elif event.keysym == 'c' or event.keysym == 'C':
            self._color = get_random_color()
            
    def safe_exit(self):
        ''' Terminate the animation before shutting down the GUI window. '''
        self._terminated = True
        self._window.destroy()


if __name__ == '__main__':
    root = Tk()
    root.title('Those crazy circles...')    
    app = CircleAnimation(root)
    root.mainloop()
