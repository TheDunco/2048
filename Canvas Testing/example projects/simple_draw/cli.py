'''
A (very) limited command-line (non-graphical) interface to Simple(non)Draw...

Created Summer, 2015

@author: kvlinden
'''
from figure import *


print('Welcome to Simple(non)Draw.')
figures = []

while True:
    try:
        # Print the current list of figures.
        if len(figures) > 0:
            print('Figures: ')
            for figure in figures:
                print('\t{0}'.format(figure))
            
        # Allow the user to specify another figure.
        print('Specify a figure (Line, Squiggle, Rectangle or Ellipse). ')
        type = input('\ttype: ').lower()
        if type == 'line':
            figures.append(Line((int(input('\tx1: ')),
                                 int(input('\ty1: '))),
                                (int(input('\tx2: ')),
                                 int(input('\ty2: '))),
                                color=input('\tcolor: ')))
        elif type == 'rectangle':
            figures.append(Rectangle((int(input('\tx: ')),
                                      int(input('\ty: '))),
                                     (int(input('\twidth: ')),
                                      int(input('\theight: '))),
                                     color=input('\tcolor: '),
                                     filled=bool(input('\tfilled (1==True/enter==False): '))))
        elif type == 'ellipse':
            figures.append(Ellipse((int(input('\tx: ')),
                                    int(input('\ty: '))),
                                   (int(input('\twidth: ')),
                                    int(input('\theight: '))),
                                   color=input('\tcolor: '),
                                   filled=bool(input('\tfilled (1==True/enter==False): '))))
        else:
            print('Invalid figure type - try again...')
            
    except ValueError as e:
        print(e, 'Try again...')

print('Good bye...')
