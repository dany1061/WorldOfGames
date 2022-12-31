import os.path
from Utils import SCORES_FILE_NAME as SCORES_FILE_NAME


def calc_Winning_Points (difficulty):
    POINTS_OF_WINNING = difficulty * 3 + 5
    return POINTS_OF_WINNING

def add_score (difficulty):
    score = int(calc_Winning_Points(difficulty))
    print(f'this is the score BEGIN: {score}')
    if (os.path.exists(SCORES_FILE_NAME)) == False:
        print('Score file doesn\'t exist, Creating it now')
        f = open (f'{SCORES_FILE_NAME}', 'w')
        print(f'this is the score DIDNT EXIST BEFORE: {score}')
        f.write(f"{str(score)}\n")
        f.close()
    else:
        f = open(f'{SCORES_FILE_NAME}', 'r')
        score = score + int(f.read())
        f.close()
        f = open(f'{SCORES_FILE_NAME}', 'w')
        f.write(f"{str(score)}\n")
        print(f'this is the score APPENDED: {score}')
        f.close()

