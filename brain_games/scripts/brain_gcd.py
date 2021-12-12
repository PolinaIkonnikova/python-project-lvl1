#!/usr/bin/env python


from brain_games.game_logic import user_name, game_process
from brain_games.games.gcd import gcd


def main():
    name = user_name()
    print("Find the greatest common divisor of given numbers.")
    game_process(name, gcd)


if __name__ == '__main__':
    main()
