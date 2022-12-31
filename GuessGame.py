import random
# from Live import load_game

def generate_number(difficulty):
    secret_number = random.randrange(1, difficulty)
    return secret_number

def get_guess_from_user(difficulty):
    guess_from_user = int(input(f'Please enter a number between 1  and {difficulty} :'))
    if (difficulty < guess_from_user) or (guess_from_user == 0):
        return print('run again')# get_guess_from_user(difficulty)
    else:
        return guess_from_user

def compare_results(secret_number, guess_from_user):
    if secret_number == guess_from_user:
        return True
    else:
        return False

def play(difficulty):
    secret_number = generate_number(difficulty)
    guess_from_user = get_guess_from_user(difficulty)
    if compare_results(secret_number, guess_from_user) == True:
        replay = str(input('You WON!\nwant to play again? Enter Y for another round...\n'))
        if replay == 'Y' or replay == 'y':
            play(difficulty)
        else:
            print('Finished playing')
    else:
        replay = str(input('You lost.\nWant to play again? Enter Y for another round...\n'))
        if replay == 'Y' or replay == 'y':
            play(difficulty)
        else:
            exit('finished game')

# def run_game(difficulty):
#     secret_number = generate_number(difficulty)
#     guess_from_user = get_guess_from_user(difficulty)
#     result = compare_results(secret_number, guess_from_user)
#     play(difficulty)
