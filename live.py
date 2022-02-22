import MemoryGame
import GuessGame
import CurrencyRouletteGame


def welcome(name):
    print(f"Hello {name} and welcome to the World of Games. Here you can find many cool games to play")

def load_game():
    print("Please choose a game to play: \n 1 Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back \n 2 Guess game - guess a number and see if you chose like a computer \n 3 Currency Roulette - try and guess the value of a random amount of USD in ILS")
    game_number = int(input("please select a game:"))
    if game_number > 0 and game_number < 4:
        game_difficulty = int(input("Please choose a difficalty from 1 to 5:"))
        if game_difficulty > 0 and game_difficulty <6:
            print("Geat Job!")
            if game_number == 1:
                MemoryGame.play(game_difficulty)
            elif game_number == 2:
                GuessGame.play(game_difficulty)
            else:
                CurrencyRouletteGame.play(game_difficulty)
        else:
            print("difficulty number not in range")
    else:
        print("game number not in range")
