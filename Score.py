import os.path
from Utils import SCORES_FILE_NAME as SCORES_FILE_NAME

def calc_Winning_Points (difficulty):
    POINTS_OF_WINNING = difficulty * 3 + 5
    return POINTS_OF_WINNING

def add_score (difficulty):
    score = int(calc_Winning_Points(difficulty))
    if (os.path.exists(SCORES_FILE_NAME)) == False:
        print('Score file doesn\'t exist, Creating it now')
        f = open(f'{SCORES_FILE_NAME}', 'w')
        score= score + int(f.read())
        f.write(f"{score}\n")
        f.close()
    else:
        f = open(f'{SCORES_FILE_NAME}', 'w')
        score = score + int(f.read())
        f.write(f"{score}\n")
        f.close()
