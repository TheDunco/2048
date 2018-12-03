'''Constants for all of the board space coordinates for 2048 game
CS108 Final Project
Created Fall 2018
@author: Duncan Van Keulen
'''

BOARD_SPACE_COORDS = [
    [(0, 0), (100, 100)], [(100, 0), (200, 100)], [(200, 0), (300, 100)], [(300, 0), (400, 100)],
    [(0, 100), (100, 200)], [(100, 100), (200, 200)], [(200, 100), (300, 200)], [(300, 100), (400, 200)],
    [(0, 200), (100, 300)], [(100, 200), (200, 300)], [(200, 200), (300, 300)], [(300, 200), (400, 300)],
    [(0, 300), (100, 400)], [(100, 300), (200, 400)], [(200, 300), (300, 400)], [(300, 300), (400, 400)]
]

BOARD_CENTER_SPACE_COORDS = [
    (50,50), (150,50), (250,50), (350,50),
    (50,150), (150,150), (250,150), (350,150),
    (50,250), (150,250), (250,250), (350,250),
    (50,350), (150,350), (250,350), (350,350)

]

SPACE0 = {
    'x1': 0, 'y1': 100,
    'x2': 0, 'y2': 100,
    'cx': 50, 'cy': 50,
    'id': 0, 'oc': False
}

SPACE1 = {
    'x1': 100, 'y1': 0,
    'x2': 200, 'y2': 100,
    'cx': 150, 'cy': 50,
    'id': 1, 'oc': False
}

SPACE2 = {
    'x1': 200, 'y1': 0,
    'x2': 300, 'y2': 100,
    'cx': 250, 'cy': 50,
    'id': 2, 'oc': False
}

SPACE3 = {
    'x1': 300, 'y1': 0,
    'x2': 400, 'y2': 100,
    'cx': 350, 'cy': 50,
    'id': 3, 'oc': False
}

SPACE4 = {
    'x1': 0, 'y1': 100,
    'x2': 100, 'y2': 200,
    'cx': 50, 'cy': 150,
    'id': 4, 'oc': False
}

SPACE5 = {
    'x1': 100, 'y1': 100,
    'x2': 200, 'y2': 200,
    'cx': 150, 'cy': 150,
    'id': 5, 'oc': False
}

SPACE6 = {
    'x1': 200, 'y1': 100,
    'x2': 300, 'y2': 200,
    'cx': 250, 'cy': 150,
    'id': 6, 'oc': False
}

SPACE7 = {
    'x1': 300, 'y1': 100,
    'x2': 400, 'y2': 200,
    'cx': 350, 'cy': 150,
    'id': 7, 'oc': False
}

SPACE8 = {
    'x1': 0, 'y1': 200,
    'x2': 100, 'y2': 300,
    'cx': 50, 'cy': 250,
    'id': 8, 'oc': False
}

SPACE9 = {
    'x1': 100, 'y1': 200,
    'x2': 200, 'y2': 300,
    'cx': 150, 'cy': 250,
    'id': 9, 'oc': False
}

SPACE10 = {
    'x1': 200, 'y1': 200,
    'x2': 300, 'y2': 300,
    'cx': 250, 'cy': 250,
    'id': 10, 'oc': False
}

SPACE11 = {
    'x1': 300, 'y1': 200,
    'x2': 400, 'y2': 300,
    'cx': 350, 'cy': 250,
    'id': 11, 'oc': False
}

SPACE12 = {
    'x1': 0, 'y1': 300,
    'x2': 100, 'y2': 400,
    'cx': 50, 'cy': 350,
    'id': 12, 'oc': False
}

SPACE13 = {
    'x1': 100, 'y1': 100,
    'x2': 200, 'y2': 400,
    'cx': 150, 'cy': 350,
    'id': 13, 'oc': False
}

SPACE14 = {
    'x1': 200, 'y1': 300,
    'x2': 300, 'y2': 400,
    'cx': 250, 'cy': 350,
    'id': 14, 'oc': False
}

SPACE15 = {
    'x1': 300, 'y1': 300,
    'x2': 400, 'y2': 400,
    'cx': 350, 'cy': 350,
    'id': 15, 'oc': False
}

SPACES = [SPACE0, SPACE1, SPACE2, SPACE3,
          SPACE4, SPACE5, SPACE6, SPACE7,
          SPACE8, SPACE9, SPACE10, SPACE11,
          SPACE12, SPACE13, SPACE14, SPACE15]

ROW0 = [SPACE0, SPACE1, SPACE2, SPACE3]
ROW1 = [SPACE4, SPACE5, SPACE6, SPACE7]
ROW2 = [SPACE8, SPACE9, SPACE10, SPACE11]
ROW3 = [SPACE12, SPACE13, SPACE14, SPACE15]

COLUMN0 = [SPACE0, SPACE4, SPACE8, SPACE12]
COLUMN1 = [SPACE1, SPACE5, SPACE9, SPACE13]
COLUMN2 = [SPACE2, SPACE6, SPACE10, SPACE14]
COLUMN3 = [SPACE3, SPACE7, SPACE11, SPACE15]
