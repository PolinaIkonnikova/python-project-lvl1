#!/usr/bin/env python


from brain_games.games.for_games import user_name, game_process
from brain_games.games.calc import calc


def main():
    name = user_name()
    print('What is the result of the expression?')
    game_process(name, calc)


if __name__ == '__main__':
    main()
