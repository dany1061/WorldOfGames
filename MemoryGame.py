import os
import random
import sys
import time

def generate_sequence(difficulty):
    randomized_list = []
    for i in range(difficulty):
        randomized_list.append(random.randint(1, 101))
    return randomized_list

def get_list_from_user(difficulty):
    guess_list_from_user = []
    for i in range(difficulty):
        guess_list_from_user.append(input('Please append what you think you saw to a list: '))
    print(str(guess_list_from_user) + 'This is the guess list from user')
    return guess_list_from_user


def is_list_equal(difficulty, guess_list_from_user, randomized_list):
    guess_list_from_user.sort()
    randomized_list.sort()
    for i in range(difficulty):
        if str(guess_list_from_user[i]) != str(randomized_list[i]):
            print('entered loop and then entered if')
            return False
    return True

def play(difficulty):
    randomized_list = generate_sequence(difficulty)
    print('Prepare to memorize numbers...')
    time.sleep(1)
    print('In 4...')
    time.sleep(1)
    print('In 3...')
    time.sleep(1)
    print('In 2...')
    time.sleep(1)
    print('In 1...')
    time.sleep(1)
    print(randomized_list, end="")
    time.sleep(0.7)
    print("\r", end="")
    print('Time is over, Were you able to memorize it all?')
    time.sleep(0.7)
    guess_list_from_user = get_list_from_user(difficulty)
    if is_list_equal(difficulty, guess_list_from_user, randomized_list) is True:
        replay = str(input('You WON!\nwant to play again? Enter Y for another round...\n'))
        if replay == 'Y' or replay == 'y':
            play(difficulty)
        else:
            exit('finished game')
    else:
        replay = str(input('You lost.\nWant to play again? Enter Y for another round...\n'))
        if replay == 'Y' or replay == 'y':
            play(difficulty)
        else:
            exit('finished game')

# play(4)