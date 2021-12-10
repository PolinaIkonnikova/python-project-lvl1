#!/usr/bin/env python


import random
from brain_games.for_games import user_name, game_process


def main():
    name = user_name()
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    for x in range(3):
        new_number = random.randint(0, 100)
        result = 'yes' if new_number % 2 == 0 else 'no'
        game_results = game_process(str(new_number), result, name)
        if game_results[0] is False:
            break
    if game_results[0] is True:
        print(game_results[1])


if __name__ == '__main__':
    main()
