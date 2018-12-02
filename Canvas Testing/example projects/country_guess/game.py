'''
The model for the country guess game, using classes, lists and files

Created Summer, 2015

@author: kvlinden
'''
from random import randint


class Country:
    ''' 
    This class encapsulates a question/answer pair for the country guessing game.
    '''
    
    def __init__(self, country, continent):
        ''' Create a new country object with name and content '''
        self._country = country
        self._continent = continent
        
    def get_country(self):
        ''' Get the country name '''
        return self._country

    def get_continent(self):
        ''' Get the continent name '''
        return self._continent
    

class Game:
    
    def __init__(self, filename):
        ''' Create a new country guess game with countries read from filename '''
        self._questions = []
        with open(filename) as f:
            for line in f:
                fields = line.split(',')
                self._questions.append(Country(fields[0].strip(), fields[1].strip()))
        if len(self._questions) == 0:
            raise ValueError('Empty file error: {0}'.format(filename))
        self.reset()
        
    def reset(self):
        ''' Pick a new country and reset the hint counter '''
        self._question_index = randint(0, len(self._questions))
        self._hint_count = 0
        
    def _set_question(self, index):
        ''' This (hidden) function sets a non-random question.
            It is only for unit testing. 
        '''
        if index < 0 or len(self._questions) <= index:
            raise ValueError('Invalid question index {0}...'.format(index))
        self._question_index = index
        self._hint_count = 0
    
    def get_answer(self):
        ''' Get the answer for the currently selected country '''
        return self._questions[self._question_index].get_country()
    
    def get_hint(self):
        ''' Get the next hint for the currently selected country '''
        country = self._questions[self._question_index]
        self._hint_count += 1
        if self._hint_count == 1:
            return 'The country is in {0}.'.format(country.get_continent())
        elif self._hint_count == 2:
            return 'The name starts with {0}.'.format(country.get_country()[0])
        elif self._hint_count == 3:
            return 'The name has {0} letters.'.format(len(country.get_country()))
        elif self._hint_count == 4:
            return 'The name ends with {0}.'.format(country.get_country()[-1:])
        else:
            return 'no more hints...'
        
    def check_answer(self, answer):
        return answer.lower() == self._questions[self._question_index].get_country().lower()

if __name__ == '__main__':
    game = Game('countries.txt')
    print(game.get_answer())
    for i in range(5):
        print(game.get_hint())
    