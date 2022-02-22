import random
from currency_converter import CurrencyConverter

def get_money_interval(d,t):
    return (t - (5 - d), t + (5 - d))


def get_guess_from_user():
    return int(input("Please enter your guess: "))

def play(d):
    c = CurrencyConverter()
    currency_rate = (c.convert(1, 'USD', 'ILS'))
    random_number = random.randint(1, 100)
    t = random_number * int(currency_rate)
    interval = get_money_interval(d,t)
    user_guess = get_guess_from_user()
    return interval[0] <= user_guess <= interval[1]

