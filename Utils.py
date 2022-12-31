import os
from time import sleep

FIRST_TIME_GAME = True

BAD_RETURN_CODE = 'App-Failure - 222341'

SCORES_FILE_NAME = 'Scores.txt'

def Screen_cleaner ():
    # Printing Some Text
    print("Cleaning the screen in:")
    sleep(0.5)
    print("4...")
    sleep(1)
    print("3...")
    sleep(1)
    print("2...")
    sleep(1)
    print("1...")
    sleep(1)
    print("~!~!~!~!~ Clearing sreen now ~!~!~!~!~!~")
    sleep(0.5)
    # Clearing the Screen
    os.system('cls')



