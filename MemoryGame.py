import random
import time


def generate_sequence(difficulty):
    randomlist = []
    for i in range(0, difficulty):
        n = random.randint(1, 101)
        randomlist.append(n)
    return(randomlist)


def get_list_from_user(difficulty):
    userlist = []
    for i in range(0, difficulty):
        n = int(input(f"Please enter the {i+1} number: (only numbers between 1 to 101) "))
        userlist.append(n)
    return userlist


def is_list_equal(generate_sequence,get_list_from_user):
    return generate_sequence == get_list_from_user


def play(difficulty):
    gen_seq = generate_sequence(difficulty)
    print(gen_seq)
    time.sleep(0.7)
    user_list = get_list_from_user(difficulty)
    return is_list_equal(gen_seq,user_list)

