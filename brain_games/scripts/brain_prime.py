#!/usr/bin/env python


from brain_games.games.for_games import user_name, game_process
from brain_games.games.prime import prime


def main():
    name = user_name()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    game_process(name, prime)


if __name__ == '__main__':
    main()
