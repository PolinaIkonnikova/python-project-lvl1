#!/usr/bin/env python


import random
from brain_games.for_games import user_name, game_process


def main():
    name = user_name()
    operation_list = ['+', '-', '*']
    print('What is the result of the expression?')
    for x in range(3):
        operation = random.choice(operation_list)
        num_1 = random.randint(0, 100)
        num_2 = random.randint(0, 100)
        if operation == '+':
            result = num_1 + num_2
        elif operation == '-':
            result = num_1 - num_2
        else:
            result = num_1 * num_2
        issue = ('{} {} {} = '.format(num_1, operation, num_2))
        game_results = game_process(issue, result, name)
        if game_results[0] is False:
            break
    if game_results[0] is True:
        print(game_results[1])


if __name__ == '__main__':
    main()
