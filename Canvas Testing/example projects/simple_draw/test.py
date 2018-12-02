'''
Unit tests for the SimpleDraw figure types...
These are pretty rudimentary; more tests would be required.

Created Summer, 2015

@author: kvlinden
'''
import unittest
from figure import *

class Test(unittest.TestCase):


    def test_figure(self):
        Figure((0, 0), 'black')

    def test_Line(self):
        l = Line((0, 0), (1, 1))
        assert abs(l.get_length() - math.sqrt(2)) < 1e-3
        
    def test_Rectangle(self):
        Rectangle((0, 0), (0, 0), color='black', filled=True)

    def test_exceptions(self):
        try:
            Figure((-1, 0), 'black')
            self.fail('Should raise an exception...')
        except ValueError:
            pass

        try:
            Line((0, 0), (-1, 0), 'black')
            self.fail('Should raise an exception...')
        except ValueError:
            pass

    def test_overlap(self):
        # It would be good to test this as well.
        pass
    
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()