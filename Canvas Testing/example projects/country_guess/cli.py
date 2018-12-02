'''
Command-line driver for the country guess game

Created Summer, 2015

@author: kvlinden
'''

from game import Game, Country

print('Welcome to the country guess game.')
game = Game('countries.txt')

while True:
    print(game.get_hint())
    guess = input('guess (G to give up; Q to quit): ')
    if guess.lower() == 'q':
        break
    elif guess.lower() == 'g':
        print('The answer was {0}. Try a new country.'.format(game.get_answer()))
        game.reset()
    elif game.check_answer(guess):
        print('Good! Try a new country.')
        game.reset()
    else:
        print('Try again.')

print('\nGood bye...')
       