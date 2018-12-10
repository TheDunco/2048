'''Constants class for all of the board space coordinates for 2048 game
CS108 Final Project
Created Fall 2018
@author: Duncan Van Keulen
'''


class Coords:
    def __init__(self):

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

    def get_space(self, space_number):
        '''Dynamically return the specified space dictionary'''
        return self._SPACES[space_number]

