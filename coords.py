'''Constants for all of the board space coordinates for 2048 game
CS108 Final Project
Created Fall 2018
@author: Duncan Van Keulen
'''


class Coords:
    def __init__(self):
        self._BOARD_SPACE_COORDS = [
            [(0, 0), (100, 100)], [(100, 0), (200, 100)], [(200, 0), (300, 100)], [(300, 0), (400, 100)],
            [(0, 100), (100, 200)], [(100, 100), (200, 200)], [(200, 100), (300, 200)], [(300, 100), (400, 200)],
            [(0, 200), (100, 300)], [(100, 200), (200, 300)], [(200, 200), (300, 300)], [(300, 200), (400, 300)],
            [(0, 300), (100, 400)], [(100, 300), (200, 400)], [(200, 300), (300, 400)], [(300, 300), (400, 400)]
        ]

        self._BOARD_CENTER_SPACE_COORDS = [
            (50,50), (150,50), (250,50), (350,50),
            (50,150), (150,150), (250,150), (350,150),
            (50,250), (150,250), (250,250), (350,250),
            (50,350), (150,350), (250,350), (350,350)

        ]

        self._SPACE0 = {
            'x1': 0, 'y1': 0,
            'x2': 100, 'y2': 100,
            'cx': 50, 'cy': 50,
            'id': 0, 'oc': False
        }

        self._SPACE1 = {
            'x1': 100, 'y1': 0,
            'x2': 200, 'y2': 100,
            'cx': 150, 'cy': 50,
            'id': 1, 'oc': False
        }

        self._SPACE2 = {
            'x1': 200, 'y1': 0,
            'x2': 300, 'y2': 100,
            'cx': 250, 'cy': 50,
            'id': 2, 'oc': False
        }

        self._SPACE3 = {
            'x1': 300, 'y1': 0,
            'x2': 400, 'y2': 100,
            'cx': 350, 'cy': 50,
            'id': 3, 'oc': False
        }

        self._SPACE4 = {
            'x1': 0, 'y1': 100,
            'x2': 100, 'y2': 200,
            'cx': 50, 'cy': 150,
            'id': 4, 'oc': False
        }

        self._SPACE5 = {
            'x1': 100, 'y1': 100,
            'x2': 200, 'y2': 200,
            'cx': 150, 'cy': 150,
            'id': 5, 'oc': False
        }

        self._SPACE6 = {
            'x1': 200, 'y1': 100,
            'x2': 300, 'y2': 200,
            'cx': 250, 'cy': 150,
            'id': 6, 'oc': False
        }

        self._SPACE7 = {
            'x1': 300, 'y1': 100,
            'x2': 400, 'y2': 200,
            'cx': 350, 'cy': 150,
            'id': 7, 'oc': False
        }

        self._SPACE8 = {
            'x1': 0, 'y1': 200,
            'x2': 100, 'y2': 300,
            'cx': 50, 'cy': 250,
            'id': 8, 'oc': False
        }

        self._SPACE9 = {
            'x1': 100, 'y1': 200,
            'x2': 200, 'y2': 300,
            'cx': 150, 'cy': 250,
            'id': 9, 'oc': False
        }

        self._SPACE10 = {
            'x1': 200, 'y1': 200,
            'x2': 300, 'y2': 300,
            'cx': 250, 'cy': 250,
            'id': 10, 'oc': False
        }

        self._SPACE11 = {
            'x1': 300, 'y1': 200,
            'x2': 400, 'y2': 300,
            'cx': 350, 'cy': 250,
            'id': 11, 'oc': False
        }

        self._SPACE12 = {
            'x1': 0, 'y1': 300,
            'x2': 100, 'y2': 400,
            'cx': 50, 'cy': 350,
            'id': 12, 'oc': False
        }

        self._SPACE13 = {
            'x1': 100, 'y1': 300,
            'x2': 200, 'y2': 400,
            'cx': 150, 'cy': 350,
            'id': 13, 'oc': False
        }

        self._SPACE14 = {
            'x1': 200, 'y1': 300,
            'x2': 300, 'y2': 400,
            'cx': 250, 'cy': 350,
            'id': 14, 'oc': False
        }

        self._SPACE15 = {
            'x1': 300, 'y1': 300,
            'x2': 400, 'y2': 400,
            'cx': 350, 'cy': 350,
            'id': 15, 'oc': False
        }

        self._SPACES = [self._SPACE0, self._SPACE1, self._SPACE2, self._SPACE3,
                        self._SPACE4, self._SPACE5, self._SPACE6, self._SPACE7,
                        self._SPACE8, self._SPACE9, self._SPACE10, self._SPACE11,
                        self._SPACE12, self._SPACE13, self._SPACE14, self._SPACE15]

        self._ROW0 = [self._SPACE0, self._SPACE1, self._SPACE2, self._SPACE3]
        self._ROW1 = [self._SPACE4, self._SPACE5, self._SPACE6, self._SPACE7]
        self._ROW2 = [self._SPACE8, self._SPACE9, self._SPACE10, self._SPACE11]
        self._ROW3 = [self._SPACE12, self._SPACE13, self._SPACE14, self._SPACE15]

        self._COLUMN0 = [self._SPACE0, self._SPACE4, self._SPACE8, self._SPACE12]
        self._COLUMN1 = [self._SPACE1, self._SPACE5, self._SPACE9, self._SPACE13]
        self._COLUMN2 = [self._SPACE2, self._SPACE6, self._SPACE10, self._SPACE14]
        self._COLUMN3 = [self._SPACE3, self._SPACE7, self._SPACE11, self._SPACE15]

    def get_space(self, space_number):
        '''Dynamically return the number of the space'''

        return self._SPACES[space_number]

    def get_row(self, row_number):
        '''Dynamically return the number of the row'''

        return self._SPACES[row_number]

    def get_column(self, column_number):
        '''Dynamically return the number of the column'''

        return self._SPACES[column_number]
