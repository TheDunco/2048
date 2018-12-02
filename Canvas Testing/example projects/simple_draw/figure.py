'''
Figure classes for a canvas-based SimpleDraw application...

Created Summer, 2015

@author: kvlinden
'''
import math
from tkinter import Tk, Canvas


class Figure:
    ''' The parent class for all figures '''
    
    def __init__(self, start, color):
        ''' Create a new figure object '''
        if not self._check_point(start):
            raise ValueError('Illegal start point: {0}'.format(start))
        self.start = start
        self.color = color 
        self.width = 2 
        
    def set_color(self, color):
        ''' Set the figure (fill & border) color '''
        self.color = color
    
    def __str__(self):
        return 'Figure: {0} {1}'.format(self.start, self.color)
    
    def _check_point(self, p):
        ''' Check that the point is on the visible canvas - p must be a x-y tuple '''
        return p[0] >= 0 and p[1] >= 0


class Line(Figure):
    ''' A figure class for simple lines '''
    
    def __init__(self, start=(0, 0), end=(10, 10), color='black'):
        Figure.__init__(self, start, color)
        if (end[0] < 0) or (end[1] < 0):
            raise ValueError('Illegal end point: {0}'.format(end))
        self.end = end
        
    def render(self, canvas):
        ''' Draw the line on the given canvas '''
        canvas.create_line(self.start, self.end, fill=self.color, width=self.width)
    
    def get_length(self):
        ''' Return the length of the line '''
        return ((self.start[0] - self.end[0])**2 + (self.start[1] - self.end[1])**2)**0.5 

    def __str__(self):
        return 'Line: {0} {1} {2}'.format(self.start, self.end, self.color)
    
    def check_overlap(self, other):
        ''' Checking overlap for various figures would be good. '''
        pass


class Squiggle(Figure):
    ''' A figure class for a user-drawn, potentially curved line '''
    
    def __init__(self, start=(0, 0), color='black'):
        ''' Create a new squiggle object with a single point '''
        if (start[0] < 0) or (start[1] < 0):
            raise ValueError('Illegal start point: {0}'.format(start))
        Figure.__init__(self, start, color)
        self.points = [start]
        
    def add_point(self, point):
        ''' Add an additional point to the squiggle - Points must be added sequentially. '''
        if not self._check_point(point):
            raise ValueError('Illegal point: {0}'.format(point))
        self.points.append(point)
        
    def render(self, canvas):
        ''' Draw the squiggle on the give canvas by connecting the points in order '''
        if len(self.points) > 1:
            for i in range(1, len(self.points)):
                canvas.create_line(self.points[i - 1], self.points[i], fill=self.color, width=self.width)

    def check_overlap(self, other):
        ''' Checking overlap for various figures would be good. '''
        pass


class ClosedFigure(Figure):
    ''' A figure class for boxed, closed figures '''

    def __init__(self, start, dimensions, color, filled):
        Figure.__init__(self, start, color)
        self.dimensions = dimensions
        self.filled = filled
        if self.filled:
            self.fill_color = self.color
        else:
            self.fill_color = None
            
    def _get_end_point(self):
        ''' 
        Return the endpoint needed by the Tk graphics routines; 
        it is based on start position and the dimensions. 
        '''
        return (self.start[0] + self.dimensions[0], self.start[1] + self.dimensions[1])
            

class Rectangle(ClosedFigure):
    ''' A figure class for a simple rectangle '''
    
    def __init__(self, start=(0, 0), dimensions=(10, 10), color='black', filled=False):
        ''' Create a new rectangle object using the given parameters '''
        ClosedFigure.__init__(self, start, dimensions, color, filled)
    
    def render(self, canvas):
        ''' Draw the rectangle on the given canvas '''
        canvas.create_rectangle(self.start, self._get_end_point(), fill=self.fill_color, outline=self.color, width=self.width)

    def get_area(self):
        ''' Return the area of the rectangle '''
        return self.dimensions[0] * self.dimensions[1]
    
    def check_overlap(self, other):
        ''' Checking overlap for various figures would be good. '''
        pass

    def __str__(self):
        if self.filled:
            filled = 'filled'
        else:
            filled = 'unfilled'
        return 'Rectangle: {0} {1} {2} {3}'.format(self.start, self.dimensions, self.color, filled)   


class Ellipse(ClosedFigure):
    ''' A figure class for ellipses '''
    
    def __init__(self, start=(0, 0), dimensions=(10, 10), color='black', filled=False):
        ''' Create a new ellipse object using the given parameters '''
        ClosedFigure.__init__(self, start, dimensions, color, filled)
    
    def render(self, canvas):
        ''' Draw the ellipse on the given canvas '''
        canvas.create_oval(self.start, self._get_end_point(), fill=self.fill_color, outline=self.color, width=self.width)
       
    def get_area(self):
        ''' Return the area of the ellipse '''
        return math.pi * self.dimensions[0] * self.dimensions[1]
    
    def check_overlap(self, other):
        ''' Checking overlap for various figures would be good. '''
        pass


    def __str__(self):
        if self.filled:
            filled = 'filled'
        else:
            filled = 'unfilled'
        return 'Ellipse: {0} {1} {2} {3}'.format(self.start, self.dimensions, self.color, filled)   


if __name__ == '__main__':
    
    figures = []
    
    figures.append(Rectangle((10, 10), (200, 200), color='green'))
    figures.append(Ellipse((100, 100), (100, 100), color='red', filled=True))
    figures.append(Line((90, 90), (200, 200), color='purple'))
    
    for figure in figures:
        print(figure)
    