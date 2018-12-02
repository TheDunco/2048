'''
Unit tests for country guess

Created Summer, 2015

@author: kvlinden
'''
import unittest
from game import Game


class Test(unittest.TestCase):


    def test_constructor(self):
        try:
            Game('blob.txt')
            self.fail('Should raise a file not found exception...')
        except FileNotFoundError:
            pass

        try:
            Game('empty.txt')
            self.fail('Should raise a value exception...')
        except ValueError:
            pass

    def test_answer(self):
        try:
            game = Game('countries.txt')
            game._set_question(0)
            assert game.get_answer() == 'Algeria'
            assert game.check_answer('algeria')
            assert game.get_answer() != 'blob'
            assert not game.check_answer('')
        except:
            self.fail('Should not raise any exceptions on a good file.')

    def test_hints(self):
        try:
            game = Game('countries.txt')
            game._set_question(0)                       # Algeria
            assert game.get_hint().find('Africa') >= 0  # The country is in Africa.
            assert game.get_hint().endswith('A.')       # ... starts with an A.
            assert game.get_hint().find('7') >= 0       # ... has 7 letters.
            assert game.get_hint().endswith('a.')       # ... ends with an a.
            assert game.get_hint() == 'no more hints...'
            assert game.get_hint() == 'no more hints...'
        except:
            self.fail('Should not raise any exceptions on hints.')
            

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()