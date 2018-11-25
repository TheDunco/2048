

from tkinter import *

master = Tk()

w = Canvas(master, width=200, height=100)
w.pack()

w.create_line(0, 0, 200, 100)
w.create_line(0, 100, 200, 0, fill='red', dash=(4,4))

w.create_rectangle(50, 25, 150, 75, fill='blue')

'''
Tkinter Canvas Guide:
http://effbot.org/tkinterbook/canvas.htm

i = w.create_line(<xy>, fill='red')

w.coords(i, <new_xy>) # Change coordinates
w.itemconfig(<i>, fill='<color>')

w.delete(i) # Remove

w.delete(ALL) # Remove all items

Canvas supports:
- Arc (arc, chord, or pieslice)
- Bitmap (built-in or read from XBM file)
- Image (a BitmapImage or PhotoImage instance)
- Line
- Oval (Circle or ellipse)
- Polygon
- Rectangle
- Text
- Window

Chords, pieslices, ovals, polygons, and rectangles consist of both an outline and an interior area, either of which can
be made transparent (and if you insist, you can make both transparent).

Window items are used to place other Tkinter widgets on top of the canvas; for these items, the Canvas widget simply
acts like a geometry manager.

You can also write your own item types in C or C++ and plug them into Tkinter via Python extension modules.
'''


mainloop()