'''
Unit tests for TicTacToe...

Created Summer, 2015

@author: kvlinden
'''
import unittest
from game import TicTacToe


class Test(unittest.TestCase):

    def setUp(self):
        self._game = TicTacToe()

    def test_constructor(self):
        print(self._game)
        assert self._game.__str__() == '  |   |  \n---------\n  |   |  \n---------\n  |   |  \n'

    def test_check_row(self):
        # Check winning "rows"...
        for row in [['O', 'O', 'O'], ['X', 'X', 'X']]:
            assert self._game._check_row(row)

        # Check loosing "rows"...
        for row in [[' ', ' ', ' '], ['X', 'O', 'X'], [' ', ' ', 'O']]:
            assert not self._game._check_row(row)
        
    def test_get_winner(self):
        mixed_row = [' ', 'O', 'X']
        # Check winning boards for X...
        for state in [[['X']*3]*3, 
                      [['X']*3, [' ']*3, mixed_row], 
                      [mixed_row, [' ']*3, ['X']*3],
                      [['X', ' ', ' '], ['X', 'O', ' '], ['X', 'O', 'O']],
                      [['O', 'O', 'X'], ['O', 'O', 'X'], [' ', ' ', 'X']],
                      [['X', ' ', ' '], [' ', 'X', ' '], [' ', ' ', 'X']],
                      [[' ', ' ', 'X'], [' ', 'X', ' '], ['X', ' ', ' ']]
                      ]:
            self._game._set_state(state)
            assert self._game.get_winner() == 'X'

        # Check a couple winning boards for O...
        for state in [[['O']*3]*3, 
                      [['O']*3, [' ']*3, mixed_row], 
                      [mixed_row, [' ']*3, ['O']*3],
                      ]:
            self._game._set_state(state)
            assert self._game.get_winner() == 'O'

        # Check non-winning boards...
        for state in [[[' '] * 3] * 3,
                      [['X', ' ', ' '], ['O', 'O', ' '], ['X', 'O', 'O']],
                      [['X', 'O', 'X'], ['O', ' ', 'O'], ['X', 'O', 'X']]
                      ]:
            self._game._set_state(state)
            assert self._game.get_winner() == None
    
    def test_make_move(self):
        # Try a sequence of valid moves.
        try:
            self._game.make_move(0, 0)
            assert self._game.get_cell(0, 0) == 'X'
            assert self._game.get_cell(1, 0) == ' '            
            assert self._game.get_cell(0, 1) == ' '            
            
            self._game.make_move(2, 2)
            assert self._game.get_cell(2, 2) == 'O'
            self._game.make_move(0, 2)
            assert self._game.get_cell(0, 2) == 'X'

            assert self._game.get_cell(1, 1) == ' '            
        except:
            self.fail('Valid moves shouldn\'t raise an exception.')
        
        # Try some invalid moves.
        try:
            self._game.make_move(0, 2)
            self.fail('Moves to filled squares should raise an exception.')
        except ValueError:
            pass
        except:
            self.fail('Moves to filled squares should raise a ValueError exception.')

        try:
            self._game.make_move(-1, 0)
            self.fail('Moves to bad coordinates should raise an exception.')
        except ValueError:
            pass
        except:
            self.fail('Moves to bad coordinates should raise a ValueError exception.')
        
    def test_is_cat_game(self):
        # Check cats...
        for state in [[['X', 'X', 'O'], ['O', 'O', 'X'], ['X', 'O', 'X']],
                      [['O', 'X', 'O'], ['X', 'O', 'O'], ['X', 'O', 'X']]
                      ]:
            self._game._set_state(state)
            assert self._game.is_cat_game()
        # Check non-cats...
        for state in [[[' ']*3]*3,
                      [['X', ' ', 'O'], ['O', 'O', 'X'], ['X', 'O', 'X']],
                      [[' ', 'X', 'O'], ['X', 'O', ' '], ['X', 'O', 'X']],
                      [['X', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'X']],
                      ]:
            self._game._set_state(state)
            assert not self._game.is_cat_game()


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
