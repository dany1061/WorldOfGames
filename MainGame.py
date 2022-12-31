from Live import load_game, welcome
import os
from Utils import SCORES_FILE_NAME as SCORES_FILE_NAME

FIRST_TIME_GAME = True

def has_numbers(inputString):   #   returns True if name paramter input had numbers entered to it
    return any(char.isdigit() for char in inputString)

def player_name():
    name = input('Please enter a name without number: ')
    if has_numbers(name) is True:
        print(f'You entered invalid name: {name}')
        return player_name()
    return name

welcome(player_name())
os.remove(SCORES_FILE_NAME)
load_game()


print('done')