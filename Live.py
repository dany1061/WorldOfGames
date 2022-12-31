import CurrencyRoulette
import GuessGame
import MemoryGame

# import CurrencyRoulette


def welcome(x):
    print(f'Hello {x} and welcome to the World of Games (WoG). \nHere you can find many cool games to play')

def load_game():
    print('''Please choose a game to Play:
    1.   Memory Game - a sequence of numbers will appear for 1 second. You will then have to recall the numbers you briefly saw
    2.   Guess Game - guess a number and see if you chose the same as the computer
    3.   Currency Roulette - try and guess the value of a random amount of USD in ILS''')

    while True:
        try:
            gameNum = int(input('Please enter the number for the game you chose: '))
        except ValueError:
            print("Invalid input entered.")
            continue
        else:
            if 0 < int(gameNum) < 4:
                break
            else:
                print('The number you entered should be between 1 to 3')
                continue
    while True:
        try:
            difficulty = int(input('Please enter the difficulty for your game of choice: '))
        except ValueError:
            print("Invalid input entered.")
            continue
        else:
            if 0 < int(difficulty) < 6:
                break
            else:
                print('The number you entered should be between 1 to 5')
                continue

    #   This section will prompt the user to chosen game with chosen difficulty
    if gameNum == 1:
        MemoryGame.play(difficulty)
    elif gameNum == 2:
        GuessGame.play(difficulty)
    elif gameNum == 3:
        CurrencyRoulette.play(difficulty)
