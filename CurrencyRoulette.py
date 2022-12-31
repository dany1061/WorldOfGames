from currency_converter import CurrencyConverter

def get_money_interval(difficulty,value_of_money):
    c = CurrencyConverter()
    print(int(c.convert(100, 'USD', 'ILS')))
    t = int(c.convert(100, 'USD', 'ILS'))
    interval = (t-5)+t*5
    return interval

    # print('This is thie currency rate from USD to ILS RIGHT NOW: '+c.get_rate('USD', 'ILS'))

def get_guess_from_user(difficulty):
    guess_from_user = int(input(f'Please enter your guess for money interval :'))
    return guess_from_user

def play(difficulty):
    value_of_money = int(input('Please enter total value for money: '))
    if (get_money_interval(difficulty,value_of_money) == get_guess_from_user(difficulty)):
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
