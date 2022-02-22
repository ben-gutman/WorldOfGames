import random


def generate_number(difficulty):
    secret_number = random.randint(1, int(difficulty))
    return secret_number


def get_guess_from_user(difficulty):
    user_guess = input(f"Please enter a number between 1 and {difficulty}: ")
    return user_guess


def compare_results(secret_number, user_guess):
    return int(secret_number) == int(user_guess)


def play(difficulty):
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    result = compare_results(secret_number, user_guess)
    return result
