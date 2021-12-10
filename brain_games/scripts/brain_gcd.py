#!/usr/bin/env python


import random
from brain_games.for_games import user_name, game_process


def main():
    name = user_name()
    print("Find the greatest common divisor of given numbers.")
    for x in range(3):
        num_1 = random.randint(0, 100)
        num_2 = random.randint(0, 100)
        issue = "{} {} ".format(num_1, num_2)
        if num_1 != num_2:
            while num_1 != num_2:
                if num_1 > num_2:
                    num_1 = num_1 - num_2
                else:
                    num_2 = num_2 - num_1
        gcd = num_1
        game_results = game_process(issue, gcd, name)
        if game_results[0] is False:
            break
    if game_results[0] is True:
        print(game_results[1])


if __name__ == '__main__':
    main()
