'''
A command-line interface for the TicTacToe player...

Created Summer, 2015

@author: kvlinden
'''
from game import TicTacToe


print('Welcome to the TicTacToe game.')
game = TicTacToe()
print(game)
moves = 0
while True:
    try:
        x = input('Player {0} (Enter to quit)\n\tmove x: '.format(game.get_player()))
        if x == '':
            print('Good bye')
            break
        x = int(x)
        y = int(input('\tmove y: '))
        game.make_move(x, y)
        print(game)
        result = game.get_winner()
        if result != None:
            print('The winner is {0}.'.format(result))
            break
        moves += 1
        if moves >= 9:
            print('Cat game...')
            break
    except ValueError as e:
        print(e, 'Try again...')
