''' 
A bare bones Tic-Tac-Toe Application, based on Serita's bare-bones app... 
This supports two human players who must take turns.

Created Summer, 2015

@author: Serita Nelesen
@author: kvlinden
'''
    
class TicTacToe:
    '''
    tokens: -1 - empty; 0 - player 0; 1 - player 1
    invariant: 
        _state: 3x3 array of characters
        cell values in _tokens + (' ',)
        len(_tokens) == 2 
        _turn in range(2)
    '''

    def __init__(self):
        ''' Creates an empty board, user tokens and sets the first player '''
        self._state = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self._tokens = ('X', 'O')
        self._empty_token = ' '
        self._turn = 0
        
    def __str__(self):
        ''' Returns the board state '''
        result = ''
        for i in range(3):
            result += ' | '.join(self._state[i]) + '\n'
            if i < 2:
                result += '---------\n'
        return result 
    
    def get_player(self):
        return self._tokens[self._turn]
    
    def get_board(self):
        return self._state
    
    def get_cell(self, x, y):
        ''' Get the value of a given cell '''
        if not self._coordinates_on_board(x, y):
            raise ValueError('Invalid coordinates: ({0},{1})'.format(x, y))        
        return self._state[x][y]
    
    def _coordinates_on_board(self, x, y):
        ''' Check if the coordinates are on the legal board '''
        return x in range(3) and y in range(3)
    
    def _set_state(self, state):
        ''' Set the given state
            This is used only for testing.'''
        self._state = state
    
    def get_winner(self):
        ''' Check if anyone has won the game '''
        # Check the horizontal and vertical rows...
        for x in range(3):
            if self._check_row([self._state[x][0], self._state[x][1], self._state[x][2]]):
                return self._state[x][0]
            if self._check_row([self._state[0][x], self._state[1][x], self._state[2][x]]):
                return self._state[0][x]
        # Check the two diagonals
        if self._check_row([self._state[0][0], self._state[1][1], self._state[2][2]]):
            return self._state[0][0]
        if self._check_row([self._state[0][2], self._state[1][1], self._state[2][0]]):
            return self._state[0][2]
        return None
                
    @staticmethod
    def _check_row(row):
        ''' Check if a given (three-element) row is filled with (non-empty) tokens from one player '''
        return (len(set(row)) == 1) and (row[0] != ' ')
        
    def make_move(self, x, y):
        ''' place current token in row x, column y '''
        if not self._coordinates_on_board(x, y):
            raise ValueError('Invalid coordinates: ({0},{1})'.format(x, y))        
        if self._state[x][y] !=  self._empty_token:
            raise ValueError('Space already filled: ({0},{1})'.format(x, y))
        self._state[x][y] = self._tokens[self._turn]
        self._turn = (self._turn + 1) % 2
        return self._state[x][y]
    
    def is_cat_game(self):
        ''' Check to see if we have a cat game, i.e., a full board with no winner '''
        for row in self._state:
            for cell in row:
                if cell == ' ':
                    return False
        return not self.get_winner()  

    
if __name__ == '__main__':
    game = TicTacToe()
    print(game)
    print(game.get_cell(0, 0))
    print(game.make_move(0, 0))
    print(game)
    
